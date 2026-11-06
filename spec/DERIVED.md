# Derived series: what the public app plays

From now on, **the public Overhear app plays only "derived" stories**: stories you create from scratch. They have their own settings,
characters, names and plots. Everything in `out/` is adapted from real TV shows (Kukhnya, Dix pour cent, Paquita
Salas and the rest). That content stays and keeps shipping as it does now, but it goes to a private tier that only the owner's
account can open, for testing. The public no longer sees it.

**The names.** The owner's app has a content setting with two choices, and this repo uses the same words:
**Original** is the adapted TV-show content in `out/`, and **Derived** is the new content this file describes. "Derived"
is only a label. These stories must be entirely your own, never derived from any existing work (section 2).

This file says what to write. The scene recipe, the formats, the checkers and the render pipeline are unchanged:
`spec/recipe.md`, `spec/quality.md`, `spec/OUTPUT-CONTRACT.md` and the README loop all still apply, except where this file
says otherwise.

## 1. Where derived content lives, and how it ships

Derived shows live in their own folder and ship through their own release tags. The publishing machine runs a separate
upload pipeline for them, and that pipeline feeds the public app. Nothing about a show decides its tier except where it
lives:

| | "Original": adapted shows (private tier) | "Derived": new shows (public app) |
|---|---|---|
| content | `out/<show>/` | `derived/<show>/` (the same per-show layout as `out/`) |
| sources | `sources/<show>/` | none |
| GitHub release tag | `render-<show>-sNNeNN` | `derived-<show>-sNNeNN` |

What you need to change in this repo:

* **The tools take the content root.** `tools/validate.py`, `tools/compose.py`, `render/pipeline.py`,
  `tools/check_render.py` and `tools/package_render.py` must work on `derived/` exactly as they do on `out/`. Add a
  `--root derived` option, or let them infer it from the path, whichever is simpler.
* **Packaging** an episode from `derived/` releases it as `derived-<episode>`, never `render-<episode>`. Episode ids
  never collide between the two folders: a derived show's slug must not equal any slug in `out/`.
* **Validation for a derived show** skips the cue checks, because there are no sources: `source.lines`, cue ranges,
  `tools/gaps.py`. Its scripts carry no `source` block, and the validator rejects one if present. For `out/` the checks
  stay exactly as they are. Add tests for both cases.
* **Progress** for derived shows goes in `derived/PROGRESS.md`.

You create everything for these shows yourself: the story, the scripts, the notes, the art, the voices (`spec/voices.md`)
and the full rendered audio. The owner only describes what is wanted. Nobody writes the stories for you.

## 2. Originality: the one rule that matters most

We are writing these because adapted content is a copyright risk. A derived show that echoes a real one brings the risk
straight back.

* **Premise, setting, characters and plots are new.** Don't retell, rename or "inspire" from any existing film, series, book,
  game or sketch, including the shows in `out/`. No famous premise with the names changed.
* **Names are new.** Use ordinary names that are common in the country, invented business and place names (real cities
  and districts are fine), and no names of real people, brands or existing fictional characters.
* **Lines are new.** Write every line yourself. No catchphrases, song lyrics, film quotes or lines lifted from `sources/`.
  Common everyday phrases ("Thank you very much", "See you tomorrow") are of course fine.
* **Art is new.** Draw the characters as `characters.md` describes them, per `art/style/STYLE.md`. They must not look like any
  real actor or person, and no logo or brand may appear.
* **Originality review.** Gemini reviews every show bible (section 4) and every episode with these questions. Does this
  premise, cast or episode resemble an existing work? Name it if so. Is any line a known quote? Fix whatever it finds before
  you commit. Record the check in `derived/PROGRESS.md`.

## 3. The shows

There is one derived series per language pair, at A1, with the same scene recipe as today: intro, story, walk-through,
replay and outro, with the English narrator. Each show is a warm, low-stakes comedy-drama about everyday life. Everyday
settings give A1 learners the words they need: greetings, shopping, food, work, directions, family, time and money. Every
episode should leave a small question that makes the listener want the next one.

The premises below are suggestions only. You write the stories: keep a premise, rework it, or replace it with a better
idea of your own, as long as it stays original and everyday. Choose your own title, slug and character names, in the
target language.

| pair | premise |
|---|---|
| ru-en | A small moving company in St Petersburg. A new hire on her first week, a grumpy veteran mover, and the owner who answers the phone. Each episode is a new flat and a new client. |
| fr-en | Two adult siblings inherit their aunt's bakery in a Lyon neighbourhood, and neither of them can bake. Regulars, a rival café across the street and a patient old baker. |
| es-en | A family-run hostel in Valencia. The daughter is back from abroad, her father resists every change, and guests arrive from everywhere. |
| pt-en | A tiny community radio station in Recife (Brazilian Portuguese). The morning host, the technician who fixes everything and listeners who call in. |
| it-en | A driving school in Bologna. The instructor, the office manager and a new student each episode. |
| de-en | A flat-share in Leipzig: a student, a night-shift nurse and a retired neighbour who keeps dropping by. |
| ar-en | A family pharmacy in Amman (Jordanian Arabic, which the existing Arabic voice profile already fits). The pharmacist, her younger cousin and the neighbourhood. |
| ja-en | A neighbourhood convenience store in Osaka on the night shift. The student clerk, the manager and the regulars. Standard, polite Japanese. |
| ko-en | A small bakery-café in Seoul run by a former office worker who just quit her job. Her part-timer and the regulars. |
| zh-en | A dumpling shop in Chengdu run by three generations of one family. Standard Mandarin. |

**Size:** a season has 6 episodes of 8-12 scenes each, with each scene the usual length (`spec/recipe.md`).

**Order: all ten languages, in a repeating cycle of episodes.**

1. Russian: 3 episodes.
2. French: 2 episodes.
3. 1 episode each of Spanish, Italian, Portuguese, German, Arabic, Japanese, Korean and Chinese.
4. Back to step 1 with the next episodes, and keep cycling.

Never skip a language or stop at the European ones: Arabic, Japanese, Korean and Chinese get their episodes in every
cycle. Make each language's voices (`spec/voices.md`) before its first episode is due, so no language stalls the cycle.
When a season's 6 episodes are done, carry on into that show's season 2 in the same cycle. Season 2 has a new 6-line arc
in the bible, with its own originality review.

Derived content now comes before all work on the adapted shows in `out/`. That content is private now, so fix it only
when no derived episode is waiting.

## 4. Writing a show

1. **Bible**: `derived/<show>/bible.md`, written before any scene. It holds the premise, setting, tone, the season's arc in 6
   lines (one per episode), and the recurring places and running jokes. The originality review (section 2) runs on it
   first.
2. **Cast**: `cast.json` and `characters.md`, as today (`spec/quality.md` §1). Keep the cast small: 3-4 regulars plus
   a few one-episode guests. Give each regular a way of speaking a listener can recognise (formal or casual address,
   favourite words). It carries the teaching.
3. **Episode outline**: `derived/<show>/sNNeNN/scenes.json`. Write the scene list from the outline, not from a cue file. Leave
   out the cue and time fields a derived show doesn't have, and give each scene a one-line summary.
4. **Scenes**: follow the README loop from step 4, with no cues. Replace "faithful to the source" with "faithful to the
   bible and the outline". Everything else in `spec/quality.md` still holds: A1, short lines, clean register, natural target
   language, explanations that teach one concrete thing.
5. **Art, notes, validate, review, commit, render, check and package** all work as today. The cover goes in `art/cover.webp`.
6. Plan vocabulary across the season. E1 introduces the core words (greetings, the place, the jobs), and later
   episodes reuse them and add a few new ones per scene. This is the main teaching advantage we have over adapted content,
   so use it.

## 5. Done means

A show's season is done when all 6 episodes pass the README "Done means" list, and the bible and every episode have a
clean originality review. Report progress per show in `derived/PROGRESS.md`.
