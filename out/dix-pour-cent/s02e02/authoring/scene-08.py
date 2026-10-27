# Authoring module for dix-pour-cent s02e02 scene 08 (cues 222-250).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e02/authoring/scene-08.py --out out/dix-pour-cent/s02e02/scene-08.json

ID = "dix-pour-cent-s02e02-scene-08"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 2
SCENE = 8
TITLE = "Gabriel défend Sofia  (Gabriel Defends Sofia)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo", "constance": "emilie"}
LABELS = {"lea": "Sofia", "gabriel": "Gabriel", "constance": "Constance"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E02"
SOURCE_FILE = "sources/dix-pour-cent/s02/e02.fr.dual.srt"
SOURCE_NOTE = ("Cues 222-250. Sofia storms into Gabriel's office furious over a casting dispute with Constance. "
               "When Constance calls in tears accusing Sofia of violence, Gabriel tries to calm both sides. "
               "Adapted for A1 French.")

INTRO = ("Inside Gabriel's office, Sofia is furious after an audition that turned into a shouting match with casting director Constance. "
         "When Constance calls in a rage to complain, Gabriel must walk a delicate line between defending his client and calming an industry heavyweight. "
         "Let's listen to the scene in French first.")

STORY = [
 ("gabriel", "Oui, ma chérie? Qu'est-ce qui ne va pas?",
  "Yes, my dear? What is wrong?",
  [(222, "Oui, ma chérie ?")], "Gabriel checks in with Sofia"),
 ("gabriel", "Je peux faire quelque chose pour vous remonter le moral?",
  "Can I do anything to cheer you up?",
  [(224, "Je peux faire quelque chose pour vous remonter le moral ?")], ""),
 ("gabriel", "Qu'est-ce que vous avez encore fait?",
  "What have you done now?",
  [(226, "Qu'est-ce que vous avez encore fait ?")], ""),
 ("gabriel", "Ce n'est pas ce que je voulais dire.",
  "That is not what I meant to say.",
  [(228, "Ce n'est pas ce que je voulais dire.")], ""),
 ("gabriel", "Laissez tomber, je vais l'appeler.",
  "Never mind, I will call her.",
  [(232, "Laissez tomber, je vais l'appeler.")], ""),
 ("gabriel", "On va arranger ça.",
  "We will sort this out.",
  [(233, "-On va arranger ça. -Dites-lui la vérité !")], ""),
 ("lea", "Dites-lui la vérité!",
  "Tell her the truth!",
  [(233, "-On va arranger ça. -Dites-lui la vérité !")], ""),
 ("gabriel", "Je m'en occupe.",
  "I will handle it.",
  [(235, "Je m'en occupe.")], ""),
 ("gabriel", "Allô, Constance, ça va?",
  "Hello, Constance, how are you?",
  [(236, "Allô, Constance, ça va ?")], ""),
 ("constance", "Vous plaisantez! Je suis complètement défigurée!",
  "Are you joking! I am completely disfigured!",
  [(238, "Vous plaisantez ! Je suis complètement défigurée !")], ""),
 ("lea", "Je l'ai à peine touchée!",
  "I barely touched her!",
  [(240, "Je l'ai à peine touchée !")], ""),
 ("gabriel", "Désolé, Constance... C'est bon, je gère.",
  "Sorry, Constance... It is fine, I will handle it.",
  [(243, "Désolé, Constance..."),
   (247, "C'est bon, je gère.")], ""),
 ("gabriel", "Calme-toi, Sofia, elle est très puissante.",
  "Calm down, Sofia, she is very powerful.",
  [(249, "Elle est très puissante.")], "Gabriel warns Sofia about Constance's influence"),
]

OPENER = "Let's examine how Gabriel tries to mediate between Sofia and Constance step by step."

WALK = [
 (0, None,
  "'Yes, my dear? What is wrong?' Gabriel addresses Sofia warmly when she enters his office in tears."),
 (1, None,
  "'Can I do anything to cheer you up?' The idiom remonter le moral means to comfort or boost someone's spirits."),
 (2, None,
  "'What have you done now?' Gabriel instinctively worries that an audition went wrong."),
 (3, None,
  "'That is not what I meant to say.' He quickly backtracks after sounding overly critical."),
 (4, None,
  "'Never mind, I will call her.' The expression laisser tomber means to drop it or let it go."),
 (5, None,
  "'We will sort this out.' The verb arranger means to fix, resolve, or sort out a difficult situation."),
 (6, None,
  "'Tell her the truth!' Sofia urges Gabriel to confront the casting director firmly."),
 (7, None,
  "'I will handle it.' The pronominal idiom s\\'en occuper means to take care of something."),
 (8, None,
  "'Hello, Constance, how are you?' Gabriel attempts a polite, friendly greeting on the phone."),
 (9, None,
  "'Are you joking! I am completely disfigured!' Constance dramatically exaggerates the altercation."),
 (10, None,
  "'I barely touched her!' The phrase a peine means scarcely or barely."),
 (11, None,
  "'Sorry, Constance... It is fine, I will handle it.' Gabriel tries to pacify both women simultaneously."),
 (12, None,
  "'Calm down, Sofia, she is very powerful.' The adjective puissante describes an influential industry figure."),
]

TRANSITION = "Now let's listen to Gabriel's difficult phone call once more."

OUTRO = ("Gabriel manages to end the call without further incident, but Constance's fury leaves Sofia's casting in jeopardy. "
         "See you in the next scene.")

CLOSING = ("gabriel", "Calme-toi, Sofia, elle est très puissante.")

if __name__ == "__main__":
    import subprocess, sys
    from pathlib import Path
    root = Path(__file__).resolve().parents[4]
    out = Path(__file__).resolve().parents[1] / f"scene-{SCENE:02d}.json"
    sys.exit(subprocess.call([sys.executable, str(root / "tools/compose.py"), __file__, "--out", str(out)]))
