"""Cached multilingual Chatterbox V2 Arabic synthesis; initialized only by the GPU stage owner."""
import copy
import os
from pathlib import Path

import numpy as np
from tts import NATIVE_SR, QwenEngine

REQUIRED_FILES = ("ve.pt", "t3_mtl23ls_v2.safetensors", "s3gen.pt", "grapheme_mtl_merged_expanded_v1.json", "Cangjie5_TC.json")


def checkpoint(settings):
    path = Path(settings["ttsAr"]["modelLocal"]).expanduser().resolve()
    if not path.is_dir() or any(not (path / name).is_file() for name in REQUIRED_FILES):
        raise ValueError("ttsAr.modelLocal must name a complete existing Chatterbox multilingual V2 snapshot; downloading is disabled")
    return path


class ChatterboxArEngine(QwenEngine):
    """Same per-sentence cache/retry interface as other engines; no synthesized reference padding."""
    def __init__(self, settings, voices, log=print):
        import torch
        os.environ.setdefault("HF_HUB_OFFLINE", "1")
        os.environ.setdefault("TRANSFORMERS_OFFLINE", "1")
        import perth
        if getattr(perth, "PerthImplicitWatermarker", None) is None:
            perth.PerthImplicitWatermarker = perth.DummyWatermarker
        from chatterbox.mtl_tts import ChatterboxMultilingualTTS
        self.torch, self.voices, self.log = torch, voices, log
        self.s = copy.deepcopy(settings)
        cfg = self.s["ttsAr"]
        self.s["tts"].update(batch=1, sentence_retries=cfg.get("sentence_retries", settings["tts"]["sentence_retries"]))
        self.s["tts"]["languages"]["ar"] = "ar"
        self.q = ChatterboxMultilingualTTS.from_local(checkpoint(settings), device="cuda")
        self.prompts = {}
        self.log("cached Arabic Chatterbox multilingual V2 ready; native pronunciation still requires independent QA")

    def generate(self, batch, seed, temperature=None, repetition_penalty=None):
        cfg = self.s["ttsAr"]
        self.torch.manual_seed(seed)
        np.random.seed(seed % (2 ** 32))
        result = []
        for voice, language, text in batch:
            if language.lower() not in ("ar", "arabic") or self.voices.lang_of(voice) != "ar":
                raise ValueError("Arabic engine requires a reviewed Arabic voice and language_id='ar'")
            reference = self.voices.ref_path(voice)
            if not reference.is_file():
                raise ValueError("Arabic voice reference must exist; no synthetic or repeated reference padding")
            wav = self.q.generate(
                text=text, language_id="ar", audio_prompt_path=str(reference),
                exaggeration=cfg.get("exaggeration", 0.5), cfg_weight=cfg.get("cfg_weight", 0.5),
                temperature=temperature if temperature is not None else cfg.get("temperature", 0.8),
                repetition_penalty=repetition_penalty if repetition_penalty is not None else cfg.get("repetition_penalty", 2.0), min_p=cfg.get("min_p", 0.05), top_p=cfg.get("top_p", 1.0))
            samples = np.asarray(wav.detach().cpu().numpy(), dtype=np.float32).reshape(-1)
            if not samples.size or not np.isfinite(samples).all():
                raise ValueError("Arabic synthesis produced empty/nonfinite audio")
            if self.q.sr != NATIVE_SR:
                import math
                from scipy.signal import resample_poly
                divisor = math.gcd(self.q.sr, NATIVE_SR)
                samples = resample_poly(samples, NATIVE_SR // divisor, self.q.sr // divisor).astype(np.float32)
            result.append(samples)
        return result
