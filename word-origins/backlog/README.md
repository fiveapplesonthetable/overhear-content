# Word-history backlog

Every word the app serves that still has no sourced history, one queue per tier:

| file | tier | built from |
|---|---|---|
| `originals.json`, `originals.md` | Overhear Originals (public app) | the public serving build and the content checkout it was published from |
| `tv-adaptations.json`, `tv-adaptations.md` | TV adaptations (private tier) | the private serving build and the content checkout it was published from |

In each JSON file, `<pair>.queue` lists the missing words with their gloss and how often they occur, most frequent first;
`<pair>.seasons.<show>/sNN.queue` gives the same per season. The `.md` files summarise the counts.

How to work it:

* Take words from the top of the queue: Originals before TV adaptations, `ru-en` first, then the other pairs.
* Write each history in `word-origins/<pair>.json` by the rules in `word-origins/README.md`: checked against a specific
  authoritative entry, linked, uncertainty stated. A word that already has a sourced entry in the file (written after the
  queue was made) is done; skip it.
* Run `python3 -I tools/validate.py . --metadata-only` and commit. Histories reach the app at the next publish of that pair;
  no audio or APK is needed.

The queue is a snapshot. The owner refreshes it from the live serving builds after publishes with
`tools/origin_coverage.py`. Never hand-edit it; it is only a work list, and `word-origins/<pair>.json` is the record.
