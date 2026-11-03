#!/usr/bin/env python3
"""Build the strict 10-language round-robin queue in /dev/shm/overhear-turbo and optionally start turbo_daemon.

Replicates the exact episode-by-episode round-robin order:
  Round 1 (s01e01 across all 10 languages + 2nd RU show):
    pt (porta-dos-fundos) -> ru (kukhnya) -> fr (dix-pour-cent) -> ar (alrawabi-school) ->
    es (paquita-salas) -> de (die-discounter) -> ko (the-producers) -> it (boris) ->
    ja (the-naked-director) -> zh (behind-the-scenes) -> ru (domashniy-arest)
  Round 2 (s01e02 round-robin across validated shows)
  Round 3+ (s01e03+ interleaved round-robin across validated shows)

Usage:
  python3 tools/launch_round_robin.py --reset-done
  OVERHEAR_HOME="$HOME/overhear" python3 tools/launch_round_robin.py --reset-done --exec-master
"""
import argparse
import json
import os
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SHM = Path("/dev/shm/overhear-turbo")

SHOW_SETTINGS = {
    "porta-dos-fundos": "render/settings.pt-qwen-en.json",
    "kukhnya": "render/settings.ru-qwen-en.json",
    "domashniy-arest": "render/settings.ru-qwen-en.json",
    "dix-pour-cent": "render/settings.fr-qwen-en.json",
    "alrawabi-school": "render/settings.ar-chatterbox-en.json",
    "paquita-salas": "render/settings.es-qwen-en.json",
    "die-discounter": "render/settings.de-qwen-en.json",
    "the-producers": "render/settings.ko-qwen-en.json",
    "boris": "render/settings.it-qwen-en.json",
    "the-naked-director": "render/settings.ja-qwen-en.json",
    "behind-the-scenes": "render/settings.zh-qwen-en.json",
}

ROUND_ROBIN_SHOW_ORDER = [
    "porta-dos-fundos",
    "kukhnya",
    "dix-pour-cent",
    "alrawabi-school",
    "paquita-salas",
    "die-discounter",
    "the-producers",
    "boris",
    "the-naked-director",
    "behind-the-scenes",
    "domashniy-arest",
]


def discover_validated_episodes() -> list[dict]:
    """Build strict round-robin episode queue from existing episodes.json or out/ tree."""
    existing = SHM / "episodes.json"
    if existing.exists():
        raw = json.loads(existing.read_text("utf-8"))
        for i, item in enumerate(raw):
            item["prio"] = i
            sh = item["episode"].rsplit("-s", 1)[0]
            item["settings"] = str((ROOT / SHOW_SETTINGS[sh]).resolve())
        return raw

    # Fallback: build round-robin across available episodes in out/
    by_show: dict[str, list[str]] = {}
    for sh in ROUND_ROBIN_SHOW_ORDER:
        sdir = ROOT / "out" / sh
        if not sdir.is_dir():
            continue
        raw_eps = sorted(p.name for p in sdir.glob("s[0-9][0-9]e[0-9][0-9]") if p.is_dir() and any(p.glob("scene-*.json")))
        # Keep alrawabi-school to s01e01 only (sources e02..e04 are wrong-show subtitles)
        if sh == "alrawabi-school":
            raw_eps = [e for e in raw_eps if e == "s01e01"]
        # Only queue episodes that pass validate.py --require-notes cleanly
        import subprocess
        eps = [
            e for e in raw_eps
            if subprocess.run(
                [sys.executable, "-I", str(ROOT / "tools" / "validate.py"), "--require-notes", str(sdir / e)],
                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
            ).returncode == 0
        ]
        by_show[sh] = eps

    out = []
    max_len = max((len(v) for v in by_show.values()), default=0)
    for r_idx in range(max_len):
        for sh in ROUND_ROBIN_SHOW_ORDER:
            eps = by_show.get(sh, [])
            if r_idx < len(eps):
                ep_code = eps[r_idx]
                out.append({
                    "prio": len(out),
                    "episode": f"{sh}-{ep_code}",
                    "settings": str((ROOT / SHOW_SETTINGS[sh]).resolve()),
                })
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--reset-done", action="store_true", help="Clear /dev/shm/overhear-turbo queues & done_*.json markers (preserves SSD cache/tts)")
    ap.add_argument("--exec-master", action="store_true", help="Exec render/turbo_daemon.py master after writing queue")
    a = ap.parse_args()

    SHM.mkdir(parents=True, exist_ok=True)
    eps = discover_validated_episodes()

    if a.reset_done:
        (SHM / "STOP").unlink(missing_ok=True)
        for sub in ("jobs_qwen", "jobs_en", "jobs_ru", "jobs_ar", "cands", "accepted"):
            d = SHM / sub
            if d.exists():
                shutil.rmtree(d)
            d.mkdir(parents=True, exist_ok=True)
        for done_f in SHM.glob("done_*.json"):
            done_f.unlink(missing_ok=True)

    (SHM / "episodes.json").write_text(json.dumps(eps, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {len(eps)} episodes in strict round-robin order to {SHM / 'episodes.json'}:")
    for item in eps[:12]:
        print(f"  prio={item['prio']:04d}  {item['episode']}")

    if a.exec_master:
        cmd = [
            sys.executable, "-B", "-I", str(ROOT / "render" / "turbo_daemon.py"),
            "master", "--qwen-workers", "1", "--en-workers", "3", "--ru-workers", "2",
            "--gate-workers", "1", "--batch-seqs", "16",
        ]
        os.execv(sys.executable, cmd)


if __name__ == "__main__":
    main()
