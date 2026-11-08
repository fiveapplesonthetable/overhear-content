"""Reviewed lexical units -> MMS/uroman targets with explicit whole-unit ownership.

No original characters are assigned evenly divided acoustic intervals. A reading
of a compound belongs to its authored span as a whole.
"""
import importlib.util
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
import re
import unicodedata

LANGUAGES = frozenset({"ja", "zh", "ko", "ar", "hi"})
VERSION = "mms-uroman-wordspans/1;uroman=1.3.1.1"
_CODES = {"ja": "jpn", "zh": "zho", "ko": "kor", "ar": "ara", "hi": "hin"}
_ALPHABET = frozenset("abcdefghijklmnopqrstuvwxyz'")
_spec = importlib.util.spec_from_file_location("overhear_authored_spans", Path(__file__).resolve().parents[1] / "tools/word_spans.py")
_spans = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_spans)


class NativeAlignmentError(ValueError):
    pass


@dataclass(frozen=True)
class Word:
    text: str
    start: int
    end: int
    reading: str | None = None


@dataclass(frozen=True)
class Targets:
    words: tuple
    letters: tuple
    owners: tuple


def words_for_segment(text, annotations, lang):
    annotations = annotations or []
    try:
        spans = _spans.annotation_spans(text, annotations, required=lang in ("ja", "zh", "hi"))
    except ValueError as exc:
        raise NativeAlignmentError(str(exc)) from exc
    if spans is None:
        tokens = [m for m in re.finditer(r"\S+", text) if any(c.isalnum() for c in m.group())]
        if annotations and [w.get("t") for w in annotations] != [m.group() for m in tokens]:
            raise NativeAlignmentError("native annotations must match exact whitespace units or supply complete explicit spans")
        spans = [(m.start(), m.end()) for m in tokens]
    words = []
    for i, (start, end) in enumerate(spans):
        reading = annotations[i].get("reading") if i < len(annotations) else None
        if lang in ("ja", "zh", "hi") and not reading:
            raise NativeAlignmentError("Japanese/Mandarin/Hindi words need reviewed readings")
        words.append(Word(text[start:end], start, end, reading))
    return tuple(words)


@lru_cache(maxsize=1)
def _romanizer():
    try:
        import uroman
        from importlib.metadata import version
        if version("uroman") != "1.3.1.1":
            raise NativeAlignmentError("install pinned pipeline/render/requirements-alignment.txt")
    except ImportError as exc:
        raise NativeAlignmentError("native alignment needs pinned uroman 1.3.1.1; install requirements-alignment.txt") from exc
    return uroman.Uroman(), uroman.RomFormat.EDGES


def _letters(text):
    out = []
    for ch in text.lower():
        if ch in _ALPHABET:
            out.append(ch)
        elif ch.isalnum() or unicodedata.category(ch).startswith("M"):
            raise NativeAlignmentError(f"unresolved MMS target {ch!r}; supply a reviewed spoken reading, including numbers")
        # Punctuation and whitespace are intentionally unspoken, not guessed.
    return out


def targets(text, lang, words):
    if lang not in LANGUAGES:
        raise NativeAlignmentError(f"unsupported native alignment language {lang!r}")
    romanizer, edge_format = _romanizer()
    edges = romanizer.romanize_string(text, lcode=_CODES[lang], rom_format=edge_format)
    letters, owners = [], []
    for owner, word in enumerate(words):
        if word.reading:
            roman = romanizer.romanize_string(word.reading, lcode=_CODES[lang])
            unit = _letters(roman)
        else:
            unit, covered = [], set()
            for edge in edges:
                if edge.end <= word.start or edge.start >= word.end:
                    continue
                source = text[edge.start:edge.end]
                if not any(c.isalnum() or unicodedata.category(c).startswith("M") for c in source):
                    continue
                part = _letters(edge.txt)
                if not word.start <= edge.start < edge.end <= word.end:
                    raise NativeAlignmentError("romanization crosses independently selectable word spans; review/coalesce the lexical unit")
                if part:
                    unit.extend(part)
                    covered.update(range(edge.start, edge.end))
            if any(c.isalnum() and c != "\u0640" and word.start + i not in covered for i, c in enumerate(word.text)):
                raise NativeAlignmentError(f"romanization omitted native letters in {word.text!r}")
        if not unit:
            raise NativeAlignmentError(f"no acoustic targets for native word {word.text!r}")
        letters.extend(unit)
        owners.extend([owner] * len(unit))
    if not letters:
        raise NativeAlignmentError("native sentence has no accountable spoken targets")
    return Targets(tuple(words), tuple(letters), tuple(owners))


def aggregate(plan, acoustic_spans, frame_seconds, duration):
    """Aggregate actual CTC spans by authored word; never manufacture missing bounds."""
    import math
    if len(acoustic_spans) != len(plan.letters):
        raise NativeAlignmentError("CTC span count does not match complete native targets")
    owned = [[] for _ in plan.words]
    for span, owner in zip(acoustic_spans, plan.owners):
        start, end = float(span.start) * frame_seconds, float(span.end) * frame_seconds
        score = float(span.score)
        if not all(math.isfinite(n) for n in (start, end, score)) or not 0 <= start < end <= duration + 1e-6:
            raise NativeAlignmentError("native CTC returned invalid or out-of-clip bounds")
        owned[owner].append((start, end, score))
    result, previous = [], 0.0
    for word, spans in zip(plan.words, owned):
        if not spans:
            raise NativeAlignmentError(f"missing native word {word.text!r}; interpolation is forbidden")
        start, end = min(t[0] for t in spans), max(t[1] for t in spans)
        if start < previous - 1e-6:
            raise NativeAlignmentError("native word intervals overlap or are out of logical order")
        result.append({"t": word.text, "span": [word.start, word.end], "s": start, "e": end,
                       "ok": True, "why": "", "confidence": min(t[2] for t in spans)})
        previous = end
    return result
