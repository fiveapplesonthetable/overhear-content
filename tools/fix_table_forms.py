#!/usr/bin/env python3
"""Repair lexicon table cells that are not real Russian forms. Stdlib only.   python3 tools/fix_table_forms.py [out]

The tables are written by the authoring agents, not generated, and a few lemmas came out with endings stuck on the lemma (кто-того, одинго,
что-нибудьго), with the animate accusative on an inanimate noun (пола, половников), with abbreviated cells ("нервный / -ого") or with a
non-standard form. Each fix below names the lemma, the slot (row label, column heading), the WRONG text and the right one; a cell is
only changed when it holds exactly the wrong text, so a table somebody has corrected already is left alone. The lexicon `stress` of
колледж is the standard колле́дж (the notes' words for it too).

Found with pipeline/render/tools/audit_forms.py (every cell against Wiktionary's inflection tables). Anything the audit lists that is NOT
here was judged doubtful or fine (aspect pairs, variants) and is left to a person.
"""
import json
import sys
from pathlib import Path

CASES = ["nominative", "genitive", "dative", "accusative", "instrumental", "prepositional"]

# lemma -> {(row, column): (wrong cell, right cell)}
CELLS = {
    "один": {("genitive", "Form"): ("одинго", "одного"), ("dative", "Form"): ("одинму", "одному"),
             ("instrumental", "Form"): ("одинм", "одним"), ("prepositional", "Form"): ("одинм", "одном")},
    "кто-то": {("genitive", "Form"): ("кто-того", "кого-то"), ("dative", "Form"): ("кто-тому", "кому-то"), ("accusative", "Form"): ("кто-то", "кого-то"),
               ("instrumental", "Form"): ("кто-том", "кем-то"), ("prepositional", "Form"): ("кто-том", "ком-то")},
    "что-нибудь": {("genitive", "Form"): ("что-нибудьго", "чего-нибудь"), ("dative", "Form"): ("что-нибудьму", "чему-нибудь"),
                   ("instrumental", "Form"): ("что-нибудьм", "чем-нибудь"), ("prepositional", "Form"): ("что-нибудьм", "чём-нибудь")},
    "какой-нибудь": {("genitive", "Form"): ("какой-нибудьго", "какого-нибудь"), ("dative", "Form"): ("какой-нибудьму", "какому-нибудь"),
                     ("instrumental", "Form"): ("какой-нибудьм", "каким-нибудь"), ("prepositional", "Form"): ("какой-нибудьм", "каком-нибудь")},
    "нечего": {("genitive", "Form"): ("нечегого", "нечего"), ("dative", "Form"): ("нечегому", "нечему"),
               ("instrumental", "Form"): ("нечегом", "нечем"), ("prepositional", "Form"): ("нечегом", "не о чем")},
    "пол": {("accusative", "sg"): ("пола", "пол"), ("accusative", "pl"): ("полов", "полы")},
    "половник": {("accusative", "sg"): ("половника", "половник"), ("accusative", "pl"): ("половников", "половники")},
    "гостья": {("genitive", "pl"): ("гостей", "гостий"), ("accusative", "pl"): ("гостей", "гостий")},
    "довести": {("past", "m"): ("довесл", "довёл"), ("past", "f"): ("довесла", "довела"), ("past", "n"): ("довесло", "довело"),
                ("past", "pl"): ("довесли", "довели")},
    "неумеха": {(c, n): ("неумехи", f) for c, forms in zip(CASES, [("неумеха", "неумехи"), ("неумехи", "неумех"), ("неумехе", "неумехам"),
                                                                     ("неумеху", "неумех"), ("неумехой", "неумехами"), ("неумехе", "неумехах")])
                for n, f in zip(("sg", "pl"), forms)},
}
STRESS = {"колледж": ("ко́лледж", "колле́дж")}      # lexicon stress and the stress of the notes' words with that lemma


def expand_endings(cell: str, lemma: str) -> str:
    """"нервный / -ого" -> "нервный / нервного": an abbreviated second form is written out (adjectives only)."""
    if "/" not in cell or "-" not in cell:
        return cell
    for end in ("ый", "ой", "ий"):
        if lemma.endswith(end):
            stem = lemma[:-len(end)]
            return " / ".join(p if not p.strip().startswith("-") else stem + p.strip()[1:] for p in (x.strip() for x in cell.split("/")))
    return cell


def fix_table(lemma: str, pos: str, table: dict) -> int:
    n = 0
    heads = table["columns"]
    for r in table["rows"]:
        for c in range(1, len(r["cells"])):
            old = r["cells"][c]
            new = old
            fix = CELLS.get(lemma, {}).get((r["cells"][0], heads[c] if c < len(heads) else ""))
            if fix and old == fix[0]:
                new = fix[1]
            if pos == "adj":
                new = expand_endings(new, lemma)
            if new != old:
                r["cells"][c] = new
                n += 1
    return n


def main():
    root = Path(sys.argv[1] if len(sys.argv) > 1 else "out")
    cells = files = stress = 0
    for f in sorted(root.rglob("scene-??.notes.json")):
        d = json.loads(f.read_text(encoding="utf-8"))
        hit = 0
        for L in d["lexicon"].values():
            for t in [L.get("forms")] + list(L.get("moreForms") or []):
                if t:
                    hit += fix_table(L["lemma"], L.get("pos"), t)
            old, new = STRESS.get(L["lemma"], (None, None))
            if old and L.get("stress") == old:
                L["stress"] = new
                hit += 1
                stress += 1
        for line in d.get("lines") or []:
            for w in line.get("words") or []:
                old, new = STRESS.get(w.get("lemma"), (None, None))
                if old and w.get("stress") and old in w["stress"]:
                    w["stress"] = w["stress"].replace(old, new)
                    hit += 1
                    stress += 1
        if hit:
            f.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            files += 1
            cells += hit
    print(f"{cells} cells / stresses fixed in {files} files ({stress} stresses)")


if __name__ == "__main__":
    main()
