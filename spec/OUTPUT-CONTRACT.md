# Output contract: exactly what the app consumes

**This is the most important document in the repo.** Everything you produce is copied byte for byte to Firebase by a
publisher you do not run. It does not fix, convert or regenerate anything: a file in the wrong place, a missing field, or an
audio file whose text drifted from its script is dropped silently or rejected. Two checkers reproduce every rule below. Run
them; never hand in work they reject.

```
python3 tools/validate.py --require-notes out/<show>/sNNeNN          # content: scripts, notes, scenes.json, cast, show.json
python3 tools/check_render.py $OVERHEAR_HOME/render-store --episode <show>-sNNeNN   # rendered audio + timing + clips + forms
```

Both must print `OK: 0 errors`. Warnings are allowed but must be read. If a rule here and a checker ever disagree, the checker
wins; fix the doc.

There are two halves:

1. **Content**, in git in this repo (`out/`): the text, translation, notes, art and casting.
2. **Renders**: the audio made from that content by `render/`, under `$OVERHEAR_HOME/render-store/`. They are shipped as
   one package per episode (a GitHub release), never committed.

A render is bound to the exact bytes of its content by `contentHash`. Changing a script or notes after rendering makes the
render stale. The publisher drops a stale render, and the scene ships without audio.

---

## 1. Content tree (git)

```
out/<show>/
  show.json                       REQUIRED. Show metadata; the show's language pair. Schema: spec/schema/show.schema.json
  cast.json                       characters -> gender, description (casting is built from it)   spec/schema/cast.schema.json
  characters.md                   who is who, for writers (TEMPLATE-characters.md)
  cover.<ext>                     optional; if show.json "cover" names a file, it must exist
  sNNeNN/
    scenes.json                   the episode's scene list, merges, source windows   spec/schema/scenes.schema.json
    scene-NN.json                 the script: segments, lines, translations           spec/schema/script.schema.json
    scene-NN.notes.json           word-level notes, lexicon, examples, forms          spec/schema/notes.schema.json
    scene-NN.webp                 the scene's art, 1024x1024 webp, unique per scene (merged scenes have none)
    authoring/scene-NN.py         the authoring module; tools/compose.py turns it into scene-NN.json
sources/<show>/sNN/eNN.<lang>[.dual].srt   the subtitles a script was built from (text only; media is never in git)
```

* **Names.** Show slug `^[a-z][a-z0-9-]*[a-z0-9]$`, which must equal the folder name and `show.json.slug`. Episode folder
  `sNNeNN`. Scene id `<show>-sNNeNN-scene-NN`. Two digits everywhere, 1-based.
* **show.json** is the only place a show's language pair lives (`"pair": "ja-en"`). It needs `schemaVersion` 1, `slug`,
  `pair`, `title{lang: str}`, `summary`, `type` (`series`|`movie`), `categories`, `seasons[{n,title}]`, and `cover`
  (a file name or null). A new show is just a new folder with a show.json; no code changes are needed.
* **Merged scenes.** A `scenes.json` entry with `"merge": "prev"` or `"next"` is folded into that neighbour. It has no script of its own, is
  **not rendered** and is not published. If one has a render folder, the checker warns; delete that folder.
* The formats inside the scripts and notes (segments, `v` roles, sentences, `words[]`, stress marks, native annotations) are
  in `spec/script-format.md`, `spec/scenes-format.md` and `spec/annotations.md`. The validator enforces them.

**Text, translation and timing stay in sync by construction.** `render/` reads the script and notes you commit. The audio,
the per-word timing and the sentence spans are all made from those bytes and stamped with their hash. Never edit a rendered
file to "fix" text. Fix the content, commit it, and re-render: the pipeline re-renders exactly the scenes whose hash changed.

## 2. Render store layout

```
$OVERHEAR_HOME/render-store/
  <sceneId>/                        one folder per non-merged scene
    audio.mp3                       the scene, 24 kHz mono, 96 kbps CBR LAME (Xing tag), program loudness -16 LUFS
    spans.json                      where each segment and sentence sits in audio.mp3
    timing.json                     per-word times for every segment
    meta.json                       provenance + integrity + render key
    report.json                     QA counters (stress, retakes, timing, loudness)
  clips/<id>.json + <id>.mp3        one clip per lexicon example sentence (status failed: .json only, no mp3)
  forms/<id>.json + <id>.mp3        one clip per filled cell of a lexicon forms table
  forms/.plan.json                  the list of planned form clips; a form ships ONLY if its id is here with the same ckey
  cache/, logs/, state.json, *.lock pipeline working files, never shipped
```

### JSON serialization (applies to every JSON file the pipeline writes)

`json.dumps(obj, ensure_ascii=False, sort_keys=True, indent=1) + "\n"`, UTF-8. Every `*Sha256` field is the sha256 of the
**file bytes as written**, never of a re-serialization. Do not reformat, re-indent or pretty-print a rendered file: that
breaks the hashes.

### `meta.json`

| field | meaning |
|---|---|
| `sceneId` | equals the folder name |
| `contentHash` | `sha256(script bytes + notes bytes)` of `scene-NN.json` and `scene-NN.notes.json` as committed. **The publisher drops the scene if this differs from the content it publishes.** |
| `contentCommit` | the content repo commit rendered from (informational) |
| `renderKey` | `sha256(contentHash, tts signature, assembly signature, [voice, refVersion] per role)`: the incremental key |
| `tts` | object `{model, lora, stressPolicy, gen}`. `model` is the dialogue model id the app credits (e.g. `Qwen/Qwen3-TTS-12Hz-1.7B-Base`) |
| `voices` | `{role: {voice, refVersion}}` for every role in the scene, narrator included |
| `voicesVersion`, `align` (`mms_fa/a1`), `pipelineVersion` (`overhear-render/1`), `renderVersion` (`r2`), `renderedAt` | provenance |
| `durationSec` | equals `spans.json.durationSec` (within 0.05 s) and the decoded mp3 length |
| `audioBytes`, `audioSha256` | size and sha256 of `audio.mp3` |
| `spansSha256`, `timingSha256` | sha256 of `spans.json` / `timing.json` bytes |
| `sampleRate` 24000, `bitrateKbps` 96 | fixed |
| `nativeAlignment` | **ja, zh, ko, ar only**: starts with `mms-uroman-wordspans/1;` |
| `wall`, `narratorRu`, `peakRepair`, ... | extra keys written by pipeline passes are allowed and ignored |

**Forbidden anywhere in a render:** a segment `sourceAudio`, meta `privateSourceAudio` or `containsOriginalSourceAudio`, and
`audioProvenance.kind == "original-source"`. Public audio is synthesized only. Original show audio may condition voices
privately but never enters an mp3. The publisher rejects the scene outright.

### `spans.json`

```json
{"durationSec": 309.949, "sampleRate": 24000, "sceneId": "kukhnya-s01e01-scene-03",
 "segs": [{"seg": 0, "start": 0.0, "end": 12.464, "nextStart": 13.264, "v": "narrator", "voice": "sky", "lang": "en",
           "sentences": [{"i": 0, "start": 0.0, "end": 4.587, "engine": "f5-tts", "text": "It's late now, ..."}]}]}
```

* `segs` has **exactly one entry per script segment**, `seg` = 0..n-1 in script order. A count mismatch drops the scene.
* Times are seconds in `audio.mp3`, non-decreasing, `0 <= start <= end <= durationSec`. `nextStart` is the next segment's start
  (or the duration). `sentences[].text` is the sentence as the script splits it.

### `timing.json`

`{"<seg>": [{"t": "word", "s": 0.255, "e": 0.481, "ok": true, "why": ""}, ...], ...}`, with a key for every segment, narrator included.

* **One item per token, in order.** Dialogue segments use the publisher's `annotated_units` (`tools/word_spans.py`): the
  author's `words[]`/annotation spans, required for ja and zh; for other languages, whitespace tokens containing a letter or
  digit. Narrator segments use whitespace tokens. `t` is the token text.
* `ok: false` (`why`: `missing`, `zero-length`) marks interpolated times. Allowed, counted in `report.json.timing.notOk`; keep it low.
* RU/FR/ES/DE/IT/PT: times are monotonic. The last word may end a few ms past its segment end, but before the next segment's start.
* **ja, zh, ko, ar (native):** every dialogue item also has `span` (half-open code-point range into the line), `ok: true`,
  `alignment` equal to the meta `nativeAlignment` convention, and times monotonic **inside** the segment. Anything less (a
  missing item, `ok: false`, or proportional fallback) and the publisher rejects the scene.

### `report.json`

`{version: 1, sceneId, audio{gainDb, mp3Seconds, programLufsBefore, seconds}, stress{...}, retake{sentences, takes},
timing{notOk, tokens}, tts{sentences, unique}, warnings[]}`. Informational for the publisher. **You** read it in review:
stress `unresolved` and `warnings` are review items.

### Clips (lexicon example sentences)

For every `lexicon.<key>.examples[].text` in a scene's notes:

* `id = sha256(pair + "\0" + text)[:16]` (pair like `ru-en`; text exactly as written in the notes)
* `clips/<id>.json`: `{id, pair, lang, text, voice, ckey, cer, durationSec, audioBytes, audioSha256, renderedAt, tries, status}`.
  `status` is `ok` (with `<id>.mp3`) or `failed` (Whisper CER stayed above `clips.cerMax` 0.15 after the retakes; no mp3, and
  the app shows no speaker icon).
* `text` must equal the notes' text. A changed example is a new id; the old file is simply unused.

### Forms (cells of lexicon tables)

For every non-empty cell of `lexicon.<key>.forms` and `moreForms[]` tables:

* `id = sha256("\0".join([pair, lemma, table title, row label (cells[0]), column label, cell]))[:16]`
* `forms/<id>.json` + `.mp3` use the same record shape as clips.
* `forms/.plan.json` is a JSON list of `{id, pair, lang, text, voice, ckey, key, plain, tts}`. **A form ships only if its id is
  in the plan with the same `ckey` as its record.** `render/forms.py` writes the plan and merges by id: a run replaces its
  own ids and keeps the others. Never hand-edit it.

## 3. Episode packages (how renders leave the A100)

```
python3 tools/package_render.py $OVERHEAR_HOME/render-store --episode <show>-sNNeNN --release
```

This re-runs `check_render.py --episode` and refuses on any error. It then writes `dist/render-<show>-sNNeNN.tar` and
uploads it as GitHub release `render-<show>-sNNeNN` on this repo. The tar contains:

```
<sceneId>/{audio.mp3, spans.json, timing.json, meta.json, report.json}   every non-merged scene of the episode
cache/tts/<key>.{flac,gates.json}                                        the sentence takes those scenes were assembled from (meta.sentenceTakes)
clips/<id>.{json,mp3}                                                    that episode's example clips
forms/<id>.{json,mp3}                                                    that episode's form clips
forms-plan/<show>-sNNeNN.json                                            the episode's rows of forms/.plan.json
MANIFEST.json                                                            episode, contentCommit, per-scene contentHash, sha256 of every file
```

**Group by episode, and only whole episodes.** A package is made only when every scene of the episode renders and passes.
Commit and push the content first: `contentCommit` must be a pushed commit of `main`. The receiving machine checks out that
commit, runs `tools/fetch_renders.py`, which re-verifies every sha256 and contentHash and merges the plan rows, then runs
`check_render.py` again. Then it copies the files to Firebase. Re-packaging an episode after a fix replaces the release asset.

The sentence takes are for fixes: `fetch_renders.py` keeps them in `<render dir>/cache/tts` (`--cache DIR` moves them), the
publisher ignores them, and a package without them (rendered before `meta.sentenceTakes`) installs as before. A fix on another
machine (`tools/fix_scene.py`) re-renders only the changed scenes from them, synthesizes only the sentences whose cache key changed,
and re-packages the whole episode.

## 4. Models

The vendored pipeline (`render/`) is the reference: ESpeech-TTS-1 RL-V2 for Russian dialogue, F5-TTS v1 for the English
narrator, Qwen3-TTS-12Hz-1.7B-Base for French and the pilot languages, Chatterbox multilingual for Arabic, MMS_FA for
alignment, faster-whisper for CER. On the A100 you may **try other or bigger models** (a larger TTS, a better aligner, a
stronger ASR judge) if all of these hold:

* the outputs keep this contract exactly and `check_render.py` passes;
* the model id and settings go into `meta.tts` and into the render key, so a model change re-renders exactly what it touches;
* quality is measured, not assumed: Whisper CER on a fixed sample (`render/bench_cer.py`, `render/smoke.sh`) is at least as
  good as the reference, and a listening pass agrees;
* the model's license allows publishing its audio, and no voice is cloned from original show audio into public output.

Record what you tried and what you measured in `out/PROGRESS.md`.
