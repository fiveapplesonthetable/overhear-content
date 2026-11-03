#!/usr/bin/env python3
"""Audio & Voice QA Diagnostic Tool for Overhear renders and reference voices.

Replicates the exact acoustic debugging checks used in production:
  1. Pitch / F0 contour (Hz via YIN): catches cartoon/high-pitched voices (>215 Hz female) or gender flips.
  2. Sliding-window speaker identity (WavLM-base-plus-sv cosine similarity every 0.9s): catches mid-line narrator voice switches.
  3. Pre-speech 'shh' / breath hiss detector (Zero-Crossing Rate ZCR + RMS before voiced speech).
  4. Plosive tail-clipping & Chatterbox post-word hum detector (compares raw .flac vs prepared clip vs MMS_FA word end).
  5. Integrated loudness (ITU-R BS.1770-4 LUFS).

Usage:
  ~/overhear/venv-asr/bin/python tools/diagnose_audio.py refs --lang it
  ~/overhear/venv-asr/bin/python tools/diagnose_audio.py scene ~/overhear/render-store/porta-dos-fundos-s01e01-scene-03
  ~/overhear/venv-asr/bin/python tools/diagnose_audio.py clip ~/overhear/render-store/cache/tts/<sha>.flac --ref render/refs/sky.flac
"""
import argparse
import json
import sys
from pathlib import Path

import numpy as np
import soundfile as sf

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "render"))
import audio  # noqa: E402
import config  # noqa: E402


def measure_pitch_and_zcr(x: np.ndarray, sr: int) -> dict:
    import librosa
    x = np.asarray(x, dtype=np.float32)
    if x.ndim > 1:
        x = x.mean(axis=1)
    f0 = librosa.yin(x, fmin=65, fmax=450, sr=sr, frame_length=1024, hop_length=256)
    rms = librosa.feature.rms(y=x, frame_length=1024, hop_length=256)[0]
    n = min(len(f0), len(rms))
    vf0 = f0[:n][(rms[:n] >= max(1e-5, rms.max() * 0.10)) & (f0[:n] > 70.0) & (f0[:n] < 430.0)]
    lead_n = min(len(x), int(0.06 * sr))
    lead = x[:lead_n]
    lead_zcr = float(np.mean(lead[:-1] * lead[1:] < 0)) if len(lead) > 1 else 0.0
    return {
        "duration_s": round(len(x) / sr, 3),
        "lufs": round(audio.lufs(x, sr), 2),
        "f0_median_hz": round(float(np.median(vf0)), 1) if len(vf0) else 0.0,
        "f0_p90_hz": round(float(np.percentile(vf0, 90)), 1) if len(vf0) else 0.0,
        "f0_std_hz": round(float(np.std(vf0)), 1) if len(vf0) else 0.0,
        "lead_60ms_zcr": round(lead_zcr, 4),
    }


def cmd_refs(args):
    vdoc = json.loads((ROOT / "render" / "voices.json").read_text("utf-8"))
    refs = vdoc["refs"]
    for name in sorted(refs):
        if args.lang and refs[name].get("lang") != args.lang and not name.startswith(f"{args.lang}-"):
            continue
        flac = ROOT / "render" / "refs" / f"{name}.flac"
        if not flac.exists():
            continue
        x, sr = sf.read(str(flac), dtype="float32")
        m = measure_pitch_and_zcr(x, sr)
        flag = ""
        if "-f" in name and m["f0_median_hz"] > 212:
            flag = " [WARN: HIGH/PERKY FEMALE F0]"
        elif "-m" in name and m["f0_median_hz"] > 165:
            flag = " [WARN: HIGH MALE F0]"
        print(f"{name:10s} med={m['f0_median_hz']:5.1f}Hz p90={m['f0_p90_hz']:5.1f}Hz std={m['f0_std_hz']:4.1f}Hz "
              f"lufs={m['lufs']:6.2f} dur={m['duration_s']:4.2f}s{flag}")


def cmd_clip(args):
    x, sr = sf.read(args.flac, dtype="float32")
    s = config.load_settings()
    prep = audio.prepare_sentence(x, sr, s["audio"])
    m_raw = measure_pitch_and_zcr(x, sr)
    m_prep = measure_pitch_and_zcr(prep, sr)
    out = {"raw": m_raw, "prepared": m_prep, "trimmed_s": round(m_raw["duration_s"] - m_prep["duration_s"], 3)}
    if args.ref:
        import gates
        g = gates.AudioGates()
        import librosa, torch
        w16 = librosa.resample(prep, orig_sr=sr, target_sr=16000) if sr != 16000 else prep
        ref_w, ref_sr = sf.read(args.ref, dtype="float32")
        if ref_w.ndim > 1:
            ref_w = ref_w.mean(axis=1)
        ref_emb = g.get_embedding(ref_w, ref_sr)
        sims = []
        win, hop = 28800, 14400
        for ws in range(0, max(1, len(w16) - win + 1), hop):
            seg = w16[ws:ws + win]
            if len(seg) < 8000:
                continue
            emb = g.get_embedding(seg, 16000)
            sims.append(round(float(torch.nn.functional.cosine_similarity(emb, ref_emb, dim=0).item()), 4))
        out["sliding_wavlm_sim"] = sims
        out["min_wavlm_sim"] = min(sims) if sims else None
    print(json.dumps(out, indent=2))


def cmd_scene(args):
    import re
    sdir = Path(args.scene_dir)
    spans = json.loads((sdir / "spans.json").read_text("utf-8"))
    timing = json.loads((sdir / "timing.json").read_text("utf-8"))
    mp3_path = sdir / "audio.mp3"
    wav, sr = (sf.read(str(mp3_path)) if mp3_path.exists() else (None, 24000))
    if wav is not None and wav.ndim > 1:
        wav = wav.mean(axis=1)
    issues = []
    for seg in spans["segs"]:
        sid = str(seg["seg"])
        toks = timing.get(sid, [])
        if toks:
            tail = round(seg["end"] - (toks[-1]["e"] or seg["end"]), 3)
            last_dur = round((toks[-1]["e"] or 0) - (toks[-1]["s"] or 0), 3)
            clean_w = re.sub(r"[^\w]", "", toks[-1].get("t", ""))
            if tail > 0.65:
                issues.append({"seg": seg["seg"], "v": seg["v"], "issue": "long_unaligned_tail", "tail_s": tail,
                               "text": seg["sentences"][-1]["text"][:80]})
            if (len(clean_w) >= 5 and seg.get("lang") == "en" and last_dur < 0.21) or (len(clean_w) >= 3 and last_dur < 0.05):
                issues.append({"seg": seg["seg"], "v": seg["v"], "issue": "clipped_final_word", "last_word_s": last_dur,
                               "word": toks[-1]["t"], "text": seg["sentences"][-1]["text"][:80]})
        if wav is not None:
            win = int(0.02 * sr)
            for sent in seg["sentences"]:
                a, b = int(sent["start"] * sr), min(len(wav), int(sent["end"] * sr))
                chunk = wav[a:b]
                for i in range(0, len(chunk) - win, win):
                    f = chunk[i:i + win]
                    rms = float(np.sqrt(np.mean(f ** 2)))
                    if rms > 0.24:
                        zcr = float(np.mean(np.abs(np.diff(np.signbit(f)))))
                        if zcr < 0.08:
                            spec = np.abs(np.fft.rfft(f * np.hanning(len(f)))) + 1e-12
                            flat = float(np.exp(np.mean(np.log(spec))) / np.mean(spec))
                            if flat > 0.35:
                                issues.append({"seg": seg["seg"], "v": seg["v"], "issue": "broadband_noise_burst",
                                               "rms": round(rms, 3), "zcr": round(zcr, 3), "flatness": round(flat, 3),
                                               "text": sent["text"][:80]})
                                break
    print(json.dumps({"sceneId": spans["sceneId"], "durationSec": spans["durationSec"], "issues": issues}, indent=2, ensure_ascii=False))


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p_refs = sub.add_parser("refs")
    p_refs.add_argument("--lang", default=None)
    p_clip = sub.add_parser("clip")
    p_clip.add_argument("flac")
    p_clip.add_argument("--ref", default=None)
    p_sc = sub.add_parser("scene")
    p_sc.add_argument("scene_dir")
    a = ap.parse_args()
    if a.cmd == "refs":
        cmd_refs(a)
    elif a.cmd == "clip":
        cmd_clip(a)
    elif a.cmd == "scene":
        cmd_scene(a)


if __name__ == "__main__":
    main()
