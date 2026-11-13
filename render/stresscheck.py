"""Russian stress check on aligned sentence clips: vowel duration (the best of the three features in
stress-check/auto/summary.md: dur 84% on Silero, rms 59%, F0 50%).

For every word with a notes stress we know the intended vowel. Predicted = the longest vowel of the word (vowel
interval = the alignment peak centre +- min(60 ms, half the gap to the neighbouring letter), as in
stress-check/auto/check.py). A word is "off" when the predicted vowel differs and is >= `ratio` times longer than the
intended one. `scope` limits which words may flag a sentence: "homographs" (the words the model can really get
wrong) or "all". Everything is reported; only in-scope words flag.
"""
from textprep import ACUTE, bare, homographs, vowel_count

VOW = set("аеёиоуыэюя")


def _centres(char_times):
    return {i: (t[0] + t[1]) / 2 for i, t in enumerate(char_times) if t is not None}


def vowel_durations(char_times, text, a, b):
    cen = _centres(char_times)
    ks = sorted(cen)
    out = {}
    for i in range(a, b):
        if text[i].lower() in VOW and i in cen:
            p = [k for k in ks if k < i]
            q = [k for k in ks if k > i]
            c = cen[i]
            lo = c - min(0.06, (c - cen[p[-1]]) / 2) if p else c - 0.04
            hi = c + min(0.06, (cen[q[0]] - c) / 2) if q else c + 0.04
            out[i] = hi - lo
    return out


def check_sentence(plain, expected, char_times, scope="homographs", ratio=1.25):
    """expected: [(offset_in_plain, token, stress_form)]. Returns list of word results."""
    hom = homographs()
    res = []
    for off, tok, stress in expected:
        if vowel_count(tok) < 2 or "ё" in tok.lower():
            continue
        # intended vowel: the char before the mark inside `stress`, located in the token
        plain_s = stress.replace(ACUTE, "")
        low_t, low_p = tok.lower().replace("ё", "е"), plain_s.lower().replace("ё", "е")
        at = low_t.find(low_p)
        if at < 0:
            continue
        marks = [i - n - 1 for n, i in enumerate([k for k, c in enumerate(stress) if c == ACUTE])]
        exp_idx = [off + at + m for m in marks]
        dur = vowel_durations(char_times, plain, off, off + len(tok))
        if len(dur) < 2:
            continue
        have = [i for i in exp_idx if i in dur]
        if not have:
            continue
        exp = have[0]
        pred = max(dur, key=dur.get)
        off_by = pred != exp and dur[pred] >= ratio * max(dur[exp], 1e-3)
        in_scope = scope == "all" or bare(tok) in hom
        res.append({"word": tok, "stress": stress, "offset": off, "expected": exp - off, "predicted": pred - off,
                    "ratio": round(dur[pred] / max(dur[exp], 1e-3), 2), "off": bool(off_by), "inScope": bool(in_scope),
                    "flag": bool(off_by and in_scope)})
    return res
