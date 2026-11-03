"""Audio assembly: edge trim, BS.1770 loudness, layout with gaps, spans, gapless LAME mp3.

Layout arithmetic is the publisher's timing.py: a unit is (speech_seconds, gap_after); a line starts where the
previous unit's padding ended and speaks for the sum of its sentences plus the inter-sentence gaps.
"""
import subprocess
import numpy as np


# ---- loudness (ITU-R BS.1770-4, as pyloudnorm) ------------------------------------------------------------
def _k_filters(sr):
    from scipy.signal import lfilter  # noqa: F401
    import math
    # high shelf
    G, Q, fc = 3.999843853973347, 0.7071752369554196, 1681.9744509555319
    K = math.tan(math.pi * fc / sr)
    Vh = 10 ** (G / 20.0)
    Vb = Vh ** 0.4996667741545416
    a0 = 1.0 + K / Q + K * K
    b_s = np.array([(Vh + Vb * K / Q + K * K) / a0, 2.0 * (K * K - Vh) / a0, (Vh - Vb * K / Q + K * K) / a0])
    a_s = np.array([1.0, 2.0 * (K * K - 1.0) / a0, (1.0 - K / Q + K * K) / a0])
    # high pass
    Q2, fc2 = 0.5003270373253953, 38.13547087613982
    K = math.tan(math.pi * fc2 / sr)
    a0 = 1.0 + K / Q2 + K * K
    b_h = np.array([1.0, -2.0, 1.0])
    a_h = np.array([1.0, 2.0 * (K * K - 1.0) / a0, (1.0 - K / Q2 + K * K) / a0])
    return (b_s, a_s), (b_h, a_h)


def lufs(x, sr):
    """Integrated loudness of a mono signal; -inf when silent.
    Short clips (< 400 ms) are tiled rather than zero-padded so 1-word callouts do not get +12 dB silence-padding gain."""
    from scipy.signal import lfilter
    x = np.asarray(x, dtype=np.float64)
    if len(x) == 0 or float(np.max(np.abs(x))) <= 1e-7:
        return float("-inf")
    blk, step = int(0.4 * sr), int(0.1 * sr)
    if len(x) < blk:
        x = np.resize(x, blk)
    (bs, as_), (bh, ah) = _k_filters(sr)
    y = lfilter(bh, ah, lfilter(bs, as_, x))
    n = 1 + (len(y) - blk) // step
    cs = np.concatenate([[0.0], np.cumsum(y * y)])
    z = (cs[np.arange(n) * step + blk] - cs[np.arange(n) * step]) / blk
    with np.errstate(divide="ignore"):
        l = -0.691 + 10 * np.log10(z)
    keep = l > -70.0
    if not keep.any():
        return float("-inf")
    rel = -0.691 + 10 * np.log10(np.mean(z[keep])) - 10.0
    keep &= l > rel
    if not keep.any():
        return float("-inf")
    return float(-0.691 + 10 * np.log10(np.mean(z[keep])))


def _strip_detached_edge_noise(x, sr):
    """Strip isolated low-energy pre-speech breaths/clicks and post-speech EOS pops/breaths
    that sit above -50 dBFS sample peak yet > 16-18 dB below speech RMS across a wide silent gap.
    Never touches real consonant clusters (Ст-, St-, gap 40..90 ms) or plosive codas ('Perder o foco?', 'last time')."""
    hop = max(1, int(0.01 * sr))
    n = len(x) // hop
    if n < 22:
        return x
    frames = x[:n * hop].reshape(n, hop)
    rms = np.sqrt(np.mean(frames * frames, axis=1))
    pk = float(rms.max())
    if pk <= 1e-6:
        return x

    # 1. Strip sub-12%-RMS pre-speech breath/sigh separated by >= 150 ms of silence before main speech
    low_thr = max(10 ** (-52.0 / 20.0), pk * 0.008)
    act_low = rms >= low_thr
    if act_low.any():
        isl = []
        i = 0
        while i < n:
            if act_low[i]:
                j = i + 1
                while j < n and act_low[j]:
                    j += 1
                isl.append((i, j))
                i = j
            else:
                i += 1
        while len(isl) >= 2:
            s0, e0 = isl[0]
            s1, _ = isl[1]
            dur_ms = (e0 - s0) * 10
            gap_ms = (s1 - e0) * 10
            p0 = float(rms[s0:e0].max())
            if dur_ms <= 450 and gap_ms >= 150 and p0 < pk * 0.12:
                cut_start = max(0, (s1 - 2) * hop)
                x = x[cut_start:]
                return _strip_detached_edge_noise(x, sr)
            break
        if len(isl) >= 2:
            prev_s, prev_e = isl[-2]
            last_s, last_e = isl[-1]
            gap_ms = (last_s - prev_e) * 10
            tail_ms = (last_e - last_s) * 10
            main_ms = (isl[-2][1] - isl[0][0]) * 10
            tail_pk = float(rms[last_s:last_e].max())
            if main_ms >= 150 and gap_ms >= 220 and tail_ms <= 180 and tail_pk < pk * 0.14:
                x = x[:min(len(x), (prev_e + 2) * hop)]
                frames = x[:(len(x) // hop) * hop].reshape(len(x) // hop, hop)
                rms = np.sqrt(np.mean(frames * frames, axis=1))
                n = len(rms)

    # 2. Strip continuous low-energy (< 6.5% pk) pre-speech inhale/sigh shelves (>= 280 ms before speech onset,
    #    keeping a 90 ms pre-onset runway for initial fricatives/stops) and post-speech exhale shelves (keeping 160 ms coda).
    main_lead = np.where(rms >= pk * 0.12)[0]
    if len(main_lead) and int(main_lead[0]) >= 28:
        pre_end = int(main_lead[0]) - 9
        if pre_end >= 18 and float(rms[:pre_end].max()) < pk * 0.065:
            x = x[pre_end * hop:].copy()
            fn = min(len(x), int(0.015 * sr))
            if fn > 0:
                x[:fn] *= (0.5 * (1.0 - np.cos(np.linspace(0.0, np.pi, fn)))).astype(x.dtype)
            frames = x[:(len(x) // hop) * hop].reshape(len(x) // hop, hop)
            rms = np.sqrt(np.mean(frames * frames, axis=1))
            n = len(rms)

    main_tail = np.where(rms >= pk * 0.10)[0]
    if len(main_tail):
        post_start = int(main_tail[-1]) + 16
        if (n - post_start) >= 24 and float(rms[post_start:].max()) < pk * 0.055:
            x = x[:min(len(x), post_start * hop)].copy()
            fn = min(len(x), int(0.020 * sr))
            if fn > 0:
                x[-fn:] *= (0.5 * (1.0 + np.cos(np.linspace(0.0, np.pi, fn)))).astype(x.dtype)
            frames = x[:(len(x) // hop) * hop].reshape(len(x) // hop, hop)
            rms = np.sqrt(np.mean(frames * frames, axis=1))
            n = len(rms)

    # 3. Also strip any tiny (<= 55 ms) higher-crest (< 25% pk) EOS click separated by >= 320 ms silence
    active_thr = max(10 ** (-42.0 / 20.0), pk * 0.06)
    act = rms >= active_thr
    if not act.any():
        return x
    islands = []
    i = 0
    while i < n:
        if act[i]:
            j = i + 1
            while j < n and act[j]:
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
        tail_pk = float(rms[last_s:last_e].max())
        if main_ms >= 150 and gap_ms >= 320 and tail_ms <= 55 and tail_pk < pk * 0.25:
            cut_sample = min(len(x), (prev_e + 2) * hop)
            x = x[:cut_sample]
    return x


def trim(x, sr, db=-50.0, margin=0.02):
    x = _strip_detached_edge_noise(x, sr)
    thr = 10 ** (db / 20.0)
    idx = np.where(np.abs(x) > thr)[0]
    if not len(idx):
        return x[:int(0.05 * sr)]
    m = int(margin * sr)
    return x[max(0, idx[0] - m): idx[-1] + m]


def fade(x, sr, ms):
    n = min(int(sr * ms / 1000), len(x) // 2)
    if n > 0:
        r = (0.5 * (1.0 - np.cos(np.linspace(0.0, np.pi, n)))).astype(x.dtype)
        x = x.copy()
        x[:n] *= r
        x[-n:] *= r[::-1]
    return x


def prepare_sentence(x, sr, audio_cfg):
    """Trim, level to the segment loudness (bounded gain), raised-cosine de-click. Returns float32."""
    x = trim(np.asarray(x, dtype=np.float32), sr, audio_cfg["trimDb"], audio_cfg.get("edgeMs", 20) / 1000.0)
    l = lufs(x, sr)
    if np.isfinite(l) and l > -60:
        max_up = 5.0 if len(x) < int(0.45 * sr) else 7.5
        g = max(-12.0, min(max_up, audio_cfg["segLufs"] - l))
        x = x * np.float32(10 ** (g / 20.0))
    return fade(x, sr, audio_cfg["fadeMs"])


def lay_out(units):
    """units: per line, [(speech_seconds, gap_after)] -> [(start, end, next_start, [(s, e) per sentence])]."""
    out, cur = [], 0.0
    for line in units:
        start, sents = cur, []
        end = cur
        for speech, gap in line:
            end = cur + speech
            sents.append((cur, end))
            cur = end + gap
        out.append((start, end, cur, sents))
    return out


def assemble(lines, sr, audio_cfg):
    """lines: per segment [(samples, gap_seconds)] (samples already prepared).
    Returns (signal float32, layout) with sample-exact starts."""
    parts, units = [], []
    for line in lines:
        u = []
        for x, gap in line:
            parts.append(x)
            gs = int(round(gap * sr))
            if gs:
                parts.append(np.zeros(gs, dtype=np.float32))
            u.append((len(x) / sr, gs / sr))
        units.append(u)
    sig = np.concatenate(parts) if parts else np.zeros(0, dtype=np.float32)
    return sig, lay_out(units)


def _podcast_warm_eq(sig, sr):
    """Subtle studio podcast warmth: 55 Hz rumble cut, +2.0 dB warm chest fullness at 155 Hz, +1.2 dB presence at 5.2 kHz."""
    if len(sig) < int(0.05 * sr):
        return sig
    from scipy.signal import butter, sosfilt, lfilter
    import math
    x = np.asarray(sig, dtype=np.float64)
    # 1. 55 Hz 2nd-order high-pass (kills subsonic thumps/pops)
    sos_hp = butter(2, 55.0 / (0.5 * sr), btype="highpass", output="sos")
    x = sosfilt(sos_hp, x)
    # 2. +2.0 dB peaking EQ at 155 Hz (Q=0.75) for full human chest resonance
    A = 10.0 ** (2.0 / 40.0)
    w0 = 2.0 * math.pi * 155.0 / sr
    alpha = math.sin(w0) / (2.0 * 0.75)
    b0 = 1.0 + alpha * A
    b1 = -2.0 * math.cos(w0)
    b2 = 1.0 - alpha * A
    a0 = 1.0 + alpha / A
    a1 = -2.0 * math.cos(w0)
    a2 = 1.0 - alpha / A
    x = lfilter([b0 / a0, b1 / a0, b2 / a0], [1.0, a1 / a0, a2 / a0], x)
    # 3. +1.2 dB high-shelf at 5200 Hz (Q=0.707) for crisp natural presence
    if 5200.0 < 0.45 * sr:
        As = 10.0 ** (1.2 / 40.0)
        ws = 2.0 * math.pi * 5200.0 / sr
        cw, sw = math.cos(ws), math.sin(ws)
        al_s = sw / 2.0 * math.sqrt((As + 1.0 / As) * (1.0 / 0.707 - 1.0) + 2.0)
        sq = 2.0 * math.sqrt(As) * al_s
        sb0 = As * ((As + 1.0) + (As - 1.0) * cw + sq)
        sb1 = -2.0 * As * ((As - 1.0) + (As + 1.0) * cw)
        sb2 = As * ((As + 1.0) + (As - 1.0) * cw - sq)
        sa0 = (As + 1.0) - (As - 1.0) * cw + sq
        sa1 = 2.0 * ((As - 1.0) - (As + 1.0) * cw)
        sa2 = (As + 1.0) - (As - 1.0) * cw - sq
        x = lfilter([sb0 / sa0, sb1 / sa0, sb2 / sa0], [1.0, sa1 / sa0, sa2 / sa0], x)
    return x.astype(np.float32)


def master(sig, sr, audio_cfg):
    """Warm podcast EQ + one constant gain to the program loudness (no pumping); returns (signal, gain_db, measured_lufs)."""
    if audio_cfg.get("warmEq", True) and "segLufs" in audio_cfg:
        sig = _podcast_warm_eq(sig, sr)
    l = lufs(sig, sr)
    if not np.isfinite(l):
        return sig, 0.0, l
    g = audio_cfg["programLufs"] - l
    return (sig * np.float32(10 ** (g / 20.0))).astype(np.float32), g, l


def encode_mp3(sig, sr, out_path, kbps=96, limits=(0.794, 0.708, 0.631, 0.562)):
    """96 kbps mono LAME with the Xing/Info + LAME tag (gapless: encoder delay/padding recorded). Peak limiter at -2 dB;
    limiting and the decoded peak check run at 96 kHz to include peaks between the stored samples. A file still reaching 0 dBFS is re-encoded with a
    ceiling 1 dB lower until it does not. `limits`: the ceilings tried in order (the narrator pass re-encodes decoded audio whose peaks already
    sit near 0.89 and starts higher, so the second limiter pass does not take 0.45 LU off the scene)."""
    peak_rate = max(sr, 96000)
    # Preserve the limiter's original delay in source samples (119 at 24 kHz),
    # which narrator splices account for when reading and replacing scene audio.
    attack_ms = ((int(sr * 0.005) - 1) / sr + 1 / peak_rate) * 1000
    for limit in limits:
        r = subprocess.run(
            ["ffmpeg", "-y", "-loglevel", "error", "-f", "f32le", "-ar", str(sr), "-ac", "1", "-i", "pipe:0",
             "-filter_threads", "1", "-af", f"aresample={peak_rate},alimiter=limit={limit}:level=disabled:attack={attack_ms:.9g},aresample={sr}",
             "-c:a", "libmp3lame", "-b:a", f"{kbps}k", "-ac", "1",
             "-write_xing", "1", "-id3v2_version", "0", "-write_id3v1", "0", str(out_path)],
            input=np.asarray(sig, dtype="<f4").tobytes(), capture_output=True)
        if r.returncode != 0:
            raise RuntimeError("ffmpeg encode failed: " + r.stderr.decode(errors="replace")[-300:])
        decoded = subprocess.run(["ffmpeg", "-v", "error", "-i", str(out_path), "-filter_threads", "1",
                                  "-ar", str(peak_rate), "-f", "f32le", "-ac", "1", "-"], capture_output=True)
        if decoded.returncode or not decoded.stdout:
            raise RuntimeError("ffmpeg could not decode the encoded mp3")
        if float(np.max(np.abs(np.frombuffer(decoded.stdout, dtype=np.float32)))) < 0.999:
            return
    raise RuntimeError("encoded mp3 still reaches full scale after resampling at every limiter ceiling")


def mp3_duration(path, sr=None) -> float:
    """Decoded length in seconds (ffmpeg honours the LAME delay/padding, i.e. what a gapless player plays)."""
    r = subprocess.run(["ffmpeg", "-v", "error", "-i", str(path), "-f", "f32le", "-ac", "1", "-"], capture_output=True)
    rate = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "stream=sample_rate", "-of", "csv=p=0", str(path)],
                          capture_output=True, text=True).stdout.split()
    return len(r.stdout) / 4 / float(sr or (rate[0] if rate else 24000))


def lame_tag(path):
    """Parse the Xing/Info frame of an mp3: {'xing': 'Info'|'Xing', 'lame': 'LAME3.100', 'delay': int, 'padding': int}.
    None when there is no such header (not gapless)."""
    data = open(path, "rb").read(4096)
    for tag in (b"Xing", b"Info"):
        i = data.find(tag)
        if i >= 0 and i < 64:
            j = data.find(b"LAME", i)
            if j < 0:
                return {"xing": tag.decode(), "lame": None, "delay": None, "padding": None}
            enc = data[j:j + 9].decode("latin1")
            d = data[j + 21:j + 24]
            delay = (d[0] << 4) | (d[1] >> 4)
            padding = ((d[1] & 0x0F) << 8) | d[2]
            return {"xing": tag.decode(), "lame": enc, "delay": delay, "padding": padding}
    return None
