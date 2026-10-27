# Authoring module for dix-pour-cent s02e02 scene 05 (cues 153-176).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e02/authoring/scene-05.py --out out/dix-pour-cent/s02e02/scene-05.json

ID = "dix-pour-cent-s02e02-scene-05"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 2
SCENE = 5
TITLE = "Le chaman de Noémie  (Noémie's Shaman)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "mathias": "theo", "gabriel": "marcel"}
LABELS = {"lea": "Noémie", "mathias": "Mathias", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E02"
SOURCE_FILE = "sources/dix-pour-cent/s02/e02.fr.dual.srt"
SOURCE_NOTE = ("Cues 153-176. Gabriel checks in at the office while Mathias loses his temper on the phone. "
               "Worried about his recent fainting spell, Noemie suggests alternative medicine and offers "
               "to introduce Mathias to her shaman. Adapted for A1 French.")

INTRO = ("Back at the ASK offices, tensions run high following Hicham's arrival as majority owner. "
         "While Gabriel checks in on his colleagues, an exhausted Mathias snaps at callers over Ramzy's departure. "
         "Worried about Mathias's health, Noemie proposes an unusual alternative cure. Let's listen to the scene in French first.")

STORY = [
 ("gabriel", "Ça va? Vous avez mangé?",
  "How are you? Have you eaten?",
  [(154, "Ça va ?"),
   (155, "Vous avez mangé ?")], ""),
 ("lea", "Oui, un soda zéro sucre.",
  "Yes, a zero-sugar soda.",
  [(156, "un soda zéro sucre.")], ""),
 ("gabriel", "Je suis juste venu proposer mon aide.",
  "I just came to offer my help.",
  [(160, "Je suis juste venu proposer mon aide.")], ""),
 ("mathias", "Agence ASK, bonjour? Je ne représente plus Ramzy!",
  "ASK agency, hello? I no longer represent Ramzy!",
  [(163, "Agence ASK, bonjour ?"),
   (164, "Je ne représente plus Ramzy.")], ""),
 ("mathias", "Je n'ai pas le numéro de son agent! Les gens sont tellement incompétents!",
  "I do not have his agent's number! People are so incompetent!",
  [(164, "Je n'ai pas le numéro de son agent !"),
   (165, "les gens sont tellement incompétents !")], ""),
 ("mathias", "Où va ce pays?",
  "What is this country coming to?",
  [(166, "Où va ce pays ?")], ""),
 ("lea", "Mathias, vous avez vu un médecin?",
  "Mathias, have you seen a doctor?",
  [(167, "Mathias, vous avez vu un médecin ?")], ""),
 ("mathias", "Il me dirait juste de dormir et faire du sport. Je n'ai pas le temps.",
  "He would just tell me to sleep and exercise. I do not have time.",
  [(168, "Il me dirait juste de dormir, faire du sport,"),
   (169, "Je n'ai pas le temps.")], ""),
 ("lea", "Des évanouissements, ça peut être grave! Vous auriez pu vous tuer!",
  "Fainting spells can be serious! You could have killed yourself!",
  [(170, "Des évanouissements, ça peut être grave."),
   (171, "Vous auriez pu vous fendre le crâne et vous tuer !")], "Simplified skull injury idiom"),
 ("lea", "Vous connaissez le chamanisme?",
  "Do you know about shamanism?",
  [(172, "Vous connaissez le chamanisme ?")], ""),
 ("mathias", "Pas vraiment. Pourquoi?",
  "Not really. Why?",
  [(173, "Pas vraiment.")], "Mathias expresses polite skepticism"),
 ("lea", "Je sais que vous êtes sceptique, mais je connais un chaman extraordinaire.",
  "I know you are skeptical, but I know an extraordinary shaman.",
  [(174, "Je sais que vous êtes sceptique"),
   (175, "Eh bien, je connais un chaman extraordinaire.")], ""),
 ("lea", "Je pourrais vous mettre en contact avec lui...",
  "I could put you in touch with him...",
  [(176, "Je pourrais vous mettre en contact avec lui...")], ""),
]

OPENER = "Let's examine how Noemie tries to help Mathias step by step."

WALK = [
 (0, None,
  "'How are you? Have you eaten?' Gabriel politely inquires after his colleagues' wellbeing."),
 (1, None,
  "'Yes, a zero-sugar soda.' Noemie answers that she has only had a quick diet drink."),
 (2, None,
  "'I just came to offer my help.' Gabriel explains his friendly presence in the reception area."),
 (3, None,
  "'ASK agency, hello? I no longer represent Ramzy!' Mathias barks into his desk telephone."),
 (4, None,
  "'I do not have his agent\\'s number! People are so incompetent!' Mathias vents his frustration at annoying phone calls."),
 (5, None,
  "'What is this country coming to?' The rhetorical question expresses exasperation at poor professional standards."),
 (6, None,
  "'Mathias, have you seen a doctor?' Noemie voices genuine concern for his physical wellbeing."),
 (7, None,
  "'He would just tell me to sleep and exercise. I do not have time.' Mathias dismisses traditional medical advice."),
 (8, None,
  "'Fainting spells can be serious! You could have killed yourself!' Noemie warns him about the dangerous consequences of passing out."),
 (9, None,
  "'Do you know about shamanism?' She introduces the topic of alternative spiritual healing."),
 (10, None,
  "'Not really. Why?' Mathias responds with polite detachment."),
 (11, None,
  "'I know you are skeptical, but I know an extraordinary shaman.' Noemie tries to overcome his scientific doubts."),
 (12, None,
  "'I could put you in touch with him...' The expression mettre en contact means to connect or introduce two people."),
]

TRANSITION = "Now let's listen to the scene once more from beginning to end."

OUTRO = ("Noemie is eager to help Mathias recover from his fainting spell by introducing him to her spiritual healer. "
         "Meanwhile, Mathias quickly pivots back to business as an aspiring young actor enters his office. "
         "See you in the next scene.")

CLOSING = ("lea", "Je pourrais vous mettre en contact avec lui...")

if __name__ == "__main__":
    import subprocess, sys
    from pathlib import Path
    root = Path(__file__).resolve().parents[4]
    out = Path(__file__).resolve().parents[1] / f"scene-{SCENE:02d}.json"
    sys.exit(subprocess.call([sys.executable, str(root / "tools/compose.py"), __file__, "--out", str(out)]))
