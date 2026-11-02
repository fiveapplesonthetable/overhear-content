"""Throughput (WP R.3): RTF of the real voices on N real sentences, for several configs.

  sh bench.sh OUTDIR     (bench.sh = this, then bench_cer.py in the Whisper venv)
Configs: batch size 1/4/8/16 (sdpa, bf16); optional attn=eager. RTF = wall seconds / audio seconds of the generation
call only (model load excluded; prompts pre-built). Writes OUTDIR/<cfg>/NN.flac, OUTDIR/items.json, OUTDIR/bench.json
(the best config's rtf is what --status uses until real runs exist).
"""
import json, os, sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
os.environ.setdefault("PYTORCH_CUDA_ALLOC_CONF", "expandable_segments:True")
import numpy as np, soundfile as sf, torch
import config, content, textprep
from voices import Voices
from plan import check_voices
from tts import QwenEngine, NATIVE_SR

N = int(os.environ.get("BENCH_N", "50"))


def pick_items(voices):
    scenes, _ = content.discover(only=lambda sh, s, e: sh == "kukhnya" and s == 1 and e == 2)
    items, seen = [], set()
    for sc in scenes[:3]:
        roles = check_voices(sc, voices)
        for g in sc.script["segments"]:
            for _, _, s in textprep.split_sentences(g["t"]):
                k = (roles[g["v"]], s)
                if k in seen:
                    continue
                seen.add(k)
                items.append({"voice": roles[g["v"]], "lang": voices.lang_of(roles[g["v"]]), "text": s})
    # interleave narrator/target to resemble a scene, keep N
    return items[:N] if len(items) >= N else items


def run(cfg, items, out, voices):
    s = config.load_settings()
    s["tts"]["batch"] = cfg.get("batch", 1)
    if cfg.get("attn"):
        s["tts"]["attn"] = cfg["attn"]
    s["lora"]["enabled"] = False
    eng = QwenEngine(s, voices, log=lambda *a: None)
    for v in {i["voice"] for i in items}:
        eng._prompt(v)
    langs = s["tts"]["languages"]
    eng.generate([(items[0]["voice"], langs[items[0]["lang"]], items[0]["text"])], 1)   # warm-up (kernels, allocator)
    torch.cuda.synchronize(); torch.cuda.reset_peak_memory_stats()
    order = sorted(range(len(items)), key=lambda i: len(items[i]["text"]))
    wall = audio = 0.0
    bs = s["tts"]["batch"]
    d = Path(out) / cfg["name"]; d.mkdir(parents=True, exist_ok=True)
    for a in range(0, len(order), bs):
        idx = order[a:a + bs]
        t = time.time()
        w = eng.generate([(items[i]["voice"], langs[items[i]["lang"]], items[i]["text"]) for i in idx], 100 + a)
        torch.cuda.synchronize(); wall += time.time() - t
        for i, x in zip(idx, w):
            audio += len(x) / NATIVE_SR
            sf.write(str(d / f"{i:02d}.flac"), x, NATIVE_SR, format="FLAC")
    r = {"name": cfg["name"], "batch": bs, "attn": s["tts"]["attn"], "sentences": len(items), "audioSec": round(audio, 1), "wallSec": round(wall, 1),
         "rtf": round(wall / audio, 3), "peakMiB": round(torch.cuda.max_memory_allocated() / 2 ** 20)}
    print(json.dumps(r), flush=True)
    eng.free(); del eng
    torch.cuda.empty_cache()
    return r


def main():
    out = Path(sys.argv[1]); out.mkdir(parents=True, exist_ok=True)
    voices = Voices()
    items = pick_items(voices)
    (out / "items.json").write_text(json.dumps(items, ensure_ascii=False))
    cfgs = [{"name": "b1", "batch": 1}, {"name": "b4", "batch": 4}, {"name": "b8", "batch": 8}, {"name": "b16", "batch": 16}]
    if os.environ.get("BENCH_CFGS"):
        cfgs = [c for c in cfgs if c["name"] in os.environ["BENCH_CFGS"].split(",")]
    res = []
    for c in cfgs:
        try:
            res.append(run(c, items, out, voices))
        except Exception as e:
            print(json.dumps({"name": c["name"], "error": f"{type(e).__name__}: {str(e)[:200]}"}), flush=True)
            torch.cuda.empty_cache()
    (out / "bench.json").write_text(json.dumps({"results": res}, indent=1))


main()
