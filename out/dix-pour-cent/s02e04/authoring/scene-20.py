# Authoring module for dix-pour-cent s02e04 scene 20 (cues 561-581).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e04/authoring/scene-20.py --out out/dix-pour-cent/s02e04/scene-20.json

ID = "dix-pour-cent-s02e04-scene-20"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 4
SCENE = 20
TITLE = "Séduction au bureau  (Hicham Flirts)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "hicham": "theo"}
LABELS = {"lea": "Andréa", "hicham": "Hicham"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E04"
SOURCE_FILE = "sources/dix-pour-cent/s02/e04.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 561-581. Hicham visits Andréa in her office before an interview. When he attempts to flirt with her, "
    "Andréa firmly and unmistakably clarifies her boundaries, tells him to leave, and forbids him from calling her Marteau."
)

INTRO = (
    "In her office at ASK, Andréa is visited by new boss Hicham Janowski. When Hicham tries to charm her, "
    "Andréa makes her personal boundaries crystal clear and orders him out of her office. "
    "Listen to the scene in French first."
)

STORY = [
    ("hicham", "Bonjour Andréa, c'est l'heure de notre réunion.",
     "Hello Andréa, it is time for our meeting.",
     [(561, "C'est l'heure de l'interview.")], ""),
    ("lea", "Non, vous êtes en avance. Revenez plus tard.",
     "No, you are early. Come back later.",
     [(562, "Non, vous êtes en avance. Revenez plus tard, je travaille.")], ""),
    ("hicham", "J'adore votre bureau et votre style.",
     "I love your office and your style.",
     [(563, "J'adore votre bureau."), (564, "Nous partageons tous les deux un goût pour les belles choses.")], ""),
    ("lea", "Arrêtez de me regarder avec insistance.",
     "Stop looking at me insistently.",
     [(565, "Arrêtez de me regarder comme ça.")], ""),
    ("hicham", "Vous êtes trop méfiante avec moi.",
     "You are too suspicious with me.",
     [(566, "T'es trop parano ! Je déteste les conflits au boulot.")], ""),
    ("lea", "Écoutez, Hicham, soyons très clairs.",
     "Listen, Hicham, let us be very clear.",
     [(568, "Écoute, Janowski.")], ""),
    ("lea", "Je préfère les femmes, uniquement les femmes.",
     "I prefer women, only women.",
     [(569, "J'aime les femmes, uniquement les femmes.")], ""),
    ("hicham", "Je comprends tout à fait votre point de vue.",
     "I completely understand your point of view.",
     [(572, "Je suis d'accord.")], ""),
    ("lea", "Non, je pense que vous ne comprenez pas.",
     "No, I think that you do not understand.",
     [(573, "Non, putain, tu comprends pas !")], ""),
    ("lea", "Pour moi, ma vie personnelle est définitive.",
     "For me, my personal life is definitive.",
     [(577, "Non, je ne peux pas revenir en arrière.")], ""),
    ("lea", "Vous ne changerez jamais ma décision.",
     "You will never change my decision.",
     [(578, "Et tu ne m'en donneras pas envie.")], ""),
    ("hicham", "Je voulais seulement discuter amicalement.",
     "I only wanted to chat in a friendly way.",
     [(576, "Bon, laisse tomber les explications, je vois ce que je vois.")], ""),
    ("lea", "Maintenant, sortez de mon bureau, s'il vous plaît.",
     "Now, leave my office, please.",
     [(579, "Maintenant, pars.")], ""),
    ("hicham", "Très bien, Marteau, je vous laisse travailler.",
     "Very well, Marteau, I leave you to work.",
     [(580, "Très bien, Marteau.")], ""),
    ("lea", "Et arrêtez de m'appeler Marteau!",
     "And stop calling me Marteau!",
     [(581, "Et arrête de m'appeler Marteau, putain !")], ""),
    ("hicham", "C'est promis, je respecte votre espace.",
     "It is promised, I respect your space.",
     [(580, "Très bien, Marteau.")], "")
]

OPENER = "Let's examine how Andréa firmly rejects the flirtatious advances of Hicham."

WALK = [
    (0, None,
     "'Hello Andréa, it is time for our meeting.' Hicham enters Andréa's office unannounced. "
     "The noun phrase l'heure de indicates a scheduled appointment time."),
    (1, None,
     "'No, you are early. Come back later.' Andréa sets immediate boundaries. "
     "The idiom en avance means ahead of schedule."),
    (2, None,
     "'I love your office and your style.' Hicham attempts flattery. "
     "The verb adorer expresses high appreciation."),
    (3, None,
     "'Stop looking at me insistently.' Andréa calls out his inappropriate gaze directly. "
     "The imperative phrase arrêtez de means stop doing something."),
    (4, None,
     "'You are too suspicious with me.' Hicham brushes off her complaint. "
     "The adjective méfiante means wary or mistrustful."),
    (5, None,
     "'Listen, Hicham, let us be very clear.' Andréa initiates a serious clarification. "
     "The imperative soyons comes from the verb être."),
    (6, None,
     "'I prefer women, only women.' Andréa states her sexual orientation unambiguously. "
     "The adverb uniquement means exclusively or solely."),
    (7, None,
     "'I completely understand your point of view.' Hicham tries to sound understanding. "
     "The locution tout à fait means entirely or completely."),
    (8, None,
     "'No, I think that you do not understand.' Andréa cuts through his superficial agreement. "
     "The negation ne... pas surrounds the verb comprenez."),
    (9, None,
     "'For me, my personal life is definitive.' Andréa reaffirms her identity with conviction. "
     "The adjective définitive means final or settled."),
    (10, None,
     "'You will never change my decision.' Andréa leaves no room for doubt. "
     "The future tense changerez expresses certainty about the future."),
    (11, None,
     "'I only wanted to chat in a friendly way.' Hicham retreats to a polite pretext. "
     "The adverb amicalement means warmly or friendly."),
    (12, None,
     "'Now, leave my office, please.' Andréa orders him to leave firmly. "
     "The imperative sortez commands departure."),
    (13, None,
     "'Very well, Marteau, I leave you to work.' Hicham yields while using her annoying nickname. "
     "The phrase vous laisse means leave you."),
    (14, None,
     "'And stop calling me Marteau!' Andréa refuses the patronizing nickname. "
     "The infinitive appeler follows the preposition de."),
    (15, None,
     "'It is promised, I respect your space.' Hicham finally accepts the boundary and departs. "
     "The phrase c'est promis means that is a promise.")
]

TRANSITION = "Now let's listen to the sharp confrontation once more at natural pace."

OUTRO = (
    "Andréa sets crystal-clear personal and professional boundaries with Hicham in her office. "
    "Listen to the tense dialogue once more in French."
)

CLOSING = ("hicham", "C'est promis, je respecte votre espace.")
