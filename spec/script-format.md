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
  "voices": {"narrator": "sky", "anya": "alisa", "chef": "anja"},
  "labels": {"chef": "Шеф"},
  "segments": [
    {"v": "narrator", "t": "…", "gap": 0.8},
    {"v": "chef", "t": "Где мой нож?", "gap": 0.55}
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
| `voices` | role -> voice key, see `recipe.md`. Must include `narrator: sky` and the protagonist role. |
| `labels` | role -> display name (target language) for roles other than `narrator`/protagonist. |
| `segments[]` | Ordered. `v` role key from `voices`; `t` the text (1-2 sentences); `gap` seconds of silence after, 0..3. |
| `source.file` | Repo-relative path of the subtitle sidecar the scene is built from. |
| `source.lines[]` | `line` = 0-based index into the *story* (part 2) lines, `cue` = cue number in the sidecar, `fragment` = text that must occur in that cue (case/punctuation-insensitive). Lines with no subtitle behind them are not listed. |

Order of `segments`: intro (narrator) / story lines / opener (narrator) / [replayed line, narrator gloss] x N /
story lines again / outro (narrator) / closing line. The validator warns if part 4 is not an exact repeat of part 2.

## Writing it
Don't hand-write gaps. Write an authoring module (see `examples/*/authoring.py`: INTRO, STORY, OPENER, WALK,
TRANSITION, OUTRO, CLOSING, plus ID, TITLE, LEVEL, PAIR, VOICES, LABELS, SOURCE_NAME, SOURCE_FILE and optional
SHOW, SEASON, EPISODE, SCENE) and run

    python3 tools/compose.py out/kukhnya/s01e02/authoring/scene-03.py --out out/kukhnya/s01e02/scene-03.json

It builds the segments with the right gaps, checks language rules, verifies every claimed subtitle fragment against the
sidecar, and writes `scene-03.REVIEW.md` (each line, its meaning and the cue it came from).
`STORY` rows are `(role, text, english, [(cue_no, "fragment"), ...], note)`; `WALK` rows are
`(story_line_index, sentence_or_None, narrator_gloss)`.
