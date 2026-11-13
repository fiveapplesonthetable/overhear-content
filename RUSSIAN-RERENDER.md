> **ON HOLD (November 13, 2026): do not follow this file.** The stress marks it adds cause mispronunciations. See
> [RUSSIAN-STRESS-HOLD.md](RUSSIAN-STRESS-HOLD.md).

# Re-render all Russian originals (dvorik-u-mosta), November 2026

Owner: the A100 render agent. Feedback issue: #57 ("замок" said as за́мок, "castle", instead of замо́к, "lock").

## What went wrong

`render/textprep.py` reads `render/data/ru_homographs.txt.gz`. That is the list of Russian words whose stress changes their
meaning (замок, уже, дома, …). Under the `homographs` stress policy, the only one the Russian engine uses, a word gets its
stress mark (U+0301) in the TTS text only if it is on that list. The stress check (`render/stresscheck.py`) also checks only
words on that list.

The file was never committed to this repo. When it was missing, `homographs()` silently returned an empty set. So:

- No Russian sentence was ever sent to the TTS with a stress mark. The model guessed every stress, and it sometimes guessed
  wrong (#57).
- The stress check had no words to check, so every scene passed. A local re-render of dvorik s02e01 scene 1 flagged
  0 of 190 words.

Scope: every Russian original, all 120 scenes of `dvorik-u-mosta` (s01e01–s03e03, 8 scenes each). With the list in place,
2,349 Russian sentences send different text to the TTS (328 distinct words now carry a mark: посмотри́те, уже́, до́ма,
звоно́к, …). Other languages are not affected.

## What changed in the repo

- `render/data/ru_homographs.txt.gz` is committed (19,741 words, from `render/tools/extract_homographs.py`).
- `textprep.homographs()` raises `FileNotFoundError` when the file is missing, instead of returning an empty set.
- The render key of a Russian scene includes a hash of the list (`plan.render_key`, `"homographs"`). Every dvorik scene is
  therefore **stale** now, and `pipeline.py --status` shows it. A sentence whose text did not change keeps its cached take.

## What to do

1. Pull this commit on the A100 (`git pull --ff-only` in the render checkout).
2. `python3 -I render/pipeline.py --status`. Expect all 120 `dvorik-u-mosta` scenes to be stale. If the command fails with
   `ru_homographs.txt.gz is missing`, the checkout is old. Pull again.
3. Render the show with the Russian profile:
   `OVERHEAR_RENDER_SETTINGS=render/settings.ru-qwen-lora-en.json python3 -I render/pipeline.py --root originals --show dvorik-u-mosta`
   Use the same voices as before (matvey = ru-m4, narrator = sky). Do not change voices or settings in the same run.
4. Check that the stress check is actually working:
   - In each scene's `report.json`, look at `stress.sentencesFlaggedInitially` and `stress.wordsFlagged`. Across the show,
     some sentences should be flagged and then retaken. If every scene still reports 0, which is what the broken runs
     reported, stop and investigate. `wordsChecked` alone proves nothing: it counted 190 words even when the list was missing.
   - Listen to `dvorik-u-mosta-s02e01-scene-01`, segment 2: it must say **замо́к** (lock). `render/retakes.json` already
     asks for a new take of that segment.
   - Read each scene's `stress.unresolved`. Fix a word that stays wrong in the scene notes (`words[].stress`) or with a
     retake in `render/retakes.json`, never by editing audio or rendered JSON.
5. Ship one whole episode at a time: `tools/check_render.py` and then `tools/package_render.py … --episode
   dvorik-u-mosta-sNNeNN --release` (README, steps 12–13). Begin with s02e01, which contains #57.
6. After s02e01 is published, close #57 per `FEEDBACK-AGENT.md` with "Fix commit: <sha>".
7. Record the run (scenes, hours, number of flagged and unresolved words) in `originals/PROGRESS.md`.

## Next time

- A data file that the render depends on must be committed, and loading it must fail loudly. A missing file must never
  silently mean "nothing to do".
- A check that never fires is a broken check. When you add or change a gate, run it on a known bad sample, for example
  a за́мок take, and confirm that it flags it.
- Anything that changes the text sent to the TTS must be part of the render key, so affected scenes become stale on their
  own and nobody has to remember to force a re-render.
