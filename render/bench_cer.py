"""CER per bench config (Whisper venv). usage: bench_cer.py OUTDIR"""
import json, re, sys, unicodedata
from pathlib import Path
import numpy as np, soundfile as sf, jiwer
from faster_whisper import WhisperModel
out = Path(sys.argv[1]); items = json.loads((out / "items.json").read_text())
m = WhisperModel("large-v3-turbo", device="cuda", compute_type="float16")
def nz(t):
    t = unicodedata.normalize("NFC", unicodedata.normalize("NFD", t).replace("́", ""))
    return re.sub(r"\s+", " ", re.sub(r"[^\w\s]", " ", t.lower().replace("ё", "е").replace("’", "'"))).strip()
res = {}
for d in sorted(p for p in out.iterdir() if p.is_dir()):
    cers = []
    if not any(d.glob("*.flac")):
        continue
    for i, it in enumerate(items):
        f = d / f"{i:02d}.flac"
        if not f.exists():
            continue
        x, sr = sf.read(str(f), dtype="float32")
        import subprocess
        r = subprocess.run(["ffmpeg", "-v", "error", "-i", str(f), "-ac", "1", "-ar", "16000", "-f", "f32le", "-"], capture_output=True)
        segs, _ = m.transcribe(np.frombuffer(r.stdout, dtype=np.float32), language=it["lang"], beam_size=5, condition_on_previous_text=False)
        hyp = " ".join(s.text for s in segs)
        cers.append(jiwer.cer(nz(it["text"]), nz(hyp)) if nz(hyp) else 1.0)
    res[d.name] = {"n": len(cers), "meanCER": round(float(np.mean(cers)), 4), "p90": round(float(np.percentile(cers, 90)), 4)}
    print(d.name, res[d.name], flush=True)
(out / "bench_cer.json").write_text(json.dumps(res, indent=1))
