import numpy as np
import soundfile as sf
import torch
import librosa
from faster_whisper import WhisperModel
import os
import scipy.signal

class AudioGates:
    def __init__(self):
        # We need whisper for repeat check and CER
        self.whisper = WhisperModel("large-v3-turbo", device="cuda", compute_type="float16", local_files_only=True)
        
        # We need WavLM for speaker similarity
        from transformers import AutoFeatureExtractor, AutoModelForAudioXVector
        self.extractor = AutoFeatureExtractor.from_pretrained("microsoft/wavlm-base-plus-sv", local_files_only=True)
        self.spk_model = AutoModelForAudioXVector.from_pretrained("microsoft/wavlm-base-plus-sv", local_files_only=True).to("cuda")
        self.spk_model.eval()
        self.ref_embeddings = {}

    def get_embedding(self, wav, sr):
        if sr != 16000:
            wav_16k = librosa.resample(wav, orig_sr=sr, target_sr=16000)
        else:
            wav_16k = wav
        if len(wav_16k) < 8000:
            wav_16k = np.pad(wav_16k, (0, 8000 - len(wav_16k)))
        inputs = self.extractor(wav_16k, return_tensors="pt", sampling_rate=16000).to("cuda")
        with torch.no_grad(), torch.backends.cudnn.flags(enabled=False):
            emb = self.spk_model(**inputs).embeddings
        return torch.nn.functional.normalize(emb, dim=-1).squeeze()

    def get_embeddings_batch(self, wavs_16k):
        """Batched 16 kHz WavLM speaker embeddings (identical math to get_embedding, ~5x faster on sliding windows)."""
        padded = [np.pad(w, (0, 8000 - len(w))) if len(w) < 8000 else w for w in wavs_16k]
        inputs = self.extractor(padded, return_tensors="pt", sampling_rate=16000, padding=True).to("cuda")
        with torch.no_grad(), torch.backends.cudnn.flags(enabled=False):
            embs = self.spk_model(**inputs).embeddings
        return torch.nn.functional.normalize(embs, dim=-1)

    @staticmethod
    def _en_expand_digits(s: str) -> str:
        """Expand integer numerals (e.g. '20,000' -> 'twenty thousand', '12' -> 'twelve') so Whisper digit formatting never triggers false CER retries."""
        import re
        ones = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
                "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
        tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

        def _under_1000(n: int) -> str:
            parts = []
            if n >= 100:
                parts.append(ones[n // 100] + " hundred")
                n %= 100
            if n >= 20:
                w = tens[n // 10]
                if n % 10:
                    w += " " + ones[n % 10]
                parts.append(w)
            elif n > 0 or not parts:
                parts.append(ones[n])
            return " ".join(parts)

        def _num(m):
            raw = m.group(0).replace(",", "")
            if not raw.isdigit() or len(raw) > 7:
                return m.group(0)
            n = int(raw)
            if n == 0:
                return "zero"
            out = []
            if n >= 1_000_000:
                out.append(_under_1000(n // 1_000_000) + " million")
                n %= 1_000_000
            if n >= 1000:
                out.append(_under_1000(n // 1000) + " thousand")
                n %= 1000
            if n > 0:
                out.append(_under_1000(n))
            return " ".join(out)

        return re.sub(r"\b\d{1,3}(?:,\d{3})+\b|\b\d+\b", _num, s)

    def check_similarity(self, wav, sr, ref_path, threshold=0.65):
        ref_path = str(ref_path)
        if ref_path not in self.ref_embeddings:
            ref_wav, ref_sr = sf.read(ref_path)
            self.ref_embeddings[ref_path] = self.get_embedding(ref_wav, ref_sr)
        emb = self.get_embedding(wav, sr)
        cos = torch.nn.functional.cosine_similarity(emb, self.ref_embeddings[ref_path], dim=0).item()
        return cos >= threshold, cos

    @staticmethod
    def _count_internal_breaks(t_strip: str) -> int:
        if len(t_strip) <= 2:
            return 0
        import re
        body = t_strip[:-1]
        # Match sentence boundaries even when followed by closing quotes/parens (e.g. ".' ", '?" ')
        return len(re.findall(r"[.!?…।。！？؟]['\"”’)\]]*\s+", body))

    def check_length_pause(self, wav, sr, text, lang, max_pause=0.72, len_mult=1.40):
        median_spc = 0.20 if lang in ["ja", "zh", "ko"] else 0.088
        t_strip = text.strip()
        n_internal_sents = self._count_internal_breaks(t_strip)
        n_clauses = sum(t_strip.count(c) for c in (",", ";", ":", "—", "–"))
        expected = max(0.85, len(t_strip) * median_spc + 0.45 + 0.55 * n_internal_sents + 0.18 * n_clauses)

        has_alnum = any(c.isalnum() for c in t_strip)
        if has_alnum:
            if len(wav) < int(sr * 0.12) or float(np.abs(wav).max()) < 0.015:
                return False, "length"
            abs_idx = np.where(np.abs(wav) > (10.0 ** (-50.0 / 20.0)))[0]
            if len(abs_idx) == 0 or (abs_idx[-1] - abs_idx[0]) / sr < 0.06:
                return False, "length"

        frame_len = int(sr * 0.05)
        hop_len = int(sr * 0.01)
        if len(wav) < frame_len:
            return (not has_alnum and len(wav) / sr <= expected * len_mult), ("ok" if (not has_alnum and len(wav) / sr <= expected * len_mult) else "length")
        rms = librosa.feature.rms(y=wav, frame_length=frame_len, hop_length=hop_len)[0]
        silence_thresh = rms.max() * 0.05
        is_silence = rms < silence_thresh

        non_sil = np.where(~is_silence)[0]
        if len(non_sil) == 0:
            return (not has_alnum), ("ok" if not has_alnum else "length")

        speech_dur = (non_sil[-1] - non_sil[0] + 1) * hop_len / sr
        if speech_dur > expected * len_mult:
            return False, "length"

        if lang == "ru" and has_alnum and len(wav) >= int(sr * 0.25):
            head_rms = float(np.sqrt(np.mean(wav[:int(0.020 * sr)] ** 2)))
            tail_sil_s = (len(rms) - 1 - int(non_sil[-1])) * hop_len / sr
            if head_rms > 0.009 or tail_sil_s < 0.045:
                return False, "length"

        is_silence_speech = is_silence[non_sil[0]:non_sil[-1]+1]

        max_sil_frames = 0
        cur_sil = 0
        for s in is_silence_speech:
            if s:
                cur_sil += 1
                if cur_sil > max_sil_frames:
                    max_sil_frames = cur_sil
            else:
                cur_sil = 0

        max_pause_sec = max_sil_frames * hop_len / sr
        eff_max_pause = 1.25 if n_internal_sents > 0 else (0.92 if n_clauses > 0 else max_pause)
        if max_pause_sec > eff_max_pause:
            return False, "pause"

        return True, "ok"

    def check_repeat_and_cer(self, wav, sr, text, lang):
        if sr != 16000:
            wav_16k = librosa.resample(wav, orig_sr=sr, target_sr=16000)
        else:
            wav_16k = wav
        wav_16k = wav_16k.astype(np.float32)
        import re
        segs, info = self.whisper.transcribe(wav_16k, language=lang, beam_size=1, word_timestamps=False, condition_on_previous_text=False)
        hyp_text = " ".join(s.text for s in segs).strip()
        words = re.findall(r"\w+", hyp_text.lower())
                    
        # Repeat check
        for i in range(len(words)-1):
            if words[i] == words[i+1] and len(words[i]) > 1:
                t_lower = text.lower()
                if t_lower.count(words[i]) < 2:
                    return False, "repeat", hyp_text.strip()
                    
        # CER calculation using JiWER
        import jiwer
        def norm(s):
            import re
            return re.sub(r'[\W_]+', ' ', s.lower()).strip()
        ref_norm = norm(text)
        hyp_norm = norm(hyp_text)
        if not ref_norm: return True, "ok", hyp_text.strip()
        cer = jiwer.cer(ref_norm, hyp_norm)
        return True, cer, hyp_text.strip()

    def check_transient(self, wav, sr, n_internal_sents=0, text_len=100):
        hop = int(sr * 0.01)
        if len(wav) < hop * 4:
            return True, "ok", wav

        rms = librosa.feature.rms(y=wav, frame_length=hop * 2, hop_length=hop)[0]
        pk_rms = float(rms.max()) if len(rms) > 0 else 0.0
        if pk_rms <= 1e-6:
            return True, "ok", wav

        silence_thresh = max(10.0 ** (-44.0 / 20.0), pk_rms * 0.06)
        speech_rms = rms[rms >= silence_thresh]
        if len(speech_rms) == 0:
            return True, "ok", wav
        med_speech_rms = float(np.median(speech_rms))
        if med_speech_rms <= 1e-6:
            return True, "ok", wav

        # 1. Detect active speech islands; strip short (< 220 ms) post-silence EOS pops/bangs and reject (>= 220 ms) babble
        act = rms >= max(silence_thresh, med_speech_rms * 0.10)
        islands = []
        i = 0
        while i < len(act):
            if act[i]:
                j = i + 1
                while j < len(act) and act[j]:
                    j += 1
                islands.append((i, j))
                i = j
            else:
                i += 1

        if len(islands) >= 2:
            prev_s, prev_e = islands[-2]
            last_s, last_e = islands[-1]
            gap_ms = (last_s - prev_e) * 10
            tail_ms = (last_e - last_s) * 10
            main_ms = (islands[-2][1] - islands[0][0]) * 10
            tail_pk = float(rms[last_s:last_e].max()) if last_e > last_s else 0.0
            if main_ms >= 100 and gap_ms >= 320 and tail_ms <= 55 and tail_pk < pk_rms * 0.25:
                cut_sample = min(len(wav), (prev_e + 2) * hop)
                wav = wav[:cut_sample]
                rms = rms[:prev_e + 2]
                islands.pop()
            elif n_internal_sents == 0 and text_len <= 22 and main_ms >= 100 and gap_ms >= 520 and tail_ms > 220:
                # Very short 1-2 word callout followed by >0.5s dead silence and extra hallucinated babble (e.g. F5 bleed)
                return False, "transient", wav

        # Strip only tiny (<= 70 ms), very quiet (< 0.18x pk) isolated pre-speech clicks separated by >= 240 ms silence
        # (never touch 40..110 ms voiceless stop closures inside initial clusters like Ст-, Чт-, Кт-, St-, Sp-, Sk-!)
        if len(islands) >= 2:
            first_s, first_e = islands[0]
            next_s, _ = islands[1]
            first_pk = float(rms[first_s:first_e].max()) if first_e > first_s else 0.0
            if (first_e - first_s) * 10 <= 70 and (next_s - first_e) * 10 >= 240 and first_pk < pk_rms * 0.18:
                cut_start = max(0, (next_s - 2) * hop)
                wav = wav[cut_start:]
                rms = librosa.feature.rms(y=wav, frame_length=hop * 2, hop_length=hop)[0]

        if len(wav) < hop * 4 or len(rms) == 0:
            return False, "transient", wav

        # 2. Check 10 ms broadband & < 150 Hz low-frequency bursts against median active speech RMS
        speech_idx = np.where(rms >= max(10.0 ** (-44.0 / 20.0), float(rms.max()) * 0.06))[0]
        if len(speech_idx) == 0:
            return False, "transient", wav
        med_rms = float(np.median(rms[speech_idx]))
        b, a = scipy.signal.butter(4, 150, btype="lowpass", fs=sr)
        wav_low = scipy.signal.filtfilt(b, a, wav)
        rms_low = librosa.feature.rms(y=wav_low, frame_length=hop * 2, hop_length=hop)[0]

        f0_i, f1_i = int(speech_idx[0]), int(speech_idx[-1])
        for idx_f in range(f0_i, min(len(rms), len(rms_low), f1_i + 1)):
            r, rl = float(rms[idx_f]), float(rms_low[idx_f])
            near_edge = (idx_f - f0_i) <= 10 or (f1_i - idx_f) <= 20   # first 100 ms or last 200 ms of active speech
            if near_edge and (r > med_rms * 4.2 or rl > med_rms * 2.5):
                return False, "transient", wav
            if r > med_rms * 5.2 or rl > med_rms * 3.2:
                return False, "transient", wav

        return True, "ok", wav

    def check_prosody(self, wav, sr):
        """Measure voiced F0 standard deviation (Hz); prefer natural expressive range 18-45 Hz over flat monotone."""
        if len(wav) < int(sr * 0.35):
            return 25.0, 0.0
        wav_16k = librosa.resample(wav, orig_sr=sr, target_sr=16000) if sr != 16000 else wav
        rms = librosa.feature.rms(y=wav_16k, frame_length=1024, hop_length=256)[0]
        if len(rms) == 0 or rms.max() <= 1e-6:
            return 0.0, 1.0
        f0 = librosa.yin(wav_16k.astype(np.float32), fmin=65, fmax=420, sr=16000, frame_length=1024, hop_length=256)
        n = min(len(rms), len(f0))
        voiced = f0[:n][(rms[:n] >= rms.max() * 0.08) & (f0[:n] >= 70.0) & (f0[:n] <= 390.0)]
        if len(voiced) < 5:
            return 25.0, 0.0
        f0_std = float(np.std(voiced))
        if 18.0 <= f0_std <= 45.0:
            return f0_std, 0.0
        dist = (18.0 - f0_std) if f0_std < 18.0 else (f0_std - 45.0)
        return f0_std, round(min(1.0, dist / 45.0), 4)

    def score_candidates(self, wavs, sr, ref_path, text_plain, lang, cpu_pool=None, beam_size=3, need_fallback=True):
        """Score N candidate takes through all 5 §6 gates + F0 prosody tie-breaker.
        Returns (best_wav, all_ok, counts_dict, best_meta)."""
        t_strip = text_plain.strip()
        n_int_sents = self._count_internal_breaks(t_strip)
        def _cpu_prep(w):
            tran_ok, tran_reason, w_trim = self.check_transient(w, sr, n_internal_sents=n_int_sents, text_len=len(t_strip))
            len_ok, len_reason = self.check_length_pause(w_trim, sr, text_plain, lang)
            w_16k = (librosa.resample(w_trim, orig_sr=sr, target_sr=16000) if sr != 16000 else w_trim).astype(np.float32)
            f0_std, pros_pen = self.check_prosody(w_16k, 16000)
            pitch_ok = True
            if lang == "en" and len(w_16k) >= 5600:
                f0_y = librosa.yin(w_16k, fmin=75, fmax=380, sr=16000, frame_length=1024, hop_length=512)
                rms_y = librosa.feature.rms(y=w_16k, frame_length=1024, hop_length=512)[0]
                ny = min(len(f0_y), len(rms_y))
                v_f0 = f0_y[:ny][(rms_y[:ny] >= rms_y.max() * 0.10) & (f0_y[:ny] > 80.0) & (f0_y[:ny] < 360.0)]
                if len(v_f0) >= 6:
                    med_f0 = float(np.median(v_f0))
                    if med_f0 < 165.0 or med_f0 > 226.0:
                        pitch_ok = False
            return len_ok, len_reason, tran_ok, tran_reason, w_trim, w_16k, f0_std, pros_pen, pitch_ok

        if cpu_pool is not None and len(wavs) > 1:
            prepped = list(cpu_pool.map(_cpu_prep, wavs))
        else:
            prepped = [_cpu_prep(w) for w in wavs]

        import jiwer, re
        raw_ref_str = self._en_expand_digits(text_plain) if lang == "en" else text_plain
        ref_norm = re.sub(r"[\W_]+", " ", raw_ref_str.lower()).strip()
        # Identify capitalized proper-noun tokens in English text (excluding basic sentence starters)
        _COMMON_EN_CAPS = {
            "i", "the", "a", "an", "and", "but", "or", "so", "if", "when", "what", "why", "how", "where", "who",
            "yes", "no", "well", "oh", "hey", "wait", "look", "listen", "now", "here", "there", "this", "that",
            "these", "those", "he", "she", "it", "we", "they", "you", "my", "your", "his", "her", "our", "their",
            "is", "are", "was", "were", "do", "does", "did", "can", "could", "will", "would", "should", "let",
            "please", "thank", "thanks", "hello", "hi", "good", "great", "fine", "okay", "sure", "maybe", "just",
            "don", "didn", "can", "won", "isn", "aren", "wasn", "tell", "give", "take", "come", "go", "stop",
        }
        en_proper_set = set()
        if lang == "en":
            for tok in re.findall(r"[A-Za-z]+", text_plain):
                if tok[0].isupper() and len(tok) >= 3 and tok.lower() not in _COMMON_EN_CAPS:
                    en_proper_set.add(tok.lower())

        ref_path = str(ref_path)
        if ref_path not in self.ref_embeddings:
            ref_wav, ref_sr = sf.read(ref_path)
            if ref_wav.ndim > 1:
                ref_wav = ref_wav.mean(axis=1)
            self.ref_embeddings[ref_path] = self.get_embedding(ref_wav, ref_sr)

        def _run_asr(w_16k, sim_val):
            segs_list = list(self.whisper.transcribe(
                w_16k, language=lang, beam_size=1,
                word_timestamps=(lang in ("en", "pt", "es", "fr", "it", "de", "ru")),
                condition_on_previous_text=False,
            )[0])
            hyp_text = " ".join(s.text for s in segs_list).strip()
            w_objs = [wo for s in segs_list for wo in (s.words or [])]
            words = re.findall(r"\w+", hyp_text.lower())
            rep_ok = True
            t_lower = raw_ref_str.lower()
            for wi in range(len(words) - 1):
                if words[wi] == words[wi + 1] and len(words[wi]) > 1 and t_lower.count(words[wi]) < 2:
                    rep_ok = False
                    break
            raw_hyp_str = self._en_expand_digits(hyp_text) if lang == "en" else hyp_text
            hyp_norm = re.sub(r"[\W_]+", " ", raw_hyp_str.lower()).strip()
            cer_val = float(jiwer.cer(ref_norm, hyp_norm)) if ref_norm else 0.0
            edge_ok = True
            if lang in ("en", "pt", "es", "fr", "it", "de", "ru"):
                import unicodedata
                _COLLOQ = {"to": "estou", "ta": "esta", "pra": "para", "pro": "para"}
                def _fold_acc(s):
                    return "".join(c for c in unicodedata.normalize("NFKD", s) if not unicodedata.combining(c))
                ref_w = [_COLLOQ.get(w, w) for w in re.findall(r"[^\W_]+", _fold_acc(ref_norm))]
                hyp_w = [_COLLOQ.get(w, w) for w in re.findall(r"[^\W_]+", _fold_acc(hyp_norm))]
                if len(ref_w) >= 2:
                    if not hyp_w:
                        edge_ok = False
                    else:
                        for is_last, (rw, hw) in enumerate(((ref_w[0], hyp_w[0]), (ref_w[-1], hyp_w[-1]))):
                            if any(ch.isdigit() for ch in rw):
                                continue
                            if lang == "en" and rw in en_proper_set and sim_val >= 0.88 and len(hw) >= 2:
                                continue
                            max_ed = 0.0 if len(rw) <= 6 else 0.15
                            if float(jiwer.cer(rw, hw)) > max_ed:
                                edge_ok = False
                                break
                            if not is_last and len(rw) >= 3 and hw == rw[1:]:
                                edge_ok = False
                                break
                            if is_last and len(rw) >= 3 and hw == rw[:-1]:
                                edge_ok = False
                                break
                        if edge_ok and w_objs and len(ref_w[-1]) >= 4:
                            lw_dur = float(w_objs[-1].end) - float(w_objs[-1].start)
                            lw_prob = float(getattr(w_objs[-1], "probability", 1.0))
                            if lw_dur < 0.09 or (lw_prob < 0.18 and not (lang == "en" and ref_w[-1] in en_proper_set and sim_val >= 0.88)):
                                edge_ok = False
                if lang == "en" and cer_val > 0.10 and en_proper_set and sim_val >= 0.88 and ref_w and hyp_w:
                    wo = jiwer.process_words(" ".join(ref_w), " ".join(hyp_w))
                    clean_ref, clean_hyp = [], []
                    proper_all_spoken = True
                    for ch in wo.alignments[0]:
                        r_slice = ref_w[ch.ref_start_idx:ch.ref_end_idx]
                        h_slice = hyp_w[ch.hyp_start_idx:ch.hyp_end_idx]
                        if ch.type == "equal":
                            clean_ref.extend(r_slice)
                            clean_hyp.extend(h_slice)
                        elif ch.type == "substitute" and all(w in en_proper_set for w in r_slice) and len(h_slice) >= 1:
                            continue
                        else:
                            if any(w in en_proper_set for w in r_slice) and not h_slice:
                                proper_all_spoken = False
                            clean_ref.extend(r_slice)
                            clean_hyp.extend(h_slice)
                    if proper_all_spoken and clean_ref:
                        cer_val = float(jiwer.cer(" ".join(clean_ref), " ".join(clean_hyp)))
            cer_ok = (cer_val <= (0.10 if lang == "en" else 0.18)) and edge_ok
            return rep_ok, cer_ok, cer_val, edge_ok

        cands = []
        for idx, (len_ok, len_reason, tran_ok, tran_reason, w_trim, w_16k, f0_std, pros_pen, pitch_ok) in enumerate(prepped):
            emb = self.get_embedding(w_16k, 16000)
            sim_val = float(torch.nn.functional.cosine_similarity(emb, self.ref_embeddings[ref_path], dim=0).item())
            if lang == "en":
                win_len = 28800
                win_hop = 14400
                if len(w_16k) >= win_len:
                    starts = list(range(0, len(w_16k) - win_len + 1, win_hop))
                    if starts[-1] != len(w_16k) - win_len:
                        starts.append(len(w_16k) - win_len)
                    win_batch = [
                        w_16k[ws:ws + win_len] for ws in starts
                        if float(np.sqrt(np.mean(w_16k[ws:ws + win_len] ** 2))) >= 0.008
                    ]
                    if win_batch:
                        w_embs = self.get_embeddings_batch(win_batch)
                        cos_all = torch.matmul(w_embs, self.ref_embeddings[ref_path])
                        sim_val = min(sim_val, float(cos_all.min().item()))
            sim_thresh = 0.85 if lang == "en" else 0.67
            sim_ok = (sim_val >= sim_thresh) and pitch_ok

            # Skip heavy Whisper transcription on candidates that ALREADY failed acoustic/voice gates
            if sim_ok and len_ok and tran_ok:
                rep_ok, cer_ok, cer_val, edge_ok = _run_asr(w_16k, sim_val)
                asr_done = True
            else:
                rep_ok, cer_ok, cer_val, edge_ok = True, True, 1.0, False
                asr_done = False

            all_ok = sim_ok and len_ok and tran_ok and rep_ok and cer_ok
            cer_bucket = 0.0 if (cer_val <= 0.004 and edge_ok) else round(cer_val, 3)
            cands.append({
                "wav": w_trim,
                "w_16k": w_16k,
                "asr_done": asr_done,
                "all_ok": all_ok,
                "cer": cer_val,
                "cer_bucket": cer_bucket,
                "pros_pen": pros_pen,
                "f0_std": f0_std,
                "sim": sim_val,
                "fails": {
                    "similarity": not sim_ok,
                    "length": (not len_ok and len_reason == "length"),
                    "pause": (not len_ok and len_reason == "pause"),
                    "transient": not tran_ok,
                    "repeat": not rep_ok,
                    "cer": (not cer_ok) if asr_done else False,
                },
            })
            # Early-exit if we already found an unmistakable golden studio take
            if all_ok and cer_bucket == 0.0 and pros_pen == 0.0 and sim_val >= (0.94 if lang == "en" else 0.92):
                break

        passing = [c for c in cands if c["all_ok"]]
        if not passing and need_fallback:
            for c in cands:
                if not c["asr_done"]:
                    rep_ok, cer_ok, cer_val, _ = _run_asr(c["w_16k"], c["sim"])
                    c["cer"] = cer_val
                    c["fails"]["repeat"] = not rep_ok
                    c["fails"]["cer"] = not cer_ok
        if passing:
            best = min(passing, key=lambda x: (x["cer_bucket"], x["pros_pen"], -x["sim"], x["cer"]))
            ok = True
        else:
            best = min(cands, key=lambda x: (x["fails"]["similarity"], sum(x["fails"].values()), -x["sim"], x["cer"], x["pros_pen"]))
            ok = False

        counts = {
            "takes": len(cands),
            "retakes": max(0, len(cands) - 1),
            "length": sum(1 for x in cands if x["fails"]["length"] or x["fails"]["pause"]),
            "repeat": sum(1 for x in cands if x["fails"]["repeat"]),
            "transient": sum(1 for x in cands if x["fails"]["transient"]),
            "similarity": sum(1 for x in cands if x["fails"]["similarity"]),
            "cer": sum(1 for x in cands if x["fails"]["cer"]),
        }
        return best["wav"], ok, counts, {"cer": round(best["cer"], 4), "sim": round(best["sim"], 4), "f0_std": round(best["f0_std"], 1)}

_gates = None
def get_gates():
    global _gates
    if _gates is None:
        _gates = AudioGates()
    return _gates
