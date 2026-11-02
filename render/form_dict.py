"""Stress of a table slot from a dictionary: Wiktionary's Russian inflection tables (wiktextract JSONL from kaikki.org, CC BY-SA).

The dump is untrusted data: it is only read with json.loads, line by line, by a `python -I` process, never executed or committed
(it lives in $OVERHEAR_HOME/dict/, see the SOURCES.md there). A lemma's entries carry `forms: [{form, tags}]` with the stress marked
(U+0301) and the grammatical tags of the slot. Our table slots (title, row label, column label) are mapped to those tags by `required_tags`;
a slot is resolved when exactly one stressed form of the lemma has those tags and the same letters as the cell (ignoring stress marks and ё/е).
"""
import json
import unicodedata

ACUTE = "́"
CASES = {"nominative", "genitive", "dative", "accusative", "instrumental", "prepositional"}
NUMBER = {"sg": "singular", "pl": "plural"}
GENDER = {"m": "masculine", "f": "feminine", "n": "neuter"}
PERSON = {"1st": "first-person", "2nd": "second-person", "3rd": "third-person"}
# tags that mark a form as not the current standard one, or the row as not a form at all
SKIP = {"dated", "obsolete", "archaic", "alternative", "romanization", "table-tags", "inflection-template", "class", "canonical"}


def required_tags(title: str, row: str, column: str):
    """The set of Wiktionary tags a form must carry to belong to our table slot, or None for a slot this table does not know."""
    t, r, c = title.strip().lower(), row.strip().lower(), column.strip().lower()
    num = NUMBER.get(c)
    if t in ("declension", "forms") and r in CASES:
        tags = {r}
        if num:
            tags.add(num)
        elif c in GENDER:
            tags.add(GENDER[c])          # adjectives and determiners: masculine / feminine / neuter carry no number
        return tags
    if t == "past" and c in GENDER:
        return {"past", GENDER[c], "singular"}
    if t == "past" and c == "pl":
        return {"past", "plural"}
    if t == "imperative" and num:
        return {"imperative", "second-person", num}
    if t in ("present", "future") and r in PERSON and num:
        return {t, PERSON[r], num}
    if t == "short forms" and (c in GENDER or c == "pl"):
        return {"short-form", GENDER.get(c, "plural")}
    return None


def letters(s: str) -> str:
    """The form's letters only: no stress mark, no footnote sign, no spaces, lower case, ё as е."""
    s = unicodedata.normalize("NFC", unicodedata.normalize("NFD", s).replace(ACUTE, ""))
    return "".join(ch for ch in s.lower() if ch.isalpha()).replace("ё", "е")


class FormDict:
    """`lemmas`: the lemmas to keep (letters form). Reads the whole dump once; keeps only those."""

    def __init__(self, path, lemmas):
        want = set(lemmas)
        self.entries = {}       # letters of the lemma -> [(pos, [(form, tags)])]
        with open(path, encoding="utf-8") as f:
            for line in f:
                try:
                    d = json.loads(line)
                except ValueError:
                    continue
                if not isinstance(d, dict) or d.get("lang_code") != "ru":
                    continue
                key = letters(str(d.get("word", "")))
                if key not in want:
                    continue
                forms = [(x["form"], set(x.get("tags") or [])) for x in d.get("forms") or []
                         if isinstance(x, dict) and isinstance(x.get("form"), str) and not (set(x.get("tags") or []) & SKIP)]
                self.entries.setdefault(key, []).append((d.get("pos"), forms))

    def slot_stress(self, pos, lemma, title, row, column, piece):
        """The stressed form of `piece` in this slot ("вина́"), or None when the dictionary does not settle it: no such lemma or slot, no form with
        these letters, or two different stressings of them."""
        need = required_tags(title, row, column)
        if need is None:
            return None
        entries = self.entries.get(letters(lemma)) or []
        same = [e for e in entries if e[0] == pos] or entries
        want = letters(piece)
        found = {form.strip().rstrip("¹²³⁴⁵⁶⁷⁸⁹ ") for _, forms in same for form, tags in forms if need <= tags and letters(form) == want}
        return next(iter(found)) if len(found) == 1 else None

    def slot_letters(self, pos, lemma, title, row, column):
        """The letters of every form the dictionary has for this slot (several for ё/е variants, animate/inanimate accusatives and the like), or None
        when it has no entry or does not know the slot."""
        need = required_tags(title, row, column)
        entries = self.entries.get(letters(lemma)) or []
        same = [e for e in entries if e[0] == pos] or entries
        if need is None or not same:
            return None
        found = {letters(form) for _, forms in same for form, tags in forms if need <= tags} - {""}      # a dash is no form
        return found or None

    def slot_forms(self, pos, lemma, title, row, column):
        """As slot_letters, but the forms as written (no stress mark, ё kept), sorted; None when the dictionary does not know the slot."""
        need = required_tags(title, row, column)
        entries = self.entries.get(letters(lemma)) or []
        same = [e for e in entries if e[0] == pos] or entries
        if need is None or not same:
            return None
        found = {unicodedata.normalize("NFC", unicodedata.normalize("NFD", form.strip().rstrip("¹²³⁴⁵⁶⁷⁸⁹ ")).replace(ACUTE, ""))
                 for _, forms in same for form, tags in forms if need <= tags}
        found = {f for f in found if letters(f)}
        return sorted(found) or None
