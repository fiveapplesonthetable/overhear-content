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
- **fr, es, it, pt, de**: the word's bare IPA, no slashes/brackets/spaces/uppercase letters (`laʒɑ̃s` for *l'agence*,
  `maˈnjana` -> no `ˈ`? Note: IPA primary stress `ˈ` is fine, never U+0301 combining acute and never accented spelling
  letters like `é, ñ, ä, ç, ã`). Only `pos: "name"` may use `stress: null`.
- **en** (for `en-<native>` pairs): bare **General American** IPA on every English word (`həˈloʊ`, `ˈkɔfi`, `ˈsuːtkeɪs`,
  `ˈwɔtɚ`), no slashes/brackets/spaces/uppercase letters and never U+0301 combining acute. Only `pos: "name"` may use
  `stress: null`. (In `en-<native>` pairs, `trans`, `gloss`, `meanings[].en`, `meanings[].note`, `examples[].trans`,
  dictionary entries, word histories, and `learn/` notes are all written in `<native>`.)
- **ja, zh, ko, ar, hi**: always `stress: null`. Spoken pronunciation and romanisation live in `words[].reading` (see below).

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
| fr | noun | `Forms`; `["","sg","pl"]`; row `form` ("l'agence", "les agences") | |
| fr | adj | `Forms`; `["","m","f"]`; sg, pl | |
| fr | verb | `Present`; `["","sg","pl"]`; 1st, 2nd, 3rd (cells include the pronoun: "je parle") | `Passé composé` (and optional `Imparfait`, `Futur`, `Imperative`) |
| es | noun | `Forms`; `["","sg","pl"]`; row `form` ("la llave", "las llaves") | |
| es | adj | `Forms`; `["","m","f"]`; rows `sg`, `pl` | |
| es | verb | `Present`; `["","sg","pl"]`; rows `1st`, `2nd`, `3rd` | `Preterite` (`["","sg","pl"]`, rows `1st`, `2nd`, `3rd`) |
| it | noun | `Forms`; `["","sg","pl"]`; row `form` ("la chiave", "le chiavi") | |
| it | adj | `Forms`; `["","m","f"]`; rows `sg`, `pl` | |
| it | verb | `Present`; `["","sg","pl"]`; rows `1st`, `2nd`, `3rd` | `Passato prossimo` (`["","sg","pl"]`, rows `1st`, `2nd`, `3rd`) |
| pt | noun | `Forms`; `["","sg","pl"]`; row `form` ("a chave", "as chaves") | |
| pt | adj | `Forms`; `["","m","f"]`; rows `sg`, `pl` | |
| pt | verb | `Present`; `["","sg","pl"]`; rows `1st`, `2nd`, `3rd` (`eu`, `você/ele`, `nós`, `vocês/eles`) | `Preterite` (`["","sg","pl"]`, rows `1st`, `2nd`, `3rd`) |
| de | noun | `Declension`; `["","sg","pl"]`; rows `nominative`, `accusative`, `dative`, `genitive` (with article) | |
| de | adj | `Forms`; `["","form"]`; rows `positive`, `comparative`, `superlative` | |
| de | verb | `Present`; `["","sg","pl"]`; rows `1st`, `2nd`, `3rd` (with pronoun: "ich mache") | `Past` (`["","sg","pl"]`, `Perfekt` or `Präteritum`) |
| ar | noun | `Forms`; `["","sg","pl"]`; row `form` (plus `gender` in lexicon) | |
| ar | adj | `Forms`; `["","m","f","pl"]`; row `form` | |
| ar | verb | `Present`; `["","sg","pl"]`; rows `1st`, `2nd m`, `2nd f`, `3rd m`, `3rd f` | `Past` (same rows) |
| ja | verb | `Forms`; `["","form"]`; rows `dictionary`, `polite`, `negative`, `past`, `te-form` | |
| ja | adj | `Forms`; `["","form"]`; rows `dictionary`, `polite`, `negative`, `past`, `adverbial` | |
| ja | noun | `Forms`; `["","form"]`; rows `plain`, `polite`, `negative`, `past` (copula frame with `だ`/`です`) | |
| ko | verb | `Forms`; `["","form"]`; rows `dictionary`, `polite`, `formal`, `past`, `negative` | |
| ko | adj | `Forms`; `["","form"]`; rows `dictionary`, `polite`, `formal`, `past`, `negative` | |
| ko | noun | `Forms`; `["","form"]`; rows `with topic`, `with subject`, `with object`, `polite copula` | |
| zh | all | `forms: null`, `moreForms: []` (Mandarin has no inflection; give measure words `量词` in `meanings[].note` and `related[]`) | |
| hi | noun | `Declension`; `["","sg","pl"]`; rows `direct`, `oblique` (plus `gender` `m`/`f` in lexicon) | |
| hi | adj | inflecting `-आ` adjectives: `Forms`; `["","m sg","m pl","f"]`; rows `direct`, `oblique` (uninflecting adjectives: `forms: null`, `moreForms: []`) | |
| hi | verb | `Present habitual`; `["","m","f"]`; rows `1st sg (मैं)`, `2nd int (तू)`, `2nd fam (तुम)`, `2nd/3rd pol (आप/ये/वे)`, `3rd sg (वह)`, `1st pl (हम)` (or `["","sg","pl"]` / gender-number rows) | `Progressive`, `Perfective past` (by gender and number: `m sg`, `m pl`, `f sg`, `f pl`), `Future`, and `Imperative` (`तू`, `तुम`, `आप`) |
| hi | prep | postpositions (`में`, `पर`, `को`, `से`, `का/के/की`, `के लिए`) use `pos: "prep"`, `forms: null` (inflecting `का` may give `Forms` `m sg / m pl / f`) | |
| en | verb | `Forms`; `["","form"]`; rows `base`, `3rd sg`, `past`, `past participle`, `-ing` | |
| en | noun | irregular plurals only: `Forms`; `["","sg","pl"]`; row `form` (regular nouns: `forms: null`, `moreForms: []`) | |
| en | adj | irregular comparatives only: `Forms`; `["","form"]`; rows `positive`, `comparative`, `superlative` (regular adjectives: `forms: null`, `moreForms: []`) | |

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
`words[].reading`. For **Overhear Originals** (`originals/`), **all five**
non-Latin scripts (`ja`, `zh`, `ko`, `ar`, `hi`) require 100% `words[].span` and
`words[].reading` coverage on every spoken word, following one fixed standard
per language:
- **Japanese (`ja`)**: Katakana kana giving contextual spoken pronunciation,
  including spoken particle readings (`は` -> `ワ`, `へ` -> `エ`, `を` -> `オ`)
  and resolved counters/numbers; romanised downstream via Modified Hepburn.
- **Mandarin (`zh`)**: Contextual Hanyu Pinyin with tone marks (`zǎo shang`),
  including `一`/`不` tone sandhi and resolved spoken numbers.
- **Korean (`ko`)**: Revised Romanization of Korean (RR, Ministry of Culture
  standard, lowercase ASCII letters) reflecting spoken liaison and consonant
  assimilation (`annyeonghaseyo`, `sinipsawonisijyo`).
- **Arabic (`ar`)**: Standardized spoken Levantine/Jordanian ASCII romanisation
  (`a-z`, `'`, `-`; long vowels `aa, ii, uu`, `'` for hamza/ʿayn, sun-letter
  assimilation `il-kheir`, `ish-shams`), matching `mms-uroman` alignment.
- **Hindi (`hi`)**: Learner-friendly ISO-15919 / IAST-based spoken romanisation
  with vowel length explicitly marked (`a` vs `ā`, `i` vs `ī`, `u` vs `ū`,
  `e`/`ē`, `o`/`ō`; retroflexes `ṭ, ḍ, ṇ, ṛ`; nasals `ṅ, ñ, ṁ`/`n` or nasalised
  vowels `ã, ĩ, ū̃`; schwa-deletion reflecting natural spoken Hindi, e.g.
  `namaste` / `kamarā` or `kamrā`, `ṭhīk`, `āṅgan`, `śukriyā`), matching
  `mms-uroman` (`lcode="hin"`).

Japanese, Mandarin, Korean, Arabic and Hindi `stress` values remain null: do not invent
stress or pitch-accent descriptions. `reading` is alignment and learner reading
guidance and does not replace the written text or establish audio quality by itself.

The renderer must reject unresolved native alignment, partial coverage or
ownership that crosses independently selectable words. Missing words cannot be
published using interpolated acoustic boundaries. Source-span correctness and
actual acoustic boundary quality are separate checks.
