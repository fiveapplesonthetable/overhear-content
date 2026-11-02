"""Smoke test: one tiny scene per language rendered end to end (the real pipeline.py path) into a scratch store.

  sh smoke.sh OUTDIR     (this file only writes the synthetic content; smoke.sh renders, then scores with Whisper)
Scenes: smoke-ru (Russian, notes with stress), smoke-fr (French), both with an English narrator, so Russian, French and
English are each covered. Writes <out>/store/<id>/* and <out>/scenes.txt.
"""
import json, sys
from pathlib import Path
A = "́"
RU = [("narrator", "A short test in Russian. First you hear the lines, then the meaning."),
      ("max", "Девушка, с вами всё в порядке?"), ("vika", "Да, спасибо за вашу помощь."),
      ("max", "Я хочу работать поваром в ресторане."), ("vika", "Мы закрываем замок на ключ. Потом идём домой."),
      ("narrator", "That was the test. See you next time.")]
FR = [("narrator", "A short test in French. Listen to the lines first."),
      ("lea", "Bonjour, je m'appelle Léa. Je travaille à l'agence."), ("gabriel", "Enchanté. Vous voulez un café?"),
      ("lea", "Oui, avec plaisir. Merci beaucoup!"), ("narrator", "That was the French test.")]
STRESS = {"Девушка,": "Де" + A + "вушка,", "вами": "ва" + A + "ми", "порядке?": "поря" + A + "дке?", "помощь.": "по" + A + "мощь.",
          "хочу": "хочу" + A, "работать": "рабо" + A + "тать", "поваром": "по" + A + "варом", "ресторане.": "ресторане" + A + ".",
          "замок": "за" + A + "мок", "ключ.": None, "Потом": "Пото" + A + "м", "идём": None, "домой.": "домо" + A + "й."}


def make(root, sid, pair, lines):
    show, ep = ("kukhnya", "s90e01") if pair == "ru-en" else ("dix-pour-cent", "s90e01")
    sid = f"{show}-{ep}-scene-{sid}"
    d = Path(root) / "out" / show / ep
    d.mkdir(parents=True, exist_ok=True)
    segs = [{"v": v, "t": t, "gap": 0.5} for v, t in lines]
    (d / f"scene-{sid[-2:]}.json").write_text(json.dumps({"schemaVersion": 1, "id": sid, "pair": pair, "segments": segs}, ensure_ascii=False))
    nl = []
    for i, (v, t) in enumerate(lines):
        if v == "narrator":
            continue
        words = []
        for tok in t.split():
            w = {"t": tok, "stress": None}
            if pair == "ru-en" and tok in STRESS and STRESS[tok] and STRESS[tok] != tok:
                w["stress"] = STRESS[tok]
            words.append(w)
        nl.append({"seg": i, "trans": "", "words": words})
    (d / f"scene-{sid[-2:]}.notes.json").write_text(json.dumps({"lines": nl}, ensure_ascii=False))
    cast = {"kukhnya": [("max", "Аня", "f"), ("vika", "Вика", "f"), ("max", "Макс", "m")], "dix-pour-cent": [("lea", "Léa", "f"), ("gabriel", "Gabriel", "m")]}[show]
    (d.parent / "cast.json").write_text(json.dumps({"schemaVersion": 1, "show": show, "cast": [{"key": k, "ru": r, "en": [r], "gender": g} for k, r, g in cast]}, ensure_ascii=False))
    return sid


def main():
    """Writes the synthetic content tree; smoke.sh then renders it with the real pipeline and scores it with Whisper."""
    out = Path(sys.argv[1])
    root = out / "content"
    ids = [make(root, "01", "ru-en", RU), make(root, "02", "fr-en", FR)]
    (out / "scenes.txt").write_text("\n".join(ids))


main()
