# Authoring module for dix-pour-cent s03e03 scene 11 (cues 433-478).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s03e03/authoring/scene-11.py --out overhear-content/out/dix-pour-cent/s03e03/scene-11.json

ID = "dix-pour-cent-s03e03-scene-11"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 3
SCENE = 11
TITLE = "Le nouveau talent brut  (The Raw New Talent)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "directeur": "marcel"}
LABELS = {"lea": "Camille", "directeur": "Directeur"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E03"
SOURCE_FILE = "sources/dix-pour-cent/s03/e03.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 433-478. In the casting studio, the director is blown away by the unexpected energy of newcomer Samy, "
    "and junior agent Camille Valentini steps forward to proudly introduce herself as his agent."
)

INTRO = (
    "At the audition studio, the casting director is astonished by the raw power of young actor Samy. "
    "Junior agent Camille Valentini steps forward to claim credit, proudly declaring that she represents this sensational new talent. "
    "Listen to the scene in French first."
)

STORY = [
    ("directeur", "Mais c'est qui ce phénomène?",
     "Who is this character, anyway?",
     [(433, "ce phénomène")], ""),
    ("lea", "Justement, je viens vous expliquer!",
     "That is exactly what I came to explain!",
     [(434, "je vous explique")], ""),
    ("directeur", "Il est absolument génial!",
     "He is absolutely brilliant!",
     [(435, "Il est génial")], ""),
    ("directeur", "Génial, c'est-à-dire très surprenant.",
     "Brilliant, meaning very surprising.",
     [(436, "Génial")], ""),
    ("directeur", "Ce n'est pas du tout le personnage prévu.",
     "He is not at all the intended character.",
     [(437, "pas du tout le personnage")], ""),
    ("directeur", "Mais après, j'ai tout de suite compris.",
     "But afterwards, I understood right away.",
     [(440, "j'ai compris")], ""),
    ("directeur", "J'ai vu exactement ce que vous avez vu.",
     "I saw exactly what you saw.",
     [(441, "ce que vous avez vu")], ""),
    ("directeur", "C'est un véritable talent brut!",
     "He is a genuine raw talent!",
     [(443, "Un talent brut")], ""),
    ("directeur", "Il a une grande force explosive.",
     "He has great explosive strength.",
     [(444, "force explosive")], ""),
    ("directeur", "Et il a aussi beaucoup de sensibilité.",
     "And he also has a lot of sensitivity.",
     [(444, "sensibilité")], ""),
    ("directeur", "C'est vraiment hyper intéressant pour le film.",
     "It is genuinely fascinating for the film.",
     [(445, "hyper intéressant")], ""),
    ("directeur", "Et qui est son agent artistique?",
     "And who is his talent agent?",
     [(447, "qui, son agent")], ""),
    ("lea", "C'est moi son agent!",
     "I am his agent!",
     [(448, "Moi")], ""),
    ("lea", "Camille Valentini, de l'agence ASK.",
     "Camille Valentini, from the ASK agency.",
     [(449, "Camille Valentini")], ""),
    ("directeur", "Enchanté, Camille, bravo pour cette découverte!",
     "Delighted, Camille, congratulations on this discovery!",
     [(450, "Enchantée"), (452, "Camille, ça va")], "")
]

OPENER = "Let's walk through the conversation step by step."

WALK = [
    (0, None,
     "'Who is this character, anyway?' The casting director asks about the magnetic actor. "
     "The informal demonstrative noun highlights his unique persona."),
    (1, None,
     "'That is exactly what I came to explain!' Camille eagerly steps forward to offer context. "
     "The present motion verb introduces her explanation."),
    (2, None,
     "'He is absolutely brilliant!' The director shares his enthusiastic impression. "
     "The predicate adjective conveys great admiration."),
    (3, None,
     "'Brilliant, meaning very surprising.' He clarifies the unusual nature of the performance. "
     "The compound adverbial link explains his specific nuance."),
    (4, None,
     "'He is not at all the intended character.' He acknowledges the departure from the script. "
     "The emphatic negative phrase notes the creative contrast."),
    (5, None,
     "'But afterwards, I understood right away.' The director describes having an artistic revelation. "
     "The past tense verb indicates sudden appreciation."),
    (6, None,
     "'I saw exactly what you saw.' He validates the agent's artistic eye. "
     "The relative clause emphasizes shared artistic perception."),
    (7, None,
     "'He is a genuine raw talent!' The director identifies rare natural ability. "
     "The descriptive adjective pair praises unpolished instinct."),
    (8, None,
     "'He has great explosive strength.' He praises the physical intensity on camera. "
     "The noun phrase describes powerful screen presence."),
    (9, None,
     "'And he also has a lot of sensitivity.' He notes the emotional depth balancing the aggression. "
     "The abstract noun complements the actor's profile."),
    (10, None,
     "'It is genuinely fascinating for the film.' He envisions the character on screen. "
     "The modern intensifier stresses compelling potential."),
    (11, None,
     "'And who is his talent agent?' The director seeks the professional representative. "
     "The interrogative sentence opens business representation."),
    (12, None,
     "'I am his agent!' Camille seizes her opportunity with confidence. "
     "The emphatic pronoun phrase claims exclusive management."),
    (13, None,
     "'Camille Valentini, from the ASK agency.' She introduces herself formally. "
     "The proper noun phrase asserts agency affiliation."),
    (14, None,
     "'Delighted, Camille, congratulations on this discovery!' The director welcomes the young agent warmly. "
     "The complimentary greeting celebrates the successful audition.")
]

TRANSITION = "Now listen to the whole scene again at normal speed, and see how much more you catch."

OUTRO = (
    "Stepping boldly into the spotlight, Camille Valentini signs an explosive young talent and establishes herself as a force at the agency. "
    "Listen to the conversation once more in French."
)

CLOSING = ("lea", "C'est un début très prometteur.")
