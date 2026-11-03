#!/usr/bin/env python3
"""Build the weighted 10-language round-robin queue in /dev/shm/overhear-turbo and optionally rebalance live jobs.

Schedule:
  - Rounds 1 & 2 (prio 0000..0017, already published): 1 episode per validated show across all 10 languages.
  - Round 3+ weighted round-robin cycle (per owner request):
      * 3 Russian episodes (`ru`: 2x `kukhnya` + 1x `domashniy-arest`, falling back to `kukhnya` once `domashniy-arest` completes)
      * 2 French episodes  (`fr`: 2x `dix-pour-cent`)
      * 1 episode each of every other available language (`pt`, `ar`, `es`, `de`, `ko`, `it`, `ja`, `zh`)
      * Repeat until all validated episodes across all shows are rendered and published!

Usage:
  python3 tools/launch_round_robin.py --rebalance-live
  python3 tools/launch_round_robin.py --reset-done
  OVERHEAR_HOME="$HOME/overhear" python3 tools/launch_round_robin.py --exec-master
"""
import argparse
import json
import os
import shutil
import subprocess
import sys
from collections import deque
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

OTHER_SHOWS_ORDER = [
    "porta-dos-fundos",   # pt
    "alrawabi-school",    # ar
    "paquita-salas",      # es
    "die-discounter",     # de
    "the-producers",      # ko
    "boris",              # it
    "the-naked-director", # ja
    "behind-the-scenes",  # zh
]

# Exact historical order of the 18 completed Round 1 + Round 2 releases + active prio 0018
PINNED_PREFIX = [
    "porta-dos-fundos-s01e01",
    "kukhnya-s01e01",
    "dix-pour-cent-s01e01",
    "alrawabi-school-s01e01",
    "paquita-salas-s01e01",
    "die-discounter-s01e01",
    "the-producers-s01e01",
    "boris-s01e01",
    "the-naked-director-s01e01",
    "behind-the-scenes-s01e01",
    "domashniy-arest-s01e01",
    "kukhnya-s01e02",
    "dix-pour-cent-s01e02",
    "paquita-salas-s01e02",
    "the-producers-s01e02",
    "the-naked-director-s01e02",
    "behind-the-scenes-s01e02",
    "domashniy-arest-s01e02",
]


def scan_validated_out() -> dict[str, deque[str]]:
    by_show: dict[str, deque[str]] = {}
    for sh in SHOW_SETTINGS:
        sdir = ROOT / "out" / sh
        if not sdir.is_dir():
            by_show[sh] = deque()
            continue
        raw_eps = sorted(p.name for p in sdir.glob("s[0-9][0-9]e[0-9][0-9]") if p.is_dir() and any(p.glob("scene-*.json")))
        if sh == "alrawabi-school":
            raw_eps = [e for e in raw_eps if e == "s01e01"]
        eps = [
            f"{sh}-{e}" for e in raw_eps
            if subprocess.run(
                [sys.executable, "-I", str(ROOT / "tools" / "validate.py"), "--require-notes", str(sdir / e)],
                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
            ).returncode == 0
        ]
        by_show[sh] = deque(eps)
    return by_show


def build_weighted_round_robin() -> list[dict]:
    """Build weighted 3 RU -> 2 FR -> 1 each of other languages schedule across all validated episodes."""
    by_show = scan_validated_out()
    all_valid = {ep for q in by_show.values() for ep in q}

    ordered: list[str] = []
    used: set[str] = set()

    # Keep pinned completed prefix first so done_*.json and historical prios never shift
    for ep in PINNED_PREFIX:
        if ep in all_valid and ep not in used:
            ordered.append(ep)
            used.add(ep)

    for sh, q in by_show.items():
        by_show[sh] = deque(ep for ep in q if ep not in used)

    while any(by_show.values()):
        # 1. Russian: 3 episodes per cycle (kukhnya -> domashniy-arest -> kukhnya, fallback to whichever has episodes)
        ru_picks = 0
        for pref in ("kukhnya", "domashniy-arest", "kukhnya"):
            if by_show[pref]:
                ordered.append(by_show[pref].popleft())
                ru_picks += 1
        while ru_picks < 3 and (by_show["kukhnya"] or by_show["domashniy-arest"]):
            src = "kukhnya" if by_show["kukhnya"] else "domashniy-arest"
            ordered.append(by_show[src].popleft())
            ru_picks += 1

        # 2. French: 2 episodes per cycle
        for _ in range(2):
            if by_show["dix-pour-cent"]:
                ordered.append(by_show["dix-pour-cent"].popleft())

        # 3. Other 8 languages: 1 episode each per cycle whenever available
        for sh in OTHER_SHOWS_ORDER:
            if by_show[sh]:
                ordered.append(by_show[sh].popleft())

    out = []
    for idx, ep in enumerate(ordered):
        sh = ep.rsplit("-s", 1)[0]
        out.append({
            "prio": idx,
            "episode": ep,
            "settings": str((ROOT / SHOW_SETTINGS[sh]).resolve()),
        })
    return out


def rebalance_live_shm(eps: list[dict], min_rebalance_prio: int = 19) -> int:
    """Atomically re-rank pending /dev/shm/overhear-turbo/jobs_* JSON files to match new weighted prios without stopping workers."""
    prio_map = {item["episode"]: item["prio"] for item in eps}
    moved = 0
    for sub in ("jobs_en", "jobs_qwen", "jobs_ru", "jobs_ar"):
        d = SHM / sub
        if not d.is_dir():
            continue
        for entry in list(os.scandir(d)):
            nm = entry.name
            if not nm.endswith(".json") or nm.startswith(".") or not nm[:4].isdigit():
                continue
            old_p = int(nm[:4])
            if old_p < min_rebalance_prio:
                continue
            # Format: {prio:04d}_{episode}_{key}.json
            rest = nm[5:-5]
            if "_" not in rest:
                continue
            ep, key = rest.rsplit("_", 1)
            new_p = prio_map.get(ep)
            if new_p is None or new_p == old_p:
                continue
            src = d / nm
            dst = d / f"{new_p:04d}_{ep}_{key}.json"
            tmp = d / f".rebal.{os.getpid()}.{new_p:04d}_{ep}_{key}.json"
            try:
                data = json.loads(src.read_text("utf-8"))
                data["prio"] = new_p
                tmp.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
                src.unlink()
                tmp.replace(dst)
                moved += 1
            except OSError:
                tmp.unlink(missing_ok=True)
    return moved


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--reset-done", action="store_true", help="Clear /dev/shm/overhear-turbo queues & done_*.json markers (preserves SSD cache/tts)")
    ap.add_argument("--rebalance-live", action="store_true", help="Re-rank pending jobs_* (prio >= 19) in /dev/shm to match weighted round-robin without restarting daemons")
    ap.add_argument("--exec-master", action="store_true", help="Exec render/turbo_daemon.py master after writing queue")
    a = ap.parse_args()

    SHM.mkdir(parents=True, exist_ok=True)
    eps = build_weighted_round_robin()

    if a.reset_done:
        (SHM / "STOP").unlink(missing_ok=True)
        for sub in ("jobs_qwen", "jobs_en", "jobs_ru", "jobs_ar", "cands", "accepted"):
            d = SHM / sub
            if d.exists():
                shutil.rmtree(d)
            d.mkdir(parents=True, exist_ok=True)
        for done_f in SHM.glob("done_*.json"):
            done_f.unlink(missing_ok=True)

    tmp_ep = SHM / f".episodes.{os.getpid()}.json"
    tmp_ep.write_text(json.dumps(eps, indent=2) + "\n", encoding="utf-8")
    tmp_ep.replace(SHM / "episodes.json")

    if a.rebalance_live:
        moved = rebalance_live_shm(eps, min_rebalance_prio=19)
        print(f"Rebalanced {moved} live job files in {SHM} to weighted 3-RU / 2-FR / 1-others schedule.")

    print(f"Wrote {len(eps)} validated episodes to {SHM / 'episodes.json'}. Upcoming queue (prio 0018..0035):")
    for item in eps[18:36]:
        print(f"  prio={item['prio']:04d}  {item['episode']}")

    if a.exec_master:
        cmd = [
            sys.executable, "-B", "-I", str(ROOT / "render" / "turbo_daemon.py"),
            "master", "--qwen-workers", "1", "--en-workers", "2", "--ru-workers", "2",
            "--gate-workers", "1", "--batch-seqs", "14",
        ]
        os.execv(sys.executable, cmd)


if __name__ == "__main__":
    main()
