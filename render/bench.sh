#!/bin/sh
# usage: sh bench.sh [OUTDIR]     RTF of the real voices (each config is one 4800 MiB reservation), then Whisper CER per config
set -e
OUT=${1:-/tmp/overhear-bench}
HERE=$(cd "$(dirname "$0")" && pwd)
GPURUN="$HERE/gpurun"
$GPURUN 4800 ${OVERHEAR_HOME:-$HOME/overhear}/venv-qwen/bin/python -I "$HERE/bench.py" "$OUT"
. "$HERE/setup/cudaenv.sh"
$GPURUN 2500 ${OVERHEAR_HOME:-$HOME/overhear}/venv-asr/bin/python -I "$HERE/bench_cer.py" "$OUT"
