"""s01e03 scene 10: История про гуся (The Story of the Goose)."""

ID = "kukhnya-s01e03-scene-10"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 3
SCENE = 10
TITLE = "История про гуся  (The Story of the Goose)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "chef": "anja", "lyova": "angelina"}
LABELS = {"anya": "Макс", "chef": "Шеф", "lyova": "Лёва"}
SOURCE_NAME = "Кухня (Kukhnya) S1.03"
SOURCE_FILE = "sources/kukhnya/s01/e03.ru.dual.srt"
SOURCE_NOTE = "Cues 235-243. Max presents a dressed market goose and claims he strangled it without spilling blood."

INTRO = (
    "Having secretly replaced the missing live goose with a dressed market carcass, Max returns to face head chef Viktor Barinov. "
    "Barinov immediately questions why Max's apron is spotless without a single drop of blood, forcing Max to tell a shocking lie. "
    "Let's listen to their confrontation in Russian first."
)

STORY = [
    ("chef", "Огузок! Где мой свежий гусь?",
     "Guzak! Where is my fresh goose?",
     [(235, "Где гусь")], "demanding the bird"),
    ("anya", "Я только что прикончил его!",
     "I have just finished it off!",
     [(236, "Я его только что прикончил")], "announcing the kill"),
    ("chef", "Почему ты такой подозрительно чистый?",
     "Why are you so suspiciously clean?",
     [(237, "А что ты такой чистенький")], "eying his white apron"),
    ("chef", "На тебе нет ни капли крови!",
     "There is not a drop of blood on you!",
     [(237, "ни капельки крови на тебя не попало")], "noticing the lack of mess"),
    ("anya", "Я его совсем не резал.",
     "I did not cut it at all.",
     [(238, "Я его не зарезал")], "explaining his method"),
    ("chef", "И как ты его убил?",
     "And how did you kill it?",
     [], "demanding specifics"),
    ("anya", "Шеф, я его просто задушил!",
     "Chef, I simply strangled it!",
     [(239, "Я его задушил")], "making up a wild lie"),
    ("chef", "Какой кошмар! Настоящий Отелло на кухне!",
     "What a nightmare! A real Othello in the kitchen!",
     [(240, "Какой ужас"), (240, "Ладно, Отелло")], "reacting in theatrical shock"),
    ("chef", "Тащи свою птицу су-шефу на стол!",
     "Drag your bird to the sous-chef's table!",
     [(240, "тащи свою дездемону с ушефу")], "ordering him to deliver the carcass"),
    ("chef", "Лёва, начинай быстро готовить гуся!",
     "Lyova, start preparing the goose quickly!",
     [(241, "Лёва, начинай готовить гуся")], "instructing his deputy"),
    ("lyova", "Понял, шеф, я включаю духовку.",
     "Understood, Chef, I am turning on the oven.",
     [(242, "Понял, шеф")], "getting straight to work"),
    ("chef", "А я займусь важным комплиментом.",
     "And I will take care of an important compliment.",
     [(243, "А я займусь комплиментом от шефа")], "turning to the special dish"),
    ("anya", "Я спас птицу и свою работу.",
     "I saved the bird and my job.",
     [], "reflecting on his narrow escape"),
]

OPENER = "Let's replay a few lines to examine key phrases and vocabulary."

WALK = [
    (1, "Я только что прикончил его!",
     "'I have just finished it off!' Max announces proudly, pretending he personally slaughtered the goose."),
    (3, "На тебе нет ни капли крови!",
     "'There is not a drop of blood on you!' Chef Barinov points out suspiciously."),
    (6, "Шеф, я его просто задушил!",
     "'Chef, I simply strangled it!' Max invents on the spot, creating a bizarre excuse."),
    (9, "Лёва, начинай быстро готовить гуся!",
     "'Lyova, start preparing the goose quickly!' Barinov commands the sous-chef without further delay."),
]

TRANSITION = "Now listen to the full kitchen exchange once more."

OUTRO = "Lyova prepares the bird for roasting while Barinov begins preparing the special compliment."

CLOSING = ("anya", "Никто никогда не узнает эту тайну.")
