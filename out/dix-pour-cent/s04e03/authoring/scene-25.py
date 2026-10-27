# Authoring module for dix-pour-cent s04e03 scene 25 (cues 1044-1083).
# Build: python3 tools/compose.py out/dix-pour-cent/s04e03/authoring/scene-25.py --out out/dix-pour-cent/s04e03/scene-25.json

ID = "dix-pour-cent-s04e03-scene-25"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 3
SCENE = 25
TITLE = "Une révélation inattendue  (An Unexpected Revelation)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "herve": "theo", "valerie": "emilie"}
LABELS = {"lea": "Camille", "herve": "Hervé", "valerie": "Valérie"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E03"
SOURCE_FILE = "sources/dix-pour-cent/s04/e03.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 1044-1083. Director Valerie Donzelli drops by ASK with a surprise announcement: she wants Herve to play a lead role in her movie. "
    "After she leaves, Camille promises to keep Herve's new acting secret safe from Gabriel."
)

INTRO = (
    "Director Valerie Donzelli drops by ASK with a surprise announcement: she wants Herve to play a lead role in her movie. After she leaves, Camille promises to keep Herve's new acting secret safe from Gabriel. Let's listen to the scene in French first."
)

STORY = [
    ("valerie", "Hervé, j'ai une excellente nouvelle.",
     "Herve, I have excellent news.",
     [(1056, "bonne nouvelle")], "Valerie enters with an enthusiastic smile"),
    ("herve", "Vous avez choisi mon acteur Alex?",
     "Did you choose my actor Alex?",
     [(1057, "Vous avez choisi mon Alex")], "Herve asks hopefully"),
    ("valerie", "Non, j'ai choisi son grand frère.",
     "No, I chose his big brother.",
     [(1059, "trouvé son frère")], ""),
    ("valerie", "Et ce frère, c'est vous, Hervé!",
     "And that brother is you, Herve!",
     [(1061, "Parce que c'est vous")], "Reveals her surprising choice"),
    ("valerie", "Vous seul pouvez jouer ce rôle.",
     "Only you can play this role.",
     [(1062, "Vous seul pouvez jouer ce rôle")], ""),
    ("valerie", "Vous étiez vraiment remarquable au casting.",
     "You were truly remarkable at the audition.",
     [(1063, "Vous étiez remarquable au casting")], "Praises his natural comedic charm"),
    ("herve", "Moi? Je ne suis pas acteur!",
     "Me? I am not an actor!",
     [(1071, "Moi non plus")], "Herve gasps in utter astonishment"),
    ("lea", "Je ne savais pas ton talent.",
     "I did not know your talent.",
     [(1070, "tu voulais être acteur")], "Camille smiles encouragingly"),
    ("lea", "Tu crois que tu diras oui?",
     "Do you think you will say yes?",
     [(1075, "Tu crois que tu vas dire oui")], ""),
    ("herve", "Je ne peux rien dire à Gabriel.",
     "I cannot say anything to Gabriel.",
     [(1078, "annoncer à Gabriel")], "Worries about his boss's reaction"),
    ("lea", "Personne ne t'oblige à lui parler.",
     "Nobody is forcing you to tell him.",
     [(1079, "Personne ne t'y oblige")], "Reassures him warmly"),
    ("lea", "Je sais très bien garder les secrets.",
     "I am very good at keeping secrets.",
     [(1081, "garder les secrets")], "Pledges complete confidentiality"),
    ("herve", "C'est le début d'une aventure secrète!",
     "This is the start of a secret adventure!",
     [(1081, "garder les secrets")], "Herve smiles with growing excitement"),
    ("lea", "Félicitations pour ton premier rôle, Hervé!",
     "Congratulations on your first role, Herve!",
     [(1081, "garder les secrets")], "Camille congratulates her beaming friend"),
]

OPENER = "Let's examine Herve's surprise transition from assistant to actor line by line."

WALK = [
    (0, None,
     "'Herve, I have excellent news.' Valerie opens the meeting with an exciting announcement."),
    (1, None,
     "'Did you choose my actor Alex?' Herve assumes his client secured the casting."),
    (2, None,
     "'No, I chose his big brother.' Valerie clarifies that she picked a different character."),
    (3, None,
     "'And that brother is you, Herve!' Valerie reveals her surprising casting decision."),
    (4, None,
     "'Only you can play this role.' Valerie insists that Herve is unique for the part."),
    (5, None,
     "'You were truly remarkable at the audition.' Valerie praises his natural screen presence."),
    (6, None,
     "'Me? I am not an actor!' Herve gasps with shock at the unexpected proposition."),
    (7, None,
     "'I did not know your talent.' Camille smiles and compliments her fellow assistant."),
    (8, None,
     "'Do you think you will say yes?' Camille asks whether he plans to accept."),
    (9, None,
     "'I cannot say anything to Gabriel.' Herve fears his boss will disapprove."),
    (10, None,
     "'Nobody is forcing you to tell him.' Camille reassures him that he has options."),
    (11, None,
     "'I am very good at keeping secrets.' Camille offers her complete confidentiality."),
    (12, None,
     "'This is the start of a secret adventure!' Herve accepts the challenge with excitement."),
    (13, None,
     "'Congratulations on your first role, Herve!' Camille celebrates his dramatic breakthrough."),
]

TRANSITION = "Now listen to the whole scene again at normal speed, and see how much more you catch."
OUTRO = "Stunned by Valerie Donzelli's offer to cast him in her film, Herve worries about Gabriel's reaction, but Camille pledges total secrecy as Herve embarks on his secret acting debut."
CLOSING = ("valerie", "Vous seul pouvez jouer ce rôle.")
