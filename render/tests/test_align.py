import numpy as np
import align
import content
import textprep as tp


def test_romanize():
    assert align.romanize_char("щ", "ru") == "sh" and align.romanize_char("ь", "ru") == ""
    assert align.romanize_char("é", "fr") == "e" and align.romanize_char("œ", "fr") == "oe"
    assert align.romanize_char("'", "fr") == "'" and align.romanize_char("3", "en") == ""


def test_token_mapping_in_order_and_split_elisions():
    text = "J'ai l'addition, merci."
    toks = ["J'", "ai", "l'", "addition,", "merci."]          # Dix annotations split elisions
    sp = tp.token_spans(text, toks)
    assert sp == [(0, 2), (2, 4), (5, 7), (7, 16), (17, 23)]
    assert tp.token_spans("a b", ["a", "zzz", "b"]) == [(0, 1), None, (2, 3)]


def test_words_from_chars_basic():
    text = "ab cd"
    ct = [(0.10, 0.14), (0.20, 0.30), None, (0.50, 0.54), (0.60, 0.70)]
    w = align.words_from_chars(ct, [(0, 2), (3, 5)], None)
    assert [x["ok"] for x in w] == [True, True]
    assert w[0]["s"] == 0.10 and w[1]["s"] == 0.50
    assert w[0]["e"] <= w[1]["s"]


def test_missing_token_is_flagged_and_interpolated():
    ct = [(0.1, 0.2), None, (0.9, 1.0)]
    w = align.words_from_chars(ct, [(0, 1), (1, 2), (2, 3)], None)
    assert w[1]["ok"] is False and w[1]["why"] == "missing"
    assert w[0]["e"] <= w[1]["s"] <= w[2]["s"]


def test_onset_snap_bounds():
    hop = 0.005
    env = np.full(400, -80.0)
    env[60:300] = -20.0                   # speech from 0.30 s
    # CTC says 0.36; onset is 0.30 -> snaps back, but at most max_snap and not before prev_end
    assert abs(align.snap_start(0.36, 0.0, env, hop, 0.12) - 0.30) < 0.011
    assert align.snap_start(0.36, 0.33, env, hop, 0.12) >= 0.33          # previous word's end
    env2 = np.full(400, -80.0)
    env2[20:300] = -20.0                  # onset 0.10, CTC at 0.36: capped at 120 ms
    assert abs(align.snap_start(0.36, 0.0, env2, hop, 0.12) - 0.24) < 0.011
    assert align.snap_start(0.36, 0.0, np.full(400, -80.0), hop, 0.12) == 0.36   # silence: unchanged
