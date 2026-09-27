"""Generate the WhatsApp voice notes for the interview with mom from docs/05-entrevista-mama.md.

Each "## Audio N" section of the markdown becomes one Ogg Opus file in audio/, and the
"## Audio único" section (all three joined) becomes audio/mama-completo.opus.
The OpenAI key is read from OPENAI_API_KEY or, failing that, from KEY_ENV_FILE,
so the key never gets copied into this project.
"""
import json
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPT_FILE = ROOT / "docs" / "05-entrevista-mama.md"
OUT_DIR = ROOT / "audio"
KEY_ENV_FILE = Path(os.environ.get("OPENAI_KEY_ENV_FILE", Path.home() / "Documents" / "curia" / ".env"))

VOICE = os.environ.get("TTS_VOICE", "ash")
MODEL = "gpt-4o-mini-tts"
FALLBACK_MODEL = "tts-1-hd"
INSTRUCTIONS = (
    "Habla en español colombiano, como un joven de Cali que le habla con cariño a su mamá. "
    "Tono cálido, cercano y natural, nada de locutor. Ritmo pausado, con una pausa breve "
    "después de cada pregunta para que se entienda bien."
)


def load_key():
    key = os.environ.get("OPENAI_API_KEY")
    if key:
        return key
    for line in KEY_ENV_FILE.read_text().splitlines():
        m = re.match(r"\s*(?:export\s+)?OPENAI_API_KEY\s*=\s*['\"]?([^'\"\s]+)", line)
        if m:
            key = m.group(1)
    if not key:
        sys.exit(f"No OPENAI_API_KEY found in environment or {KEY_ENV_FILE}")
    return key


def load_sections():
    text = SCRIPT_FILE.read_text()
    sections = re.findall(r"^## (Audio \d+)[^\n]*\n(.*?)(?=^## |\Z)", text, flags=re.M | re.S)
    result = [(name.split()[-1], body.strip()) for name, body in sections]
    single = re.search(r"^## Audio único[^\n]*\n\n[^\n]*\n\n(.*?)(?=^## |\Z)", text, flags=re.M | re.S)
    if single:
        result.append(("completo", single.group(1).strip()))
    return result


def synthesize(key, text, model):
    payload = {"model": model, "voice": VOICE, "input": text, "response_format": "opus"}
    if model == MODEL:
        payload["instructions"] = INSTRUCTIONS
    req = urllib.request.Request(
        "https://api.openai.com/v1/audio/speech",
        data=json.dumps(payload).encode(),
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=180) as resp:
        return resp.read()


def main():
    key = load_key()
    OUT_DIR.mkdir(exist_ok=True)
    only = sys.argv[1:]
    for name, body in load_sections():
        if only and name not in only:
            continue
        out = OUT_DIR / f"mama-{name}.opus"
        try:
            audio = synthesize(key, body, MODEL)
        except urllib.error.HTTPError as err:
            if err.code == 401:
                sys.exit(f"The key in {KEY_ENV_FILE} was rejected (401)")
            print(f"{name}: {MODEL} failed ({err.code}: {err.read()[:200]!r}), retrying with {FALLBACK_MODEL}")
            audio = synthesize(key, body, FALLBACK_MODEL)
        out.write_bytes(audio)
        print(f"{name}: {len(body.split())} words -> {out.relative_to(ROOT)} ({len(audio) // 1024} KB)")


if __name__ == "__main__":
    main()
