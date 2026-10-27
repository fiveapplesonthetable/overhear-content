ID = "kukhnya-s01e15-scene-03"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 15
SCENE = 3
TITLE = "Утренний звонок  (A Morning Call)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "lyuba": "anja"}
LABELS = {"anya": "Баринов", "lyuba": "Люба"}
SOURCE_NAME = "Кухня (Kukhnya) S1.15"
SOURCE_FILE = "sources/kukhnya/s01/e15.ru.dual.srt"
SOURCE_NOTE = "Cues 15-20. Lyuba calls Viktor Petrovich."

INTRO = "Viktor Petrovich wakes up with a terrible headache as Lyuba calls to remind him about work. Let's listen closely to their exchange in Russian first, and then walk through each line together."

STORY = [
    ("anya", "Что за шум с утра пораньше?",
     "What is that noise early in the morning?",
     [], "new"),
    ("anya", "Кто мне звонит так рано утром?",
     "Who is calling me so early in the morning?",
     [], "new"),
    ("lyuba", "Алло, Виктор Петрович, вы уже встали?",
     "Hello, Viktor Petrovich, are you up already?",
     [(16, "Алло. Виктор Петрович, вы уже встали?")], "adapted"),
    ("anya", "Конечно, я давно уже на ногах.",
     "Of course, I have been up for a long time.",
     [], "new"),
    ("lyuba", "Вы меня обманываете, вы ещё спите!",
     "You are lying to me, you are still sleeping!",
     [(17, "Вы меня обманываете")], "adapted"),
    ("anya", "Я бодрый и полон новых сил.",
     "I am cheerful and full of new strength.",
     [], "new"),
    ("lyuba", "Виктор Петрович, вы опоздаете на работу!",
     "Viktor Petrovich, you will be late for work!",
     [(18, "Виктор Петрович, вы опоздаете на работу")], "adapted"),
    ("anya", "Люба, отстань, я знаю своё дело.",
     "Lyuba, leave me alone, I know my business.",
     [(19, "Люба, отстань")], "adapted"),
    ("lyuba", "Ресторан скоро открывается для гостей.",
     "The restaurant is opening soon for guests.",
     [], "new"),
    ("anya", "Это ты опоздаешь сегодня на смену!",
     "You are the one who will be late for the shift today!",
     [(19, "Это ты опоздаешь")], "adapted"),
    ("lyuba", "А когда вы сами приедете на кухню?",
     "And when will you arrive at the kitchen yourself?",
     [], "new"),
    ("anya", "А я шеф, я немного задержусь!",
     "And I am the chef, I will be a little late!",
     [(20, "А я задержусь")], "adapted"),
]

OPENER = "Let's break down this morning phone call."

WALK = [
    (0, None,
     "'What is that noise early in the morning?' -- Viktor complains about the loud phone ring."),
    (1, None,
     "'Who is calling me so early in the morning?' -- The chef is annoyed by this sudden wake up call."),
    (2, None,
     "'Hello, Viktor Petrovich, are you up already?' -- Lyuba checks if he is awake and ready."),
    (3, None,
     "'Of course, I have been up for a long time.' -- Viktor pretends that he woke up hours ago."),
    (4, None,
     "'You are lying to me, you are still sleeping!' -- She can tell from his sleepy voice that he is in bed."),
    (5, None,
     "'I am cheerful and full of new strength.' -- He claims to be completely fresh and energized."),
    (6, None,
     "'Viktor Petrovich, you will be late for work!' -- She warns him that the kitchen awaits his arrival."),
    (7, None,
     "'Lyuba, leave me alone, I know my business.' -- The chef brushes off her concerns with annoyance."),
    (8, None,
     "'The restaurant is opening soon for guests.' -- She reminds him of the opening time for patrons."),
    (9, None,
     "'You are the one who will be late for the shift today!' -- Viktor retorts that she should mind her own schedule."),
    (10, None,
     "'And when will you arrive at the kitchen yourself?' -- She persists in asking about his plans."),
    (11, None,
     "'And I am the chef, I will be a little late!' -- He asserts his authority to come in whenever he wants."),
]

TRANSITION = "Now let's listen to the scene again without interruption."
OUTRO = "Viktor hangs up the phone, determined to get a few more minutes of rest."
CLOSING = ("anya", "А я шеф, я немного задержусь!")
