#!/usr/bin/env python3
"""Replace placeholder text that leaked from an old summary into narrator lines. Stdlib only.   python3 tools/fix_placeholder_narration.py [out]

Narrator intros/outros of the form `[Focused on X, ](ENG |The characters discuss their situation. )<garbled cue text> Let's listen...`
(or `... Next time you watch ...`) get the scene's own summary from scenes.json in place of everything before "Let's listen" /
"Next time". The summary is the hand-written one (see FEEDBACK.md), so no new facts enter the narration."""
import json, re, sys
from pathlib import Path

PAT = re.compile(r"^(?:Focused on [^,]+, |In this scene focused on [^,]+, )?(?:ENG |The characters discuss their situation\. ).*?(?= (?:Let's listen|Next time))", re.S)
n = 0
for ep in sorted(Path(sys.argv[1] if len(sys.argv) > 1 else "out").glob("*/s??e??")):
    sc = {s["scene"]: s for s in json.loads((ep / "scenes.json").read_text(encoding="utf-8"))["scenes"]}
    for f in sorted(ep.glob("scene-??.json")):
        d = json.loads(f.read_text(encoding="utf-8")); hit = False
        summary = sc[d["scene"]]["summary"]
        for g in d["segments"]:
            if g["v"] == "narrator" and PAT.match(g["t"]):
                g["t"] = PAT.sub(lambda m: summary, g["t"], count=1); hit = True; n += 1
        if hit: f.write_text(json.dumps(d, ensure_ascii=False, indent=2 if f.read_text(encoding="utf-8").startswith('{\n  "') else 1) + "\n", encoding="utf-8")
print(n, "narrator lines rewritten")
