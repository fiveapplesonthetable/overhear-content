# Standing lesson requirements

Read `spec/OUTPUT-CONTRACT.md`, `spec/ORIGINALS.md`, `spec/script-format.md`, `spec/annotations.md`, `spec/voices.md`, and `word-origins/README.md` before authoring or rendering. Keep their exact file formats and the established five-part lesson template.

- Learner-facing titles and descriptions contain the story name and premise only. Keep TTS providers, model names, trial labels and implementation details in technical metadata and documentation.
- Match the actual published reference `originals/dvorik-u-mosta/s01e01/scene-01.json`: introduction, whole conversation, each line replayed followed only by its quoted translation, unchanged replay, closing and farewell. No added spoken explanations or embellishments. Keep grammar, forms and histories in the written notes.
- Use the established simple flat SVG artwork style by default. Inspect the rendered image at full size and thumbnail size before publication. If generated characters are used, reject extra limbs, malformed hands, bad anatomy and broken object contact; a more capable model does not replace visual review.
- Narrators are always female: warm, relaxed, clear and conversational. English is always British English, in the established Southern British storytelling style. Other narration languages use a comparable native female voice. Character dialogue retains its individual casting.
- A different TTS provider replaces speech generation only. Preserve introduction, story, line-by-line replay with quoted translation only, exact replay and outro; complete notes, translations, forms, examples, art and sourced etymologies/history remain required.
- New original stories belong in `originals/`, packaged as `original-<episode>` for the ordinary public catalogue. Adaptations in `out/` remain private. Never republish private adaptations publicly or change that catalogue as a side effect.
- Validate with `--require-notes --strict-teaching`; check the render, authentic word timing, example/form assets and word-history coverage for the new season. Include grammar words and names. Use sourced, qualified histories, not invented explanations.
- A persistently failed optional dictionary recording follows the existing failed-clip path: keep its written forms and omit its audio button. Report it, keep the quality gate, and proceed with otherwise valid scene publication. Missing scene speech/timing still blocks publication.
- Use existing authenticated access before asking for keys. Never commit or print secrets. Preserve provider/model/voice instructions and usage for every billable request, including tests and retries.
- “Live in the app” requires server readback of the title, episode, scene, catalogue versions and referenced assets. A GitHub release or uploaded MP3 alone is not sufficient. Separate speech estimates, promotional credits, actual billing and unknown charges.

The Google trial reference is `originals/last-train-google/README.md` and `google-voices.json`; it does not change the default voices of other episodes. The publisher repo's `publish/CONTENT-RUNBOOK.md` documents receiver selection, additive catalogue checks and remote verification.
