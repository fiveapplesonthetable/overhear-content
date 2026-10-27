# Authoring module for kukhnya s01e17 scene 16 (cues 265-269).
# Build: python3 tools/compose.py out/kukhnya/s01e17/authoring/scene-16.py --out out/kukhnya/s01e17/scene-16.json

ID = "kukhnya-s01e17-scene-16"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 17
SCENE = 16
TITLE = "Строгая оценка  (A Strict Assessment)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "shef": "anja", "nagiev": "angelina"}
LABELS = {"anya": "Хостес", "shef": "Шеф", "nagiev": "Нагиев"}
SOURCE_NAME = "Кухня (Kukhnya) S1.17"
SOURCE_FILE = "sources/kukhnya/s01/e17.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 265-269. After finishing their meal at the rival restaurant, the hostess asks how they liked the food; "
    "while his companion praises the meal, Chef Viktor grudgingly admits that it will do."
)

INTRO = (
    "After finishing their meal at the rival restaurant, the hostess approaches the table to ask for their impressions. "
    "While his companion enthusiastically praises the dishes, Chef Viktor Barinov gives a reluctant verdict. "
    "Let's listen to their conversation in Russian first."
)

OPENER = "Now let's examine this conversation line by line."

STORY = [
    ("anya", "Добрый день, уважаемые гости нашего ресторана.",
     "Good afternoon, respected guests of our restaurant.",
     [(265, "Добрый день")], "adapted"),
    ("anya", "Я надеюсь, вам сегодня всё понравилось.",
     "I hope you enjoyed everything today.",
     [(266, "Я надеюсь, вам все понравилось")], "adapted"),
    ("nagiev", "Здравствуйте, да, всё было очень вкусно.",
     "Hello, yes, everything was very delicious.",
     [(267, "Да, очень вкусно")], "adapted"),
    ("nagiev", "У вас тут просто отличная кухня.",
     "You have a simply great kitchen here.",
     [(267, "очень вкусно")], "adapted"),
    ("nagiev", "Почти так же вкусно, как дома.",
     "Almost as delicious as at home.",
     [(268, "Практически как у нас")], "adapted"),
    ("nagiev", "Ты согласен со мной, дорогой друг?",
     "Do you agree with me, dear friend?",
     [(268, "Да, Вик")], "adapted"),
    ("shef", "Ну, в целом эта еда нормальная.",
     "Well, overall this food is fine.",
     [(269, "Сойдет")], "adapted"),
    ("anya", "Спасибо вам за такие добрые слова.",
     "Thank you for such kind words.",
     [(266, "вам все понравилось")], "adapted"),
    ("nagiev", "Мы провели здесь очень приятный день.",
     "We spent a very pleasant day here.",
     [(267, "очень вкусно")], "adapted"),
    ("shef", "Но наш ресторан всё равно лучше.",
     "But our restaurant is still better.",
     [(268, "как у нас")], "adapted"),
    ("anya", "Приходите к нам в гости снова.",
     "Come visit us again.",
     [(265, "Добрый день")], "adapted"),
    ("nagiev", "Обязательно придём сюда в следующий раз.",
     "We will definitely come here next time.",
     [(267, "очень вкусно")], "adapted"),
    ("shef", "Ладно, нам уже пора ехать обратно.",
     "All right, it is time for us to head back.",
     [(269, "Сойдет")], "adapted"),
    ("anya", "Всего доброго, до новой скорой встречи!",
     "All the best, until we meet again soon!",
     [(265, "Добрый день")], "adapted"),
]

WALK = [
    (0, None,
     "'Good afternoon, respected guests of our restaurant.' -- The hostess greets the diners politely at their table."),
    (1, None,
     "'I hope you enjoyed everything today.' -- She asks whether they were satisfied with the meal."),
    (2, None,
     "'Hello, yes, everything was very delicious.' -- The guest responds with warm praise for the cooking."),
    (3, None,
     "'You have a simply great kitchen here.' -- He compliments the culinary team of the rival venue."),
    (4, None,
     "'Almost as delicious as at home.' -- He compares the dishes favorably to their own place."),
    (5, None,
     "'Do you agree with me, dear friend?' -- He turns to Viktor to ask for his culinary opinion."),
    (6, None,
     "'Well, overall this food is fine.' -- The proud head chef reluctantly concedes that the food is passable."),
    (7, None,
     "'Thank you for such kind words.' -- The hostess expresses gratitude for the positive feedback."),
    (8, None,
     "'We spent a very pleasant day here.' -- The guest remarks on their enjoyable afternoon visit."),
    (9, None,
     "'But our restaurant is still better.' -- Viktor mutters loyally that Claude Monet remains superior."),
    (10, None,
     "'Come visit us again.' -- The hostess invites them to return in the future."),
    (11, None,
     "'We will definitely come here next time.' -- The guest promises that they will stop by again."),
    (12, None,
     "'All right, it is time for us to head back.' -- Viktor signals that they need to return to work."),
    (13, None,
     "'All the best, until we meet again soon!' -- The hostess bids them a warm farewell."),
]

TRANSITION = "Now let's listen to the whole restaurant farewell scene again without interruption."
OUTRO = (
    "Though reluctant to praise a competitor, Chef Viktor Barinov admits that the rival restaurant's dishes "
    "are passable before heading back to Claude Monet."
)
CLOSING = ("shef", "Ну, в целом эта еда нормальная.")
