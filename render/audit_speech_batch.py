"""Audit every rendered sentence, decoding audio once and batching unprompted ASR.

Run under gpurun with the faster-whisper venv. Exact normalized text mismatches
remain review items; this report never approves a scene by a loose CER threshold.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import time
import unicodedata


def normalized(text, lang=None):
    if lang and re.search(r'\d', text):
        from num2words import num2words
        if lang == 'fr':
            text = re.sub(r'\b(\d+)\s*h\b', lambda m: num2words(int(m[1]), lang='fr') + ' heures', text)
        text = re.sub(r'\b(?:\d{1,3}(?:,\d{3})+|\d+)\b', lambda m: num2words(int(m[0].replace(',', '')), lang=lang), text)
    text = unicodedata.normalize('NFC', text.lower().replace('’', "'"))
    # Preserve phonemic native spelling: año/ano, schön/schon, が/か and أ/ا
    # must never become a silent exact-match waiver. Legacy RU/FR/EN keeps its
    # established comparison; new-language orthographic variants need review.
    if lang == 'ar':
        text = re.sub(r'[\u064b-\u0652\u0670]', '', text)
    elif lang not in {'es', 'de', 'it', 'ja', 'zh', 'ko', 'pt'}:
        text = ''.join(c for c in unicodedata.normalize('NFD', text) if not unicodedata.combining(c))
    return re.sub(r'\s+', ' ', re.sub(r'[^\w\s]', ' ', text)).strip()


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def inspect(directory, content):
    meta = json.loads((directory / 'meta.json').read_text())
    spans = json.loads((directory / 'spans.json').read_text())
    timing = json.loads((directory / 'timing.json').read_text())
    errors = []
    for name, key in [('audio.mp3', 'audioSha256'), ('spans.json', 'spansSha256'), ('timing.json', 'timingSha256')]:
        if digest(directory / name) != meta[key]:
            errors.append(f'{name} hash mismatch')
    sid = directory.name
    match = re.fullmatch(r'(.+)-(s\d\de\d\d)-(scene-\d\d)', sid)
    script = content / 'out' / match[1] / match[2] / (match[3] + '.json')
    notes = script.with_suffix('.notes.json')
    if hashlib.sha256(script.read_bytes() + notes.read_bytes()).hexdigest() != meta['contentHash']:
        errors.append('content hash mismatch')
    previous = 0
    for seg in spans['segs']:
        if not previous <= seg['start'] < seg['end'] <= meta['durationSec'] + .001:
            errors.append(f"invalid/overlapping segment {seg['seg']}")
        previous = seg['end']
        prior = seg['start']
        for sentence in seg['sentences']:
            if not prior <= sentence['start'] < sentence['end'] <= seg['end'] + .001:
                errors.append(f"invalid/overlapping sentence {seg['seg']}:{sentence['i']}")
            prior = sentence['end']
        prior = seg['start']
        tokens = timing.get(str(seg['seg']), [])
        if not tokens:
            errors.append(f"missing tokens {seg['seg']}")
        for token in tokens:
            # MMS's final frame may extend slightly into intentional silence.
            # It must still end before the next segment and decoded audio end.
            token_limit = min(seg.get('nextStart', meta['durationSec']), meta['durationSec'])
            if not prior <= token['s'] < token['e'] <= token_limit + .001:
                errors.append(f"invalid/overlapping token {seg['seg']}:{token['t']}")
            prior = token['e']
    return meta, spans, errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--store', type=Path, required=True)
    parser.add_argument('--content', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--batch-size', type=int, default=4)
    parser.add_argument('scenes', nargs='+')
    args = parser.parse_args()
    import numpy as np
    import jiwer
    from faster_whisper import WhisperModel, BatchedInferencePipeline
    start = time.monotonic()
    model = WhisperModel('large-v3-turbo', device='cuda', compute_type='float16')
    pipeline = BatchedInferencePipeline(model=model)
    reports = []
    for sid in args.scenes:
        directory = args.store / sid
        meta, spans, errors = inspect(directory, args.content)
        process = subprocess.run(['ffmpeg', '-v', 'error', '-i', str(directory / 'audio.mp3'), '-ac', '1', '-ar', '16000', '-f', 'f32le', '-'], capture_output=True, check=True)
        audio = np.frombuffer(process.stdout, dtype=np.float32)
        if abs(len(audio) / 16000 - meta['durationSec']) > .05:
            errors.append('decoded duration mismatch')
        rows = []
        for seg in spans['segs']:
            for sent in seg['sentences']:
                rows.append(dict(scene=sid, seg=seg['seg'], sentence=sent['i'], role=seg['v'], voice=seg['voice'], lang=seg['lang'], ref=sent['text'], start=sent['start'], end=sent['end'], hyp=''))
        for lang in sorted({row['lang'] for row in rows}):
            selected = [row for row in rows if row['lang'] == lang]
            clips = [{'start': max(0, row['start'] - .05), 'end': min(len(audio) / 16000, row['end'] + .05)} for row in selected]
            # Explicit clips avoid VAD dropping brief words. Never silently truncate.
            if any(clip['end'] - clip['start'] > 30 for clip in clips):
                raise ValueError(f'{sid}: sentence exceeds Whisper 30-second chunk; use individual ASR')
            seeks = {int(int(clip['start'] * 16000) / 16000 * model.frames_per_second): row for clip, row in zip(clips, selected)}
            if len(seeks) != len(selected):
                raise ValueError('ambiguous clip starts')
            segments, _ = pipeline.transcribe(audio, language=lang, beam_size=5, condition_on_previous_text=False, initial_prompt=None, hotwords=None, vad_filter=False, clip_timestamps=clips, batch_size=args.batch_size, without_timestamps=True)
            for part in segments:
                if part.seek not in seeks:
                    raise ValueError(f'unmatched ASR clip {part.seek}')
                row = seeks[part.seek]
                row['hyp'] = (row['hyp'] + ' ' + part.text).strip()
        for row in rows:
            ref, hyp = normalized(row['ref'], row['lang']), normalized(row['hyp'], row['lang'])
            row['normalizedRef'], row['normalizedHyp'] = ref, hyp
            row['cer'] = round(jiwer.cer(ref, hyp), 5) if hyp else 1.0
            row['needsReview'] = ref != hyp
        # Unprompted first-story context helps review short homophones/names. It
        # supplements each sentence's audit and never silently waives a mismatch.
        story = []
        for seg in spans['segs']:
            if seg['lang'] != 'en':
                story.append(seg)
            elif story:
                break
        context = ''
        if story:
            clip = audio[max(0, int((story[0]['start'] - .05) * 16000)):int((story[-1]['end'] + .05) * 16000)]
            parts, _ = model.transcribe(clip, language=story[0]['lang'], beam_size=5, condition_on_previous_text=True, initial_prompt=None, hotwords=None, vad_filter=False)
            context = ' '.join(part.text for part in parts).strip()
        report = dict(scene=sid, audioSha256=meta['audioSha256'], contentHash=meta['contentHash'], errors=errors, rows=rows, firstStoryHyp=context, sentenceCount=len(rows), reviewCount=sum(r['needsReview'] for r in rows))
        reports.append(report)
        args.out.write_text(json.dumps(dict(method='large-v3-turbo, every sentence, beam5, no prompt/hotwords/VAD', reports=reports, elapsedSec=round(time.monotonic()-start, 2)), ensure_ascii=False, indent=2) + '\n')
        print(json.dumps({key: report[key] for key in ['scene', 'errors', 'sentenceCount', 'reviewCount']}) , flush=True)


if __name__ == '__main__':
    main()
