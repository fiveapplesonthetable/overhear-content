"""List the served dictionary words still needing an editorially reviewed history.

Reads only the blobs referenced by the current serving catalogue. This is an
inventory, not evidence that a citation supports a claim; that needs human review.
No network requests or audio generation are involved.
"""
import argparse
import collections
import gzip
import hashlib
import json
from pathlib import Path
from urllib.parse import unquote, urlsplit


def blob_document(out, blob):
    name = unquote(urlsplit(blob['url']).path.split('/o/', 1)[1])
    root = (out / 'gcs').resolve()
    path = (root / name).resolve()
    if not path.is_relative_to(root):
        raise ValueError('Blob path escapes serving directory')
    data = path.read_bytes()
    if hashlib.sha256(data).hexdigest() != blob['sha256']:
        raise ValueError(f'Blob digest mismatch: {name}')
    return json.loads(gzip.decompress(data) if data.startswith(b'\x1f\x8b') else data)


def covered(entry):
    return bool(entry.get('etymology', '').strip() and entry.get('sources') and all(
        s.get('title', '').strip() and s.get('url', '').startswith('https://') for s in entry['sources']))


def inventory(out, content):
    meta = json.loads((out / 'meta/app.json').read_text())
    result = {}
    for pair in meta['pairs']:
        if not pair['published']:
            continue
        pair_id = pair['id']
        doc = json.loads((out / f'pairs/{pair_id}/pair.json').read_text())
        if not doc['index']['manifest']:
            continue
        manifest = blob_document(out, doc['index']['manifest'])
        entries = {}
        for shard in manifest.get('lexicon', {}).get('shards', {}).values():
            entries.update(blob_document(out, shard['blob'])['entries'])
        path = content / f'word-origins/{pair_id}.json'
        histories = json.loads(path.read_text())['entries'] if path.exists() else {}
        occurrences = collections.Counter()
        for scene_file in sorted((out / f'pairs/{pair_id}/scenes').glob('*.json')):
            scene = json.loads(scene_file.read_text())
            if not scene.get('published') or not scene.get('content'):
                continue
            for line in blob_document(out, scene['content'])['transcript']['lines']:
                if line['lang'] == pair['learn']:
                    occurrences.update((w.get('lex') or w.get('lemma') or '').lower() for w in line['words'])
        missing = [dict(lemma=key, gloss=entries[key]['gloss'], occurrences=occurrences[key])
                   for key in sorted(entries, key=lambda key: (-occurrences[key], key))
                   if not covered(histories.get(key, {}))]
        result[pair_id] = dict(words=len(entries), covered=len(entries) - len(missing),
                               missing=len(missing), queue=missing,
                               outsideDictionary=sorted(set(histories) - set(entries)))
    return result


def markdown(report):
    lines = ['# Word-history coverage', '',
             'Target: a sourced, reviewed Origin entry for every served dictionary word. '
             'An origin described as unknown or disputed still needs a specific supporting source. '
             'A source link alone does not verify the accompanying claim.', '',
             '| Pair | Dictionary words | Sourced histories | Still to review |',
             '| --- | ---: | ---: | ---: |']
    for pair, row in report.items():
        lines.append(f"| {pair} | {row['words']} | {row['covered']} | {row['missing']} |")
    lines += ['', 'Counts describe the serving catalogue used for this report; they are not a claim of full coverage. '
              'The queue includes grammar words, names and phrases rather than silently excluding them. '
              'Refresh it as episodes or dictionary entries are added.', '']
    for pair, row in report.items():
        lines += [f'## Next words: {pair}', '', ', '.join(w['lemma'] for w in row['queue'][:20]), '']
    lines += ['Regenerate from a verified serving build:', '', '```sh',
              'python3 tools/origin_coverage.py --serving-out /path/to/verified/out '
              '--markdown word-origins/COVERAGE.md --json /path/to/review-queue.json', '```', '']
    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--serving-out', required=True, type=Path)
    parser.add_argument('--content-dir', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--json', type=Path)
    parser.add_argument('--markdown', type=Path)
    args = parser.parse_args()
    report = inventory(args.serving_out, args.content_dir)
    if args.json:
        args.json.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    if args.markdown:
        args.markdown.write_text(markdown(report))
    for pair, row in report.items():
        print(f"{pair}: {row['covered']}/{row['words']} sourced histories; {row['missing']} still to review")


if __name__ == '__main__':
    main()
