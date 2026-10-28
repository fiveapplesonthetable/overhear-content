# Scene breakdown: `out/<show>/sNNeNN/scenes.json`

One per episode, written first. Illustration: `spec/scenes.example.json`.

```json
{"show": "kukhnya", "season": 1, "episode": 2, "title": "episode title or null",
 "scenes": [
  {"scene": 1, "start": "00:00:12,340", "end": "00:02:30,000", "title": "…", "summary": "one line",
   "characters": ["Chef", "Nastya"], "location": "restaurant kitchen", "merge": null}
 ]}
```

| field | rule |
|---|---|
| `show` | folder name of the show: `kukhnya`, `domashniy-arest`, `dix-pour-cent`. Must match the folder. |
| `season`,`episode` | integers matching the `sNNeNN` folder. Domashniy Arest is season 1. |
| `scenes[].scene` | 1..N, in order, no gaps. |
| `start`,`end` | SRT timestamps `HH:MM:SS,mmm`. `start` = first cue of the scene, `end` = end of its last cue. |
| `title`,`summary` | English working title; one line saying what happens. |
| `characters` | Who speaks or is present, names as in `characters.md`. |
| `location` | Where it happens, short ("restaurant kitchen", "Max's flat"). |
| `merge` | `null`, `"prev"` or `"next"`. A very short transitional scene (a few lines, no plot of its own) stays **in the list** with `merge` naming the neighbour it folds into; it needs no script or art. Its lines may be used by the neighbour's story. |

Coverage rules (checked): scenes in time order, no overlap; **every subtitle cue of the episode lies inside some
scene** (else ERROR); the last scene reaches the last cue; uncovered gaps >1 s between scenes are warnings; a scene with
a >120 s silence between cues is flagged as maybe two scenes.

A scene break is: a long silence (`tools/gaps.py`), a change of location, or a change of who is present/speaking.
Mid-sentence subtitle splits across a long gap (cue ends "You can't", next starts "just pop out…") are NOT breaks.

## Schema and canonical form (v1)
Machine-readable: `spec/schema/scenes.schema.json`, enforced by `tools/validate.py`.
- Top level has exactly `schemaVersion` (`1`), `show`, `season`, `episode`, `title` (string or null), `scenes`.
  No `source_file`, `total_cues`, `source`.
- Each scene has exactly `scene`, `start`, `end`, `title`, `summary`, `characters`, `location`, `merge`. No `id`,
  `time_range`, `status`, `cue_start`, `cue_end`, `merged_into` (the scene id is derived: `<show>-sNNeNN-scene-NN`).
- `title` and `summary` are **English only**: not the bilingual `<target>  (<English>)` form (that belongs in
  `scene-NN.json`), no double spaces, never placeholder text such as `The characters discuss their situation.`
- `location` is never empty.
