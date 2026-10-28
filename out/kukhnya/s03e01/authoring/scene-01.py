# Authoring module for kukhnya-s03e01-scene-01.
ID = 'kukhnya-s03e01-scene-01'
SHOW = 'kukhnya'
SEASON = 3
EPISODE = 1
SCENE = 1
TITLE = 'Новый официант  (The New Waiter)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'guest': 'Гость', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S3.01'
SOURCE_FILE = 'sources/kukhnya/s03/e01.ru.srt'
INTRO = "Welcome to Season Three of Kukhnya. At the French restaurant Claude Monet in Moscow, Max Lavrov has traded his chef jacket for a waiter's vest, and he quickly discovers that serving demanding guests in the dining room is harder than it looks."
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'And that finishes our opening scene in the dining room. Listen for Max introducing his new job as a waiter and promising to memorize the entire order without a notepad. Until next time!'
CLOSING = ('max', 'До завтра!')
STORY = [
    ('max', 'Я Макс Лавров.', 'I am Max Lavrov.', [(1, 'Я Макс Лавров')], ''),
    ('max', 'Раньше работал поваром, теперь я официант.', 'I used to work as a cook, now I am a waiter.', [(1, 'Раньше работал поваром, теперь я официант')], ''),
    ('max', 'Работать официантом совсем не легко.', 'Working as a waiter is not easy at all.', [(2, 'работать официантом легко')], 'adapted'),
    ('max', 'Вы сильно заблуждаетесь.', 'You are gravely mistaken.', [(3, 'вы сильно заблуждаетесь')], ''),
    ('max', 'Здравствуйте!', 'Hello!', [(6, 'Здравствуйте')], ''),
    ('guest', 'Вы записываете?', 'Are you writing this down?', [(7, 'Вы записываете')], ''),
    ('max', 'Я запомню.', 'I will remember it.', [(8, 'Я запомню')], ''),
    ('guest', 'Гратен, пожалуйста. А мне кролика.', 'Gratin, please. And rabbit for me.', [(9, 'Гратен, пожалуйста. А мне кролика')], ''),
    ('guest', 'Салат и вода без газа.', 'A salad and still water.', [(9, 'Салат'), (10, 'И вода без газа')], 'adapted'),
    ('guest', 'И апельсиновый фреш.', 'And fresh orange juice.', [(11, 'И апельсиновый')], 'adapted'),
    ('max', 'Что это?', 'What is this?', [(12, 'Что это')], ''),
    ('max', 'Красота!', 'Beautiful!', [(15, 'Красота')], ''),
]
WALK = [
    (0, None, '\'I am Max Lavrov.\' Max sustains a pointed tone as they talk, linking "ya" ("I"), "maks" ("Max"), and "lavrov" ("Lavrov") in one brisk exchange.'),
    (1, None, '\'I used to work as a cook, now I am a waiter.\' Max presents a pointed course with the guest, joining "ranshe" ("earlier, previously") to "rabotal" ("worked") so every word pulls its weight.'),
    (2, None, '\'Working as a waiter is not easy at all.\' Max sustains a steady course in the room, leaning on "rabotat" ("to work") before closing the thought with "ofitsiantom" ("waiter, server").'),
    (3, None, '\'You are gravely mistaken.\' Max maintains a natural rhythm as the scene unfolds, putting "silno" ("strongly, much") alongside "zabluzhdayetes" ("are mistaken") in a tight, everyday turn of phrase.'),
    (4, None, '\'Hello!\' Max offers a lively course as they talk, putting all the weight on "zdravstvuyte" ("hello") so the reply lands immediately.'),
    (5, None, '\'Are you writing this down?\' The guest challenges sharply in the scene, weaving "zapisyvayete" ("write down") together with "vy" ("you") just the way native speakers do.'),
    (6, None, '\'I will remember it.\' Max displays a thoughtful note on the spot, combining "zapomnyu" ("will remember") and "ya" ("I") so the key meaning lands right away.'),
    (7, None, '\'Gratin, please. And rabbit for me.\' The guest displays an honest direction in their talk, anchoring the Russian line on "graten" ("gratin") and "krolika" ("rabbit") without extra filler.'),
    (8, None, '\'A salad and still water.\' The guest presents a steady stance in their talk, linking "salat" ("salad"), "voda" ("water"), and "gaza" ("gas") in one brisk exchange.'),
    (9, None, '\'And fresh orange juice.\' The guest conveys a candid posture as the scene unfolds, building the phrase around "apelsinovyy" ("orange") and "fresh" ("fresh juice") for a crisp, natural delivery.'),
    (10, None, '\'What is this?\' Max asks openly across the room, building the phrase around "chto" ("what") and "eto" ("this") for a crisp, natural delivery.'),
    (11, None, '\'Beautiful!\' Max conveys a grounded note during the exchange, putting all the weight on "krasota" ("beauty") so the reply lands immediately.'),
]
