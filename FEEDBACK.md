# FEEDBACK: review of the content so far (2026-10-28)

From the Overhear side. Read this before touching anything else. Everything here is about one goal: **we ingest your
output exactly as it is, with zero manual fixing.** Today we cannot, for the reasons below.

## Read this first

- The output is **complete**: 59 episodes (Kukhnya 23, Domashniy Arest 12, Dix pour cent 24), 1617 scripts, 1617
  annotation files, 1617 pictures, 55 merged scenes. Every non-merged scene has `scene-NN.json`, `.notes.json`, `.webp`
  and `REVIEW.md`; ids are unique and match the folder; no stress mark leaks outside `stress` fields; no script title has
  stray spaces; every picture is a 1024x1024 webp. Keep all of that.
- The old validator said `OK` for all 59 episodes (0 errors, 2464 warnings) because it did not check most of what we need.
  **`tools/validate.py` now checks them, and the same run prints `FAIL: ~29,800 errors`.** The errors fall in 12 groups,
  listed below in the order to fix them. Most are mechanical and can be done by script over the existing files
  (editing in place is fine); a few need rewriting a line or a scene.
- **The command that must print `OK`:**

      python3 -I tools/validate.py out --require-notes
      python3 -I -m unittest discover -s tests

  Run it per episode while you work (`python3 -I tools/validate.py out/<show>/sNNeNN --require-notes`). Three checks are
  across the whole show (voices, lexicon, art) and are only judged when you run the whole of `out`, so run that before
  every push. The tool lists the first 150 errors and then a count by kind; to see all of them redirect the output to a
  file.
- Do the work in this order: **P0 (format) -> P1 (correctness of the data) -> P2 (content quality) -> new Kukhnya
  episodes (S2 e04+)**. Do not start new episodes until `out` validates `OK`; new episodes must pass from the start.
- Harmless, ignore: the 1400 `gap of Ns between scenes` warnings (music, prep sequences) and the 1064 `narrator line has
  French letters` warnings (accented names such as Andréa in English narration).

## New rules

1. **Schemas.** `spec/schema/{scenes,script,notes}.schema.json` (JSON Schema draft 2020-12) are the format. Every file has
   `"schemaVersion": 1` as its first field. A file with an unknown field, a missing field or a wrong value is an error.
   `characters.md` is prose and has no schema; its machine-read part is the backticked role keys (rule 5).
2. **Stable ids.** `<show>-sNNeNN-scene-NN` (script id, notes `id`, file names) never changes meaning once it is on
   `main`. Never renumber, never reuse a number for a different scene. **Editing a published scene in place is fine**
   (and is how you do the fixes below); we re-read the file, so you need not create anything new. If a scene must go,
   mark it `merge` in `scenes.json` only when its lines really fold into a neighbour; do not delete numbers.
3. **Closing line.** The last segment of every script is a short, new farewell by a speaking role: `Пока!`,
   `До свидания!`, `До встречи!`, `Хорошего дня!`, `Всего хорошего!`, `À bientôt!`, `Au revoir!`, `À demain!`, `Bonne
   soirée!` (max 6 words). Never a repeat of a story line.
4. **One voice and one role key per character per show.** The label (the character's name in `labels`) decides: same
   label, same role key, same voice, in every scene of the show. See "Voices" below.
5. **`characters.md` lists every role key** a script uses, as `Story role key / voice: \`key\` -> voice`, backticked.
   `anya` / `lea` are exempt (see Voices).
6. **Source ties stay inside the scene.** Every `source.lines[].cue` lies inside that scene's `start`-`end` (2 s slack).
   `source.file` is the sidecar you used (`.dual.srt`, or `eNN.ru.srt` for Russian-only episodes).
7. **Annotation tokens.** `words[].t` are the segment text split on whitespace, one entry per token, in order; nothing
   merged, nothing split; bare dashes (`—`) skipped. A word has `stress` (`null` only for names, one-vowel Russian
   words and `ё`; French always has IPA).
8. **One lexicon entry shape per lemma across the whole show** (same `pos`, `gender`, `aspect`, `pair`, `stress` every
   time), lowercase keys, Russian lexicon stress carries the mark.
9. **One picture per scene** (no byte-identical files in two scenes), 1024x1024 webp, no text, as before.
10. **No placeholder text** (`The characters discuss their situation.`, `ENG `) in `scenes.json` or in any narrator line.
    `scenes.json` `title` and `summary` are English only and have no double spaces.

## P0: format (all mechanical, all existing files)

Counts are from the validator on 2026-10-28. "files" = JSON files affected.

### 1. `scenes.json` (59 files)
Exact form: `{"schemaVersion": 1, "show", "season", "episode", "title", "scenes": [...]}`, each scene
`{"scene","start","end","title","summary","characters","location","merge"}` and nothing else.
- add `schemaVersion` (59 files).
- remove `source_file` (20 files), `total_cues` (19), `source` (1), and per scene `cue_start`/`cue_end` (580 scenes,
  21 files), `id`/`time_range`/`status` (555 scenes, 20 files; `id` is a string in 525 and an integer in 30), `merged_into`
  (2 scenes, 1 file). The scene id is derived, we do not need it stored.
- `title` is English only: 942 scene titles are in the bilingual `<target>  (<English>)` form (Kukhnya 551, Dix 314,
  Domashniy Arest 77). Keep only the English part. (The bilingual form belongs in `scene-NN.json`.)
- 99 summaries are placeholders or garbled (`The characters discuss their situation. -,   ,   -  ...`): Domashniy Arest
  s01e11 (35 scenes) and s01e12 (29), Kukhnya s01e01 (8), s01e19 (8), s02e02 (5), s02e03 (8), and the `ENG ...` ones.
  Write one real English line saying what happens.
- 4 empty `location` values (dix-pour-cent s04e06).

### 2. `scene-NN.json` (1617 files)
Exact form: see `spec/script-format.md` and `script.schema.json`.
- add `schemaVersion` (1617). `compose.py` now writes it, plus `show/season/episode/scene` derived from `ID`, so
  re-composing the scene does it for you.
- 25 scripts lack `show/season/episode/scene` (Kukhnya s01e01 to s01e08, scenes that were not recomposed).
- `level` must be exactly `"A1 — Duolingo Section 2"` (ru) / `"A1 — débutant"` (fr): 36 scripts say `"beginner"`, 27 say
  `"A1"` (Domashniy Arest 43, Kukhnya 20: s01e07 to s01e12, Kukhnya s01e01, s01e09, s01e10, s01e11).
- 2 narrator lines have trailing whitespace; one is fixed (see "What I changed"), one is the placeholder one in
  Kukhnya s02e03 scene-22 (item 4 below).

### 3. `scene-NN.notes.json` (1617 files)
Exact form: `spec/annotations.md` and `notes.schema.json`.
- add `schemaVersion` (1617) and `id` equal to the script's id (1369 lack `id`).
- remove `show`/`season`/`episode`/`scene` (246 files, the ones that have `id`).
- word field `grammar` -> `gram` (7202 words in 31 files; when both exist keep `gram`); word field `note` (1746 words in
  7 files) -> fold into `gram` or drop; `stress` key missing on 1423 words in 44 files (add it, value per rule 7).
- line field `text` (80 lines in 2 files, Kukhnya): drop.
- lexicon: `gender: null` (194 entries, 174 files): omit the key. `gender` other than `m|f|n`: `pl` (34), `mo` (19),
  `m/f` (12), `mf` (2), `fan`, `pwɛ̃`, `pisin` (spelling/IPA put in the wrong field): use the real `m`/`f`/`n`.
  Plural-only nouns (`деньги`, `выборы`, `ребята`, `дебаты`, `les vacances`): `"number": "pl"` (158 entries use
  `"number": "plural only"`), plus the usual gender when it exists.
- lexicon `aspect` must be `impf` or `pf`: `perf` 167, `imperf` 58, `imperfective` 42, `perfective` 35, `ipf` 1.
- lexicon `animacy` must be `anim` or `inan`: `inanimate` 49, `animate` 9, `inanim` 4; the 38 `"animate": true/false`
  fields become `animacy`; the 7 `transitivity` fields are dropped.
- lexicon `pos` is one of the 13 listed values: about 50 entries hold IPA or a word instead (`tudəsɥit` 24, `diʁɛktəmɑ̃`
  11, `ajœʁ` 3, `aj` 2, `lao` 2, `sudɛnmɑ̃`, `tʃin`, and the Russian `затем`/`близко`/`хреново`): these entries have
  their fields shifted; re-write them. `tout de suite` and `directement` are the commonest.
- `forms` is a table (>= 2 columns) or `null`: 10 entries have a one-column table (`сей`, `фсб`, `казино`): use `null`.
  48 entries lack `moreForms` (`[]`), 1 lacks `forms` (`чё`, Kukhnya s01e20 scene-03), 3 French entries lack `stress` and
  carry `ipa` instead (`absent`, `révoltant`, `diamant`, dix s04e04 scenes 22-24): move `ipa` to `stress`.
- table titles: use the names in `spec/annotations.md` (`Declension`, `Present`, `Future`, `Forms`; `Past`,
  `Imperative`, `Passé composé`, `Imparfait`, `Futur`). About 1100 primary tables use other names (`Conjugation`,
  `Singular & plural`, `Declension (m / n / f / pl)`, ...) and `Future` is used as a secondary title 547 times; the
  validator does not enforce this yet, but the app will group by title, so please normalise when you touch them.

### 4. Placeholder text that reaches the narrator (8 scripts)
`kukhnya/s01e19/scene-05..08` and `kukhnya/s02e03/scene-20..23`: the narrator intro contains `The characters discuss
their situation. -,   ,   - ...` (leaked from the summary). The audio would read this aloud. Rewrite the intro (and the
summary, item 1).

## P1: correctness of the data

### 5. Closing line (1444 of 1617 scripts; Dix 573, Kukhnya 492, Domashniy Arest 379)
`CLOSING` in the authoring modules was set to a repeat of the last story line (`Да, в Воронеже все любят рыбу!`,
`Но людям также нужна высокая культура!`). The recipe says a new farewell. Expected last segments:
`{"v": "anya", "t": "Пока!", "gap": 0.3}` / `{"v": "lea", "t": "À bientôt!", "gap": 0.3}`, spoken by a role in the
scene. Fix `CLOSING` in `authoring/scene-NN.py` and recompose; the notes file then needs one more entry (the new segment
index is the same, only the text changes: `trans`, `words`). Also: 1035 outros do not say "see you next time" as the
recipe asks, and some outros are not a send-off at all (`Let's review the key casting and observation vocabulary from
this scene.`, dix s04e02 scene-05). Not enforced yet; please fix when you are in there.

### 6. Source ties outside the scene (142 scripts, 695 lines; Kukhnya 72, Dix 52, Domashniy Arest 18)
`source.lines` cite cues that lie outside the scene's own time range. Example: kukhnya s01e18 scene-10 ("Плохая рыба",
locker room) ties its story lines 0, 1, 2 ... to cue 1, the episode's opening narration, with the fragment `девушки`,
which none of those lines is built from. Re-tie each such line to the cue it really comes from, or
drop it from `source.lines` if it is new text. If the story as a whole is not from the scene's cues, that is a P2
faithfulness problem (see Content).

### 7. Voices and role keys (show-wide)
Counts of characters (labels) read by more than one voice / appearing under more than one role key:
Kukhnya 27 / 27, Domashniy Arest 39 / 30, Dix pour cent 53 / 51. Cause: the `anya` / `lea` slot was used for "whoever is
the viewpoint of this scene", so the same person is `anya`/alisa in one scene and `chef`/anja in another (Kukhnya
s01e01 alone has Вика as alisa, angelina and anja). Known case: **Tatyana (domashniy-arest) is `anya`/`alisa` in 3 scenes
(s01e10 scene-12 is one) and `tanya`/`anja` in another**; Dix `Gabriel` is `theo` 181 times and `marcel` 26.
Fix (Voices):
1. Choose one lead per show for the `anya`/`lea` slot. Counts suggest Макс (Kukhnya, 199 scenes), Аркадий (Domashniy
   Arest, 162), Andréa (Dix, 245). The lead is not required to be in every scene any more.
2. Every other character gets its own role key (`vika`, `chef`, `tatyana`, ...) and **one voice**: the voice it has
   most often today. Write the table at the top of `characters.md`: `| role key | label | voice |`.
3. Rewrite the scenes that disagree: change `voices`/`labels` and every `v` in `segments` (and the role of the replayed
   lines). The text itself stays.
4. Two characters sharing a voice in one scene is not allowed (one voice per role). If the assignment puts two such
   characters together, give the less important one's lines to the narrator, or pick the voices so that characters who
   meet often differ. (Russian pool: `alisa` for the lead only, `anja`, `angelina`. French: `lucie` lead, `emilie`,
   `theo`, `marcel`.) At most 3 speaking roles per scene stays.
`validate.py` reports both counts per show at the top of the error list, with examples.

### 8. `characters.md` coverage (Kukhnya 36 role keys missing, Domashniy Arest 49, Dix 97; 963 uses)
Biggest: Dix `gabriel` (207 uses), `mathias` (168), `herve` (43), `colette`, `camille`, `andrea`, `arlette`, `noemie`;
Kukhnya `leva` (34), `guest` (32), `nagiev`, `dmitry`; Domashniy Arest `sokolov`, `viktor`, `arkady`. Add each as a
section (or one line in an "Extras" list for one-scene characters): name, label, how to draw them, and the line
`Story role key / voice: \`key\` -> voice`. 24 Kukhnya, 66 Dix and 44 Domashniy Arest labels are not mentioned in
`characters.md` at all; add them while you are there (not enforced).

### 9. Annotation tokens and stress (Dix 5706 lines in 336 scenes, Kukhnya 10 lines; stress: Dix 397 words, ru 20)
Dix annotations split elisions and hyphenated words (`J'ai` -> `J'` + `ai`; `Qu'est-ce qu'elle` -> `Qu'est-ce qu'` +
`elle`; `Remettez-m'en` -> 4 entries) and merge multiword units (`ce que`, `un peu`, `tout de suite`); some drop the
final punctuation (`boire?` -> `boire`). Required: one entry per whitespace token, exactly as written
(`J'ai`, `Qu'est-ce`, `qu'elle`, `ce`, `que`). dix s04e04 scenes 22-24 also have 397 words with no IPA at all. In ru,
20 words of two or more vowels have `stress: null` (Domashniy Arest 18, Kukhnya 2), e.g. `центра.`.

### 10. Lexicon conflicts (ru: 84 lemmas, fr: 53 lemmas) and bad entries
The same lemma is described differently in different scenes. Examples: `пойти` is `pf` 166 times and `impf` 10
times, `мочь` has pair `смочь` 234 times and `null` once; `брать` has stress `брать` once (no mark); `болеть` `боле́ть`
vs `бо́леть` (two different verbs: split into two homograph entries only if you give them different glosses, otherwise
choose); fr `oui` is `adv` 277 / `interj` 8, `ce` is `det` 536 / `pron` 3, `en` `prep` 268 / `pron` 4, `pas` `part`
484 / `adv` 3; `rappeler`, `laisser`, `au revoir` have 2 different IPA strings; 20 fr entries use dotted IPA
(`a.ni.vɛʁ.sɛʁ`; no dots). 22 annotation files have lexicon keys that differ only by case or ё. Decide one value per
lemma (the dominant one if it is correct; check `пойти`, `найти`, `сойти`: they are `pf`) and apply it everywhere
(a script over `out/` is the right tool). The validator prints each field's conflicts with examples.

### 11. Art: 61 pictures used by more than one scene (130 scenes), 5 very thin pictures
Byte-identical files are shared between scenes (e.g. dix s02e01 scene-13 = dix s04e06 scene-13;
domashniy-arest s01e10 scene-04 = s01e11 scene-04). Each scene needs its own picture of its own moment. Also look at
the 5 smallest files (18-20 KB: dix s04e04 scene-24, domashniy-arest s01e08 scene-48, s01e10 scene-04, s01e11 scene-04
and scene-40): they are very plain compared with the rest. The three I opened (a flat vector style, no text) look fine
as pictures but several show a generic figure that is not obviously the scene's characters; check against
`characters.md`.

## Content quality (from reading 6 scenes: kukhnya s01e05/08, s01e18/10, s02e03/22; domashniy-arest s01e03/20,
s01e10/12, s01e11/06; dix s01e01/14, s02e03/10, s04e02/05)

Not mechanically checkable, but these are what a learner or a native speaker would notice. Please re-read your scenes
for these:
- **Faithfulness.** domashniy-arest s01e10 scene-12 ("Новый редактор") is invented: the real scene (cues 311-330) is a
  prank about reading a colleague's texts, then "coffee detention"; the story has Tatyana and an editor discussing
  ratings and theatre, none of which is in the episode. kukhnya s01e18 scene-10 ties to cue 1 only and has no basis in
  the scene's cues. kukhnya s01e05 scene-08 is close but turns "your mom" into a joke the source does not make. The
  recipe: "Don't invent plot."
- **Real people and politics.** domashniy-arest s01e11 scene-06 (and 6 other scripts) name the real president;
  `Президент Владимир Путин скоро приедет к нам` as an A1 story line is not something we can ship. Use "the
  president" ("президент") or reframe.
- **Level.** A1 means short present-tense sentences. Too hard: `Представь: тебе сорок лет, жена красавица, дети, бизнес.`
  (domashniy-arest s01e03 scene-20), `Ou de brouiller les pistes avant de commencer.`, `Ce milieu déteste les gens qui
  font trop de choses.`, `Gabriel est amoureux, il te croit capable de tout.` (dix s02e03 scene-10). 60 Dix and 32
  Domashniy Arest scripts have story lines over 12 words; 207 intros are over 70 words (the recipe says 2-3
  sentences; one intro in s01e03 scene-20 is a single 60-word sentence).
- **Verbatim runs.** dix s02e03 scene-10 uses cues 245-258 almost line for line: a 14-line stretch of the episode.
  The README says short real lines only; adapt and shorten. Lines 255-258 there are commentary ("Mathias est un agent
  pragmatique qui manque d'imagination") that no character says to another; make it dialogue or narrate it.
- **Register and taste.** 18 scripts keep coarse words in story lines (`Ни хрена себе`, `сожрал` in kukhnya s01e18
  scene-10). The recipe says clean A1; replace.
- **Walk-through.** 602 scripts explain with case/aspect jargon (`nominative predicate noun phrase`, `imperative verb`,
  `accusative`): fine in small doses, but for an A1 listener say what it means in plain words ("Russians say 'to me is
  bad' where we say 'I feel bad'"). Some glosses read like machine translation (`'Max is surprised that anyone would
  reach him at work.'` is fine, `'No, I am very bad.'` is not: `мне очень плохо` is "I feel really bad").
- **Mixed tense/perspective in narration**: some outros narrate things not in the scene ("In the next scene, panic
  spreads through campaign headquarters", s01e11 scene-06). Say only what the scene shows.

## Russian-only Kukhnya episodes (S2 e04 - S6 e20): new plan

Complete Whisper transcripts exist for all of them, `sources/kukhnya/sNN/eNN.ru.srt` (97 files; S2 e04-e20, S3-S6 e01-e20).
**There will be no English dual subtitles. Do not wait for them.** Do these episodes after everything above is `OK`
and the higher priorities in the README are done, in order (S2 e04 first). Work from the Russian file: translate it
yourself for your own understanding; `scenes.json`, `source.file` and the cue checks all work with `.ru.srt`
(`validate.py` and `compose.py` accept it). In `out/kukhnya/NOTES.md` write that the transcripts are machine
recognised, and per episode list the cues you suspect are misheard (names especially, `Шеф`/`Лёва` forms, numbers)
and how you read them; where a line is unclear use a line you are sure of, or leave it out. Do not invent what the
text does not support. README, `sources/INDEX.md` (regenerated) and `out/PROGRESS.md` have been updated to say this.

## What I changed in this review (so you know what is not yours)

- `FEEDBACK.md`, a pointer at the top of `README.md`, new README rules, README priority 5, `out/PROGRESS.md` header,
  `sources/INDEX.md` (regenerated by `tools/index_sources.py`, now listing the `ru-only` episodes; subtitle files
  untouched), `spec/*.md` (a "Schema and canonical form" section in each).
- `spec/schema/*.schema.json` (new).
- `tools/validate.py` (schema checks with a small stdlib JSON-Schema subset checker, plus the rules above), `tools/compose.py`
  (writes `schemaVersion`, derives `show/season/episode/scene`), `tools/index_sources.py`, `tools/gaps.py` (docstring),
  `tests/test_validate.py` (+23 tests, 35 total). `examples/` is untouched; its `show` field is a display name
  (legacy) and has no `schemaVersion`, so `validate.py --script` reports schema differences for examples as warnings only.
- One mechanical fix in your output: `out/domashniy-arest/s01e06/scene-04.json` segment 26, a trailing space removed
  (the authoring module still has it; remove it there too so a recompose does not bring it back).

## How to verify

    python3 -I -m unittest discover -s tests                  # must print OK
    python3 -I tools/validate.py out --require-notes > /tmp/v.txt; tail -1 /tmp/v.txt     # must print "OK: 0 errors, N warnings"
    python3 -I tools/validate.py out/kukhnya/s01e01 --require-notes                       # a single episode

Order of work to keep the error list shrinking quickly: items 2 and 3 (one script over `out/`), 1, 4, then 9, 10 (script,
then check by hand), 5, 6, 7, 8, 11, then the content points. Commit per group (`git add -A && git commit`), push
after each; never force-push.

## Status 2026-10-28 (content side): migration done, what is left

Done by script (all checked in, each with its output in a separate commit): `tools/migrate_v1.py` (P0 format: schemaVersion,
`gram`, aspect/animacy/gender/number spellings, IPA moved out of `pos`, notes ids, scenes.json fields and English-only titles),
`tools/fix_tokens.py` (item 9: 5,716 Dix lines now one word entry per whitespace token), `tools/fill_stress.py` (461 French IPA
values from the corpus or espeak-ng, 20 Russian stress marks from the corpus or RuAccent), `tools/fix_invariable_forms.py`
(3 indeclinable nouns), plus 99 hand-written summaries, 8 rewritten narrator intros and 4 filled locations. Result with the app
validator (`--require-notes`): lenient 1617 of 1617 scenes pass, strict 68 of 1617 pass (the repo validator gives the same 68).

Still failing strictly, none of it mechanical:
- **Closing line (1,444 scripts).** Needs a new farewell segment and its annotation entry per script (item 5).
- **Source ties outside the scene (142 scripts)** (item 6) and **role keys missing from `characters.md`** (item 8). Writing
  the character entries needs a human decision about who each extra is.
- **Show-wide**: voices and role keys (item 7), lexicon conflicts (item 10), 61 duplicated pictures (item 11).

## Needs human (not done on purpose)

- **Plot accuracy.** The new summaries only say what each scene's own lines say; whether a scene is faithful to the episode
  (domashniy-arest s01e10 scene-12, kukhnya s01e18 scene-10, ...) was not judged. Kukhnya s01e19 scene-05 to -08 have
  story lines that are mostly filler ("What a pleasant evening N") and need rewriting from the real cues; their summaries are
  deliberately minimal. kukhnya s02e03 scene-20 to -23 have mismatched role labels.
- **Real president.** `Путин` is still in domashniy-arest s01e11 scene-05, -06, -07, -14, -15, -17. Reframe or reword; the
  summaries say "the president" and do not name him.
- **Generated annotation text.** Where a split or merged token had no correct entry elsewhere in the show, its gloss/gram
  was composed from the pieces (e.g. `l'ai` = "have him"); French IPA for 198 rare tokens comes from espeak-ng, not a
  dictionary. A French speaker should skim them.
- **Level, register, A1 difficulty and the walk-through wording** (Content quality above) are untouched.
