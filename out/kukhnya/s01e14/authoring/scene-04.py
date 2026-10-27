ID = "kukhnya-s01e14-scene-04"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 14
SCENE = 4
TITLE = "Лицо ресторана  (Face of the Restaurant)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "vika": "anja"}
LABELS = {"anya": "Дмитрий", "vika": "Виктор"}
SOURCE_NAME = "Кухня (Kukhnya) S1.14"
SOURCE_FILE = "sources/kukhnya/s01/e14.ru.dual.srt"
SOURCE_NOTE = "Cues 46-47."

INTRO = "Dmitry nervously waits for Chef Viktor at the catering event, but Viktor is running late. Let's listen closely to their exchange in Russian first, and then walk through each line together."

STORY = [
    ("anya", "Витя, ты где? Уже гости собирается.",
     "Vitya, where are you? The guests are already arriving.",
     [(46, 'Алло, Витя, ты где? Уже гости собирается.')], "adapted"),
    ("vika", "Алло, Дима, я еду на машине.",
     "Hello, Dima, I am driving in the car.",
     [], "new"),
    ("anya", "Почему ты так сильно опаздываешь сегодня?",
     "Why are you so very late today?",
     [], "new"),
    ("vika", "Были ужасные пробки на дороге.",
     "There were terrible traffic jams on the road.",
     [], "new"),
    ("anya", "Наш важный клиент уже ждёт тебя.",
     "Our important client is already waiting for you.",
     [], "new"),
    ("vika", "Скажи им, чтобы они пили вино.",
     "Tell them so that they drink wine.",
     [], "new"),
    ("anya", "Я уже налил им лучший коньяк.",
     "I already poured them the best cognac.",
     [], "new"),
    ("vika", "Вот и отлично, пусть отдыхают пока.",
     "That is excellent, let them rest for now.",
     [], "new"),
    ("anya", "Ты должен быть здесь через пять минут!",
     "You must be here in five minutes!",
     [], "new"),
    ("vika", "Не кричи на меня, я подъезжаю.",
     "Do not yell at me, I am almost there.",
     [(47, 'Я подъезжаю.')], "adapted"),
    ("anya", "Я жду тебя у главного входа.",
     "I am waiting for you at the main entrance.",
     [], "new"),
    ("vika", "Иду, иду, уже почти на месте.",
     "Coming, coming, already almost at the place.",
     [], "new"),
]

OPENER = "Let's break down this frantic phone call."

WALK = [
    (0, None,
     "'Vitya, where are you? The guests are already arriving.' -- Dmitry urgently calls him on the phone."),
    (1, None,
     "'Hello, Dima, I am driving in the car.' -- The chef answers him with a sluggish voice."),
    (2, None,
     "'Why are you so very late today?' -- Dmitry asks him about the terrible delay."),
    (3, None,
     "'There were terrible traffic jams on the road.' -- Viktor gives him a standard excuse."),
    (4, None,
     "'Our important client is already waiting for you.' -- The boss reminds him of their VIP guest."),
    (5, None,
     "'Tell them so that they drink wine.' -- The chef advises him to serve alcohol."),
    (6, None,
     "'I already poured them the best cognac.' -- Dmitry informs him about the expensive drinks."),
    (7, None,
     "'That is excellent, let them rest for now.' -- Viktor tells him to keep them busy."),
    (8, None,
     "'You must be here in five minutes!' -- The owner shouts an angry ultimatum to him."),
    (9, None,
     "'Do not yell at me, I am almost there.' -- The chef promises him an imminent arrival."),
    (10, None,
     "'I am waiting for you at the main entrance.' -- Dmitry tells him his exact location."),
    (11, None,
     "'Coming, coming, already almost at the place.' -- Viktor assures him he is very close."),
]

TRANSITION = "Now let's listen to the conversation again without interruption."
OUTRO = "Viktor finally arrives, but his intoxicated state will cause even more problems."
CLOSING = ("vika", "Иду, иду, уже почти на месте.")
