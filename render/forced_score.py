"""Forced scoring: how likely Whisper finds a given spelling for this audio (teacher forcing), against the other forms of the lemma.

Free decoding of a lone word is biased toward the citation form (the audio of "белой" is written "Белый"). So a take of a table form also passes when
the reference spelling is more probable, given the audio, than EVERY other form of the paradigm and than Whisper's own free decoding, by `margin` nats.
The model is faster-whisper's large-v3-turbo (the same one as the CER check); needs ctranslate2 4.x (`generate(..., return_logits_vocab=True)`).

  scorer = ForcedScorer(model, "ru")
  enc = scorer.encode(samples_16k)
  scorer.margin(enc, "белой", others=["белый", "белая", ...], heard="Белый.")  -> nats (reference score - best competitor score)
"""
import re

import numpy as np


def _logsoftmax(x):
    x = x.astype(np.float64)
    m = x.max()
    return x - (m + np.log(np.exp(x - m).sum()))


def variants(text):
    """The written shapes Whisper gives a lone word: " Белой." " Белой!" " Белой?" (capitalised, ended by a mark)."""
    t = text.strip()
    cap = t[:1].upper() + t[1:]
    return [" " + cap + m for m in (".", "!", "?")]


class ForcedScorer:
    def __init__(self, model, language="ru"):
        from faster_whisper.tokenizer import Tokenizer
        self.m = model
        self.tok = Tokenizer(model.hf_tokenizer, True, task="transcribe", language=language)
        self.base = list(self.tok.sot_sequence) + [self.tok.no_timestamps]
        self.eot = self.tok.eot
        self._cache = {}
        self._enc = None

    def encode(self, samples):
        """Encoder output of one clip (30 s window, as Whisper does for a short clip); resets the prefix cache."""
        from faster_whisper.audio import pad_or_trim
        feats = self.m.feature_extractor(samples)[:, :3000]
        self._enc = self.m.encode(pad_or_trim(feats))
        self._cache = {}
        return self._enc

    def score_tokens(self, ids):
        """log P(ids | audio) (the end-of-text step is left out: the decoder masks it right after forced tokens, and every candidate ends in a mark). One decoder pass: the tokens are given as the prompt, and the model returns its distribution at every
        position of the output, the forced ones included (position k predicts token k)."""
        import ctranslate2
        key = tuple(ids)
        if key in self._cache:
            return self._cache[key]
        prompt = self.base + list(ids)
        r = self.m.model.generate(self._enc, [prompt], beam_size=1, max_length=len(prompt) + len(ids) + 4, return_logits_vocab=True)[0]
        steps = r.logits[0]
        if len(steps) < len(ids):
            raise RuntimeError(f'short logits {len(steps)} for {ids} -> {r.sequences_ids}')
        total = 0.0
        for k, t in enumerate(ids):
            lp = _logsoftmax(np.array(steps[k].to_device(ctranslate2.Device.cpu)).reshape(-1))
            total += float(lp[t])
        self._cache[key] = total
        return total

    def score(self, text):
        """log P(text, end | audio): the best of the written variants."""
        best = -1e9
        for v in variants(text):
            best = max(best, self.score_tokens(self.tok.encode(v)))
        return best

    def score_raw(self, text):
        """The score of `text` exactly as written (Whisper's own output, with its punctuation and case)."""
        t = text if text.startswith(" ") else " " + text
        return self.score_tokens(self.tok.encode(t))

    def margin(self, ref, others, heard=""):
        """score(ref) - max(score of every other form, score of what free decoding wrote)."""
        ref_n = norm(ref)
        uniq = {}
        for o in others:
            o = o.replace("́", "").strip().lower()
            if o and norm(o) != ref_n:
                uniq.setdefault(norm(o), o)
        comp = [self.score(o) for o in uniq.values()]
        if heard and norm(heard) != ref_n:
            comp.append(self.score_raw(heard.strip()))
        if not comp:
            return float("inf")
        return self.score(ref.replace("́", "").strip().lower()) - max(comp)


def norm(t):
    return re.sub(r"\s+", " ", re.sub(r"[^\w\s-]", " ", t.lower().replace("ё", "е").replace("́", ""))).strip()
