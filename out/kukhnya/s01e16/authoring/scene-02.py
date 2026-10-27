ID = "kukhnya-s01e16-scene-02"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 16
SCENE = 2
TITLE = "Случайный звонок  (An Accidental Call)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "leva": "anja", "guest": "angelina"}
LABELS = {'anya': 'Инспектор', 'leva': 'Вика', 'guest': 'Дмитрий'}
SOURCE_NAME = "Кухня (Kukhnya) S1.16"
SOURCE_FILE = "sources/kukhnya/s01/e16.ru.dual.srt"
SOURCE_NOTE = "Cues."

INTRO = (
    "The fire inspector continues his strict check and rejects several fire extinguishers. The restaurant owner, Dmitry, arrives and demands to know the real reason behind this sudden and aggressive inspection. Let us listen to their conversation in Russian first."
)

STORY = [
    ("anya", "Где ваш огнетушитель?",
     "Where is your fire extinguisher?",
     [(10, 'А где огнетушитель?')], "adapted"),
    ("leva", "Он висел здесь в прошлый раз.",
     "It was hanging here last time.",
     [(11, 'Он же висел у вас в прошлый раз.')], "adapted"),
    ("anya", "Вы что, смеётесь надо мной?",
     "Are you laughing at me?",
     [(12, 'Вы что, издеваетесь, что ли?')], "adapted"),
    ("anya", "Этот не подходит.",
     "This one is not suitable.",
     [(14, 'Не годим.')], "adapted"),
    ("leva", "Вот нормальный огнетушитель.",
     "Here is a normal fire extinguisher.",
     [(15, 'Браку! Ну вот, нормальный огнетушитель.')], "adapted"),
    ("anya", "А где его пломба?",
     "And where is its seal?",
     [(16, 'А пломба где?')], "adapted"),
    ("guest", "Добрый день.",
     "Good afternoon.",
     [], "new"),
    ("guest", "Можно узнать одну вещь?",
     "May I know one thing?",
     [(19, 'А можно узнать, чем вызван столь бурный интерес к пожарной безопасности моего')], "adapted"),
    ("guest", "Почему у вас такой интерес к ресторану?",
     "Why do you have such an interest in the restaurant?",
     [(20, 'ресторана? Можно.')], "adapted"),
    ("anya", "Мы боремся с плохим руководством.",
     "We are fighting with bad management.",
     [(21, 'Интерес вызван борьбой с халатностью руководства,')], "adapted"),
    ("anya", "Был звонок моему начальнику.",
     "There was a call to my boss.",
     [(22, 'а также с безобразным состоянием пожарной техники и звонком моему')], "adapted"),
    ("anya", "Из соседнего ресторана.",
     "From the neighboring restaurant.",
     [(23, 'начальнику из соседнего ресторана.')], "adapted"),
    ("guest", "Всё понятно.",
     "Everything is clear.",
     [(25, 'Понятно.')], "adapted"),
    ("anya", "Ну что, до завтра.",
     "Well then, until tomorrow.",
     [(26, 'Ну что, до завтра.')], "adapted"),
]

OPENER = "Now let us examine the conversation line by line."

WALK = [
    (0, None,
     "'Where is your fire extinguisher?' -- The speaker makes the statement."),
    (1, None,
     "'It was hanging here last time.' -- The speaker makes the statement."),
    (2, None,
     "'Are you laughing at me?' -- The speaker makes the statement."),
    (3, None,
     "'This one is not suitable.' -- The speaker makes the statement."),
    (4, None,
     "'Here is a normal fire extinguisher.' -- The speaker makes the statement."),
    (5, None,
     "'And where is its seal?' -- The speaker makes the statement."),
    (6, None,
     "'Good afternoon.' -- The speaker makes the statement."),
    (7, None,
     "'May I know one thing?' -- The speaker makes the statement."),
    (8, None,
     "'Why do you have such an interest in the restaurant?' -- The speaker makes the statement."),
    (9, None,
     "'We are fighting with bad management.' -- The speaker makes the statement."),
    (10, None,
     "'There was a call to my boss.' -- The speaker makes the statement."),
    (11, None,
     "'From the neighboring restaurant.' -- The speaker makes the statement."),
    (12, None,
     "'Everything is clear.' -- The speaker makes the statement."),
    (13, None,
     "'Well then, until tomorrow.' -- The speaker makes the statement."),
]

TRANSITION = "Now let us listen to the conversation once again."
OUTRO = "The conversation concludes the matter at hand."
CLOSING = ("anya", "Ну что, до завтра.")
