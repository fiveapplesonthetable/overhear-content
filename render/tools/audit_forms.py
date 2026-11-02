"""Audit the lexicon tables of the rendered scenes against the Wiktionary dump (see form_dict.py): every cell piece whose letters are not among the
dictionary's forms for that lemma and slot is listed. Slots the dictionary has no entry for are counted, not judged.

  python3 -I tools/audit_forms.py [--out FILE.jsonl]        (content: OVERHEAR_CONTENT, store: OVERHEAR_RENDER_STORE, dump: settings forms.dictionary)
"""
import argparse
import collections
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import config  # noqa: E402
import content  # noqa: E402
import form_dict  # noqa: E402
import forms  # noqa: E402
from store import Store  # noqa: E402


KNOWN_COLUMNS = {"sg", "pl", "m", "f", "n", "form", ""}


def audit(scenes, fdict):
    """-> (mismatches [dict], counts Counter). One entry per (scene, lemma) table cell piece."""
    out, counts = [], collections.Counter()
    for sc in scenes:
        if sc.lang != "ru":
            continue
        for key, entry in (sc.notes.get("lexicon") or {}).items():
            for sl in forms.slots_of(entry):
                for p in forms.pieces(sl.cell):
                    if sl.column.strip().lower() not in KNOWN_COLUMNS:       # a table with its own layout (Feminine, Interrogative (кто)...): not judged
                        counts["unknown"] += 1
                        continue
                    got = fdict.slot_letters(entry.get("pos"), entry["lemma"], sl.title, sl.row, sl.column)
                    if got is None:
                        counts["unknown"] += 1
                    elif form_dict.letters(p) in got:
                        counts["match"] += 1
                    else:
                        counts["mismatch"] += 1
                        out.append({"scene": sc.id, "lemma": entry["lemma"], "pos": entry.get("pos"), "title": sl.title, "row": sl.row,
                                    "column": sl.column, "cell": sl.cell, "piece": p, "dictionary": sorted(got)})
    return out, counts


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out")
    ap.add_argument("--all-scenes", action="store_true", help="every scene of the content, not only the rendered ones")
    a = ap.parse_args()
    s = config.load_settings()
    store = Store(config.STORE)
    scenes, _ = content.discover(config.CONTENT_DIR)
    if not a.all_scenes:
        scenes = [sc for sc in scenes if (store.meta(sc.id) or {}).get("contentHash") == sc.content_hash]
    lemmas = {form_dict.letters(e["lemma"]) for sc in scenes for e in (sc.notes.get("lexicon") or {}).values()}
    bad, counts = audit(scenes, form_dict.FormDict(s["forms"]["dictionary"], lemmas))
    print(f"{len(scenes)} scenes: {dict(counts)}")
    if a.out:
        Path(a.out).write_text("".join(json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n" for r in bad), "utf-8")
    for r in bad[:40]:
        print(r["scene"], r["lemma"], r["title"], r["row"], r["column"], "|", r["piece"], "| dictionary:", r["dictionary"])


if __name__ == "__main__":
    main()
