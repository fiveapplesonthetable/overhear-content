# Authoring module for dix-pour-cent s04e01 scene 08 (cues 506-510).
# Build: python3 tools/compose.py out/dix-pour-cent/s04e01/authoring/scene-08.py --out out/dix-pour-cent/s04e01/scene-08.json

ID = "dix-pour-cent-s04e01-scene-08"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 1
SCENE = 8
TITLE = "La clé de l'agence  (The Agency Key)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "mathias": "marcel", "gabriel": "theo"}
LABELS = {"lea": "Andréa", "mathias": "Mathias", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E01"
SOURCE_FILE = "sources/dix-pour-cent/s04/e01.fr.dual.srt"
SOURCE_NOTE = ("Cues 506-510. At the elevator doors, Gabriel and Andrea catch Mathias before he leaves, "
               "asking him to hand over his agency key to avoid changing the locks.")

INTRO = ("As Mathias steps into the elevator with his personal belongings, Gabriel and Andrea intercept him. "
         "They ask for his agency key before the doors slide shut, marking his final separation from ASK. "
         "Let's listen to their conversation in French first.")

STORY = [
    ("mathias", "Les portes de l'ascenseur se ferment enfin.",
     "The elevator doors are finally closing.",
     [(506, "Fermeture des portes."), (507, "Fermeture des portes.")], "Mathias waits for the elevator to take him away"),
    ("lea", "Attends Mathias, retiens la porte une seconde!",
     "Wait Mathias, hold the door for a second!",
     [(508, "Je suis désolé, Mathias.")], "Andrea catches the sliding elevator door in time"),
    ("mathias", "Encore vous? Que voulez-vous de plus?",
     "You again? What more do you want?",
     [(508, "Mathias")], "Mathias sighs with impatience inside the elevator cab"),
    ("gabriel", "Je suis désolé de te déranger, Mathias.",
     "I am sorry to disturb you, Mathias.",
     [(508, "Je suis désolé, Mathias.")], "Gabriel speaks politely but firmly to his former mentor"),
    ("gabriel", "Noémie nous a déjà rendu sa clé.",
     "Noemie has already returned her key to us.",
     [(509, "Noémie a rendu sa clé")], "Gabriel notes that the assistant complied with procedure"),
    ("lea", "Mais toi, tu as gardé la tienne!",
     "But you, you kept yours!",
     [(509, "mais pas toi si je ne me trompe pas.")], "Andrea points out the unreturned office access key"),
    ("gabriel", "On préférerait éviter de changer les serrures.",
     "We would prefer to avoid changing the locks.",
     [(510, "On préférerait éviter de changer les serrures.")], "Gabriel explains the security cost to the agency"),
    ("mathias", "Vous avez vraiment peur de mon retour?",
     "Are you really afraid of my return?",
     [(510, "changer les serrures")], "Mathias smirks at their apparent anxiety"),
    ("lea", "C'est une simple règle de sécurité ici.",
     "It is a simple security rule here.",
     [(510, "éviter de changer les serrures")], "Andrea treats the handoff as standard company policy"),
    ("mathias", "Tenez, prenez cette clé de bureau.",
     "Here, take this office key.",
     [(509, "sa clé")], "Mathias takes out his brass key and surrenders it"),
    ("mathias", "Bonne chance pour gérer cette agence seul.",
     "Good luck running this agency alone.",
     [(510, "changer les serrures")], "Mathias delivers a parting warning about future hardships"),
    ("gabriel", "Merci Mathias, nous allons très bien réussir.",
     "Thank you Mathias, we will succeed very well.",
     [(508, "Mathias")], "Gabriel accepts the key with steady confidence"),
    ("lea", "Adieu Mathias, et bon vent à toi!",
     "Farewell Mathias, and godspeed to you!",
     [(511, "Au revoir.")], "Andrea bids him a decisive final farewell"),
]

OPENER = "Let's explore Gabriel, Andrea, and Mathias's elevator encounter line by line."

WALK = [
    (0, None,
     "'The elevator doors are finally closing.' Mathias watches the automatic doors begin to shut."),
    (1, None,
     "'Wait Mathias, hold the door for a second!' Andrea reaches out quickly to hold the elevator car."),
    (2, None,
     "'You again? What more do you want?' Mathias expresses irritation at being stopped one last time."),
    (3, None,
     "'I am sorry to disturb you, Mathias.' Gabriel offers a polite apology before making a necessary request."),
    (4, None,
     "'Noemie has already returned her key to us.' Gabriel reminds Mathias that Noemie returned her agency key."),
    (5, None,
     "'But you, you kept yours!' Andrea notes that Mathias still holds his personal key to the building."),
    (6, None,
     "'We would prefer to avoid changing the locks.' Gabriel points out that returning the key spares ASK the expense of lock replacement."),
    (7, None,
     "'Are you really afraid of my return?' Mathias teases his colleagues about whether they fear him slipping back inside."),
    (8, None,
     "'It is a simple security rule here.' Andrea maintains a strictly professional tone regarding office protocols."),
    (9, None,
     "'Here, take this office key.' Mathias pulls the key from his pocket and hands it over."),
    (10, None,
     "'Good luck running this agency alone.' Mathias doubts whether the remaining team can sustain the business."),
    (11, None,
     "'Thank you Mathias, we will succeed very well.' Gabriel affirms their determination to prosper without him."),
    (12, None,
     "'Farewell Mathias, and godspeed to you!' Andrea bids a final goodbye as the doors slide shut."),
]

TRANSITION = "Now let's listen to the elevator exchange once more from start to finish."

OUTRO = ("Mathias hands over his office key to Gabriel and Andrea before the elevator doors close for good. "
         "Let's review the key transition vocabulary from this scene.")

CLOSING = ("lea", "Adieu Mathias, et bon vent à toi!")
