# The story recipe and house rules

Adapted from the project's recipe. Every scene becomes one short listening story ("scene script").

## Cast (fixed)
- **narrator** = voice `sky`. English only, calm London delivery, like a friend explaining. No "welcome back!",
  no exclamations, no hype, no innuendo. Reassure, don't perform.
- Target-language speakers. Each scene has at most **three** speaking roles besides the narrator; fewer is better.

| show language | protagonist role key (always present) | other role keys (any name, voice from this pool) |
|---|---|---|
| ru (Russian) | `anya` -> voice `alisa` | `anja` or `angelina` (e.g. `chef`, `lena`, `seller`) |
| fr (French)  | `lea`  -> voice `lucie` | `emilie`, `theo`, `marcel` |

The protagonist key is the *viewpoint character* of the scene retold for the learner (the listener's stand-in).
Other roles get a display name in `labels` (role -> name in the target language). Each role has its own voice.
Characters from the show who have no voice are spoken about by the narrator or folded into the nearest role.

## Level and tone
- **A1** (Duolingo section 2/3): very simple vocabulary, short present-tense sentences, a few new words per scene,
  reuse words from earlier scenes. Past/future only if the source line needs it, kept simple.
- Target-language text must read naturally to a native speaker. Polite *вы / vous* with strangers and bosses,
  *ты / tu* with friends. No textbook stiffness, no translationese.
- Lines come from the subtitle file where possible (verbatim or lightly adapted); write new lines only to glue the
  scene together. Every line taken from a subtitle goes in `source.lines` (cue number + exact fragment).
- The scene must stay true to what happens in that part of the episode (who, where, what changes).

## Five parts (in this order)
1. **Narrator intro** (2-3 sentences). Scene 1 of an episode: full intro (show, who the characters are, the setting,
   what the episode is about). Later scenes: one-sentence bridge + recap ("Meanwhile, back in the kitchen, ... Last
   time ...") then the situation. Every scene must work alone and back to back with its neighbours. Say we hear it
   in the target language first and not to worry about catching every word.
2. **Whole story in the target language**: 12-18 short lines, a tiny plot with a small warm turn.
3. **Narrator walk-through**: go back through it in English, replaying key target lines (verbatim from the story, one
   sentence at a time, by the right role) then giving their meaning; teach 1-2 grammar points in passing.
   Narrator text never contains target-language words (replays are separate target segments).
4. **Whole story again**: the same lines, unchanged, shorter gaps.
5. **Narrator send-off** (2 sentences; reassure; "see you next time") then **one short target-language line**
   from a character (Пока! / До свидания! / À bientôt!). The last segment is always that target line.

## Gaps (seconds of silence after a segment)
0.8 after the intro; 0.55 between story lines (pass 1); 0.4 after narrator walk-through lines; 0.55 after a replayed line;
0.9 at section boundaries (last story line, last walk-through line); 0.5 in the second pass; 0.5 after the outro;
0.3 after the final line. `tools/compose.py` applies all of these for you.

## Text rules
- No stress marks (U+0301) anywhere except in `stress` fields.
- French: punctuation attached to the word (`là?`, `Bonjour!`), no space before `? ! : ;`, straight apostrophe `'`,
  no guillemets in spoken lines.
- Russian: Cyrillic only in spoken lines (no Latin letters).
- Split sentences with `. ! ? …`; each segment is 1-2 sentences.
