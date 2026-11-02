import json
import sys
import re

def squash(s):
    return re.sub(r"[\W_]+", " ", s.lower().replace("ё", "е")).strip()

def main():
    scene_file = sys.argv[1]
    notes_file = scene_file.replace(".json", ".notes.json")
    
    with open(scene_file, "r", encoding="utf-8") as f:
        scene = json.load(f)
        
    with open(notes_file, "r", encoding="utf-8") as f:
        notes = json.load(f)
        
    segs = scene["segments"]
    original_lines = notes.get("lines", [])
    new_lines = []
    
    text_to_line = {}
    story_lines = []
    
    story_target_segs = []
    for i, s in enumerate(segs):
        if i == 0: continue
        if s["v"] == "narrator": break
        story_target_segs.append(s["t"])
        
    for i, text in enumerate(story_target_segs):
        if i < len(original_lines):
            story_lines.append((text, original_lines[i]))
            text_to_line[squash(text)] = original_lines[i]
            
    for i, s in enumerate(segs):
        if s["v"] == "narrator":
            continue
            
        t_squash = squash(s["t"])
        
        if t_squash in text_to_line:
            new_entry = dict(text_to_line[t_squash])
            new_entry["seg"] = i
            new_lines.append(new_entry)
            continue
            
        parent_text, parent_ann = None, None
        for st_text, st_ann in story_lines:
            if s["t"] in st_text:
                parent_text, parent_ann = st_text, st_ann
                break
            callout_tokens = [x for x in s["t"].split() if re.search(r"\w", x)]
            callout_squashed_tokens = [squash(x) for x in callout_tokens]
            st_squashed_tokens = squash(st_text).split()
            if any(st_squashed_tokens[j:j+len(callout_squashed_tokens)] == callout_squashed_tokens for j in range(len(st_squashed_tokens) - len(callout_squashed_tokens) + 1)):
                parent_text, parent_ann = st_text, st_ann
                break
            if t_squash.strip() in squash(st_text).strip():
                parent_text, parent_ann = st_text, st_ann
                break
                parent_text, parent_ann = st_text, st_ann
                break
            if re.search(r"\b" + re.escape(t_squash) + r"\b", squash(st_text)): 
                parent_text, parent_ann = st_text, st_ann
                break
                
        if parent_ann:
            callout_words = []
            parent_words = parent_ann.get("words", [])
            match_start = -1
            match_end = -1
            
            # CJK-friendly concat match
            for j in range(len(parent_words)):
                for k in range(j + 1, len(parent_words) + 1):
                    combined = squash("".join(w.get("t", "") for w in parent_words[j:k]))
                    if combined.replace(" ", "") == t_squash.replace(" ", ""):
                        match_start = j
                        match_end = k
                        break
                if match_start != -1:
                    break
            
            # Fallback 1: substring match (for CJK sub-tokens like らしさ)
            if match_start == -1:
                for j, w in enumerate(parent_words):
                    if t_squash.replace(" ", "") in squash(w.get("t", "")).replace(" ", ""):
                        match_start = j
                        match_end = j + 1
                        break
            
            # Original space-separated match
            if match_start == -1:
                callout_tokens = s["t"].split()
                callout_squashed_tokens = [squash(x) for x in callout_tokens if re.search(r"\w", x)]
                parent_squashed = [squash(w.get("t", "")) for w in parent_words]
                for j in range(len(parent_squashed) - len(callout_squashed_tokens) + 1):
                    if parent_squashed[j:j+len(callout_squashed_tokens)] == callout_squashed_tokens:
                        match_start = j
                        match_end = j + len(callout_squashed_tokens)
                        break

            if match_start != -1:

                import copy
                callout_words_orig = copy.deepcopy(parent_words[match_start:match_end])
                
                pos = 0
                for w in callout_words_orig:
                    idx = s["t"].lower().find(w["t"].lower(), pos)
                    if idx != -1:
                        w["t"] = s["t"][idx:idx+len(w["t"])]
                        if "span" in w or any(lang in s["t"] for lang in ("ja", "zh", "ko", "ar")):
                            w["span"] = [idx, idx + len(w["t"])]
                        pos = idx + len(w["t"])
                    else:
                        if "span" in w or any(lang in s["t"] for lang in ("ja", "zh", "ko", "ar")):
                            w["span"] = [pos, pos + len(w["t"])]
                        pos += len(w["t"])
                        
                callout_words = callout_words_orig
                trans = " / ".join(w.get("gloss","") for w in callout_words_orig if w.get("gloss"))
                if not trans: trans = parent_ann.get("trans", "")
                if trans:
                    # To apply trans correctly, we actually just set it in new_ann below
                    pass


            if match_start == -1:
                print(f"Warning: could not find token match for {s['t']} in {parent_text}. Expected tokens: {callout_squashed_tokens}, got {parent_squashed}")
                callout_words = []
            
            if not callout_words:
                callout_words = [{"t": s["t"], "lemma": s["t"].replace("。", "").replace("?", "").replace("!", ""), "pos": "noun", "gloss": "fallback", "gram": "fallback", "span": [0, len(s["t"])], "stress": s["t"].replace("-", "") if "ё" not in s["t"] and sum(1 for c in s["t"] if c in "аеёиоуыэюя") == 1 else None}]
                callout_words_orig = callout_words
            new_entry = {
                "seg": i,
                "trans": " / ".join(w.get("gloss","") for w in callout_words_orig if w.get("gloss")) or parent_ann.get("trans", ""),
                "words": callout_words
            }
            new_lines.append(new_entry)
        else:
            # CLOSING segment
            t_squashed = squash(s["t"])
            found = False
            for old_line in original_lines:
                combined = squash("".join(w.get("t", "") for w in old_line.get("words", [])))
                if combined == t_squashed:
                    new_entry = dict(old_line)
                    new_entry["seg"] = i
                    new_lines.append(new_entry)
                    found = True
                    break
            if not found:
                callout_tokens = [squash(x) for x in s["t"].split() if re.search(r"\w", x)]
                for old_line in original_lines:
                    old_tokens = [squash(w.get("t", "")) for w in old_line.get("words", [])]
                    if old_tokens == callout_tokens:
                        new_entry = dict(old_line)
                        new_entry["seg"] = i
                        new_lines.append(new_entry)
                        found = True
                        break
            if not found:
                print(f"Warning: could not find annotation for target segment {i}: {s['t']}", file=sys.stderr)
                new_lines.append({
                    "seg": i,
                    "trans": "Translation.",
                    "words": [{"t": s["t"], "lemma": s["t"], "pos": "noun", "gloss": "closing", "gram": "closing", "span": [0, len(s["t"])], "reading": s["t"], "stress": None}]
                })

    notes["lines"] = new_lines
    with open(notes_file, "w", encoding="utf-8") as f:
        json.dump(notes, f, ensure_ascii=False, indent=2)
        f.write("\n")
        
if __name__ == "__main__":
    main()
