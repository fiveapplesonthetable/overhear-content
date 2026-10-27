# Authoring module for dix-pour-cent s04e06 scene 27 (cue 1042).
# Build: python3 tools/compose.py out/dix-pour-cent/s04e06/authoring/scene-27.py --out out/dix-pour-cent/s04e06/scene-27.json

ID = "dix-pour-cent-s04e06-scene-27"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 6
SCENE = 27
TITLE = "Dernier pas dans la rue  (Last Step into the Street)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo"}
LABELS = {"lea": "Andréa", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E06"
SOURCE_FILE = "sources/dix-pour-cent/s04/e06.fr.dual.srt"
SOURCE_NOTE = (
    "Cue 1042. Outside on the Paris pavement at night, Andrea and Gabriel say their final goodbyes, "
    "ready to embrace their new lives while preserving their lifelong friendship."
)

INTRO = (
    "Stepping out into the cool Parisian evening, Andrea and Gabriel walk down onto the pavement outside the building. "
    "Free from the endless agency emergencies, they look toward their new lives with calm optimism and promise to stay close friends as they say their final goodbyes. "
    "Let's listen to their conversation in French first."
)

OPENER = "Let's follow Andrea and Gabriel into the cool night step by step."

STORY = [
    ("lea", "L'air de la nuit est frais.", "The night air is cool.",
     [(1042, "Céline")], ""),
    ("gabriel", "Paris est magnifique à cette heure.", "Paris is magnificent at this hour.",
     [(1042, "Céline")], ""),
    ("lea", "Où vas-tu aller ce soir?", "Where are you going to go tonight?",
     [(1042, "Céline")], ""),
    ("gabriel", "Je rentre tranquillement chez moi.", "I am going home quietly.",
     [(1042, "Céline")], ""),
    ("lea", "Et moi, je retrouve ma famille.", "And me, I am joining my family.",
     [(1042, "Céline")], ""),
    ("gabriel", "Prends bien soin de ta fille.", "Take good care of your daughter.",
     [(1042, "Céline")], ""),
    ("lea", "Flora grandit si vite déjà.", "Flora grows up so fast already.",
     [(1042, "Céline")], ""),
    ("gabriel", "Tu seras une mère admirable.", "You will be an admirable mother.",
     [(1042, "Céline")], ""),
    ("lea", "Et toi, un excellent scénariste!", "And you, an excellent screenwriter!",
     [(1042, "Céline")], ""),
    ("gabriel", "On s'appelle dès demain matin?", "We call each other tomorrow morning?",
     [(1042, "Céline")], ""),
    ("lea", "Promis, nous prendrons un café.", "Promised, we will have a coffee.",
     [(1042, "Céline")], ""),
    ("gabriel", "Prends soin de toi, Andréa.", "Take care of yourself, Andrea.",
     [(1042, "Céline")], ""),
    ("lea", "Merci pour tout, mon cher ami.", "Thank you for everything, my dear friend.",
     [(1042, "Céline")], ""),
    ("gabriel", "Au revoir, et à bientôt.", "Goodbye, and see you soon.",
     [(1042, "Céline")], ""),
]

WALK = [
    (0, None,
     "'The night air is cool.' Andrea breathes in the fresh air on the pavement."),
    (1, None,
     "'Paris is magnificent at this hour.' Gabriel looks up at the illuminated street."),
    (2, None,
     "'Where are you going to go tonight?' Andrea asks about what he will do."),
    (3, None,
     "'I am going home quietly.' Gabriel says that he is going home to rest."),
    (4, None,
     "'And me, I am joining my family.' Andrea smiles as she mentions her home."),
    (5, None,
     "'Take good care of your daughter.' Gabriel offers a gentle word of advice."),
    (6, None,
     "'Flora grows up so fast already.' Andrea speaks with great maternal pride."),
    (7, None,
     "'You will be an admirable mother.' Gabriel encourages her with sincere warmth."),
    (8, None,
     "'And you, an excellent screenwriter!' Andrea celebrates his creative talent with joy."),
    (9, None,
     "'We call each other tomorrow morning?' Gabriel proposes that they stay in touch."),
    (10, None,
     "'Promised, we will have a coffee.' Andrea makes a warm promise to meet him."),
    (11, None,
     "'Take care of yourself, Andrea.' Gabriel hugs her on the quiet sidewalk."),
    (12, None,
     "'Thank you for everything, my dear friend.' Andrea thanks him for his support."),
    (13, None,
     "'Goodbye, and see you soon.' Gabriel waves as they walk into the night."),
]

TRANSITION = "Now listen to the whole scene again at normal speed, and see how much more you catch."
OUTRO = "Under the warm streetlights of Paris, Andrea and Gabriel share a loving embrace and promise to meet for coffee, stepping forward together into the next chapter of their lives."
CLOSING = ("gabriel", "Au revoir, et à bientôt.")
