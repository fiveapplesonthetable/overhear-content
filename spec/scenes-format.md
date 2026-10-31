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
- Top level requires `schemaVersion` (`1`), `show`, `season`, `episode`, `title` (string or null), `scenes`; optional `coverage` explicitly declares a taster excerpt (below).
  No `source_file`, `total_cues`, `source`.
- Each scene has exactly `scene`, `start`, `end`, `title`, `summary`, `characters`, `location`, `merge`. No `id`,
  `time_range`, `status`, `cue_start`, `cue_end`, `merged_into` (the scene id is derived: `<show>-sNNeNN-scene-NN`).
- `title` and `summary` are **English only**: not the bilingual `<target>  (<English>)` form (that belongs in
  `scene-NN.json`), no double spaces, never placeholder text such as `The characters discuss their situation.`
- `location` is never empty.

## Explicit taster excerpts

Whole-episode coverage remains the default. A user-requested short taster can declare the optional top-level object:

```json
"coverage": {
  "type": "excerpt",
  "start": "00:00:05,760",
  "end": "00:01:17,520",
  "sourceSha256": "<SHA-256 of the complete retained source SRT bytes>",
  "reason": "One reviewed opening taster; the rest of this episode is not published."
}
```

Keep original source captions intact, including their numbering and source-relative timestamps. If no native caption
track exists, a reviewed partial transcript must be clearly described as partial in the source-review document; never
invent or imply the rest of an episode was transcribed. The hash binds exactly that retained transcript, not a claim
of full episode verification. The reason must describe the actual bounded scope. Use a taster label in the lesson's
English title/intro so users can see the scope.

Every cue overlapping the declared interval must be fully inside it (never cut through a cue), and every cue in that
interval must belong to a scene. All scene boundaries and script source citations must stay in the declared interval;
scripts must cite the same hashed subtitle file. Every original story line must have an indexed citation whose fragment occurs in that line as well as in the source cue; empty citation lists and out-of-range line indexes fail. Ordinary notes, script, teaching, cast, art and source-fragment checks
still apply. The excerpt declaration does not approve audio, word timing, native accuracy or publication. Without this
object the existing full-episode coverage and end-time checks apply unchanged. It is an optional v1 extension.

Registered taster shows are Die Discounter (`die-discounter`, `de-en`), Paquita Salas (`paquita-salas`, `es-en`), Boris
(`boris`, `it-en`), The Producers (`the-producers`, `ko-en`), The Naked Director (`the-naked-director`, `ja-en`), Behind
the Scenes (`behind-the-scenes`, `zh-en`) Al Maktab (`al-maktab`, `ar-en`) and Porta dos Fundos (`porta-dos-fundos`, `pt-en`, Brazilian Portuguese). Registration alone never activates a pair.

### Short taster structure

A script within an explicit excerpt may additionally declare `"format": "taster"` (authoring modules: `FORMAT = "taster"`).
This permits a genuinely short story without padding to the full-lesson twenty-segment minimum; at least seven
segments and the existing introduction/story/walk-through/exact-recap/outro structure still apply. The recap must
repeat the whole original story unchanged. Every original story line remains source-cited. Ordinary annotations,
teaching and audio gates stay in place. Without the matching excerpt, the taster marker is an error.

An explicit taster may finish naturally with its English outro (`CLOSING = None` in compose), or with a replay of an
actual story line. It need not fabricate a new target-language farewell absent from the source. A newly authored
farewell is also allowed when genuinely synthesized and verified; do not pretend it came from the show. Full lessons
retain the existing native farewell and minimum-length rules. Original recordings remain private verification and
voice-conditioning inputs; final public lesson dialogue is generated and independently checked.
