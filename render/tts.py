"""Qwen3-TTS-12Hz-1.7B-Base voice cloning (ICL: ref_audio + ref_text), with a per-sentence content-addressed cache.

GPU stage: the caller holds gpurun reservation and sets PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True.
The stress LoRA is a config switch (settings.json lora.enabled); it is merged into the talker at load time.
"""
import hashlib
import json
import os
import sys
import time
from pathlib import Path

import numpy as np
import soundfile as sf

import config

NATIVE_SR = 24000


from plan import cache_key, plausible  # noqa: E402,F401


def _local_snapshot(repo_or_path, revision=None):
    if repo_or_path and Path(str(repo_or_path)).exists():
        return str(repo_or_path)
    try:
        from huggingface_hub import snapshot_download
        return snapshot_download(repo_or_path, revision=revision, local_files_only=True)
    except Exception:
        return repo_or_path


class QwenEngine:
    def __init__(self, settings, voices, log=print):
        import torch
        self.torch = torch
        self.s, self.voices, self.log = settings, voices, log
        t = settings["tts"]
        from qwen_tts import Qwen3TTSModel
        t0 = time.time()
        dtype = {"bfloat16": torch.bfloat16, "float16": torch.float16}[t["dtype"]]
        kw = dict(device_map="cuda:0", dtype=dtype)
        if t.get("attn"):
            kw["attn_implementation"] = t["attn"]
        model_src = _local_snapshot(t["model"])
        self.q = Qwen3TTSModel.from_pretrained(model_src, **kw)
        self.lora_info = None
        if settings["lora"]["enabled"]:
            self._load_lora(settings["lora"])
        self.prompts = {}
        self.log(f"model ready in {time.time() - t0:.1f}s (lora={self.lora_info})")

    def _load_lora(self, cfg):
        from peft import PeftModel
        src = cfg["local"] if cfg.get("local") and Path(cfg["local"]).exists() else _local_snapshot(cfg["hf"], cfg.get("revision"))
        kw = {}
        if not Path(str(src)).exists():
            tok = config.HF_TOKEN_FILE.read_text().strip() if config.HF_TOKEN_FILE.exists() else None
            if tok:
                kw["token"] = tok
            if cfg.get("revision"):
                kw["revision"] = cfg["revision"]
        pm = PeftModel.from_pretrained(self.q.model, src, **kw)
        self.q.model = pm.merge_and_unload()
        self.lora_info = {"source": str(src) if Path(str(src)).exists() else cfg["hf"], "tag": cfg["tag"]}

    def free(self):
        self.q = None
        self.prompts = {}
        import gc
        gc.collect()
        self.torch.cuda.empty_cache()

    def _prompt(self, voice):
        if voice not in self.prompts:
            ref = self.voices.ref_path(voice)
            x, sr = sf.read(str(ref), dtype="float32")
            self.prompts[voice] = self.q.create_voice_clone_prompt(ref_audio=(x, sr), ref_text=self.voices.refs[voice]["text"])[0]
        return self.prompts[voice]

    def generate(self, batch, seed, temperature=None):
        """batch: [(voice, language_name, text_for_model)] -> [np.float32 wav at 24 kHz]."""
        torch = self.torch
        torch.manual_seed(seed)
        np.random.seed(seed % (2 ** 32))
        t = self.s["tts"]
        longest = max(len(b[2]) for b in batch)
        max_tokens = min(t["max_new_tokens"], int((longest / 4.5 + 3) * 12.5) + 30)
        wavs, sr = self.q.generate_voice_clone(
            text=[b[2] for b in batch], language=[b[1] for b in batch],
            voice_clone_prompt=[self._prompt(b[0]) for b in batch],
            temperature=temperature or t["temperature"], top_k=t["top_k"], top_p=t["top_p"],
            repetition_penalty=t["repetition_penalty"], max_new_tokens=max_tokens)
        assert sr == NATIVE_SR, sr
        return [np.asarray(w, dtype=np.float32) for w in wavs]

    def synth_many(self, items, store):
        """items: [dict(key, voice, lang, text_tts, text_plain)] unique by key. Fills store.tts_path(key) for each.
        Returns stats {n, audio_s, wall_s, retries}."""
        torch = self.torch
        t = self.s["tts"]
        langs = t["languages"]
        todo = [it for it in items if not store.tts_path(it["key"]).exists()]
        todo.sort(key=lambda it: len(it["text_tts"]))
        stats = {"n": 0, "audio_s": 0.0, "wall_s": 0.0, "retries": 0, "cached": len(items) - len(todo)}
        bs = max(1, int(t["batch"]))
        pending = list(todo)
        attempt = 0
        t0 = time.time()
        while pending and attempt <= t["sentence_retries"]:
            nxt = []
            i = 0
            while i < len(pending):
                chunk = pending[i:i + bs]
                seed = int(chunk[0]["key"][:8], 16) + attempt * 7919
                try:
                    wavs = self.generate([(c["voice"], langs[c["lang"]], c["text_tts"]) for c in chunk], seed)
                except torch.cuda.OutOfMemoryError:
                    torch.cuda.empty_cache()
                    if bs == 1:
                        raise
                    bs = max(1, bs // 2)
                    self.log(f"OOM: batch size -> {bs}")
                    continue
                i += len(chunk)
                for c, w in zip(chunk, wavs):
                    sec = len(w) / NATIVE_SR
                    ok = plausible(c["text_plain"], sec)
                    best = c.get("_best")
                    if best is None or abs(sec - len(c["text_plain"]) / 14.0) < abs(len(best) / NATIVE_SR - len(c["text_plain"]) / 14.0):
                        c["_best"] = w
                    if ok or attempt == t["sentence_retries"]:
                        w = w if ok else c["_best"]
                        p = store.tts_path(c["key"])
                        tmp = p.with_suffix(".tmp.flac")
                        sf.write(str(tmp), w, NATIVE_SR, format="FLAC", subtype="PCM_16")
                        tmp.replace(p)
                        stats["n"] += 1
                        stats["audio_s"] += len(w) / NATIVE_SR
                        if not ok:
                            self.log(f"WARN implausible length kept after retries: {c['text_plain'][:60]!r} {sec:.1f}s")
                    else:
                        nxt.append(c)
                        stats["retries"] += 1
            pending = nxt
            attempt += 1
        stats["wall_s"] = time.time() - t0
        return stats


def load_wav(path):
    x, sr = sf.read(str(path), dtype="float32")
    return x, sr

