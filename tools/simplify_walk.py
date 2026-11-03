#!/usr/bin/env python3
"""Simplify Overhear scene scripts to translation-only line-by-line narration.

Preserves:
  1. English SCENE_INTRO at the start (seg 0)
  2. Full target-language dialogue play (COLD_OPEN)
  3. English line-by-line introduction ('Now let's go through it line by line...')
  4. Line-by-line section: [Target-language line] -> [English translation ONLY]
     (strips all AI-slop grammar/vocab explanation prose and inline word-callout sub-segments)
  5. Transition ('Now let's listen to the whole scene again...') + full target-language replay + English OUTRO + target-language CLOSING.

Also updates:
  - Corresponding `scene-NN.notes.json` (`seg` indices remapped cleanly; deleted inline-callout note lines dropped)
  - Corresponding `learn/**/*.json` (`examples[].seg` indices remapped cleanly if pointing into modified scenes)
  - Optional `authoring/scene-NN.py` files when `--sync-authoring` is set.

Usage:
  python3 tools/simplify_walk.py out/porta-dos-fundos/s01e01
  python3 tools/simplify_walk.py --all out
"""
import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

GLOSS_RE = re.compile(r"^'(.+?)'(?=\s|$)\s*(.*)$", re.S)
DBL_GLOSS_RE = re.compile(r'^"(.+?)"(?=\s|$)\s*(.*)$', re.S)
TRANSITION_RE = re.compile(
    r"((?:Now|Let's|Next,?)\s+(?:let's\s+|we\s+will\s+|we'll\s+)?(?:listen|hear)\b[^'\"\\n]*[.!])$",
    re.I,
)


def extract_translation_and_transition(full_narr_text: str) -> tuple[str, str]:
    """Extract ('<English translation>', optional_transition_sentence) from a WALK narrator block."""
    txt = full_narr_text.strip()
    trans = ""
    m_tr = TRANSITION_RE.search(txt)
    if m_tr:
        trans = m_tr.group(1).strip()
        txt_body = txt[:m_tr.start()].strip()
    else:
        txt_body = txt

    # Strip mechanical leading stub like "It literally means this. 'Hello.'"
    txt_body = re.sub(r"^(?:It literally means this\.|The word for)\s+", "", txt_body)

    m = GLOSS_RE.match(txt_body)
    if m:
        gloss = m.group(1).strip().strip("'\"")
        if gloss and gloss[-1] not in ".!?…":
            gloss += "."
        return f"'{gloss}'", trans

    m2 = DBL_GLOSS_RE.match(txt_body)
    if m2:
        gloss = m2.group(1).strip().strip("'\"")
        if gloss and gloss[-1] not in ".!?…":
            gloss += "."
        return f"'{gloss}'", trans

    # Fallback: take first sentence only
    first = re.split(r"(?<=[.!?])\s+", txt_body, maxsplit=1)[0].strip().strip("'\"")
    if first and first[-1] not in ".!?…":
        first += "."
    return f"'{first}'", trans


def find_scene_bounds(segs: list[dict]) -> tuple[int, int] | None:
    """Locate (walk_start_idx, replay_start_idx) in scene segments, matching validate.py's 5-part structure."""
    if len(segs) < 6 or segs[0]["v"] != "narrator":
        return None
    # Part 1: cold-open story = segs[1 : opener_idx]
    opener_idx = next((i for i in range(1, len(segs)) if segs[i]["v"] == "narrator"), None)
    if opener_idx is None or opener_idx < 2:
        return None
    story_pairs = [(segs[k]["v"], segs[k]["t"]) for k in range(1, opener_idx)]
    n_story = len(story_pairs)
    # Find the final story replay near the end
    replay_idx = None
    for cand in range(len(segs) - n_story - 1, opener_idx, -1):
        if [(segs[cand + m]["v"], segs[cand + m]["t"]) for m in range(n_story)] == story_pairs:
            replay_idx = cand
            break
    if replay_idx is None:
        return None
    return opener_idx + 1, replay_idx


def simplify_scene_file(scene_json: Path, seg_remap_by_scene_id: dict[str, dict[int, int]]) -> bool:
    doc = json.loads(scene_json.read_text("utf-8"))
    segs = doc.get("segments", [])
    bounds = find_scene_bounds(segs)
    if bounds is None:
        return False
    walk_start, replay_start = bounds

    new_segs = []
    old_to_new: dict[int, int] = {}

    # 1. Keep SCENE_INTRO + COLD_OPEN + WALK_INTRO (0 .. walk_start - 1) untouched
    for idx in range(0, walk_start):
        old_to_new[idx] = len(new_segs)
        new_segs.append(dict(segs[idx]))

    # 2. Simplify WALK [walk_start .. replay_start - 1] into [Foreign replay] -> ['<Translation>'] pairs
    i = walk_start
    walk_turns = []
    while i < replay_start:
        # Target-language replay line (could occasionally be 2 consecutive non-narrator lines if split, though standard is 1)
        if segs[i]["v"] == "narrator":
            # Standalone transition narrator right before replay
            old_to_new[i] = len(new_segs)
            new_segs.append(dict(segs[i]))
            i += 1
            continue

        foreign_idx = i
        foreign_seg = dict(segs[i])
        foreign_seg["gap"] = 0.55
        i += 1

        # Collect the narrator translation + any split inline callout chain belonging to this turn
        narr_first_idx = None
        narr_parts = []
        while i < replay_start:
            if segs[i]["v"] == "narrator":
                if narr_first_idx is None:
                    narr_first_idx = i
                narr_parts.append(segs[i]["t"])
                i += 1
            elif segs[i]["v"] != "narrator" and float(segs[i].get("gap", 0.35) or 0) <= 0.251:
                # Inline word callout inside explanation -> drop!
                i += 1
            else:
                break

        full_narr_str = " ".join(narr_parts)
        if narr_first_idx is not None and full_narr_str.strip():
            walk_turns.append((foreign_idx, foreign_seg, narr_first_idx, full_narr_str))
        # Otherwise foreign_seg had no narrator translation after it (orphaned trailing inline callout) -> drop!

    for t_idx, (f_old_idx, f_seg, n_old_idx, full_narr) in enumerate(walk_turns):
        old_to_new[f_old_idx] = len(new_segs)
        new_segs.append(f_seg)
        if n_old_idx is not None and full_narr.strip():
            gloss_only, trans = extract_translation_and_transition(full_narr)
            is_last = (t_idx == len(walk_turns) - 1)
            if is_last and trans:
                out_t = f"{gloss_only} {trans}"
                out_gap = 0.9
            else:
                out_t = gloss_only
                out_gap = 0.9 if is_last else 0.45
            old_to_new[n_old_idx] = len(new_segs)
            new_segs.append({"v": "narrator", "t": out_t, "gap": out_gap})

    # 3. Keep REPLAY + OUTRO + CLOSING [replay_start .. end] untouched
    for idx in range(replay_start, len(segs)):
        old_to_new[idx] = len(new_segs)
        new_segs.append(dict(segs[idx]))

    if new_segs == segs:
        return False

    doc["segments"] = new_segs
    scene_json.write_text(json.dumps(doc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    # Remap scene-NN.notes.json
    notes_path = scene_json.with_name(f"{scene_json.stem}.notes.json")
    if notes_path.exists():
        ndoc = json.loads(notes_path.read_text("utf-8"))
        new_lines = []
        for ln in ndoc.get("lines", []):
            old_s = ln.get("seg")
            if old_s in old_to_new and new_segs[old_to_new[old_s]]["v"] != "narrator":
                ln_copy = dict(ln)
                ln_copy["seg"] = old_to_new[old_s]
                new_lines.append(ln_copy)
        ndoc["lines"] = new_lines
        notes_path.write_text(json.dumps(ndoc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    scene_id = doc.get("id") or f"{scene_json.parent.parent.name}-{scene_json.parent.name}-{scene_json.stem}"
    seg_remap_by_scene_id[scene_id] = old_to_new
    return True


def update_learn_references(seg_remap_by_scene_id: dict[str, dict[int, int]]):
    if not seg_remap_by_scene_id:
        return
    learn_root = ROOT / "learn"
    if not learn_root.exists():
        return
    for lf in sorted(learn_root.glob("*/*.json")):
        ldoc = json.loads(lf.read_text("utf-8"))
        changed = False
        for ex in ldoc.get("examples", []):
            sid = ex.get("sceneId")
            if sid in seg_remap_by_scene_id:
                remap = seg_remap_by_scene_id[sid]
                if ex.get("seg") in remap and remap[ex["seg"]] != ex["seg"]:
                    ex["seg"] = remap[ex["seg"]]
                    changed = True
        if changed:
            lf.write_text(json.dumps(ldoc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("paths", nargs="+", help="Episode dir(s) or 'out' with --all")
    ap.add_argument("--all", action="store_true", help="Recurse into all episodes under given path(s)")
    a = ap.parse_args()

    scene_files = []
    for p_str in a.paths:
        p = Path(p_str)
        if a.all or (p / "kukhnya").exists() or (p / "scenes.json").exists() is False:
            scene_files.extend(sorted(f for f in p.rglob("scene-*.json") if not f.name.endswith(".notes.json") and "authoring" not in f.parts))
        else:
            scene_files.extend(sorted(f for f in p.glob("scene-*.json") if not f.name.endswith(".notes.json")))

    seg_remap = {}
    modified = 0
    for sf_path in scene_files:
        if simplify_scene_file(sf_path, seg_remap):
            modified += 1
    update_learn_references(seg_remap)
    print(f"Simplified {modified}/{len(scene_files)} scene files (remapped {len(seg_remap)} scene note tables).")


if __name__ == "__main__":
    main()
