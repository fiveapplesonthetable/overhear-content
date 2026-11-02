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
        inputs = self.extractor(wav_16k, return_tensors="pt", sampling_rate=16000).to("cuda")
        with torch.no_grad():
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

    def check_length_pause(self, wav, sr, text, lang, max_pause=0.60, len_mult=1.35):
        median_spc = 0.20 if lang in ["ja", "zh", "ko"] else 0.085
        dur = len(wav) / sr
        expected = len(text) * median_spc
        if expected < 0.8: expected = 0.8
        
        if dur > expected * len_mult:
            return False, "length"

        frame_len = int(sr * 0.05)
        hop_len = int(sr * 0.01)
        if len(wav) < frame_len:
            return True, "ok"
        rms = librosa.feature.rms(y=wav, frame_length=frame_len, hop_length=hop_len)[0]
        silence_thresh = rms.max() * 0.05
        is_silence = rms < silence_thresh
        
        non_sil = np.where(~is_silence)[0]
        if len(non_sil) == 0:
            return True, "ok"
        
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
        if max_pause_sec > max_pause:
            return False, "pause"
            
        return True, "ok"

    def check_repeat_and_cer(self, wav, sr, text, lang):
        if sr != 16000:
            wav_16k = librosa.resample(wav, orig_sr=sr, target_sr=16000)
        else:
            wav_16k = wav
        wav_16k = wav_16k.astype(np.float32)
        segs, info = self.whisper.transcribe(wav_16k, language=lang, beam_size=5, word_timestamps=True, condition_on_previous_text=False)
        words = []
        hyp_text = ""
        for s in segs:
            hyp_text += s.text + " "
            if s.words:
                for w in s.words:
                    words.append(w.word.strip().lower())
                    
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

    def check_transient(self, wav, sr):
        hop = int(sr * 0.01)
        if len(wav) < hop: return True, "ok", wav
        
        rms = librosa.feature.rms(y=wav, frame_length=hop*2, hop_length=hop)[0]
        silence_thresh = rms.max() * 0.05
        speech_rms = rms[rms >= silence_thresh]
        mean_speech_rms = speech_rms.mean() if len(speech_rms) > 0 else 0
        if mean_speech_rms == 0: return True, "ok", wav
        
        b, a = scipy.signal.butter(4, 150, btype='lowpass', fs=sr)
        wav_low = scipy.signal.filtfilt(b, a, wav)
        rms_low = librosa.feature.rms(y=wav_low, frame_length=hop*2, hop_length=hop)[0]
        
        first_speech = np.where(rms >= silence_thresh)[0][0] * hop
        last_speech = np.where(rms >= silence_thresh)[0][-1] * hop
        
        # Check bursts
        retake = False
        trim_start = 0
        trim_end = len(wav)
        
        for i, (r, r_low) in enumerate(zip(rms, rms_low)):
            if r > mean_speech_rms * 4.0 or r_low > mean_speech_rms * 4.0:
                pos = i * hop
                time_ms = pos / sr * 1000
                if pos < first_speech:
                    trim_start = max(trim_start, pos + hop)
                elif pos > last_speech:
                    trim_end = min(trim_end, pos - hop)
                else:
                    if time_ms < 80 or time_ms > (len(wav)/sr*1000 - 80):
                        retake = True
        
        if retake:
            return False, "transient", wav
        
        if trim_start > 0 or trim_end < len(wav):
            if trim_start < trim_end:
                wav = wav[trim_start:trim_end]
            else:
                return False, "transient", wav
                
        return True, "ok", wav

_gates = None
def get_gates():
    global _gates
    if _gates is None:
        _gates = AudioGates()
    return _gates
