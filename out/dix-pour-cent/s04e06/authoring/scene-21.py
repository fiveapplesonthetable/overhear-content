# Authoring module for dix-pour-cent s04e06 scene 21 (cues 881-911).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s04e06/authoring/scene-21.py --out overhear-content/out/dix-pour-cent/s04e06/scene-21.json

ID = "dix-pour-cent-s04e06-scene-21"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 6
SCENE = 21
TITLE = "Le visage de Gabriel  (Gabriel's Face)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo"}
LABELS = {"lea": "Andréa", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E06"
SOURCE_FILE = "sources/dix-pour-cent/s04/e06.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 881-911. Andrea confronts Gabriel in the hallway about his secret agreement with Elise Formain. "
    "Gabriel erupts in frustration, declaring that ASK is dead and he is tired of being the nice guy, before both share a tender moment."
)

INTRO = (
    "In the quiet hallway of ASK, Andrea Martel confronts Gabriel Sarda about his behind-the-scenes deal with rival agent Elise Formain. "
    "Pushing back against Andrea's accusations, Gabriel passionately defends his choices as the agency faces inevitable dissolution. "
    "Let's listen to their confrontation in French first."
)

OPENER = "Let's examine the conversation line by line and explore the French expressions."
TRANSITION = "Now let's listen to the complete discussion once more to reinforce the vocabulary."

STORY = [
    ("lea", "Pourquoi tu as fait ça, Gabriel?",
     "Why did you do that, Gabriel?",
     [(886, "Pourquoi tu as fait ça, Gabriel ?")], "Andrea demands an immediate explanation"),
    ("gabriel", "De quoi tu parles exactement?",
     "What are you talking about exactly?",
     [(887, "Qu'est-ce que j'ai fait ?")], "Gabriel tries to feign ignorance"),
    ("lea", "Tu as négocié avec Élise Formain!",
     "You negotiated with Elise Formain!",
     [(888, "Élise... Le film d'Ozon...")], "Andrea accuses him directly"),
    ("gabriel", "Je l'ai fait pour te protéger.",
     "I did it to protect you.",
     [(894, "Tu ne pouvais pas rater ce rôle, pas à cause de moi.")], "Gabriel justifies his actions"),
    ("lea", "Comment peux-tu trahir notre agence?",
     "How can you betray our agency?",
     [(898, "Comment tu peux te regarder dans la glace si tu trahis ASK ?")], "Andrea expresses disbelief"),
    ("gabriel", "Cette agence est morte, Andréa!",
     "This agency is dead, Andrea!",
     [(900, "Cette agence est morte ! Tu ne le vois pas ?")], "Gabriel speaks the painful truth"),
    ("gabriel", "C'est fini et tout le monde le sait.",
     "It is over and everyone knows it.",
     [(901, "C'est fini, tout le monde le sait.")], "Gabriel states the agency's fate"),
    ("gabriel", "J'en ai assez d'être le gentil!",
     "I have had enough of being nice!",
     [(902, "Et j'en ai marre d'être le gentil !"), (903, "J'en ai assez !")], "Gabriel vents his exhaustion"),
    ("gabriel", "C'est mon tour d'être le méchant.",
     "It is my turn to be the villain.",
     [(904, "C'est mon tour d'être le méchant !")], "Gabriel claims a new hardline persona"),
    ("gabriel", "Je vais travailler avec elle.",
     "I am going to work with her.",
     [(905, "Alors oui, je vais bosser avec cette garce")], "Gabriel confirms joining the rival"),
    ("gabriel", "Je vais surveiller cette peste.",
     "I will keep an eye on that pest.",
     [(906, "Et je vais surveiller cette peste.")], "Gabriel reveals his protective motive"),
    ("gabriel", "Même si je perds la face!",
     "Even if I lose face!",
     [(908, "Même si ça doit me coûter la face !")], "Gabriel accepts losing his pride"),
    ("lea", "Mais j'aime ton vrai visage.",
     "But I love your true face.",
     [(909, "Mais j'aime ton visage.")], "Andrea reassures him with tenderness"),
    ("gabriel", "Moi aussi j'adore ton visage.",
     "I adore your face too.",
     [(910, "Moi aussi j'aime ton visage."), (911, "J'adore ton visage...")], "Gabriel smiles through his emotion"),
]

WALK = [
    (0, None,
     "'Why did you do that, Gabriel?' Andrea demands an immediate explanation from her partner. "
     "The interrogative 'pourquoi' asks why."),
    (1, None,
     "'What are you talking about exactly?' Gabriel tries to evade the confrontation. "
     "The adverb 'exactement' means exactly."),
    (2, None,
     "'You negotiated with Elise Formain!' Andrea accuses him of betraying the agency. "
     "The verb 'negocier' signifies negotiating."),
    (3, None,
     "'I did it to protect you.' Gabriel insists he acted out of loyalty. "
     "The infinitive 'proteger' means to protect."),
    (4, None,
     "'How can you betray our agency?' Andrea cannot understand his surrender to their rival. "
     "The verb 'trahir' means to betray."),
    (5, None,
     "'This agency is dead, Andrea!' Gabriel shouts the harsh reality aloud. "
     "The feminine adjective 'morte' means dead."),
    (6, None,
     "'It is over and everyone knows it.' Gabriel faces the imminent financial collapse. "
     "The past participle 'fini' indicates completion."),
    (7, None,
     "'I have had enough of being nice!' Gabriel vents his frustration at being passive. "
     "The idiom 'en avoir assez' expresses having had enough."),
    (8, None,
     "'It is my turn to be the villain.' Gabriel embraces a ruthless attitude to survive. "
     "The noun 'mechant' designates the bad guy or villain."),
    (9, None,
     "'I am going to work with her.' Gabriel confirms his plan to join Elise's firm. "
     "The verb 'travailler' means to work."),
    (10, None,
     "'I will keep an eye on that pest.' Gabriel reveals his true undercover strategy. "
     "The noun 'peste' refers to an annoying or malicious person."),
    (11, None,
     "'Even if I lose face!' Gabriel accepts the damage to his reputation. "
     "The idiom 'perdre la face' means to lose face."),
    (12, None,
     "'But I love your true face.' Andrea responds with tender affection and understanding. "
     "The masculine noun 'visage' means face."),
    (13, None,
     "'I adore your face too.' Gabriel softens completely before his longtime friend. "
     "The verb 'adorer' means to adore or love deeply."),
]

OUTRO = (
    "In the fading halls of ASK, Gabriel and Andrea lay bare their fears and loyalty to one another. "
    "Though their agency is crumbling, the profound friendship between the two agents remains entirely unbroken. "
    "Now let's listen to the scene one last time."
)

CLOSING = ("lea", "Nous resterons toujours complices!")
