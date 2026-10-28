#!/usr/bin/env python3
"""Help split an episode into scenes: list silences between subtitle cues and the lines around them.

  python3 tools/gaps.py sources/kukhnya/s01/e02.ru.dual.srt [--min 8]   # gaps of >= 8 s (default)
  (a Russian-only sidecar, sources/kukhnya/s02/e04.ru.srt, works the same way)
Also prints episode length and cue count. Big gaps are scene-break candidates; confirm by reading the
lines either side (who is speaking, where they are).
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from validate import parse_srt, fmt

import argparse
ap = argparse.ArgumentParser()
ap.add_argument("srt")
ap.add_argument("--min", type=float, default=8.0)
a = ap.parse_args()
mn, path = a.min, a.srt
cues = sorted(parse_srt(path).items())
print(f"{len(cues)} cues, last ends {fmt(max(c[1][1] for c in cues))}")
for (n1, c1), (n2, c2) in zip(cues, cues[1:]):
    if c2[0] - c1[1] >= mn:
        print(f"-- gap {c2[0] - c1[1]:5.1f}s  cue {n1} ends {fmt(c1[1])} | cue {n2} starts {fmt(c2[0])}\n     before: {c1[2][:70]}\n     after : {c2[2][:70]}")
