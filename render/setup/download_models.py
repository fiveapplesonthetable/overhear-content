"""Fetch every model the renderer uses into the Hugging Face cache (and the two that need a fixed local path into OVERHEAR_HOME).
HF_TOKEN comes from the environment only. usage: venv-qwen/bin/python -I download_models.py --home ~/overhear"""
import argparse
import bz2
import os
import shutil
import subprocess
import urllib.request
from pathlib import Path

from huggingface_hub import snapshot_download

HF = [
    "Qwen/Qwen3-TTS-12Hz-1.7B-Base",          # scene + narrator TTS for every Qwen language
    "Qwen/Qwen3-TTS-12Hz-1.7B-VoiceDesign",   # making new synthetic voice refs (spec/voices.md)
    "Qwen/Qwen3-TTS-Tokenizer-12Hz",          # speech tokenizer (pulled by qwen-tts; fetched up front so runs never block)
    "ESpeech/ESpeech-TTS-1_RL-V2",            # Russian dialogue
    "SWivid/F5-TTS",                          # English narrator (F5TTS_v1_Base)
    "charactr/vocos-mel-24khz",               # F5 vocoder
    "mobiuslabsgmbh/faster-whisper-large-v3-turbo",   # CER checks (faster-whisper "large-v3-turbo")
    "zimuzostanley/qwen3-tts-ru-stress-lora", # Russian stress LoRA (narrator method B, form clips)
]
KAIKKI = "https://kaikki.org/dictionary/Russian/kaikki.org-dictionary-Russian.jsonl"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--home", type=Path, default=Path(os.environ.get("OVERHEAR_HOME", Path.home() / "overhear")))
    a = ap.parse_args()
    tok = os.environ.get("HF_TOKEN")
    for repo in HF:
        print("model", repo, flush=True)
        snapshot_download(repo, token=tok)
    cb = a.home / "models" / "chatterbox"
    if not (cb / "t3_mtl23ls_v2.safetensors").exists():
        print("model ResembleAI/chatterbox ->", cb, flush=True)
        snapshot_download("ResembleAI/chatterbox", local_dir=cb, token=tok)
    # MMS_FA alignment weights (torchaudio downloads them on first use; do it now).
    import torchaudio
    torchaudio.pipelines.MMS_FA.get_model()
    # RUAccent models (downloaded on first load).
    f5py = a.home / "venv-f5" / "bin" / "python"
    subprocess.run([str(f5py), "-I", "-c", "from ruaccent import RUAccent; \n[RUAccent().load(omograph_model_size=m, use_dictionary=True, device='CPU') for m in ('turbo', 'turbo3.1')]"], check=True)
    # Russian Wiktionary inflection tables (CC BY-SA, kaikki.org) for form-clip stress; ~2 GB, not in git.
    d = a.home / "dict" / "kaikki.org-dictionary-Russian.jsonl"
    if not d.exists():
        print("dict", KAIKKI, flush=True)
        tmp = d.with_suffix(".part")
        with urllib.request.urlopen(KAIKKI) as r, open(tmp, "wb") as f:
            shutil.copyfileobj(r, f, 1 << 20)
        tmp.rename(d)


if __name__ == "__main__":
    main()
