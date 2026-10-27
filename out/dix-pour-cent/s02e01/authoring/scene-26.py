# Authoring module for dix-pour-cent s02e01 scene 26 (cues 781-789).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e01/authoring/scene-26.py --out out/dix-pour-cent/s02e01/scene-26.json

ID = "dix-pour-cent-s02e01-scene-26"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 1
SCENE = 26
TITLE = "Ramzy sur le plateau télé  (Ramzy on the TV Set)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "ramzy": "theo", "michel": "marcel"}
LABELS = {"lea": "Virginie", "ramzy": "Ramzy", "michel": "Michel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E01"
SOURCE_FILE = "sources/dix-pour-cent/s02/e01.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 781-789. On the set of Vivement Dimanche, Ramzy jokes on the red sofa with host Michel Drucker "
    "and pet dog Isia. Meanwhile, Michel prepares to bring on an unannounced surprise guest, "
    "while Virginie watches from the wings. Adapted for A1 French."
)

INTRO = (
    "On the television studio set of Vivement Dimanche, Ramzy Bedia is seated on the red sofa. "
    "He chats comfortably with host Michel Drucker while petting the dog, unaware that a major surprise awaits. "
    "Let's listen to the scene in French first."
)

STORY = [
    ("ramzy", "Je crois que ta chienne m'aime bien, Michel!",
     "I think your dog likes me, Michel!",
     [(781, "Je crois que ta chienne m'aime bien, Michel !")], ""),
    ("ramzy", "Elle sait que je suis un homme blessé.",
     "She knows that I am a wounded man.",
     [(782, "Elle sait que je suis un homme blessé")], ""),
    ("ramzy", "J'ai besoin de réconfort aujourd'hui.",
     "I need comforting today.",
     [(782, "qui a besoin de réconfort.")], "Adapted with aujourd'hui"),
    ("ramzy", "J'aurais dû l'épouser!",
     "I should have married her!",
     [(783, "J'aurais dû l'épouser.")], ""),
    ("michel", "Demande-lui!",
     "Ask her!",
     [(784, "Demande !")], "Adapted to Demande-lui"),
    ("ramzy", "Pardon? Oui?",
     "Excuse me? Yes?",
     [(785, "Pardon. Oui ?")], ""),
    ("michel", "Nous avons un invité surprise.",
     "We have a surprise guest.",
     [(787, "Nous avons un invité surprise.")], ""),
    ("ramzy", "Mon professeur de judo quand j'avais dix ans?",
     "My judo teacher from when I was ten?",
     [(788, "Mon professeur de judo quand j'avais 10 ans ?")], "Spelled out number 10"),
    ("michel", "Je ne sais pas, c'est une surprise!",
     "I do not know, it is a surprise!",
     [(789, "Je sais pas, c'est une surprise !")], "Formalized negation with ne"),
    ("lea", "C'est mon tour d'entrer en scène.",
     "It is my turn to go on stage.",
     [], "Virginie waiting in the wings"),
    ("lea", "Ramzy ne sait pas que je suis là.",
     "Ramzy does not know that I am here.",
     [], "Virginie commenting backstage"),
    ("lea", "Nous allons régler nos comptes en direct.",
     "We are going to settle our scores live.",
     [], "Virginie preparing to reveal the secret"),
]

OPENER = "Let's examine how Ramzy jokes with Michel Drucker before the surprise arrival."

WALK = [
    (0, None,
     "'I think your dog likes me, Michel!' The verb croire expressing an impression or belief."),
    (1, None,
     "'She knows that I am a wounded man.' The verb savoir followed by a descriptive past participle."),
    (2, None,
     "'I need comforting today.' The common idiom avoir besoin de followed by a noun."),
    (3, None,
     "'I should have married her!' A past conditional expressing humorous regret."),
    (4, None,
     "'Ask her!' An imperative with the indirect object pronoun lui."),
    (5, None,
     "'Excuse me? Yes?' Familiar words used to show polite confusion."),
    (6, None,
     "'We have a surprise guest.' The noun invite used with the modifier surprise."),
    (7, None,
     "'My judo teacher from when I was ten?' The imperfect tense of avoir used for age."),
    (8, None,
     "'I do not know, it is a surprise!' Standard negation with savoir followed by a presentative clause."),
    (9, None,
     "'It is my turn to go on stage.' The phrase c'est mon tour followed by de and an infinitive."),
    (10, None,
     "'Ramzy does not know that I am here.' A negative clause followed by the adverb la."),
    (11, None,
     "'We are going to settle our scores live.' The idiom regler nos comptes meaning to settle scores."),
]

TRANSITION = "Now let's listen to the whole discussion again without stopping."

OUTRO = (
    "Ramzy is relaxed and making jokes on the sofa, completely unaware of what is coming. "
    "Virginie is about to step onto the television set for a dramatic confrontation."
)

CLOSING = ("lea", "Me voilà, Michel!")
