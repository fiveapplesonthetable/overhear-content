# overhear-content: brief for the content agent

> **Latest review: read FEEDBACK.md first.** It lists what must change in the existing output (with counts and the exact
> expected form), the new rules, and the command that has to print `OK`.

You are making the story content for **Overhear**, an app that teaches Russian and French by turning scenes of TV shows
into short narrated listening stories. You have **no app code and no other context**: this repository is everything.
Work through it all day without asking questions; where something is ambiguous, pick the reading that follows the rules
below, note the decision in `out/<show>/NOTES.md`, and carry on.

## Mission
Turn **every scene of every episode** of these shows, in order, into a listening story for learners, each with
a script, annotations and one picture:

| show | slug | language | sidecars in `sources/` |
|---|---|---|---|
| Кухня (Kukhnya) | `kukhnya` | ru | S1 e01-20, S2 e01-03 dual; S2 e04-S6 e20 Russian only, `eNN.ru.srt` (see `sources/INDEX.md`) |
| Dix pour cent (Call My Agent!) | `dix-pour-cent` | fr | S1-S4, 6 episodes each |
| Домашний арест (Domashniy Arest) | `domashniy-arest` | ru | S1 e01-12 |

Structure: **Show -> Season -> Episode -> Scenes** (a movie would be Movie -> Scenes). The **first scene of an episode
carries the full intro** (the show, who the characters are, the setting, what the episode is about). **Later scenes open
with a short bridge and recap** ("Meanwhile, back in the kitchen, ... "), so each works alone and also back to back with
its neighbours. Every scene is one story following the 5-part recipe in `spec/recipe.md`: narrator intro, whole story
in the target language, narrator walk-through, whole story again, send-off plus one short target-language line.
The narrator speaks **English only**, calm, no hype. Target-language text must read **naturally to a native speaker**.
**No stress marks anywhere except inside `stress` fields.** Learner level: A1 (see recipe).

## What is where
| path | what |
|---|---|
| `sources/<show>/sNN/eNN.<lang>.dual.srt` or `eNN.ru.srt` | the subtitles: `dual` = for each cue the original line, then its English; `eNN.ru.srt` = Russian only (Whisper transcript, may contain recognition errors; Kukhnya S2 e04 - S6 e20). Copyrighted show material, input only. |
| `sources/INDEX.md` | coverage, cue counts, running time per episode |
| `spec/recipe.md` | cast, voices, level, tone, 5 parts, gaps, text rules |
| `spec/script-format.md` | `scene-NN.json` field by field |
| `spec/scenes-format.md`, `spec/scenes.example.json` | `scenes.json` |
| `spec/annotations.md` | `scene-NN.notes.json`: translations, word notes, lemma, POS, stress, meanings, forms |
| `art/style/` | house style, reusable prompt (`STYLE.md`), 9 reference pictures, SVG sources |
| `examples/` | three finished models: `kukhnya-s01e02-knife`, `kukhnya-s01e05-orders`, `dix-pour-cent-s04e01-agence` (each: `scene.json`, `authoring.py`, `REVIEW.md`, `art.webp`, `sample.mp3` (a low-bitrate sample of how it sounds); the knife one also has `scene.notes.json`, an excerpt of the annotation format). Read them before starting. |
| `spec/schema/*.schema.json` | JSON Schemas (draft 2020-12, versioned by `schemaVersion`) for `scenes.json`, `scene-NN.json`, `scene-NN.notes.json`; `validate.py` enforces them |
| `tools/validate.py` | the checker (stdlib only) |
| `tools/compose.py` | authoring module -> `scene-NN.json` with correct gaps + `REVIEW.md` |
| `tools/gaps.py` | lists silences between cues to find scene breaks |
| `out/` | **your output** |

**Do not edit `examples/` or `sources/`.** No audio: voices and timing are produced elsewhere. Don't make mp3s.

## Priority order
1. Kukhnya S1, e01 -> e20 in order.
2. Dix pour cent S1, e01 -> e06.
3. Domashniy Arest S1, e01 -> e12.
4. Kukhnya S2 e01-03, then Dix pour cent S2, S3, S4.
5. Kukhnya S2 e04 -> S6 e20 last. These are `eNN.ru.srt`: Russian only, machine transcribed (Whisper), complete for every
   episode; **no English dual subtitles are coming, so do not wait for them**. Do them only after everything above, in
   order, working from the Russian-only file: translate it yourself for your own understanding, and in
   `out/kukhnya/NOTES.md` note that the transcript may have recognition errors (and list any line you suspected was
   misheard and how you read it). Where a cue looks garbled, prefer a line you are sure of or leave it out. If an
   `eNN.ru.dual.srt` ever does appear next to one, use that instead.

Finish an episode completely (all scenes, notes, art, validated, pushed) before starting the next.

## Workflow for one episode (`<show>`, `sNNeNN`)
1. **Read the subtitles** in `sources/<show>/sNN/eNN.<lang>.dual.srt` (or `eNN.ru.srt` for the Russian-only Kukhnya episodes; skim all of it; you need the plot). Read the
   previous episode's `scenes.json`/`NOTES.md` and `out/<show>/characters.md` for continuity.
2. **Break it into scenes.** Run `python3 tools/gaps.py <srt>` to list silences, then read the lines around each gap.
   Split on **time gaps, a change of who is speaking or present, and a change of location**. Capture **every** scene,
   skip none: the scenes must cover the whole file from first to last cue (the validator enforces it). A very short
   transitional scene (a few lines, no plot of its own) is **not dropped**: keep it in the list with `merge: "prev"` or
   `"next"`. Write `out/<show>/sNNeNN/scenes.json` ([format](spec/scenes-format.md)). Typical: 5-12 scenes per episode.
   Opening titles and credits belong to the neighbouring scene, not their own.
3. **Character sheet.** Add any new character/place to `out/<show>/characters.md` (start from `out/TEMPLATE-characters.md`):
   name, role in the show, how to draw them (hair, clothes, colours, prop), their story role key and label.
4. **Write each (non-merged) scene** `scene-NN`: an authoring module `out/<show>/sNNeNN/authoring/scene-NN.py`
   (copy the closest `examples/*/authoring.py`), borrowing short real lines from the cues of that scene's time range,
   then `python3 tools/compose.py out/<show>/sNNeNN/authoring/scene-NN.py --out out/<show>/sNNeNN/scene-NN.json`.
   Fix every PROBLEM it prints. Scene 1 gets the full intro; later scenes the bridge and recap. Keep the recipe's 5 parts, A1 level,
   12-18 story lines, 2 (max 3) speaking roles. The compose step also writes `scene-NN.REVIEW.md` (commit it).
5. **Annotate** each scene: `out/<show>/sNNeNN/scene-NN.notes.json` ([format](spec/annotations.md)): English translation of
   every target-language segment, per-word lemma/POS/stress/gloss/grammar, and a lexicon entry per lemma with meanings and
   forms tables. Be correct: check gender, aspect pairs, conjugations, IPA.
6. **Art**: one image per scene, `scene-NN.webp` (1024x1024), per `art/style/STYLE.md`, drawing characters exactly as in
   `characters.md`. Look at the picture before accepting it: no text in it, right characters, readable small.
7. **Validate**: `python3 tools/validate.py out/<show>/sNNeNN --require-notes` must print `OK` (read the warnings too, and fix
   those that are real; subtitle-gap warnings can be explained in `NOTES.md`). Also `python3 -m unittest discover -s tests`
   if you touched the tools (you shouldn't).
8. **Commit and push**, one episode per commit: add the episode folder, update `out/PROGRESS.md` and `characters.md`, then
   `git add -A && git commit -m "<show> sNNeNN: N scenes" && git push`. Push after every episode. If push fails, retry; never
   force-push, never rewrite history.
9. Next episode.

## Output layout
```
out/
  PROGRESS.md
  <show>/
    characters.md            # people and places, for art consistency
    NOTES.md                 # decisions, open questions, anything odd (append)
    s01e01/
      scenes.json            # the breakdown
      scene-01.json          # script (episode JSON format)
      scene-01.notes.json    # annotations
      scene-01.webp          # art, square 1024
      scene-01.REVIEW.md     # from compose.py
      authoring/scene-01.py  # source of scene-01.json
      scene-02.json ...      # a merged scene has no files of its own, only its entry in scenes.json
```

## Rules recap
- Narrator English only; never target-language words in narrator lines (replay them as separate target segments).
- Target language: natural, A1, polite/familiar register correct for the relationship; French punctuation attached
  (`là?`), straight apostrophes; Russian Cyrillic only.
- No stress marks outside `stress`; no emoji; no text inside images.
- Tie each borrowed line to its cue (`source.lines`), the validator checks the fragment exists in that cue.
- Don't invent plot: the story must match what happens in that stretch of the episode. Don't quote long runs of
  dialogue: short lines only.
- Never output audio; never edit `examples/`, `sources/`, `tools/`, `spec/`; never commit secrets or credentials.
- Every JSON file you write carries `"schemaVersion": 1` and follows `spec/schema/` exactly (no extra fields, no renamed
  fields). `compose.py` writes it for scripts; you add it to `scenes.json` and `scene-NN.notes.json`.
- Scene ids and filenames are stable: once published, `<show>-sNNeNN-scene-NN` never changes meaning. Editing a published
  scene in place is fine (and expected when FEEDBACK.md asks for it); renumbering scenes is not.
- The last segment of a script is a short new farewell (`Пока!`, `À bientôt!`), never a repeat of a story line.
- A character keeps one role key (their own name) for the whole show; every key is in `out/<show>/cast.json`; scripts have no `voices`. Read FEEDBACK.md "P-1" first.
- Run the validator before every push: `python3 -I tools/validate.py out --require-notes` must print `OK`.

## Learning notes and word histories

`learn/<pair>/<id>.json` holds focused learning notes with checked source-scene examples. French examples are italicised in English prose so the app can recognise the target-language spans. Keep explanations specific and avoid claims that a word has one fixed translation in every construction.

`dictionary/<pair>.json` can provide written dictionary entries before scene audio exists. `word-origins/<pair>.json` holds etymology, historical forms, word parts, cognates, word families and source links. These are separate from the scene render inputs: editing them does not invalidate audio. Their versioned schemas are in `spec/schema/`. Restored records retain their previous certainty labels; a dictionary check can correct an older claim and add a source.

For changes confined to these metadata folders, run `python3 -I tools/validate.py . --metadata-only` and the unit tests. Full corpus validation remains required for scene changes; known problems in the unrendered corpus are not hidden by the metadata check.
