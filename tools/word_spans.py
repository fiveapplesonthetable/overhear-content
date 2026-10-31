"""Exact authored lexical spans; offsets are half-open Unicode code points, never UTF-16 units."""
import math
import re
import unicodedata
from pathlib import PurePosixPath


def spoken(character):
    return unicodedata.category(character)[0] in "LNM"


def annotation_spans(text, words, required=False):
    """Explicit word spans, or None for unchanged legacy whitespace annotation.

    Every spoken letter/number/attached mark must have exactly one owner. A
    punctuation-only gap is allowed; a missing native substring is not.
    """
    words = words or []
    explicit = any("span" in word for word in words)
    if not explicit:
        if required:
            raise ValueError("this language requires explicit code-point span on every annotated word")
        return None
    spans, cursor = [], 0
    for word in words:
        span = word.get("span")
        if not isinstance(span, list) or len(span) != 2 or any(type(n) is not int for n in span):
            raise ValueError("every word must have span:[start,end] integer code-point offsets")
        start, end = span
        if not cursor <= start < end <= len(text):
            raise ValueError(f"word span {span!r} overlaps, is empty, or is outside its segment")
        if text[start:end] != word.get("t"):
            raise ValueError(f"word span {span!r} does not select its exact written token")
        if any(spoken(c) for c in text[cursor:start]):
            raise ValueError(f"spoken text between offsets {cursor} and {start} has no annotated owner")
        if unicodedata.category(text[start]).startswith("M") or (end < len(text) and unicodedata.category(text[end]).startswith("M")):
            raise ValueError("a span must not split a base character from its combining marks")
        if not any(spoken(c) for c in text[start:end]):
            raise ValueError("an annotated word must contain spoken text")
        spans.append((start, end))
        cursor = end
    if any(spoken(c) for c in text[cursor:]):
        raise ValueError(f"spoken text after offset {cursor} has no annotated owner")
    return spans


def source_audio_metadata(value):
    """Validate public metadata only. The renderer verifies private bytes and actual media bounds."""
    if not isinstance(value, dict) or set(value) != {"file", "sha256", "start", "end"}:
        raise ValueError("sourceAudio needs exactly file, sha256, start and end")
    name = value["file"]
    if not isinstance(name, str) or not name.startswith("sources/") or "\\" in name:
        raise ValueError("sourceAudio.file must be a canonical relative sources/ identifier")
    path = PurePosixPath(name)
    if path.is_absolute() or ".." in path.parts or str(path) != name:
        raise ValueError("sourceAudio.file may not traverse or name an absolute/private path")
    if not re.fullmatch(r"[0-9a-f]{64}", str(value["sha256"])):
        raise ValueError("sourceAudio.sha256 must be the entire original media SHA256")
    start, end = value["start"], value["end"]
    if any(isinstance(n, bool) or not isinstance(n, (int, float)) or not math.isfinite(n) for n in (start, end)) or not 0 <= start < end:
        raise ValueError("sourceAudio start/end must be finite, positive-duration seconds")
    return dict(value)
