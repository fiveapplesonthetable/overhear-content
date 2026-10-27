# Authoring module for dix-pour-cent s03e06 scene 23 (cues 1219-1221).
# Build: python3 tools/compose.py out/dix-pour-cent/s03e06/authoring/scene-23.py --out out/dix-pour-cent/s03e06/scene-23.json

ID = "dix-pour-cent-s03e06-scene-23"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 6
SCENE = 23
TITLE = "Avant le discours  (Before the Speech)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "hicham": "marcel"}
LABELS = {"lea": "Camille", "hicham": "Hicham"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E06"
SOURCE_FILE = "sources/dix-pour-cent/s03/e06.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 1219-1221. Backstage at the ASK thirtieth anniversary gala, Camille alerts Hicham that the packed room is waiting for him. "
    "Noticing his nervous tension, she brings him a glass of water before he steps up to the microphone."
)

INTRO = (
    "Backstage at the ASK thirtieth anniversary gala, Camille alerts Hicham that the packed room is waiting for him. "
    "Noticing his nervous tension, she brings him a glass of water before he steps up to the microphone. "
    "Let's listen to the scene in French first."
)

STORY = [
    ("lea", "Hicham, tout le monde vous attend là-bas.",
     "Hicham, everyone is waiting for you over there.",
     [(1219, "Il est tout là-bas")], "Warned him that the guests are gathered"),
    ("hicham", "La salle entière est déjà bien remplie?",
     "Is the entire hall already well filled?",
     [(1219, "là-bas")], "Asked about the size of the crowd"),
    ("lea", "Oui, tous les artistes célèbres sont arrivés.",
     "Yes, all the famous artists have arrived.",
     [(1219, "là-bas")], "Confirmed that star clients have arrived"),
    ("hicham", "J'avoue que j'ai un trac terrible.",
     "I confess that I have terrible stage fright.",
     [(1220, "Ça va être à vous")], "Admitted his severe public speaking nerves"),
    ("lea", "Ça va être à vous de monter.",
     "It is going to be your turn to go up.",
     [(1220, "Ça va être à vous")], "Signaled the imminent stage cue"),
    ("hicham", "J'ai préparé quelques mots très simples.",
     "I prepared a few very simple words.",
     [(1220, "Ça va être à vous")], "Reviewed his short speech notes"),
    ("lea", "Je vais vous chercher un verre d'eau.",
     "I will get you a glass of water.",
     [(1220, "Je vais vous chercher un petit verre d'eau")], "Offered refreshing water to calm him"),
    ("hicham", "Merci Camille, vous êtes toujours très prévenante.",
     "Thank you Camille, you are always very thoughtful.",
     [(1220, "verre d'eau")], "Thanked her for her thoughtful care"),
    ("lea", "Pardonnez-moi, je me faufile rapidement.",
     "Pardon me, I am slipping through quickly.",
     [(1221, "Pardon")], "Apologized as she moved through the crowd"),
    ("hicham", "Cette trentième fête d'anniversaire est grandiose.",
     "This thirtieth anniversary party is grandiose.",
     [(1220, "Ça va être à vous")], "Marvelled at the milestone celebration"),
    ("lea", "Votre discours va énormément toucher l'assemblée.",
     "Your speech will touch the audience enormously.",
     [(1220, "Ça va être à vous")], "Reassured him of a warm reception"),
    ("hicham", "Je veux surtout rendre hommage aux agents.",
     "I especially want to pay tribute to agents.",
     [(1220, "Ça va être à vous")], "Clarified his central message of gratitude"),
    ("lea", "Buvez cette eau fraîche avant de commencer.",
     "Drink this fresh water before starting.",
     [(1220, "verre d'eau")], "Handed him the soothing drink"),
    ("hicham", "Je suis maintenant prêt pour la scène.",
     "I am now ready for the stage.",
     [(1220, "Ça va être à vous")], "Stepped forward toward the spotlight")
]

OPENER = "Let's break down the dialogue line by line."

WALK = [
    (0, None,
     "'Hicham, everyone is waiting for you over there.' Camille points across the crowded room. "
     "The present tense verb indicates the expectant crowd."),
    (1, None,
     "'Is the entire hall already well filled?' Hicham asks about the audience. "
     "The descriptive adjective phrase gauges the pressure on stage."),
    (2, None,
     "'Yes, all the famous artists have arrived.' Camille confirms the glamorous turnout. "
     "The compound past verb highlights the distinguished guests."),
    (3, None,
     "'I confess that I have terrible stage fright.' Hicham reveals his underlying anxiety. "
     "The noun phrase vividly describes public speaking jitters."),
    (4, None,
     "'It is going to be your turn to go up.' Camille gives the official countdown. "
     "The near-future verbal idiom signals his upcoming turn at the microphone."),
    (5, None,
     "'I prepared a few very simple words.' Hicham clutches his prompt cards. "
     "The compound past verb stresses his desire for heartfelt brevity."),
    (6, None,
     "'I will get you a glass of water.' Camille steps away to fetch a drink. "
     "The near-future construction promises immediate assistance."),
    (7, None,
     "'Thank you Camille, you are always very thoughtful.' Hicham expresses sincere gratitude. "
     "The complimentary adjective praises her professional attentiveness."),
    (8, None,
     "'Pardon me, I am slipping through quickly.' Camille squeezes past the VIPs. "
     "The polite imperative verb excuses her brisk movement in the crowd."),
    (9, None,
     "'This thirtieth anniversary party is grandiose.' Hicham takes in the lavish hall. "
     "The ordinal numeral celebrates thirty years of cinematic history."),
    (10, None,
     "'Your speech will touch the audience enormously.' Camille offers encouraging support. "
     "The near-future verb with an adverb boosts his confidence."),
    (11, None,
     "'I especially want to pay tribute to agents.' Hicham defines his noble purpose. "
     "The idiomatic verbal phrase underscores collective corporate honor."),
    (12, None,
     "'Drink this fresh water before starting.' Camille delivers the soothing glass. "
     "The imperative verb urges him to clear his throat."),
    (13, None,
     "'I am now ready for the stage.' Hicham takes a deep breath and steps forward. "
     "The predicate adjective announces his complete readiness.")
]

TRANSITION = "Now listen to the scene again at normal speed and see how much you understand."

OUTRO = (
    "In the wings of the grand anniversary hall, Camille steadies Hicham before he steps into the spotlight. "
    "Listen to the conversation one last time in French."
)

CLOSING = ("hicham", "Je suis maintenant prêt pour la scène.")
