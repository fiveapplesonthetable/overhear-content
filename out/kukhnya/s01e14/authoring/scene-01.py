ID = "kukhnya-s01e14-scene-01"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 14
SCENE = 1
TITLE = "Утренние игры  (Morning Games)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "vika": "anja"}
LABELS = {"anya": "Макс", "vika": "Вика"}
SOURCE_NAME = "Кухня (Kukhnya) S1.14"
SOURCE_FILE = "sources/kukhnya/s01/e14.ru.dual.srt"
SOURCE_NOTE = "Cues 1-3. Morning with Max and Vika."

INTRO = "Max wakes up in Vika's apartment and tries to be playful, but Vika is focused on her day. Let's listen closely to their exchange in Russian first, and then walk through each line together. Let's listen closely to their exchange in Russian first, and then walk through each line together."

STORY = [
    ("anya", "Вика, ты уже проснулась сегодня?",
     "Vika, are you awake already today?",
     [], "new"),
    ("vika", "Да, я уже давно не сплю.",
     "Yes, I have not been sleeping for a long time.",
     [], "new"),
    ("anya", "Почему ты так рано встала?",
     "Why did you get up so early?",
     [], "new"),
    ("vika", "У меня сегодня очень много дел.",
     "I have a lot of things today.",
     [], "new"),
    ("anya", "А как же наш вкусный завтрак?",
     "And what about our tasty breakfast?",
     [], "new"),
    ("vika", "Ты можешь приготовить его сам.",
     "You can prepare it yourself.",
     [], "new"),
    ("anya", "И Макс, я озабоченный человек-паук.",
     "And Max, I am a horny Spider-Man.",
     [(1, 'И Макс, я озабоченный человек-паук.')], "adapted"),
    ("vika", "Очень смешно, но мне надо идти.",
     "Very funny, but I need to go.",
     [], "new"),
    ("anya", "Сейчас я тебя. Какой я тебя?",
     "I will get you now. What am I getting you?",
     [(2, 'Сейчас я тебя. Какой я тебя?')], "adapted"),
    ("vika", "Макс, прекрати это немедленно!",
     "Max, stop this immediately!",
     [], "new"),
    ("anya", "Хорошо, я иду варить нам кофе.",
     "Alright, I am going to brew coffee for us.",
     [], "new"),
    ("vika", "Пока ты не сходишь в душ.",
     "Before you go take a shower.",
     [(3, 'Пока ты не сходишь в душ.')], "adapted"),
]

OPENER = "Let's break down this morning interaction."

WALK = [
    (0, None,
     "'Vika, are you awake already today?' -- Max asks her a simple morning question."),
    (1, None,
     "'Yes, I have not been sleeping for a long time.' -- She replies to him quickly."),
    (2, None,
     "'Why did you get up so early?' -- The young cook wants to know her reason."),
    (3, None,
     "'I have a lot of things today.' -- Victoria tells him about her busy schedule."),
    (4, None,
     "'And what about our tasty breakfast?' -- He reminds her of their shared meal."),
    (5, None,
     "'You can prepare it yourself.' -- The manager suggests he cooks for them."),
    (6, None,
     "'And Max, I am a horny Spider-Man.' -- He makes a silly superhero joke to amuse her."),
    (7, None,
     "'Very funny, but I need to go.' -- She is not impressed by his jokes."),
    (8, None,
     "'I will get you now. What am I getting you?' -- He tries to grab her arm playfully."),
    (9, None,
     "'Max, stop this immediately!' -- She orders him to stop fooling around."),
    (10, None,
     "'Alright, I am going to brew coffee for us.' -- He surrenders and decides to leave her."),
    (11, None,
     "'Before you go take a shower.' -- She reminds him to wash his body first."),
]

TRANSITION = "Now let's listen to the conversation again without interruption."
OUTRO = "Max heads to the shower while Vika prepares for her busy day at the restaurant."
CLOSING = ("vika", "Пока ты не сходишь в душ.")
