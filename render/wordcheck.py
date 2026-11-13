"""Per-word ASR check for Russian takes: a word that matters for the stress (an in-scope homograph, or any word that
carried a U+0301 mark in the TTS text) must be heard as that word in the take's Whisper transcript.

The stress check (stresscheck.py) only compares vowel lengths and the sentence CER gate tolerates a wrong word, so a
take that says «чивка» for «чека» passed both. Pure Python: shared by the synthesis gates and the scene finish.
"""
import re

from textprep import ACUTE, bare, homographs

_NOT_LETTERS = re.compile(r"[^\w]+|_")


def norm_words(text: str):
    """Lowercase, ё -> е, marks and punctuation dropped; a hyphenated word counts as its parts."""
    return [w for w in _NOT_LETTERS.split(text.replace(ACUTE, "").lower().replace("ё", "е")) if w]


def required_words(sent, scope: str = "homographs", hom=None):
    """Words of a sentence (textprep.Sentence) that its transcript must contain: the notes words in the stress check's
    scope, plus every word that carries a mark in the text sent to the TTS."""
    hom = homographs() if hom is None else hom
    words = [tok for _off, tok, _stress in sent.expected if scope == "all" or bare(tok) in hom]
    words += [t for t in sent.tts.split() if ACUTE in t]
    unique = {}
    for w in words:
        unique.setdefault(tuple(norm_words(w)), w)      # a marked word is the same word as its plain form
    return list(unique.values())


def missing(words, transcript: str):
    """The `words` that the transcript does not contain."""
    heard = set(norm_words(transcript))
    return [w for w in words if not all(part in heard for part in norm_words(w))]
