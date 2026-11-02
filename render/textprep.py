"""Sentence splitting and Russian stress injection (pure Python, no heavy imports).

The sentence split is the content repo's compose.py regex: break after
. ! ? ... followed by whitespace. Stress comes from the notes' `words[].stress` (surface form with U+0301);
only that field may put a combining acute into the text sent to the model.
"""
import gzip
import json
import re
import unicodedata
from dataclasses import dataclass, field
from pathlib import Path

ACUTE = "́"
_SENT = re.compile(r"(?<=[.!?…])\s+")
_NATIVE_SENT = re.compile(r"[。！？؟]+[」』”’\"')\]]*")
_CYR = re.compile("[Ѐ-ӿ]")
_VOWELS = set("аеёиоуыэюяАЕЁИОУЫЭЮЯ")
_LETTER = re.compile(r"[^\W\d_]", re.UNICODE)


def split_sentences(text: str):
    """[(start, end, sentence)] with offsets into `text` (so stress insertions can be mapped)."""
    out, pos = [], 0
    text_s = text
    boundaries = [(m.start(), m.end()) for m in _SENT.finditer(text_s)]
    for match in _NATIVE_SENT.finditer(text_s):
        end = match.end()
        following = end
        while following < len(text_s) and text_s[following].isspace():
            following += 1
        boundaries.append((end, following))
    for end, following in sorted(set(boundaries)):
        if end < pos:
            continue
        seg = text_s[pos:end]
        if seg.strip():
            out.append((pos, end, seg))
        pos = following
    tail = text_s[pos:]
    if tail.strip():
        out.append((pos, len(text_s), tail))
    if not out and text.strip():
        out = [(0, len(text), text)]
    return out


def strip_acute(s: str) -> str:
    return unicodedata.normalize("NFC", unicodedata.normalize("NFD", s).replace(ACUTE, "")) if ACUTE in unicodedata.normalize("NFD", s) else s


def has_cyrillic(s: str) -> bool:
    return bool(_CYR.search(s))


def vowel_count(word: str) -> int:
    return sum(1 for c in word if c in _VOWELS)


def bare(token: str) -> str:
    """Letters only, lowercase, ё folded to е (homograph dictionary key)."""
    return "".join(c for c in token.lower() if c.isalpha()).replace("ё", "е")


_HOMOGRAPHS = None


def homographs(path=None):
    global _HOMOGRAPHS
    if _HOMOGRAPHS is None:
        p = Path(path or Path(__file__).resolve().parent / "data" / "ru_homographs.txt.gz")
        if p.exists():
            _HOMOGRAPHS = frozenset(gzip.open(p, "rt", encoding="utf-8").read().split())
        else:
            _HOMOGRAPHS = frozenset()
    return _HOMOGRAPHS


def token_spans(text: str, tokens, start=0):
    """Char span of each token found in order (None when a token cannot be found; never raises)."""
    spans, cur = [], start
    for tok in tokens:
        at = text.find(tok, cur)
        if at < 0:
            spans.append(None)
            continue
        spans.append((at, at + len(tok)))
        cur = at + len(tok)
    return spans


def acute_offsets(token: str, stress: str):
    """Offsets (into `token`) where a U+0301 goes so that `token` carries the marks of `stress`.
    None when the letters do not match. `stress` is the notes' marked surface form (same letters)."""
    if not stress or ACUTE not in stress:
        return []
    plain = stress.replace(ACUTE, "")
    low_t, low_p = token.lower().replace("ё", "е"), plain.lower().replace("ё", "е")
    at = low_t.find(low_p)
    if at < 0:
        return None
    offs, n = [], 0
    for i, c in enumerate(stress):
        if c == ACUTE:
            offs.append(at + (i - n))   # insertion point: just after the vowel
            n += 1
    return offs


@dataclass
class Sentence:
    seg: int
    idx: int                 # sentence index inside the segment
    role: str
    lang: str                # ru | fr | en
    plain: str               # text as written (no marks)
    tts: str                 # text sent to the model (marks injected)
    start: int = 0           # offset of `plain` inside the segment text
    marks: list = field(default_factory=list)       # [(offset_in_plain, token)] injected
    missing: list = field(default_factory=list)     # tokens that wanted a mark and had none
    expected: list = field(default_factory=list)    # [(offset_in_plain, token, stress)] all notes stresses (for the check)
    gap: float = 0.0


def segment_inserts(text: str, words, policy: str, hom=None):
    """Plan the mark insertions for one Russian segment.
    Returns (inserts{offset: True}, expected[(start,end,stress)], missing_tokens[(start,end)])."""
    hom = homographs() if hom is None else hom
    toks = [w.get("t", "") for w in (words or [])]
    spans = token_spans(text, toks)
    inserts, expected = set(), []
    covered = set()
    for w, sp in zip(words or [], spans):
        if sp is None:
            continue
        covered.add(sp)
        s = w.get("stress")
        if not s or ACUTE not in s:
            continue
        offs = acute_offsets(text[sp[0]:sp[1]], s)
        if offs is None:
            continue
        expected.append((sp[0], sp[1], s))
        if policy == "all" or (policy == "homographs" and bare(text[sp[0]:sp[1]]) in hom):
            inserts.update(sp[0] + o for o in offs)
    # tokens of the text with no notes entry (or no stress) that would want a mark
    missing = []
    for m in re.finditer(r"\S+", text):
        sp = (m.start(), m.end())
        tok = m.group()
        if not has_cyrillic(tok) or vowel_count(tok) < 2 or "ё" in tok.lower():
            continue
        if any(sp[0] >= a and sp[1] <= b for a, b in [(e[0], e[1]) for e in expected]):
            continue
        if policy == "none":
            continue
        if policy == "homographs" and bare(tok) not in hom:
            continue
        missing.append(sp)
    return inserts, expected, missing


def apply_inserts(text: str, offsets) -> str:
    out, last = [], 0
    for o in sorted(set(offsets)):
        out.append(text[last:o])
        out.append(ACUTE)
        last = o
    out.append(text[last:])
    return "".join(out)


def group_turn_chunks(sents, text: str, max_chars: int = 0):
    """Merge consecutive sentences of one segment up to `max_chars` so TTS voices whole turns with continuous prosody."""
    if not max_chars or len(sents) <= 1:
        return sents
    chunks = []
    ca, cb = sents[0][0], sents[0][1]
    for a, b, _s in sents[1:]:
        if (b - ca) <= max_chars:
            cb = b
        else:
            chunks.append((ca, cb, text[ca:cb]))
            ca, cb = a, b
    chunks.append((ca, cb, text[ca:cb]))
    return chunks


_INTRO_COMMA_RE = re.compile(
    r"(^|(?<=[.!?…]\s)|(?<=['\"]\s))"
    r"(A little later|Later that (?:night|evening|day|morning)|The next (?:morning|day)|"
    r"Tomorrow morning|This morning|Last night|Right now|At first|At last|At the start|At the end|"
    r"In the present tense|In the past tense|In the future tense|"
    r"In Russian|In French|In Spanish|In German|In Italian|In Portuguese|In Arabic|In Japanese|In Korean|In Mandarin|In Chinese|In English|"
    r"Meanwhile|Afterwards|Instead|Otherwise|Fortunately|Unfortunately|Luckily|Finally|Normally|Usually|Literally|Word for word)"
    r"\s+(?=[A-Z\"'a-z])"
)


def polish_english_commas(text: str) -> str:
    """Insert missing natural prosodic commas after introductory English phrases for TTS delivery."""
    def _repl(m):
        return f"{m.group(1)}{m.group(2)}, "
    return _INTRO_COMMA_RE.sub(_repl, text)


def prepare_segment(seg_i: int, role: str, text: str, lang: str, words, policy: str, gap: float, isent: float,
                    hom=None, ruaccent=None, max_turn_chars: int = 0):
    """Sentences (or merged whole-turn chunks <= `max_turn_chars`) of one segment.
    `ruaccent`: optional callable(list[str]) -> list[str] marked with U+0301, used for tokens the notes do not cover."""
    sents = group_turn_chunks(split_sentences(text), text, max_turn_chars)
    out = []
    if lang != "ru" or policy == "none":
        for k, (a, b, s) in enumerate(sents):
            s_tts = polish_english_commas(s) if lang == "en" else s
            out.append(Sentence(seg_i, k, role, lang, s, s_tts, a, gap=(gap if k == len(sents) - 1 else isent)))
        return out
    inserts, expected, missing = segment_inserts(text, words, policy, hom)
    for k, (a, b, s) in enumerate(sents):
        offs = [o - a for o in inserts if a <= o < b]
        tts = apply_inserts(s, offs)
        marks = [(o, s[:o][-1:] ) for o in sorted(offs)]
        exp = [(e0 - a, text[e0:e1], e2) for e0, e1, e2 in expected if a <= e0 and e1 <= b]
        miss = [text[m0:m1] for m0, m1 in missing if a <= m0 and m1 <= b]
        sent = Sentence(seg_i, k, role, lang, s, tts, a, marks, miss, exp, gap=(gap if k == len(sents) - 1 else isent))
        if miss and ruaccent is not None:
            marked = ruaccent([s])[0]
            sent.tts, sent.missing = _merge_ruaccent(sent, marked)
        out.append(sent)
    return out


def _merge_ruaccent(sent: Sentence, marked: str):
    """Copy RuAccent's marks onto the tokens in sent.missing only (never on tokens the notes decided)."""
    plain_tokens = list(re.finditer(r"\S+", sent.plain))
    mk_tokens = marked.split()
    if len(mk_tokens) != len(plain_tokens):
        return sent.tts, sent.missing
    want = set(sent.missing)
    offs = []
    for pt, mt in zip(plain_tokens, mk_tokens):
        if pt.group() not in want or ACUTE not in mt:
            continue
        o = acute_offsets(pt.group(), mt)
        if o is not None:
            offs.extend(pt.start() + x for x in o)
    if not offs:
        return sent.tts, sent.missing
    existing = [m[0] for m in sent.marks]
    return apply_inserts(sent.plain, existing + offs), []
