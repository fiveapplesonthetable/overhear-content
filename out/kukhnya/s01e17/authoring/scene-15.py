# Authoring module for kukhnya s01e17 scene 15 (cues 241-264).
# Build: python3 tools/compose.py out/kukhnya/s01e17/authoring/scene-15.py --out out/kukhnya/s01e17/scene-15.json

ID = "kukhnya-s01e17-scene-15"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 17
SCENE = 15
TITLE = "Билет в клуб  (A Ticket to the Club)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "vika": "anja", "shef": "angelina"}
LABELS = {"anya": "Макс", "vika": "Вика", "shef": "Шеф"}
SOURCE_NAME = "Кухня (Kukhnya) S1.17"
SOURCE_FILE = "sources/kukhnya/s01/e17.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 241-264. While Chef Viktor mocks the rival restaurant's chaotic fusion menu, Vika tells Max about "
    "her holiday dinner plans and discovers his single club ticket from Kostya and Nastya."
)

INTRO = (
    "At the rival restaurant, Chef Viktor Barinov scoffs at a chaotic menu combining cuisines from around the world. "
    "Meanwhile back at Claude Monet, Vika shares her dinner plans with Max before spotting his concert ticket. "
    "Let's listen to their conversation in Russian first."
)

OPENER = "Now let's examine this conversation line by line."

STORY = [
    ("shef", "Меню уже у нас, большое спасибо.",
     "We already have the menu, thank you very much.",
     [(241, "Меню есть, спасибо")], "adapted"),
    ("shef", "Ну и что тут у нас?",
     "So what do we have here?",
     [(244, "Ну что тут у нас")], "adapted"),
    ("shef", "Тут русская, французская и японская кухня.",
     "Here is Russian, French, and Japanese cuisine.",
     [(245, "Русская кухня, французская")], "adapted"),
    ("shef", "Они называют это всей кухней мира.",
     "They call this cuisine from all over the world.",
     [(247, "Вся кухня мира")], "adapted"),
    ("shef", "Тут есть пицца, суши и борщ.",
     "They have pizza, sushi, and borscht here.",
     [(251, "Пицца, суши")], "adapted"),
    ("vika", "Макс, как идут дела на кухне?",
     "Max, how are things going in the kitchen?",
     [(254, "Как дела")], "adapted"),
    ("anya", "Всё хорошо, мы спокойно работаем.",
     "Everything is fine, we are working calmly.",
     [(255, "Вот, работаем")], "adapted"),
    ("vika", "Я придумала блюдо на праздничный ужин.",
     "I thought of a dish for the holiday dinner.",
     [(256, "приготовить на праздничный ужин")], "adapted"),
    ("anya", "Это просто здорово, большое спасибо тебе.",
     "That is simply great, thank you very much.",
     [(257, "Здорово")], "adapted"),
    ("vika", "Подожди, а это что за билет?",
     "Wait, what kind of ticket is this?",
     [(258, "А это что")], "adapted"),
    ("anya", "Настя и Костя подарили билет в клуб.",
     "Nastya and Kostya gave me a ticket to the club.",
     [(259, "подарили билет на сегодня в клуб")], "adapted"),
    ("vika", "Значит, там только один билет?",
     "So there is only one ticket there?",
     [(260, "Один")], "adapted"),
    ("vika", "Мне готовить сегодня ужин или нет?",
     "Should I cook dinner tonight or not?",
     [(262, "мне готовить ужин или нет")], "adapted"),
    ("anya", "Вика, мои друзья меня точно поймут.",
     "Vika, my friends will definitely understand me.",
     [(264, "они меня поймут")], "adapted"),
]

WALK = [
    (0, None,
     "'We already have the menu, thank you very much.' -- Viktor tells the waiter they do not need another menu."),
    (1, None,
     "'So what do we have here?' -- The head chef opens the menu to examine the rival dishes."),
    (2, None,
     "'Here is Russian, French, and Japanese cuisine.' -- He reads out the wildly different culinary styles."),
    (3, None,
     "'They call this cuisine from all over the world.' -- He mocks the pretentious fusion concept."),
    (4, None,
     "'They have pizza, sushi, and borscht here.' -- Viktor laughs at the absurd combination of dishes."),
    (5, None,
     "'Max, how are things going in the kitchen?' -- Back at Claude Monet, Vika checks in on Max."),
    (6, None,
     "'Everything is fine, we are working calmly.' -- Max reports that the kitchen shift is going smoothly."),
    (7, None,
     "'I thought of a dish for the holiday dinner.' -- Vika reveals that she planned a special birthday meal for him."),
    (8, None,
     "'That is simply great, thank you very much.' -- Max appreciates the romantic gesture from her."),
    (9, None,
     "'Wait, what kind of ticket is this?' -- Vika suddenly notices the club pass on the counter."),
    (10, None,
     "'Nastya and Kostya gave me a ticket to the club.' -- Max explains that his friends bought it as a gift."),
    (11, None,
     "'So there is only one ticket there?' -- Vika points out that she was not included in their club plan."),
    (12, None,
     "'Should I cook dinner tonight or not?' -- She asks pointedly whether he is choosing the club or her dinner."),
    (13, None,
     "'Vika, my friends will definitely understand me.' -- Max reassures her that he would rather spend the evening with her."),
]

TRANSITION = "Now let's listen to the whole scene again without interruption."
OUTRO = (
    "Caught between his friends' club outing and Vika's romantic birthday dinner, Max promises Vika "
    "that Kostya and Nastya will understand if he stays with her."
)
CLOSING = ("anya", "Вика, мои друзья меня точно поймут.")
