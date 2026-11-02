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
    """Integrated loudness of a mono signal; -inf when silent."""
    from scipy.signal import lfilter
    x = np.asarray(x, dtype=np.float64)
    blk, step = int(0.4 * sr), int(0.1 * sr)
    if len(x) < blk:
        x = np.pad(x, (0, blk - len(x)))
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


def trim(x, sr, db=-50.0, margin=0.02):
    thr = 10 ** (db / 20.0)
    idx = np.where(np.abs(x) > thr)[0]
    if not len(idx):
        return x[:int(0.05 * sr)]
    m = int(margin * sr)
    return x[max(0, idx[0] - m): idx[-1] + m]


def fade(x, sr, ms):
    n = min(int(sr * ms / 1000), len(x) // 2)
    if n > 0:
        r = np.linspace(0, 1, n, dtype=x.dtype)
        x = x.copy()
        x[:n] *= r
        x[-n:] *= r[::-1]
    return x


def prepare_sentence(x, sr, audio_cfg):
    """Trim, level to the segment loudness, de-click. Returns float32."""
    x = trim(np.asarray(x, dtype=np.float32), sr, audio_cfg["trimDb"], audio_cfg.get("edgeMs", 20) / 1000.0)
    l = lufs(x, sr)
    if np.isfinite(l) and l > -60:
        g = max(-12.0, min(15.0, audio_cfg["segLufs"] - l))
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


def master(sig, sr, audio_cfg):
    """One constant gain to the program loudness (no pumping); returns (signal, gain_db, measured_lufs)."""
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
