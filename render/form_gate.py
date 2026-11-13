"""Pronunciation gate for the Whisper check of form clips (ar, hi, ja, ko, fr).

A form is a single short word, so spelling-level CER is brutal: one letter is 20 %+ of the word, and Whisper picks a spelling for what it hears
(लाएगा heard as लाइगा, 칸이 as 카니, 越し as 腰, parlent as parle). Both sides are reduced to a language's sound units and compared there with a
weighted edit distance: sounds that are the same (or, for a few pairs, easily confused) cost nothing (or half), a different sound costs 1. A genuinely
different word still costs 1 per sound. The gate is `min(spelling CER, sound distance)`, so it can only pass more clips than the plain CER did.

  Hindi     vowel letters = matras, no nukta, chandrabindu = anusvara, nasal conjuncts = anusvara, the inherent schwa and halant dropped
  Arabic    no harakat/shadda/tatweel, alef and hamza forms = alef, alef maqsura = yaa, taa marbuta = haa; omitting a long vowel letter costs half
  Japanese  the reading (pykakasi) in hiragana, digits as kanji numerals, long vowels and ぢ/づ/を folded
  Korean    jamo, final consonants linked into a following vowel syllable (칸이 = 카니) or neutralised, ㅐ = ㅔ; lax/tense/aspirated stops cost half
  French    a rough grapheme-to-sound pass per word (silent endings, -er/-é/-ez, ou, on, an, ph, qu ...)

GATE_VERSION is stored in a failed record; a failed record from another version is stale (clips.ClipStore.is_done), so changing a normaliser or a
cost here retries exactly the forms that were failed by the old gate. Bump it with every change to this file's behaviour.
"""
import re
import unicodedata

GATE_VERSION = "fg1"
LANGS = ("ar", "hi", "ja", "ko", "fr")
HALF = 0.5
MIN_UNITS = 4          # a word of fewer sounds is scored as if it had four: one confusable sound (half a point) never fails it, one different sound (a whole point) still does

# ---- edit distance ----------------------------------------------------------------------------------------------------
def weighted_distance(ref, hyp, sub=lambda a, b: 1.0, optional=(), edge=True):
    """Edit distance between two unit lists. `sub(a, b)` prices a substitution (default 1); inserting or deleting a unit in `optional` costs
    half (unless `edge` is False and it is the first or last unit of its list); any other insertion or deletion costs 1."""
    optional = set(optional)

    def indel(seq, k):
        return HALF if seq[k] in optional and (edge or 0 < k < len(seq) - 1) else 1.0
    prev = [0.0]
    for k in range(len(hyp)):
        prev.append(prev[-1] + indel(hyp, k))
    for i, r in enumerate(ref):
        cur = [prev[0] + indel(ref, i)]
        for j, h in enumerate(hyp):
            cur.append(min(prev[j + 1] + indel(ref, i), cur[j] + indel(hyp, j), prev[j] + (0.0 if r == h else sub(r, h))))
        prev = cur
    return prev[-1]


def _pair_cost(groups):
    """sub(): half cost inside one of the `groups` (strings of easily confused units), else 1."""
    return lambda a, b: HALF if any(a in g and b in g for g in groups) else 1.0


def _letters(text):
    return "".join(ch for ch in unicodedata.normalize("NFC", text).lower() if unicodedata.category(ch)[0] in "LMN")


# ---- Hindi ------------------------------------------------------------------------------------------------------------
_HI_VOWELS = {"अ": "", "आ": "ा", "इ": "ि", "ई": "ी", "उ": "ु", "ऊ": "ू", "ए": "े", "ऐ": "ै", "ओ": "ो", "औ": "ौ", "ऋ": "ृ", "ऑ": "ॉ", "ॉ": "ो"}
_HI_SAME = {"ष": "श", "ण": "न", "ङ": "ं", "ञ": "ं", "ँ": "ं", "ऽ": ""}
_HI_CONS = "कखगघचछजझटठडढतथदधनपफबभमयरलवशषसह"
_HI_GROUPS = ("िी", "ुू", "ेै", "ोौ", "िे", "ुो", "कखग", "गघ", "चछ", "जझ", "टठ", "डढ", "तथ", "दध", "पफ", "बभ", "शस", "वब", "ृि", "ंनम")


def hindi_units(text):
    t = unicodedata.normalize("NFC", text).lower().replace("़", "")
    t = re.sub(r"[^ऀ-ॿ]", "", t)                 # also drops the spaces between a word the voice read as one and Whisper as two
    t = "".join(_HI_VOWELS.get(c, c) for c in t)
    t = "".join(_HI_SAME.get(c, c) for c in t)
    t = re.sub("य(?=[ेीै])", "", t)                         # ये = ए, यी = ई (the glide is not written the same way twice)
    t = t.replace("्", "")                              # halant: the schwa it silences is not counted either
    return list(re.sub(rf"([{_HI_CONS}])\1", r"\1", t))      # a doubled consonant (गुस्से) is often written once


# ---- Arabic -----------------------------------------------------------------------------------------------------------
_AR_MAP = str.maketrans({"أ": "ا", "إ": "ا", "آ": "ا", "ٱ": "ا", "ى": "ي", "ة": "ه", "ؤ": "و", "ئ": "ي", "ء": "", "ـ": ""})
_AR_GROUPS = ("صس", "طت", "ضد", "ظذز", "ثس", "ذز", "ثت", "ظض", "دذ", "ها")
_AR_LONG = "اوي"


def arabic_units(text):
    t = unicodedata.normalize("NFC", text).lower().translate(_AR_MAP)
    t = re.sub(r"[ً-ٰٟ]", "", t)
    t = "".join(ch for ch in t if "؀" <= ch <= "ۿ" and unicodedata.category(ch)[0] == "L")
    t = re.sub(r"(?<=و)ا$", "", t)                          # the silent alef of the plural/past -وا
    return list(t)


# ---- Japanese ---------------------------------------------------------------------------------------------------------
_KANJI_DIGITS = "〇一二三四五六七八九"
_ROW = {"あかがさざただなはばぱまやらわぁゃ": "あ", "いきぎしじちぢにひびぴみりぃ": "い", "うくぐすずつづぬふぶぷむゆるぅゅゔ": "う",
        "えけげせぜてでねへべぺめれぇ": "え", "おこごそぞとどのほぼぽもよろをぉょ": "お"}
_kakasi = None


def _kanji_number(n):
    """12 -> 十二 (up to 9999: a form's number is a year or a count)."""
    if n == 0:
        return _KANJI_DIGITS[0]
    out = ""
    for value, unit in ((1000, "千"), (100, "百"), (10, "十")):
        d, n = divmod(n, value)
        out += ("" if d == 1 else _KANJI_DIGITS[d]) * bool(d) + unit * bool(d)
    return out + (_KANJI_DIGITS[n] if n else "")


def japanese_reading(text):
    """The reading of `text` in hiragana (kanji, katakana and digits alike)."""
    global _kakasi
    if _kakasi is None:
        import pykakasi
        _kakasi = pykakasi.kakasi()
    text = unicodedata.normalize("NFKC", text)
    text = re.sub(r"\d+", lambda m: _kanji_number(int(m[0])) if len(m[0]) < 5 else m[0], text)
    return "".join(x["hira"] for x in _kakasi.convert(text))


def japanese_units(text):
    kana = "".join(ch for ch in japanese_reading(text) if "぀" <= ch <= "ゟ" or ch == "ー")
    out = []
    for ch in kana:
        if ch == "ー" and out:                               # a long vowel mark repeats the vowel of the kana before it
            ch = next((v for g, v in _ROW.items() if out[-1] in g), "")
        elif ch in "うい" and out:                           # おう = おお, えい = ええ: both are written either way
            v = next((v for g, v in _ROW.items() if out[-1] in g), "")
            ch = v if (ch == "う" and v == "お") or (ch == "い" and v == "え") else ch
        out.append({"ぢ": "じ", "づ": "ず", "を": "お"}.get(ch, ch))
    return out


# ---- Korean -----------------------------------------------------------------------------------------------------------
_KO_FINAL_NEUTRAL = {"ㄲ": "ㄱ", "ㅋ": "ㄱ", "ㄳ": "ㄱ", "ㅅ": "ㄷ", "ㅆ": "ㄷ", "ㅈ": "ㄷ", "ㅊ": "ㄷ", "ㅌ": "ㄷ", "ㅎ": "ㄷ", "ㅍ": "ㅂ", "ㅄ": "ㅂ",
                     "ㄵ": "ㄴ", "ㄶ": "ㄴ", "ㄺ": "ㄱ", "ㄻ": "ㅁ", "ㄼ": "ㄹ", "ㄽ": "ㄹ", "ㄾ": "ㄹ", "ㄿ": "ㅂ", "ㅀ": "ㄹ"}
_KO_VOWEL = {"ㅐ": "ㅔ", "ㅒ": "ㅔ", "ㅖ": "ㅔ"}                  # ㅐ/ㅔ and 얘/예/에 are no longer told apart in speech
_KO_GROUPS = ("ㄱㅋㄲ", "ㄷㅌㄸ", "ㅂㅍㅃ", "ㅈㅊㅉ", "ㅅㅆ")


_CHO, _JUNG = "ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ", "ㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅟㅠㅡㅢㅣ"
_JONG = " ㄱㄲㄳㄴㄵㄶㄷㄹㄺㄻㄼㄽㄾㄿㅀㅁㅂㅄㅅㅆㅇㅈㅊㅋㅌㅍㅎ"


def _jamo(syllable):
    """(initial, vowel, final) of a Hangul syllable in compatibility jamo; final "" when it has none."""
    code = ord(syllable) - 0xAC00
    return _CHO[code // 588], _JUNG[code % 588 // 28], _JONG[code % 28].strip()


def korean_units(text):
    """The syllables of `text` as heard: (initial, vowel, final) in compatibility jamo, with a final consonant carried over to a following vowel
    syllable (칸이 = 카니) and the other finals reduced to their sound (빛 = 빗 = 빋). Spaces are dropped."""
    syl = []
    for ch in unicodedata.normalize("NFC", text):
        if "가" <= ch <= "힣":
            i, v, f = _jamo(ch)
            syl.append([i, _KO_VOWEL.get(v, v), f])
    for cur, nxt in zip(syl, syl[1:]):
        if cur[2] not in ("", "ㅇ") and nxt[0] == "ㅇ":
            nxt[0], cur[2] = ("" if cur[2] == "ㅎ" else cur[2]), ""
    return [("" if i == "ㅇ" else i, v, _KO_FINAL_NEUTRAL.get(f, f)) for i, v, f in syl]


def _korean_sub(a, b):
    """Two different syllables: half a point when only one sound differs and it is a lax/tense/aspirated pair, else a whole one."""
    diff = [(x, y) for x, y in zip(a, b) if x != y]
    return HALF if len(diff) == 1 and any(x in g and y in g for g in _KO_GROUPS for x, y in diff) else 1.0


# ---- French -----------------------------------------------------------------------------------------------------------
_FR_RULES = [                                                   # (pattern, sound), applied in order on a lower-case word
    (r"œ|æ", "e"), (r"[àâä]", "a"), (r"[îï]", "i"), (r"[ôö]", "o"), (r"[ùûü]", "u"), (r"[èêë]", "è"), (r"ç", "s"),
    (r"(?<=[^aeiouyéèh])ents?$", "e"), (r"(?<=[^s])[sxtdp]+$", ""),         # -ent of a verb, then the silent final consonants
    (r"ai$", "è"), (r"(ées?|és|ez|er)$", "é"), (r"(?<=[^aeiouyéè])e$|(?<=[iuo])e$", ""),
    (r"^h|(?<=[^cspt])h", ""), (r"ph", "f"), (r"qu|(?<=.)k", "k"), (r"gn", "ñ"), (r"ch", "ʃ"), (r"g(?=[eiyéè])", "j"), (r"gu(?=[eiyéè])", "g"),
    (r"c(?=[eiyéè])", "s"), (r"c", "k"), (r"eau|au", "o"), (r"ou", "U"), (r"oi", "wa"), (r"ai|ei", "è"), (r"eu|œu", "ø"),
    (r"(?:[ae]n|[ae]m)(?=[^aeiouyéè]|$)", "ã"), (r"(?:[ie]n|ain|aim|im|yn|ym|in)(?=[^aeiouyéè]|$)", "ẽ"), (r"(?:on|om)(?=[^aeiouyéè]|$)", "õ"), (r"un|um(?=[^aeiouyéè]|$)", "ẽ"),
    (r"y", "i"), (r"w", "u"), (r"(.)\1", r"\1"),
]
_FR_GROUPS = ("éèe", "sz", "kg", "td", "pb")


def french_units(text):
    words = re.findall(r"[^\W\d_]+|\d+", unicodedata.normalize("NFC", text).lower().replace("’", "'"))
    out = []
    for w in words:
        for pat, sub in _FR_RULES:
            w = re.sub(pat, sub, w)
        out += list(w)
    return out


# ---- the gate -----------------------------------------------------------------------------------------------------------
def units(lang, text):
    return {"hi": hindi_units, "ar": arabic_units, "ja": japanese_units, "ko": korean_units, "fr": french_units}[lang](text)


def sound_cer(lang, ref, hyp):
    """Weighted distance between the sounds of `ref` and `hyp` / the number of sounds of `ref`; 1.0 when either has none."""
    r, h = units(lang, ref), units(lang, hyp)
    if not r or not h:
        return 1.0
    sub = _korean_sub if lang == "ko" else _pair_cost({"hi": _HI_GROUPS, "ar": _AR_GROUPS, "fr": _FR_GROUPS}.get(lang, ()))
    optional = {"ar": _AR_LONG, "hi": "ं"}.get(lang, "")        # a long vowel letter (ar) or a nasalisation mark (hi) is often left out; in Arabic only
    d = weighted_distance(r, h, sub, optional, edge=lang != "ar")   # inside a word (a missing last letter there is a missing suffix)
    return d / max(len(r), MIN_UNITS)


def gated_cer(lang, ref, hyp, strict_cer):
    """The number the clip is judged on: the spelling CER, or the sound distance where that is lower. Other languages: the spelling CER."""
    if lang not in LANGS:
        return strict_cer
    try:
        return min(strict_cer, sound_cer(lang, ref, hyp))
    except ImportError:                                           # no pykakasi in this venv: judge Japanese by spelling, as before
        return strict_cer


def main():
    """Dry run over a store: how many failed form records the current gate would pass, judged on their stored hyp (no audio, no GPU).
    A failed record keeps no audio, so the real re-gate is the next forms run (failed records of another GATE_VERSION are stale)."""
    import argparse
    import collections
    import json
    from pathlib import Path
    import forms
    ap = argparse.ArgumentParser(description=main.__doc__)
    ap.add_argument("--store", required=True)
    ap.add_argument("--cer-max", type=float, default=0.15)
    ap.add_argument("--show", type=int, default=0, help="print this many still-failing records per pair, nearest misses first")
    a = ap.parse_args()
    seen, rows = collections.Counter(), collections.defaultdict(list)
    for p in sorted((Path(a.store) / "forms").glob("*.json")):
        r = json.loads(p.read_text("utf-8"))
        if not isinstance(r, dict) or r.get("lang") not in LANGS:
            continue
        seen[r["pair"]] += 1
        if r.get("status") == "failed":
            ref = forms.spoken_form(r["lang"], r["text"]) or r["text"]
            rows[r["pair"]].append((gated_cer(r["lang"], ref, r.get("hyp") or "", r["cer"]), r))
    for pair, rs in sorted(rows.items()):
        bad = sorted(((c, r) for c, r in rs if c > a.cer_max), key=lambda x: x[0])
        print(f"{pair}: {len(rs)} of {seen[pair]} failed; the gate {GATE_VERSION} passes {len(rs) - len(bad)}, {len(bad)} still fail "
              f"({len(rs) / seen[pair]:.1%} -> {len(bad) / seen[pair]:.1%})")
        for c, r in bad[:a.show]:
            print(f"    {c:.2f} {r['text']!r} heard {r['hyp']!r}")


if __name__ == "__main__":
    main()
