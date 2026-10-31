# Arabic pilot scope and validation

One short Al Maktab S1E1 taster: four retained source utterances, 14 native written words, 20 script segments. The partial SRT is bound by the explicit excerpt coverage hash. This does not claim a complete episode, a season, or the whole 94-second official clip transcript.

Validation on the frozen content:

- `python3 -I tools/validate.py out/al-maktab/s01e01 --strict-teaching --require-notes`: 0 errors; one expected warning that the deliberately short taster has four story lines. Teaching is 4/4, 100%.
- `python3 -I tools/validate.py . --metadata-only`: 0 errors.
- Existing taster-contract and native-span suites: 22 + 8 tests pass.
- Authoring composes reproducibly to the script; both stronger independent source decoders corroborate every retained word; all native translations match authoring across replays. All 44 word spans select the exact original logical substring. The final art is inspected, 1024×1024 WebP.

Four checked ordinary-word histories and two source-linked Learn notes are included. The dictionary covers all 14 lemmas with contextual glosses and useful forms. Other word histories are not claimed complete; no filler etymology or guessed pronunciation is used. Arabic stress fields remain null under the native-script contract.

Final public native speech is synthesized, not copied from the show. GPU voice trials, complete speech/pronunciation checks, acoustic word timing, serving verification and actual-device Arabic/RTL checks remain production responsibilities before publication. Original media and reference WAVs stay private. Source and speaker decisions are documented in `s01e01/authoring/SOURCE-REVIEW.md`.
