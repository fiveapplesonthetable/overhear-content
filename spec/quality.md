# Quality: what a good scene is

The format (`spec/OUTPUT-CONTRACT.md`) is what makes a scene *ship*. This file covers what makes it *worth listening to*.
Each rule says whether `tools/validate.py` enforces it. The rest you check by reading and listening.

**Gold scenes, copy their approach:** `out/kukhnya/s01e02/scene-01.json`, `scene-02.json` and `scene-03.json`, with their
`authoring/scene-0N.py`, plus `examples/*`. Read one before you write your first scene in a new language.

## 1. Cast: names, keys, voices (enforced)

* **One character = one role key across the whole show.** The key is the character's own name in lowercase Latin: `max`,
  `barinov`, `nastya`. There are no viewpoint or slot keys (`anya`, `lea`, `lead`, `hero`, `protagonist`, `viewpoint`,
  `main`, `extra`).
* Every show has `out/<show>/cast.json` (`spec/schema/cast.schema.json`):

      {"schemaVersion": 1, "show": "kukhnya", "other_names": ["Claude Monet", "Arcobaleno"],
       "cast": [{"key": "max", "ru": "Макс", "en": ["Max", "Maksim", "Lavrov"], "gender": "m"}, ...]}

  * `ru` is the display name in the target language, whatever the language (the field name is historical). It must equal
    the script's `labels[key]`.
  * `en` lists every name the English narration may use. The first entry is the canonical name.
  * `gender` (`m`/`f`) drives voice casting and the grammar check.
  * `other_names` holds non-character proper nouns the narration may use (places, restaurants, teams).
  * No two keys may share a `ru` name or an English name.
  * One-scene extras ("Гость", "Врач") get their own key and gender too.
* **Scripts carry no `voices`.** The renderer casts voices from `cast.json` by gender (`render/casting/<show>.json`).
* **Narration names the right person.** Every capitalised name in narrator text must belong to `cast.json` (or
  `other_names`). An explanation that follows a line must name that line's speaker, or use a pronoun or role ("the
  chef"). If the validator says the narration names X but Y speaks the line, read the source cue to see who really says
  it. Don't just rename.
* Grammar follows gender (warning): a male speaker saying a feminine past form ("Я слышала") is flagged. Fix the line or
  the speaker. If you change a story line, its notes must change too.
* `characters.md` is prose for writers and art (looks, manner). `cast.json` is the machine-read file.

## 2. Walk-through explanations: they teach the language

After a replayed line, the narrator gives its English gloss in quotes, then the explanation. The explanation is the point
of the product. It sounds like a warm, plain-spoken teacher explaining the scene to a friend. **It says one concrete thing
about the target language**, varied from line to line:

* the word for X and what it is built from: "The Russian word for 'reigns' is built from the word for tsar, so chaos is
  literally on the throne."
* a small word doing a big job: "The tiny word for 'simply' is the shrug in the sentence."
* where the language differs from English: "Russian happily doubles the no here, 'never' and 'not' together, and that's
  correct."
* a reusable chunk: "It's a handy sentence for any job you find tough, so swap in your own work for 'kitchen'."
* a named word, transliterated: "Kostya's little word 'zato' means 'but on the plus side'."
* register: "She uses the formal 'you' even while disagreeing, which is how a waitress objects to her boss."

A plot or tone note is fine on top of that ("Max sounds proud."), and fine on its own for at most about one line in four.
Vary openings and lengths. Leave out the speaker's name when it is obvious.

| bad (real lines that were rejected) | good (gold) |
|---|---|
| 'Our chef cooks the most delicious food.' Notice how naturally this everyday Russian phrase expresses the speaker's point. | 'Our chef cooks the most delicious food.' Max sounds proud. Saying "our chef" rather than "the chef" makes him sound like part of the family already. |
| 'Lavrov, you are two hours late!' The chef confronts Max with a past tense verb and duration phrase. | 'Lavrov, you are two hours late!' Barinov doesn't say "Max". He uses the surname, the way a stern boss puts you in your place. |
| 'Now go to work immediately, oguzok!' Barinov barks his signature insult using command form verbs. | 'Now go to work immediately, oguzok!' "Oguzok" is Barinov's nickname for Max. It's actually a cut of meat from the rear of the animal, so the chef is calling him scraps. |
| 'Chef, I have a very urgent question.' Notice how naturally this everyday Russian phrase expresses the speaker's point. | 'Chef, I have a very urgent question.' In Russian she says "at me is a very urgent question" rather than "I have": the question sits with her. |
| 'I am not your boyfriend.' Max delivers a blunt reality check about his role. (plot paraphrase, teaches nothing) | 'And we simply pour them wine.' That is Kostya's job in one line. The tiny word for "simply" is the shrug in the sentence. |

**Enforced by `tools/validate.py`:**

| rule | limit |
|---|---|
| no grammar-label endings ("... with an imperfective verb.", "... using a superlative adjective.") | error per line |
| no reused templates: the first 6 words of an explanation, with quotes as Q, names as N and lowercased | more than 15 uses in a show is an error on every such line |
| no repeated phrases: any run of 4+ words in the explanations | more than 50 uses in a show is an error |
| grammar jargon (verb, noun, tense, case names, ...) | in more than 30% of a scene's explanations is an error; aim for one in five |
| word-teaching share: explanations that point at a word, chunk or form | below 60% in a scene with 4+ explanations is a warning; with `--strict-teaching` it is an error. Release runs use `--strict-teaching`. |

The run of the whole of `out/` prints `SHOW <show>: word-teaching: N%` and the most repeated phrases. Run it before every push.
Template and phrase limits apply show-wide, so they are only judged on a whole-`out/` run.

**This cannot be done by a script.** Write every explanation by reading the scene and its source cues. A generator that
fills sentence skeletons with gloss words is exactly what the checks catch, and listeners hear it at once ("why does every
sentence end with the part of speech", "it's so robotic"). Opus writes, Gemini reviews (see README "Review"). Plain words
like "the word for", "literally", "built from" and "swap in" are not jargon; they are what we want.

## 3. Story content (read, not enforced)

* **Faithful.** The scene tells what really happens in that stretch of the episode: who, where, what changes. Don't invent
  plot, don't change who says what, don't add jokes the source doesn't make.
* **A1.** Short present-tense sentences, usually 12 words or fewer. Past or future only when the source needs it. A few new
  words per scene, and reuse earlier ones. The intro is 2-3 sentences, not 70 words.
* **Adapted, not transcribed.** Short real lines, adapted and shortened. Never a long verbatim stretch of the episode.
  Commentary nobody says to anybody becomes narration or goes.
* **Clean register.** No coarse words or slurs in story lines. Replace them.
* **No real politicians by name** in story lines ("the president", not the name).
* **Natural target language.** It must read naturally to a native speaker, with correct formal or informal address. A gloss
  should sound like English a person says ("I feel really bad", not "To me is very bad").
* **Outro** says only what the scene showed, reassures, says "see you next time", then the new target-language farewell.
* **Machine-transcribed sources** (Whisper `.srt`, e.g. Kukhnya S2-S6 and the pilots without subtitles) can mishear names
  and numbers. When a cue is unclear, use a line you are sure of, or leave it out. Never build a line on a guess.

## 4. Notes (enforced)

* `words[].t` are the segment text split on whitespace: one entry per token, in order, nothing merged or split. Bare dashes
  are skipped. ja/zh use the author's annotation spans (`spec/annotations.md`).
* `stress`: Russian carries U+0301 on every word of two or more vowels (`null` only for names, one-vowel words and `ё`).
  French uses IPA. Other languages follow `spec/annotations.md`.
* **One lexicon shape per lemma across a show:** the same `pos`, `gender`, `aspect`, `pair` and `stress` everywhere. Lowercase
  keys. Table titles use the names in `spec/annotations.md`.

## 5. Art (enforced: format and uniqueness)

One picture per non-merged scene: `scene-NN.webp`, 1024x1024, no text in the image, never byte-identical to another scene's.
It shows *this* scene's moment and characters as `characters.md` describes them, in the show's style (`art/style/STYLE.md`).
Flat, generic figures that could be anyone are a review failure.

## 6. Audio (enforced by the render gates; you listen)

The pipeline gates every sentence on Whisper CER and retakes failures. Read every `report.json`:

* `stress.unresolved`: Russian words the stress model couldn't place. Add `stress` in the notes and re-render.
* `warnings` and `timing.notOk`: these should be near zero.

Then listen to at least the first scene of each episode, and every scene a gate flagged. Fix the content and re-render.
Never patch an mp3.

**Known weak spot: the English narrator.** Owner listening found narrator sentences that lose words or come out flat. A
short phrase such as "I wish you..." was left out, and the intonation did not match the meaning: questions not rising,
wishes and warnings read like a list. Whisper CER can still pass when a short phrase is missing. So in review, compare
the narrator's audio word for word against the script (the `timing.json` items marked `ok: false` or `missing` are the
first place to look), and judge tone, not just words. Re-take or re-word such sentences, try a different seed, or try a
stronger English TTS (contract §4), and record what worked in `out/PROGRESS.md`.
