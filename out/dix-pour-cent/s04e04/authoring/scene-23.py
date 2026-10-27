ID = "dix-pour-cent-s04e04-scene-23"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 4
SCENE = 23
TITLE = "Vos méthodes sont révoltantes  (Your methods are revolting)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E04"
SOURCE_FILE = "sources/dix-pour-cent/s04/e04.fr.dual.srt"

VOICES = {
    "narrator": "sky",
    "mathias": "theo",
    "lea": "lucie"
}

INTRO = (
    "Mathias is furious about what happened to Camille. "
    "He decides to call the author, Ulrika, to cancel their secret deal. "
    "We'll hear it in French first, don't worry about catching every word."
)
OPENER = "Let's go back through it. Mathias makes his call."
TRANSITION = "Let's listen to the whole scene again."
OUTRO = "Mathias has finally made his choice."

STORY = [
    ("lea", "Allô?", "Hello?", [(1207, "Allô ?")], ""),
    ("mathias", "Ulrika?", "Is this Ulrika?", [(1207, "Ulrika ?")], ""),
    ("mathias", "Ici Mathias Barneville.", "This is Mathias Barneville speaking.", [(1208, "Ici Mathias Barneville.")], ""),
    ("lea", "Oui, bonjour Mathias.", "Yes, hello Mathias.", [], ""),
    ("mathias", "Camille m'a tout dit.", "Camille told me everything.", [(1209, "Camille m'a tout dit.")], ""),
    ("mathias", "Je sais la vérité.", "I know the truth.", [], ""),
    ("lea", "Mais Mathias, attendez.", "But Mathias, wait.", [], ""),
    ("mathias", "Non, c'est terminé.", "No, it's over.", [], ""),
    ("mathias", "Vos méthodes sont révoltantes.", "Your methods are revolting.", [(1209, "Vos méthodes sont révoltantes,")], ""),
    ("mathias", "Je refuse de travailler avec vous.", "I refuse to work with you.", [], ""),
    ("lea", "Vous faites une erreur.", "You are making a mistake.", [], ""),
    ("mathias", "Ne me rappelez plus jamais.", "Don't ever call me again.", [(1210, "ne me rappelez plus jamais.")], ""),
    ("mathias", "Au revoir, Ulrika.", "Goodbye, Ulrika.", [], "")
]

WALK = [
    (0, None, "'Hello?' The author answers the phone."),
    (1, None, "'Ulrika?' He confirms it is her on the line."),
    (2, None, "'This is Mathias Barneville.' He introduces himself formally with his full name."),
    (3, None, "'Yes, hello Mathias.' She replies calmly."),
    (4, None, "'Camille told me everything.' He says Camille confessed about the scheme."),
    (5, None, "'I know the truth.' He knows all the details now."),
    (6, None, "'But Mathias, wait.' She tries to stop him from speaking."),
    (7, None, "'No, it is over.' He refuses to listen to her excuses."),
    (8, None, "'Your methods are revolting.' He condemns her terrible actions."),
    (9, None, "'I refuse to work with you.' He cancels their secret deal completely."),
    (10, None, "'You are making a mistake.' She tries to warn him."),
    (11, None, "'Do not ever call me again.' He gives a strict instruction to stay away."),
    (12, None, "'Goodbye, Ulrika.' He says farewell and cuts the line.")
]

LABELS = {
    "lea": "Ulrika",
    "mathias": "Mathias"
}

CLOSING = ("mathias", "Au revoir.")
