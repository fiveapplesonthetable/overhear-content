# Re-gate the failed form clips (ar, hi, ja, ko, fr), November 2026

Owner: the A100 render agent. Applies to the forms store (`<store>/forms/`), pairs `ar-en`, `hi-en`, `ja-en`, `ko-en`, `fr-en`.

## What went wrong

A form clip is one word (a table cell). It is voiced, transcribed with Whisper, and compared with the text by spelling CER.
After 3 tries over `cerMax` 0.15 the record becomes `status: "failed"`, the audio is deleted, and the app plays nothing when
that form is tapped.

On one word, one letter is 20 % or more of the CER, and Whisper picks one of several valid spellings of what it hears. So
correct audio failed. Hindi `लाएगा` was heard as `लाइगा` (cer 0.2), Korean `칸이` as `카니` (1.0), Japanese `はまって` as
`ハマって` (0.5), French `ils/elles comparent` as `Il compare, elle compare.` (0.21).

Failed records in the store, before this change:

| pair | failed | of | rate |
|---|---|---|---|
| ar-en | 2006 | 7399 | 27.1 % |
| hi-en | 815 | 2646 | 30.8 % |
| ja-en | 681 | 4708 | 14.5 % |
| ko-en | 850 | 9627 | 8.8 % |
| fr-en | 1136 | 13961 | 8.1 % |

Analysis of those records, using the stored `hyp` (nothing re-synthesised):

| pair | same sound, other spelling | different word, near (0.15 to 0.3) | different word, far | hallucination / empty / very long |
|---|---|---|---|---|
| ar-en | 619 | 767 | 548 | 72 |
| hi-en | 159 | 315 | 299 | 42 |
| ja-en | 474 | 105 | 100 | 2 |
| ko-en | 332 | 232 | 138 | 148 |
| fr-en | 920 | 143 | 72 | 1 |

"Same sound" is what the new gate passes. The rest are real failures of the voice (Hindi and Arabic are the weak ones, and
Korean has 148 clips where Whisper heard nothing and wrote "다음 영상에서 만나요."). They stay failed and are retried.

## What changed in the repo

- `render/form_gate.py` (new). Both sides are reduced to sound units per language and compared with a weighted edit
  distance: the same sound costs 0, a pair people confuse costs 0.5, a different sound costs 1, divided by the number of
  sounds in the target (at least 4, so one confusable sound never fails a very short word, and one different sound still does).
  - hi: vowel letters = matras, no nukta, chandrabindu = anusvara, halant/schwa and doubled consonants folded,
    short/long vowel and aspirate pairs half a point, a missing nasal mark half a point.
  - ar: no harakat/shadda/tatweel, alef and hamza forms, ى = ي, ة = ه, spaces ignored; a missing long-vowel letter inside
    the word is half a point, a missing last letter is a whole one (that is a missing suffix); emphatic/plain pairs half a point.
  - ja: reading in hiragana via pykakasi (already in `venv-asr`), digits read as kanji numerals, long vowels folded.
  - ko: syllables as heard (final consonant carried into a following vowel syllable, finals neutralised, ㅐ = ㅔ);
    a syllable that differs only by a lax/tense/aspirated pair is half a point.
  - fr: a rough per-word grapheme-to-sound pass (silent endings, -er/-é/-ez, ou, on, an, ph, qu, ...).
  - The gate is `min(spelling CER, sound distance)`: it passes more than before and never fewer. Other languages are unchanged.
- `clip_asr.comparison_cer` uses it for `--kind forms`. Example clips (`--kind clips`) are unchanged.
- `GATE_VERSION` (`fg1`) is written into every failed record (`clips.fail_final`). `ClipStore.is_done` treats a failed
  record without the current version as **stale**. A failed record keeps no audio, so the forms are rendered and checked
  again on the next run: the cached Qwen take is reused when it exists (no new synthesis), then Whisper judges it with the new gate.
  Passed clips are untouched (a gate change never makes a pass stricter). Changing any rule or cost in `form_gate.py`
  must bump `GATE_VERSION`; that alone makes the affected failures stale.
- `forms.spoken_form(lang, cell)` is the text the voice is asked to say (factored out of `forms.plan`).
- `python3 render/form_gate.py --store <store>` is a dry run on the stored hyps (no GPU, no audio).

## What to do

1. Pull this commit on the A100 (`git pull --ff-only` in the render checkout).
2. Dry run, to see what the new gate will do with the stored failures:
   `$OVERHEAR_HOME/venv-asr/bin/python -I render/form_gate.py --store <store>` (the `--store` of `pipeline.py`; ja needs `pykakasi`,
   which that venv has). Expected on the s02 store, which has the same records:
   ar-en 27.1 % -> 18.7 %, hi-en 30.8 % -> 24.8 %, ja-en 14.5 % -> 4.4 %, ko-en 8.8 % -> 5.4 %, fr-en 8.1 % -> 1.5 %.
   `--show 20` prints the nearest misses that still fail.
3. Re-run the forms, one pair at a time, with that pair's usual settings file (the failed records of that pair are now pending):
   `OVERHEAR_RENDER_SETTINGS=render/settings.<pair settings>.json python3 -I render/pipeline.py --forms-only`
   (`--forms-limit N` for a checkpoint, `--max-minutes` as usual). Settings: ja `settings.ja-qwen-en.json`, ko `settings.ko-qwen-en.json`,
   fr `settings.fr-qwen-en.json`, hi `settings.hi-chatterbox-en.json`, ar `settings.ar-chatterbox-en.json`.
   Do not change voices or settings in the same run.
   Start with ja-en and fr-en: they recover the most and need the least GPU time.
4. Verify:
   - Count `status: "failed"` per pair again (`form_gate.py --store` prints it). The rates must fall to about the table above, plus whatever the
     retakes win back. `pipeline.py` logs `forms dropped <id>: <text> heard <hyp> cer <c>` for every form that still fails.
   - `render/tests/test_form_gate.py` must pass in the ASR venv. It holds the known-bad samples (hi `हटाओगे` heard `अटाओगे`, ar `قلقوا` heard `غلقوا`,
     ko `창고를` heard `참고를`, ja `方だった` heard `型だった`, fr `pull` heard `Poules.`, and hallucinated hyps). All of them must fail the gate. If
     one passes, stop and fix the gate before shipping.
   - Listen to 10 newly passed clips per pair that were failed before (`status: "ok"`, `tries` 1 to 3, `renderedAt` today). They must say the
     target word. A clip that says another word means the gate is too loose for that language: report it, do not ship.
5. Ship through the normal publisher run. A form is shipped only when its record is `ok` and its `ckey` is in `.plan.json`; nothing else changes.

## Next time

- A gate that decides on spelling will reject correct audio in languages with several spellings for a sound. Compare what is
  heard, not how it is written, and score short words so that one letter cannot decide.
- Re-calibrate on the failed records whenever a gate changes: bucket them (same sound / different word / nothing heard) and check
  that known-bad samples still fail. A looser gate that passes a wrong word is worse than a strict one.
- A failure that deletes its audio cannot be re-judged later. Anything that decides a drop must be part of what makes the record
  stale (`GATE_VERSION`), so a gate change retries exactly those records and nobody has to remember to force it.
- Languages not covered here (de, es, it, pt, ru, and the English forms in the `en-*` pairs, which fail on homophones such as
  buy/bye) still use the spelling CER. Add a normaliser to `form_gate.py` and bump `GATE_VERSION` if their failure rate matters.
