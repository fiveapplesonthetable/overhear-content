# HOLD: do not render or release Russian audio (November 13, 2026)

Owner: the A100 render agent and the feedback fixer. Feedback issue: #58 («чека» is heard as «чивка»).

## Stop now

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

## What happens next

The owner's session is fixing this in the render code:

1. By default, send Russian to the TTS without stress marks, as before November 11.
2. Keep a mark only for a word that the model stresses wrongly without one (for example замо́к, #57).
3. Add a per-word ASR check: every marked word must be heard as that word. If not, retake the sentence, and if it still
   fails, report it in `report.json`.
4. Test the new check on the «чивка» takes above and confirm that it flags them.

When that lands, this file will say how to re-render Russian, one episode at a time. Until then, render other languages
only.
