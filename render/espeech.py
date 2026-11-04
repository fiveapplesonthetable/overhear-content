"""ESpeech-TTS-1 (F5-TTS DiT) reference-cloned Russian synthesis, batched per reference voice, with the sentence cache.

Runs in the F5 venv (config.VENV_F5), under gpurun. Same interface as tts.QwenEngine (generate / synth_many) so the
renderer's retake path works unchanged. Settings: settings.json `ttsRu`.

Text: RUAccent on the whole sentence ('+' before the stressed vowel, F5/ESpeech convention); tokens that carry a combining
acute in the pipeline's marked text (the notes' homograph stress) win over RUAccent's choice.
Batching: sentences of one voice that fit one F5 chunk are sampled together (padded, lens-masked); anything longer than one
chunk goes through F5's own infer_process (chunk + crossfade). Duration is F5's usual rule (bytes ratio to the reference) / speed.
"""
import os
import re
import time
import unicodedata

import numpy as np
import soundfile as sf

import config
import textprep
from plan import plausible

NATIVE_SR = 24000
HOP = 256
CFG = dict(dim=1024, depth=22, heads=16, ff_mult=2, text_dim=512, conv_layers=4)
ACUTE = textprep.ACUTE


def acute2plus(t):
    t = unicodedata.normalize("NFD", t)
    return unicodedata.normalize("NFC", re.sub(r"([аеёиоуыэюяАЕЁИОУЫЭЮЯ])́", r"+\1", t))


class EspeechEngine:
    SETTINGS_KEY = "ttsRu"
    LANG_NAME = "Russian"
    BATCH_KEY = "batchRu"

    def __init__(self, settings, voices, log=print):
        import torch
        self.torch = torch
        self.s, self.voices, self.log = settings, voices, log
        self.c = settings[self.SETTINGS_KEY]
        t0 = time.time()
        from huggingface_hub import hf_hub_download
        from f5_tts.infer.utils_infer import load_model, load_vocoder
        from f5_tts.model import DiT
        from ruaccent import RUAccent
        self.acc = RUAccent()
        self.acc.load(omograph_model_size=self.c["ruaccent"], use_dictionary=True, tiny_mode=False)
        self.voc = load_vocoder()
        self.m = load_model(DiT, CFG, hf_hub_download(self.c["repo"], self.c["ckpt"]), vocab_file=hf_hub_download(self.c["repo"], "vocab.txt"))
        self.refs = {}
        self.log(f"espeech ready in {time.time() - t0:.1f}s")

    def free(self):
        self.m = self.voc = self.acc = None
        self.refs = {}
        import gc
        gc.collect()
        self.torch.cuda.empty_cache()

    # ---- text -------------------------------------------------------------------------------------------------
    def _accent(self, t):
        try:
            return self.acc.process_all(t)
        except Exception:     # RUAccent sometimes raises on a sentence: per-word fallback
            out = []
            for w in t.split():
                try:
                    out.append(self.acc.process_all(w))
                except Exception:
                    out.append(w)
            return " ".join(out)

    def text(self, tts_marked):
        """Pipeline-marked sentence (U+0301 on notes homographs) -> ESpeech text ('+' marks)."""
        plain = textprep.strip_acute(tts_marked)
        if plain.strip() in textprep.STANDALONE_PRONOUNCED:
            return "Пак+а!" if "!" in plain else "Пак+а."
        auto = self._accent(plain).replace("Отп+устите", "Отпуст+ите").replace("отп+устите", "отпуст+ите")
        a, b = auto.split(), tts_marked.split()
        if len(a) != len(b):
            return auto
        return " ".join(acute2plus(tb) if ACUTE in tb else ta for ta, tb in zip(a, b))

    # ---- reference ----------------------------------------------------------------------------------------------
    def _ref(self, voice):
        if voice not in self.refs:
            import torch
            import torchaudio
            w, sr = sf.read(str(self.voices.ref_path(voice)), dtype="float32")
            a = torch.from_numpy(w if w.ndim == 1 else w.mean(1))[None]
            rms = torch.sqrt(torch.mean(a ** 2))
            if rms < 0.1:
                a = a * 0.1 / rms
            if sr != NATIVE_SR:
                a = torchaudio.transforms.Resample(sr, NATIVE_SR)(a)
            # Guarantee >= 180 ms of pure digital silence at the end of `a` so slicing at `n_ref - 10`
            # captures early voiceless clusters (Ст-, Чт-, Кт-) without any reference speech bleed.
            win = int(0.010 * NATIVE_SR)
            a_np = a[0].numpy()
            n_win = len(a_np) // win
            if n_win > 0:
                f_rms = np.sqrt(np.mean(a_np[:n_win * win].reshape(n_win, win) ** 2, axis=1))
                act = np.where(f_rms > 0.006)[0]
                trail_ms = (n_win - 1 - int(act[-1])) * 10 if len(act) else 200
                if trail_ms < 180:
                    pad_n = int((0.190 - trail_ms / 1000.0) * NATIVE_SR)
                    a = torch.cat([a, torch.zeros((1, pad_n), dtype=a.dtype)], dim=-1)
            rt = self._accent(self.voices.refs[voice]["text"]).rstrip() + " "
            self.refs[voice] = (a.cuda(), rt, float(rms))
        return self.refs[voice]

    def _max_chars(self, voice, speed):
        a, rt, _ = self._ref(voice)
        sec = a.shape[-1] / NATIVE_SR
        return int(len(rt.encode("utf-8")) / sec * (22 - sec) * speed)

    # ---- sampling -----------------------------------------------------------------------------------------------
    def _batch(self, voice, texts, speed):
        """texts: ESpeech strings, all short enough for one chunk -> list of float32 wavs (24 kHz)."""
        torch = self.torch
        from f5_tts.model.utils import convert_char_to_pinyin
        a, rt, rms = self._ref(voice)
        n_ref = a.shape[-1] // HOP
        durs, tl = [], []
        min_gen_frames = int(0.68 * NATIVE_SR / HOP)
        for g in texts:
            g_clean = g.strip("-–— ") or g
            is_short = len(g_clean) <= 24
            if is_short and g_clean and g_clean[-1] not in ".!?…":
                g_clean = g_clean + "."
            sp = max(0.86, speed) if len(g_clean) <= 16 else speed
            raw_frames = int(n_ref / len(rt.encode("utf-8")) * len(g_clean.encode("utf-8")) / sp)
            # Always add +12% prosodic-pause headroom + 32 frames (~340 ms) so final stops/fricatives
            # (коньяк, нож, соус, матч) complete their closure + release burst well before durs[i].
            gen_frames = min(max(256, 2060 - n_ref), max(min_gen_frames, int(raw_frames * 1.12) + 32))
            durs.append(n_ref + gen_frames)
            tl.append(rt + " " + g_clean + "  ")
        txt = convert_char_to_pinyin(tl)
        B = len(texts)
        slice_start = max(0, n_ref - 10)
        with torch.inference_mode():
            gen, _ = self.m.sample(cond=a.repeat(B, 1), text=txt, duration=torch.tensor(durs, device=a.device), steps=self.c["nfe"],
                                   cfg_strength=self.c["cfg"], sway_sampling_coef=self.c["sway"])
            del _
            outs = []
            for i in range(B):
                mel = gen[i:i + 1, slice_start:durs[i], :].to(torch.float32).permute(0, 2, 1)
                w = self.voc.decode(mel)
                if rms < 0.1:
                    w = w * rms / 0.1
                outs.append(w.squeeze().cpu().numpy().astype(np.float32))
        return outs

    def _single(self, voice, text, speed):
        from f5_tts.infer.utils_infer import infer_process
        a, rt, _ = self._ref(voice)
        p = self.voices.ref_path(voice)
        w, sr, _ = infer_process(str(p), rt, " " + text + "   ", self.m, self.voc, nfe_step=self.c["nfe"], cfg_strength=self.c["cfg"],
                                 sway_sampling_coef=self.c["sway"], speed=speed * 0.94, show_info=lambda *x: None, progress=None)
        return np.asarray(w, dtype=np.float32)

    def generate(self, batch, seed, temperature=None, speed=None):
        """batch: [(voice, language_name, text_for_model)] -> [float32 wav at 24 kHz]. `temperature` is ignored (F5 has none);
        a different seed (and `speed`) gives a different take."""
        torch = self.torch
        speed = speed or self.c["speeds"][0]
        res = [None] * len(batch)
        by_voice = {}
        for i, (v, _lang, t) in enumerate(batch):
            by_voice.setdefault(v, []).append((i, self.text(t)))
        for v, items in by_voice.items():
            mc = self._max_chars(v, speed)
            short = [(i, g) for i, g in items if len(g.encode("utf-8")) <= mc]
            for i, g in items:
                if len(g.encode("utf-8")) > mc:
                    torch.manual_seed(seed + i)
                    res[i] = self._single(v, g, speed)
            if short:
                torch.manual_seed(seed)
                for i, w in zip([i for i, _ in short], self._batch(v, [g for _, g in short], speed)):
                    res[i] = w
        return res

    def synth_many(self, items, store):
        """items: [dict(key, voice, lang, text_tts, text_plain)] unique by key; fills store.tts_path(key). Returns stats."""
        torch = self.torch
        todo = [it for it in items if not store.tts_path(it["key"]).exists()]
        stats = {"n": 0, "audio_s": 0.0, "wall_s": 0.0, "retries": 0, "cached": len(items) - len(todo)}
        bs = max(1, int(self.s["tts"].get(self.BATCH_KEY, 8)))
        speeds = self.c["speeds"]
        t0 = time.time()
        by_voice = {}
        for it in todo:
            by_voice.setdefault(it["voice"], []).append(it)
        for voice, its in by_voice.items():
            pending = sorted(its, key=lambda it: len(it["text_tts"]))
            for attempt, speed in enumerate(speeds):
                nxt = []
                i = 0
                while i < len(pending):
                    chunk = pending[i:i + bs]
                    seed = int(chunk[0]["key"][:8], 16) + attempt * 7919

                    expanded = []
                    for c in chunk:
                        for cand_idx in range(3):
                            expanded.append(c)
                            
                    try:
                        ct_bs = max(1, bs // 3)
                        wavs = []
                        for j in range(0, len(expanded), ct_bs * 3):
                            expanded_slice = expanded[j:j + ct_bs * 3]
                            wavs.extend(self.generate([(voice, self.LANG_NAME, c["text_tts"]) for c in expanded_slice], seed, speed=speed))
                    except torch.cuda.OutOfMemoryError:
                        torch.cuda.empty_cache()
                        if bs == 1:
                            raise
                        bs = max(1, bs // 2)
                        self.log(f"OOM: batch -> {bs}")
                        continue
                    i += len(chunk)
                    
                    import gates
                    g = gates.get_gates()
                    import json
                    
                    for c_idx, c in enumerate(chunk):
                        w_list = wavs[c_idx*3 : c_idx*3 + 3]
                        candidates_info = []
                        ref_path = self.voices.ref_path(c["voice"])
                        for w in w_list:
                            sim_ok, sim_val = g.check_similarity(w, NATIVE_SR, ref_path)
                            len_ok, len_reason = g.check_length_pause(w, NATIVE_SR, c["text_plain"], c["lang"])
                            tran_ok, tran_reason, w_trimmed = g.check_transient(w, NATIVE_SR)
                            rep_ok, cer_val, hyp = g.check_repeat_and_cer(w_trimmed, NATIVE_SR, c["text_plain"], c["lang"])
                            w = w_trimmed
                            
                            all_ok = sim_ok and len_ok and tran_ok and rep_ok
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
                            
                        passing = [info for info in candidates_info if info["all_ok"]]
                        if passing:
                            best_info = min(passing, key=lambda x: (x["cer"], -x["sim"]))
                            ok = True
                        else:
                            best_info = min(candidates_info, key=lambda x: (x["cer"], -x["sim"]))
                            ok = False
                            
                        w = best_info["wav"]
                        sec = len(w) / NATIVE_SR
                        
                        # In espeech, we also check plausible length as an ultimate fallback
                        from plan import plausible
                        ok = ok and plausible(c["text_plain"], sec)
                        
                        if ok or attempt == len(speeds) - 1:
                            p = store.tts_path(c["key"])
                            tmp = p.with_suffix(".tmp.flac")
                            sf.write(str(tmp), w, NATIVE_SR, format="FLAC", subtype="PCM_16")
                            tmp.replace(p)
                            stats["n"] += 1
                            stats["audio_s"] += sec
                            
                            marker = store.tts_path(c["key"]).with_name(f'{c["key"]}.gates.json')
                            counts = {"takes": len(candidates_info), "retakes": len(candidates_info) - 1, 
                                      "length": sum(1 for x in candidates_info if x["fails"]["length"] or x["fails"]["pause"]),
                                      "repeat": sum(1 for x in candidates_info if x["fails"]["repeat"]),
                                      "transient": sum(1 for x in candidates_info if x["fails"]["transient"]),
                                      "similarity": sum(1 for x in candidates_info if x["fails"]["similarity"]),
                                      "cer": sum(1 for x in candidates_info if isinstance(x["cer"], float) and x["cer"] > 0.15)}
                            marker.write_text(json.dumps(counts))
                            
                            if not ok:
                                self.log(f"WARN implausible length/fails kept: {c['text_plain'][:60]!r} {sec:.1f}s")
                        else:
                            nxt.append(c)
                            stats["retries"] += 1

                pending = nxt
                if not pending:
                    break
        stats["wall_s"] = time.time() - t0
        return stats
