"""Put the Docs copy on the macOS clipboard as rich HTML (Arial, black, no links) plus plain text.

Pasting into Google Docs keeps headings, bold and tables without any blue text.
Usage: python copy_to_clipboard.py
"""
import re
import subprocess
import tempfile
from pathlib import Path

import fit

HERE = Path(__file__).resolve().parent
BASE = "font-family:Arial,sans-serif;color:#000000;"
STYLES = {
    "h1": BASE + "font-size:16pt;font-weight:bold;margin:0 0 6pt 0;",
    "h2": BASE + "font-size:14pt;font-weight:bold;margin:12pt 0 6pt 0;",
    "h3": BASE + "font-size:12pt;font-weight:bold;margin:10pt 0 6pt 0;",
    "p": BASE + "font-size:11pt;line-height:1.15;margin:0 0 6pt 0;",
    "li": BASE + "font-size:11pt;line-height:1.15;",
    "table": BASE + "border-collapse:collapse;width:100%;font-size:9pt;",
    "th": BASE + "font-size:9pt;font-weight:bold;border:1px solid #999999;padding:2pt 4pt;vertical-align:top;text-align:left;",
    "td": BASE + "font-size:9pt;border:1px solid #999999;padding:2pt 4pt;vertical-align:top;text-align:left;",
}


def rich_html() -> str:
    doc = fit.md_to_html(fit.MD.read_text(encoding="utf-8"))
    body = re.search(r"<body>(.*)</body>", doc, flags=re.S).group(1)
    body = body.replace('<div id="body-end"></div>', "")
    body = body.replace('<p class="annex">', "<p>")
    for tag, style in STYLES.items():
        body = re.sub(rf"<{tag}>", f'<{tag} style="{style}">', body)
    return f'<meta charset="utf-8"><div style="{BASE}">{body}</div>'


def main() -> None:
    html_text = rich_html()
    plain = (HERE / "informe-docs.txt").read_text(encoding="utf-8")
    with tempfile.TemporaryDirectory() as tmp:
        h, t = Path(tmp) / "c.html", Path(tmp) / "c.txt"
        h.write_text(html_text, encoding="utf-8")
        t.write_text(plain, encoding="utf-8")
        jxa = f"""
ObjC.import('AppKit');
function read(p) {{ return $.NSString.stringWithContentsOfFileEncodingError(p, $.NSUTF8StringEncoding, null); }}
var pb = $.NSPasteboard.generalPasteboard;
pb.clearContents;
pb.setStringForType(read('{h}'), 'public.html');
pb.setStringForType(read('{t}'), 'public.utf8-plain-text');
'ok';
"""
        out = subprocess.run(["osascript", "-l", "JavaScript", "-e", jxa], capture_output=True, text=True)
        print(out.stdout.strip() or out.stderr.strip())
    print(f"HTML chars: {len(html_text)}, plain chars: {len(plain)}")


if __name__ == "__main__":
    main()
