"""Hindi narrator / dialogue engine: Chatterbox multilingual V2 with language_id='hi'.

Same per-sentence cache/retry interface as ChatterboxArEngine (render/chatterbox_ar.py); settings block `ttsHi`
(engine "chatterbox"). Voices must be reviewed synthetic Hindi references (render/refs/hi-*.flac, lang "hi").
"""
import copy
import os

import numpy as np

from chatterbox_ar import ChatterboxArEngine, _patch_chatterbox_arabic, checkpoint
from tts import NATIVE_SR

_HI_END = "।.!?…"


class HindiEngine(ChatterboxArEngine):
    single_candidate_per_attempt = True

    def __init__(self, settings, voices, log=print):
        import torch
        os.environ.setdefault("HF_HUB_OFFLINE", "1")
        os.environ.setdefault("TRANSFORMERS_OFFLINE", "1")
        import perth
        if getattr(perth, "PerthImplicitWatermarker", None) is None:
            perth.PerthImplicitWatermarker = perth.DummyWatermarker
        _patch_chatterbox_arabic()
        from chatterbox.mtl_tts import ChatterboxMultilingualTTS
        self.torch, self.voices, self.log = torch, voices, log
        self.s = copy.deepcopy(settings)
        cfg = self.s["ttsHi"]
        self.s["tts"].update(batch=1, sentence_retries=cfg.get("sentence_retries", settings["tts"]["sentence_retries"]))
        self.s["tts"]["languages"]["hi"] = "hi"
        self.q = ChatterboxMultilingualTTS.from_local(checkpoint({"ttsAr": cfg}), device="cuda")
        self.prompts = {}
        self.log("Hindi Chatterbox multilingual V2 ready (language_id='hi')")

    def generate(self, batch, seed, temperature=None, repetition_penalty=None):
        cfg = self.s["ttsHi"]
        self.torch.manual_seed(seed)
        np.random.seed(seed % (2 ** 32))
        exag = cfg.get("exaggeration", 0.5)
        result = []
        for voice, language, text in batch:
            if language.lower() not in ("hi", "hindi") or self.voices.lang_of(voice) != "hi":
                raise ValueError("Hindi engine requires a reviewed Hindi voice and language_id='hi'")
            reference = self.voices.ref_path(voice)
            if not reference.is_file():
                raise ValueError("Hindi voice reference must exist")
            t_in = text.strip()
            if not any(ch.isalnum() for ch in t_in):
                result.append(np.zeros(int(0.08 * NATIVE_SR), dtype=np.float32))
                continue
            if t_in[-1] not in _HI_END:
                t_in = t_in + "।"
            prompt_arg = self._activate_voice(voice, reference, exag)
            wav = None
            for sub_try in range(4):
                try:
                    if sub_try > 0:
                        self.torch.manual_seed(seed + sub_try * 997)
                    wav = self.q.generate(
                        text=t_in, language_id="hi", audio_prompt_path=prompt_arg,
                        exaggeration=exag, cfg_weight=cfg.get("cfg_weight", 0.5),
                        temperature=temperature if temperature is not None else cfg.get("temperature", 0.8),
                        repetition_penalty=repetition_penalty if repetition_penalty is not None else cfg.get("repetition_penalty", 2.0),
                        min_p=cfg.get("min_p", 0.05), top_p=cfg.get("top_p", 1.0))
                    break
                except RuntimeError:
                    if sub_try == 3:
                        raise
            samples = np.asarray(wav.detach().cpu().numpy(), dtype=np.float32).reshape(-1)
            if not samples.size or not np.isfinite(samples).all():
                raise ValueError("Hindi synthesis produced empty/nonfinite audio")
            if self.q.sr != NATIVE_SR:
                import math
                from scipy.signal import resample_poly
                divisor = math.gcd(self.q.sr, NATIVE_SR)
                samples = resample_poly(samples, NATIVE_SR // divisor, self.q.sr // divisor).astype(np.float32)
            result.append(samples)
        return result
