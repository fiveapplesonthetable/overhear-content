# Authoring module for dix-pour-cent s02e01 scene 07 (cues 150-170).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e01/authoring/scene-07.py --out out/dix-pour-cent/s02e01/scene-07.json

ID = "dix-pour-cent-s02e01-scene-07"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 1
SCENE = 7
TITLE = "Réunion de crise financière  (Financial Crisis Meeting)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "mathias": "theo", "gabriel": "marcel"}
LABELS = {"lea": "Andréa", "mathias": "Mathias", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E01"
SOURCE_FILE = "sources/dix-pour-cent/s02/e01.fr.dual.srt"
SOURCE_NOTE = ("Cues 150-170. Mathias gathers the partners in the conference room to reveal ASK's alarming debt. "
               "Facing a 500,000 euro tax penalty, he proposes a two-month salary reduction. "
               "Andrea and Gabriel vigorously reject the austerity measure. Adapted for A1 French.")

INTRO = ("In the ASK conference room, Mathias calls an urgent meeting of the agency partners to discuss their dire finances. "
         "Between sluggish film productions and a massive five hundred thousand euro tax bill, drastic measures are needed immediately. "
         "Let's listen to the scene in French first.")

STORY = [
 ("mathias", "Tout le monde est là? On peut commencer.",
  "Is everyone here? We can get started.",
  [(150, "Tout le monde est là ?")], "Mathias opens the crisis meeting"),
 ("lea", "Tu vois bien que oui. Qu'est-ce qui se passe?",
  "You can see we are. What is going on?",
  [(151, "Tu vois bien que oui.")], "Andrea asks for the agenda"),
 ("mathias", "Voilà, on a eu six mois difficiles.",
  "Well, we have had six difficult months.",
  [(152, "Voilà, on a eu six mois difficiles.")], ""),
 ("mathias", "Monter des films est compliqué, et on a des contrats en suspens.",
  "Setting up films is complicated, and we have contracts on hold.",
  [(153, "on a des contrats en suspens...")], ""),
 ("mathias", "Sans compter le nouveau cadre sur les salaires, nos bénéfices sont en baisse.",
  "Not to mention the new rules on salaries, our profits are down.",
  [(154, "Sans compter le nouveau cadre sur les salaires des comédiens..."),
   (155, "Nos bénéfices sont en baisse sur le premier semestre.")], ""),
 ("mathias", "On pourrait s'en sortir, mais nous avons un redressement fiscal de cinq cent mille euros.",
  "We could get by, but we have a tax audit of five hundred thousand euros.",
  [(156, "On pourrait s'en sortir"),
   (157, "si Mme Brancillon ne nous avait pas frappés"),
   (158, "avec un redressement fiscal de 500 000 €.")], "Spelled out €500,000 in French words"),
 ("gabriel", "Cinq cent mille euros? C'est absurde!",
  "Five hundred thousand euros? That is absurd!",
  [(168, "C'est absurde.")], "Gabriel reacts with shock to the penalty"),
 ("lea", "Dommage que la femme de Mathias n'ait pas pris de parts.",
  "Too bad Mathias's wife did not take shares.",
  [(160, "Dommage que la femme de Mathias n'ait pas pris de parts.")], ""),
 ("mathias", "Mais elle n'en a pas pris. En conclusion...",
  "But she did not take any. In conclusion...",
  [(161, "Mais elle n'en a pas pris."),
   (162, "En conclusion...")], ""),
 ("mathias", "Notre seule option est de réduire les salaires pendant deux mois.",
  "Our only option is to reduce salaries for two months.",
  [(164, "Notre seule option est de réduire les salaires pendant deux mois.")], "Mathias announces the salary cuts"),
 ("gabriel", "Pardon? Les salaires de qui?",
  "Excuse me? Whose salaries?",
  [(165, "Pardon ?"),
   (166, "-Les salaires de qui ? -De tout le monde.")], ""),
 ("mathias", "Les salaires de tout le monde. Il n'y a pas d'autre solution.",
  "Everyone's salaries. There is no other solution.",
  [(166, "-Les salaires de qui ? -De tout le monde.")], ""),
 ("lea", "Hors de question, si vous réduisez le mien, je vais crever de faim!",
  "Out of the question, if you reduce mine, I will starve!",
  [(167, "Hors de question, si vous réduisez le mien, je vais crever de faim.")], "Andrea refuses any salary sacrifice"),
 ("gabriel", "C'est absurde, je suis d'accord!",
  "It is absurd, I agree!",
  [(168, "C'est absurde."),
   (170, "Je suis d'accord !")], "Gabriel sides with Andrea against the proposal"),
]

OPENER = "Let's examine how the partners react to the emergency financial proposal step by step."

WALK = [
 (0, None,
  "'Is everyone here? We can get started.' Mathias checks the attendance around the conference table."),
 (1, None,
  "'You can see we are. What is going on?' Andrea impatiently presses for the reason behind the sudden gathering."),
 (2, None,
  "'Well, we have had six difficult months.' Mathias begins his gloomy financial summary of the past semester."),
 (3, None,
  "'Setting up films is complicated, and we have contracts on hold.' The phrase en suspens indicates pending agreements."),
 (4, None,
  "'Not to mention the new rules on salaries, our profits are down.' Decreasing revenues have tightened cash flow."),
 (5, None,
  "'We could get by, but we have a tax audit of five hundred thousand euros.' The audit by tax inspector Brancillon has created an immediate crisis."),
 (6, None,
  "'Five hundred thousand euros? That is absurd!' Gabriel expresses genuine disbelief at the astronomical tax penalty."),
 (7, None,
  "'Too bad Mathias\\'s wife did not take shares.' Andrea laments that Catherine refused to invest her personal fortune into ASK."),
 (8, None,
  "'But she did not take any. In conclusion...' Mathias cuts off the discussion about his private life."),
 (9, None,
  "'Our only option is to reduce salaries for two months.' He proposes a temporary wage reduction across the board."),
 (10, None,
  "'Excuse me? Whose salaries?' Gabriel is stunned by the idea that employees and partners should take pay cuts."),
 (11, None,
  "'Everyone\\'s salaries. There is no other solution.' Mathias insists that survival requires equal sacrifice."),
 (12, None,
  "'Out of the question, if you reduce mine, I will starve!' The colloquial expression crever de faim emphasizes extreme indignation."),
 (13, None,
  "'It is absurd, I agree!' Gabriel backs Andrea and rejects the proposed payroll reductions."),
]

TRANSITION = "Now let's listen to the tense partners meeting once more."

OUTRO = ("The partners are in open revolt against Mathias's austerity plan, refusing to accept any salary reductions. "
         "Meanwhile, Ramzy Bedia waits anxiously in Mathias's private office, determined to confront his agent about "
         "the humiliating magazine cover. See you in the next scene.")

CLOSING = ("lea", "Hors de question, si vous réduisez le mien, je vais crever de faim!")

if __name__ == "__main__":
    import subprocess, sys
    from pathlib import Path
    root = Path(__file__).resolve().parents[4]
    out = Path(__file__).resolve().parents[1] / f"scene-{SCENE:02d}.json"
    sys.exit(subprocess.call([sys.executable, str(root / "tools/compose.py"), __file__, "--out", str(out)]))
