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

        while len(islands) >= 2:
            prev_s, prev_e = islands[-2]
            last_s, last_e = islands[-1]
            gap_ms = (last_s - prev_e) * 10
            tail_ms = (last_e - last_s) * 10
            main_ms = (islands[-2][1] - islands[0][0]) * 10
            if main_ms >= 100 and gap_ms >= 260 and tail_ms <= 150:
                cut_sample = min(len(wav), (prev_e + 2) * hop)
                wav = wav[:cut_sample]
                rms = rms[:prev_e + 2]
                islands.pop()
            elif n_internal_sents == 0 and text_len <= 22 and main_ms >= 100 and gap_ms >= 520 and tail_ms > 220:
                # Very short 1-2 word callout followed by >0.5s dead silence and extra hallucinated babble (e.g. F5 bleed)
                return False, "transient", wav
            else:
                break

        # Also strip any isolated <= 220 ms pre-speech breath/shush/click separated by >= 35 ms before main speech
        if len(islands) >= 2:
            first_s, first_e = islands[0]
            next_s, _ = islands[1]
            first_pk = float(rms[first_s:first_e].max()) if first_e > first_s else 0.0
            if (first_e - first_s) * 10 <= 220 and (next_s - first_e) * 10 >= 35 and first_pk < pk_rms * 0.35:
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

    def score_candidates(self, wavs, sr, ref_path, text_plain, lang, cpu_pool=None, beam_size=3):
        """Score N candidate takes through all 5 §6 gates + F0 prosody tie-breaker.
        Returns (best_wav, all_ok, counts_dict, best_meta)."""
        t_strip = text_plain.strip()
        n_int_sents = self._count_internal_breaks(t_strip)
        def _cpu_prep(w):
            tran_ok, tran_reason, w_trim = self.check_transient(w, sr, n_internal_sents=n_int_sents, text_len=len(t_strip))
            len_ok, len_reason = self.check_length_pause(w_trim, sr, text_plain, lang)
            w_16k = (librosa.resample(w_trim, orig_sr=sr, target_sr=16000) if sr != 16000 else w_trim).astype(np.float32)
            f0_std, pros_pen = self.check_prosody(w_16k, 16000)
            return len_ok, len_reason, tran_ok, tran_reason, w_trim, w_16k, f0_std, pros_pen

        if cpu_pool is not None and len(wavs) > 1:
            prepped = list(cpu_pool.map(_cpu_prep, wavs))
        else:
            prepped = [_cpu_prep(w) for w in wavs]

        import jiwer, re
        ref_norm = re.sub(r"[\W_]+", " ", text_plain.lower()).strip()
        ref_path = str(ref_path)
        if ref_path not in self.ref_embeddings:
            ref_wav, ref_sr = sf.read(ref_path)
            if ref_wav.ndim > 1:
                ref_wav = ref_wav.mean(axis=1)
            self.ref_embeddings[ref_path] = self.get_embedding(ref_wav, ref_sr)

        cands = []
        for idx, (len_ok, len_reason, tran_ok, tran_reason, w_trim, w_16k, f0_std, pros_pen) in enumerate(prepped):
            emb = self.get_embedding(w_16k, 16000)
            sim_val = float(torch.nn.functional.cosine_similarity(emb, self.ref_embeddings[ref_path], dim=0).item())
            if lang == "en" and len(w_16k) >= 40000:
                # Split-window speaker check: catch any 2s opening/closing roleplay flip out of British 'sky'
                emb_h = self.get_embedding(w_16k[:35200], 16000)
                emb_t = self.get_embedding(w_16k[-35200:], 16000)
                sim_h = float(torch.nn.functional.cosine_similarity(emb_h, self.ref_embeddings[ref_path], dim=0).item())
                sim_t = float(torch.nn.functional.cosine_similarity(emb_t, self.ref_embeddings[ref_path], dim=0).item())
                sim_val = min(sim_val, sim_h, sim_t)
            sim_thresh = 0.82 if lang == "en" else 0.67
            sim_ok = sim_val >= sim_thresh

            segs, _ = self.whisper.transcribe(
                w_16k, language=lang, beam_size=1,
                word_timestamps=False, condition_on_previous_text=False,
            )
            hyp_text = " ".join(s.text for s in segs).strip()
            words = re.findall(r"\w+", hyp_text.lower())
            rep_ok = True
            t_lower = text_plain.lower()
            for wi in range(len(words) - 1):
                if words[wi] == words[wi + 1] and len(words[wi]) > 1 and t_lower.count(words[wi]) < 2:
                    rep_ok = False
                    break
            hyp_norm = re.sub(r"[\W_]+", " ", hyp_text.lower()).strip()
            cer_val = float(jiwer.cer(ref_norm, hyp_norm)) if ref_norm else 0.0
            cer_ok = cer_val <= 0.18

            all_ok = sim_ok and len_ok and tran_ok and rep_ok and cer_ok
            cer_bucket = 0.0 if cer_val <= 0.02 else round(cer_val, 2)
            cands.append({
                "wav": w_trim,
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
                    "cer": not cer_ok,
                },
            })

        passing = [c for c in cands if c["all_ok"]]
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
