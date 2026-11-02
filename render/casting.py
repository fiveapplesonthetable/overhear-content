"""Character -> voice casting, persisted in git (casting/<show>.json), append-only.

Source of truth for who exists: overhear-content out/<show>/cast.json (key, ru, en[], gender m|f). The renderer casts
by gender from the pool in voices.json:
  * the narrator is always the female English voice in the casting file ("sky");
  * a character gets one voice for the whole show, of its own gender, and keeps it forever (an existing entry is never
    rewritten; new characters are appended);
  * characters who share scenes get different voices when the pool allows: each new character takes the voice that
    collides least (by co-occurrence counts) with the characters already holding it, then the least used, then pool order;
  * `designedFor` in voices.json pins a voice to the character it was designed for (voice-lab) when that voice is free.
To change a voice: edit casting/<show>.json by hand (and commit); scenes using it re-render by themselves.
"""
import json
from pathlib import Path

import config

import os
DIR = Path(os.environ.get("OVERHEAR_CASTING_DIR", config.HERE / "casting"))


def path(show):
    return DIR / f"{show}.json"


def load(show):
    p = path(show)
    return json.loads(p.read_text("utf-8")) if p.exists() else None


def cooccurrence(scenes):
    count, co = {}, {}
    for sc in scenes:
        roles = sorted({g["v"] for g in sc.script["segments"] if g["v"] != "narrator"})
        for r in roles:
            count[r] = count.get(r, 0) + 1
        for i, a in enumerate(roles):
            for b in roles[i + 1:]:
                co[(a, b)] = co.get((a, b), 0) + 1
    return count, co


def extend(show, cast, scenes, voices, lang):
    """Return (casting_doc, [new keys]). Does not write."""
    doc = load(show) or {"schemaVersion": 1, "show": show, "narrator": "sky", "characters": {}}
    chars = doc["characters"]
    count, co = cooccurrence(scenes)
    new = []
    todo = sorted((k for k in count if k in cast and k not in chars), key=lambda k: (-count[k], k))
    for k in todo:
        g = cast[k]["gender"]
        pool = [v for v, r in voices.refs.items() if r["lang"] == lang and r.get("gender") == g and v != doc["narrator"]]
        if not pool:
            continue
        used = {}
        for ck, cv in chars.items():
            used.setdefault(cv["voice"], []).append(ck)
        designed = [v for v in pool if voices.refs[v].get("designedFor") == k and v not in used]
        if designed:
            pick = designed[0]
        else:
            def score(v):
                clash = sum(co.get(tuple(sorted((k, o))), 0) for o in used.get(v, []))
                return (clash, len(used.get(v, [])), pool.index(v))
            pick = min(pool, key=score)
        chars[k] = {"voice": pick, "gender": g, "ru": cast[k].get("ru")}
        new.append(k)
    doc["characters"] = dict(sorted(chars.items()))
    return doc, new


def save(doc):
    DIR.mkdir(exist_ok=True)
    p = path(doc["show"])
    tmp = p.with_suffix(".tmp")
    tmp.write_text(json.dumps(doc, ensure_ascii=False, indent=1, sort_keys=True) + "\n", "utf-8")
    tmp.replace(p)


def ensure(scenes, casts, voices, log=print):
    """Extend and save the casting file of every show that has a cast.json. Idempotent."""
    by_show = {}
    for sc in scenes:
        by_show.setdefault(sc.show, []).append(sc)
    for show, scs in by_show.items():
        cast = casts.get(show)
        if not cast:
            continue
        doc, new = extend(show, cast, scs, voices, scs[0].lang)
        if new or not path(show).exists():
            save(doc)
            log(f"casting/{show}.json: +{len(new)} character(s): " + ", ".join(f"{k}->{doc['characters'][k]['voice']}" for k in new[:12]) + (" ..." if len(new) > 12 else ""))
