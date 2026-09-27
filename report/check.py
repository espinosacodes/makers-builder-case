#!/usr/bin/env python3
"""Pre-submission checks for the Makers Builder Case PDF.

Checks: page count, page where ANEXOS starts (main body <= 5 pages, ANEXOS at the
top of its page), forbidden dash characters and spaced-hyphen dashes in both the
PDF text and informe.html, exact file name, denylisted personal names, and words
per page. Exits non-zero if any check fails.
"""

import html
import re
import sys
from pathlib import Path

from pypdf import PdfReader

HERE = Path(__file__).resolve().parent
EXPECTED_NAME = "MAKERS_SANTIAGO_ESPINOSA_CALI.pdf"
PDF_PATH = HERE / EXPECTED_NAME
HTML_PATH = HERE / "informe.html"
MAX_BODY_PAGES = 5
ANNEX_MARKER = "ANEXOS"
# How many non-empty lines at the top of a page may precede ANEXOS (running header).
ANNEX_TOP_LINES = 3

NAME_DENYLIST = ["Gabriel", "Edwin", "Lorena", "Angie", "Brandon", "Randall", "Sandy", "Carla"]

# Dash characters that must never appear.
FORBIDDEN_CHARS = {
    "–": "EN DASH (U+2013)",
    "—": "EM DASH (U+2014)",
    "‒": "FIGURE DASH (U+2012)",
    "―": "HORIZONTAL BAR (U+2015)",
}
# A hyphen with whitespace on both sides reads as a fake em dash.
SPACED_HYPHEN = re.compile(r"(?<=\S)[  ]+-[  ]+(?=\S)")

failures = []


def result(label, ok, detail=""):
    status = "PASS" if ok else "FAIL"
    if not ok:
        failures.append(label)
    print(f"[{status}] {label}" + (f": {detail}" if detail else ""))


def context(text, idx, width=40):
    start = max(0, idx - width)
    end = min(len(text), idx + width)
    return text[start:end].replace("\n", " ")


def html_visible_text(raw):
    """Strip tags, style, script and comments so CSS/JS do not trigger false positives."""
    raw = re.sub(r"<!--.*?-->", " ", raw, flags=re.S)
    raw = re.sub(r"<(style|script)\b.*?</\1>", " ", raw, flags=re.S | re.I)
    raw = re.sub(r"<[^>]+>", " ", raw)
    return html.unescape(raw)


def scan_dashes(label, text, raw_for_entities=None):
    hits = []
    for ch, name in FORBIDDEN_CHARS.items():
        for m in re.finditer(re.escape(ch), text):
            hits.append(f"{name} near '{context(text, m.start())}'")
    if raw_for_entities is not None:
        for m in re.finditer(r"&(mdash|ndash|#8211|#8212|#x2013|#x2014);", raw_for_entities, flags=re.I):
            hits.append(f"entity &{m.group(1)}; near '{context(raw_for_entities, m.start())}'")
    for m in SPACED_HYPHEN.finditer(text):
        hits.append(f"spaced hyphen near '{context(text, m.start())}'")
    shown = "; ".join(hits[:8]) + (f"; ... (+{len(hits) - 8} more)" if len(hits) > 8 else "")
    result(f"no dashes in {label}", not hits, shown if hits else "none found")


def scan_names(label, text):
    found = {}
    for name in NAME_DENYLIST:
        n = len(re.findall(rf"\b{name}\b", text, flags=re.I))
        if n:
            found[name] = n
    detail = ", ".join(f"{k} x{v}" for k, v in found.items()) if found else "none found"
    result(f"no denylisted names in {label}", not found, detail)


def main():
    print(f"PDF:  {PDF_PATH}")
    print(f"HTML: {HTML_PATH}\n")

    # File name
    pdfs = sorted(p.name for p in HERE.glob("*.pdf"))
    result("file name", PDF_PATH.exists(), f"found {pdfs}" if pdfs else "no PDF in report/")
    if not PDF_PATH.exists():
        return

    reader = PdfReader(str(PDF_PATH))
    pages = [(pg.extract_text() or "") for pg in reader.pages]
    total = len(pages)
    print(f"Total pages: {total}")

    # ANEXOS position
    annex_page = None
    annex_at_top = False
    for i, txt in enumerate(pages, start=1):
        if re.search(rf"\b{ANNEX_MARKER}\b", txt):
            annex_page = i
            lines = [ln.strip() for ln in txt.splitlines() if ln.strip()]
            annex_at_top = any(
                re.search(rf"\b{ANNEX_MARKER}\b", ln) for ln in lines[:ANNEX_TOP_LINES]
            )
            break
    print(f"ANEXOS first appears on page: {annex_page if annex_page else 'NOT FOUND'}")
    if annex_page is None:
        result(f"main body <= {MAX_BODY_PAGES} pages", total <= MAX_BODY_PAGES,
               f"no ANEXOS heading; body is all {total} pages")
    else:
        body = annex_page - 1
        result(f"main body <= {MAX_BODY_PAGES} pages", body <= MAX_BODY_PAGES and annex_at_top,
               f"body = {body} pages; ANEXOS at top of page {annex_page}: {annex_at_top}")

    # Dashes
    pdf_text = "\n".join(pages)
    scan_dashes("PDF text", pdf_text)
    if HTML_PATH.exists():
        raw = HTML_PATH.read_text(encoding="utf-8")
        html_text = html_visible_text(raw)
        # Raw file too: catches dashes inside attributes, titles and comments.
        scan_dashes("informe.html (visible text)", html_text, raw_for_entities=raw)
        raw_hits = [n for ch, n in FORBIDDEN_CHARS.items() if ch in raw]
        result("no dash chars anywhere in informe.html source", not raw_hits,
               ", ".join(raw_hits) if raw_hits else "none found")
        scan_names("informe.html", html_text)
    else:
        result("informe.html exists", False)

    scan_names("PDF text", pdf_text)

    # Words per page
    print("\nWords per page:")
    for i, txt in enumerate(pages, start=1):
        words = len(re.findall(r"\w+", txt))
        tag = "  <- ANEXOS" if i == annex_page else ""
        region = "body " if annex_page is None or i < annex_page else "annex"
        print(f"  p{i:>2} [{region}] {words:>5} words{tag}")
    body_pages = pages[: (annex_page - 1) if annex_page else total]
    body_words = sum(len(re.findall(r"\w+", t)) for t in body_pages)
    print(f"  main body total: {body_words} words")


if __name__ == "__main__":
    main()
    print()
    if failures:
        print(f"RESULT: FAIL ({len(failures)}): " + "; ".join(failures))
        sys.exit(1)
    print("RESULT: ALL PASS")
    sys.exit(0)
