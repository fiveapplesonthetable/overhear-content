"""Whisper CER per sentence of rendered scenes (venv with faster-whisper; GPU, under the lock).

  $OVERHEAR_HOME/venv-asr/bin/python -I asr_cer.py --store DIR --out cer.json SCENE_ID [...]

Cuts each sentence from audio.mp3 by spans.json, transcribes with the segment language (en for the narrator),
and compares with the text as written (marks stripped, punctuation/case/ё folded).
"""
import argparse, json, re, subprocess, sys, unicodedata
from pathlib import Path
import numpy as np


def load(path, start, end):
    r = subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{max(0, start - 0.05):.3f}", "-t", f"{end - start + 0.1:.3f}", "-i", str(path),
                        "-ac", "1", "-ar", "16000", "-f", "f32le", "-"], capture_output=True)
    return np.frombuffer(r.stdout, dtype=np.float32)


def nz(t):
    t = unicodedata.normalize("NFC", unicodedata.normalize("NFD", t).replace("́", ""))
    t = re.sub(r"[^\w\s]", " ", t.lower().replace("’", "'").replace("ё", "е"))
    return re.sub(r"\s+", " ", t).strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--store", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("scenes", nargs="+")
    a = ap.parse_args()
    import jiwer
    from faster_whisper import WhisperModel
    try:
        m = WhisperModel("large-v3-turbo", device="cuda", compute_type="float16")
    except Exception as e:
        print("cuda unavailable, cpu:", e, file=sys.stderr)
        m = WhisperModel("large-v3-turbo", device="cpu", compute_type="int8")
    rows = []
    for sid in a.scenes:
        d = Path(a.store) / sid
        spans = json.loads((d / "spans.json").read_text())
        for seg in spans["segs"]:
            lang = seg["lang"]
            for s in seg["sentences"]:
                x = load(d / "audio.mp3", s["start"], s["end"])
                segs, _ = m.transcribe(x, language=lang, beam_size=5, condition_on_previous_text=False, vad_filter=False)
                hyp = " ".join(t.text for t in segs).strip()
                ref = s["text"]
                c = jiwer.cer(nz(ref), nz(hyp)) if nz(hyp) else 1.0
                rows.append({"scene": sid, "seg": seg["seg"], "role": seg["v"], "voice": seg["voice"], "lang": lang, "ref": ref, "hyp": hyp, "cer": round(c, 4)})
    by = {}
    for r in rows:
        by.setdefault(r["lang"] + ("-narrator" if r["role"] == "narrator" else ""), []).append(r["cer"])
    summary = {k: {"n": len(v), "meanCER": round(float(np.mean(v)), 4), "maxCER": round(float(np.max(v)), 4)} for k, v in by.items()}
    Path(a.out).write_text(json.dumps({"summary": summary, "rows": rows}, ensure_ascii=False, indent=1))
    print(json.dumps(summary, ensure_ascii=False))


if __name__ == "__main__":
    main()
