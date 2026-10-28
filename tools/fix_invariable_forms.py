#!/usr/bin/env python3
"""Give invariable Russian nouns (казино, фсб) a real `forms` table. Stdlib only.   python3 tools/fix_invariable_forms.py [out]

The validator wants a forms table for every Russian noun/adj/verb, and a one-column table is not allowed (migrate_v1.py
turned those into null). For an indeclinable noun the honest table is one form in every case, so that is what is written.
Only Russian nouns whose forms are null are touched; the lemma is the form."""
import json, sys
from pathlib import Path

CASES = ["nominative", "genitive", "dative", "accusative", "instrumental", "prepositional"]
n = 0
for f in sorted(Path(sys.argv[1] if len(sys.argv) > 1 else "out").rglob("scene-??.notes.json")):
    if f.parent.parent.name == "dix-pour-cent": continue
    d = json.loads(f.read_text(encoding="utf-8")); hit = False
    for k, L in d["lexicon"].items():
        if L["pos"] == "noun" and L["forms"] is None:
            L["forms"] = {"title": "Declension", "columns": ["", "sg"], "rows": [{"cells": [c, k]} for c in CASES]}
            hit = True; n += 1
    if hit: f.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(n, "entries")
