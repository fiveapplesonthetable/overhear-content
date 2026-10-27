# Kukhnya (Кухня) — Authoring & Validation Notes

## Timing Gap Warnings (`validate.py`)
- `tools/validate.py` emits `WARN ... gap to prev is ...s (> 10s)` when music montages, kitchen prep sequences, or exterior transitions occur between subtitle cues in `.dual.srt`. All spoken subtitle cues from cue 1 to the final cue of each episode are covered contiguously in `scenes.json`.

## Voice Assignment Convention
- Per `spec/recipe.md`, every scripted scene maps its primary speaker to role key `anya` (`alisa`), and supporting speakers to `anja` and `angelina`. Kitchen slang and mild insults (e.g., *огузок*, *инвалиды*) are adapted to clean A1–A2 Russian suitable for language learners.
