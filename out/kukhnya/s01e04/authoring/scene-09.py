"""s01e04 scene 09: Приступай к работе (Get to Work)."""

ID = "kukhnya-s01e04-scene-09"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 4
SCENE = 9
TITLE = "Приступай к работе  (Get to Work)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "chef": "anja"}
LABELS = {"anya": "Макс", "chef": "Шеф"}
SOURCE_NAME = "Кухня (Kukhnya) S1.04"
SOURCE_FILE = "sources/kukhnya/s01/e04.ru.dual.srt"

INTRO = (
    "At the hot line of Claude Monet, Chef Viktor Barinov demands a status report from Max about the soup order. "
    "Warning his young cook against foolish errors, the Chef orders him to start cooking immediately without distractions. "
    "Listen to their conversation in Russian first."
)

STORY = [
    ("chef", "Лавров, ты всё понял по заказу?",
     "Lavrov, did you understand everything about the order?",
     [(98, "ты все понял")], "checking comprehension"),
    ("anya", "Да, шеф, я всё отлично понял!",
     "Yes, Chef, I understood everything perfectly!",
     [(99, "Да")], "reporting ready"),
    ("chef", "Суп должен быть идеальным и горячим.",
     "The soup must be ideal and hot.",
     [], "stating requirements"),
    ("anya", "Я использую лучшие овощи и сливки.",
     "I use the best vegetables and cream.",
     [], "listing quality ingredients"),
    ("chef", "Наши гости не терпят глупых ошибок.",
     "Our guests do not tolerate foolish mistakes.",
     [], "setting strict standards"),
    ("anya", "Я гарантирую безупречный вкус этого блюда.",
     "I guarantee the flawless taste of this dish.",
     [], "promising perfection"),
    ("chef", "Хватит болтать языком, Лавров.",
     "Stop chattering away, Lavrov.",
     [], "cutting him off"),
    ("chef", "Ну приступай скорее к работе!",
     "Well get to work quickly!",
     [(99, "Ну приступай")], "commanding action"),
    ("anya", "Уже начинаю готовить прямо сейчас, шеф!",
     "Already starting to cook right now, Chef!",
     [], "getting to work"),
    ("chef", "И внимательно следи за этой плитой!",
     "And watch this stove attentively!",
     [], "giving strict instructions"),
    ("anya", "Я не отойду от неё никуда!",
     "I will not step away from it anywhere!",
     [], "swearing focus"),
    ("chef", "Посмотрим, какой ты повар на деле.",
     "We will see what kind of cook you are in practice.",
     [], "challenging him"),
]

OPENER = "Let's examine this intense kitchen inspection line by line."

WALK = [
    (0, None,
     "'Lavrov, did you understand everything about the order?' Chef Viktor Barinov begins his inspection."),
    (1, None,
     "'Yes, Chef, I understood everything perfectly!' Max responds with eager military precision."),
    (2, None,
     "'The soup must be ideal and hot.' Barinov lays down non-negotiable culinary standards."),
    (3, None,
     "'I use the best vegetables and cream.' Max highlights the premium quality of his ingredients."),
    (4, None,
     "'Our guests do not tolerate foolish mistakes.' The Chef reminds him of the restaurant's reputation."),
    (5, None,
     "'I guarantee the flawless taste of this dish.' Max boldly offers a personal guarantee of success."),
    (6, None,
     "'Stop chattering away, Lavrov.' Barinov cuts short the any boastful kitchen chatter."),
    (7, None,
     "'Well get to work quickly!' The Chef issues an immediate command to begin culinary operations."),
    (8, None,
     "'Already starting to cook right now, Chef!' Max turns to the stove without hesitation."),
    (9, None,
     "'And watch this stove attentively!' Barinov reinforces the necessity of constant temperature control."),
    (10, None,
     "'I will not step away from it anywhere!' Max promises complete devotion to the simmering pot."),
    (11, None,
     "'We will see what kind of cook you are in practice.' The Chef leaves him with a demanding challenge."),
]

TRANSITION = "Now let's listen to the whole exchange again at full speed."

OUTRO = (
    "Under the watchful eye of Chef Barinov, Max takes full charge of the soup station. "
    "See you next time!"
)

CLOSING = ("chef", "Ну приступай скорее к работе!")
