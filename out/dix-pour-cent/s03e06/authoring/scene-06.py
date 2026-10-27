# Authoring module for dix-pour-cent s03e06 scene 06 (cues 363-387).
# Build: python3 tools/compose.py out/dix-pour-cent/s03e06/authoring/scene-06.py --out out/dix-pour-cent/s03e06/scene-06.json

ID = "dix-pour-cent-s03e06-scene-06"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 6
SCENE = 6
TITLE = "L'homonyme  (The Namesake)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "isabelle": "emilie"}
LABELS = {"lea": "Andréa", "isabelle": "Isabelle"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E06"
SOURCE_FILE = "sources/dix-pour-cent/s03/e06.fr.dual.srt"
SOURCE_NOTE = ("Cues 363-387. Andrea tracks down a hospital nurse whose legal name is Isabelle Huppert, "
               "attempting to pitch her a movie role for an immediate afternoon shoot. Adapted for A1 French.")

INTRO = ("In a Paris hospital corridor, Andrea Martel tracks down a hospital worker named Isabelle Huppert. "
         "Desperate to solve a movie production crisis, Andrea pitches an acting role to the bewildered nurse. "
         "Let's listen to their encounter in French first.")

STORY = [
    ("lea", "Bonjour, vous êtes bien Isabelle Huppert?",
     "Hello, are you indeed Isabelle Huppert?",
     [(363, "Isabelle Huppert ?")], "Andrea confirms the woman's name"),
    ("isabelle", "Oui, c'est moi, pourquoi cette question?",
     "Yes, that is me, why that question?",
     [(364, "Oui ?")], "Isabelle wonders why she is addressed"),
    ("lea", "Je suis Andréa Martel, agente artistique.",
     "I am Andrea Martel, talent agent.",
     [(365, "Bonjour, Andréa Martel de l'agence INSCA")], "Andrea introduces herself"),
    ("lea", "Nous aimerions vous proposer un rôle.",
     "We would like to offer you a role.",
     [(372, "c'est à vous que nous aimerions proposer un rôle.")], "Andrea reveals her bold proposition"),
    ("isabelle", "Un rôle d'actrice au cinéma?",
     "An acting role in cinema?",
     [(374, "Dans un film.")], "Isabelle reacts with skepticism"),
    ("isabelle", "Je vous arrête tout de suite.",
     "Let me stop you right there.",
     [(377, "Je vous arrête tout de suite.")], "Isabelle tries to cut the conversation short"),
    ("isabelle", "Le showbiz n'est pas mon truc!",
     "Show business is not my thing!",
     [(378, "c'est pas du tout mon truc.")], "Isabelle dismisses the entertainment world"),
    ("lea", "Attendez, je n'ai rien expliqué encore!",
     "Wait, I have not explained anything yet!",
     [(380, "Attendez.")], "Andrea pleads for a hearing"),
    ("lea", "C'est vraiment pas grand-chose à faire.",
     "It is really not a big deal to do.",
     [(382, "c'est vraiment pas grand-chose.")], "Andrea downplays the difficulty"),
    ("lea", "Nous en avons juste pour cet après-midi.",
     "We only need you for this afternoon.",
     [(383, "On en a juste pour cet après-midi")], "Andrea specifies the brief timeframe"),
    ("isabelle", "C'est pour aujourd'hui en plus?",
     "It is for today on top of that?",
     [(384, "C'est pour aujourd'hui, en plus ?")], "Isabelle is shocked by the urgency"),
    ("lea", "Oui, cela peut être très amusant!",
     "Yes, it can be very fun!",
     [(383, "ça peut être vraiment très amusant.")], "Andrea tries enthusiasm"),
    ("isabelle", "Je travaille et je suis de garde!",
     "I work and I am on duty!",
     [(387, "je suis de garde à l'hôpital.")], "Isabelle cites hospital duty"),
]

OPENER = "Let's explore how Andrea pitches an acting role to an ordinary hospital nurse line by line."

WALK = [
    (0, None,
     "'Hello, are you indeed Isabelle Huppert?' Andrea approaches the hospital worker to verify her identity."),
    (1, None,
     "'Yes, that is me, why that question?' Isabelle is puzzled by the stranger addressing her by full name."),
    (2, None,
     "'I am Andrea Martel, talent agent.' Andrea introduces her profession with confident energy."),
    (3, None,
     "'We would like to offer you a role.' Andrea explains her surprising proposal to a non-actress."),
    (4, None,
     "'An acting role in cinema?' Isabelle questions the bizarre proposition in disbelief."),
    (5, None,
     "'Let me stop you right there.' Isabelle cuts off the sales pitch before it goes further."),
    (6, None,
     "'Show business is not my thing!' Isabelle expresses her complete lack of interest in glamour."),
    (7, None,
     "'Wait, I have not explained anything yet!' Andrea begs for a few moments to clarify the situation."),
    (8, None,
     "'It is really not a big deal to do.' Andrea attempts to minimize the acting requirements."),
    (9, None,
     "'We only need you for this afternoon.' Andrea stresses the short duration of the shoot."),
    (10, None,
     "'It is for today on top of that?' Isabelle is astonished by the immediate timeframe."),
    (11, None,
     "'Yes, it can be very fun!' Andrea paints the shoot as an enjoyable adventure."),
    (12, None,
     "'I work and I am on duty!' Isabelle points out her real-world medical responsibilities."),
]

TRANSITION = "Now let's listen to this unusual hospital dialogue once more from beginning to end."

OUTRO = ("Andrea encounters firm resistance from an everyday healthcare worker with a famous name. "
         "Let's review the essential vocabulary from this hospital conversation.")

CLOSING = ("isabelle", "Je travaille et je suis de garde!")
