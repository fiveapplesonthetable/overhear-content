#!/usr/bin/env python3
"""Rebuild sources/INDEX.md: per show/season, the episodes present, cue counts, running time."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from validate import parse_srt, fmt, ROOT, SHOWS

EXPECT = {"kukhnya": {1: 20, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}, "dix-pour-cent": {1: 6, 2: 6, 3: 6, 4: 6},
          "domashniy-arest": {1: 12}}   # 0 = season total unknown / not on put.io (only what is present is listed)
NAMES = {"kukhnya": "Кухня (Kukhnya)", "dix-pour-cent": "Dix pour cent (Call My Agent!)", "domashniy-arest": "Домашний арест (Domashniy Arest)"}
out = ["# Subtitle sources: coverage", "",
       "`sources/<show>/sNN/eNN.<lang>.dual.srt`: each cue = original line + English line. Episode titles are not carried by the sidecars;",
       "if you learn an official title, put it in `scenes.json` `title`.", ""]
for show in SHOWS:
    out += [f"## {NAMES[show]}  (`{show}`, {SHOWS[show]})", "", "| season | present | missing | episodes (cues, length) |", "|---|---|---|---|"]
    seasons = sorted(set(list(EXPECT[show]) + [int(p.name[1:]) for p in (ROOT / "sources" / show).glob("s*")]))
    for s in seasons:
        files = sorted((ROOT / "sources" / show / f"s{s:02d}").glob("e*.dual.srt"))
        have = {int(f.name[1:3]) for f in files}
        exp = EXPECT[show].get(s, 0)
        missing = [e for e in range(1, exp + 1) if e not in have]
        det = []
        for f in files:
            c = parse_srt(f)
            det.append(f"e{f.name[1:3]} ({len(c)}, {fmt(max(x[1] for x in c.values()))[:8]})")
        if exp == 0:
            out.append(f"| S{s} | {len(have)}/? | season total unknown; rest not on put.io | {'; '.join(det) or '-'} |"); continue
        mtxt = ("e" + ",".join(f"{e:02d}" for e in missing)) if missing and have else ("all" if missing else "none")
        out.append(f"| S{s} | {len(have)}/{exp} | {mtxt} | {'; '.join(det) or '-'} |")
    out.append("")
(ROOT / "sources" / "INDEX.md").write_text("\n".join(out) + "\n", encoding="utf-8")
print("\n".join(out))
