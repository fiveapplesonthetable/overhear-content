# Scene script: `scene-NN.json`

One file per scene. This is the "episode JSON" of the recipe plus provenance fields. Examples:
`examples/*/scene.json`. Validate with `python3 tools/validate.py <episode dir>`.

```json
{
  "id": "kukhnya-s01e02-scene-03",
  "pair": "ru-en",
  "show": "kukhnya", "season": 1, "episode": 2, "scene": 3,
  "title": "Где мой нож?  (Where's My Knife?)",
  "level": "A1 — Duolingo Section 2",
  "labels": {"barinov": "Шеф"},
  "segments": [
    {"v": "narrator", "t": "…", "gap": 0.8},
    {"v": "barinov", "t": "Где мой нож?", "gap": 0.55}
  ],
  "source": {"show": "Кухня (Kukhnya) S1.02", "file": "sources/kukhnya/s01/e02.ru.dual.srt",
             "lines": [{"line": 0, "cue": 76, "fragment": "где мой нож"}]}
}
```

| field | rule |
|---|---|
| `id` | `<show>-sNNeNN-scene-NN`, matching the folder and file (`kukhnya`, `domashniy-arest`, `dix-pour-cent`). |
| `pair` | `ru-en` for Russian shows, `fr-en` for French. |
| `show`,`season`,`episode`,`scene` | Integers (show is the slug). Recommended. |
| `title` | `<target-language title>  (<English title>)`, two spaces before the bracket. Short, concrete. No scene number. |
| `level` | `"A1 — Duolingo Section 2"` (ru) or `"A1 — débutant"` (fr). |
| `labels` | role key -> display name for every speaking role. Must equal `ru` of that key in `out/<show>/cast.json`. There is **no `voices` field**: the renderer casts voices from `cast.json` by gender. |
| `segments[]` | Ordered. `v` is `narrator` or a key of `out/<show>/cast.json` (the character's own name: `max`, `barinov`; never a viewpoint slot such as `anya`/`lea`); `t` the text (1-2 sentences); `gap` seconds of silence after, 0..3. |
| `source.file` | Repo-relative path of the subtitle sidecar the scene is built from. |
| `source.lines[]` | `line` = 0-based index into the *story* (part 2) lines, `cue` = cue number in the sidecar, `fragment` = text that must occur in that cue (case/punctuation-insensitive). Lines with no subtitle behind them are not listed. |

Order of `segments`: intro (narrator) / story lines / opener (narrator) / [replayed line, narrator gloss] x N /
story lines again / outro (narrator) / closing line. The validator warns if part 4 is not an exact repeat of part 2.

## Writing it
Don't hand-write gaps. Write an authoring module (see `examples/*/authoring.py`: INTRO, STORY, OPENER, WALK,
TRANSITION, OUTRO, CLOSING, plus ID, TITLE, LEVEL, PAIR, LABELS, SOURCE_NAME, SOURCE_FILE and optional
SHOW, SEASON, EPISODE, SCENE) and run

    python3 tools/compose.py out/kukhnya/s01e02/authoring/scene-03.py --out out/kukhnya/s01e02/scene-03.json

It builds the segments with the right gaps, checks language rules, verifies every claimed subtitle fragment against the
sidecar, and writes `scene-03.REVIEW.md` (each line, its meaning and the cue it came from).
`STORY` rows are `(role, text, english, [(cue_no, "fragment"), ...], note)`; `WALK` rows are
`(story_line_index, sentence_or_None, narrator_gloss)`.

## Schema and canonical form (v1)
Machine-readable: `spec/schema/script.schema.json`, enforced by `tools/validate.py`. On top of the table above:
- `schemaVersion` (integer, `1`) is the first field. `show` is the slug (`kukhnya`, ...), **not** a display name (the
  `show` field of the old `examples/` files is legacy); `show`, `season`, `episode`, `scene` are required and
  must match `id`. No other top-level fields.
- `level` is exactly `"A1 — Duolingo Section 2"` (ru) or `"A1 — débutant"` (fr), never `"A1"` or `"beginner"`.
- `title` is `<target title>  (<English title>)`: exactly two spaces before the bracket, no other double space, no
  leading or trailing space.
- `source.file` is the sidecar actually used: `sources/<show>/sNN/eNN.<lang>.dual.srt`, or `eNN.ru.srt` for the
  Russian-only Kukhnya episodes. Every `source.lines[].cue` must lie inside that scene's `start`-`end` in `scenes.json`.
- The **last segment is a short farewell** by a speaking role (`Пока!`, `До свидания!`, `Хорошего дня!`, `À bientôt!`,
  `Au revoir!`), new text, not a repeat of a story line.
- `labels` has an entry for every speaking role, equal to its `cast.json` `ru`; one character = one role key = one label
  for the whole show. No `voices`. See `spec/schema/cast.schema.json` and FEEDBACK.md "P-1".
- Narration names only people of `cast.json` (or its `other_names`), and the person who actually speaks the line it
  explains. Explanations follow the P-1 rules in FEEDBACK.md (no templates, no grammar-label endings).
- Narration never contains placeholder text (`The characters discuss their situation`, `ENG `).

## Original native source audio

A native segment may specify:

```json
"sourceAudio": {
  "file": "sources/al-maktab/s01/e01.mp4",
  "sha256": "<entire original media SHA256, 64 lowercase hex characters>",
  "start": 12.5,
  "end": 14.2
}
```

This portable relative identifier resolves only under the renderer's external
private `OVERHEAR_SOURCE_AUDIO_ROOT` (default `/mnt/agent/pilot-source-audio`).
Production provisions the original media there; **never commit full video/audio
or an absolute private file path into the content repository**. Path traversal
and symlink escapes are rejected. The renderer verifies the media hash and
actual bounds before extracting speech. Replays reuse the identical hash and
window. The segment text must be a reviewed transcript of that exact speech;
source reuse cannot justify invented or changed dialogue. English narrator
segments continue to use their configured narrator voice. Public transcript
content omits `sourceAudio` entirely.
