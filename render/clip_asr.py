"""Whisper check of rendered example clips (venv with faster-whisper + jiwer; GPU, ~2.5 GB).

  python -I clip_asr.py --store DIR --cer-max 0.15 --retakes 2 [--kind forms --pad-sec 0.3 --fold-vowels] ID [ID ...]

Transcribes .work/<id>.mp3 in the clip's language and compares it with its reference (spoken alternatives for non-Russian forms). A pass is committed to clips/<id>.mp3;
a fail is marked for a retake, or recorded as failed when the retakes are used up. Prints one line:
  OK {"passed": n, "retry": [ids], "failed": [ids], "cer": {id: cer}}
"""
import argparse
import json
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import clips  # noqa: E402
from asr_cer import nz  # noqa: E402
import numwords  # noqa: E402


def load(path, pad_sec=0.0):
    """16 kHz mono samples, with `pad_sec` of silence on each side (for Whisper only: a lone word is easier to hear with a lead-in)."""
    r = subprocess.run(["ffmpeg", "-v", "error", "-i", str(path), "-ac", "1", "-ar", "16000", "-f", "f32le", "-"], capture_output=True)
    x = np.frombuffer(r.stdout, dtype=np.float32)
    if pad_sec:
        pad = np.zeros(int(16000 * pad_sec), dtype=np.float32)
        x = np.concatenate([pad, x, pad])
    return x


_PAIRS = {"о": "а", "е": "и"}
ACUTE = "́"


def chars_with_stress(tts):
    """[(letter, unstressed)] of the text sent to the model, normalised like asr_cer.nz (lower case, ё as е, words separated by one space).
    A vowel is unstressed when its word carries a stress mark elsewhere (>= 2 vowels); a lone vowel, a ё and a word with no mark are stressed or unknown."""
    out = []
    for word in tts.replace("-", " ").split():       # a hyphenated compound is heard (and written by Whisper) as separate words
        letters = []
        for ch in word:
            if ch == ACUTE:
                if letters:
                    letters[-1][1] = False
            elif ch.isalpha():
                letters.append([nz(ch) or ch.lower(), ch not in "ёЁ"])
        vowels = [x for x in letters if x[0] in "аеёиоуыэюя"]
        marked = any(not x[1] for x in vowels)
        for x in letters:
            x[1] = bool(marked and x[1] and len(vowels) >= 2 and x[0] in _PAIRS)
        if letters:
            out += [(x[0], x[1]) for x in letters] + [(" ", False)]
    return out[:-1] if out else out


_ADJ_ENDINGS = ("ый", "ой", "ий", "ая", "яя", "ое", "ее", "ые", "ие", "ую", "юю")


def unstressed_adjective_ending(tts):
    """True when the last word of the text sent to the model ends in an adjective ending that carries no stress mark ("ва́жной"): the one
    place where the voice and Whisper tend to disagree about -ой/-ый, which a further take often settles."""
    words = tts.split()
    if not words:
        return False
    w = words[-1].strip(",.")
    return w.endswith(_ADJ_ENDINGS) and ACUTE in w and w.index(ACUTE) < len(w) - 3


def folded_cer(tts, hyp):
    """Edit distance / length of the reference where an UNSTRESSED о may be heard as а and an unstressed е as и (and back): the reduction of
    unstressed vowels is correct Russian, but a wrong case ending (вино/вина, дне/дни) still costs, because it is on a stressed vowel or a lone one."""
    ref = chars_with_stress(tts)
    hyp = nz(hyp)
    if not ref:
        return 1.0 if hyp else 0.0
    prev = list(range(len(hyp) + 1))
    for i, (rc, unstressed) in enumerate(ref, 1):
        cur = [i]
        for j, hc in enumerate(hyp, 1):
            same = rc == hc or (unstressed and _PAIRS.get(rc) == hc) or (unstressed and rc in _PAIRS.values() and _PAIRS.get(hc) == rc)
            cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (0 if same else 1)))
        prev = cur
    return prev[-1] / len(ref)


def comparison_texts(record, kind, hyp):
    """Compare spoken table alternatives; number expansion is Russian only."""
    ref = record["tts"] if kind == "forms" and record["lang"] != "ru" else record["text"]
    heard = numwords.expand(hyp, ref) if record["lang"] == "ru" and any(ch.isdigit() for ch in hyp) else hyp
    return ref, heard


def comparison_cer(record, kind, hyp, fold_vowels=False):
    import jiwer
    ref, heard = comparison_texts(record, kind, hyp)
    # Russian acute accents are editorial stress marks. French acute accents
    # are spelling and can change pronunciation (parle/parlé), so retain them.
    def normalize(text):
        if record["lang"] == "ru":
            return nz(text)
        text = unicodedata.normalize("NFC", text).lower()
        if record["lang"] == "ar":
            text = re.sub(r"[\u0640\u064b-\u065f\u0670]", "", text)
            text = re.sub(r"[أإآٱ]", "ا", text)
        if record["lang"] == "hi":
            text = text.replace("\u093c", "").replace("\u0901", "\u0902")
            for a, b in (("ये", "ए"), ("यी", "ई"), ("ईए", "इए"), ("न्", "ं"), ("म्", "ं")):
                text = text.replace(a, b)
            cleaned = "".join(ch if unicodedata.category(ch)[0] in ("L", "M", "N") else " " for ch in text)
            return re.sub(r"\s+", " ", cleaned).strip()
        if record["lang"] in ("ja", "zh"):
            return re.sub(r"[^\w]", "", text)
        return re.sub(r"\s+", " ", re.sub(r"[^\w\s]", " ", text)).strip()
    if not normalize(heard):
        return 1.0
    if fold_vowels and record["lang"] == "ru":
        return folded_cer(record["tts"], heard)
    return jiwer.cer(normalize(ref), normalize(heard))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--store", required=True)
    ap.add_argument("--cer-max", type=float, required=True)
    ap.add_argument("--retakes", type=int, required=True)
    ap.add_argument("--kind", default="clips", help="store directory: clips | forms")
    ap.add_argument("--pad-sec", type=float, default=0.0)
    ap.add_argument("--fold-vowels", action="store_true")
    ap.add_argument("--second-pad", type=float, default=0.0, help="when a take fails, listen once more with this much silence on each side (same beam 5, no conditioning, same CER gate)")
    ap.add_argument("--paradigm", default="", help="forms only: JSON {id: {text, single, others}}; with --margin, a take that fails the CER gate still passes when the forced-scoring gate accepts it")
    ap.add_argument("--margin", type=float, default=None, help="forced-scoring gate: nats by which the reference must outscore every other form of the lemma and Whisper's own decoding")
    ap.add_argument("--extra-retakes", type=int, default=0, help="further retakes for forms with an unstressed adjective ending")
    ap.add_argument("ids", nargs="+")
    a = ap.parse_args()
    from faster_whisper import WhisperModel
    import time
    try:
        m = WhisperModel("large-v3-turbo", device="cuda", compute_type="float16")
    except Exception as e:
        print("cuda unavailable, cpu:", e, file=sys.stderr)
        m = WhisperModel("large-v3-turbo", device="cpu", compute_type="int8")
    cpu_m = None

    def run_transcribe(audio_arr, lang):
        nonlocal cpu_m, m
        if m is not None:
            for attempt in range(3):
                try:
                    segs, _ = m.transcribe(audio_arr, language=lang, beam_size=5, condition_on_previous_text=False, vad_filter=False)
                    return " ".join(t.text for t in segs).strip()
                except RuntimeError as e:
                    if attempt < 2:
                        import gc
                        m = None
                        gc.collect()
                        time.sleep(2.5 * (attempt + 1))
                        try:
                            m = WhisperModel("large-v3-turbo", device="cuda", compute_type="float16")
                        except Exception:
                            pass
                        if m is not None:
                            continue
                    print(f"clip_asr cuda error ({e}); switching to cpu WhisperModel", file=sys.stderr, flush=True)
                    m = None
                    break
        if cpu_m is None:
            cpu_m = WhisperModel("large-v3-turbo", device="cpu", compute_type="int8", cpu_threads=12)
        segs, _ = cpu_m.transcribe(audio_arr, language=lang, beam_size=5, condition_on_previous_text=False, vad_filter=False)
        return " ".join(t.text for t in segs).strip()

    cs = clips.ClipStore(a.store, a.kind)
    out = {"passed": 0, "retry": [], "failed": [], "cer": {}, "forced": {}}
    para = json.load(open(a.paradigm)) if a.paradigm else {}
    scorer = None
    if para and a.margin is not None:
        import forced_score
        scorer = forced_score.ForcedScorer(m, "ru")
    for cid in a.ids:
        w = cs.work_record(cid)
        if not w:
            continue
        hyp = run_transcribe(load(cs.work / f"{cid}.mp3", a.pad_sec), w["lang"])
        cer = comparison_cer(w, a.kind, hyp, a.fold_vowels)
        if cer > a.cer_max and a.second_pad and a.second_pad != a.pad_sec:
            hyp2 = run_transcribe(load(cs.work / f"{cid}.mp3", a.second_pad), w["lang"])
            cer2 = comparison_cer(w, a.kind, hyp2, a.fold_vowels)
            if cer2 < cer:
                cer, hyp = cer2, hyp2
        out["cer"][cid] = round(cer, 4)
        gate = None
        if cer > a.cer_max and w["lang"] == "ru" and scorer is not None and cid in para and para[cid]["single"] and para[cid]["others"] and nz(hyp):
            try:
                scorer.encode(load(cs.work / f"{cid}.mp3", a.pad_sec))
                gate = scorer.margin(para[cid]["text"], para[cid]["others"], hyp)
                out["forced"][cid] = round(gate, 2)
            except RuntimeError:
                gate = None
        if cer <= a.cer_max or (gate is not None and gate >= a.margin):
            clips.commit(a.store, cid, cer, hyp, None, a.kind)
            if gate is not None and gate >= a.margin:
                rp = Path(a.store) / a.kind / f"{cid}.json"
                rec = json.loads(rp.read_text("utf-8"))
                rec.update(gate="forced", forcedMargin=round(gate, 2), hyp=hyp)
                rp.write_text(json.dumps(rec, ensure_ascii=False, sort_keys=True, indent=1), "utf-8")
            out["passed"] += 1
        elif w["tries"] >= a.retakes + (a.extra_retakes if unstressed_adjective_ending(w.get("tts", "")) else 0):
            clips.fail_final(a.store, cid, cer, hyp, a.kind)
            out["failed"].append(cid)
        else:
            w["failedCheck"] = True
            w.setdefault("history", []).append({"try": w["tries"], "cer": round(cer, 4), "hyp": hyp, **({"margin": round(gate, 2)} if gate is not None else {})})
            cs.write_work(cid, w)
            out["retry"].append(cid)
    print("OK " + json.dumps(out, ensure_ascii=False), flush=True)


if __name__ == "__main__":
    main()
