#!/usr/bin/env python3
"""Ear-check page: index.html + one mp3 per scene (word highlight from timing.json, flag-rate summary, voices table).

  python3 -I listen_page.py OUTDIR SCENE_ID [...] [--cer cer.json] [--bench bench.json]
"""
import html, json, shutil, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import config, content
from voices import Voices
from content import scene_path


def main():
    args = sys.argv[1:]
    out = Path(args.pop(0))
    opts = {}
    for k in ("--cer", "--bench"):
        if k in args:
            i = args.index(k); opts[k] = args[i + 1]; del args[i:i + 2]
    out.mkdir(parents=True, exist_ok=True)
    voices = Voices()
    store = Path(config.STORE)
    scenes = []
    for sid in args:
        sc = content.load_scene(scene_path(config.CONTENT_DIR, sid))
        d = store / sid
        meta, spans, timing, report = (json.loads((d / f).read_text()) for f in ("meta.json", "spans.json", "timing.json", "report.json"))
        shutil.copyfile(d / "audio.mp3", out / f"{sid}.mp3")
        notes = {l["seg"]: l.get("trans", "") for l in sc.notes.get("lines", [])}
        lines = []
        for seg in spans["segs"]:
            g = sc.script["segments"][seg["seg"]]
            lines.append({"seg": seg["seg"], "role": seg["v"], "label": sc.script.get("labels", {}).get(seg["v"], seg["v"]), "voice": seg["voice"],
                          "start": seg["start"], "end": seg["end"], "text": g["t"], "trans": notes.get(seg["seg"], ""),
                          "words": timing[str(seg["seg"])]})
        st = report["stress"]
        scenes.append({"id": sid, "title": sc.script.get("title", sid), "duration": meta["durationSec"], "lines": lines,
                       "ru": st["russianSentences"], "flaggedInitially": st["sentencesFlaggedInitially"], "stillFlagged": st["stillFlagged"],
                       "unresolved": st["unresolved"], "retakes": report["retake"]["sentences"], "notOk": report["timing"]["notOk"],
                       "tokens": report["timing"]["tokens"], "wall": meta["wall"]["total"], "lufs": report["audio"]["programLufsBefore"],
                       "lora": meta["tts"]["lora"], "policy": meta["tts"]["stressPolicy"], "missing": st["missingMarks"]})
    cer = json.loads(Path(opts["--cer"]).read_text())["summary"] if "--cer" in opts else None
    bench = json.loads(Path(opts["--bench"]).read_text()) if "--bench" in opts else None
    vt = "".join(f"<tr><td><b>{html.escape(k)}</b></td><td>{r['lang']}</td><td>{r['seconds'] if 'seconds' in r else ''}</td><td>{html.escape(r['text'])}</td></tr>" for k, r in voices.refs.items())
    doc = TEMPLATE.replace("__DATA__", json.dumps({"scenes": scenes, "cer": cer, "bench": bench}, ensure_ascii=False)).replace("__VOICES__", vt)
    (out / "index.html").write_text(doc, encoding="utf-8")
    print(out / "index.html")


TEMPLATE = r"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Overhear render check</title>
<style>
:root{--bg:#fff;--fg:#1a1a1a;--mut:#666;--line:#e4e4e4;--acc:#2a5db0;--hl:#ffe9a8;--bad:#b3261e}
@media(prefers-color-scheme:dark){:root{--bg:#161616;--fg:#e8e8e8;--mut:#9a9a9a;--line:#2c2c2c;--acc:#7fa8e8;--hl:#4a3d12;--bad:#f2867f}}
body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.5 system-ui,sans-serif}
main{max-width:760px;margin:0 auto;padding:16px}
h1{font-size:1.3rem}h2{font-size:1.1rem;margin-top:2rem}
.mut{color:var(--mut);font-size:.9rem}table{border-collapse:collapse;width:100%;font-size:.85rem}td,th{border-bottom:1px solid var(--line);padding:4px 6px;text-align:left;vertical-align:top}
audio{width:100%;position:sticky;top:0;background:var(--bg);padding:6px 0;z-index:2}
.line{display:flex;gap:10px;padding:8px 0;border-bottom:1px solid var(--line);cursor:pointer}
.who{flex:0 0 92px;color:var(--mut);font-size:.8rem}.who b{display:block;color:var(--fg)}
.txt{flex:1}.tr{color:var(--mut);font-size:.88rem}
.w.on{background:var(--hl);border-radius:3px}.w.bad{border-bottom:1px dotted var(--bad)}
.line.cur{background:color-mix(in srgb,var(--hl) 35%,transparent)}
.flag{color:var(--bad)}
</style></head><body><main>
<h1>Overhear render check</h1>
<p class="mut">Local Qwen3-TTS-12Hz-1.7B-Base, voices cloned from the old ElevenLabs clips. Tap a line to jump to it; the current word is highlighted from the MMS alignment (dotted underline: a word the aligner could not place).</p>
<div id="summary"></div>
<div id="scenes"></div>
<h2>Voices</h2><table><tr><th>key</th><th>lang</th><th>ref s</th><th>reference transcript</th></tr>__VOICES__</table>
<script>
const D=__DATA__;
const esc=s=>s.replace(/[&<>]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;'}[c]));
let h='';
const tot=D.scenes.reduce((a,s)=>({ru:a.ru+s.ru,f:a.f+s.flaggedInitially,sf:a.sf+s.stillFlagged}),{ru:0,f:0,sf:0});
h+='<h2>Flag-rate summary</h2><table><tr><th>scene</th><th>Russian lines</th><th>flagged first take</th><th>still flagged after retakes</th><th>words not placed</th><th>render s</th></tr>';
D.scenes.forEach(s=>{h+=`<tr><td>${s.id}</td><td>${s.ru}</td><td>${s.flaggedInitially}</td><td class="${s.stillFlagged?'flag':''}">${s.stillFlagged}</td><td>${s.notOk}/${s.tokens}</td><td>${s.wall}</td></tr>`});
h+=`<tr><td><b>all</b></td><td>${tot.ru}</td><td>${tot.f}${tot.ru?` (${(100*tot.f/tot.ru).toFixed(1)}%)`:''}</td><td>${tot.sf}${tot.ru?` (${(100*tot.sf/tot.ru).toFixed(1)}%)`:''}</td><td></td><td></td></tr></table>`;
h+=`<p class="mut">Stress policy: ${D.scenes[0]?.policy}; LoRA: ${JSON.stringify(D.scenes[0]?.lora)}. Flag = the stress checker thinks a risky word was stressed on the wrong vowel (about 84% accurate itself).</p>`;
if(D.cer){h+='<h2>Whisper CER (smoke)</h2><table><tr><th>set</th><th>sentences</th><th>mean</th><th>max</th></tr>'+Object.entries(D.cer).map(([k,v])=>`<tr><td>${k}</td><td>${v.n}</td><td>${v.meanCER}</td><td>${v.maxCER}</td></tr>`).join('')+'</table>'}
if(D.bench){h+='<h2>Throughput</h2><table><tr><th>config</th><th>batch</th><th>audio s</th><th>wall s</th><th>RTF</th><th>peak MiB</th></tr>'+D.bench.results.map(r=>`<tr><td>${r.name}</td><td>${r.batch||''}</td><td>${r.audioSec||''}</td><td>${r.wallSec||''}</td><td>${r.rtf||r.error}</td><td>${r.peakMiB||''}</td></tr>`).join('')+'</table>'}
document.getElementById('summary').innerHTML=h;
const root=document.getElementById('scenes');
D.scenes.forEach((s,si)=>{
 const sec=document.createElement('section');
 sec.innerHTML=`<h2>${esc(s.title)}</h2><div class="mut">${s.id} · ${Math.floor(s.duration/60)}:${String(Math.round(s.duration%60)).padStart(2,'0')} · ${s.ru} Russian lines, ${s.stillFlagged} still flagged</div><audio controls preload="none" src="${s.id}.mp3"></audio>`;
 const a=sec.querySelector('audio');const els=[];
 s.lines.forEach((l,li)=>{
  const d=document.createElement('div');d.className='line';
  const ws=l.words.map((w,wi)=>`<span class="w${w.ok?'':' bad'}" data-s="${w.s}" data-e="${w.e}">${esc(w.t)}</span>`).join(' ');
  d.innerHTML=`<div class="who"><b>${esc(l.label)}</b>${l.voice}</div><div class="txt">${ws}${l.trans?`<div class="tr">${esc(l.trans)}</div>`:''}</div>`;
  d.onclick=()=>{a.currentTime=l.start;a.play()};sec.appendChild(d);els.push([l,d]);
 });
 a.ontimeupdate=()=>{const t=a.currentTime;els.forEach(([l,d])=>{const cur=t>=l.start&&t<l.end+0.4;d.classList.toggle('cur',cur);d.querySelectorAll('.w').forEach(w=>w.classList.toggle('on',cur&&t>=+w.dataset.s&&t<+w.dataset.e+0.05))})};
 a.onplay=()=>document.querySelectorAll('audio').forEach(o=>{if(o!==a)o.pause()});
 root.appendChild(sec);
});
</script></main></body></html>"""

if __name__ == "__main__":
    main()
