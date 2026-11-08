"""Render one scene: TTS (cloned voices) -> assemble -> MMS alignment -> stress check -> (ElevenLabs fallback) -> store.

GPU work; the caller (worker.py) holds gpurun reservation.
"""
import datetime
import json
import re
import time
from pathlib import Path

import numpy as np

import audio
import config
import stresscheck
import textprep
import tts
import native_text
from plan import check_voices, render_key, voice_clashes
from store import sha256_file

TOKEN_RE = re.compile(r"[\w]", re.UNICODE)


def seg_tokens(text, words=None):
    """Tokens timed per segment: the whitespace tokens that contain a letter or digit, exactly the publisher's
    tokens.tokenize(), so render_source.word_times() finds one timing entry per token."""
    return [t for t in text.split() if TOKEN_RE.search(t)]


class CarrierChain:
    """One continuous WALK explanation chain [a..b] where all English narrator parts are synthesized
    as a single unbroken sentence (with 'phrase' placeholders at target-language callout slots) and sliced at MMS_FA valleys."""

    def __init__(self, a, b, carrier_key, carrier_text, char_maps, gaps_override):
        self.a, self.b = a, b
        self.key = carrier_key
        self.text = carrier_text
        self.char_maps = char_maps          # {seg_idx: [carrier_char_idx_or_None, ...]}
        self.gaps_override = gaps_override  # {seg_idx: float_gap_sec}


def _find_inline_chains(segments):
    chains = []
    n = len(segments)
    i = 0
    while i < n - 1:
        g_val = round(float(segments[i].get("gap", 0.35) or 0), 3)
        if g_val == 0.25:
            a = i
            b = i + 1
            while b < n - 1 and round(float(segments[b].get("gap", 0.35) or 0), 3) == 0.25:
                b += 1
            roles_in = {segments[k]["v"] for k in range(a, b + 1)}
            if "narrator" in roles_in and len(roles_in) >= 2:
                chains.append((a, b))
            i = b + 1
        else:
            i += 1
    return chains


def _build_carrier_spec(segments, a, b):
    """Build (carrier_text, char_maps, gaps_override) for inline chain segments[a..b]."""
    buf = []
    char_maps = {}
    gaps_override = {}
    consumed_leading = set()

    for k in range(a, b + 1):
        seg = segments[k]
        orig_gap = float(seg.get("gap", 0.35) or 0)
        if seg["v"] == "narrator":
            orig = seg["t"]
            cmap = [None] * len(orig)
            if not seg_tokens(orig):
                # Punctuation-only narrator tail (e.g. '.' or '!'): punctuation already attached to preceding placeholder
                char_maps[k] = cmap
                gaps_override[k] = orig_gap
                continue
            start_ci = 0
            if k in consumed_leading:
                m = re.match(r"^(\s*[,;:]+)", orig)
                if m:
                    start_ci = m.end()
            if buf and buf[-1] not in (" ", "\n") and start_ci < len(orig) and not orig[start_ci].isspace():
                buf.append(" ")
            end_ci = len(orig.rstrip(" ")) if (k < b and segments[k + 1]["v"] != "narrator") else len(orig)
            for ci in range(start_ci, end_ci):
                ch = orig[ci]
                if ci == start_ci and ch.isspace() and buf and buf[-1] == " ":
                    continue
                cmap[ci] = len(buf)
                buf.append(ch)
            char_maps[k] = cmap
            if k < b:
                r_txt = orig.rstrip()
                tail_ch = r_txt[-1:] if r_txt else ""
                if tail_ch in ".!?…":
                    gaps_override[k] = 0.22
                elif tail_ch in ":;":
                    gaps_override[k] = 0.13
                elif tail_ch == ",":
                    gaps_override[k] = 0.11
                else:
                    gaps_override[k] = 0.05
            else:
                gaps_override[k] = orig_gap
        else:
            # Target-language callout slot -> insert comma-isolated nasal placeholder ', name,' so narrator
            # finishes every preceding English vowel cleanly into a prosodic micro-pause with zero coarticulation
            core_tail = "".join(buf).rstrip(" '\"\t\n)")[-1:]
            if core_tail and core_tail.isalnum():
                while buf and buf[-1] == " ":
                    buf.pop()
                buf.extend([",", " "])
            elif buf and buf[-1] not in (" ", "\n", "(") and not (buf[-1] in ('"', "'") and (len(buf) == 1 or buf[-2] == " ")):
                buf.append(" ")
            punct = ""
            comma_pause = False
            t_strip = seg["t"].rstrip()
            if k + 1 <= b and segments[k + 1]["v"] == "narrator":
                nxt_t = segments[k + 1]["t"]
                if not seg_tokens(nxt_t):
                    p_only = nxt_t.strip()
                    punct = p_only if p_only in (".", "!", "?", '."', ".'") else "."
                else:
                    m = re.match(r"^\s*([,;:]+)", nxt_t)
                    if m:
                        punct = m.group(1)[0]
                        consumed_leading.add(k + 1)
                        comma_pause = True
                    elif re.match(r'^\s*[A-Za-z0-9"\']', nxt_t):
                        punct = ","
            if not punct and t_strip[-1:] in ",;:":
                punct = ","
                comma_pause = True
            if k == b and not punct:
                punct = "."
            ph = "Name" if (core_tail and core_tail in ".!?…") else "name"
            for ch in (ph + punct):
                buf.append(ch)
            if k < b:
                if k + 1 <= b and segments[k + 1]["v"] == "narrator" and not seg_tokens(segments[k + 1]["t"]):
                    gaps_override[k] = 0.01
                elif comma_pause:
                    gaps_override[k] = 0.12
                else:
                    gaps_override[k] = 0.06
            else:
                gaps_override[k] = orig_gap

    carrier_text = re.sub(r" {2,}", " ", "".join(buf)).strip()
    # Recompute exact character map on clean carrier_text by building without duplicate spaces
    buf2 = []
    cmap_clean = {k: [None] * len(segments[k]["t"]) for k in range(a, b + 1) if segments[k]["v"] == "narrator"}
    for idx_b, ch in enumerate(buf):
        if ch == " " and (not buf2 or buf2[-1] == " "):
            continue
        new_pos = len(buf2)
        buf2.append(ch)
        for k, cm in char_maps.items():
            for ci, old_p in enumerate(cm):
                if old_p == idx_b:
                    cmap_clean[k][ci] = new_pos
    while buf2 and buf2[-1] == " ":
        buf2.pop()
    return "".join(buf2), cmap_clean, gaps_override


class Ctx:
    def __init__(self, scene, roles, rkey, sents, uniq, carriers=None):
        self.scene, self.roles, self.rkey, self.sents, self.uniq = scene, roles, rkey, sents, uniq
        self.carriers = carriers or []


class Renderer:
    """Three GPU-light steps, each run in its own process under its own VRAM reservation (see stage.py):
    synth (Qwen, 4.8 GB) -> finish (MMS_FA alignment, 1.5 GB) -> [retake (Qwen) -> finish]."""

    def __init__(self, settings, voices, store, ruaccent=None, log=print):
        self.s, self.voices, self.store = settings, voices, store
        self.ruaccent, self.log = ruaccent, log
        self.sr = settings["audio"]["sampleRate"]
        self.policy = config.stress_policy(settings)

    # -- planning -------------------------------------------------------------------------------------------
    def prepare(self, scene):
        if any("sourceAudio" in seg for seg in scene.script["segments"]):
            raise ValueError("original show sourceAudio is private verification only; public render requires validated native synthesis")
        import retakes
        takes = retakes.for_scene(scene)
        roles = check_voices(scene, self.voices)
        rkey = render_key(scene, self.voices, self.s, roles)
        notes_by_seg = {l["seg"]: l.get("words") or [] for l in scene.notes.get("lines", []) if isinstance(l, dict)}
        sents = []
        isent_cfg = self.s["audio"]["interSentenceGap"]
        segments = scene.script["segments"]

        # Build continuous carrier sentences for split WALK inline callout chains so the narrator speaks
        # one unbroken, comma-inflected sentence per explanation with tight conversational inline timing.
        carriers = []
        chain_by_seg = {}
        narr_voice = roles["narrator"]
        narr_lang = self.voices.lang_of(narr_voice)
        for a, b in _find_inline_chains(segments):
            c_text, c_maps, g_over = _build_carrier_spec(segments, a, b)
            if c_text and c_maps:
                affected = {str(i): takes[str(i)] for i in range(a, b + 1) if str(i) in takes}
                # A carrier is one cached utterance spanning several authored segments.
                counter = int(config.sha(affected)[:16], 16) if affected else 0
                c_key = tts.cache_key(self.s, narr_voice, self.voices.ref_version(narr_voice), narr_lang, c_text, retake=counter)
                ch_obj = CarrierChain(a, b, c_key, c_text, c_maps, g_over)
                carriers.append(ch_obj)
                for k in range(a, b + 1):
                    chain_by_seg[k] = ch_obj

        for i, g in enumerate(segments):
            voice = roles[g["v"]]
            lang = self.voices.lang_of(voice)
            ch_obj = chain_by_seg.get(i)
            if ch_obj is not None and g["v"] == "narrator":
                st = textprep.Sentence(i, 0, "narrator", lang, g["t"], g["t"], 0, gap=ch_obj.gaps_override[i])
                st.voice = voice
                st.key = f"{ch_obj.key}__part_{i}"
                st.carrier_chain = ch_obj
                sents.append(st)
                continue

            eff_gap = ch_obj.gaps_override[i] if ch_obj is not None else float(g.get("gap", 0.35) or 0)
            native_words = native_text.words_for_segment(g["t"], notes_by_seg.get(i), lang) if lang in native_text.LANGUAGES else ()
            ru_cfg = config.ru_engine(self.s)
            ar_cfg = config.ar_engine(self.s)
            seg_policy = self.policy
            turn_max = int(self.s["audio"].get("turnMaxChars", 240))
            if lang == "ru" and ru_cfg:
                if ru_cfg.get("engine") in ("qwen", "qwen-lora"):
                    seg_policy = ru_cfg.get("stress", "all" if ru_cfg.get("lora") else "homographs")
                    turn_max = int(ru_cfg.get("turnMaxChars", 0))
                else:
                    turn_max = min(turn_max, 90)
            elif lang == "ar" and ar_cfg:
                turn_max = int(ar_cfg.get("turnMaxChars", 0))
            elif lang == "en" and turn_max > 145:
                # Preserve existing 240-char cached English takes on already-rendered scenes;
                # use <=145-char chunks for any uncached English turns so 8s sky.flac + gen stays inside Qwen's 20s window.
                cand_240 = textprep.prepare_segment(
                    i, g["v"], g["t"], lang, notes_by_seg.get(i), seg_policy, eff_gap, isent_cfg.get(lang, isent_cfg["en"]),
                    max_turn_chars=turn_max)
                if not all(self.store.tts_path(tts.cache_key(self.s, voice, self.voices.ref_version(voice), lang, st.tts, retake=takes.get(str(i), 0))).exists() for st in cand_240):
                    turn_max = 145
            for st in textprep.prepare_segment(
                    i, g["v"], g["t"], lang, notes_by_seg.get(i), seg_policy, eff_gap, isent_cfg.get(lang, isent_cfg["en"]),
                    ruaccent=self.ruaccent if (lang == "ru" and self.s["stress"]["ruaccentFallback"]) else None,
                    max_turn_chars=turn_max):
                st.voice = voice
                st.key = tts.cache_key(self.s, voice, self.voices.ref_version(voice), lang, st.tts, retake=takes.get(str(i), 0))
                if native_words:
                    end = st.start + len(st.plain)
                    overlapping = [word for word in native_words if word.start < end and word.end > st.start]
                    if any(word.start < st.start or word.end > end for word in overlapping):
                        raise native_text.NativeAlignmentError("an authored native word crosses a sentence boundary")
                    st.alignment_words = tuple(native_text.Word(word.text, word.start - st.start, word.end - st.start, word.reading) for word in overlapping)
                    st.key = config.sha({"ttsKey": st.key, "nativeAlignment": native_text.VERSION,
                                         "words": [[word.text, word.start, word.end, word.reading] for word in st.alignment_words]})
                sents.append(st)
        uniq = {}
        for ch_obj in carriers:
            c_tts = textprep.sanitize_english_narrator_tts(ch_obj.text) if narr_lang == "en" else ch_obj.text
            uniq.setdefault(ch_obj.key, {"key": ch_obj.key, "voice": narr_voice, "lang": narr_lang,
                                         "text_tts": c_tts, "text_plain": ch_obj.text})
        for st in sents:
            if getattr(st, "carrier_chain", None) is not None:
                continue
            uniq.setdefault(st.key, {"key": st.key, "voice": st.voice, "lang": st.lang, "text_tts": st.tts, "text_plain": st.plain})
        return Ctx(scene, roles, rkey, sents, uniq, carriers=carriers)

    # -- step 1: synthesis ------------------------------------------------------------------------------------
    def synth(self, ctx, engine, lang=None, not_lang=None):
        """Missing sentences of the scene; `lang` / `not_lang` pick the engine's share (Russian goes to ESpeech when ttsRu is set)."""
        items = [it for it in ctx.uniq.values() if (lang is None or it["lang"] == lang) and (not_lang is None or it["lang"] != not_lang)]
        return engine.synth_many(items, self.store)

    # -- step 3: stress retakes (local, other seeds / temperatures) --------------------------------------------
    def cand_path(self, key, k):
        return self.store.tts_path(key).with_name(f"{key}.c{k}.flac")

    def marker(self, key):
        return self.store.tts_path(key).with_name(f"{key}.cands.json")

    def retake(self, ctx, engine, keys):
        import soundfile as sf
        cfg = self.s["stressRetry"]
        items = [ctx.uniq[k] for k in keys]
        bs = max(1, int(self.s["tts"]["batch"]))
        made = {k: [] for k in keys}
        for t in range(cfg["attempts"]):
            temp = cfg["temperatures"][t % len(cfg["temperatures"])]
            for i in range(0, len(items), bs):
                chunk = items[i:i + bs]
                seed = int(chunk[0]["key"][8:16], 16) + 1000 * (t + 1)
                langs = self.s["tts"]["languages"]
                wavs = engine.generate([(c["voice"], langs[c["lang"]], c["text_tts"]) for c in chunk], seed, temp)
                for c, w in zip(chunk, wavs):
                    if tts.plausible(c["text_plain"], len(w) / tts.NATIVE_SR):
                        sf.write(str(self.cand_path(c["key"], t)), w, tts.NATIVE_SR, format="FLAC", subtype="PCM_16")
                        made[c["key"]].append(t)
        for k in keys:
            self.marker(k).write_text(json.dumps({"attempts": cfg["attempts"], "made": made[k]}))
        return {"retaken": len(keys), "takes": sum(len(v) for v in made.values())}

    # -- step 2: align, check, assemble, store -----------------------------------------------------------------
    def finish(self, ctx, aligner, content_commit=None, allow_retake=True, times=None):
        """("retake", [keys]) when flagged sentences have no local retakes yet, else ("done", result)."""
        t_start = time.time()
        import soundfile as sf
        s, sents, scene, roles, voices = self.s, ctx.sents, ctx.scene, ctx.roles, self.voices
        sr = self.sr

        def evaluate(st, wav):
            clip = audio.prepare_sentence(wav, sr, s["audio"])
            if st.lang in native_text.LANGUAGES:
                ct, x16 = aligner.word_times(clip, sr, st.plain, st.lang, st.alignment_words)
                if st.lang == "ar" and ct:
                    valid_ends = [w["e"] for w in ct if isinstance(w, dict) and w.get("e") is not None]
                    if valid_ends:
                        last_e = max(valid_ends)
                        # Chatterbox T3 AlignmentStreamAnalyzer can emit 0.4..2.3s of post-sentence breath/hum/hiss
                        # before forcing EOS; crop cleanly at the quietest valley in [last_e + 45ms, last_e + 125ms].
                        if len(clip) / sr > last_e + 0.16:
                            env_a, hop_a = audio_env(x16)
                            f0 = max(0, int((last_e + 0.045) / hop_a))
                            f1 = min(len(env_a), max(f0 + 1, int((last_e + 0.125) / hop_a) + 1))
                            cut_s = (f0 + int(np.argmin(env_a[f0:f1]))) * hop_a if f1 > f0 else (last_e + 0.085)
                            cut_s = max(last_e + 0.025, cut_s)
                            cut_n = min(len(clip), max(int(0.08 * sr), int(round(cut_s * sr))))
                            clip = audio.fade(clip[:cut_n], sr, 15)
                            x16 = x16[:min(len(x16), int(round(cut_s * 16000)))]
            else:
                ct, x16 = aligner.char_times(clip, sr, st.plain, st.lang)
            return clip, ct, x16, self.check(st, ct)

        first = {}
        for st in sents:
            if getattr(st, "carrier_chain", None) is None:
                first.setdefault(st.key, st)
        best = {}
        for key, st in first.items():
            wav = tts.load_wav(self.store.tts_path(key))[0]
            clip, ct, x16, ck = evaluate(st, wav)
            best[key] = {"bad": self.badness(ck), "wav": wav, "clip": clip, "ct": ct, "x16": x16, "ck": ck, "take": 0}

        # Slice continuous narrator carrier waveforms cleanly at MMS_FA acoustic energy valleys around 'phrase' slots
        carrier_aligned = {}
        for ch_obj in getattr(ctx, "carriers", []):
            if ch_obj.key not in carrier_aligned:
                c_wav = tts.load_wav(self.store.tts_path(ch_obj.key))[0]
                c_clip = audio.prepare_sentence(c_wav, sr, s["audio"])
                c_ct, c_x16 = aligner.char_times(c_clip, sr, ch_obj.text, "en")
                c_env, c_hop = audio_env(c_x16)
                carrier_aligned[ch_obj.key] = (c_clip, c_ct, c_x16, c_env, c_hop)
            c_clip, c_ct, c_x16, c_env, c_hop = carrier_aligned[ch_obj.key]
            dur_c = len(c_clip) / sr

            for k_seg, cmap in ch_obj.char_maps.items():
                part_key = f"{ch_obj.key}__part_{k_seg}"
                orig_t = scene.script["segments"][k_seg]["t"]
                valid_mi = [mi for mi in cmap if mi is not None and mi < len(c_ct) and c_ct[mi] is not None]
                if not seg_tokens(orig_t):
                    sil_clip = np.zeros(int(0.025 * sr), dtype=np.float32)
                    sil_16 = np.zeros(int(0.025 * 16000), dtype=np.float32)
                    best[part_key] = {"bad": (0, 0.0), "wav": sil_clip, "clip": sil_clip,
                                      "ct": [None] * len(orig_t), "x16": sil_16, "ck": [], "take": 0}
                    continue
                if not valid_mi:
                    # Rare CTC fallback: proportional slice across carrier duration
                    n_parts = max(1, len(ch_obj.char_maps))
                    rank = sorted(ch_obj.char_maps).index(k_seg)
                    s_sec = dur_c * rank / n_parts
                    e_sec = max(s_sec + 0.06, dur_c * (rank + 1) / n_parts)
                else:
                    min_mi, max_mi = min(valid_mi), max(valid_mi)
                    raw_s = min(c_ct[mi][0] for mi in valid_mi)
                    raw_e = max(c_ct[mi][1] for mi in valid_mi)
                    prev_hits = [c_ct[p][1] for p in range(0, min_mi) if p < len(c_ct) and c_ct[p] is not None]
                    next_hits = [c_ct[p][0] for p in range(max_mi + 1, len(c_ct)) if c_ct[p] is not None]

                    if k_seg == ch_obj.a:
                        s_sec = 0.0
                    else:
                        prev_e = max(prev_hits) if prev_hits else 0.0
                        lo_s = max(0.0, min(raw_s, max(prev_e + 0.014, raw_s - 0.024)))
                        f0 = max(0, int(lo_s / c_hop))
                        f1 = min(len(c_env), max(f0 + 1, int(raw_s / c_hop) + 1))
                        s_sec = (f0 + int(np.argmin(c_env[f0:f1]))) * c_hop if f1 > f0 else lo_s

                    if k_seg == ch_obj.b:
                        e_sec = dur_c
                    elif next_hits:
                        next_s = min(next_hits)
                        if next_s - raw_e <= 0.18:
                            # Continuous speech into 'name': MMS_FA next_s ('n' CTC spike) fires ~40 ms after oral->nasal
                            # closure; cutting in [next_s - 46ms, next_s - 38ms] keeps the full English vowel with zero '/n/' murmur.
                            lo_e = min(max(raw_e + 0.012, next_s - 0.046), max(raw_e, next_s - 0.036))
                            hi_e = max(lo_e, next_s - 0.038)
                        else:
                            # Prosodic comma/sentence pause before 'name': let final phoneme/plosive finish (~95..220 ms) and cut in silence.
                            lo_e = min(next_s - 0.030, raw_e + 0.095)
                            hi_e = max(lo_e, min(next_s - 0.030, raw_e + 0.220))
                        f0 = max(0, int(lo_e / c_hop))
                        f1 = min(len(c_env), max(f0 + 1, int(hi_e / c_hop) + 1))
                        e_sec = (f0 + int(np.argmin(c_env[f0:f1]))) * c_hop if f1 > f0 else hi_e
                    else:
                        e_sec = dur_c

                    if e_sec < s_sec + 0.045:
                        e_sec = min(dur_c, s_sec + 0.045)

                i0, i1 = max(0, int(round(s_sec * sr))), min(len(c_clip), int(round(e_sec * sr)))
                if i1 <= i0:
                    i1 = min(len(c_clip), i0 + int(0.045 * sr))
                # De-shush guard on resumed segments: if the resumed English word does not begin with a fricative/sibilant,
                # advance i0 past any residual high-ZCR unvoiced hiss frames (< 60 ms) at the cut boundary.
                lead_word = orig_t.lstrip(" '\",;:—–-(").lower()
                if k_seg > ch_obj.a and lead_word and lead_word[0] not in "scfhzwvtp" and (i1 - i0) > int(0.10 * sr):
                    step_n = max(1, int(0.008 * sr))
                    seg_pk = float(np.abs(c_clip[i0:i1]).max()) + 1e-8
                    max_trim = i0 + int(0.056 * sr)
                    while i0 + step_n < min(max_trim, i1 - int(0.05 * sr)):
                        fr = c_clip[i0:i0 + step_n]
                        zcr = float(np.mean(fr[:-1] * fr[1:] < 0)) if len(fr) > 1 else 0.0
                        if zcr > 0.20 and float(np.sqrt(np.mean(fr * fr))) < seg_pk * 0.25:
                            i0 += step_n
                        else:
                            break
                    s_sec = i0 / sr
                part_clip = audio.fade(c_clip[i0:i1], sr, 7)
                part_dur = len(part_clip) / sr
                j0, j1 = max(0, int(round(s_sec * 16000))), min(len(c_x16), int(round(e_sec * 16000)))
                part_x16 = c_x16[j0:j1] if j1 > j0 else np.zeros(int(0.045 * 16000), dtype=np.float32)

                part_ct = [None] * len(orig_t)
                for ci, mi in enumerate(cmap):
                    if mi is not None and mi < len(c_ct) and c_ct[mi] is not None:
                        ca = max(0.0, min(part_dur, c_ct[mi][0] - s_sec))
                        cb = max(ca, min(part_dur, c_ct[mi][1] - s_sec))
                        part_ct[ci] = (ca, cb)

                best[part_key] = {"bad": (0, 0.0), "wav": part_clip, "clip": part_clip,
                                  "ct": part_ct, "x16": part_x16, "ck": [], "take": 0}

        # New Retake Stats Aggregation from .gates.json (created by synth_many gates)
        retake = {"sentences": [], "takes": 0, "retakes": 0, "length": 0, "repeat": 0, "transient": 0, "similarity": 0, "cer": 0}
        seen_gate_keys = set(first.keys()) | {ch.key for ch in getattr(ctx, "carriers", [])}
        for key in seen_gate_keys:
            if self.store.tts_path(key).with_name(f"{key}.gates.json").exists():
                try:
                    counts = json.loads(self.store.tts_path(key).with_name(f"{key}.gates.json").read_text())
                    if "takes" in counts:
                        retake["takes"] += counts.get("takes", 0)
                        retake["retakes"] += counts.get("retakes", 0)
                        retake["length"] += counts.get("length", 0)
                        retake["repeat"] += counts.get("repeat", 0)
                        retake["transient"] += counts.get("transient", 0)
                        retake["similarity"] += counts.get("similarity", 0)
                        retake["cer"] += counts.get("cer", 0)
                except Exception:
                    pass

        flagged_keys = [k for k, b in best.items() if b["bad"][0] > 0]
        # Legacy retake marker handling (if any fallback)
        need = [k for k in flagged_keys if not self.marker(k).exists()]
        if need and allow_retake and s["stressRetry"]["attempts"] > 0:
            return "retake", need
            
        for key in flagged_keys:
            st, b = first[key], best[key]
            made = []
            if self.store.tts_path(key).with_name(f"{key}.gates.json").exists():
                try:
                    cands = json.loads(self.store.tts_path(key).with_name(f"{key}.gates.json").read_text())
                    made = cands.get("made", [])
                except:
                    made = []
            for t in made:
                p = self.cand_path(key, t)
                if not p.exists():
                    continue
                w = tts.load_wav(p)[0]
                clip, ct, x16, ck = evaluate(st, w)
                bad = self.badness(ck)
                if bad < b["bad"]:
                    b.update(bad=bad, wav=w, clip=clip, ct=ct, x16=x16, ck=ck, take=t + 1)
            if b["take"]:   # keep the better take for good
                cp = self.store.tts_path(key)
                tmpf = cp.with_suffix(".tmp.flac")
                sf.write(str(tmpf), b["wav"], tts.NATIVE_SR, format="FLAC", subtype="PCM_16")
                tmpf.replace(cp)
            retake["sentences"].append({"seg": st.seg, "idx": st.idx, "text": st.plain, "takesTried": len(made),
                                        "bestTake": b["take"], "stillFlagged": b["bad"][0] > 0})
            for t in made:
                self.cand_path(key, t).unlink(missing_ok=True)

        warnings = [f"voice {k} is shared by roles {rs} in this scene" for k, rs in voice_clashes(roles).items()]
        clips = [best[st.key]["clip"] for st in sents]
        checks = {n: best[st.key]["ck"] for n, st in enumerate(sents)}
        x16s = {n: best[st.key]["x16"] for n, st in enumerate(sents)}
        char_times = {n: best[st.key]["ct"] for n, st in enumerate(sents)}
        flagged_first = len(flagged_keys)
        t_align = time.time() - t_start

        lines = {}
        for st, x in zip(sents, clips):
            lines.setdefault(st.seg, []).append((x, st.gap))
        sig, lay = audio.assemble([lines[k] for k in sorted(lines)], sr, s["audio"])
        sig, gain, measured = audio.master(sig, sr, s["audio"])
        tmp = self.store.root / f".{scene.id}.{int(time.time())}.mp3"
        audio.encode_mp3(sig, sr, tmp, s["audio"]["mp3Kbps"])
        dur_mp3 = audio.mp3_duration(tmp, sr)
        duration = len(sig) / sr

        spans_segments, timing = [], {}
        by_seg = {}
        for n, st in enumerate(sents):
            by_seg.setdefault(st.seg, []).append(n)
        notes_by_seg = {l["seg"]: l.get("words") or [] for l in scene.notes.get("lines", []) if isinstance(l, dict)}
        timing_bad = 0
        for si, g in enumerate(scene.script["segments"]):
            start, end, nxt, sent_spans = lay[si]
            ids = by_seg[si]
            native = sents[ids[0]].lang in native_text.LANGUAGES
            units = native_text.words_for_segment(g["t"], notes_by_seg.get(si), sents[ids[0]].lang) if native else ()
            toks = [word.text for word in units] if native else seg_tokens(g["t"], notes_by_seg.get(si))
            tspans = [(word.start, word.end) for word in units] if native else textprep.token_spans(g["t"], toks)
            words = [None] * len(toks)
            for n, (a, b) in zip(ids, sent_spans):
                st = sents[n]
                idx = [j for j, sp in enumerate(tspans) if sp is not None and st.start <= sp[0] < st.start + len(st.plain)]
                if not idx:
                    continue
                rel = [(tspans[j][0] - st.start, tspans[j][1] - st.start) for j in idx]
                if native:
                    wt = char_times[n]
                    if len(wt) != len(idx) or any(not word["ok"] for word in wt):
                        raise native_text.NativeAlignmentError("incomplete native acoustic word alignment; interpolation is forbidden")
                else:
                    env, hop = audio_env(x16s[n])
                    wt = align_words(char_times[n], rel, env, hop, s["align"]["snapMaxMs"])
                seg_s_r, seg_e_r = round(start, 3), round(end, 3)
                for j, w in zip(idx, wt):
                    ws = max(seg_s_r, min(seg_e_r, round(a + w["s"], 3)))
                    we = max(ws, min(seg_e_r, round(a + w["e"], 3)))
                    words[j] = {"t": toks[j], "s": ws, "e": we, "ok": w["ok"], "why": w["why"]}
                    if native:
                        words[j].update(span=list(tspans[j]), confidence=w["confidence"], alignment=native_text.VERSION)
            seg_s_r, seg_e_r = round(start, 3), round(end, 3)
            prev = seg_s_r
            for j, w in enumerate(words):
                if w is None:
                    if native:
                        raise native_text.NativeAlignmentError("missing native word timing; interpolation is forbidden")
                    words[j] = {"t": toks[j], "s": round(prev, 3), "e": round(prev, 3), "ok": False, "why": "missing"}
                else:
                    w["s"] = max(prev, min(seg_e_r, w["s"]))
                    w["e"] = max(w["s"], min(seg_e_r, w["e"]))
                prev = words[j]["e"]
            timing_bad += sum(1 for w in words if not w["ok"])
            timing[str(si)] = words

            # Derive fine per-sentence (start, end) spans inside merged whole-turn chunks from MMS_FA word timestamps
            sub_sents = textprep.split_sentences(g["t"])
            eng_lbl = config.engine_label(s, sents[ids[0]].lang)
            if len(sub_sents) == len(ids):
                fine_sentences = [{"i": sents[n].idx, "start": round(a, 3), "end": round(b, 3), "text": sents[n].plain,
                                   "engine": eng_lbl} for n, (a, b) in zip(ids, sent_spans)]
            else:
                fine_sentences = []
                cur_s = start
                for sk, (sa, sb, stext) in enumerate(sub_sents):
                    sw = [words[j] for j, sp in enumerate(tspans) if sp is not None and sa <= sp[0] < sb and words[j] is not None and words[j]["e"] > words[j]["s"]]
                    if sk == 0:
                        s_a = start
                    elif sw:
                        s_a = max(cur_s, sw[0]["s"])
                    else:
                        s_a = cur_s
                    if sk == len(sub_sents) - 1:
                        s_b = end
                    elif sw:
                        s_b = min(end, max(s_a + 0.01, sw[-1]["e"]))
                    else:
                        s_b = min(end, s_a + max(0.05, (end - cur_s) / (len(sub_sents) - sk)))
                    cur_s = s_b
                    fine_sentences.append({"i": sk, "start": round(s_a, 3), "end": round(s_b, 3), "text": stext, "engine": eng_lbl})

            spans_segments.append({
                "seg": si, "v": g["v"], "voice": roles[g["v"]], "lang": sents[ids[0]].lang,
                "start": round(start, 3), "end": round(end, 3), "nextStart": round(nxt, 3),
                "sentences": fine_sentences})

        still = []
        checked = flagged_words = 0
        for n, c in checks.items():
            checked += len(c)
            flagged_words += sum(w["flag"] for w in c)
            if any(w["flag"] for w in c):
                still.append({"seg": sents[n].seg, "idx": sents[n].idx, "text": sents[n].plain, "words": [w for w in c if w["flag"]]})
        ru_sents = [n for n, st in enumerate(sents) if st.lang == "ru" and st.role != "narrator"]
        uniq_still = {x["text"] for x in still}
        report = {
            "version": 1, "sceneId": scene.id,
            "stress": {"policy": self.policy, "scope": s["stressCheck"]["scope"], "ratio": s["stressCheck"]["ratio"],
                       "russianSentences": len(ru_sents), "wordsChecked": checked, "wordsFlagged": flagged_words,
                       "sentencesFlaggedInitially": flagged_first, "stillFlagged": len(uniq_still),
                       "flaggedRatio": round(flagged_first / max(1, len({sents[n].key for n in ru_sents})), 4),
                       "unresolved": still,
                       "missingMarks": [{"seg": st.seg, "idx": st.idx, "tokens": st.missing} for st in sents if st.missing]},
            "retake": retake,
            "tts": {"sentences": len(sents), "unique": len(ctx.uniq)},
            "timing": {"tokens": sum(len(v) for v in timing.values()), "notOk": timing_bad},
            "audio": {"seconds": round(duration, 3), "mp3Seconds": round(dur_mp3, 3), "programLufsBefore": round(measured, 2),
                      "gainDb": round(gain, 2)},
            "warnings": warnings,
        }
        spans = {"version": 1, "sceneId": scene.id, "sampleRate": sr, "durationSec": round(duration, 3), "segs": spans_segments}
        timing_doc = timing          # publisher shape: {"<seg>": [{t, s, e, ok, why}]}, nothing else at the top level
        jb = lambda o: (json.dumps(o, ensure_ascii=False, sort_keys=True, indent=1) + "\n").encode("utf-8")
        spans_b, timing_b, report_b = jb(spans), jb(timing_doc), jb(report)
        times = times or {}
        meta = {
            "sceneId": scene.id, "renderKey": ctx.rkey, "contentHash": scene.content_hash, "contentCommit": content_commit,
            **({"nativeAlignment": native_text.VERSION} if scene.lang in native_text.LANGUAGES else {}),
            "pipelineVersion": config.PIPELINE_VERSION, "renderVersion": s["renderVersion"],
            "tts": {"model": (f"{config.engine_label(s, 'ar')}+{config.engine_label(s, 'en')}" if scene.lang == "ar" and config.ar_engine(s) else s["tts"]["model"]),
                    "lora": (s["lora"]["tag"] if s["lora"]["enabled"] else None), "stressPolicy": self.policy, "gen": config.tts_signature(s)["gen"],
                    **({"nativeEngine": config.engine_label(s, scene.lang)} if scene.lang in native_text.LANGUAGES else {}),
                    **({"nativeGen": {key: value for key, value in config.ar_engine(s).items() if key in ("temperature", "cfg_weight", "exaggeration", "repetition_penalty", "min_p", "top_p")}} if scene.lang == "ar" and config.ar_engine(s) else {})},
            "voicesVersion": voices.voices_version(),
            "voices": {r: {"voice": k, "refVersion": voices.ref_version(k)} for r, k in sorted(roles.items())},
            "align": f"mms_fa/{s['align']['version']}",
            "renderedAt": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "durationSec": round(duration, 3), "sampleRate": sr, "bitrateKbps": s["audio"]["mp3Kbps"],
            "audioSha256": sha256_file(tmp), "audioBytes": tmp.stat().st_size,
            "spansSha256": config.sha(spans_b), "timingSha256": config.sha(timing_b),
            "wall": {"total": round(times.get("synth", 0) + times.get("retake", 0) + time.time() - t_start, 2),
                     "tts": round(times.get("synth", 0) + times.get("retake", 0), 2), "align": round(time.time() - t_start, 2)},
        }
        self.store.commit_scene(scene.id, {"audio.mp3": tmp, "spans.json": spans_b, "timing.json": timing_b,
                                           "report.json": report_b, "meta.json": jb(meta)})
        tmp.unlink(missing_ok=True)
        return "done", {"sceneId": scene.id, "renderKey": ctx.rkey, "audioSec": duration, "wallSec": meta["wall"]["total"],
                        "ttsSec": meta["wall"]["tts"], "generatedSec": times.get("generatedSec", 0.0),
                        "generated": times.get("generated", 0), "cached": times.get("cached", 0),
                        "flagged": flagged_first, "stillFlagged": len(uniq_still), "russian": len(ru_sents), "timingNotOk": timing_bad}

    @staticmethod
    def badness(ck):
        """(flagged words, worst off-ratio): lower is better."""
        fl = [w for w in ck if w["flag"]]
        return (len(fl), max([w["ratio"] for w in fl], default=0.0))

    def check(self, st, char_times):
        if st.lang != "ru" or st.role == "narrator" or not st.expected:
            return []
        return stresscheck.check_sentence(st.plain, st.expected, char_times, self.s["stressCheck"]["scope"], self.s["stressCheck"]["ratio"])


def audio_env(x16):
    from align import envelope
    return envelope(x16)


def align_words(char_times, spans, env, hop, snap_ms):
    from align import words_from_chars
    return words_from_chars(char_times, spans, env, hop, snap_ms)
