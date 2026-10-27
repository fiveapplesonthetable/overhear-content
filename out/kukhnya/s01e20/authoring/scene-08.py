ID = "kukhnya-s01e20-scene-08"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 20
SCENE = 8
TITLE = "Утренний сюрприз  (A Morning Surprise)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "kostya": "anja"}
LABELS = {"anya": "Настя", "kostya": "Костя"}
SOURCE_NAME = "Кухня (Kukhnya) S1.20"
SOURCE_FILE = "sources/kukhnya/s01/e20.ru.dual.srt"
SOURCE_NOTE = "Scene 8"

INTRO = "Kostya wakes up in a good mood and misinterprets the situation completely, and we will listen to their dialogue in Russian first; do not worry about catching every single word."

STORY = [
    ("kostya", "Доброе утро, моя дорогая.",
     "Good morning, my dear.",
     [], "new"),
    ("anya", "Это не доброе утро.",
     "It is not a good morning.",
     [], "new"),
    ("kostya", "Почему ты так на меня смотришь?",
     "Why are you looking at me like that?",
     [], "new"),
    ("anya", "Я ждала, когда ты проснешься.",
     "I have been waiting for you to wake up.",
     [], "new"),
    ("kostya", "Ты проснулась и хочешь поиграть со мной?",
     "Are you awake and wanting to play with me?",
     [], "new"),
    ("anya", "Нет, Костя.",
     "No, Kostya.",
     [], "new"),
    ("kostya", "А...",
     "Ah...",
     [], "new"),
    ("kostya", "Я сделал что-то не так?",
     "Did I do something wrong?",
     [], "new"),
    ("anya", "Ты забыл, что мы обсуждали.",
     "You forgot what we discussed.",
     [], "new"),
    ("kostya", "Я всё помню.",
     "I remember everything.",
     [], "new"),
    ("anya", "Тогда почему ты шутишь?",
     "Then why are you joking?",
     [], "new"),
    ("kostya", "Я просто пытаюсь быть милым.",
     "I am just trying to be nice.",
     [], "new"),
]

OPENER = "Let us break down this interaction."

WALK = [
    (0, None,
     "'Good morning, my dear.' -- He says this to her."),
    (1, None,
     "'It is not a good morning.' -- She tells him this."),
    (2, None,
     "'Why are you looking at me like that?' -- He talks directly to her."),
    (3, None,
     "'I have been waiting for you to wake up.' -- She talks directly to him."),
    (4, None,
     "'Are you awake and wanting to play with me?' -- He talks directly to her."),
    (5, None,
     "'No, Kostya.' -- She tells him this."),
    (6, None,
     "'Ah...' -- He says this to her."),
    (7, None,
     "'Did I do something wrong?' -- He asks her a question."),
    (8, None,
     "'You forgot what we discussed.' -- She talks directly to him."),
    (9, None,
     "'I remember everything.' -- He explains his feelings to her."),
    (10, None,
     "'Then why are you joking?' -- She talks directly to him."),
    (11, None,
     "'I am just trying to be nice.' -- He explains his feelings to her."),
]

TRANSITION = "Now let us listen to the conversation again without interruption."
OUTRO = "Nastya quickly ruins his playful mood by bringing up their previous serious chat."
CLOSING = ("kostya", "Я просто пытаюсь быть милым.")
