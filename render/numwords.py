"""Digits in a Whisper transcript -> Russian number words, so a clip read "пять рублей" is not scored against "5 рублей".

Whisper writes numerals as digits; the clip text is spelled out. `expand(hyp, ref)` replaces every digit group (0..999999) of `hyp` by the
declension (case x gender of the last unit) whose words are closest to the reference text, so the reference's own form is used whenever the
audio matches it. No third-party package; pure functions."""
import re

CASES = ("nom", "gen", "dat", "acc", "ins", "prep")
GENDERS = ("m", "f", "n")

# case order: nom gen dat acc ins prep
_UNITS = {
    1: {"m": "один одного одному один одним одном", "f": "одна одной одной одну одной одной", "n": "одно одного одному одно одним одном"},
    2: {"m": "два двух двум два двумя двух", "f": "две двух двум две двумя двух", "n": "два двух двум два двумя двух"},
}
_FIXED = {
    0: "ноль нуля нулю ноль нулём ноле",
    3: "три трёх трём три тремя трёх",
    4: "четыре четырёх четырём четыре четырьмя четырёх",
    5: "пять пяти пяти пять пятью пяти",
    6: "шесть шести шести шесть шестью шести",
    7: "семь семи семи семь семью семи",
    8: "восемь восьми восьми восемь восемью восьми",
    9: "девять девяти девяти девять девятью девяти",
    10: "десять десяти десяти десять десятью десяти",
    40: "сорок сорока сорока сорок сорока сорока",
    90: "девяносто девяноста девяноста девяносто девяноста девяноста",
    100: "сто ста ста сто ста ста",
    200: "двести двухсот двумстам двести двумястами двухстах",
    300: "триста трёхсот тремстам триста тремястами трёхстах",
    400: "четыреста четырёхсот четырёмстам четыреста четырьмястами четырёхстах",
    500: "пятьсот пятисот пятистам пятьсот пятьюстами пятистах",
    600: "шестьсот шестисот шестистам шестьсот шестьюстами шестистах",
    700: "семьсот семисот семистам семьсот семьюстами семистах",
    800: "восемьсот восьмисот восьмистам восемьсот восемьюстами восьмистах",
    900: "девятьсот девятисот девятистам девятьсот девятьюстами девятистах",
}
_SOFT = {11: "одиннадцать", 12: "двенадцать", 13: "тринадцать", 14: "четырнадцать", 15: "пятнадцать", 16: "шестнадцать", 17: "семнадцать",
         18: "восемнадцать", 19: "девятнадцать", 20: "двадцать", 30: "тридцать"}
_TENS = {50: ("пятьдесят", "пяти", "пятью"), 60: ("шестьдесят", "шести", "шестью"), 70: ("семьдесят", "семи", "семью"), 80: ("восемьдесят", "восьми", "восемью")}
_THOUSAND_SG = "тысяча тысячи тысяче тысячу тысячей тысяче".split()
_THOUSAND_PL = {"nom": "тысячи", "gen": "тысяч", "dat": "тысячам", "acc": "тысячи", "ins": "тысячами", "prep": "тысячах"}
_THOUSAND_5 = {**_THOUSAND_PL, "nom": "тысяч", "acc": "тысяч"}


def _forms(n, gender):
    """The six case forms of a number 0..99 or a round hundred below 1000 (a list, in CASES order)."""
    if n in _UNITS:
        return _UNITS[n][gender].split()
    if n in _FIXED:
        return _FIXED[n].split()
    if n in _SOFT:
        w = _SOFT[n]
        s = w[:-1] + "и"
        return [w, s, s, w, w[:-1] + "ью", s]
    if n in _TENS:
        w, oblique, ins = _TENS[n]
        # пятьдесят / пяти+десяти / пятью+десятью
        base = oblique + "десяти"
        return [w, base, base, w, ins + "десятью", base]
    raise ValueError(n)


def _under_1000(n, case, gender):
    words = []
    h, rest = (n // 100) * 100, n % 100
    if h:
        words.append(_forms(h, gender)[CASES.index(case)])
    if rest:
        if rest in _FIXED or rest in _SOFT or rest in _UNITS or rest in _TENS or rest == 0:
            words.append(_forms(rest, gender)[CASES.index(case)])
        else:
            t, u = rest - rest % 10, rest % 10
            words.append(_forms(t, gender)[CASES.index(case)])
            if u:
                words.append(_forms(u, gender)[CASES.index(case)])
    return words


def spell(n, case="nom", gender="m"):
    """n in 0..999999 as Russian words (the unit gets `gender`, the thousands count is feminine)."""
    if n == 0:
        return _forms(0, gender)[CASES.index(case)]
    k, rest = divmod(n, 1000)
    words = []
    if k:
        if k % 10 == 1 and k % 100 != 11:
            thousand = _THOUSAND_SG[CASES.index(case)]
            head = _under_1000(k, case, "f")
            if k == 1:
                head = []
            elif head:
                head = head
        elif k % 10 in (2, 3, 4) and k % 100 not in (12, 13, 14):
            thousand = _THOUSAND_PL[case]
            head = _under_1000(k, case, "f")
        else:
            thousand = _THOUSAND_5[case]
            head = _under_1000(k, case, "f")
        words += head + [thousand]
    words += _under_1000(rest, case, gender)
    return " ".join(words)


def spellings(n):
    """Every distinct spelling of n (case x gender)."""
    return sorted({spell(n, c, g) for c in CASES for g in GENDERS})


def _lev(a, b):
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != cb)))
        prev = cur
    return prev[-1]


_NUM = re.compile(r"\d[\d ]*\d|\d")


def expand(hyp, ref):
    """`hyp` with each number (digits, optionally space-grouped "7 000") written out in the declension closest to `ref` (a text, any case)."""
    from asr_cer import nz
    out, pos = [], 0
    r = nz(ref)
    for m in _NUM.finditer(hyp):
        digits = m.group(0).replace(" ", "")
        if len(digits) > 6:
            continue
        n = int(digits)
        cands = spellings(n)
        best = min(cands, key=lambda c: (0 if c in r else 1, _lev(c, r)))
        out.append((m.start(), m.end(), best))
    res = hyp
    for s, e, w in reversed(out):
        res = res[:s] + w + res[e:]
    return res
