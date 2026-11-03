#!/usr/bin/env python3
"""Generate and acoustically verify warm, grounded synthetic VoiceDesign reference voices.

Two-stage anti-perkiness recipe (eliminates high-pitched 'Duolingo' sing-song voices):
  Stage 1: Qwen3-TTS-12Hz-1.7B-VoiceDesign generates a calm, low-pitched English contralto/mezzo anchor
           (where VoiceDesign's instruct control is tightest: med_f0 165..195 Hz, std <= 28 Hz).
  Stage 2: Qwen3-TTS-12Hz-1.7B-Base clones that grounded timbre onto native target-language studio prose
           at low temperature (0.58), producing a 100% native-accented, calm, adult reference clip.

Usage:
  OVERHEAR_HOME="$HOME/overhear" ~/overhear/venv-qwen/bin/python tools/design_voices.py --voices it-f1,it-f2
"""
import argparse
import glob
import json
import subprocess
import sys
from pathlib import Path

import numpy as np
import soundfile as sf

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "render"))
import audio  # noqa: E402


VOICE_SPECS = {
    "it-f1": {
        "lang": "Italian",
        "anchor_instruct": "A 38-year-old woman with a deep, warm, calm contralto voice, speaking quietly and evenly in a studio with minimal pitch variation.",
        "anchor_text": "Good evening. Before we start filming the next scene, let us review the schedule quietly together.",
        "text": "Ascolta, prima di cominciare le riprese sul set, controlliamo insieme il programma di oggi con calma.",
        "f0_range": (162.0, 198.0),
    },
    "it-f2": {
        "lang": "Italian",
        "anchor_instruct": "A 34-year-old woman with a smooth, grounded, composed mezzo-soprano voice, relaxed conversational tone, steady low register.",
        "anchor_text": "Do not worry about this morning, we can speak with the director for a moment and sort out the whole scene.",
        "text": "Non ti preoccupare per stamattina, parliamo un attimo con il regista e sistemiamo subito tutta la scena.",
        "f0_range": (168.0, 202.0),
    },
}


def find_snapshot(repo_slug: str) -> str:
    snaps = sorted(glob.glob(str(Path.home() / f".cache/huggingface/hub/models--{repo_slug}/snapshots/*")))
    return snaps[-1] if snaps else repo_slug.replace("--", "/")


def measure_f0(flac_path: Path) -> tuple[float, float, float]:
    chk = subprocess.check_output([
        str(Path.home() / "overhear/venv-asr/bin/python"), "-c",
        f"import librosa, soundfile as sf, numpy as np; "
        f"x, sr = sf.read('{flac_path}', dtype='float32'); "
        f"f0 = librosa.yin(x, fmin=65, fmax=420, sr=sr, frame_length=1024, hop_length=256); "
        f"rms = librosa.feature.rms(y=x, frame_length=1024, hop_length=256)[0]; "
        f"vf = f0[(rms >= rms.max()*0.1) & (f0 > 75) & (f0 < 400)]; "
        f"print(round(float(np.median(vf)),1), round(float(np.percentile(vf,90)),1), round(float(np.std(vf)),1))"
    ], text=True).strip().split()
    return float(chk[0]), float(chk[1]), float(chk[2])


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--voices", default="it-f1,it-f2")
    a = ap.parse_args()
    targets = [v.strip() for v in a.voices.split(",") if v.strip()]

    import gc
    import torch
    from qwen_tts import Qwen3TTSModel

    vd_src = find_snapshot("Qwen--Qwen3-TTS-12Hz-1.7B-VoiceDesign")
    print(f"Stage 1: Loading VoiceDesign ({vd_src})...")
    vd = Qwen3TTSModel.from_pretrained(vd_src, device_map="cuda:0", dtype=torch.bfloat16)

    anchors = {}
    for vname in targets:
        spec = VOICE_SPECS[vname]
        lo, hi = spec["f0_range"]
        for seed in (112, 101, 121, 102, 106, 111):
            torch.manual_seed(seed)
            np.random.seed(seed)
            wavs, sr = vd.generate_voice_design(
                text=spec["anchor_text"],
                language="English",
                instruct=spec["anchor_instruct"],
                temperature=0.58,
                top_p=0.85,
                repetition_penalty=1.06,
                max_new_tokens=180,
            )
            w = audio.fade(audio.trim(np.asarray(wavs[0], dtype=np.float32), sr, -46.0, 0.04), sr, 15)
            tmp_a = Path(f"/tmp/{vname}_anchor.flac")
            sf.write(str(tmp_a), w, sr, format="FLAC", subtype="PCM_16")
            med_f0, p90_f0, std_f0 = measure_f0(tmp_a)
            print(f"  anchor {vname} seed={seed}: med_f0={med_f0}Hz p90={p90_f0}Hz std={std_f0}Hz")
            if (lo - 8.0) <= med_f0 <= hi and p90_f0 <= 224.0 and std_f0 <= 34.0:
                anchors[vname] = (w, sr, spec["anchor_text"])
                break
        if vname not in anchors:
            raise RuntimeError(f"Failed to design calm anchor for {vname}")

    del vd
    gc.collect()
    torch.cuda.empty_cache()

    base_src = find_snapshot("Qwen--Qwen3-TTS-12Hz-1.7B-Base")
    print(f"Stage 2: Loading Base ({base_src}) for native target-language cloning...")
    base = Qwen3TTSModel.from_pretrained(base_src, device_map="cuda:0", dtype=torch.bfloat16)

    vdoc_path = ROOT / "render" / "voices.json"
    vdoc = json.loads(vdoc_path.read_text("utf-8"))

    for vname in targets:
        spec = VOICE_SPECS[vname]
        lo, hi = spec["f0_range"]
        a_wav, a_sr, a_txt = anchors[vname]
        prompt = base.create_voice_clone_prompt(ref_audio=(a_wav, a_sr), x_vector_only_mode=True)[0]
        best = None
        for seed in range(201, 220):
            torch.manual_seed(seed)
            np.random.seed(seed)
            wavs, sr = base.generate_voice_clone(
                text=[spec["text"]],
                language=[spec["lang"]],
                voice_clone_prompt=[prompt],
                temperature=0.56,
                top_k=25,
                top_p=0.85,
                repetition_penalty=1.08,
                max_new_tokens=200,
            )
            w = audio.fade(audio.trim(np.asarray(wavs[0], dtype=np.float32), sr, -46.0, 0.04), sr, 15)
            dur = len(w) / sr
            if dur < 5.0 or dur > 11.0:
                continue
            tmp_f = Path(f"/tmp/{vname}_it_{seed}.flac")
            sf.write(str(tmp_f), w, sr, format="FLAC", subtype="PCM_16")
            med_f0, p90_f0, std_f0 = measure_f0(tmp_f)
            print(f"  native {vname} seed={seed}: med_f0={med_f0}Hz p90={p90_f0}Hz std={std_f0}Hz dur={dur:.2f}s")
            if lo <= med_f0 <= hi and p90_f0 <= 232.0 and std_f0 <= 40.0:
                best = (w, sr, med_f0, p90_f0, std_f0, dur)
                break
        if best is None:
            raise RuntimeError(f"Failed to synthesize grounded native ref for {vname}")
        w, sr, med_f0, p90_f0, std_f0, dur = best
        out_flac = ROOT / "render" / "refs" / f"{vname}.flac"
        sf.write(str(out_flac), w, sr, format="FLAC", subtype="PCM_16")
        entry = vdoc["refs"][vname]
        entry["text"] = spec["text"]
        old_v = str(entry.get("version", "v2"))
        entry["version"] = f"v{int(old_v.lstrip('v')) + 1}" if old_v.lstrip("v").isdigit() else "v3"
        print(f"SAVED {out_flac}: version={entry['version']} med_f0={med_f0}Hz p90={p90_f0}Hz std={std_f0}Hz")

    vdoc_path.write_text(json.dumps(vdoc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
