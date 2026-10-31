# Arabic pilot scope and validation

One short Al Maktab S1E1 taster: four retained source utterances, 14 native written words, 20 script segments. The partial SRT is bound by the explicit excerpt coverage hash. This does not claim a complete episode, a season, or the whole 94-second official clip transcript.

Validation on the frozen content:

- `python3 -I tools/validate.py out/al-maktab/s01e01 --strict-teaching --require-notes`: 0 errors; one expected warning that the deliberately short taster has four story lines. Teaching is 4/4, 100%.
- `python3 -I tools/validate.py . --metadata-only`: 0 errors.
- Existing taster-contract and native-span suites: 22 + 8 tests pass.
- Authoring composes reproducibly to the script; both stronger independent source decoders corroborate every retained word; all native translations match authoring across replays. All 44 word spans select the exact original logical substring. The final art is inspected, 1024×1024 WebP.

All 14 ordinary dictionary lemmas now have specifically checked word histories, alongside two source-linked Learn notes. Their 27 italic native word occurrences (12 distinct surfaces) all resolve to reviewed dictionary lemmas and sourced histories. No extra practice vocabulary, filler etymology or guessed pronunciation is used. Historical disputes and reconstructions are labelled. Arabic stress fields remain null under the native-script contract. The authored completeness proof is private `arabic-research/authored-origin-coverage-complete.json`; the actual serving-candidate `origin_coverage --require-complete` check remains a publication gate once production has real approved audio.

Final public native speech is synthesized, not copied from the show. GPU voice trials, complete speech/pronunciation checks, acoustic word timing, serving verification and actual-device Arabic/RTL checks remain production responsibilities before publication. Original media and reference WAVs stay private. Source and speaker decisions are documented in `s01e01/authoring/SOURCE-REVIEW.md`.
