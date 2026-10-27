# Authoring module for dix-pour-cent s03e01 scene 15 (cues 442-503).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s03e01/authoring/scene-15.py --out overhear-content/out/dix-pour-cent/s03e01/scene-15.json

ID = "dix-pour-cent-s03e01-scene-15"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 1
SCENE = 15
TITLE = "La réunion d'agence  (The Agency Meeting)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "mathias": "theo", "hicham": "marcel"}
LABELS = {"lea": "Andréa", "mathias": "Mathias", "hicham": "Hicham"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E01"
SOURCE_FILE = "sources/dix-pour-cent/s03/e01.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 442-503. Around the ASK conference table, Andréa and the agents discuss Jean Dujardin's "
    "refusal to abandon his 1870 deserter persona, comparing his method acting to Daniel Day-Lewis."
)

INTRO = (
    "Gathered in the agency conference room, Andrea and the agents hold an urgent meeting about star client Jean Dujardin's method acting crisis. "
    "As Hicham demands to know whether Jean signed his new film contract, Mathias lectures the room on how famous actors struggle to shed intense roles. "
    "Listen to the scene in French first."
)

STORY = [
    ("lea", "Le tournage est fini depuis deux semaines.",
     "Filming wrapped two weeks ago.",
     [(442, "Le tournage est fini depuis deux semaines")], ""),
    ("lea", "Et il doit enchaîner avec l'autre film!",
     "And he has to jump straight into the next film!",
     [(443, "il doit enchaîner avec l'autre film")], ""),
    ("lea", "C'est un cauchemar, les gars.",
     "It is a nightmare, guys.",
     [(444, "C'est un cauchemar, les gars")], ""),
    ("hicham", "Il ne veut pas se laver?",
     "He does not want to wash?",
     [(445, "veut pas se laver ou se raser")], ""),
    ("lea", "Non, il ne veut rien faire!",
     "No, he does not want to do anything!",
     [(447, "Non, rien. Rien")], ""),
    ("lea", "J'ai un acteur en pleine Delewis!",
     "I have an actor in full Day-Lewis mode!",
     [(458, "un acteur en pleine Delewis")], ""),
    ("hicham", "Daniel Delewis, l'acteur anglais?",
     "Daniel Day-Lewis, the English actor?",
     [(460, "Daniel Delewis")], ""),
    ("mathias", "Il ne peut plus en sortir.",
     "He can no longer come out of it.",
     [(462, "il peut plus en sortir")], ""),
    ("mathias", "C'est utile pour diriger une agence!",
     "It is useful for running an agency!",
     [(464, "quand on dirige une agence artistique")], ""),
    ("mathias", "Day-Lewis a vécu six mois en forêt.",
     "Day-Lewis lived six months in the forest.",
     [(466, "vécu comme un Indien pendant six mois")], ""),
    ("mathias", "C'est la méthode de l'Actor Studio.",
     "It is the Actor Studio method.",
     [(471, "Méthode acteur studio")], ""),
    ("hicham", "Finalement, il a signé son contrat?",
     "Finally, did he sign his contract?",
     [(479, "il a signé son contrat")], ""),
    ("lea", "Non, mais c'est en cours.",
     "No, but it is in progress.",
     [(481, "c'est en cours")], ""),
    ("mathias", "Fabriquer des chaussures aide beaucoup l'acteur.",
     "Making shoes helps the actor a lot.",
     [(498, "Ça l'aide à se retrouver lui-même")], ""),
    ("mathias", "Depardieu buvait pour quitter Rodin!",
     "Depardieu drank heavily to leave Rodin!",
     [(501, "sortir du personnage de Rodin")], "")
]

OPENER = "Let's walk through the conversation step by step."

WALK = [
    (0, None,
     "'Filming wrapped two weeks ago.' Andrea outlines the urgent timing problem to the team. "
     "The temporal prepositional phrase indicates elapsed time."),
    (1, None,
     "'And he has to jump straight into the next film!' Andrea highlights the tight schedule for the upcoming shoot. "
     "The modal verb denotes pressing obligation."),
    (2, None,
     "'It is a nightmare, guys.' She describes the escalating crisis with her star client. "
     "The predicate noun captures professional dread."),
    (3, None,
     "'He does not want to wash?' Hicham asks in disbelief about Jean's hygiene. "
     "The negative modal verb construction expresses refusal."),
    (4, None,
     "'No, he does not want to do anything!' Andrea confirms his total immersion in wild living. "
     "The negative indefinite pronoun emphasizes absolute refusal."),
    (5, None,
     "'I have an actor in full Day-Lewis mode!' She coins a phrase comparing him to the famously intense British method actor. "
     "The idiomatic noun phrase characterizes total immersion."),
    (6, None,
     "'Daniel Day-Lewis, the English actor?' Hicham clarifies the celebrity reference. "
     "The appositive noun phrase identifies the foreign star."),
    (7, None,
     "'He can no longer come out of it.' Mathias explains how immersive acting traps performers. "
     "The negative adverbial pronoun construction indicates emotional entrapment."),
    (8, None,
     "'It is useful for running an agency!' Mathias lectures Hicham on the value of film culture. "
     "The purposive prepositional phrase highlights industry knowledge."),
    (9, None,
     "'Day-Lewis lived six months in the forest.' Mathias cites historical method acting lore. "
     "The past active verb describes extreme preparation."),
    (10, None,
     "'It is the Actor Studio method.' He references the famous dramatic training technique. "
     "The proper noun phrase labels the American acting tradition."),
    (11, None,
     "'Finally, did he sign his contract?' Hicham cuts through film history to check business reality. "
     "The temporal adverb demands a bottom-line answer."),
    (12, None,
     "'No, but it is in progress.' Andrea evasively downplays the unsigned contract. "
     "The prepositional phrase buys time for negotiations."),
    (13, None,
     "'Making shoes helps the actor a lot.' Mathias notes how physical craft grounds disoriented actors. "
     "The transitive verb describes therapeutic manual work."),
    (14, None,
     "'Depardieu drank heavily to leave Rodin!' Mathias recalls French cinema lore about shaking off roles. "
     "The imperfect verb recalls coping through excess.")
]

TRANSITION = "Now listen to the whole scene again at normal speed, and see how much more you catch."

OUTRO = (
    "Comparing Jean Dujardin's crisis to Daniel Day-Lewis, the agency team debates how to coax their wild actor back into civilized society. "
    "Listen to the conversation once more in French."
)

CLOSING = ("lea", "Trouvons une solution avant demain matin.")
