#!/bin/sh
# usage: sh smoke.sh [OUTDIR]     Russian + French scene (English narrator in both) through the real pipeline, then Whisper CER.
set -e
OUT=${1:-/tmp/overhear-smoke}
HERE=$(cd "$(dirname "$0")" && pwd)
GPURUN="$HERE/gpurun"
rm -rf "$OUT"; mkdir -p "$OUT"
python3 -I "$HERE/smoke.py" "$OUT"
OVERHEAR_CASTING_DIR="$OUT/casting" python3 -I "$HERE/pipeline.py" --content "$OUT/content" --store "$OUT/store" --force --allow-no-notes
. "$HERE/setup/cudaenv.sh"
$GPURUN 2500 ${OVERHEAR_HOME:-$HOME/overhear}/venv-asr/bin/python -I "$HERE/asr_cer.py" --store "$OUT/store" --out "$OUT/cer.json" $(cat "$OUT/scenes.txt")
