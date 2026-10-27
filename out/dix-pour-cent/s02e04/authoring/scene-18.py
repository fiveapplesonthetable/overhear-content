# Authoring module for dix-pour-cent s02e04 scene 18 (cues 481-515).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e04/authoring/scene-18.py --out out/dix-pour-cent/s02e04/scene-18.json

ID = "dix-pour-cent-s02e04-scene-18"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 4
SCENE = 18
TITLE = "Nouveau rendez-vous  (Rescheduling the Meeting)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "sacha": "theo"}
LABELS = {"lea": "Andréa", "sacha": "Sacha"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E04"
SOURCE_FILE = "sources/dix-pour-cent/s02/e04.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 481-515. Film director Sacha Hartman is furious because he believes Isabelle Adjani is avoiding him. "
    "Andréa calms him down, picks up the phone, and speaks directly with Isabelle to set up a meeting at the office "
    "the next morning at eleven o'clock."
)

INTRO = (
    "In her office, Andréa meets with German film director Sacha Hartman, who is furious because he believes "
    "superstar Isabelle Adjani is ignoring him. Andréa decides to take control of the situation and calls Isabelle directly. "
    "Listen to the scene in French first."
)

STORY = [
    ("sacha", "Comment ça, Isabelle est indisponible?",
     "What do you mean, Isabelle is unavailable?",
     [(481, "Comment ça, indisponible ?")], ""),
    ("lea", "Elle a un défilé et des essayages.",
     "She has a fashion show and costume fittings.",
     [(482, "Rien. Elle a des essayages"), (483, "puis un défilé Chanel")], ""),
    ("sacha", "Je suis resté à Paris exprès pour elle!",
     "I stayed in Paris specially for her!",
     [(485, "Mais je suis resté exprès. Qu'est-ce qu'elle fait ?")], ""),
    ("sacha", "Elle me séduit, puis elle me snobe.",
     "She charms me, then she snubs me.",
     [(487, "Elle vous séduit, puis vous snobe")], ""),
    ("lea", "Sacha, ne soyez pas si paranoïaque.",
     "Sacha, do not be so paranoid.",
     [(489, "Sacha, ne soyez pas si paranoïaque")], ""),
    ("sacha", "Je n'ai pas besoin d'Adjani pour mon film.",
     "I do not need Adjani for my movie.",
     [(492, "Je n'ai pas besoin d'Adjani !")], ""),
    ("sacha", "Il y a d'autres grandes actrices.",
     "There are other great actresses.",
     [(493, "Il y a plein de grandes actrices")], ""),
    ("lea", "Attendez, je vais l'appeler tout de suite.",
     "Wait, I am going to call her right away.",
     [(494, "Attendez, je vais l'appeler")], ""),
    ("lea", "Allô Isabelle? C'est Andréa Martel.",
     "Hello Isabelle? It is Andréa Martel.",
     [(497, "Isabelle, c'est Andréa Martel d'ASK")], ""),
    ("lea", "Sacha Hartman aimerait beaucoup vous voir.",
     "Sacha Hartman would really like to see you.",
     [(498, "J'appelle de la part de Sacha Hartman"), (499, "Souhaitez-vous le rencontrer ?")], ""),
    ("lea", "Seriez-vous libre demain matin au bureau?",
     "Would you be free tomorrow morning at the office?",
     [(501, "Demain, au bureau ?")], ""),
    ("lea", "Parfait, rendez-vous demain à onze heures!",
     "Perfect, see you tomorrow at eleven o'clock!",
     [(504, "Demain à 11h"), (505, "Parfait, à demain, Isabelle")], ""),
    ("lea", "Vous voyez, Sacha? C'est réglé.",
     "You see, Sacha? It is settled.",
     [(510, "Alors, c'est réglé !")], ""),
    ("sacha", "Elle a vraiment accepté de me voir?",
     "She really agreed to see me?",
     [(506, "Indisponible ?")], ""),
    ("lea", "Oui, elle essaie de vous joindre depuis deux jours.",
     "Yes, she has been trying to reach you for two days.",
     [(499, "Depuis deux jours"), (500, "j'essaie !")], ""),
    ("sacha", "D'accord, alors je serai là demain.",
     "Alright, then I will be there tomorrow.",
     [(504, "D'accord, merci"), (511, "Très bien")], "")
]

OPENER = "Let's examine how Andréa calms down an angry film director."

WALK = [
    (0, None,
     "'What do you mean, Isabelle is unavailable?' Sacha reacts with disbelief and irritation. "
     "The phrase comment ça expresses shock or surprise."),
    (1, None,
     "'She has a fashion show and costume fittings.' Andréa explains the packed schedule. "
     "The noun défilé refers to a fashion runway show."),
    (2, None,
     "'I stayed in Paris specially for her!' Sacha stresses his personal sacrifice. "
     "The adverb exprès means deliberately or on purpose."),
    (3, None,
     "'She charms me, then she snubs me.' Sacha complains about erratic behavior. "
     "The adverb puis marks chronological succession."),
    (4, None,
     "'Sacha, do not be so paranoid.' Andréa tries to calm his growing suspicion. "
     "The formal imperative ne soyez pas expresses gentle advice."),
    (5, None,
     "'I do not need Adjani for my movie.' Sacha defensively claims he can manage without her. "
     "The verbal expression avoir besoin de means to need."),
    (6, None,
     "'There are other great actresses.' Sacha insists that alternatives exist. "
     "The plural adjective autres precedes the noun."),
    (7, None,
     "'Wait, I am going to call her right away.' Andréa takes matters into her own hands. "
     "The locution tout de suite means immediately."),
    (8, None,
     "'Hello Isabelle? It is Andréa Martel.' Andréa greets the star politely on the phone. "
     "The interjection allô is standard when starting phone calls."),
    (9, None,
     "'Sacha Hartman would really like to see you.' Andréa presents the director's interest smoothly. "
     "The conditional aimerait expresses a polite wish."),
    (10, None,
     "'Would you be free tomorrow morning at the office?' She suggests a convenient meeting time. "
     "The conditional seriez-vous politely asks about availability."),
    (11, None,
     "'Perfect, see you tomorrow at eleven o'clock!' Andréa confirms the agreed time enthusiastically. "
     "The noun rendez-vous designates an appointment."),
    (12, None,
     "'You see, Sacha? It is settled.' Andréa shows him that his fears were unfounded. "
     "The phrase c'est réglé means it is taken care of."),
    (13, None,
     "'She really agreed to see me?' Sacha is pleasantly stunned by the outcome. "
     "The adverb vraiment emphasizes genuine surprise."),
    (14, None,
     "'Yes, she has been trying to reach you for two days.' Andréa reveals Isabelle's true interest. "
     "The preposition depuis denotes an action continuing from the past."),
    (15, None,
     "'Alright, then I will be there tomorrow.' Sacha commits to attending the appointment. "
     "The simple future serai expresses a firm promise.")
]

TRANSITION = "Now let's listen to the negotiation once more at normal pace."

OUTRO = (
    "With a single phone call, Andréa fixes the misunderstanding and confirms the meeting with Isabelle Adjani. "
    "Listen to the conversation once more in French."
)

CLOSING = ("sacha", "D'accord, alors je serai là demain.")
