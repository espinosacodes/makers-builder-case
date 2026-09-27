#!/usr/bin/env bash
# Render informe.html to the final PDF with headless Chrome.
set -euo pipefail

DIR="$(cd "$(dirname "$0")" && pwd)"
SRC="$DIR/informe.html"
OUT="$DIR/MAKERS_SANTIAGO_ESPINOSA_CALI.pdf"
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

if [[ ! -f "$SRC" ]]; then
  echo "missing $SRC" >&2
  exit 1
fi

rm -f "$OUT"

# Chrome prints noisy but harmless stderr (GPU, updater, dbus); discard it.
"$CHROME" \
  --headless=new \
  --disable-gpu \
  --no-pdf-header-footer \
  --no-first-run \
  --no-default-browser-check \
  --run-all-compositor-stages-before-draw \
  --virtual-time-budget=5000 \
  --print-to-pdf="$OUT" \
  "file://$SRC" 2>/dev/null >/dev/null || true

if [[ ! -s "$OUT" ]]; then
  echo "render failed: $OUT was not produced" >&2
  exit 1
fi

echo "wrote $OUT ($(wc -c < "$OUT" | tr -d ' ') bytes)"
