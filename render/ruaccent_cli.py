"""Runs inside the RuAccent venv (CPU): stdin JSON list of sentences -> stdout JSON list with U+0301 marks."""
import json, re, sys
from ruaccent import RUAccent

A = RUAccent()
A.load(omograph_model_size="turbo", use_dictionary=True, device="CPU")


def conv(s):
    return re.sub(r"\+([ЁёА-Яа-я])", lambda m: m.group(1) if m.group(1) in "Ёё" else m.group(1) + "́", s)


norm = lambda s: re.sub(r"[^а-яё]", "", s.lower().replace("+", "").replace("́", "").replace("ё", "е"))
res = []
for t in json.load(sys.stdin):
    try:
        o = A.process_all(t)
        res.append(conv(o) if norm(o) == norm(t) else t)
    except Exception:
        res.append(t)
json.dump(res, sys.stdout, ensure_ascii=False)
