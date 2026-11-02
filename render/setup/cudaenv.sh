# Source before running faster-whisper in venv-asr: puts the pip-installed cuBLAS/cuDNN on the loader path.
_v="${OVERHEAR_VENV_ASR:-${OVERHEAR_HOME:-$HOME/overhear}/venv-asr}"
_sp="$("$_v/bin/python" -c 'import site; print(site.getsitepackages()[0])')"
export LD_LIBRARY_PATH="$_sp/nvidia/cublas/lib:$_sp/nvidia/cudnn/lib${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"
