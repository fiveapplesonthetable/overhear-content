#!/usr/bin/env python3
"""Render a bounded ru-en pilot with Google TTS; never uploads or changes default engines.

Uses the current gcloud identity, without creating or persisting an API key.
Run synth with system Python; finish/qa need the renderer's torch/ASR environment.
Raw takes are cached by the complete Google request. Repeated story lines reuse takes.
"""
import argparse
import base64
import hashlib
import io
import json
import pathlib
import re
import subprocess
import sys
import urllib.error
import urllib.request
import wave
from datetime import datetime, timezone

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'render'))
MODEL = 'gemini-3.8-flash-tts'
SR = 24000


def digest(b):
    return hashlib.sha256(b).hexdigest()


def save(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, sort_keys=True, indent=1) + '\n')


def payload(seg, casting):
    spec = casting[seg['v']]
    return {'contents': [{'role': 'user', 'parts': [{'text': seg['t'],
            'speechMetadata': {'style': spec['style']}}]}],
            'generationConfig': {'responseModalities': ['AUDIO'],
            'speechConfig': {'voiceConfig': {'voice': spec['voice']}}}}


def cache_key(seg, casting):
    return digest(json.dumps([MODEL, payload(seg, casting)], ensure_ascii=False, sort_keys=True).encode())


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('stage', choices=['synth', 'finish', 'qa'])
    ap.add_argument('--script', required=True, type=pathlib.Path)
    ap.add_argument('--casting', required=True, type=pathlib.Path)
    ap.add_argument('--store', required=True, type=pathlib.Path)
    ap.add_argument('--project', default='cyclevpn')
    ap.add_argument('--device', default='cuda')
    args = ap.parse_args()
    script = json.loads(args.script.read_text())
    if script['pair'] != 'ru-en':
        ap.error('This pilot supports ru-en only; other languages need a reviewed configuration.')
    casting = json.loads(args.casting.read_text())
    for seg in script['segments']:
        if seg['v'] not in casting:
            ap.error('Missing voice casting for ' + seg['v'])
    cache = args.store / 'google-takes'
    cache.mkdir(parents=True, exist_ok=True)
    takes = {cache_key(seg, casting): seg for seg in script['segments']}
    if args.stage == 'synth':
        endpoint = f'https://aiplatform.googleapis.com/v1/projects/{args.project}/locations/global/publishers/google/models/{MODEL}:generateContent'
        for key, seg in takes.items():
            target = cache / (key + '.wav')
            if target.exists():
                continue
            token = subprocess.run(['gcloud', 'auth', 'print-access-token'], check=True,
                                   capture_output=True, text=True).stdout.strip()
            request = urllib.request.Request(endpoint, data=json.dumps(payload(seg, casting)).encode(),
                      headers={'Authorization': 'Bearer ' + token, 'Content-Type': 'application/json'})
            try:
                with urllib.request.urlopen(request, timeout=180) as response:
                    result = json.load(response)
            except urllib.error.HTTPError as exc:
                error = json.loads(exc.read()).get('error', {})
                raise RuntimeError(f'Google TTS HTTP {exc.code}: {error.get("message", "request failed")}') from None
            parts = [part for c in result.get('candidates', []) for part in c.get('content', {}).get('parts', [])
                     if 'inlineData' in part]
            if len(parts) != 1 or parts[0]['inlineData']['mimeType'] != 'audio/wav':
                raise RuntimeError('Expected one WAV response; no audio cached.')
            raw = base64.b64decode(parts[0]['inlineData']['data'], validate=True)
            with wave.open(io.BytesIO(raw)) as w:
                if (w.getframerate(), w.getnchannels(), w.getsampwidth()) != (SR, 1, 2):
                    raise RuntimeError('Unexpected PCM format')
                duration = w.getnframes() / SR
                if not 0.1 < duration < 180:
                    raise RuntimeError('Implausible clip length')
            temp = target.with_suffix('.tmp')
            temp.write_bytes(raw)
            temp.replace(target)
            save(cache / (key + '.json'), {'model': MODEL, 'request': payload(seg, casting),
                 'audioSha256': digest(raw), 'durationSec': duration, 'usage': result.get('usageMetadata')})
            print(f'{seg["v"]}: {duration:.2f}s | {seg["t"][:85]}', flush=True)
        return

    import numpy as np
    import soundfile as sf
    import audio
    prepared = {}
    cfg = dict(sampleRate=SR, segLufs=-20, programLufs=-16, mp3Kbps=96,
               fadeMs=15, trimDb=-50, edgeMs=20, warmEq=False)
    for key in takes:
        raw = (cache / (key + '.wav')).read_bytes()
        metadata = json.loads((cache / (key + '.json')).read_text())
        if digest(raw) != metadata['audioSha256']:
            raise RuntimeError('Cached take integrity check failed: ' + key)
        wav, sr = sf.read(io.BytesIO(raw), dtype='float32')
        if sr != SR:
            raise RuntimeError('Wrong sample rate')
        prepared[key] = audio.prepare_sentence(wav, SR, cfg)

    output = args.store / script['id']
    output.mkdir(parents=True, exist_ok=True)
    if args.stage == 'qa':
        from faster_whisper import WhisperModel
        import jiwer
        model = WhisperModel('large-v3-turbo', device=args.device,
                             compute_type='float16' if args.device == 'cuda' else 'int8')
        norm = lambda t: ' '.join(re.findall(r'\w+', t.lower().replace('ё', 'е')))
        checks = []
        # Decode the finished MP3, not just the pre-encoding takes. Check each
        # distinct segment once, with no reference transcript or hotword prompt.
        spans = json.loads((output / 'spans.json').read_text())['segs']
        decoded = subprocess.run(['ffmpeg', '-v', 'error', '-i', str(output/'audio.mp3'),
                      '-ar', '16000', '-ac', '1', '-f', 'f32le', '-'], capture_output=True, check=True).stdout
        samples = np.frombuffer(decoded, dtype='<f4')
        done = set()
        for seg, span in zip(script['segments'], spans):
            key = cache_key(seg, casting)
            if key in done:
                continue
            done.add(key)
            clip = samples[int(span['start']*16000):int(span['end']*16000)]
            chunks, _ = model.transcribe(clip, language='en' if seg['v']=='narrator' else 'ru',
                  beam_size=5, condition_on_previous_text=False, vad_filter=False)
            heard = ' '.join(c.text.strip() for c in chunks)
            cer = jiwer.cer(norm(seg['t']), norm(heard))
            checks.append(dict(seg=span['seg'], role=seg['v'], expected=seg['t'], heard=heard, cer=cer))
            print(f'CER {cer:.3f} | {heard}', flush=True)
        save(output/'asr-review.json', {'model':'faster-whisper-large-v3-turbo',
             'source':'final audio.mp3, distinct segments', 'checks':checks,
             'flagged':[x['seg'] for x in checks if x['cer'] > 0.10],
             'humanListening':False})
        if any(x['cer'] > 0.10 for x in checks):
            raise SystemExit('ASR discrepancies need review before publishing.')
        return

    import align
    from textprep import split_sentences
    import torch
    torch.set_num_threads(4)
    aligner = align.Aligner(args.device)
    word_cache = {}
    for key, seg in takes.items():
        wav = prepared[key]
        chars, x16 = aligner.char_times(wav, SR, seg['t'], 'en' if seg['v']=='narrator' else 'ru')
        matches = [m for m in re.finditer(r'\S+', seg['t']) if any(c.isalnum() for c in m[0])]
        env, hop = align.envelope(x16)
        times = align.words_from_chars(chars, [m.span() for m in matches], env, hop)
        for w, m in zip(times, matches):
            w['t'] = m[0]
            w['e'] = min(w['e'], len(wav)/SR)
        if any(not w['ok'] or w['e'] <= w['s'] for w in times):
            raise RuntimeError('Word alignment needs review: ' + seg['t'])
        word_cache[key] = (times, matches)
        print('Aligned:', seg['t'][:85], flush=True)
    lines = [[(prepared[cache_key(seg, casting)], seg['gap'])] for seg in script['segments']]
    signal, layout = audio.assemble(lines, SR, cfg)
    signal, gain, before = audio.master(signal, SR, cfg)
    audio.encode_mp3(signal, SR, output/'audio.mp3')
    duration = audio.mp3_duration(output/'audio.mp3')
    if abs(duration-len(signal)/SR)>0.05:
        raise RuntimeError('Encoded audio duration mismatch')
    spans, timing = [], {}
    for i, (seg, (start, end, next_start, _)) in enumerate(zip(script['segments'], layout)):
        local, matches = word_cache[cache_key(seg, casting)]
        timing[str(i)] = [{**w, 's':w['s']+start, 'e':w['e']+start} for w in local]
        sentences = []
        for j, (a,b,text) in enumerate(split_sentences(seg['t'])):
            words = [w for w,m in zip(timing[str(i)], matches) if a <= m.start() < b]
            if not words:
                raise RuntimeError('Sentence has no aligned words')
            sentences.append(dict(i=j,start=words[0]['s'],end=words[-1]['e'],text=text,engine=MODEL))
        spans.append(dict(seg=i,start=start,end=end,nextStart=next_start,v=seg['v'],
                     voice=casting[seg['v']]['voice'],lang='en' if seg['v']=='narrator' else 'ru',sentences=sentences))
    save(output/'spans.json',dict(version=1,sceneId=script['id'],sampleRate=SR,durationSec=duration,segs=spans))
    save(output/'timing.json',timing)
    notes = args.script.with_suffix('.notes.json')
    content_hash = digest(args.script.read_bytes()+notes.read_bytes())
    commit = subprocess.run(['git','-C',str(ROOT),'rev-parse','HEAD'],capture_output=True,text=True,check=True).stdout.strip()
    save(output/'meta.json',dict(sceneId=script['id'],contentHash=content_hash,contentCommit=commit,
         tts=dict(model=MODEL,lora=False,stressPolicy='plain-text',gen={'provider':'Google Agent Platform'}),
         voices={k:{'voice':v['voice'],'refVersion':digest(json.dumps(v,sort_keys=True).encode())[:8]} for k,v in casting.items()},
         voicesVersion=digest(args.casting.read_bytes())[:8],align='mms_fa/a1',pipelineVersion='overhear-google-pilot/1',
         renderVersion='google-pilot-1',renderKey=digest(json.dumps([content_hash,MODEL,casting,cfg,sorted(takes)],sort_keys=True).encode()),
         renderedAt=datetime.now(timezone.utc).isoformat(),durationSec=duration,sampleRate=SR,bitrateKbps=96,
         audioSha256=digest((output/'audio.mp3').read_bytes()),audioBytes=(output/'audio.mp3').stat().st_size,
         spansSha256=digest((output/'spans.json').read_bytes()),timingSha256=digest((output/'timing.json').read_bytes())))
    save(output/'report.json',dict(version=1,sceneId=script['id'],audio=dict(gainDb=gain,mp3Seconds=duration,
         programLufsBefore=before,seconds=len(signal)/SR),stress={'checked':False},retake={'sentences':0,'takes':0},
         timing={'notOk':0,'tokens':sum(map(len,timing.values()))},tts={'segments':len(lines),'unique':len(takes)},
         warnings=['Pilot: automatic transcription review is separate; human voice-quality review pending.']))
    print(f'Rendered {duration:.2f}s: {output}',flush=True)


if __name__ == '__main__':
    main()
