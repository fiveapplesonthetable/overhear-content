# Overhear Originals: what the public app plays

From now on, **the public Overhear app plays only Overhear Originals**: stories you create from scratch. They have their own settings,
characters, names and plots. Everything in `out/` is adapted from real TV shows (Kukhnya, Dix pour cent, Paquita
Salas and the rest). That content stays and keeps shipping as it does now, but it goes to a private tier that only the owner's
account can open, for testing. The public no longer sees it.

**The names.** The new content is **Overhear Originals**: our own shows, like a studio's "originals". The
adapted content in `out/` is **TV adaptations**. The owner's app has a switch with that name, and only the owner can see it.

This file says what to write. The scene recipe, the formats, the checkers and the render pipeline are unchanged:
`spec/recipe.md`, `spec/quality.md`, `spec/OUTPUT-CONTRACT.md` and the README loop all still apply, except where this file
says otherwise.

## 1. Where Originals live, and how it ships

Original shows live in their own folder and ship through their own release tags. The publishing machine runs a separate
upload pipeline for them, and that pipeline feeds the public app. Nothing about a show decides its tier except where it
lives:

| | TV adaptations (private tier) | Overhear Originals (public app) |
|---|---|---|
| content | `out/<show>/` | `originals/<show>/` (the same per-show layout as `out/`) |
| sources | `sources/<show>/` | none |
| GitHub release tag | `render-<show>-sNNeNN` | `original-<show>-sNNeNN` |

What you need to change in this repo:

* **The tools take the content root.** `tools/validate.py`, `tools/compose.py`, `render/pipeline.py`,
  `tools/check_render.py` and `tools/package_render.py` must work on `originals/` exactly as they do on `out/`. Add a
  `--root originals` option, or let them infer it from the path, whichever is simpler.
* **Packaging** an episode from `originals/` releases it as `original-<episode>`, never `render-<episode>`. Episode ids
  never collide between the two folders: an original show's slug must not equal any slug in `out/`.
* **Validation for an original show** skips the cue checks, because there are no sources: `source.lines`, cue ranges,
  `tools/gaps.py`. Its scripts carry no `source` block, and the validator rejects one if present. For `out/` the checks
  stay exactly as they are. Add tests for both cases.
* **Progress** for original shows goes in `originals/PROGRESS.md`.

You create everything for these shows yourself: the story, the scripts, the notes, the art, the voices (`spec/voices.md`)
and the full rendered audio. The owner only describes what is wanted. Nobody writes the stories for you.

## 2. Originality: the one rule that matters most

We are writing these because adapted content is a copyright risk. An original show that echoes a real one brings the risk
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
  you commit. Record the check in `originals/PROGRESS.md`.

## 3. The shows

There is one original series per language pair, at A1, with the same scene recipe as today: intro, story, walk-through,
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

Originals now come before all work on the adapted shows in `out/`. That content is private now, so fix it only
when no Originals episode is waiting.

## 4. Writing a show

1. **Bible**: `originals/<show>/bible.md`, written before any scene. It holds the premise, setting, tone, the season's arc in 6
   lines (one per episode), and the recurring places and running jokes. The originality review (section 2) runs on it
   first.
2. **Cast**: `cast.json` and `characters.md`, as today (`spec/quality.md` §1). Keep the cast small: 3-4 regulars plus
   a few one-episode guests. Give each regular a way of speaking a listener can recognise (formal or casual address,
   favourite words). It carries the teaching.
3. **Episode outline**: `originals/<show>/sNNeNN/scenes.json`. Write the scene list from the outline, not from a cue file. Leave
   out the cue and time fields an original show doesn't have, and give each scene a one-line summary.
4. **Scenes**: follow the README loop from step 4, with no cues. Replace "faithful to the source" with "faithful to the
   bible and the outline". Everything else in `spec/quality.md` still holds: A1, short lines, clean register, natural target
   language, explanations that teach one concrete thing.
5. **Art, notes, validate, review, commit, render, check and package** all work as today. The cover goes in `art/cover.webp`.
6. Plan vocabulary across the season. E1 introduces the core words (greetings, the place, the jobs), and later
   episodes reuse them and add a few new ones per scene. This is the main teaching advantage we have over adapted content,
   so use it.

## 5. The full learning data, for every language

An Originals episode ships with the whole learning layer the app shows: translations, word notes, pronunciation, word tables,
dictionary entries, word histories and learning notes. This holds for all ten languages, not just Russian and French. Today
several languages have gaps; Originals close them.

1. **Scene notes** (`spec/annotations.md`) for every scene, as today: a translation for every line, and for every word its
   lemma, part of speech, gloss and grammar, plus a lexicon entry with meanings, examples and related words.
2. **Pronunciation and transliteration on every word.** Russian stress marks, French IPA, and for the non-Latin scripts a reviewed
   reading on every word with no gaps: Japanese kana, Mandarin pinyin, and Korean and Arabic readings too (they are optional in
   `annotations.md` today; for Originals they are required). Romanisation for Japanese, Korean and Arabic follows one standard
   per language; write which one into `annotations.md` and keep to it. The publisher reports reading coverage per pair: it must be
   100% for every Originals scene.
3. **Word tables for every language.** `annotations.md` defines conjugation and declension tables only for Russian and French.
   Add the tables for the other eight to `annotations.md`, in the same shape (title, columns, rows), and teach the validator to
   check them: at least present-tense conjugation for verbs in es, it, pt and de, plus their past and noun or adjective forms where
   the language has them; Arabic verb conjugation by person, gender and number, and noun forms with gender and plural; Japanese
   verb and adjective forms (dictionary, polite, negative, past, te-form); Korean verb and adjective endings (plain, polite,
   past, negative). Mandarin has no inflection, so its words carry `forms: null`; give its measure words in the lexicon instead.
   Every verb, noun and adjective that an Originals scene uses gets its table.
4. **Dictionary** (`dictionary/<pair>.json`): an entry for every lemma that Originals use, for all ten pairs. Japanese, Korean
   and Russian have no file today and the others are thin.
5. **Word histories** (`word-origins/<pair>.json`): a sourced history for the words Originals use, by the existing rules: check
   each against an authoritative entry, link it, and never publish an unsourced one. Every lemma in the episode's lexicon
   needs one before you package the episode (`tools/check_render.py` enforces it; see README). Words already published without
   a history are listed in `word-origins/backlog/originals.json`; work them down as README says.
6. **Learning notes** (`learn/<pair>/`): today only Russian and French have them. Write notes for all ten pairs, about 10 per
   pair to start, covering what the season teaches (greetings, polite address, numbers and money, the main verb patterns, the
   particles or cases a learner meets first), with examples that point at Originals scenes.

**These folders are shared by both tiers.** `dictionary/`, `word-origins/` and `learn/` are published to the public app as well as
the private one, so nothing in them may quote a line from a TV adaptation (`out/`) or point an example at an `out/` scene.
Write your own example sentences or cite Originals scenes. Where an existing file quotes an adapted scene, replace that example.

**Voices before the cycle reaches a language.** Portuguese renders have mostly failed so far (8 of 9 in the last batch): find
out why and fix it before the first Portuguese Originals episode is due, and check that every other language renders end to end
before its first episode.

## 6. Done means

A show's season is done when all 6 episodes pass the README "Done means" list, the learning data in section 5 is complete for
them, and the bible and every episode have a clean originality review. Report progress per show in `originals/PROGRESS.md`.
