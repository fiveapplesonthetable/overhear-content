# Authoring module for dix-pour-cent s02e01 scene 08 (cues 171-195).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e01/authoring/scene-08.py --out out/dix-pour-cent/s02e01/scene-08.json

ID = "dix-pour-cent-s02e01-scene-08"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 1
SCENE = 8
TITLE = "Ramzy refuse de voir Virginie  (Ramzy Refuses to See Virginie)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "mathias": "theo", "ramzy": "marcel"}
LABELS = {"lea": "Sofia", "mathias": "Mathias", "ramzy": "Ramzy"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E01"
SOURCE_FILE = "sources/dix-pour-cent/s02/e01.fr.dual.srt"
SOURCE_NOTE = ("Cues 171-195. In Mathias's office, Ramzy Bedia expresses his pain over the gossip photos. "
               "Accusing Mathias of playing both sides as a double agent, Ramzy demands that he choose between them. "
               "When Sofia announces Virginie's arrival, Ramzy refuses to face her. Adapted for A1 French.")

INTRO = ("Inside Mathias's office, Ramzy Bedia confronts his agent about the humiliating paparazzi photos of Virginie Efira. "
         "Feeling betrayed and demanding total loyalty, Ramzy refuses to share an agent with Virginie. "
         "Let's listen to the scene in French first.")

STORY = [
 ("mathias", "Ne t'inquiète pas, personne ne nous dérangera ici. Thé ou café?",
  "Do not worry, no one will bother us here. Tea or coffee?",
  [(171, "Ne t'inquiète pas, personne ne nous dérangera ici."),
   (173, "-Tu étais au courant ? -Thé ou café ?")], ""),
 ("ramzy", "Tu étais au courant? Elle t'a appelé à trois heures du matin.",
  "Did you know? She called you at three o'clock in the morning.",
  [(173, "-Tu étais au courant ? -Thé ou café ?"),
   (174, "Elle t'a appelé à 3h09 du matin.")], "Spelled out time to standard French"),
 ("ramzy", "Qu'est-ce qu'elle t'a dit?",
  "What did she say to you?",
  [(175, "Qu'est-ce qu'elle t'a dit ?")], ""),
 ("mathias", "Mon rôle est de vous protéger tous les deux, votre vie privée ne me regarde pas.",
  "My role is to protect both of you, your private life does not concern me.",
  [(176, "Mon rôle"),
   (177, "est de vous protéger tous les deux, votre vie privée ne me regarde pas,")], ""),
 ("mathias", "Mais quand elle est attaquée, je la défends. On va attaquer en justice, et soyez sûrs qu'on gagnera.",
  "But when it is attacked, I defend it. We will sue in court, and be sure we will win.",
  [(178, "mais quand elle est attaquée, je la défends."),
   (179, "On va attaquer en justice, et soyez sûrs qu'on gagnera.")], ""),
 ("ramzy", "Ça n'atténuera pas mon humiliation publique.",
  "That will not diminish my public humiliation.",
  [(180, "Ça n'atténuera pas mon humiliation publique.")], ""),
 ("ramzy", "Elle a appelé et laissé un message?",
  "Did she call and leave a message?",
  [(184, "Elle a appelé et laissé un message ?")], ""),
 ("mathias", "Non, mais elle pourrait, je suis son agent aussi.",
  "No, but she could, I am her agent too.",
  [(185, "Non, mais elle pourrait, je suis son agent aussi.")], ""),
 ("ramzy", "C'est bien le problème, tu es un agent double!",
  "That is the exact problem, you are a double agent!",
  [(186, "C'est bien le problème, tu es un agent double !")], ""),
 ("mathias", "Pas tout à fait, je suis l'agent de vous deux.",
  "Not quite, I am the agent of both of you.",
  [(187, "Pas tout à fait, je suis l'agent de vous deux.")], ""),
 ("ramzy", "Eh bien, maintenant il faut choisir.",
  "Well, now you must choose.",
  [(188, "Eh bien, maintenant il faut choisir.")], ""),
 ("lea", "Pardon de vous déranger, Mathias. Virginie Efira est là.",
  "Sorry to disturb you, Mathias. Virginie Efira is here.",
  [(191, "Oui, Sofia ?"),
   (192, "Virginie Efira est là.")], "Sofia announces Virginie's arrival"),
 ("ramzy", "Tu vois? Fais ce qu'il faut, je ne veux pas la voir.",
  "See? Do what is necessary, I do not want to see her.",
  [(193, "Tu vois ? Je ne veux pas la voir."),
   (194, "Fais ce qu'il faut,"),
   (195, "je ne veux pas la voir.")], ""),
]

OPENER = "Let's examine how Ramzy confronts Mathias about his conflict of interest step by step."

WALK = [
 (0, None,
  "'Do not worry, no one will bother us here. Tea or coffee?' Mathias welcomes Ramzy into his private office to speak calmly."),
 (1, None,
  "'Did you know? She called you at three o'clock in the morning.' Ramzy checks whether Mathias knew about the affair before anyone else."),
 (2, None,
  "'What did she say to you?' Ramzy demands details of their late-night phone call."),
 (3, None,
  "'My role is to protect both of you, your private life does not concern me.' The expression ne regarder pas means to be none of one's business."),
 (4, None,
  "'But when it is attacked, I defend it. We will sue in court, and be sure we will win.' The phrase attaquer en justice means to take legal action against the magazine."),
 (5, None,
  "'That will not diminish my public humiliation.' Ramzy feels deeply disgraced by the widely circulated pictures."),
 (6, None,
  "'Did she call and leave a message?' Ramzy wonders if Virginie tried to explain herself."),
 (7, None,
  "'No, but she could, I am her agent too.' Mathias reminds him that his professional loyalty extends to both clients."),
 (8, None,
  "'That is the exact problem, you are a double agent!' Ramzy angrily accuses Mathias of being torn between competing loyalties."),
 (9, None,
  "'Not quite, I am the agent of both of you.' The phrase pas tout a fait means not quite or not exactly."),
 (10, None,
  "'Well, now you must choose.' Ramzy issues an uncompromising ultimatum to his representative."),
 (11, None,
  "'Sorry to disturb you, Mathias. Virginie Efira is here.' Sofia steps into the office to announce the unexpected visitor."),
 (12, None,
  "'See? Do what is necessary, I do not want to see her.' Ramzy firmly refuses to speak to Virginie in person."),
]

TRANSITION = "Now let's listen to the heated confrontation between Ramzy and Mathias once more."

OUTRO = ("Ramzy has delivered an ultimatum to Mathias, forcing him to choose between representing him or Virginie. "
         "To prevent an open clash in the lobby, Mathias must quickly keep the two estranged stars apart. "
         "See you in the next scene.")

CLOSING = ("ramzy", "Fais ce qu'il faut, je ne veux pas la voir.")

if __name__ == "__main__":
    import subprocess, sys
    from pathlib import Path
    root = Path(__file__).resolve().parents[4]
    out = Path(__file__).resolve().parents[1] / f"scene-{SCENE:02d}.json"
    sys.exit(subprocess.call([sys.executable, str(root / "tools/compose.py"), __file__, "--out", str(out)]))
