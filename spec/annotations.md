# Annotations: `scene-NN.notes.json`

Translations and word notes for every target-language line. Example (excerpt): `examples/kukhnya-s01e02-knife/scene.notes.json`.
Required for a finished scene (`--require-notes`). You write it yourself, carefully.

```json
{"lines": [
   {"seg": 2, "trans": "Chef, I didn't take it.",
    "words": [{"t": "брала.", "lemma": "брать", "pos": "verb", "stress": "брала́",
               "gloss": "took (she)", "gram": "past, feminine singular, imperfective"}]}],
 "lexicon": { "брать": { "...": "see below" } } }
```

## `lines[]`
| field | meaning |
|---|---|
| `seg` | index into `segments` of the scene script. Every non-narrator segment needs an entry. |
| `trans` | natural English translation of that segment. |
| `words[]` | one entry per spoken word, **in order**; `t` is the token exactly as in the text, punctuation attached (`"шеф!"`), and must occur in the segment text in order. |

## `words[]`
| field | meaning |
|---|---|
| `t` | token as written. |
| `lemma` | dictionary form, lowercase, ё kept. Must be a key of `lexicon` (except `pos:"name"`). |
| `pos` | one of `noun verb adj adv pron prep conj part num interj det phrase name`. |
| `stress` | the pronunciation line (below), or null. |
| `gloss` | meaning **in this line**, a few English words. |
| `gram` | short grammar: case/tense/person/number/gender/aspect, e.g. `imperative, 2nd person singular, imperfective`. |

### `stress` per language
- **ru**: the word with a combining acute U+0301 after the stressed vowel (`ре́жь`). Same letters as the word; ё gets
  no mark; one-vowel words no mark. This is the *only* place U+0301 may appear anywhere in the output.
- **fr**: the word's IPA, no slashes/brackets/spaces/stress marks (`laʒɑ̃s` for *l'agence*). IPA symbols only,
  never accented spelling letters.

## `lexicon{}` (one entry per lemma used, key = lemma)
| field | meaning |
|---|---|
| `lemma`, `stress`, `pos`, `gloss` | as above (`gloss` = general meaning). Required. |
| `aspect`, `pair` | ru verbs: `"impf"`/`"pf"` and the other-aspect lemma (`"взять"`) or null. |
| `gender` | nouns: `m`/`f`/`n` (ru), `m`/`f` (fr); `plural`: fr nouns, plural without article. |
| `governs`, `register` | short construction note ("+ dative"), usage register ("informal"), only when relevant. |
| `meanings[]` | `{en, note}` each; at least one; cover the senses a learner will meet. |
| `forms` | the primary table (below) or null. `moreForms`: further tables, `[]` if none. |
| `examples[]` | 2-3 short `{text, trans}` sentences, clean (no U+0301). |
| `related[]` | optional `{word, gloss}`, 0-5. |

### Tables
`{"title": "Declension", "columns": ["", "sg", "pl"], "rows": [{"cells": ["nominative", "шеф", "шефы"]}]}`.
Every row has as many cells as `columns`; the first cell is the row label; a non-existent form is `—`.

| lang | pos | `forms` title; columns; rows | `moreForms` |
|---|---|---|---|
| ru | noun | `Declension`; `["","sg","pl"]`; nominative, genitive, dative, accusative, instrumental, prepositional | |
| ru | adj | `Declension`; `["","m","f","n","pl"]`; the same six cases | |
| ru | verb | `Present` (impf) or `Future` (pf); `["","sg","pl"]`; 1st, 2nd, 3rd | `Past`: `["","m","f","n","pl"]`, row `past`; optional `Imperative`: `["","sg","pl"]`, row `imperative` |
| fr | noun | optional `Forms`; `["","sg","pl"]`; row `form` ("l'agence", "les agences") | |
| fr | adj | `Forms`; `["","m","f"]`; sg, pl | |
| fr | verb | `Present`; `["","sg","pl"]`; 1st, 2nd, 3rd (cells include the pronoun: "je parle") | `Passé composé`, `Imparfait`, `Futur` (same shape); optional `Imperative` |

Other words (adverbs, prepositions, particles, pronouns) have `forms: null`, `moreForms: []`.
The validator checks table shape, that every used `lemma` has an entry, that ru nouns/adjs/verbs have `forms`, that
`stress` carries the mark and that no stray U+0301 exists elsewhere. Linguistic correctness is on you: double check
genders, aspect pairs and forms.
