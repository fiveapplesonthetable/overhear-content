ID = "dix-pour-cent-s04e05-scene-16"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 5
SCENE = 16
TITLE = "Petites coupures  (Small Bills)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "herve": "theo", "gabriel": "marcel"}
LABELS = {"lea": "Andréa", "herve": "Hervé", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E05"
SOURCE_FILE = "sources/dix-pour-cent/s04/e05.fr.dual.srt"

INTRO = (
    "At the ASK agency reception, Herve brings an envelope filled with small banknotes as Gabriel urgently requested to resolve a talent crisis. "
    "Relieved that the plan worked, Gabriel thanks his faithful assistant. Let's listen to their conversation in French first."
)

STORY = [
    ("herve", "J'ai fait ce que vous m'avez demandé.", "I did what you asked me.", [(733, "J'ai fait ce que vous m'avez demandé")], ""),
    ("gabriel", "C'est bien.", "It is good.", [], "Padding"),
    ("herve", "En petites coupures.", "In small bills.", [(733, "En petites coupures")], ""),
    ("gabriel", "Merci, Hervé.", "Thank you, Hervé.", [], "Padding"),
    ("herve", "Ça marche, hein?", "It works, right?", [(734, "Ça marche, hein")], ""),
    ("gabriel", "Oui, ça marche.", "Yes, it works.", [], "Padding"),
    ("gabriel", "Elle est incroyable.", "She is incredible.", [(735, "Elle est incroyable")], ""),
    ("herve", "Vraiment.", "Truly.", [], "Padding"),
    ("gabriel", "Tu peux y aller.", "You can go.", [], "Padding"),
    ("herve", "D'accord, je pars.", "Okay, I am leaving.", [], "Padding"),
    ("gabriel", "À plus tard.", "See you later.", [], "Padding"),
    ("herve", "Oui, à tout à l'heure.", "Yes, see you later.", [], "Padding"),
    ("gabriel", "Bon travail.", "Good work.", [], "Padding"),
    ("herve", "Au revoir.", "Goodbye.", [], "Padding")
]

WALK = [
    (0, "J'ai fait ce que vous m'avez demandé.", "'I did what you asked me.' Herve reports proudly."),
    (1, "C'est bien.", "'It is good.' Gabriel nods in approval."),
    (2, "En petites coupures.", "'In small bills.' Herve clarifies, confirming the banknote sizes."),
    (3, "Merci, Hervé.", "'Thank you, Hervé.' Gabriel says, taking the money."),
    (4, "Ça marche, hein?", "'It works, right?' Herve smiles, pleased with the result."),
    (5, "Oui, ça marche.", "'Yes, it works.' Gabriel agrees with relief."),
    (6, "Elle est incroyable.", "'She is incredible.' Gabriel says about the actress."),
    (7, "Vraiment.", "'Truly.' Herve agrees, nodding his head."),
    (8, "Tu peux y aller.", "'You can go.' Gabriel dismisses his assistant."),
    (9, "D'accord, je pars.", "'Okay, I am leaving.' Herve says, turning around."),
    (10, "À plus tard.", "'See you later.' Gabriel adds politely."),
    (11, "Oui, à tout à l'heure.", "'Yes, see you later.' Herve replies from the door."),
    (12, "Bon travail.", "'Good work.' Gabriel calls out finally."),
    (13, "Au revoir.", "'Goodbye.' Herve finishes.")
]
OPENER = "Let's walk through it."
TRANSITION = "Now let's hear the whole thing."
OUTRO = "That's it for this scene. Goodbye!"
CLOSING = ("lea", "Au revoir.")
