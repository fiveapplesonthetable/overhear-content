ID = "kukhnya-s01e18-scene-01"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 18
SCENE = 1
TITLE = "История Золушки  (A Cinderella Story)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "sasha": "anja", "dmitry": "angelina"}
LABELS = {"anya": "Кристина", "sasha": "Саша", "dmitry": "Дмитрий"}
SOURCE_NAME = "Кухня (Kukhnya) S1.18"
SOURCE_FILE = "sources/kukhnya/s01/e18.ru.dual.srt"
SOURCE_NOTE = "Cues 1-17. Kristina visits the restaurant as Dmitry's wife."

INTRO = "Kristina, a former hostess who married the wealthy restaurant owner Dmitry, visits her old friends at work. Let's listen closely to their exchange in Russian first, and then walk through each line together."

STORY = [
    ("sasha", "Ой, Кристина, здравствуйте!",
     "Oh, Kristina, hello!",
     [(5, "Ой, Кристина, здравствуйте.")], "adapted"),
    ("anya", "Что ещё за официальное здравствуйте?",
     "What is with the formal hello?",
     [(6, "что за здравствуйте")], "adapted"),
    ("sasha", "Я не могу иначе, я на работе.",
     "I cannot do otherwise, I am at work.",
     [(7, "Я не могу")], "adapted"),
    ("anya", "Я тебя прекрасно понимаю, подруга.",
     "I understand you very well, friend.",
     [(8, "Я тебя прекрасно понимаю")], "adapted"),
    ("anya", "Я сама здесь целый год работала.",
     "I worked here for a whole year myself.",
     [(8, "я сама здесь год")], "adapted"),
    ("sasha", "Привет, Кристина, ты отлично выглядишь!",
     "Hi, Kristina, you look great!",
     [(11, "Привет, отлично выглядишь!")], "adapted"),
    ("anya", "Спасибо, моя хорошая!",
     "Thank you, my dear!",
     [(10, "моя хорошая")], "adapted"),
    ("sasha", "Ты когда вернулась домой в Москву?",
     "When did you return home to Moscow?",
     [(12, "Ты когда вернулась?")], "adapted"),
    ("anya", "Позавчера, но тут мне очень скучно.",
     "The day before yesterday, but I am very bored here.",
     [(13, "Позавчера")], "adapted"),
    ("anya", "Я думаю скоро улететь в Монако!",
     "I am thinking of flying to Monaco soon!",
     [(13, "в Монако улететь")], "adapted"),
    ("dmitry", "Сейчас я проверю отчёты и поедем.",
     "Now I will check the reports and we will go.",
     [(15, "отчеты проверю и поедем")], "adapted"),
    ("dmitry", "Мы поедем в магазин и купим подарки!",
     "We will go to the store and buy gifts!",
     [(15, "поедем в магазин")], "adapted"),
]

OPENER = "Let's break down this friendly reunion."

WALK = [
    (0, None,
     "'Oh, Kristina, hello!' -- The waitress greets the owner's wife with formal politeness."),
    (1, None,
     "'What is with the formal hello?' -- Kristina asks her friend to speak casually with her."),
    (2, None,
     "'I cannot do otherwise, I am at work.' -- She explains that rules apply during her shift."),
    (3, None,
     "'I understand you very well, friend.' -- Kristina remembers how strict the manager can be."),
    (4, None,
     "'I worked here for a whole year myself.' -- She recalls her own time as a hostess in the hall."),
    (5, None,
     "'Hi, Kristina, you look great!' -- Sasha admires her stylish outfit and happy smile."),
    (6, None,
     "'Thank you, my dear!' -- Kristina warmly thanks her former colleague for the compliment."),
    (7, None,
     "'When did you return home to Moscow?' -- Sasha asks about the recent trip abroad."),
    (8, None,
     "'The day before yesterday, but I am very bored here.' -- Kristina complains that city life feels dull to her."),
    (9, None,
     "'I am thinking of flying to Monaco soon!' -- She shares her glamorous travel plans with the girls."),
    (10, None,
     "'Now I will check the reports and we will go.' -- Dmitry promises to finish his paperwork quickly."),
    (11, None,
     "'We will go to the store and buy gifts!' -- He invites his wife to go shopping with him."),
]

TRANSITION = "Now let's listen to the scene again without interruption."
OUTRO = "Dmitry heads to the office to check the restaurant figures while Kristina waits."
CLOSING = ("dmitry", "Мы поедем в магазин и купим подарки!")
