# New pairs: Hindi, then English for speakers of every language

Two additions to Overhear Originals. Both reuse the Courtyard Inn master story in `originals/_english/` the way every other
pair does. Both follow `spec/ORIGINALS.md` (originality, the full learning data in its section 5, done means) unless this
file says otherwise.

The ten-language cycle in ORIGINALS.md section 3 keeps running. These pairs join that cycle and never replace it.

## 1. Hindi (`hi-en`): first

### 1a. Choose the voice model with a bake-off

The model is chosen by a measured comparison, not by assumption. Start a separate agent to run the bake-off while the cycle
continues on the main work. Give it this section as its brief, and have it report back.

**Candidates:**

| model | why it's a candidate | check before use |
|---|---|---|
| **Chatterbox Multilingual** (`chatterbox-tts`, the multilingual model) | Already installed and patched for Arabic (`render/chatterbox_ar.py`), and Hindi is one of its languages. It would need the least new setup. | The Arabic patches in `chatterbox_ar.py` may matter for Hindi too: check long sentences for truncation and questions for flat intonation. |
| **IndicF5** (`ai4bharat/IndicF5`) | F5-TTS trained on Indian languages including Hindi. It's the same model family as our Russian and English voices, so it's likely the most natural Hindi prosody. | Its licence must allow publishing the audio. If it doesn't, drop it. |
| **Indic Parler-TTS** (`ai4bharat/indic-parler-tts`) | Designs a voice from a text description, as Qwen VoiceDesign does for other languages. | Use it to make synthetic Hindi **reference** voices for the other two models. It can be a dialogue candidate as well. |

Qwen3-TTS, which most pairs use, is not believed to support Hindi. Check its current language list once. Add it as a
candidate only if Hindi is listed.

**Method:**
1. **Test set:** write 20 Hindi test lines in Devanagari. Include:
   - short A1 dialogue, questions and exclamations,
   - numbers, prices and times,
   - English loanwords as people actually say them (होटल, टिकट, फ़ोन),
   - names,
   - one long sentence of 25 words or more.
2. **References:** make 2 female and 2 male references with Indic Parler-TTS. They are synthetic, follow `spec/voices.md`'s
   rules, and use no real person's recording. Each candidate gets the same references.
3. **Render:** every line, with every candidate, with every reference.
4. **Score each take:**
   - Whisper large-v3 CER against the text,
   - speaker similarity to its reference,
   - truncation and artefact count,
   - speed on the A100.

   Then have Gemini listen to a blind shortlist. Ask it about naturalness, accent, and whether anything is shrill, thin or
   robotic (the owner's complaint about earlier Arabic and Portuguese voices, `spec/voices.md`).
5. **Decide:** pick the winner on the numbers plus the listening. Record the table, the scores and the decision in
   `originals/PROGRESS.md`.
   - Add a render profile `render/settings.hi-<model>-en.json` for the winner.
   - Add a test that the profile renders one scene end to end.

### 1b. Hindi Originals

- **Story:** localise Courtyard Inn into Hindi exactly as the other pairs do.
  - **Setting:** an Indian city of your choice.
  - **Speech:** everyday standard Hindi, the kind spoken at home and in shops. Use neither heavily Sanskritised nor heavily
    Urdu register.
  - **Cast and names:** new, by ORIGINALS.md section 2.
- **Script:** Devanagari. Hindi is a native-script pair like ja, zh, ko and ar, so every dialogue item carries `span`, and
  every word carries a reviewed reading.
  - Use one learner-friendly romanisation with vowel length marked. Pick it once, write which into `annotations.md`, and
    keep to it.
  - Reading coverage must be 100%.
- **Word tables:** add Hindi to `annotations.md` in the same table shape as the others, and teach the validator to check them.
  - **Verbs:** present habitual, progressive, perfective past (by gender and number), future, and the imperative for तू, तुम
    and आप.
  - **Nouns:** direct and oblique, singular and plural, with gender.
  - **Adjectives:** the inflecting -आ adjectives.
  - **Postpositions:** in the lexicon.
- **Learning layer:**
  - `dictionary/hi-en.json` and `word-origins/hi-en.json`, sourced by the existing rules.
  - About 10 notes in `learn/hi-en/`. Start with the three levels of "you", postpositions and the oblique case, gender
    agreement, and numbers and money.
- **Cycle:** once Hindi S1E1 passes, Hindi gets 1 episode in every cycle, like the other eight.

## 2. English for speakers of every other language (`en-<native>`): next

Today every pair teaches *from* English. These pairs teach English *to* speakers of the languages we already have.

### Order

Spanish and Portuguese are priorities. Their season 1 runs at 1 episode each per cycle before any other English pair starts:

1. `en-es` (Spanish speakers) and `en-pt` (Brazilian Portuguese speakers). Start these as soon as Hindi S1E1 ships.
2. When both reach S1E6, add the rest, 1 episode each per cycle: `en-fr`, `en-de`, `en-it`, `en-ru`, `en-ar`, `en-ja`,
   `en-ko`, `en-zh`, `en-hi`.

### What is different

- **The story is the English master.** Set it in an English-speaking city of your choice. Edit the master only where needed so
  it plays as natural spoken English at A1.
  - Each `en-<native>` pair shares the same English story text.
  - The narration and teaching are written fresh for each native language.
- **The narrator speaks the learner's language.**
  - Translations, explanations, word glosses, notes, dictionary entries, word histories and learning notes are all written in
    `<native>`.
  - The English is what's studied.
  - The scene recipe is otherwise unchanged.
- **Voices:**
  - **English characters:** design English character voices (Qwen VoiceDesign).
  - **Narrator:** the narrator for each native language comes from that language's existing render profile (Arabic and Hindi
    included). It needs one calm narrator voice per language.
- **Pronunciation:** IPA on every English word, with a single accent kept throughout (General American or Southern British,
  your choice). Write the choice into `annotations.md`.
- **Word tables:**
  - **Verbs:** base, third person singular, past, past participle and -ing.
  - **Nouns:** irregular plurals.
  - **Adjectives:** irregular comparatives.
- **Tools:** the formats, checkers and render pipeline currently assume an English narrator and English as the native
  language.
  - Generalise them so the narrator language is the pair's native language.
  - Add tests that both `ru-en` and `en-es` validate and render.
  - Make no change to existing output: the `-en` pairs must come out byte-identical.
- **App and publisher:** the app and its publisher (owner side, not this repo) currently treat English as the only native
  language.
  - Ship the first `en-es` episode as a pilot.
  - List in `originals/PROGRESS.md` anything the output contract can't express for a non-English native language, so the
    owner can update the app before more English episodes are made.
