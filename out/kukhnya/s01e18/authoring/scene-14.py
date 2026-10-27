ID = "kukhnya-s01e18-scene-14"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 18
SCENE = 14
TITLE = "Секретный разговор  (Secret Conversation)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "leva": "anja", "dima": "angelina"}
LABELS = {'anya': 'Кристина', 'leva': 'Вика', 'dima': 'Шеф'}
SOURCE_NAME = "Кухня (Kukhnya) S1.18"
SOURCE_FILE = "sources/kukhnya/s01/e18.ru.dual.srt"
SOURCE_NOTE = "Cues 265-271."

INTRO = (
    "Kristina talks with Victoria and Viktor about the restaurant's finances. She asks Victoria to leave them alone. Let us listen to their conversation in Russian first."
)

STORY = [
    ("anya", "Мы с Димой обсудили дела.",
     "Dima and I discussed the affairs.",
     [(265, "Мы с Димочкой обсудили дела в ресторане,")], "adapted"),
    ("anya", "У меня есть хорошая идея.",
     "I have a good idea.",
     [(265, "и у меня есть пара мыслей,")], "adapted"),
    ("anya", "Как сделать ресторан лучше.",
     "How to make the restaurant better.",
     [(266, "как сделать снова его рентабельным.")], "adapted"),
    ("anya", "Но сначала хочу поговорить с вами.",
     "But first I want to talk with you.",
     [(267, "Но для начала я хотела бы обсудить с вами")], "adapted"),
    ("anya", "Только с вами, Виктор Петрович.",
     "Only with you, Viktor Petrovich.",
     [(267, "Виктор Петрович,")], "adapted"),
    ("anya", "Если вы не против, Виктория Сергеевна?",
     "If you do not mind, Victoria Sergeyevna?",
     [(268, "если вы, конечно, не против."), (269, "А вы не против, Виктория Сергеевна?")], "adapted"),
    ("leva", "Да, конечно, я не против.",
     "Yes, of course, I do not mind.",
     [(270, "Да, конечно.")], "adapted"),
    ("dima", "Замечательно, я вас слушаю.",
     "Great, I am listening to you.",
     [(271, "Замечательно. Ну, я слышу.")], "adapted"),
    ("anya", "Я посмотрела зарплаты сотрудников.",
     "I looked at the employees salaries.",
     [(282, "Так вот, Виктор Петрович, я посмотрела ведомости с зарплатами сотрудников и поняла,")], "adapted"),
    ("anya", "Нам нужно сделать увольнения.",
     "We need to make layoffs.",
     [(283, "чтобы сократить наши расходы, нужно произвести увольнение.")], "adapted"),
    ("dima", "О чём вы говорите?",
     "What are you talking about?",
     [(284, "Ты о чем?")], "adapted"),
    ("anya", "Вика получает очень много денег.",
     "Vika receives a lot of money.",
     [(286, "Вот, к примеру, Виктория Сергеевна получает аж сто пятьдесят тысяч рублей в месяц.")], "adapted"),
]

OPENER = "Now let us examine the conversation line by line."

WALK = [
    (0, None,
     "'Dima and I discussed the affairs.' -- The speaker states this. ENG"),
    (1, None,
     "'I have a good idea.' -- The speaker states this. ENG"),
    (2, None,
     "'How to make the restaurant better.' -- The speaker states this. ENG"),
    (3, None,
     "'But first I want to talk with you.' -- The speaker states this. ENG"),
    (4, None,
     "'Only with you, Viktor Petrovich.' -- The speaker states this. ENG"),
    (5, None,
     "'If you do not mind, Victoria Sergeyevna?' -- The speaker states this. ENG"),
    (6, None,
     "'Yes, of course, I do not mind.' -- The speaker states this. ENG"),
    (7, None,
     "'Great, I am listening to you.' -- The speaker states this. ENG"),
    (8, None,
     "'I looked at the employees salaries.' -- The speaker states this. ENG"),
    (9, None,
     "'We need to make layoffs.' -- The speaker states this. ENG"),
    (10, None,
     "'What are you talking about?' -- The speaker states this. ENG"),
    (11, None,
     "'Vika receives a lot of money.' -- The speaker states this. ENG"),
]

TRANSITION = "Now let us listen to the conversation once again."
OUTRO = "The conversation concludes the matter at hand."
CLOSING = ("anya", "Вика получает очень много денег.")
