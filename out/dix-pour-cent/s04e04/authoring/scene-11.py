# Authoring module for dix-pour-cent s04e04 scene 11 (cues 876-885).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s04e04/authoring/scene-11.py --out overhear-content/out/dix-pour-cent/s04e04/scene-11.json

ID = "dix-pour-cent-s04e04-scene-11"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 4
SCENE = 11
TITLE = "La robe dorée  (The Golden Dress)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo"}
LABELS = {"lea": "Sofia", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E04"
SOURCE_FILE = "sources/dix-pour-cent/s04/e04.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 876-885. Arriving at ASK in a glamorous golden gown from a nearby photoshoot, "
    "Sofia Leprince is playfully greeted by Gabriel as Charlize Theron. When Gabriel tells her "
    "Camille is in a meeting, Sofia heads to Camille's office to wait for her agent."
)

INTRO = (
    "Sofia Leprince arrives at the agency reception wearing a dazzling golden dress from a photoshoot next door. "
    "Gabriel admires her glamorous outfit and informs her that Camille is currently in a meeting. "
    "Let's listen to their exchange in French first."
)

OPENER = "Let's examine the conversation line by line and explore the French expressions."
TRANSITION = "Now let's listen to the complete discussion once more to reinforce the vocabulary."

STORY = [
    ("lea", "Bonjour Gabriel, regarde ma nouvelle robe!",
     "Hello Gabriel, look at my new dress!",
     [(876, "Dior")], "Sofia shows off her golden gown"),
    ("gabriel", "Wow, Charlize Theron est de retour!",
     "Wow, Charlize Theron is back!",
     [(877, "Charlize Theron est de retour")], "Gabriel compares her to Charlize Theron"),
    ("lea", "Merci! C'est une robe magnifique.",
     "Thank you! It is a gorgeous dress.",
     [(878, "Je sais")], "Sofia admires the dress"),
    ("gabriel", "C'est quoi cette belle tenue?",
     "What is this beautiful outfit?",
     [(879, "C'est quoi cette tenue")], "Gabriel asks about the outfit"),
    ("lea", "J'ai une séance photo à côté.",
     "I have a photo session next door.",
     [(880, "shooting photo à côté")], "Sofia explains the nearby shoot"),
    ("lea", "Je voulais juste dire bonjour.",
     "I just wanted to say hello.",
     [(880, "Je voulais juste dire bonjour")], "Sofia explains her brief visit"),
    ("gabriel", "C'est très gentil de ta part.",
     "That is very kind of you.",
     [(878, "Carrément")], "Gabriel appreciates the gesture"),
    ("lea", "Camille est dans son bureau?",
     "Is Camille in her office?",
     [(881, "Camille est là")], "Sofia asks for her agent"),
    ("gabriel", "Non, elle est sortie maintenant.",
     "No, she went out now.",
     [(882, "elle est sortie")], "Gabriel says Camille stepped out"),
    ("gabriel", "Elle a une réunion importante.",
     "She has an important meeting.",
     [(882, "pour une réunion")], "Gabriel explains she is in a meeting"),
    ("lea", "Il faut que je rentre vite.",
     "I must go back quickly.",
     [(881, "Il faut que je rentre")], "Sofia notes she must return soon"),
    ("gabriel", "Tu peux l'attendre dans son bureau.",
     "You can wait for her in her office.",
     [(882, "l'attendre dans son bureau")], "Gabriel suggests waiting in Camille's office"),
    ("lea", "D'accord, je vais l'attendre un peu.",
     "All right, I am going to wait for her a bit.",
     [(883, "OK")], "Sofia agrees to wait"),
    ("gabriel", "À tout à l'heure, grande star!",
     "See you later, big star!",
     [(884, "Mme Theron")], "Gabriel playfully bids her farewell"),
]

WALK = [
    (0, None,
     "'Hello Gabriel, look at my new dress!' Sofia makes a grand entrance in her shimmering gown. "
     "The imperative 'regarde' invites someone to look closely."),
    (1, None,
     "'Wow, Charlize Theron is back!' Gabriel jokes about the iconic perfume commercial featuring a golden dress. "
     "The idiom 'etre de retour' means to be back."),
    (2, None,
     "'Thank you! It is a gorgeous dress.' Sofia beams with pride in her high-fashion attire. "
     "The adjective 'magnifique' means magnificent or gorgeous."),
    (3, None,
     "'What is this beautiful outfit?' Gabriel wonders why she is dressed so formally in the middle of the day. "
     "The feminine noun 'tenue' designates an outfit or attire."),
    (4, None,
     "'I have a photo session next door.' Sofia explains that her studio is right down the street. "
     "The locative phrase 'a cote' means next door or nearby."),
    (5, None,
     "'I just wanted to say hello.' Sofia stepped out during a break to greet her agency friends. "
     "The imperfect 'voulais' softens a polite intention."),
    (6, None,
     "'That is very kind of you.' Gabriel appreciates her friendly visit to the office. "
     "The expression 'de ta part' means on your part or of you."),
    (7, None,
     "'Is Camille in her office?' Sofia hopes to catch up with her agent before returning to set. "
     "The possessive 'son' is used before masculine singular nouns like 'bureau'."),
    (8, None,
     "'No, she went out now.' Gabriel informs her that Camille is temporarily away from her desk. "
     "The past participle 'sortie' takes an extra 'e' to agree with a female subject."),
    (9, None,
     "'She has an important meeting.' Gabriel explains why Camille had to step out. "
     "The feminine noun 'reunion' refers to a business meeting."),
    (10, None,
     "'I must go back quickly.' Sofia remembers that the photographer is waiting for her next door. "
     "The impersonal structure 'il faut que' expresses necessity."),
    (11, None,
     "'You can wait for her in her office.' Gabriel suggests she relax in Camille's room for a few minutes. "
     "The direct object pronoun 'la' contracts to 'l' before a vowel."),
    (12, None,
     "'All right, I am going to wait for her a bit.' Sofia decides to stay briefly until Camille returns. "
     "The quantifier 'un peu' means a little bit."),
    (13, None,
     "'See you later, big star!' Gabriel waves goodbye with a playful tease. "
     "The farewell 'a tout a l'heure' is used when you will see someone again the same day."),
]

OUTRO = (
    "Sofia heads down the corridor toward Camille's office in her sparkling golden gown. "
    "She settles in to wait for her agent before returning to her photoshoot. "
    "Now let's listen to the scene one last time."
)

CLOSING = ("lea", "Oui, s'il te plaît, merci!")
