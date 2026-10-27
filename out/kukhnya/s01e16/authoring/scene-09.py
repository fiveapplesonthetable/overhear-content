ID = "kukhnya-s01e16-scene-09"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 16
SCENE = 9
TITLE = "Проверка у конкурентов  (Inspection at the Rivals)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "leva": "anja", "dima": "angelina"}
LABELS = {'anya': 'Елена', 'leva': 'Инспектор', 'dima': 'Шеф'}
SOURCE_NAME = "Кухня (Kukhnya) S1.16"
SOURCE_FILE = "sources/kukhnya/s01/e16.ru.dual.srt"
SOURCE_NOTE = "Cues 62-87."

INTRO = (
    "A migration inspector finishes his check at Elena's restaurant. He is very impressed. He says there are no illegal workers. They decide to eat at Claude Monet. Let us listen to their conversation in Russian first."
)

STORY = [
    ("leva", "Ваш ресторан будет отличным.",
     "Your restaurant will be excellent.",
     [(62, "Ну что же, уважаемая Елена Павловна, мне кажется, что ваш ресторан будет..."), (63, "весьма успешным.")], "adapted"),
    ("anya", "Мы все делаем правильно.", "We do everything right.", [], "new"),
    ("anya", "Большое спасибо вам.",
     "Thank you very much.",
     [(64, "Спасибо.")], "adapted"),
    ("leva", "Вы меня очень удивили.",
     "You really surprised me.",
     [(66, "Признаюсь, вы меня очень сильно удивили.")], "adapted"),
    ("leva", "Ни одного повара без документов.",
     "Not a single cook without documents.",
     [(67, "Ни одного нелегального работника на кухне.")], "adapted"),
    ("anya", "Я привыкла работать по закону.",
     "I got used to working by the law.",
     [(68, "Дело в том, что я очень долго работала за границей и привыкла,"), (69, "чтобы все было по закону.")], "adapted"),
    ("leva", "Мне было очень приятно.",
     "It was very pleasant for me.",
     [(72, "Мне было чрезвычайно приятно с вами познакомиться.")], "adapted"),
    ("leva", "Пойдём в другой ресторан?",
     "Let us go to another restaurant?",
     [(74, "Может, мы еще куда-нибудь прогуляемся?")], "adapted"),
    ("leva", "Тут есть Клод Моне.",
     "Here is Claude Monet.",
     [(75, "В этом же здании есть ресторан."), (76, "Клод Мане.")], "adapted"),
    ("anya", "Отлично, люблю французскую кухню.",
     "Excellent, I love French cuisine.",
     [(77, "Отлично. Я обожаю французскую кухню.")], "adapted"),
    ("dima", "К нам идёт проверка!",
     "An inspection is coming to us!",
     [(79, "К нам идет проверка ФМС.")], "adapted"),
    ("dima", "Все без документов, вон!",
     "Everyone without documents, get out!",
     [(84, "Все нелегалы немедленно вон из ресторана.")], "adapted"),
]

OPENER = "Now let us examine the conversation line by line."

WALK = [
    (0, None,
     "'Your restaurant will be excellent.' -- The speaker states this. ENG"),
    (1, None,
     "'We do everything right.' -- The speaker states this. ENG"),
    (2, None,
     "'Thank you very much.' -- The speaker states this. ENG"),
    (3, None,
     "'You really surprised me.' -- The speaker states this. ENG"),
    (4, None,
     "'Not a single cook without documents.' -- The speaker states this. ENG"),
    (5, None,
     "'I got used to working by the law.' -- The speaker states this. ENG"),
    (6, None,
     "'It was very pleasant for me.' -- The speaker states this. ENG"),
    (7, None,
     "'Let us go to another restaurant?' -- The speaker states this. ENG"),
    (8, None,
     "'Here is Claude Monet.' -- The speaker states this. ENG"),
    (9, None,
     "'Excellent, I love French cuisine.' -- The speaker states this. ENG"),
    (10, None,
     "'An inspection is coming to us!' -- The speaker states this. ENG"),
    (11, None,
     "'Everyone without documents, get out!' -- The speaker states this. ENG"),
]



TRANSITION = "Now let us listen to the conversation once again."
OUTRO = "The conversation concludes the matter at hand."
CLOSING = ("dima", "Все без документов, вон!")
