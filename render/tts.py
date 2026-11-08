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
            if voice == "sky" and len(x) > int(7.88 * sr):
                # Strip the cut-off 7.90..8.08s post-sentence inhale/shush in sky.flac and pad clean digital silence
                x = x[:int(7.88 * sr)].copy()
                fn = int(0.015 * sr)
                x[-fn:] *= 0.5 * (1.0 + np.cos(np.linspace(0.0, np.pi, fn, dtype=np.float32)))
                x = np.concatenate([x, np.zeros(int(0.16 * sr), dtype=np.float32)])
            elif voice == "alisa":
                fn = int(0.015 * sr)
                x = x.copy()
                x[-fn:] *= 0.5 * (1.0 + np.cos(np.linspace(0.0, np.pi, fn, dtype=np.float32)))
                x = np.concatenate([x, np.zeros(int(0.16 * sr), dtype=np.float32)])
            elif voice in ("zh-m1", "zh-m2", "zh-m3", "zh-f2"):
                # Strip leading/trailing sighs in Mandarin reference clips in-memory so ICL prompts stay sigh-free
                cuts = {
                    "zh-m1": (0.0, 7.26),
                    "zh-m2": (1.08, 7.16),
                    "zh-m3": (0.0, 8.00),
                    "zh-f2": (0.80, None),
                }
                s_sec, e_sec = cuts[voice]
                s_idx = int(s_sec * sr)
                e_idx = int(e_sec * sr) if e_sec is not None else len(x)
                x = x[s_idx:min(len(x), e_idx)].copy()
                fn = int(0.015 * sr)
                x[:fn] *= 0.5 * (1.0 - np.cos(np.linspace(0.0, np.pi, fn, dtype=np.float32)))
                x[-fn:] *= 0.5 * (1.0 + np.cos(np.linspace(0.0, np.pi, fn, dtype=np.float32)))
                x = np.concatenate([np.zeros(int(0.10 * sr), dtype=np.float32), x, np.zeros(int(0.16 * sr), dtype=np.float32)])
            self.prompts[voice] = self.q.create_voice_clone_prompt(ref_audio=(x, sr), ref_text=self.voices.refs[voice]["text"])[0]
        return self.prompts[voice]

    def generate(self, batch, seed, temperature=None, repetition_penalty=None, top_k=None, top_p=None):
        """batch: [(voice, language_name, text_for_model)] -> [np.float32 wav at 24 kHz]."""
        torch = self.torch
        out = [None] * len(batch)
        real_idx = []
        for idx, b in enumerate(batch):
            if not any(ch.isalnum() for ch in b[2]):
                out[idx] = np.zeros(int(0.08 * NATIVE_SR), dtype=np.float32)
            else:
                real_idx.append(idx)
        if not real_idx:
            return out
        sub = [batch[i] for i in real_idx]
        torch.manual_seed(seed)
        np.random.seed(seed % (2 ** 32))
        t = self.s["tts"]
        longest = max(len(b[2]) for b in sub)
        pause_pad = 0.35 * max(b[2].count(",") + b[2].count("—") + b[2].count(":") + b[2].count(";") for b in sub)
        cps_floor = 4.5 if any(b[1] in ("Chinese", "Japanese", "Korean") for b in sub) else (9.5 if all(b[1] == "English" for b in sub) else 6.0)
        max_tokens = min(t["max_new_tokens"], int((longest / cps_floor + 2.2 + pause_pad) * 12.5) + 20)
        import re
        texts_in = [re.sub(r"\b([A-Z][a-z]+(?:yev|ev|ov))na\b", r"\1-nah", b[2]) if b[1] == "English" else b[2] for b in sub]
        wavs, sr = self.q.generate_voice_clone(
            text=texts_in, language=[b[1] for b in sub],
            voice_clone_prompt=[self._prompt(b[0]) for b in sub],
            temperature=temperature or t["temperature"],
            top_k=top_k if top_k is not None else t["top_k"],
            top_p=top_p if top_p is not None else t["top_p"],
            repetition_penalty=repetition_penalty if repetition_penalty is not None else t["repetition_penalty"], max_new_tokens=max_tokens)
        assert sr == NATIVE_SR, sr
        for idx, w in zip(real_idx, wavs):
            out[idx] = np.asarray(w, dtype=np.float32)
        return out


class QwenCustomEngine:
    """Qwen3-TTS-12Hz-1.7B-CustomVoice instruct-steered narrator synthesis."""

    def __init__(self, settings, voices, log=print, model_name="Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice"):
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
        model_src = _local_snapshot(model_name)
        self.q = Qwen3TTSModel.from_pretrained(model_src, **kw)
        self.log(f"custom-voice model ready in {time.time() - t0:.1f}s ({model_name})")

    def free(self):
        self.q = None
        import gc
        gc.collect()
        self.torch.cuda.empty_cache()

    def generate(self, batch, seed, temperature=None, repetition_penalty=None):
        """batch: [(voice, language_name, text_for_model)] -> [np.float32 wav at 24 kHz]."""
        torch = self.torch
        out = [None] * len(batch)
        real_idx = []
        for idx, b in enumerate(batch):
            if not any(ch.isalnum() for ch in b[2]):
                out[idx] = np.zeros(int(0.08 * NATIVE_SR), dtype=np.float32)
            else:
                real_idx.append(idx)
        if not real_idx:
            return out
        sub = [batch[i] for i in real_idx]
        torch.manual_seed(seed)
        np.random.seed(seed % (2 ** 32))
        t = self.s["tts"]
        longest = max(len(b[2]) for b in sub)
        # Alphabetic English speaks at ~13-16 chars/s; 9.5 chars/s + 2.0s gives generous ceiling without 80s EOS-miss babble
        cps_floor = 4.5 if any(b[1] in ("Chinese", "Japanese", "Korean") for b in sub) else 9.5
        max_tokens = min(t["max_new_tokens"], int((longest / cps_floor + 2.0) * 12.5) + 16)
        speakers = [self.voices.refs[b[0]]["customVoice"]["speaker"] for b in sub]
        instructs = [self.voices.refs[b[0]]["customVoice"].get("instruct", "") for b in sub]
        wavs, sr = self.q.generate_custom_voice(
            text=[b[2] for b in sub],
            speaker=speakers,
            language=[b[1] for b in sub],
            instruct=instructs,
            temperature=temperature or t["temperature"],
            top_k=t["top_k"],
            top_p=t["top_p"],
            repetition_penalty=repetition_penalty if repetition_penalty is not None else t["repetition_penalty"],
            max_new_tokens=max_tokens,
        )
        assert sr == NATIVE_SR, sr
        for idx, w in zip(real_idx, wavs):
            out[idx] = np.asarray(w, dtype=np.float32)
        return out

    def synth_many(self, items, store):
        """items: [dict(key, voice, lang, text_tts, text_plain)] unique by key. Fills store.tts_path(key) for each.
        Returns stats {n, audio_s, wall_s, retries}."""
        torch = self.torch
        t = self.s["tts"]
        langs = {"ko": "Korean", "ja": "Japanese", "zh": "Chinese", "it": "Italian", "pt": "Portuguese", "ar": "Arabic", "es": "Spanish", "de": "German"}
        langs.update(t.get("languages", {}))
        todo = [it for it in items if not store.tts_path(it["key"]).exists()]
        todo.sort(key=lambda it: len(it["text_tts"]))
        stats = {"n": 0, "audio_s": 0.0, "wall_s": 0.0, "retries": 0, "cached": len(items) - len(todo)}
        init_bs = max(1, int(os.environ.get("OVERHEAR_TTS_BATCH", t["batch"])))
        bs = init_bs
        pending = list(todo)
        attempt = 0
        t0 = time.time()
        
        import gates
        g = gates.get_gates()
        import json
        from plan import plausible
        
        while pending and attempt <= t["sentence_retries"]:
            nxt = []
            i = 0
            while i < len(pending):
                chunk = pending[i:i + bs]
                seed = int(chunk[0]["key"][:8], 16) + attempt * 7919
                
                chunk_en = [c for c in chunk if c["lang"] == "en"]
                chunk_target = [c for c in chunk if c["lang"] != "en"]
                
                wavs_en = []
                if chunk_en:
                    try:
                        torch.cuda.empty_cache()
                        wavs_en = self.generate(
                            [(c["voice"], langs[c["lang"]], c["text_tts"]) for c in chunk_en],
                            seed, temperature=0.54, repetition_penalty=1.08, top_k=25, top_p=0.85,
                        )
                    except torch.cuda.OutOfMemoryError:
                        torch.cuda.empty_cache()
                        if bs == 1: raise
                        bs = max(1, bs // 2)
                        self.log(f"OOM: batch size -> {bs}")
                        time.sleep(1.5)
                        continue


                wavs_target = []
                n_cands = 1 if getattr(self, "single_candidate_per_attempt", False) else 3
                if chunk_target:
                    ct_bs = max(1, bs // n_cands)
                    try:
                        temp = t.get("temperature", 0.7) * 0.95
                        rep = t.get("repetition_penalty", 1.0) * 1.1
                        for j in range(0, len(chunk_target), ct_bs):
                            ct_slice = chunk_target[j:j + ct_bs]
                            expanded_target = []
                            for c in ct_slice:
                                for cand_idx in range(n_cands):
                                    expanded_target.append(c)
                            torch.cuda.empty_cache()
                            wavs_target.extend(self.generate([(c["voice"], langs[c["lang"]], c["text_tts"]) for c in expanded_target], seed, temperature=temp, repetition_penalty=rep))
                    except torch.cuda.OutOfMemoryError:
                        torch.cuda.empty_cache()
                        if bs == 1: raise
                        bs = max(1, bs // 2)
                        self.log(f"OOM: batch size -> {bs}")
                        time.sleep(1.5)
                        continue

                
                i += len(chunk)
                if bs < init_bs:
                    bs = min(init_bs, bs * 2)
                torch.cuda.empty_cache()
                
                # process en
                for c, w in zip(chunk_en, wavs_en):
                    ref_path = self.voices.ref_path(c["voice"])
                    sim_ok, sim_val = g.check_similarity(w, NATIVE_SR, ref_path, threshold=0.78)
                    len_ok, len_reason = g.check_length_pause(w, NATIVE_SR, c["text_plain"], c["lang"])
                    tran_ok, tran_reason, w_trimmed = g.check_transient(w, NATIVE_SR)
                    rep_ok, cer_val, hyp = g.check_repeat_and_cer(w_trimmed, NATIVE_SR, c["text_plain"], c["lang"])
                    w = w_trimmed
                    all_ok = sim_ok and len_ok and tran_ok and rep_ok
                    
                    cer_val_fl = cer_val if isinstance(cer_val, float) else 1.0
                    
                    best = c.get("_best")
                    best_cer = c.get("_best_cer", 100.0)
                    if all_ok:
                        c["_best"] = w
                        c["_best_cer"] = cer_val_fl
                    else:
                        if best is None or cer_val_fl < best_cer:
                            c["_best"] = w
                            c["_best_cer"] = cer_val_fl
                            
                    ok = all_ok
                    if ok or attempt == t["sentence_retries"]:
                        w = w if ok else c["_best"]
                        p = store.tts_path(c["key"])
                        tmp = p.with_suffix(".tmp.flac")
                        sf.write(str(tmp), w, NATIVE_SR, format="FLAC", subtype="PCM_16")
                        tmp.replace(p)
                        stats["n"] += 1
                        stats["audio_s"] += len(w) / NATIVE_SR
                        
                        marker = store.tts_path(c["key"]).with_name(f'{c["key"]}.gates.json')
                        counts = {"takes": 1, "retakes": 0, "length": int(not len_ok), "repeat": int(not rep_ok), "transient": int(not tran_ok), "similarity": int(not sim_ok), "cer": int(cer_val_fl > 0.15)}
                        marker.write_text(json.dumps(counts))
                    else:
                        nxt.append(c)
                        stats["retries"] += 1
                        
                # process target
                for c_idx, c in enumerate(chunk_target):
                    w_list = wavs_target[c_idx*n_cands : c_idx*n_cands + n_cands]
                    candidates_info = []
                    ref_path = self.voices.ref_path(c["voice"])
                    for w in w_list:
                        sim_ok, sim_val = g.check_similarity(w, NATIVE_SR, ref_path)
                        len_ok, len_reason = g.check_length_pause(w, NATIVE_SR, c["text_plain"], c["lang"])
                        tran_ok, tran_reason, w = g.check_transient(w, NATIVE_SR)
                        rep_ok, cer_val, hyp = g.check_repeat_and_cer(w, NATIVE_SR, c["text_plain"], c["lang"])
                        cer_ok = (not isinstance(cer_val, float)) or cer_val <= (0.42 if c["lang"] == "ar" else 0.70)
                        
                        all_ok = sim_ok and len_ok and tran_ok and rep_ok and cer_ok
                        candidates_info.append({
                            "wav": w, "all_ok": all_ok, "cer": cer_val if isinstance(cer_val, float) else 1.0, 
                            "sim": sim_val,
                            "fails": {
                                "similarity": not sim_ok,
                                "length": (not len_ok and len_reason == "length"),
                                "pause": (not len_ok and len_reason == "pause"),
                                "transient": not tran_ok,
                                "repeat": not rep_ok
                            }
                        })
                    all_cands = c.setdefault("_all_candidates", [])
                    all_cands.extend(candidates_info)
                        
                    passing = [info for info in candidates_info if info["all_ok"]]
                    if passing:
                        best_info = min(passing, key=lambda x: (x["cer"], -x["sim"]))
                        ok = True
                    else:
                        best_info = min(all_cands, key=lambda x: (x["cer"], -x["sim"]))
                        ok = False
                        
                    w = best_info["wav"]
                    sec = len(w) / NATIVE_SR
                    
                    if ok or attempt == t["sentence_retries"]:
                        p = store.tts_path(c["key"])
                        tmp = p.with_suffix(".tmp.flac")
                        sf.write(str(tmp), w, NATIVE_SR, format="FLAC", subtype="PCM_16")
                        tmp.replace(p)
                        stats["n"] += 1
                        stats["audio_s"] += len(w) / NATIVE_SR
                        
                        marker = store.tts_path(c["key"]).with_name(f'{c["key"]}.gates.json')
                        counts = {"takes": len(candidates_info), "retakes": len(candidates_info) - 1, 
                                  "length": sum(1 for x in candidates_info if x["fails"]["length"] or x["fails"]["pause"]),
                                  "repeat": sum(1 for x in candidates_info if x["fails"]["repeat"]),
                                  "transient": sum(1 for x in candidates_info if x["fails"]["transient"]),
                                  "similarity": sum(1 for x in candidates_info if x["fails"]["similarity"]),
                                  "cer": sum(1 for x in candidates_info if isinstance(x["cer"], float) and x["cer"] > 0.15)} # arbitrary logic for CER fail count
                        marker.write_text(json.dumps(counts))
                    else:
                        nxt.append(c)
                        stats["retries"] += 1
            pending = nxt
            attempt += 1
        stats["wall_s"] = time.time() - t0
        return stats


QwenEngine.synth_many = QwenCustomEngine.synth_many


def load_wav(path):
    x, sr = sf.read(str(path), dtype="float32")
    return x, sr

