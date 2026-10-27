# Authoring module for kukhnya s01e17 scene 13 (cues 221-230).
# Build: python3 tools/compose.py out/kukhnya/s01e17/authoring/scene-13.py --out out/kukhnya/s01e17/scene-13.json

ID = "kukhnya-s01e17-scene-13"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 17
SCENE = 13
TITLE = "Два зала  (Two Dining Rooms)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "shef": "anja"}
LABELS = {"anya": "Хостес", "shef": "Шеф"}
SOURCE_NAME = "Кухня (Kukhnya) S1.17"
SOURCE_FILE = "sources/kukhnya/s01/e17.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 221-230. Visiting a rival restaurant, Chef Viktor Barinov jokes sarcastically about its amenities "
    "before requesting a table in the smoking section."
)

INTRO = (
    "Arriving at a rival restaurant to inspect the competition, Chef Viktor Barinov greets the hostess with heavy sarcasm. "
    "He mocks the dining room amenities before asking for a table in the smoking section. "
    "Let's listen to their conversation in Russian first."
)

OPENER = "Now let's examine this conversation line by line."

STORY = [
    ("anya", "Добрый день, рада видеть вас здесь.",
     "Good afternoon, I am glad to see you here.",
     [(221, "Добрый день. Рада видеть вас")], "adapted"),
    ("anya", "Добро пожаловать в наш новый ресторан.",
     "Welcome to our new restaurant.",
     [(221, "в нашем ресторане")], "adapted"),
    ("anya", "Вам зал для курящих или нет?",
     "Would you like the smoking room or not?",
     [(222, "Вам зал для курящих")], "adapted"),
    ("shef", "А у вас тут есть разделение?",
     "Do you have separate sections here?",
     [(223, "А у вас разделение")], "adapted"),
    ("anya", "Да, у нас есть два зала.",
     "Yes, we have two dining rooms.",
     [(224, "два зала есть")], "adapted"),
    ("shef", "Надо же, даже два зала есть!",
     "Well now, there are even two rooms!",
     [(224, "Надо же. И два зала есть")], "adapted"),
    ("shef", "И кондиционер тут тоже работает хорошо.",
     "And the air conditioner works well here too.",
     [(225, "И кондиционер")], "adapted"),
    ("shef", "Это просто настоящий дворец восточного шейха.",
     "This is simply a real palace of an eastern sheikh.",
     [(226, "Просто дворец шейха")], "adapted"),
    ("anya", "У вас сегодня очень смешные шутки.",
     "You have very funny jokes today.",
     [(227, "Шутки такие")], "adapted"),
    ("shef", "Нам нужен простой зал для курящих.",
     "We need a regular room for smokers.",
     [(228, "Нам простой зал")], "adapted"),
    ("anya", "Хорошо, прошу вас пройти за мной.",
     "Very well, please follow me.",
     [(229, "Прошу")], "adapted"),
    ("shef", "Большое спасибо, мы идём за вами.",
     "Thank you very much, we are following you.",
     [(229, "Спасибо")], "adapted"),
    ("anya", "Вот ваш удобный столик у окна.",
     "Here is your comfortable table by the window.",
     [(230, "Прошу")], "adapted"),
    ("shef", "Отлично, принесите нам меню, пожалуйста.",
     "Great, bring us the menu, please.",
     [(229, "Спасибо")], "adapted"),
]

WALK = [
    (0, None,
     "'Good afternoon, I am glad to see you here.' -- The hostess politely welcomes the guests at the door."),
    (1, None,
     "'Welcome to our new restaurant.' -- She invites them into the dining room."),
    (2, None,
     "'Would you like the smoking room or not?' -- She asks which section of the restaurant they prefer."),
    (3, None,
     "'Do you have separate sections here?' -- Viktor feigns surprise at the basic layout of the rival venue."),
    (4, None,
     "'Yes, we have two dining rooms.' -- The hostess confirms that the restaurant has two distinct halls."),
    (5, None,
     "'Well now, there are even two rooms!' -- Viktor teases the staff with exaggerated amazement."),
    (6, None,
     "'And the air conditioner works well here too.' -- He continues his ironic praise of the ventilation."),
    (7, None,
     "'This is simply a real palace of an eastern sheikh.' -- He compares the modest place to a royal palace."),
    (8, None,
     "'You have very funny jokes today.' -- The remark earns an unimpressed reaction to his humor."),
    (9, None,
     "'We need a regular room for smokers.' -- Viktor finally states their seating preference to the hostess."),
    (10, None,
     "'Very well, please follow me.' -- The hostess gestures for the guests to walk with her."),
    (11, None,
     "'Thank you very much, we are following you.' -- Viktor acknowledges her politely as they head inside."),
    (12, None,
     "'Here is your comfortable table by the window.' -- She shows them to an open table."),
    (13, None,
     "'Great, bring us the menu, please.' -- Viktor settles into his seat and asks for the menu."),
]

TRANSITION = "Now let's listen to the whole restaurant greeting again without interruption."
OUTRO = (
    "Having amused himself with sarcastic remarks about the rival establishment, Chef Viktor Barinov takes his seat "
    "in the smoking section to inspect their menu."
)
CLOSING = ("shef", "Нам нужен простой зал для курящих.")
