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
import re
import unicodedata
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


def surface_key(text, lang):
    text = unicodedata.normalize('NFC', text).lower().replace('’', "'").replace('ʼ', "'")
    if lang == 'ru':
        text = text.replace('\u0301', '').replace('ё', 'е')
    if lang == 'fr' and "'" in text:
        prefix, rest = text.split("'", 1)
        if prefix in {'c', 'd', 'j', 'l', 'm', 'n', 'qu', 's', 't', 'jusqu', 'lorsqu', 'puisqu', 'quoiqu'} and rest:
            text = rest
    return text


def season_of(scene_id):
    match = re.match(r'^(.+)-s(\d+)e\d+-scene-\d+$', scene_id)
    return f'{match[1]}/s{int(match[2]):02d}' if match else None


def completeness(report, season=None):
    if season:
        rows = [r['seasons'][season] for r in report.values() if season in r['seasons']]
        if not rows:
            raise ValueError(f'Season not found in published scope: {season}')
    else:
        rows = list(report.values()) + [s for r in report.values() for s in r['seasons'].values()]
    return all(not r['missing'] and not r.get('unresolved') for r in rows)


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
        season_words = collections.defaultdict(set)
        unresolved = collections.defaultdict(set)
        scene_counts = collections.Counter()
        article_counts = collections.Counter()
        aliases = collections.defaultdict(set)
        for key, entry in entries.items():
            for form in [key, *entry.get('surface', [])]:
                aliases[surface_key(form, pair['learn'])].add(key)

        def note_word(season, word):
            candidates = aliases.get(surface_key(word, pair['learn']), set())
            if len(candidates) == 1:
                season_words[season].update(candidates)
            elif any(ch.isalpha() for ch in word):
                unresolved[season].add(word)

        for scene_file in sorted((out / f'pairs/{pair_id}/scenes').glob('*.json')):
            scene = json.loads(scene_file.read_text())
            if not scene.get('published') or not scene.get('content'):
                continue
            season = season_of(scene['id'])
            if season is None:
                raise ValueError(f"Cannot identify season of published scene: {scene['id']}")
            scene_counts[season] += 1
            assembled = blob_document(out, scene['content'])
            for line in assembled['transcript']['lines']:
                if line['lang'] == pair['learn']:
                    occurrences.update((w.get('lex') or w.get('lemma') or '').lower() for w in line['words'])
                    for word in line['words']:
                        key = (word.get('lex') or word.get('lemma') or '').lower()
                        if key in entries:
                            season_words[season].add(key)
                        else:
                            note_word(season, word['t'])
            for field in ['vocab', 'conjugations']:
                for vocab in assembled.get('notes', {}).get(field, []):
                    key = vocab.get('lex')
                    if key in entries:
                        season_words[season].add(key)
                    elif key:
                        unresolved[season].add(key)
        # Only articles present in the serving manifest enter this audit. Source
        # example references retain the season even before its audio is available.
        for article_id in manifest.get('learn', {}):
            path = content / f'learn/{pair_id}/{article_id}.json'
            if not path.exists():
                raise ValueError(f'Published article has no authored source: {article_id}')
            article = json.loads(path.read_text())
            seasons = {s for ref in article.get('examples', []) if (s := season_of(ref['sceneId']))}
            body = article['body'].get(pair['from'], '')
            if pair['learn'] == 'ru':
                words = re.findall(r'[А-Яа-яЁё]+(?:[-\u0301][А-Яа-яЁё]+)*', body)
            else:
                runs = re.findall(r'(?<!\*)\*([^*]+)\*(?!\*)', body)
                words = [w for run in runs for w in re.findall(r"[^\W_]+(?:[-'’][^\W_]+)*", run)]
            for season in seasons:
                article_counts[season] += 1
                for word in words:
                    note_word(season, word)
        missing = [dict(lemma=key, gloss=entries[key]['gloss'], occurrences=occurrences[key])
                   for key in sorted(entries, key=lambda key: (-occurrences[key], key))
                   if not covered(histories.get(key, {}))]
        result[pair_id] = dict(words=len(entries), covered=len(entries) - len(missing),
                               missing=len(missing), queue=missing,
                               outsideDictionary=sorted(set(histories) - set(entries)), seasons={})
        for season in sorted(set(season_words) | set(unresolved)):
            words = season_words[season]
            gaps = sorted(k for k in words if not covered(histories.get(k, {})))
            result[pair_id]['seasons'][season] = dict(audioScenes=scene_counts[season], learningNotes=article_counts[season],
                words=len(words), covered=len(words) - len(gaps),
                missing=len(gaps), queue=gaps, unresolved=sorted(unresolved[season]))
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
    lines += ['## Every published season', '',
              '| Pair | Season | Audio scenes | Learning notes | Resolved headwords | Histories | Missing | Unresolved forms |',
              '| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |']
    for pair, row in report.items():
        for season, scope in row['seasons'].items():
            lines.append(f"| {pair} | {season} | {scope['audioScenes']} | {scope['learningNotes']} | {scope['words']} | {scope['covered']} | {scope['missing']} | {len(scope['unresolved'])} |")
    lines += ['', 'The season audit includes spoken words, episode vocabulary and published learning-note target text. '
              'A row with learning notes and zero audio scenes does not mean episode audio is published. '
              'Unresolved or ambiguous forms, including teaching fragments that need classification, are reported separately and prevent a completeness pass; '
              'they are not silently omitted. Unpublished draft episodes do not enter the report.', '']
    for pair, row in report.items():
        lines += [f'## Next words: {pair}', '', ', '.join(w['lemma'] for w in row['queue'][:20]), '']
    lines += ['Regenerate from a verified serving build:', '', '```sh',
              'python3 tools/origin_coverage.py --serving-out /path/to/verified/out '
              '--markdown word-origins/COVERAGE.md --json /path/to/review-queue.json', '```', '']
    lines += ['Before publishing a new or expanded season, require a complete audited candidate:', '', '```sh',
              'python3 tools/origin_coverage.py --serving-out /path/to/verified/candidate '
              '--season dix-pour-cent/s01 --require-complete', '```', '',
              'Omit `--season` to require complete coverage of every served dictionary and season. '
              'The command exits unsuccessfully while any requested scope has gaps.', '']
    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--serving-out', required=True, type=Path)
    parser.add_argument('--content-dir', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--json', type=Path)
    parser.add_argument('--markdown', type=Path)
    parser.add_argument('--season', help='Season to check, e.g. kukhnya/s01; default: every published scope')
    parser.add_argument('--require-complete', action='store_true', help='Exit unsuccessfully if requested coverage has gaps')
    args = parser.parse_args()
    report = inventory(args.serving_out, args.content_dir)
    if args.json:
        args.json.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    if args.markdown:
        args.markdown.write_text(markdown(report))
    for pair, row in report.items():
        print(f"{pair}: {row['covered']}/{row['words']} sourced histories; {row['missing']} still to review")
        for season, scope in row['seasons'].items():
            print(f"  {season}: {scope['missing']} histories missing; {len(scope['unresolved'])} unresolved forms")
    try:
        complete = completeness(report, args.season)
    except ValueError as error:
        parser.error(str(error))
    if args.require_complete and not complete:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
