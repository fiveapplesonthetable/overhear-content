import subprocess
import numpy as np
import pytest
pytest.importorskip("scipy")
import audio


def tone(sec, sr=24000, f=220, a=0.1):
    t = np.arange(int(sec * sr)) / sr
    return (a * np.sin(2 * np.pi * f * t)).astype(np.float32)


def test_layout_arithmetic():
    # two lines; line 0 has two sentences (0.5 s inter-sentence gap), line 1 one
    lay = audio.lay_out([[(1.0, 0.5), (0.8, 0.4)], [(2.0, 0.3)]])
    assert lay[0][:3] == (0.0, 1.5 + 0.8, 1.5 + 0.8 + 0.4)
    assert lay[0][3] == [(0.0, 1.0), (1.5, 2.3)]
    assert abs(lay[1][0] - 2.7) < 1e-9 and abs(lay[1][1] - 4.7) < 1e-9 and abs(lay[1][2] - 5.0) < 1e-9


def test_assemble_matches_layout_in_samples():
    sr = 24000
    cfg = {"trimDb": -50}
    sig, lay = audio.assemble([[(tone(1.0), 0.5), (tone(0.8), 0.4)], [(tone(2.0), 0.3)]], sr, cfg)
    assert abs(len(sig) / sr - lay[-1][2]) < 1e-3


def test_lufs_matches_ffmpeg():
    sr = 24000
    rng = np.random.default_rng(1)
    x = (0.05 * rng.standard_normal(sr * 5)).astype(np.float32)
    ours = audio.lufs(x, sr)
    r = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-f", "f32le", "-ar", str(sr), "-ac", "1", "-i", "pipe:0", "-af", "ebur128", "-f", "null", "-"],
                       input=x.tobytes(), capture_output=True)
    import re
    ref = float(re.findall(r"\bI:\s*(-?[\d.]+)\s*LUFS", r.stderr.decode())[-1])
    assert abs(ours - ref) < 0.3, (ours, ref)


def test_master_hits_program_loudness():
    sr = 24000
    x = tone(6.0, a=0.02)
    y, g, before = audio.master(x, sr, {"programLufs": -16.0})
    assert abs(audio.lufs(y, sr) + 16.0) < 0.2


def test_mp3_gapless_header_and_duration(tmp_path):
    sr = 24000
    sig, lay = audio.assemble([[(tone(2.0, a=0.2), 0.5)], [(tone(1.5, a=0.2), 0.3)]], sr, {"trimDb": -50})
    p = tmp_path / "a.mp3"
    audio.encode_mp3(sig, sr, p, 96)
    tag = audio.lame_tag(p)
    assert tag and tag["xing"] in ("Xing", "Info") and tag["lame"] and tag["lame"].startswith("LAME")
    assert tag["delay"] is not None and tag["delay"] > 0      # encoder delay recorded => decoders skip it
    assert abs(audio.mp3_duration(p) - len(sig) / sr) < 0.05  # spans match the mp3 within 50 ms
    # no ID3 tag in front
    assert p.read_bytes()[:3] != b"ID3"


def test_trim_and_fade_keep_length_sane():
    x = np.concatenate([np.zeros(2400, np.float32), tone(1.0), np.zeros(2400, np.float32)])
    y = audio.trim(x, 24000, -50)
    assert 24000 <= len(y) <= 24000 + 2 * 480 + 10
    z = audio.fade(y, 24000, 15)
    assert z[0] == 0 and abs(z[-1]) < 1e-6


def test_mp3_does_not_clip_when_the_phone_resamples_it(tmp_path):
    import re
    sr = 24000
    t = np.arange(sr * 3) / sr
    # These stored samples are below full scale; the reconstructed signal peaks between them.
    x = (1.3 * np.sin(2 * np.pi * 6000 * t + np.pi / 4)).astype(np.float32)
    assert np.max(np.abs(x)) < 1
    p = tmp_path / "intersample.mp3"
    audio.encode_mp3(x, sr, p)
    check = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", str(p), "-filter_threads", "1",
                            "-af", "ebur128=peak=true", "-f", "null", "-"], capture_output=True, check=True)
    peak = float(re.findall(r"Peak:\s+(-?[\d.]+) dBFS", check.stderr.decode())[-1])
    assert peak < 0, peak
