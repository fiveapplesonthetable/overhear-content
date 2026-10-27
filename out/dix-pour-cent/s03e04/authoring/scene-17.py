# Authoring module for dix-pour-cent s03e04 scene 17 (cues 904-930).
# Build: python3 tools/compose.py out/dix-pour-cent/s03e04/authoring/scene-17.py --out out/dix-pour-cent/s03e04/scene-17.json

ID = "dix-pour-cent-s03e04-scene-17"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 4
SCENE = 17
TITLE = "Des croissants chauds  (Warm Croissants)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "mathias": "theo"}
LABELS = {"lea": "Noémie", "mathias": "Mathias"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E04"
SOURCE_FILE = "sources/dix-pour-cent/s03/e04.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 904-930. Mathias calls Noémie from outside her building after the shoot with Isabelle Huppert. "
    "He credits her assistance with saving the day, confirms she is alone, and brings warm croissants upstairs."
)

INTRO = (
    "Mathias calls Noémie from outside her apartment building after the successful shoot. "
    "He thanks her warmly for saving the day, confirms she is alone, and brings warm croissants up to her flat. "
    "Let's listen to the scene in French first."
)

STORY = [
    ("mathias", "Allô Noémie, je ne vous dérange pas?",
     "Hello Noémie, am I not disturbing you?",
     [(913, "Eh, Mathias"), (914, "Je vous dérange pas")], "Mathias begins the morning phone call"),
    ("lea", "Non Mathias, tout va très bien.",
     "No Mathias, everything is going very well.",
     [(915, "Non, non, ça va")], "Noémie responds with pleasant calm"),
    ("mathias", "Le tournage d'Isabelle est terminé.",
     "Isabelle's shoot is finished.",
     [(916, "nuit d'Isabelle Huppert")], "Mathias shares the filming completion"),
    ("mathias", "Nous avons réussi cette folle nuit!",
     "We made it through this crazy night!",
     [(916, "cette folle nuit")], "Mathias celebrates the agency victory"),
    ("lea", "C'est une merveilleuse nouvelle pour vous!",
     "That is wonderful news for you!",
     [(918, "c'est super")], "Noémie shares his delight"),
    ("mathias", "C'est largement grâce à votre aide.",
     "It is largely thanks to your help.",
     [(917, "grâce à vous")], "Mathias gives her all the credit"),
    ("mathias", "Vous avez été tout simplement formidable.",
     "You were quite simply wonderful.",
     [(917, "grâce à vous")], "Mathias showers her with compliments"),
    ("lea", "Je suis très heureuse pour vous.",
     "I am very happy for you.",
     [(919, "Je suis contente pour vous")], "Noémie expresses sincere happiness"),
    ("mathias", "Vous n'êtes pas avec Alexandre?",
     "Are you not with Alexandre?",
     [(922, "Vous êtes pas avec Alexandre")], "Mathias tentatively probes her relationship"),
    ("lea", "Non, je suis toute seule.",
     "No, I am all alone.",
     [(923, "pas du tout")], "Noémie confirms she is by herself"),
    ("lea", "Et vous, avec votre femme?",
     "And you, with your wife?",
     [(924, "pas avec votre femme")], "Noémie asks about his situation in return"),
    ("mathias", "Non, je suis en bas.",
     "No, I am downstairs.",
     [(925, "Non"), (926, "en bas de chez vous")], "Mathias reveals his close location"),
    ("mathias", "J'apporte des croissants bien chauds!",
     "I am bringing warm croissants!",
     [(926, "croissants chauds")], "Mathias offers a breakfast treat"),
    ("lea", "Sonnez vite, je vous ouvre!",
     "Ring quickly, I am buzzing you in!",
     [(929, "sonnez, je vous ouvre")], "Noémie warmly welcomes him upstairs")
]

OPENER = "Let's break down the dialogue line by line."

WALK = [
    (0, None,
     "'Hello Noémie, am I not disturbing you?' Mathias checks politely if she is free to speak. "
     "The negative question politely inquires about her availability."),
    (1, None,
     "'No Mathias, everything is going very well.' Noémie answers with warm reassurance. "
     "The present linking verb confirms that she is awake and pleased."),
    (2, None,
     "'Isabelle's shoot is finished.' Mathias reports the end of the marathon filming. "
     "The passive state participle confirms the successful conclusion."),
    (3, None,
     "'We made it through this crazy night!' Mathias expresses relief after the crisis. "
     "The compound past verb celebrates overcoming stressful obstacles."),
    (4, None,
     "'That is wonderful news for you!' Noémie rejoices at their collective relief. "
     "The descriptive adjective praises the happy outcome."),
    (5, None,
     "'It is largely thanks to your help.' Mathias attributes their triumph to her logistics. "
     "The causal prepositional phrase credits her indispensable support."),
    (6, None,
     "'You were quite simply wonderful.' Mathias compliments her exceptional dedication. "
     "The compound past verb with an adverbial phrase expresses heartfelt praise."),
    (7, None,
     "'I am very happy for you.' Noémie responds with modest professional warmth. "
     "The predicate adjective expresses genuine personal joy."),
    (8, None,
     "'Are you not with Alexandre?' Mathias discreetly inquires about her romantic status. "
     "The negative question checks whether she has company."),
    (9, None,
     "'No, I am all alone.' Noémie assures him of her solitary morning. "
     "The predicate adjective confirms that she is unaccompanied."),
    (10, None,
     "'And you, with your wife?' Noémie gently questions his domestic situation. "
     "The elliptical question asks whether he returned home to Catherine."),
    (11, None,
     "'No, I am downstairs.' Mathias reveals his unexpected presence outside her flat. "
     "The spatial prepositional phrase discloses his doorstep surprise."),
    (12, None,
     "'I am bringing warm croissants!' Mathias tempts her with fresh French pastries. "
     "The present motion verb announces his breakfast offering."),
    (13, None,
     "'Ring quickly, I am buzzing you in!' Noémie invites him up without hesitation. "
     "The urgent imperative welcomes him inside her building.")
]

TRANSITION = "Now listen to the scene again at normal speed and see how much you understand."

OUTRO = (
    "With a bag of warm croissants and genuine gratitude, Mathias reconnects with Noémie after a stressful night. "
    "Listen to the conversation one last time in French."
)

CLOSING = ("lea", "Sonnez vite, je vous ouvre!")
