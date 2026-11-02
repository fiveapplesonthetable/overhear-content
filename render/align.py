"""Word timing by MMS forced alignment (torchaudio MMS_FA), one sentence clip at a time.

Characters are romanised to the MMS alphabet, aligned with CTC, and each token (a notes `words[].t`, or a
whitespace token for narrator lines) takes the time of its first to last aligned letter. Starts then get a bounded
onset snap (<= snapMaxMs earlier, never before the previous word's end) because CTC places a letter at its peak
frame, a little after the acoustic onset.
"""
import unicodedata

import numpy as np

ROM_RU = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'ye', 'ё': 'yo', 'ж': 'j', 'з': 'z', 'и': 'i', 'й': 'y',
          'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f',
          'х': 'h', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'sh', 'ъ': '', 'ы': 'i', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
_LIG = {'œ': 'oe', 'æ': 'ae', 'ß': 'ss', 'ø': 'o', 'ł': 'l'}


def romanize_char(c, lang):
    """MMS letters for one character ('' when it has none)."""
    lc = c.lower()
    if lang == "ru":
        return ROM_RU.get(lc, "")
    if lc in _LIG:
        return _LIG[lc]
    if lc == "'" or lc == "’":
        return "'"
    d = unicodedata.normalize("NFD", lc)
    base = "".join(ch for ch in d if unicodedata.category(ch) != "Mn")
    return "".join(ch for ch in base if "a" <= ch <= "z")


class Aligner:
    def __init__(self, device="cpu"):
        import torch
        import torchaudio
        self.torch, self.ta = torch, torchaudio
        bundle = torchaudio.pipelines.MMS_FA
        self.device = device
        self.model = bundle.get_model(with_star=False).to(device).eval()
        self.dict = bundle.get_dict(star=None)
        self.sr = bundle.sample_rate

    def char_times(self, wav, sr, text, lang):
        """Per character of `text`: (t0, t1) seconds in the clip, or None. Also returns the 16 kHz signal."""
        torch, ta = self.torch, self.ta
        x = torch.from_numpy(np.asarray(wav, dtype=np.float32))[None]
        if sr != self.sr:
            x = ta.functional.resample(x, sr, self.sr)
        toks, owner = [], []
        for i, c in enumerate(text):
            for l in romanize_char(c, lang):
                if l in self.dict:
                    toks.append(self.dict[l])
                    owner.append(i)
        res = [None] * len(text)
        x_orig = x[0].numpy()
        if not toks:
            return res, x_orig
        min_frames = len(toks) + sum(1 for i in range(1, len(toks)) if toks[i] == toks[i - 1]) + 2
        min_samples = min_frames * 320 + 400
        x_in = torch.nn.functional.pad(x, (0, min_samples - x.shape[1])) if x.shape[1] < min_samples else x
        with torch.inference_mode():
            em, _ = self.model(x_in.to(self.device))
            if em.shape[1] < min_frames - 2:
                return res, x_orig
            al, sc = ta.functional.forced_align(em, torch.tensor([toks], dtype=torch.int32, device=self.device), blank=0)
        spans = ta.functional.merge_tokens(al[0].cpu(), sc[0].exp().cpu())
        if len(spans) != len(toks):
            return res, x_orig
        orig_dur = len(x_orig) / self.sr
        fr = x_in.shape[1] / self.sr / em.shape[1]
        for sp, ci in zip(spans, owner):
            a = min(orig_dur, sp.start * fr)
            b = min(orig_dur, max(a, sp.end * fr))
            old = res[ci]
            res[ci] = (a, b) if old is None else (min(old[0], a), max(old[1], b))
        return res, x_orig

    def word_times(self, wav, sr, text, lang, words):
        """Native-script timings for explicit lexical units, with whole-span reading ownership."""
        import native_text
        plan = native_text.targets(text, lang, words)
        torch, ta = self.torch, self.ta
        x = torch.from_numpy(np.asarray(wav, dtype=np.float32))[None]
        if sr != self.sr:
            x = ta.functional.resample(x, sr, self.sr)
        if any(letter not in self.dict for letter in plan.letters):
            raise native_text.NativeAlignmentError("native normalization and MMS alphabet disagree")
        tokens = [self.dict[letter] for letter in plan.letters]
        x_orig = x[0].numpy()
        min_frames = len(tokens) + sum(1 for i in range(1, len(tokens)) if tokens[i] == tokens[i - 1]) + 2
        min_samples = min_frames * 320 + 400
        x_in = torch.nn.functional.pad(x, (0, min_samples - x.shape[1])) if x.shape[1] < min_samples else x
        with torch.inference_mode():
            emission, _ = self.model(x_in.to(self.device))
            alignment, scores = ta.functional.forced_align(
                emission, torch.tensor([tokens], dtype=torch.int32, device=self.device), blank=0)
        spans = ta.functional.merge_tokens(alignment[0].cpu(), scores[0].exp().cpu())
        duration = len(x_orig) / self.sr
        return native_text.aggregate(plan, spans, duration / emission.shape[1], duration), x_orig


def envelope(x16, sr=16000, hop=0.005):
    """Frame RMS in dB."""
    h = int(sr * hop)
    n = len(x16) // h
    if n == 0:
        return np.zeros(1) - 120, hop
    f = x16[: n * h].reshape(n, h)
    return 20 * np.log10(np.sqrt((f ** 2).mean(1)) + 1e-9), hop


def snap_start(s, prev_end, env, hop, max_snap):
    """Move a word start earlier to the acoustic onset, at most `max_snap` seconds, not before `prev_end`."""
    lo = max(prev_end, s - max_snap, 0.0)
    if s <= lo + hop:
        return s
    i0 = int(s / hop)
    if i0 >= len(env):
        return s
    floor = np.percentile(env, 10)
    local_peak = env[i0: i0 + int(0.15 / hop) + 1].max()
    thr = max(floor + 8.0, local_peak - 30.0)
    if env[i0] < thr:
        return s
    i = i0
    while i > int(lo / hop) and env[i - 1] > thr:
        i -= 1
    return max(lo, i * hop)


def words_from_chars(char_times, spans, env=None, hop=0.005, snap_ms=120, end_ext=0.06):
    """spans: [(a, b) | None] char spans of tokens in the sentence text. -> [{s, e, ok, why}] (clip time)."""
    out = []
    for sp in spans:
        ct = [char_times[i] for i in range(*sp) if char_times[i] is not None] if sp else []
        if not ct:
            out.append({"s": None, "e": None, "ok": False, "why": "missing"})
        else:
            out.append({"s": min(c[0] for c in ct), "e": max(c[1] for c in ct), "ok": True, "why": ""})
    # fill missing tokens by interpolating between neighbours so the transcript still has monotonic times
    n = len(out)
    for i, w in enumerate(out):
        if w["s"] is None:
            left = next((out[j]["e"] for j in range(i - 1, -1, -1) if out[j]["e"] is not None), 0.0)
            right = next((out[j]["s"] for j in range(i + 1, n) if out[j]["s"] is not None), left)
            w["s"], w["e"] = left, max(left, right)
    prev_end = 0.0
    for i, w in enumerate(out):
        nxt = out[i + 1]["s"] if i + 1 < n else None
        if w["ok"]:
            if env is not None:
                w["s"] = snap_start(w["s"], prev_end, env, hop, snap_ms / 1000.0)
            w["e"] = w["e"] + end_ext
            if nxt is not None:
                w["e"] = min(w["e"], max(nxt, w["s"]))
        w["s"] = max(w["s"], prev_end if w["ok"] else w["s"])
        if w["ok"] and w["e"] - w["s"] < 0.005:
            w["ok"], w["why"] = False, "zero-length"
        prev_end = max(prev_end, w["e"])
    # starts were snapped using the unsnapped next start; make sure e<=next s after snapping
    for i in range(n - 1):
        if out[i]["e"] > out[i + 1]["s"]:
            out[i]["e"] = max(out[i]["s"], out[i + 1]["s"])
    return out
