# Russian stress marks: hold, then a gated re-render (November 13, 2026)

Owner: the A100 render agent and the feedback fixer. Feedback issue: #58 («чека» is heard as «чивка»).

## Stop now (until you have pulled the fix below)

- Do not render, retake or release any Russian (`ru`) audio: dvorik-u-mosta scenes, the Russian lines of any other
  pair, clips or forms. Stop a Russian run that is in progress. Other languages may go on.
- Do not continue [RUSSIAN-RERENDER.md](RUSSIAN-RERENDER.md). That re-render is what causes the problem.
- Do not close #58 with a retake. The retake in `render/retakes.json` (commit a5e3eebb6) sends the same marked text to the
  TTS, so the new take is most likely wrong in the same way. Leave #58 open.
- Do not pull or replace Russian audio that is already published. It stays live until the fixed renders replace it.

## What is wrong

Since the November 11 re-render, Russian homographs reach Qwen3-TTS with a stress mark (U+0301), for example
«три старых че́ка». The stress lands on the right vowel, but the model often changes the sounds around the mark.
Whisper large-v3 hears all three takes of that line in s01e01 scene 3 (segments 7, 26 and 45) as «три старых **чивка**».
3,378 of the 6,392 Russian sentences in dvorik-u-mosta carry at least one mark, so the fault can be in about half the show.

Both checks passed these takes:

- `stresscheck.py` aligns the audio to the intended text and compares vowel lengths. It cannot notice a sound that was
  added or changed, so it reports 0 flagged words.
- The Whisper gate in `gates.py` allows a sentence CER of 0.18 for non-English text. One wrong word in a sentence of
  about 40 letters is roughly 0.05, so it passes.

## How widespread

A sample of 150 Russian sentences from across the show was transcribed with Whisper large-v3-turbo:

| Words | Not heard as written |
|---|---|
| words with a stress mark | 38% (49 of 129) |
| unmarked words in the same sentences | 3.8% |
| sentences without any mark | 3.4% |

The model often turns the mark into an extra «ю» or «й» sound: «саюхара», «одиун», «хлеюба», «утраю», «ужею».

## The fix (render code, pushed with this file)

- `ttsRu.stress` is now `"onflag"` in `settings.ru-qwen-lora-en.json` and `settings.en-ru.json`. Russian goes to the TTS
  without marks. Only a word that the stress check flags, or that the transcript lacks, is retaken with a mark on that
  word alone. The marked take is kept only if it passes both checks.
- `render/wordcheck.py`: every in-scope homograph and every marked word must be in the take's Whisper transcript. A miss
  fails the take. It flags all three published «чека» takes, while the sentence CER gate passed them at 0.053.
- `report.json` gains `stress.heard` (`wordsRequired`, `wordsNotHeard`, `sentencesUnverified`), `retake.words` and
  `notHeard` in each `stress.unresolved` entry.
- The render key changes, so every dvorik-u-mosta scene is stale. A sentence that never carried a mark keeps its cached
  take. About 3,400 sentences that carried one are synthesized again.

## Re-render, gated

1. `git pull --ff-only`. Check that `ttsRu.stress` is `"onflag"` in `render/settings.ru-qwen-lora-en.json`.
2. `python3 -I render/pipeline.py --status`. All dvorik-u-mosta scenes should be stale.
3. Pilot, one scene, no release:
   `OVERHEAR_RENDER_SETTINGS=render/settings.ru-qwen-lora-en.json python3 -I render/pipeline.py --root originals --scene dvorik-u-mosta-s01e01-scene-03`
   Use the same voices and settings as before. Then cut segs 7, 26 and 45 from its `audio.mp3` and transcribe them with
   Whisper. All three must contain «чека». Also check that `stress.heard.wordsNotHeard` in its `report.json` is at most 2.
   If either check fails, stop: leave the hold on and write what you saw into `originals/PROGRESS.md`.
4. If the pilot passes, render and ship one whole episode at a time: s01e01 first (#58), then s02e01 (#57), then the
   rest. Use `tools/check_render.py`, then `tools/package_render.py … --episode dvorik-u-mosta-sNNeNN --release`.
   Before each release, read every scene's `stress.unresolved`. Release no episode whose scenes together have more than
   5 `notHeard` words. Fix those words in the notes or in `render/retakes.json`, never by editing audio or rendered JSON.
5. Close #58 after s01e01 is published, and #57 after s02e01, with "Fix commit: <sha>" as in `FEEDBACK-AGENT.md`.
6. Record each episode in `originals/PROGRESS.md`: scenes, hours, `wordsNotHeard`, `stillFlagged`.

Until a step's check passes, render no other Russian. Other languages may go on.
