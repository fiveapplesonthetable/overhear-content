"""GPU / audio steps of the narrator method (driven by narrator.py; each runs as its own process under gpurun).

  narrator_work.py en     --work DIR   F5-TTS v1 Base, voice sky: the English parts (venv-f5, settings ttsEn)
  narrator_work.py ru     --work DIR   Qwen3-TTS 1.7B + run3 stress LoRA, voice ru-f1: the Russian parts (venv-qwen)
  narrator_work.py check  --work DIR   Whisper (large-v3-turbo): each Russian part as Russian, each English part as English (ASR venv)
  narrator_work.py build  --work DIR   splice the winning takes into the stored scenes: audio, spans, timing, meta (ASR venv, CPU)

DIR holds plan.json (written by narrator.py), todo_{en,ru}.json, takes/<id>.t<k>.wav and checks.json.
"""
import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import time
import traceback
import unicodedata
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import config  # noqa: E402

NATIVE_SR = 24000
ENC_LAG = 119          # samples the limiter in audio.encode_mp3 delays the decoded signal by (tests/test_narrator.py pins it)
ATTEMPTS_BEFORE_STICKY = 2   # scene-wide failures (word times) that may be transient are remembered the 2nd time
MAX_TAKES = 64         # highest take index looked at per part (takesPerRound x rounds stays far below it)


class NarratorError(Exception):
    """An invariant of the splice broke (never an assert: those vanish under python -O)."""


class SceneSkip(Exception):
    """This scene is left as it is. sticky: the same inputs would fail again, so the failure is remembered per render key and version."""

    def __init__(self, why, sticky=True, lines=None, kind=None):
        super().__init__(why)
        self.why, self.sticky, self.kind = why, sticky, kind
        self.lines = lines          # [(seg, i)] the lines that caused it; the failure is remembered for these only (None: every line of the scene)
        # kind: a scene-wide failure that may be transient; it turns sticky when it has happened ATTEMPTS_BEFORE_STICKY times for this render


class LoudnessError(NarratorError):
    """A take cannot be brought to the level of the line it replaces within the gain / limiter budget."""


def log(*a):
    print(time.strftime("%H:%M:%S"), *a, file=sys.stderr, flush=True)


def seed_of(pid, k):
    return int(hashlib.sha256(pid.encode()).hexdigest()[:8], 16) + 7919 * k


def nz(t):
    t = unicodedata.normalize("NFC", unicodedata.normalize("NFD", t).replace("́", ""))
    t = re.sub(r"[^\w\s]", " ", t.lower().replace("’", "'").replace("ё", "е"))
    return re.sub(r"\s+", " ", t).strip()


def lev(a, b):
    d = list(range(len(b) + 1))
    for i in range(1, len(a) + 1):
        p, d[0] = d[:], i
        for j in range(1, len(b) + 1):
            d[j] = min(p[j] + 1, d[j - 1] + 1, p[j - 1] + (a[i - 1] != b[j - 1]))
    return d[len(b)]


def cer(ref, hyp):
    r, h = nz(ref), nz(hyp)
    return lev(r, h) / max(1, len(r))


def plausible_part(plain, seconds):
    """A short part (a word or two) is not a sentence: allow 0.12 s up to 0.45 s per character plus a second."""
    n = len(plain.strip())
    return 0.12 <= seconds <= 1.0 + 0.45 * n


def is_fragment(ref):
    """A line that quotes a Russian/Latin syllable or word (text inside double quotes, or a token ending in a hyphen) or has <= 6 words."""
    return '"' in ref or bool(re.search(r"\w-(?=[\s,.;:!?\"']|$)", ref)) or len(ref.split()) <= 6


def unquoted_words(ref):
    """The English words of a fragment line outside quotes, normalised (lowercase, no punctuation); hyphen-ending syllables are dropped."""
    t = re.sub(r'"[^"]*"', " ", ref)
    t = re.sub(r"\b\w+-(?=[\s,.;:!?\"']|$)", " ", t)
    return nz(t).split()


_ONES = "zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen".split()
_TENS = "_ _ twenty thirty forty fifty sixty seventy eighty ninety".split()


def num_words(n):
    """English words for 0 <= n < 10**9 ("20000" -> "twenty thousand"); Whisper writes spoken numbers as digits."""
    if n < 20:
        return _ONES[n]
    if n < 100:
        return _TENS[n // 10] + ("" if n % 10 == 0 else " " + _ONES[n % 10])
    if n < 1000:
        return _ONES[n // 100] + " hundred" + ("" if n % 100 == 0 else " " + num_words(n % 100))
    for k, w in ((10 ** 6, "million"), (1000, "thousand")):
        if n >= k:
            return num_words(n // k) + " " + w + ("" if n % k == 0 else " " + num_words(n % k))


def spell_numbers(t):
    """Digits (with thousands commas and a currency sign) to words, so "£20,000" matches "twenty thousand pounds"."""
    cur = {"£": "pounds", "$": "dollars", "€": "euros"}

    def one(m):
        n = int(m.group(2).replace(",", ""))
        return " " + (num_words(n) if n < 10 ** 9 else m.group(2)) + (" " + cur[m.group(1)] if m.group(1) else "") + " "
    return re.sub(r"([£$€]?)(\d{1,3}(?:,\d{3})+|\d+)", one, t)


# words Whisper drops or swallows at the edge of a clipped fragment ('is "X", and' -> "and"; "guest, and" -> "guest.")
EDGE_WORDS = {"and", "is", "a", "an", "the", "for", "on", "of", "to", "in", "or", "but", "so", "it"}


def sound_key(w):
    """A loose English sound key for a name: c/k/q/ck as k, ph as f, a final s/'s dropped, then vowels and h/w/y removed and
    doubles collapsed ("Ainura" = "newer", "Vika's" ~ "Vickers")."""
    w = re.sub(r"'s$|s$", "", w.lower())
    w = re.sub(r"ck|q|c(?![eiy])", "k", w).replace("ph", "f")
    return re.sub(r"(.)\1+", r"\1", re.sub(r"[aeiouyhw]", "", w))


def spelling_key(w):
    """Homophone spellings of one ordinary word: doubled letters collapsed and a final -ie/-ey/-y as one ending ("carry" = "Carrie")."""
    return re.sub(r"(ie|ey|y)$", "i", re.sub(r"(.)\1+", r"\1", w.lower()))


# short words Whisper writes as another spelling of the same sound ('"for"' heard "Four"/"4", "-u" heard "you", a non-rhotic
# '"or"' heard "awe", '"our"' heard "R")
HOMOPHONES = {"for": {"four", "fore"}, "or": {"awe", "oar", "ore"}, "our": {"are", "r", "hour"}, "to": {"two", "too"}, "too": {"to", "two"}, "u": {"you"}, "you": {"u"}, "be": {"bee"},
              "i": {"eye"}, "no": {"know"}, "by": {"bye", "buy"}}


def word_like(w, h, names):
    """An unquoted word heard as h: exact; the same homophone spelling; or, for a name of the script (capitalised there, >= 4
    letters), the same sound key (within one edit when it has three or more consonants). Ordinary words never match by sound alone (smile/small, turns/tons)."""
    if w == h or h in HOMOPHONES.get(w, ()) or (len(w) >= 4 and spelling_key(w) == spelling_key(h)):
        return True
    if w not in names or len(w) < 4 or not h:
        return False
    k1, k2 = sound_key(w), sound_key(h)
    return bool(k1) and lev(k1, k2) <= (1 if len(k1) >= 3 else 0)     # a two-consonant key must match exactly (Ainura/Kanra)


def in_order(words, hyp_words, names=None):
    """All words present in this order; with `names` (see `word_like`) a word may also match a homophone or a misheard name, and
    a word next to a name may run into it as one transcript word, matched by sound ("for Vika" heard "Favica")."""
    if names is None:
        it = iter(hyp_words)
        return all(w in it for w in words)
    i = j = 0
    while i < len(words):
        w = words[i]
        hit = next((n for n in range(j, len(hyp_words)) if word_like(w, hyp_words[n], names)), None)
        step = 1
        if hit is None and i + 1 < len(words) and {w, words[i + 1]} & names:
            both = w + words[i + 1]
            hit = next((n for n in range(j, len(hyp_words)) if word_like(both, hyp_words[n], {both})), None)
            step = 2
        if hit is None:
            return False
        i, j = i + step, hit + 1
    return True


def quotes_heard(ref, hyp_words):
    """Every quoted gloss or transliteration of the line ("I remember", "povtor") is heard: at least half of its words of >= 2
    letters match a transcript word, or two adjacent transcript words run together ("povtor" heard "Puff Tour"), by sound
    (`word_like` with every quoted word treated as a name). Quotes made only of hyphen syllables ("-sya") are left to the duration
    test. F5 sometimes skips a quoted gloss, leaving 'is "I remember", and' spoken as "is ... and"."""
    cands = list(hyp_words) + [a + b for a, b in zip(hyp_words, hyp_words[1:])]
    for q in re.findall(r'"([^"]*)"', ref):
        ws = [w for w in nz(re.sub(r"\b\w+-|-\w+\b", " ", q)).split() if len(w) >= 2]
        if ws and 2 * sum(1 for w in ws if any(word_like(w, h, set(ws)) for h in cands)) < len(ws):
            return False
    return True


def edge_trimmed(words):
    """The word list without the edge words Whisper may drop (EDGE_WORDS) at either end; at least one word is kept."""
    out = list(words)
    while len(out) > 1 and out[0] in EDGE_WORDS:
        out = out[1:]
    while len(out) > 1 and out[-1] in EDGE_WORDS:
        out = out[:-1]
    return out


_RU_PAIR = str.maketrans("бвгдзж", "пфктсш")


def ru_key(t):
    """Consonant skeleton of a short Russian word with voicing merged: Whisper writes a lone "же" as "Ж" and "мог" as "мок"."""
    return re.sub(r"[аеиоуыэюяйьъ\s]", "", nz(t)).translate(_RU_PAIR)


def syllable_key(t):
    """What a bare ending or prefix is judged on when Whisper answers in Cyrillic: its consonant skeleton (`ru_key`), for a vowel-only
    one (-а, -ое) its vowels with the hard / soft pairs merged (я=а, э=е, ы=и, ю=у)."""
    return ru_key(t) or nz(t).translate(str.maketrans("яэыю", "аеиу")).replace(" ", "")


def passes(kind, ref, hyp, cfg, syllable=False):
    """Whisper verdict for one take. Russian: CER on the Cyrillic; a one-word part of <= 4 letters (же, мог) may instead match on
    the consonant skeleton (voicing merged) when the transcript is Cyrillic. English: CER (digits in the transcript spelled out),
    or word recall for chunks of <= 3 words (Whisper drops a clipped trailing 'and'). English fragment lines (a quoted syllable or
    word, or <= 6 words): the unquoted English words must all be present in order in the transcript and each quote must be heard
    (`quotes_heard`); failing the first, the same with an edge word such as a trailing 'and' allowed missing and words of >= 4 letters (names)
    matched by sound. A Russian ending / prefix (`syllable`: -ла, пере) is too short for Whisper: unless it answers in Cyrillic with a
    different syllable, the take stands on the caller's duration test, like the quoted hyphen syllables of an English line.
    The duration test is made by the caller."""
    c = cer(ref, hyp)
    if kind == "ru" and syllable:
        return not re.search(r"[а-я]", nz(hyp)) or c <= cfg["ruCer"] or syllable_key(ref) == syllable_key(hyp), c
    if kind == "ru":
        r = nz(ref)
        if c > cfg["ruCer"] and len(r.split()) == 1 and len(r) <= 4 and re.search(r"[а-я]", nz(hyp)):
            return bool(ru_key(r)) and ru_key(r) == ru_key(hyp), c
        return c <= cfg["ruCer"], c
    sp = spell_numbers(hyp)
    rw, hw = nz(ref).split(), nz(sp).split()
    c = min(c, cer(ref, sp))
    if is_fragment(ref):
        uw = unquoted_words(ref)
        names = {nz(w) for w in re.findall(r"\b[A-Z][\w']*", re.sub(r'"[^"]*"', " ", ref))} - EDGE_WORDS
        if (not uw or in_order(uw, hw) or in_order(edge_trimmed(uw), hw, names)) and quotes_heard(ref, hw):
            return True, c
        # not in order: a take whose whole-line CER is within the English limit (a spelling variant such as favorite/favourite)
        # stays accepted unless the transcript is shorter by more than a letter (a dropped syllable: "attention" heard "tension");
        # the old word-recall shortcut for <= 3 words is not used for fragments (it let a dropped word through)
        return c <= cfg["enCer"] and len(nz(sp)) >= len(nz(ref)) - 1, c
    if len(rw) <= 3:
        rec = sum(1 for w in rw if w in hw) / max(1, len(rw))
        return (rec >= 0.66 and c <= 0.45), c
    return c <= cfg["enCer"], c


def trimmed_dur(path):
    """Speech duration of a take: the wave after the relative -42 dB edge trim (the raw F5 length is only its duration estimate)."""
    import soundfile as sf
    x, sr = sf.read(str(path), dtype="float32")
    x = x if x.ndim == 1 else x.mean(1)
    return len(trim_rel(x, sr)) / sr


def duration_ok(plain, tdur):
    """Fragment takes: trimmed speech of at least max(0.2 s, 0.04 s per character), i.e. the take is not a click or a swallowed
    word; the upper bound is `plausible_part`'s. F5's take lengths are quantised (1.76, 1.17, 0.58 ... s), so the earlier window
    around the median of same-length takes rejected correct takes ("the stove.", "is a debt.")."""
    return tdur is None or tdur >= max(0.2, 0.04 * len(plain.strip()))


# ---------------------------------------------------------------------------------------------------------------------
def take_speed(plain, k, speeds):
    """F5 speed of English take k: 1.0 for a full line; a fragment cycles through `speeds` (1.0, 0.85, 0.7, 0.55). At 1.0 F5 often
    swallows the quoted gloss of a short fragment ('is "loudly", and' spoken as "and") and every seed gives the same short take; a
    slower take keeps it. The lowest passing take wins, so the fastest speed that is heard right is used."""
    return speeds[k % len(speeds)] if is_fragment(plain) else 1.0


def stage_en(a):
    import copy
    import soundfile as sf
    from voices import Voices
    s = config.load_settings(a.settings)
    todo = json.loads((Path(a.work) / "todo_en.json").read_text("utf-8"))
    out = Path(a.work) / "takes"
    out.mkdir(exist_ok=True)
    voice = s["narratorRu"]["enVoice"]
    n = 0
    if not config.en_engine(s):
        from tts import QwenEngine
        nr = s["narratorRu"]
        sq = copy.deepcopy(s)
        sq["lora"]["enabled"] = False
        batch = int(nr.get("enBatch", sq["tts"].get("batchEn", 32)))
        sq["tts"]["batch"] = batch
        eng = QwenEngine(sq, Voices(), log=log)
        temps = nr["temperatures"]
        for k, chunk in ru_chunks(todo, batch):
            wavs = eng.generate([(voice, sq["tts"]["languages"]["en"], it["plain"]) for it in chunk],
                                seed_of(chunk[0]["id"], k), temps[k % len(temps)])
            for it, w in zip(chunk, wavs):
                sf.write(str(out / f"{it['id']}.t{k}.wav"), w, NATIVE_SR)
                n += 1
        print("OK " + json.dumps({"stage": "en", "takes": n}), flush=True)
        return
    from f5en import F5EnEngine
    import torch
    eng = F5EnEngine(s, Voices(), log=log)
    speeds = s["narratorRu"]["fragmentSpeeds"]
    for it in todo:
        for k in it["takes"]:
            torch.manual_seed(seed_of(it["id"], k))
            w = eng._single(voice, eng.text(it["text"]), take_speed(it["plain"], k, speeds))
            sf.write(str(out / f"{it['id']}.t{k}.wav"), w, NATIVE_SR)
            n += 1
    print("OK " + json.dumps({"stage": "en", "takes": n}), flush=True)


def ru_chunks(todo, batch):
    """[(take index k, [todo items])]: one chunk = one take index, because the seed and temperature are per generate() call. Takes 0 and 1
    of one part therefore never share a draw. Within a take index the items go by text length (batches of similar length)."""
    by_k = {}
    for it in todo:
        for k in it["takes"]:
            by_k.setdefault(k, []).append(it)
    bs = max(1, int(batch))
    out = []
    for k in sorted(by_k):
        items = sorted(by_k[k], key=lambda it: len(it["text"]))
        out += [(k, items[i:i + bs]) for i in range(0, len(items), bs)]
    return out


def stage_ru(a):
    import copy
    import numpy as np
    import soundfile as sf
    from voices import Voices
    from tts import QwenEngine
    s = config.load_settings(a.settings)
    nr = s["narratorRu"]
    s = copy.deepcopy(s)
    s["lora"]["enabled"] = bool(nr.get("lora", True))   # narrator-specific: the run3 stress LoRA (marks on every word); the global lora.enabled stays as it is
    s["tts"]["batch"] = nr["ruBatch"]
    todo = json.loads((Path(a.work) / "todo_ru.json").read_text("utf-8"))
    eng = QwenEngine(s, Voices(), log=log)
    out = Path(a.work) / "takes"
    out.mkdir(exist_ok=True)
    n = 0
    temps = nr["temperatures"]
    for k, chunk in ru_chunks(todo, nr["ruBatch"]):
        wavs = eng.generate([(nr["ruVoice"], s["tts"]["languages"]["ru"], it["text"] + ".") for it in chunk],
                            seed_of(chunk[0]["id"], k), temps[k % len(temps)])
        for it, w in zip(chunk, wavs):
            sf.write(str(out / f"{it['id']}.t{k}.wav"), w, NATIVE_SR)
            n += 1
    print("OK " + json.dumps({"stage": "ru", "takes": n}), flush=True)


def load16(path):
    import numpy as np
    import soundfile as sf
    import scipy.signal as ss
    x, sr = sf.read(str(path), dtype="float32")
    x = x if x.ndim == 1 else x.mean(1)
    return ss.resample_poly(x, 16000, sr).astype("float32") if sr != 16000 else x


def stage_check(a):
    import soundfile as sf
    from faster_whisper import WhisperModel
    import gates
    g = gates.get_gates()
    from voices import Voices
    v = Voices.load(s["voices"])
    
    s = config.load_settings(a.settings)
    nr = s["narratorRu"]
    work = Path(a.work)
    plan = json.loads((work / "plan.json").read_text("utf-8"))
    checks_p = work / "checks.json"
    checks = json.loads(checks_p.read_text("utf-8")) if checks_p.exists() else {}
    parts = {p["id"]: p for p in plan["parts"]}
    
    for tid, c in checks.items():      # speech duration of every stored take (once)
        if "tdur" not in c and (work / "takes" / f"{tid}.wav").exists():
            c["tdur"] = round(trimmed_dur(work / "takes" / f"{tid}.wav"), 3)
            
    for tid, c in checks.items():      # re-judge stored hypotheses with the current rules
        p = parts.get(tid.rsplit(".t", 1)[0])
        if p:
            frag = p.get("syllable") or (p["kind"] == "en" and is_fragment(p["plain"]))
            c["plausible"] = plausible_part(p["plain"], c["dur"]) and (duration_ok(p["plain"], c.get("tdur")) if frag else True)
            c["pass"] = bool(passes(p["kind"], p["plain"], c["hyp"], nr, p.get("syllable", False))[0] and c["plausible"])
            c["via"] = (p.get("run") or {}).get("via")
            
    m = WhisperModel("large-v3-turbo", device="cuda", compute_type="float16")
    n = 0
    for f in sorted((work / "takes").glob("*.wav")):
        tid = f.stem                      # <partid>.t<k>
        if tid in checks:
            continue
        pid = tid.rsplit(".t", 1)[0]
        p = parts.get(pid)
        if not p:
            continue
        dur = sf.info(str(f)).duration
        wav, sr = sf.read(str(f))
        
        c = {"dur": round(dur, 3), "tdur": round(trimmed_dur(f), 3)}
        
        # New gates check
        voice_id = s["narratorRu"]["ruVoice"] if p["kind"] == "ru" else "sky"
        ref_path = v.ref_path(voice_id)
        
        sim_ok, sim_val = g.check_similarity(wav, sr, ref_path)
        len_ok, len_reason = g.check_length_pause(wav, sr, p["plain"], p["kind"])
        tran_ok, tran_reason, wav = g.check_transient(wav, sr)
        rep_ok, cer_val, hyp = g.check_repeat_and_cer(wav, sr, p["plain"], p["kind"])
        
        c["hyp"] = hyp
        c["cer"] = cer_val if isinstance(cer_val, float) else 1.0
        
        # We replace the original whisper check with the gates check since it uses Whisper under the hood.
        # But for passes(), we still evaluate the old rules alongside gates.
        
        frag = p.get("syllable") or (p["kind"] == "en" and is_fragment(p["plain"]))
        c["plausible"] = plausible_part(p["plain"], c["dur"]) and (duration_ok(p["plain"], c.get("tdur")) if frag else True)
        
        old_pass, _ = passes(p["kind"], p["plain"], hyp, nr, p.get("syllable", False))
        gates_pass = sim_ok and len_ok and tran_ok and rep_ok
        
        c["pass"] = bool(old_pass and c["plausible"] and gates_pass)
        
        if p.get("run"):
            c["via"] = p["run"].get("via")
            
        checks[tid] = c
        n += 1
        
    if n > 0:
        checks_p.write_text(json.dumps(checks, ensure_ascii=False, indent=1), "utf-8")
    log(f"checked {n} new takes")
    print("OK " + json.dumps({"stage": "check", "checked": n}), flush=True)


# ---- build -----------------------------------------------------------------------------------------------------------
def trim_rel(x, sr, db=-42.0, margin=0.02):
    import numpy as np
    fr = int(0.01 * sr)
    n = len(x) // fr
    if n == 0:
        return x
    e = np.sqrt((x[:n * fr].reshape(n, fr) ** 2).mean(1) + 1e-12)
    idx = np.where(e > e.max() * 10 ** (db / 20))[0]
    if not len(idx):
        return x
    a0, b0 = max(0, idx[0] * fr - int(margin * sr)), min(len(x), (idx[-1] + 1) * fr + int(margin * sr))
    y = x[a0:b0].copy()
    f = min(int(0.008 * sr), len(y) // 2)
    if f:
        y[:f] *= np.linspace(0, 1, f, dtype=y.dtype)
        y[-f:] *= np.linspace(1, 0, f, dtype=y.dtype)
    return y


def act_rms(x, sr):
    import numpy as np
    fr = int(0.02 * sr)
    n = max(1, len(x) // fr)
    e = np.sqrt((x[:n * fr].reshape(n, -1) ** 2).mean(1) + 1e-12)
    m = e > e.max() * 10 ** (-30 / 20)
    return float(np.sqrt((e[m] ** 2).mean()))


def compose(job, takes, nr, sr, rng):
    """job parts + chosen take waves -> (signal, [(start_s, end_s) per part]) with 150-250 ms gaps and matched part levels."""
    import numpy as np
    pieces = [trim_rel(w, sr) for w in takes]
    ens = [act_rms(p, sr) for p, part in zip(pieces, job["parts"]) if part["kind"] == "en"]
    ref = float(np.median(ens)) if ens else act_rms(pieces[0], sr)
    out, offs, pos = [], [], 0
    for i, (p, part) in enumerate(zip(pieces, job["parts"])):
        p = (p * (ref / act_rms(p, sr))).astype("float32")
        out.append(p)
        offs.append((pos / sr, (pos + len(p)) / sr))
        pos += len(p)
        if i < len(pieces) - 1:
            g = int(rng.uniform(nr["gapMs"][0], nr["gapMs"][1]) / 1000 * sr)
            out.append(np.zeros(g, dtype="float32"))
            pos += g
    return np.concatenate(out), offs


def distribute(job, offs, tok_spans):
    """Word times of the new sentence from the known part offsets: tokens of a part share its span by syllable / letter weight."""
    import narrator_ru as N
    parts = job["parts"]
    owner = N.token_parts(job["text"], parts, tok_spans)
    times = [None] * len(tok_spans)
    for pi, part in enumerate(parts):
        idx = [i for i, o in enumerate(owner) if o == pi]
        if not idx:
            continue
        a0, b0 = offs[pi]
        if part["kind"] == "ru" and len(part["run"]["cyr"]) == len(idx):
            w = [N.vowels(c) for c in part["run"]["cyr"]]
        else:
            w = [max(1, sum(ch.isalpha() for ch in job["text"][tok_spans[i][0]:tok_spans[i][1]])) for i in idx]
        tot, cur = float(sum(w)), a0
        for i, wi in zip(idx, w):
            e = cur + (b0 - a0) * wi / tot
            times[i] = (cur, e)
            cur = e
    prev = 0.0
    for i, t in enumerate(times):          # tokens of no part (cannot happen, but never leave a hole)
        if t is None:
            times[i] = (prev, prev)
        prev = times[i][1]
    return times


def shift_doc(spans, timing, old_e, d):
    """Everything at or after old_e moves by d seconds (unrounded: callers round once at the end, so edits do not accumulate error)."""
    for g in spans["segs"]:
        for k in ("start", "end", "nextStart"):
            if g[k] >= old_e - 1e-6:
                g[k] = g[k] + d
        for q in g["sentences"]:
            for k in ("start", "end"):
                if q[k] >= old_e - 1e-6:
                    q[k] = q[k] + d
    for k, ws in timing.items():
        for w in ws:
            for f in ("s", "e"):
                if w[f] >= old_e - 1e-6:
                    w[f] = w[f] + d
    spans["durationSec"] = spans["durationSec"] + d


def round_docs(spans, timing):
    for g in spans["segs"]:
        for k in ("start", "end", "nextStart"):
            g[k] = round(g[k], 3)
        for q in g["sentences"]:
            q["start"], q["end"] = round(q["start"], 3), round(q["end"], 3)
    for ws in timing.values():
        for w in ws:
            w["s"], w["e"] = round(w["s"], 3), round(w["e"], 3)
    spans["durationSec"] = round(spans["durationSec"], 3)


def decode_mp3(path, sr):
    import numpy as np
    r = subprocess.run(["ffmpeg", "-v", "error", "-i", str(path), "-f", "f32le", "-ac", "1", "-ar", str(sr), "-"], capture_output=True)
    if r.returncode != 0 or not r.stdout:
        raise NarratorError(f"cannot decode {path}: {r.stderr.decode(errors='replace')[-200:]}")
    return np.frombuffer(r.stdout, dtype=np.float32).copy()


def quiet_point(sig, lo, hi, anchor, f, after):
    """A cut position p in [lo, hi] where the signal is nearly silent: the lowest RMS over the f samples after p (after=True; for the
    left join) or before p (the right join). Among positions within 2x of the quietest (and 0.2 mRMS) the one closest to `anchor`
    wins, so the gap is kept as long as possible."""
    import numpy as np
    n = len(sig)
    lo, hi = (max(lo, 0), min(hi, n - f)) if after else (max(lo, f), min(hi, n))
    if hi < lo:
        return int(min(max(anchor, 0), n))
    cs = np.concatenate([[0.0], np.cumsum(sig.astype(np.float64) ** 2)])
    p = np.arange(lo, hi + 1)
    e = (cs[p + f] - cs[p]) if after else (cs[p] - cs[p - f])
    rms = np.sqrt(e / f)
    m = float(rms.min())
    ok = np.where(rms <= max(m * 2.0, m + 2e-4))[0]
    return int(p[ok[np.argmin(np.abs(p[ok] - anchor))]])


ENC_LIMITS = (0.90, 0.794, 0.708, 0.631, 0.562)     # encoder ceilings for a rebuilt scene: the decoded original already peaks near 0.89 (limiter -2 dB + mp3 overshoot)
GAIN_CLAMP_DB = 1.0    # the most the scene-wide generation-loss correction may move the whole scene
LIMIT = 0.88           # ceiling of the line limiter, just under the first encoder ceiling


def limit_peaks(x, ceiling=LIMIT, sr=24000, ms=5.0):
    """Smooth look-ahead peak limiter: the gain needed at each sample, minimum-filtered over +-ms and box-smoothed over the same width, so the
    smoothed gain never exceeds the gain any sample needs (no overshoot) and has no steps (no clicks)."""
    import numpy as np
    from scipy.ndimage import minimum_filter1d, uniform_filter1d
    x = np.asarray(x, dtype=np.float32)
    w = max(3, int(sr * ms / 1000) * 2 + 1)
    need = np.minimum(1.0, ceiling / np.maximum(np.abs(x), 1e-9)).astype(np.float64)
    g = uniform_filter1d(minimum_filter1d(need, w, mode="nearest"), w, mode="nearest")
    return (x * g).astype(np.float32)


def match_loudness(y, ref, sr, iters=5, max_gain_db=12.0, max_limit_db=3.0):
    """y scaled so that its loudness AFTER the peak limiter equals the loudness of `ref` (the line it replaces). A peaky TTS line
    that is only scaled to the reference loudness and then limited ends up 1-4 dB quieter than the original narrator audio.
    Raises LoudnessError when that needs more than `max_gain_db` of gain or makes the limiter take more than `max_limit_db` off
    (a silent or garbage take would otherwise be boosted into noise)."""
    import numpy as np
    import audio
    lo, ln = audio.lufs(ref, sr), audio.lufs(y, sr)
    if not (np.isfinite(lo) and np.isfinite(ln)):
        raise LoudnessError(f"loudness of the take ({ln}) or of the line it replaces ({lo}) is not measurable")
    g = 10 ** ((lo - ln) / 20)
    z = pre = None
    for _ in range(iters):
        if 20 * np.log10(g) > max_gain_db:
            raise LoudnessError(f"the take needs {20 * np.log10(g):+.1f} dB of gain (limit {max_gain_db:g} dB)")
        pre = y * np.float32(g)
        z = limit_peaks(pre, sr=sr)
        d = lo - audio.lufs(z, sr)
        if abs(d) < 0.05:
            break
        g *= 10 ** (d / 20)
    red = audio.lufs(pre, sr) - audio.lufs(z, sr)
    if red > max_limit_db:
        raise LoudnessError(f"the limiter takes {red:.1f} dB off the take (limit {max_limit_db:g} dB)")
    return z


def splice(sig, y, cl, cr, f):
    """sig[cl:cr] -> y, with an equal-power crossfade of f samples at both joins. The fades run INSIDE the replaced region (old audio
    sig[cl:cl+f] against y[:f], y[-f:] against sig[cr-f:cr]), so sig[:cl] and sig[cr:] are untouched, the first/last output sample of
    each join equals the old neighbour, and the length is exactly len(sig) - (cr - cl) + len(y). Cut at near-silent points (quiet_point)."""
    import numpy as np
    y = np.asarray(y, dtype=np.float32)
    n = len(y)
    f = int(max(0, min(f, n // 2, cr - cl)))
    out = np.concatenate([sig[:cl], y, sig[cr:]]).astype(np.float32)
    if f:
        t = (np.arange(1, f + 1, dtype=np.float64) / (f + 1)) * (np.pi / 2)
        w_in, w_out = np.sin(t).astype(np.float32), np.cos(t).astype(np.float32)
        out[cl:cl + f] = sig[cl:cl + f] * w_out + y[:f] * w_in
        out[cl + n - f:cl + n] = y[n - f:] * w_out + sig[cr - f:cr] * w_in
    return out


def verify_tokens(g, tl, narrator):
    """None when the segment's timing tokens are exactly the sentences' tokens in order (so the per-sentence slices line up with the
    spans); else the reason. A token that moved across a sentence boundary keeps the total equal but fails here."""
    exp = [narrator.seg_tokens(x["text"]) for x in g["sentences"]]
    got = [w["t"] for w in tl]
    if sum(len(e) for e in exp) != len(got):
        return f"token count {sum(len(e) for e in exp)} != timing {len(got)}"
    pos = 0
    for x, e in zip(g["sentences"], exp):
        if got[pos:pos + len(e)] != e:
            return f"timing tokens do not line up with the sentence tokens at sentence {x['i']}"
        pos += len(e)
    return None


def neighbours(spans, q):
    """(end of the previous sentence, start of the next one) in seconds, over all segments."""
    others = [(x["start"], x["end"]) for g in spans["segs"] for x in g["sentences"] if x is not q]
    prev_end = max([e for s, e in others if e <= q["start"] + 1e-6] or [0.0])
    next_start = min([s for s, e in others if s >= q["end"] - 1e-6] or [spans["durationSec"]])
    return prev_end, next_start


def ensure_original(store, sid, dry):
    """-> (base dir, live meta). The pristine render the splice is built from, kept at <store>/.narrator-before/<sid> keyed to the live
    renderKey: refreshed whenever the live scene is a newer render, never taken from a narrated scene."""
    import narrator
    from store import sha256_file, exchange_dirs
    d, lm, note = narrator.original_dir(store.root, sid)
    if d is None:
        raise SceneSkip(note, sticky=False)
    before = store.root / ".narrator-before" / sid
    bm = narrator._read(before / "meta.json") or {}
    if note == "live" and (bm.get("renderKey"), bm.get("audioSha256"), bm.get("narratorRu")) == (lm.get("renderKey"), lm.get("audioSha256"), None) \
            and sha256_file(before / "audio.mp3") == lm.get("audioSha256"):
        return before, lm                         # the before-copy is already this render
    if note == "live" and not dry:                # live and pristine: (re)make the before-copy
        tmp = before.parent / f".{sid}.tmp.{os.getpid()}"
        before.parent.mkdir(parents=True, exist_ok=True)
        shutil.rmtree(tmp, ignore_errors=True)
        try:
            shutil.copytree(d, tmp)
            if sha256_file(tmp / "audio.mp3") != lm.get("audioSha256"):
                raise SceneSkip("live audio does not match its meta audioSha256", sticky=False)
            if before.exists():
                if not exchange_dirs(tmp, before):        # atomic: a valid before-copy exists at every instant
                    old = before.parent / f".{sid}.old.{os.getpid()}"
                    before.rename(old)
                    tmp.rename(before)
                    shutil.rmtree(old, ignore_errors=True)
                else:
                    shutil.rmtree(tmp, ignore_errors=True)    # tmp now holds the previous copy
            else:
                tmp.rename(before)
        except BaseException:                          # SceneSkip, OSError (disk full), anything: no half copy is left behind
            shutil.rmtree(tmp, ignore_errors=True)
            raise
        d = before
    return d, lm


class RegionLoudness(Exception):
    """Replaced lines that came out off the level of the audio they replaced; the scene is built again without them."""

    def __init__(self, lines, why):
        super().__init__(why)
        self.lines, self.why = lines, why


def build_scene(a, s, store, sc, work, checks, res, fails):
    """Splice one scene from its original render and commit it (or write it to --out). Raises SceneSkip. A line whose region comes out off
    the level of the audio it replaced keeps its sky audio (sticky failure for that line) and the scene is built again without it."""
    skip = set()
    for _ in range(3):
        lres, lfails = {"scenes": 0, "lines": 0, "loudnessLU": {}}, []
        try:
            r = _build_scene(a, s, store, sc, work, checks, lres, lfails, skip)
        except RegionLoudness as e:
            for j in sc["jobs"]:
                if (j["seg"], j["i"]) in e.lines:
                    fails.append({"scene": sc["scene"], "seg": j["seg"], "i": j["i"], "text": j["text"], "why": e.why, "sticky": True,
                                  "sig": j["sig"], "renderKey": sc["renderKey"]})
            skip |= set(e.lines)
            continue
        except BaseException:
            fails.extend(lfails)
            raise
        fails.extend(lfails)
        res["scenes"] += lres["scenes"]
        res["lines"] += lres["lines"]
        res.setdefault("loudnessLU", {}).update(lres["loudnessLU"])
        return r
    raise SceneSkip("loudness: replaced lines still off the original level after dropping the bad ones", sticky=False)


def _build_scene(a, s, store, sc, work, checks, res, fails, skip):
    import numpy as np
    import random
    import audio
    import narrator
    from store import sha256_file, flock_ctx, LockTimeout
    import soundfile as sf
    nr = s["narratorRu"]
    sr = s["audio"]["sampleRate"]
    A = ENC_LAG
    F = int(round(nr.get("crossfadeMs", 8) / 1000 * sr))
    win, small = int(0.06 * sr), int(0.01 * sr)
    sid = sc["scene"]
    live = store.scene_dir(sid)
    base, lm0 = ensure_original(store, sid, bool(a.out))
    if lm0.get("renderKey") != sc.get("renderKey"):
        raise SceneSkip("the scene was re-rendered since the plan was made; run again", sticky=False)
    key0 = (lm0.get("renderKey"), lm0.get("audioSha256"))
    jr = lambda n: json.loads((base / n).read_text("utf-8"))
    spans, timing, meta, report = jr("spans.json"), jr("timing.json"), jr("meta.json"), jr("report.json")
    base_sig = decode_mp3(base / "audio.mp3", sr)
    sig = base_sig
    done = []
    regions = []
    seen = set()
    for job in sorted(sc["jobs"], key=lambda j: j["start"]):
        if (job["seg"], job["i"]) in seen or (job["seg"], job["i"]) in skip:
            continue              # a line is spliced once, whatever a (concurrent or repeated) plan says
        seen.add((job["seg"], job["i"]))
        why, chosen = None, []
        for part in job["parts"]:
            ok = [k for k in range(MAX_TAKES) if checks.get(f"{part['id']}.t{k}", {}).get("pass")]
            if not ok:
                why = f"no take of part {part['id']} ({part['kind']}: {part['plain']!r}) passed Whisper"
                break
            chosen.append(ok[0])
        g = next((g for g in spans["segs"] if g["seg"] == job["seg"]), None)
        q = next((q for q in g["sentences"] if q["i"] == job["i"]), None) if g else None
        if not why and q is None:
            why = "sentence not found in the scene's spans"
        if not why and q["text"] != job["text"]:
            why = "sentence text differs from the plan"
        tl = timing.get(str(job["seg"])) if not why else None
        if not why:
            why = verify_tokens(g, tl, narrator)
        if why:
            fails.append({"scene": sid, "seg": job["seg"], "i": job["i"], "text": job["text"], "why": why, "sticky": True, "sig": job["sig"],
                          "renderKey": sc["renderKey"]})
            continue
        ws = [sf.read(str(work / "takes" / f"{p['id']}.t{k}.wav"), dtype="float32")[0] for p, k in zip(job["parts"], chosen)]
        y, offs = compose(job, ws, nr, sr, random.Random(job["parts"][0]["id"]))
        # spans.json times are on the stored file's timeline; the decoded signal is ENC_LAG samples later (the limiter's look-ahead)
        S, E = int(round(q["start"] * sr)) + A, int(round(q["end"] * sr)) + A
        pe, ns = neighbours(spans, q)
        cl = quiet_point(sig, int(round(pe * sr)) + A, S + small, S, F, after=True)
        cr = quiet_point(sig, E - small, min(len(sig), int(round(ns * sr)) + A, E + win), E, F, after=False)
        if not (0 <= cl < cr <= len(sig)):
            fails.append({"scene": sid, "seg": job["seg"], "i": job["i"], "text": job["text"], "why": f"no cut points ({cl}, {cr})",
                          "sticky": True, "sig": job["sig"], "renderKey": sc["renderKey"]})
            continue
        ref = sig[S:E].copy()
        try:
            y = match_loudness(y, ref, sr, max_gain_db=float(nr.get("maxGainDb", 12.0)), max_limit_db=float(nr.get("maxLimiterDb", 3.0)))
        except LoudnessError as e:
            fails.append({"scene": sid, "seg": job["seg"], "i": job["i"], "text": job["text"], "why": f"loudness: {e}", "sticky": True,
                          "sig": job["sig"], "renderKey": sc["renderKey"]})
            continue
        counts = [len(narrator.seg_tokens(x["text"])) for x in g["sentences"]]
        si = g["sentences"].index(q)
        t0 = sum(counts[:si])
        toks = [w["t"] for w in tl[t0:t0 + counts[si]]]
        tsp = narrator.token_char_spans(job["text"], toks)
        if any(t is None for t in tsp):
            fails.append({"scene": sid, "seg": job["seg"], "i": job["i"], "text": job["text"], "why": "token not found in sentence text",
                          "sticky": True, "sig": job["sig"], "renderKey": sc["renderKey"]})
            continue
        wt = distribute(job, offs, tsp)
        old_s, old_e = q["start"], q["end"]
        first = si == 0 and abs(g["start"] - old_s) < 1e-6
        last = si == len(g["sentences"]) - 1 and abs(g["end"] - old_e) < 1e-6
        out = splice(sig, y, cl, cr, F)
        regions.append(((job["seg"], job["i"]), cl, len(y), ref))      # later splices are all after this one: [cl, cl + len(y)) stays valid
        dsec = (len(out) - len(sig)) / sr
        sig = out
        shift_doc(spans, timing, old_e, dsec)
        new_s, new_e = (cl - A) / sr, (cl + len(y) - A) / sr          # the new audio of this sentence occupies [cl, cl + len(y))
        for g2 in spans["segs"]:
            if first and abs(g2["nextStart"] - old_s) < 1e-6 and g2 is not g:
                g2["nextStart"] = new_s
        q["start"], q["end"] = new_s, new_e
        if first:
            g["start"] = new_s
        if last:
            g["end"] = new_e
        q["engine"] = "f5-tts+qwen3-tts"
        for w, (ts, te) in zip(tl[t0:t0 + counts[si]], wt):
            w["s"], w["e"], w["ok"], w["why"] = new_s + ts, new_s + te, True, "part-offsets"
        done.append({"seg": job["seg"], "i": job["i"], "sig": job["sig"], "version": nr["version"],
                     "oldSec": round(old_e - old_s, 3), "newSec": round(len(y) / sr, 3),
                     "joins": [round((cl - A) / sr, 4), round((cl + len(y) - A) / sr, 4)],      # the two splice points on the NEW timeline
                     "parts": [{"kind": p["kind"], "text": p["plain"], "take": k} for p, k in zip(job["parts"], chosen)]})
        res["lines"] += 1
    live_narrated = bool((_json(live / "meta.json") or {}).get("narratorRu"))
    if not done and not live_narrated:
        return False                          # nothing to splice and nothing to take back
    jb = lambda o: (json.dumps(o, ensure_ascii=False, sort_keys=True, indent=1) + "\n").encode("utf-8")
    if a.out:
        outd = Path(a.out)
        outd.mkdir(parents=True, exist_ok=True)
        tmp = outd / f"{sid}.mp3"
    else:
        tmp = store.root / f".{sid}.narr.{os.getpid()}.mp3"
    try:
        if not done:                          # lines that no longer qualify: put the original back, byte for byte
            spans_b, timing_b, meta_b, report_b = ((base / n).read_bytes() for n in ("spans.json", "timing.json", "meta.json", "report.json"))
            tmp = base / "audio.mp3"
        else:
            round_docs(spans, timing)
            # audio.encode_mp3's limiter delays the decoded stream by ENC_LAG samples; the original already has that delay once, so feed
            # the encoder the signal ENC_LAG early: the new file keeps the original's timeline exactly. Every decode/encode generation costs
            # about 0.45 LU: measure the scene's loss and give it back as one uniform gain, clamped to +-1 dB (untouched dialogue and the
            # new lines move together). Loudness is then checked per replaced region, against the audio that region replaced.
            l0 = audio.lufs(base_sig, sr)
            gain, gmax = 1.0, 10 ** (GAIN_CLAMP_DB / 20)
            for attempt in range(3):
                audio.encode_mp3(np.concatenate([(sig * np.float32(gain))[A:], np.zeros(A, dtype=np.float32)]), sr, tmp, s["audio"]["mp3Kbps"], ENC_LIMITS)
                dec = decode_mp3(tmp, sr)
                l1 = audio.lufs(dec, sr)
                if not (np.isfinite(l0) and np.isfinite(l1)) or abs(l0 - l1) <= 0.1 or attempt == 2:
                    break
                gain = float(np.clip(gain * 10 ** ((l0 - l1) / 20), 1 / gmax, gmax))
            dur_mp3 = audio.mp3_duration(tmp, sr)
            if abs(dur_mp3 - len(sig) / sr) >= 0.05:
                raise SceneSkip(f"encoded length {dur_mp3:.3f}s != spliced length {len(sig) / sr:.3f}s", sticky=False)
            for k, ws_ in timing.items():
                for w1, w2 in zip(ws_, ws_[1:]):
                    if w2["s"] < w1["s"] - 1e-6:
                        raise SceneSkip(f"word times not monotonic in seg {k}: {w1} then {w2}", sticky=False, kind="monotonic")
            last_e = max((w["e"] for ws_ in timing.values() for w in ws_), default=0)
            if last_e > dur_mp3 + 0.05:
                raise SceneSkip(f"word times run past the audio ({last_e:.3f}s > {dur_mp3:.3f}s)", sticky=False, kind="past-audio")
            tol = float(nr.get("lineLoudnessTolLU", 1.5))
            bad, drift, prev_end = [], [], 0
            for key, cl_, n_, ref_ in regions:
                lo_ = max(cl_, prev_end)                     # a region never counts the tail of the one before it
                prev_end = cl_ + n_
                a_, b_ = audio.lufs(ref_, sr), audio.lufs(dec[lo_:cl_ + n_], sr)
                if np.isfinite(a_) and np.isfinite(b_):
                    drift.append(round(float(b_ - a_), 2))
                    if abs(b_ - a_) > tol:
                        bad.append((key, float(b_ - a_)))
            if bad:
                raise RegionLoudness({k for k, _ in bad}, "replaced line off the original level after encoding: "
                                     + ", ".join(f"{d:+.2f} LU" for _, d in bad) + f" (limit {tol} LU)")
            res.setdefault("loudnessLU", {})[sid] = {"scene": round(float(l1 - l0), 3) if np.isfinite(l0) and np.isfinite(l1) else None,
                                                     "gainDb": round(20 * float(np.log10(gain)), 2), "lines": drift}
            meta["narratorRu"] = {"version": nr["version"], "ruVoice": nr["ruVoice"], "enVoice": nr["enVoice"], "lora": s["lora"]["tag"],
                                  "lines": done, "renderedAt": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
            meta["durationSec"] = round(len(sig) / sr, 3)
            meta["audioSha256"], meta["audioBytes"] = sha256_file(tmp), tmp.stat().st_size
            spans_b, timing_b = jb(spans), jb(timing)
            meta["spansSha256"], meta["timingSha256"] = config.sha(spans_b), config.sha(timing_b)
            report["narratorRu"] = {"lines": len(done), "failedThisRun": [f for f in fails if f["scene"] == sid]}
            report.setdefault("audio", {})["seconds"] = round(len(sig) / sr, 3)
            report["audio"]["mp3Seconds"] = round(dur_mp3, 3)
            meta_b, report_b = jb(meta), jb(report)
        if a.out:
            (Path(a.out) / f"{sid}.spans.json").write_bytes(spans_b)
            (Path(a.out) / f"{sid}.timing.json").write_bytes(timing_b)
            (Path(a.out) / f"{sid}.meta.json").write_bytes(meta_b)
        else:
            # the publisher reads scenes under publish.lock: take it for the commit only, and look again at the live scene first
            try:
                with flock_ctx(config.PUBLISH_LOCK, timeout=float(nr.get("publishLockWaitSec", 3600))):
                    lm = _json(live / "meta.json") or {}
                    if (lm.get("renderKey"), lm.get("audioSha256")) != key0:
                        raise SceneSkip("the scene changed while the narrator was working (renderKey/audioSha256); nothing committed", sticky=False)
                    store.commit_scene(sid, {"audio.mp3": tmp, "spans.json": spans_b, "timing.json": timing_b,
                                             "report.json": report_b, "meta.json": meta_b})
            except LockTimeout as e:
                raise SceneSkip(f"publish.lock busy: {e}", sticky=False)
    finally:
        if done and not a.out:
            Path(tmp).unlink(missing_ok=True)
    res["scenes"] += 1
    return True


def _json(p):
    try:
        return json.loads(Path(p).read_text("utf-8"))
    except Exception:
        return None


def stage_build(a):
    from store import Store
    import narrator
    s = config.load_settings(a.settings)
    work = Path(a.work)
    plan = json.loads((work / "plan.json").read_text("utf-8"))
    checks = _json(work / "checks.json") or {}
    store = Store(a.store)
    res = {"scenes": 0, "lines": 0, "failed": 0}
    fails = []
    attempts_p = work / "attempts.json"
    attempts = _json(attempts_p) or {}
    for sc in plan["scenes"]:
        try:
            build_scene(a, s, store, sc, work, checks, res, fails)
        except SceneSkip as e:
            culprit = [j for j in sc["jobs"] if e.lines is None or (j["seg"], j["i"]) in e.lines]
            if e.kind and not e.sticky and not a.out:     # a scene-wide failure that might be transient: the second time for this render it is final
                k = f"{sc['scene']}|{sc.get('renderKey')}|{s['narratorRu']['version']}|{e.kind}"
                attempts[k] = attempts.get(k, 0) + 1
                if attempts[k] >= ATTEMPTS_BEFORE_STICKY:
                    e.sticky, e.why = True, f"{e.why} (failed {attempts[k]} times: remembered)"
            fails.append({"scene": sc["scene"], "why": e.why, "sticky": e.sticky, "renderKey": sc.get("renderKey"),
                          "jobs": [{"seg": j["seg"], "i": j["i"], "sig": j["sig"]} for j in culprit]})
            log("scene skipped:", sc["scene"], e.why)
        except Exception as e:                       # one bad scene never stops the batch
            traceback.print_exc()
            fails.append({"scene": sc["scene"], "why": f"{type(e).__name__}: {str(e)[:200]}", "sticky": False, "renderKey": sc.get("renderKey"),
                          "jobs": []})
    lines_failed = set()                             # distinct (scene, seg, i); a scene-wide failure with no line counts once
    for x in fails:
        lines_failed |= {(x["scene"], j["seg"], j["i"]) for j in x["jobs"]} if x.get("jobs") else {(x["scene"], x.get("seg"), x.get("i"))}
    res["failed"] = len(lines_failed)
    if not a.out:                                    # a dry run (--out) leaves no trace in the store or the failure memory
        attempts_p.write_text(json.dumps(attempts, indent=1), "utf-8")
        if fails:
            with open(Path(a.store) / "narrator-failures.jsonl", "a", encoding="utf-8") as f:
                for x in fails:
                    f.write(json.dumps({"at": time.strftime("%Y-%m-%dT%H:%M:%S"), **x}, ensure_ascii=False) + "\n")
        memo = narrator.load_failed(work)
        for x in fails:
            if not x.get("sticky"):
                continue
            for j in (x["jobs"] if "jobs" in x else [{"seg": x.get("seg"), "i": x.get("i"), "sig": x.get("sig")}]):
                memo[narrator.failed_key(x["scene"], x["renderKey"], j)] = {"why": x["why"], "at": time.strftime("%Y-%m-%dT%H:%M:%S")}
        (work / "failed.json").write_text(json.dumps(memo, ensure_ascii=False, indent=1), "utf-8")
    res["failures"] = fails
    print("OK " + json.dumps(res, ensure_ascii=False), flush=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("stage", choices=["en", "ru", "check", "build"])
    ap.add_argument("--work", required=True)
    ap.add_argument("--settings", default=None)
    ap.add_argument("--store", default=str(config.STORE))
    ap.add_argument("--out", default="")
    a = ap.parse_args()
    try:
        {"en": stage_en, "ru": stage_ru, "check": stage_check, "build": stage_build}[a.stage](a)
    except Exception as e:
        traceback.print_exc()
        print("FAIL " + json.dumps({"error": f"{type(e).__name__}: {str(e)[:300]}"}), flush=True)
        sys.exit(1)


if __name__ == "__main__":
    main()
