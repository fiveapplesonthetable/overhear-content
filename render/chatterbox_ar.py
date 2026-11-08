"""Cached multilingual Chatterbox V2 Arabic synthesis; initialized only by the GPU stage owner."""
import copy
import logging
import os
from pathlib import Path

import numpy as np
from tts import NATIVE_SR, QwenEngine

REQUIRED_FILES = ("ve.pt", "t3_mtl23ls_v2.safetensors", "s3gen.pt", "grapheme_mtl_merged_expanded_v1.json", "Cangjie5_TC.json")


def _patch_chatterbox_arabic():
    """Fix two upstream chatterbox-tts bugs that truncate Arabic sentences and flatten Arabic questions:
    1) mtl_tts.punc_norm omits Arabic '؟'/'،'/'؛' from sentence_enders, turning 'الباب مسكر؟' into 'الباب مسكر؟.'.
    2) AlignmentStreamAnalyzer.step triggers token_repetition on any 2x identical speech token (80ms comma/vowel pause)
       even when self.complete is False, forcing premature EOS mid-sentence."""
    import chatterbox.mtl_tts as mtl_tts
    from chatterbox.models.t3.inference import alignment_stream_analyzer as asa

    if getattr(mtl_tts, "_overhear_ar_patched", False):
        return

    def punc_norm_ar(text: str) -> str:
        if len(text) == 0:
            return "You need to add some text for me to talk."
        if text[0].islower():
            text = text[0].upper() + text[1:]
        text = " ".join(text.split())
        for old_seq, new_ch in (
            ("...", ", "), ("…", ", "), (":", ","), (" - ", ", "),
            (";", ", "), ("؛", "، "), ("—", "-"), ("–", "-"),
            (" ,", ","), (" ،", "،"), ("“", '"'), ("”", '"'), ("‘", "'"), ("’", "'"),
        ):
            text = text.replace(old_seq, new_ch)
        text = text.rstrip(" ")
        sentence_enders = {".", "!", "?", "؟", "-", ",", "،", "、", "，", "。", "？", "！"}
        if not any(text.endswith(p) for p in sentence_enders):
            text += "."
        return text

    def step_ar_safe(self, logits, next_token=None):
        import torch
        aligned_attn = torch.stack(self.last_aligned_attns).mean(dim=0)
        i, j = self.text_tokens_slice
        if self.curr_frame_pos == 0:
            A_chunk = aligned_attn[j:, i:j].clone().cpu()
        else:
            A_chunk = aligned_attn[:, i:j].clone().cpu()
        A_chunk[:, self.curr_frame_pos + 1:] = 0
        self.alignment = torch.cat((self.alignment, A_chunk), dim=0)
        A = self.alignment
        T, S = A.shape
        cur_text_posn = A_chunk[-1].argmax()
        discontinuity = not (-4 < cur_text_posn - self.text_position < 7)
        if not discontinuity:
            self.text_position = cur_text_posn
        false_start = (not self.started) and (A[-2:, -2:].max() > 0.1 or A[:, :4].max() < 0.5)
        self.started = not false_start
        if self.started and self.started_at is None:
            self.started_at = T
        self.complete = self.complete or self.text_position >= S - 3
        if self.complete and self.completed_at is None:
            self.completed_at = T
        long_tail = self.complete and (A[self.completed_at:, -3:].sum(dim=0).max() >= 5)
        alignment_repetition = self.complete and (A[self.completed_at:, :-5].max(dim=1).values.sum() > 5)
        if next_token is not None:
            token_id = next_token.item() if isinstance(next_token, torch.Tensor) and next_token.numel() == 1 else (
                next_token.view(-1)[0].item() if isinstance(next_token, torch.Tensor) else next_token
            )
            self.generated_tokens.append(token_id)
            if len(self.generated_tokens) > 10:
                self.generated_tokens = self.generated_tokens[-10:]
        # Mid-sentence comma/breath pauses routinely emit 2-4 identical silence tokens; only treat 8x mid-sentence
        # or 3x post-completion as runaway repetition.
        if self.complete:
            token_repetition = len(self.generated_tokens) >= 3 and len(set(self.generated_tokens[-3:])) == 1
        else:
            token_repetition = len(self.generated_tokens) >= 8 and len(set(self.generated_tokens[-8:])) == 1
        if cur_text_posn < S - 3 and S > 5:
            logits[..., self.eos_idx] = -2**15
        if long_tail or alignment_repetition or token_repetition:
            logging.getLogger(asa.__name__).debug(
                f"forcing EOS token, {long_tail=}, {alignment_repetition=}, {token_repetition=}"
            )
            logits = -(2**15) * torch.ones_like(logits)
            logits[..., self.eos_idx] = 2**15
        self.curr_frame_pos += 1
        return logits

    mtl_tts.punc_norm = punc_norm_ar
    asa.AlignmentStreamAnalyzer.step = step_ar_safe
    mtl_tts._overhear_ar_patched = True


def checkpoint(settings):
    path = Path(settings["ttsAr"]["modelLocal"]).expanduser().resolve()
    if not path.is_dir() or any(not (path / name).is_file() for name in REQUIRED_FILES):
        raise ValueError("ttsAr.modelLocal must name a complete existing Chatterbox multilingual V2 snapshot; downloading is disabled")
    return path


class ChatterboxArEngine(QwenEngine):
    """Same per-sentence cache/retry interface as other engines; no synthesized reference padding."""
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
        cfg = self.s["ttsAr"]
        self.s["tts"].update(batch=1, sentence_retries=cfg.get("sentence_retries", settings["tts"]["sentence_retries"]))
        self.s["tts"]["languages"]["ar"] = "ar"
        self.q = ChatterboxMultilingualTTS.from_local(checkpoint(settings), device="cuda")
        self.prompts = {}
        self.log("cached Arabic Chatterbox multilingual V2 ready (punc_norm + alignment_stream patched)")

    def _activate_voice(self, voice: str, reference: Path, exaggeration: float):
        if not hasattr(self.q, "prepare_conditionals"):
            return str(reference)
        if not hasattr(self, "prompts"):
            self.prompts = {}
        key = (voice, round(float(exaggeration), 4))
        if key not in self.prompts:
            self.q.prepare_conditionals(str(reference), exaggeration=exaggeration)
            self.prompts[key] = self.q.conds
        else:
            self.q.conds = self.prompts[key]
        return None

    def generate(self, batch, seed, temperature=None, repetition_penalty=None):
        cfg = self.s["ttsAr"]
        self.torch.manual_seed(seed)
        np.random.seed(seed % (2 ** 32))
        exag = cfg.get("exaggeration", 0.5)
        result = []
        for voice, language, text in batch:
            if language.lower() not in ("ar", "arabic") or self.voices.lang_of(voice) != "ar":
                raise ValueError("Arabic engine requires a reviewed Arabic voice and language_id='ar'")
            reference = self.voices.ref_path(voice)
            if not reference.is_file():
                raise ValueError("Arabic voice reference must exist; no synthetic or repeated reference padding")
            t_in = text.strip()
            if not any(ch.isalnum() for ch in t_in):
                result.append(np.zeros(int(0.08 * NATIVE_SR), dtype=np.float32))
                continue
            if len(t_in) == 1:
                t_in = t_in + "َ."
            elif len(t_in) <= 3 and t_in[-1] not in ".!؟?…":
                t_in = t_in + "."
            prompt_arg = self._activate_voice(voice, reference, exag)
            wav = None
            for sub_try in range(4):
                try:
                    if sub_try > 0:
                        self.torch.manual_seed(seed + sub_try * 997)
                    t_try = t_in if sub_try < 2 else (text.strip() + "َ.")
                    wav = self.q.generate(
                        text=t_try, language_id="ar", audio_prompt_path=prompt_arg,
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
                raise ValueError("Arabic synthesis produced empty/nonfinite audio")
            if self.q.sr != NATIVE_SR:
                import math
                from scipy.signal import resample_poly
                divisor = math.gcd(self.q.sr, NATIVE_SR)
                samples = resample_poly(samples, NATIVE_SR // divisor, self.q.sr // divisor).astype(np.float32)
            result.append(samples)
        return result
