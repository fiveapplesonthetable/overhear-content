#!/usr/bin/env bash
# One-time machine setup for rendering (Ubuntu 22.04/24.04, NVIDIA driver with CUDA 12.4+ and 13 runtimes; tested shape: A100 40 GB).
# Creates $OVERHEAR_HOME/{venv-qwen,venv-f5,venv-asr}, downloads every model and the Russian Wiktionary dump, runs the self-check.
# usage: OVERHEAR_HOME=~/overhear HF_TOKEN=hf_... bash render/setup/setup.sh
set -euo pipefail
HERE=$(cd "$(dirname "$0")" && pwd)
H="${OVERHEAR_HOME:-$HOME/overhear}"
mkdir -p "$H"/{models,dict,render-store,gpu-slots/queue}
command -v ffmpeg >/dev/null && command -v lame >/dev/null || sudo apt-get install -y ffmpeg lame python3.12-venv sox
mkvenv() {   # name requirements [extra pip args]
  [ -x "$H/$1/bin/python" ] || python3.12 -m venv "$H/$1"
  "$H/$1/bin/pip" install -q --upgrade pip
  "$H/$1/bin/pip" install -q -r "$HERE/$2" "${@:3}"
}
mkvenv venv-qwen requirements-qwen.txt     # Qwen3-TTS (fr/es/de/it/pt/ja/zh/ko + narrator for those), MMS_FA alignment, assembly
mkvenv venv-f5   requirements-f5.txt       # ESpeech-TTS (ru), F5-TTS (en narrator), RUAccent
mkvenv venv-asr  requirements-asr.txt --extra-index-url https://download.pytorch.org/whl/cu124   # faster-whisper CER, Chatterbox (ar)
"$H/venv-qwen/bin/python" -I "$HERE/download_models.py" --home "$H"
"$H/venv-qwen/bin/python" -I "$HERE/selfcheck.py"
echo "setup done: export OVERHEAR_HOME=$H GPURUN_BUDGET_MIB=38500"
