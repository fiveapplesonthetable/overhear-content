# overhear-content: brief for the production agent

You are making Overhear lessons: short A1 listening scenes adapted from real TV episodes, told by an English narrator
who replays the target-language lines and explains them. You make **everything**: scene breakdowns, scripts, translations,
word notes, art, and the rendered audio with word timing. You review your own work. A separate machine then fetches
your output, verifies it and copies it to Firebase **unchanged**. Nobody fixes anything after you.

## Priority now: original series (read [spec/ORIGINALS.md](spec/ORIGINALS.md) first)

The public app now plays only **original** stories that you create from scratch in `originals/`, released as
`original-<episode>`. Everything in `out/` is adapted from real TV shows and now ships only to a private tier for the owner's
testing. The original series come before all other work below.

## The one rule that matters most: file formats and groupings

The app reads exactly the files the pipeline writes, in exactly the layout it writes them. Read
**[spec/OUTPUT-CONTRACT.md](spec/OUTPUT-CONTRACT.md) first**. It defines every file, field, id, hash and grouping. Two
checkers enforce it. Work they reject does not ship:

```
python3 -I tools/validate.py --require-notes out/<show>/sNNeNN              # content (git)
python3 -I tools/check_render.py $OVERHEAR_HOME/render-store --episode <show>-sNNeNN   # rendered audio, timing, clips, forms
```

Never invent a field, rename a file, re-serialize a rendered JSON or hand-edit audio. Text, translation and timing stay in
sync because the audio and timing are rendered from the committed script and notes and stamped with their hash. To fix
anything, fix the content, commit, and re-render.

## What to produce

| language | show (slug) | target | sources in `sources/` |
|---|---|---|---|
| ru | Кухня (`kukhnya`) | **every season, S1-S6** (20 episodes each) | S1, S2 e01-e03: ru+en dual subtitles. S2 e04-S6: Russian-only Whisper transcripts (`eNN.ru.srt`); translate yourself |
| ru | Домашний арест (`domashniy-arest`) | **S1** (12 episodes, the whole show) | ru+en dual |
| fr | Dix pour cent (`dix-pour-cent`) | **every season, S1-S4** (6 episodes each) | fr+en dual |
| es | Paquita Salas (`paquita-salas`) | full **season 1** (E1 first) | `eNN.es.srt` + `eNN.en.srt`, E1-E5 (Netflix subtitles; the Spanish is a transcript of the Spanish audio) |
| de | Die Discounter (`die-discounter`) | one full episode, S1E1 | `e01.de.srt` (Whisper) + `e01.de-orig.auto.vtt` (platform auto-captions) |
| pt | Porta dos Fundos (`porta-dos-fundos`) | one full sketch, "Vem pra reunião" | `e01.pt.srt` (Whisper) + auto-captions |
| ko | The Producers (`the-producers`) | S1E1-E11 (of 12) | `e01..e11.ko.srt` (Whisper large-v3, the whole episode: KBS's three uploaded parts joined) |
| it | Boris (`boris`) | one full episode, S1E1 | `e01.it.srt` (Whisper large-v3) + `e01.en.srt` (English subtitles) |
| zh | 幕后之王 Behind the Scenes (`behind-the-scenes`) | full season 1 in progress: E1-E19 of 46 | `e01..e19.zh.srt` (Whisper large-v3) |
| ja | 全裸監督 The Naked Director (`the-naked-director`) | full **seasons 1 and 2** (S1E1 first) | `s01/eNN.ja.srt` + `s01/eNN.en.srt` and `s02/...`, E1-E8 each (Netflix subtitles). Closed-caption marks (speaker names in （）, readings in ( ), sound cues) are not dialogue. The show is about the adult-video industry, so keep story lines clean (spec/quality.md §3) |
| ar | مدرسة الروابي للبنات AlRawabi School for Girls (`alrawabi-school`) | S1E1-E4 (of 6) | `e01..e04.ar.srt` (Whisper large-v3, Jordanian Arabic) |

A "full episode" means the whole episode, every scene from the first cue to the last, as for RU and FR. A pilot language
starts with `out/<slug>/show.json` (`spec/schema/show.schema.json`); no code change is needed for a new show or language.

**Sources are text only, and everything you need is in `sources/`.** There is no media to fetch: every episode has a
subtitle or Whisper transcript, and that is what you build from. Never put show audio in a render, a voice reference or a
release (contract §2, "Forbidden anywhere in a render").

## Order of work

1. **Bring the existing RU and FR content up to the gates, Kukhnya S1 first.** Every RU and FR episode already has a seed
   in `out/` (156 episodes: scene breakdowns, scripts, notes, art, casting). It has the right structure but fails the
   quality gates (see `out/PROGRESS.md`): mostly repeated narrator phrasing and too little word teaching. Rewrite the
   explanations by hand per `spec/quality.md`, and re-check story, speakers and notes against the sources, until the
   whole-`out/` validator run passes with `--strict-teaching`. Kukhnya S2 e04 onwards was written from Whisper transcripts,
   so re-read those scenes against their cues: where a name or number looks misheard, use a line you are sure of or leave it out.
2. **Render and package season by season**, in `render/settings.json` `priority` order: Kukhnya S1, Dix pour cent S1,
   Domashniy Arest S1, Kukhnya S2, Dix S2-S4, then Kukhnya S3-S6. Package each episode as soon as it passes. Fix the next
   season's text while the GPU renders the current one.
3. **Pilots, in this order:** es, de, pt, ko; then it and zh; then ja and ar. Make
   their voices first (`spec/voices.md`).

Work in parallel where the machine allows (writing the next episode while the GPU renders the last one), but never ship an
episode before it passes.

## Machine setup (A100 40 GB)

```
git clone https://github.com/fiveapplesonthetable/overhear-content && cd overhear-content
OVERHEAR_HOME=~/overhear HF_TOKEN=hf_... bash render/setup/setup.sh     # venvs, every model, self-check
export OVERHEAR_HOME=~/overhear GPURUN_BUDGET_MIB=38500
python3 -I render/pipeline.py --status
```

The HF token comes from the owner. Never commit it or print it. `render/settings.json` is already sized for 40 GB (batch 16,
several scenes on the GPU at once through `render/gpurun`). Use the RAM and cores too: run Whisper and alignment beside
TTS, and pre-render the next episode while you review the last. If a step runs out of memory, lower `tts.batch`, not the
reservations. You may try bigger or better models if the conditions in contract §4 hold. Measure them, and record what you
measured in `out/PROGRESS.md`.

**Settings per language.** `render/settings.json` renders ru and fr. A pilot language renders with its own profile:
`OVERHEAR_RENDER_SETTINGS=render/settings.<lang>-qwen-en.json` (Arabic: `settings.ar-chatterbox-en.json`). Set that
profile's `priority` to your show slug.

## The loop, per episode (`<show>`, `sNNeNN`)

1. **Read the sources** (`sources/<show>/sNN/eNN.*`) end to end, plus the previous episode's `scenes.json`, and
   `out/<show>/characters.md` and `cast.json`.
2. **Split into scenes.** `python3 tools/gaps.py <srt>` lists silences. Split on time gaps, a change of who is present, or a
   change of place. Cover the whole file, first cue to last. A short transitional scene stays in the list with
   `"merge": "prev"` or `"next"`. Write `out/<show>/sNNeNN/scenes.json` (`spec/scenes-format.md`). Typically 8-30 scenes.
3. **Cast.** Add every new speaker to `out/<show>/cast.json` (one key per character for the whole show) and describe them in
   `characters.md` (start from `out/TEMPLATE-characters.md`).
4. **Write each non-merged scene** as `authoring/scene-NN.py`. Copy the closest `examples/*/authoring.py` or a gold scene,
   follow `spec/recipe.md` and `spec/quality.md`, and borrow short real lines tied to their cues. Then
   `python3 -I tools/compose.py out/<show>/sNNeNN/authoring/scene-NN.py --out out/<show>/sNNeNN/scene-NN.json` and fix every
   PROBLEM it prints.
5. **Annotate**: `scene-NN.notes.json` (`spec/annotations.md`): the translation of every target segment, per-word lemma, POS,
   stress or IPA, gloss and grammar, and a lexicon entry per lemma with examples and forms tables. Check gender, aspect,
   conjugation and IPA. Wrong notes teach wrong things.
6. **Art**: `scene-NN.webp`, 1024x1024, per `art/style/STYLE.md`, with the characters as `characters.md` describes them. Look
   at every image before keeping it.
7. **Validate.** Run `python3 -I tools/validate.py --require-notes out/<show>/sNNeNN`, then the whole corpus with
   `python3 -I tools/validate.py --require-notes --strict-teaching out` (template and phrase limits are show-wide). Both must
   print `OK`. Read the warnings.
8. **Review the text** (below). Fix, re-compose, re-validate.
9. **Commit and push the content**, one episode per commit (`<show> sNNeNN: N scenes`), with `out/PROGRESS.md` updated in the
   same commit. Never force-push or rewrite history.
10. **Render**: `python3 -I render/pipeline.py --episode <show>-sNNeNN`. It renders the scenes, then the example clips and the
    form clips. `--status` shows progress.
11. **Review the audio** (below). A fix means changing the content, committing, and rendering again.
12. **Check and ship**: `python3 -I tools/check_render.py $OVERHEAR_HOME/render-store --episode <show>-sNNeNN`, then
    `python3 -I tools/package_render.py $OVERHEAR_HOME/render-store --episode <show>-sNNeNN --release`. Package only a pushed
    commit, and only the whole episode.

## Review: Opus writes, Gemini reviews

Every scene gets a second read by a different model before it is committed, and every rendered episode gets a listening pass.

* **Text review (Gemini, given the scene JSON, notes and the source cues for its time range):** Is it faithful to the episode?
  Is each speaker right? Is the formal or informal address right (FR tu/vous, RU ты/вы, and so on)? Is the target language
  natural? Is it A1? Does each explanation teach one concrete thing, per `spec/quality.md` §2? Are the translations and
  notes correct (stress, IPA, gender, aspect)? Ask for specific line-level findings, fix them, and repeat until it has none
  that are real.
* **Audio review:** read every `report.json` (`stress.unresolved`, `warnings`, `timing.notOk`). Listen to at least the first
  scene of every episode and every scene a gate flagged. `render/listen_page.py` builds an ear-check page. Have Gemini
  listen to a sample too: wrong stress, a wrong voice for a character, a mispronounced name, clipped words.
* **Speaker check against the original:** for lines where the subtitles are ambiguous about who speaks (common in Whisper
  sources), use the cue timing and context; if it is still unclear, leave the line out. Never ship a guess.

Record what each review found and what you changed in `out/PROGRESS.md`. Do not commit review sheets next to the scenes.

## Done means

Per episode: every non-merged scene has a script, notes and art, and `validate.py --strict-teaching` passes for the whole
of `out/`. Text review is clean. `check_render.py --episode` prints `OK: 0 errors`. Every report has been read and the
listening pass is done. The package is released from a pushed commit, and `out/PROGRESS.md` says so. RU and FR are done when
every listed season is; each pilot language is done when every episode it has in `sources/` is; do its E1 first, then the rest in order.

## Rules recap

* The narrator speaks English only, and never says a target-language word in English pronunciation. A word or line the
  narrator names is its own short target segment, voiced by the character who said it, so it is heard with a native accent:
  narrator "Kostya's little word" / kostya "Зато." / narrator "means 'but on the plus side'." The real line is replayed the same way. ja/zh/ko/ar story lines are in native script.
* Target lines are natural, A1, short, and in the right register. Russian is Cyrillic only. French punctuation is attached
  (`là?`) with straight apostrophes.
* Stress marks go only in notes `stress`. No emoji. No text in images.
* Tie each borrowed line to its cue (`source.lines`). Never invent plot or change who says what. Never quote long runs.
* Every JSON you write carries `"schemaVersion": 1` and matches `spec/schema/` exactly.
* Scene ids are permanent: `<show>-sNNeNN-scene-NN` never changes meaning once published. Edit in place; never renumber.
* The last segment is a short new farewell, never a repeated story line.
* No secrets, tokens or media in git. No original show audio in any public output.
* The tools and specs are yours to fix if they are wrong, but a change to a checker needs a test (`tests/`) and must keep
  the contract. Run `python3 -m pytest -q tests` and `render/tests/run_all.sh`.

## What is where

| path | what |
|---|---|
| `spec/OUTPUT-CONTRACT.md` | **the file formats and groupings the app consumes** |
| `spec/quality.md` | what a good scene is: cast, explanations, story, notes, art, audio |
| `spec/recipe.md` | the 5-part scene recipe (intro, story, walk-through, replay, outro) |
| `spec/script-format.md`, `spec/scenes-format.md`, `spec/annotations.md`, `spec/schema/` | content formats |
| `spec/voices.md` | the voice pool, and how to make voices for a new language |
| `examples/` | three reviewed scenes with authoring module, script, sample audio and review |
| `out/` | the content: one folder per show (`show.json`, `cast.json`, `characters.md`, episodes); `out/PROGRESS.md` |
| `sources/` | subtitles per show and episode; `sources/INDEX.md` lists coverage |
| `art/style/` | the art style guide and reference images |
| `render/` | the render pipeline (TTS, alignment, gates, assembly, clips, forms); `render/README.md` |
| `tools/validate.py`, `tools/check_render.py` | the two checkers |
| `tools/compose.py`, `tools/gaps.py` | authoring module to script; scene-break finder |
| `tools/package_render.py`, `tools/fetch_renders.py` | episode packages: make on the A100, install on the receiving machine |
| `learn/`, `dictionary/`, `word-origins/` | learning notes, written dictionary entries, word histories (below) |

## Learning notes, dictionary and word histories

`learn/<pair>/<id>.json` holds focused learning notes with checked examples from source scenes. `dictionary/<pair>.json`
gives written dictionary entries. `word-origins/<pair>.json` holds etymology with a source link per entry (see
`word-origins/README.md`). None of these affect rendering. After changing only these folders, run
`python3 -I tools/validate.py . --metadata-only`. Add a history only after checking it against a specific authoritative
entry, and link that entry. Never publish an unsourced history. The publishing machine reports missing histories per
season (`tools/origin_coverage.py` runs on its serving build); fill the gaps it reports when the owner passes them on.
