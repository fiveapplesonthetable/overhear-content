"""English narrator synthesis: F5-TTS v1 Base reference-cloned, batched per reference voice, with the sentence cache.

Runs in the F5 venv (config.VENV_F5) under gpurun. It is the English twin of espeech.EspeechEngine (same generate /
synth_many interface, so the renderer's retake path is unchanged) and reuses its batched sampler; only the model loading,
the text (plain English, no accent step) and the reference handling differ. Settings: settings.json `ttsEn`.

Reference: the voice's clip from voices.json, optionally trimmed to `refTrim[voice] = {seconds, text}` (a shorter prompt is
cheaper per step; text must be the words spoken in the trimmed clip). The block is part of the English cache key.
"""
import os
import tempfile
import time

import numpy as np
import soundfile as sf

from espeech import EspeechEngine, NATIVE_SR
from f5ref import ref_text_for_f5, trim_plan


class F5EnEngine(EspeechEngine):
    SETTINGS_KEY = "ttsEn"
    LANG_NAME = "English"
    BATCH_KEY = "batchEn"

    def __init__(self, settings, voices, log=print):
        import torch
        self.torch = torch
        self.s, self.voices, self.log = settings, voices, log
        self.c = settings[self.SETTINGS_KEY]
        t0 = time.time()
        from f5_tts.api import F5TTS
        api = F5TTS(model=self.c["model"], device="cuda")
        self.m, self.voc = api.ema_model, api.vocoder
        self.refs, self.paths = {}, {}
        self._tmp = tempfile.mkdtemp(prefix="f5en-")
        self.log(f"f5 {self.c['model']} ready in {time.time() - t0:.1f}s")

    def free(self):
        super().free()
        self.m = self.voc = None

    # English needs no accent step
    def text(self, tts_marked):
        return " ".join(tts_marked.split())

    def _ref(self, voice):
        if voice not in self.refs:
            import torch
            import torchaudio
            w, sr = sf.read(str(self.voices.ref_path(voice)), dtype="float32")
            w = w if w.ndim == 1 else w.mean(1)
            keep, text = trim_plan(self.c, voice, len(w) / sr, self.voices.refs[voice]["text"])
            w = w[:int(keep * sr)]
            a = torch.from_numpy(w)[None]
            rms = torch.sqrt(torch.mean(a ** 2))
            if rms < 0.1:
                a = a * 0.1 / rms
            if sr != NATIVE_SR:
                a = torchaudio.transforms.Resample(sr, NATIVE_SR)(a)
            path = os.path.join(self._tmp, f"{voice}.wav")
            sf.write(path, a.squeeze(0).numpy(), NATIVE_SR)
            self.paths[voice] = path
            self.refs[voice] = (a.cuda(), ref_text_for_f5(text), float(rms))
        return self.refs[voice]

    def _max_chars(self, voice, speed):
        a, rt, _ = self._ref(voice)
        sec = a.shape[-1] / NATIVE_SR
        return int(len(rt.encode("utf-8")) / sec * (22 - sec) * speed)

    def _single(self, voice, text, speed):
        from f5_tts.infer.utils_infer import infer_process
        _, rt, _ = self._ref(voice)
        path = self.paths[voice]
        w, sr, _ = infer_process(path, rt, text, self.m, self.voc, nfe_step=self.c["nfe"], cfg_strength=self.c["cfg"],
                                 sway_sampling_coef=self.c["sway"], speed=speed, show_info=lambda *x: None, progress=None)
        return np.asarray(w, dtype=np.float32)
