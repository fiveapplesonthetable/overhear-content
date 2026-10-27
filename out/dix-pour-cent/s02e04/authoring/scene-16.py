# Authoring module for dix-pour-cent s02e04 scene 16 (cues 426-447).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s02e04/authoring/scene-16.py --out overhear-content/out/dix-pour-cent/s02e04/scene-16.json

ID = "dix-pour-cent-s02e04-scene-16"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 4
SCENE = 16
TITLE = "L'attente de Julien  (Waiting for Julien)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo"}
LABELS = {"lea": "Sofia", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E04"
SOURCE_FILE = "sources/dix-pour-cent/s02/e04.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 426-447. In Gabriel's office, Gabriel and Sofia wait anxiously for Julien Doré to call back "
    "regarding her audition."
)

INTRO = (
    "Back at the agency, agent Gabriel and actress Sofia wait anxiously beside the phone for singer Julien Dore to call back. "
    "While Gabriel fidgets with impatience, Sofia tries to stay composed and avoid sounding overly eager. "
    "Listen to the scene in French first."
)

STORY = [
    ("gabriel", "C'est bizarre qu'il n'ait pas rappelé.",
     "It is strange that he has not called back.",
     [(426, "C'est bizarre qu'il n'ait pas rappelé")], ""),
    ("lea", "Tu parles de Julien?",
     "Are you talking about Julien?",
     [(427, "Julien")], ""),
    ("gabriel", "Il a dit qu'il rappellerait très vite.",
     "He said he would call back very quickly.",
     [(428, "Il a dit qu'il rappellerait très vite")], ""),
    ("gabriel", "Ça commence à traîner.",
     "Things are starting to drag out.",
     [(429, "Ça commence à traîner")], ""),
    ("lea", "Tu as fait les tests ce matin!",
     "You did the screen tests this morning!",
     [(430, "Tu as fait les tests ce matin")], ""),
    ("gabriel", "Oui, c'est vrai, t'as raison.",
     "Yes, that is true, you are right.",
     [(431, "T'as raison")], ""),
    ("lea", "Et si tu l'appelais directement?",
     "What if you called him directly?",
     [(435, "Et si tu l'appelais")], ""),
    ("lea", "Après tout, tu es son agent.",
     "After all, you are his agent.",
     [(436, "Tu es son agent")], ""),
    ("lea", "Juste pour le sonder un peu.",
     "Just to sound him out a little.",
     [(437, "Juste pour le sonder")], ""),
    ("gabriel", "Il est en train de voir d'autres filles.",
     "He is currently seeing other girls.",
     [(438, "de voir d'autres filles")], ""),
    ("lea", "Vraiment? Il l'a dit?",
     "Really? Did he say that?",
     [(439, "Vraiment"), (440, "Il l'a dit")], ""),
    ("gabriel", "Je sais pas, peut-être bien.",
     "I do not know, quite possibly.",
     [(441, "Je sais pas")], ""),
    ("gabriel", "Il a plein de choses à faire.",
     "He has plenty of things to do.",
     [(442, "plein de choses à faire")], ""),
    ("lea", "Laissons Juju tranquille pour l'instant.",
     "Let us leave Juju alone for now.",
     [(445, "Laissons Juju tranquille")], ""),
    ("gabriel", "Bien sûr. Évidemment.",
     "Of course. Obviously.",
     [(446, "Bien sûr. Évidemment")], "")
]

OPENER = "Let's walk through the conversation step by step."

WALK = [
    (0, None,
     "'It is strange that he has not called back.' Gabriel expresses nervous concern about radio silence. "
     "The impersonal construction takes a subjunctive subordinate clause."),
    (1, None,
     "'Are you talking about Julien?' Sofia clarifies which client is on his mind. "
     "The prepositional verb specifies the topic of inquiry."),
    (2, None,
     "'He said he would call back very quickly.' Gabriel quotes the earlier promise of rapid contact. "
     "The conditional verb expresses future in the past."),
    (3, None,
     "'Things are starting to drag out.' The agent grows visibly impatient with the wait. "
     "The inchoative verb introduces an infinitive of prolongation."),
    (4, None,
     "'You did the screen tests this morning!' Sofia reminds him that barely any time has passed. "
     "The temporal noun phrase points to the current morning."),
    (5, None,
     "'Yes, that is true, you are right.' Gabriel concedes that he might be overreacting. "
     "The colloquial contraction replaces the second-person subject pronoun and verb."),
    (6, None,
     "'What if you called him directly?' Sofia suggests taking initiative with a phone call. "
     "The hypothetical structure introduces an imperfect indicative suggestion."),
    (7, None,
     "'After all, you are his agent.' She points out his professional right to check in. "
     "The fixed transitional idiom emphasizes legitimate standing."),
    (8, None,
     "'Just to sound him out a little.' Sofia wants discreet information without seeming needy. "
     "The adverbial quantifier softens the inquiry intent."),
    (9, None,
     "'He is currently seeing other girls.' Gabriel stokes her insecurity about audition competitors. "
     "The continuous progressive construction emphasizes ongoing action."),
    (10, None,
     "'Really? Did he say that?' Sofia's cool exterior cracks with instant curiosity. "
     "The direct object pronoun stands for the statement made."),
    (11, None,
     "'I do not know, quite possibly.' Gabriel backpedals on his unverified speculation. "
     "The colloquial negation omits the initial particle in rapid speech."),
    (12, None,
     "'He has plenty of things to do.' The agent rationalizes the singer's busy schedule. "
     "The quantifier phrase introduces plural obligations."),
    (13, None,
     "'Let us leave Juju alone for now.' Sofia decides against appearing too eager or demanding. "
     "The first-person plural imperative encourages mutual patience."),
    (14, None,
     "'Of course. Obviously.' Gabriel agrees to respect the artist's personal space. "
     "The pair of affirmative adverbs seals their tactical restraint.")
]

TRANSITION = "Now listen to the whole scene again at normal speed, and see how much more you catch."

OUTRO = (
    "Gabriel and Sofia resolve to stay calm and wait for Julien's decision, though neither can resist watching the silent telephone. "
    "Listen to the French scene once more."
)

CLOSING = ("lea", "Le téléphone va sonner bientôt.")
