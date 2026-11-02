"""After setup.sh: every venv imports what the renderer needs, the GPU is visible, ffmpeg/lame exist, the refs are in place.
usage: venv-qwen/bin/python -I selfcheck.py   (exit 1 on any failure)"""
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

RENDER = Path(__file__).resolve().parent.parent
H = Path(os.environ.get("OVERHEAR_HOME", Path.home() / "overhear"))
CHECKS = {
    "venv-qwen": "import torch, torchaudio, qwen_tts, peft, librosa, soundfile, uroman; assert torch.cuda.is_available(); print(torch.cuda.get_device_name(0), torch.cuda.get_device_properties(0).total_memory >> 20, 'MiB')",
    "venv-f5": "import torch, f5_tts, ruaccent, vocos; assert torch.cuda.is_available()",
    "venv-asr": "import torch, faster_whisper, chatterbox, jiwer, pyloudnorm; assert torch.cuda.is_available()",
}
bad = 0
for venv, code in CHECKS.items():
    r = subprocess.run([str(H / venv / "bin" / "python"), "-I", "-c", code], capture_output=True, text=True)
    print(("ok  " if r.returncode == 0 else "FAIL"), venv, (r.stdout + r.stderr).strip()[-300:])
    bad += r.returncode != 0
for tool in ("ffmpeg", "lame"):
    ok = shutil.which(tool) is not None
    print(("ok  " if ok else "FAIL"), tool)
    bad += not ok
voices = json.loads((RENDER / "voices.json").read_text(encoding="utf-8"))["refs"]
missing = [k for k, v in voices.items() if not (RENDER / v["file"]).is_file()]
print(("ok  " if not missing else "FAIL"), len(voices), "voice refs", missing or "")
bad += bool(missing)
for p in (H / "models" / "chatterbox" / "t3_mtl23ls_v2.safetensors", H / "dict" / "kaikki.org-dictionary-Russian.jsonl"):
    print(("ok  " if p.exists() else "FAIL"), p)
    bad += not p.exists()
sys.exit(1 if bad else 0)
