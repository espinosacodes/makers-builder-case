"""Fit test for informe-docs.md.

Converts the markdown to HTML with a minimal converter, styles it to imitate
Google Docs (Arial 11, line spacing 1.15, US Letter, 1 inch margins), prints it
to PDF with headless Chrome and reports on which page the body ends.

Google Docs applies its line spacing on top of the font's own line height
(about 1.15 em for Arial), so "1.15" in Docs is close to 1.32 em in CSS.
Run with --strict to test that closer approximation, with Docs' default
5pt table cell padding and equal column widths; the strict run writes fit-test-strict.pdf.
"""
import html
import re
import subprocess
import sys
from pathlib import Path

from pypdf import PdfReader

HERE = Path(__file__).resolve().parent
MD = HERE / "informe-docs.md"
HTML_OUT = HERE / "fit-test.html"
PDF_OUT = HERE / "fit-test.pdf"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
ANNEX_MARKER = "ANEXOS"

STRICT = "--strict" in sys.argv
LINE_HEIGHT = "1.32" if STRICT else "1.15"
CELL_PADDING = "5pt 5pt" if STRICT else "2pt 4pt"
# Docs gives pasted tables equal column widths.
TABLE_LAYOUT = "fixed" if STRICT else "auto"
if STRICT:
    PDF_OUT = HERE / "fit-test-strict.pdf"

CSS = """
@page { size: Letter; margin: 1in; }
html, body { margin: 0; padding: 0; background: #fff; color: #000; }
body { font-family: Arial, Helvetica, sans-serif; font-size: 11pt; line-height: LH; }
p, li { margin: 0 0 6pt 0; }
ul, ol { margin: 0 0 6pt 0; padding-left: 0.35in; }
h1 { font-size: 16pt; font-weight: bold; margin: 0 0 6pt 0; }
h2 { font-size: 14pt; font-weight: bold; margin: 12pt 0 6pt 0; }
h3 { font-size: 12pt; font-weight: bold; margin: 10pt 0 6pt 0; }
table { table-layout: TL; border-collapse: collapse; width: 100%; margin: 0 0 6pt 0; font-size: 9pt; line-height: LH; }
th, td { border: 0.5pt solid #999; padding: CP; vertical-align: top; text-align: left; }
th { font-weight: bold; }
thead { display: table-row-group; }
tr, td { break-inside: auto; }
.annex { page-break-before: always; }
#body-end { height: 0; }
""".replace("LH", LINE_HEIGHT).replace("CP", CELL_PADDING).replace("TL", TABLE_LAYOUT)


def inline(text: str) -> str:
    """Escape and apply bold and italics."""
    text = html.escape(text, quote=False)
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"(?<![*\w])\*(?!\s)(.+?)(?<!\s)\*(?![*\w])", r"<i>\1</i>", text)
    return text


def split_row(line: str) -> list:
    return [c.strip() for c in line.strip().strip("|").split("|")]


def md_to_html(md: str) -> str:
    lines = md.splitlines()
    out = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
            continue
        if line.strip() == ANNEX_MARKER:
            out.append('<div id="body-end"></div>')
            out.append(f'<p class="annex"><b>{ANNEX_MARKER}</b></p>')
            i += 1
            continue
        m = re.match(r"^(#{1,3})\s+(.*)$", line)
        if m:
            level = len(m.group(1))
            out.append(f"<h{level}>{inline(m.group(2))}</h{level}>")
            i += 1
            continue
        if line.lstrip().startswith("|") and i + 1 < len(lines) and re.match(r"^\s*\|[\s:|-]+\|\s*$", lines[i + 1]):
            header = split_row(line)
            i += 2
            rows = []
            while i < len(lines) and lines[i].lstrip().startswith("|"):
                rows.append(split_row(lines[i]))
                i += 1
            parts = ["<table><thead><tr>"]
            parts += [f"<th>{inline(c)}</th>" for c in header]
            parts.append("</tr></thead><tbody>")
            for r in rows:
                parts.append("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>")
            parts.append("</tbody></table>")
            out.append("".join(parts))
            continue
        if re.match(r"^\s*[-*]\s+", line):
            items = []
            while i < len(lines) and re.match(r"^\s*[-*]\s+", lines[i]):
                items.append(re.sub(r"^\s*[-*]\s+", "", lines[i]))
                i += 1
            out.append("<ul>" + "".join(f"<li>{inline(t)}</li>" for t in items) + "</ul>")
            continue
        if re.match(r"^\s*\d+\.\s+", line):
            items = []
            while i < len(lines) and re.match(r"^\s*\d+\.\s+", lines[i]):
                items.append(re.sub(r"^\s*\d+\.\s+", "", lines[i]))
                i += 1
            out.append("<ol>" + "".join(f"<li>{inline(t)}</li>" for t in items) + "</ol>")
            continue
        para = [line.strip()]
        i += 1
        while i < len(lines) and lines[i].strip() and not re.match(r"^(#|\||\s*[-*]\s|\s*\d+\.\s)", lines[i]) and lines[i].strip() != ANNEX_MARKER:
            para.append(lines[i].strip())
            i += 1
        out.append(f"<p>{inline(' '.join(para))}</p>")
    body = "\n".join(out)
    return f'<!doctype html><html lang="es"><head><meta charset="utf-8"><style>{CSS}</style></head><body>{body}</body></html>'


def body_word_count(md: str) -> int:
    body = md.split("\n" + ANNEX_MARKER + "\n")[0]
    body = re.sub(r"^\|[\s:|-]+\|\s*$", "", body, flags=re.M)
    body = re.sub(r"[|#*]", " ", body)
    return len(body.split())


def find_body_end(reader: PdfReader) -> tuple:
    """Return (page number where the body ends, fraction of that page used)."""
    annex_page = None
    for idx, page in enumerate(reader.pages):
        if ANNEX_MARKER in (page.extract_text() or ""):
            annex_page = idx
            break
    last = annex_page - 1 if annex_page is not None else len(reader.pages) - 1
    # Chrome can leave an empty page before the forced annex break; Docs does not.
    while last > 0 and not (reader.pages[last].extract_text() or "").strip():
        last -= 1
    page = reader.pages[last]
    height = float(page.mediabox.height)
    ys = []

    def visitor(text, cm, tm, font_dict, font_size):
        if text.strip():
            ys.append(tm[5] * cm[3] + cm[5])

    page.extract_text(visitor_text=visitor)
    lowest = min(ys) if ys else height
    top_margin = bottom_margin = 72.0
    usable = height - top_margin - bottom_margin
    used = (height - top_margin - lowest) / usable
    return last + 1, max(0.0, min(1.0, used))


def main() -> int:
    md = MD.read_text(encoding="utf-8")
    bad = [ch for ch in ("—", "–") if ch in md]
    if bad:
        print("ERROR: em or en dash found")
        return 1
    HTML_OUT.write_text(md_to_html(md), encoding="utf-8")
    subprocess.run(
        [CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
         f"--print-to-pdf={PDF_OUT}", HTML_OUT.as_uri()],
        check=True, capture_output=True,
    )
    reader = PdfReader(str(PDF_OUT))
    end_page, used = find_body_end(reader)
    words = body_word_count(md)
    print(f"body words: {words}")
    print(f"total pages: {len(reader.pages)}")
    print(f"mode: {'strict (Docs line height)' if STRICT else 'nominal'}")
    print(f"body ends on page {end_page}, using {used:.0%} of it")
    if STRICT:
        # Pessimistic model: the body only has to end within page 5.
        ok = end_page <= 5
        print("PASS" if ok else "FAIL: body must end by page 5")
    else:
        ok = end_page < 5 or (end_page == 5 and used <= 0.75)
        print("PASS" if ok else "FAIL: body must end by page 5 with a quarter page of slack")
    HTML_OUT.unlink(missing_ok=True)
    return 0 if ok else 2


if __name__ == "__main__":
    sys.exit(main())
