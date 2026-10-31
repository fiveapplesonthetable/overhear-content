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

## Schema and canonical form (v1)
Machine-readable: `spec/schema/notes.schema.json`, enforced by `tools/validate.py`.
- Top level has exactly `schemaVersion` (`1`), `id` (the id of the scene script it annotates), `lines`, `lexicon`.
  Not `show`/`season`/`episode`/`scene`.
- `lines[]` has exactly `seg`, `trans`, `words`. `words[]` has exactly `t`, `lemma`, `pos`, `stress`, `gloss`, `gram`
  (`gram`, not `grammar`; no `note`). `stress` is always present: the marked form / IPA, or `null` only for names, for
  Russian one-vowel words and words with `ё`, and never for a French word.
- **Tokens**: `words[].t` are the segment text split on whitespace, one entry per token, in order. Do not merge
  (`ce que`, `un peu`) and do not split elisions or hyphenated words (`J'ai`, `l'addition.`, `Qu'est-ce`,
  `réponds-moi.` are one token each; lemma = the main word). A bare dash token (`—`) is skipped.
- `lexicon{}` entries have the required fields `lemma, stress, pos, gloss, meanings, forms, moreForms, examples (2-3),
  related`, and optionally `aspect` (`impf`|`pf` only), `pair`, `gender` (`m`|`f`|`n` only), `plural`, `animacy`
  (`anim`|`inan`), `number` (`"pl"`, for plural-only nouns such as `деньги`, instead of any gender value), `governs`,
  `register`. No other fields (`animate`, `transitivity`, `ipa`, `note` do not exist). `pos` is one of the 13 listed
  values, never an IPA string. Russian lexicon `stress` carries the U+0301 mark on every word of 2+ vowels.
- The same lemma has the same `pos`, `gender`, `aspect`, `pair` and `stress` in every scene's lexicon (a lemma is
  looked up, not re-decided per scene). Keys are lowercase.

## Exact native word spans and reviewed readings

`words[].span: [start, end]` uses half-open **Unicode code-point** offsets into
that script segment's exact `t`. The selected substring must equal `words[].t`.
A line uses explicit spans on every word or on none. Spans must be ordered,
nonoverlapping and cover every written letter, number and attached combining
mark; whitespace and punctuation may remain in gaps. Do not split a base
character from its marks. Do not insert spaces into Japanese or Mandarin to make
annotation easier. Python indices already use these units; Android converts them
to UTF-16 indices at the content boundary.

Japanese and Mandarin native lines require explicit spans and a reviewed
`words[].reading`. Japanese readings use contextually correct kana, including
spoken particles; a compound's reading belongs to its entire authored lexical
span, not invented per-kanji intervals. Mandarin readings use reviewed contextual
pinyin, including resolved spoken numbers. Korean and Arabic may also provide
reviewed readings; their native written spacing and logical order remain intact.
Japanese, Mandarin, Korean and Arabic `stress` values remain null: do not invent
stress or pitch-accent descriptions. `reading` is alignment guidance and does
not replace the written text or establish pronunciation/audio quality by itself.

The renderer must reject unresolved native alignment, partial coverage or
ownership that crosses independently selectable words. Missing words cannot be
published using interpolated acoustic boundaries. Source-span correctness and
actual acoustic boundary quality are separate checks.
