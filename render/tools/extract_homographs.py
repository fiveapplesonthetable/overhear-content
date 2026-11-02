"""One-off: dump RuAccent's homograph surface forms (words with >1 stress variant) to data/ru_homographs.txt.gz.
usage: $OVERHEAR_HOME/venv-f5/bin/python extract_homographs.py"""
import gzip, json, pathlib, ruaccent
d = pathlib.Path(ruaccent.__file__).parent / "dictionary" / "omographs.json.gz"
words = sorted({w.replace("ё", "е") for w in json.load(gzip.open(d))})
out = pathlib.Path(__file__).resolve().parents[1] / "data" / "ru_homographs.txt.gz"
gzip.open(out, "wt", encoding="utf-8").write("\n".join(words) + "\n")
print(len(words), out)
