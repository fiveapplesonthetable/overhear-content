"""The reviewed stress overrides for slots nothing else settles (form_overrides.json, next to this file; see its _note)."""
import json
from functools import lru_cache
from pathlib import Path

import form_dict

PATH = Path(__file__).resolve().parent / "form_overrides.json"


@lru_cache(maxsize=1)
def table():
    """{(lemma, cell): [(slots | None, text, why)]}; an entry whose text does not have the cell's letters is a mistake and is refused."""
    out = {}
    for e in json.loads(PATH.read_text("utf-8"))["entries"]:
        if form_dict.letters(e["text"]) != form_dict.letters(e["cell"]):
            raise ValueError(f"override {e['lemma']!r}: {e['text']!r} is not the cell {e['cell']!r}")
        slots = None if e["slots"] == "all" else {tuple(s) for s in e["slots"]}
        out.setdefault((e["lemma"], e["cell"]), []).append((slots, e["text"], e["why"]))
    return out


def find(lemma, slot):
    """(text, why) for this slot of the lemma, or None."""
    for slots, text, why in table().get((lemma, slot.cell), []):
        if slots is None or (slot.title, slot.row, slot.column) in slots:
            return text, why
    return None
