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

## 2. Walk-through: translation only (owner requirement)

The current published format is the reference. Read these complete scenes before writing:

- `originals/dvorik-u-mosta/s01e01/scene-01.json` (public Original).
- `out/kukhnya/s01e01/scene-01.json` (format reference only; keep this adaptation private).

After each replayed target-language line, the narrator says only its quoted translation. Do not append grammar lessons,
word definitions, cultural commentary, a plot explanation, prompts, quizzes or other embellishments. Written token notes,
grammar, examples, forms and sourced etymologies/history remain complete in the app.

For example, replay `Нет, ваш поезд на втором пути.` in the character's Russian voice, then the British female narrator
says only `'No, your train is on track two.'` The following segment is the next Russian line, not an explanation.

Keep the existing sequence: scene introduction; full conversation; line-by-line replay and translation; full unchanged
conversation again; short reassuring closing and the character's farewell. Use the standard transitions and pacing from
the reference. Do not treat changing TTS provider as permission to change the editorial format.

`tools/validate.py --require-notes --strict-teaching` already accepts translation-only walkthroughs cleanly (zero
explanations). Its historical teaching-density checks apply when explanation text exists; they are not an instruction to
add explanation text. The previous prose requirement to teach a grammar point in every scene was stale and contradicted
the current published examples and the owner's explicit preference.

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
* **Original language only.** Story lines come from the `<lang>` source, which is a transcript of the episode's original
  audio: its own-language subtitles or Whisper, never a dub and never a subtitle translated from another language. An
  `.en.srt` beside it is only a meaning aid for glosses. Netflix Japanese captions (`the-naked-director`) carry speaker names
  `（村西とおる）`, furigana `村西(むらにし)` and sound notes `（…のあえぎ声）`: use them to attribute lines and read names, but
  never put them in a line.
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

**Known weak spot: stammers and bangs inside a take.** Owner listening (2026-11-02) heard a stammered "Et demain, tu
déjeunes avec Audiard" (dix-pour-cent s01e01 scene-02) and a loud bang between some sentences. The joins are not the
cause: `render/audio.py` trims and fades every clip, and the silence between sentences measured clean. The noise is
inside the take the TTS produced: Qwen3-TTS sometimes repeats a syllable, or starts or ends a take with a burst. Whisper
CER does not catch these: Whisper tidies away repeats, and a bang is not a word. The old renders show `retake.takes: 0`,
so no take was ever redone. Before a take is accepted, gate it on all of these:

* **Length:** its duration against the voice's median seconds per character. A take more than ~1.35x as long as
  expected, or with an internal pause over ~0.6 s, is a stammer or a hang. Retake it.
* **Verbatim repeats:** a Whisper pass with word timestamps and no text normalisation. A word or syllable said twice
  in a row that the text does not repeat fails the take.
* **Transients:** a 10 ms window whose peak is more than ~4x the take's speech RMS, or a low-frequency (<150 Hz) burst,
  especially in the first or last 80 ms. Retake it, or trim it if it lies outside the words.
* **Best of N:** render 2-3 takes of every target-language line (seed or temperature varied) and keep the one that
  passes with the lowest CER. Lower the sampling temperature or raise the repetition penalty if repeats stay common.

* **Same voice:** owner listening also heard the narrator sound like different people from one sentence to the next.
  A voice described in words (voice design) is re-imagined on every take. Design the narrator (and each character)
  once, keep one approved reference clip, and clone every take from that clip with the same settings. Gate each take
  on speaker similarity (e.g. an ECAPA or WavLM speaker embedding, cosine against the reference); retake outliers.

Record the counts in `report.json` `retake` and in `out/PROGRESS.md`.

Then listen to at least the first scene of each episode, and every scene a gate flagged. Fix the content and re-render.
Never patch an mp3.

**Known weak spot: the English narrator.** Owner listening found narrator sentences that lose words or come out flat. A
short phrase such as "I wish you..." was left out, and the intonation did not match the meaning: questions not rising,
wishes and warnings read like a list. Whisper CER can still pass when a short phrase is missing. So in review, compare
the narrator's audio word for word against the script (the `timing.json` items marked `ok: false` or `missing` are the
first place to look), and judge tone, not just words. Re-take or re-word such sentences, try a different seed, or try a
stronger English TTS, and record what worked in `out/PROGRESS.md`.

**Run an English narrator bake-off early** (contract §4 rules apply). The owner suspects a different English model would
sound better. Render the same 30 narrator sentences (questions, wishes such as "I wish you...", warnings, quoted glosses) with
F5-TTS v1 (today's reference), Qwen3-TTS-12Hz-1.7B (Base, and VoiceDesign for a fresh warm narrator), Chatterbox (its
exaggeration control helps intonation) and any other openly licensed English TTS that fits the A100. Score each on Whisper
CER, dropped words, and a blind listen by you and by Gemini for natural intonation. Switch the narrator only if the winner is
clearly better and passes `check_render.py`. The model goes into `meta.tts` and the render key, so everything re-renders
by itself.
