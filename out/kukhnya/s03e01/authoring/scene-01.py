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
    (0, None, '\'I am Max Lavrov.\' Leaning in warmly to the guest, Max links the Russian words directly in the present with no word for "am", "is", or "are" needed.'),
    (1, None, '\'I used to work as a cook, now I am a waiter.\' Underscoring a waiter beside the guest, Max chooses "ofitsiant" ("waiter") so the guest gets the point right away.'),
    (2, None, "'Working as a waiter is not easy at all.' Max steps in decisively watching the guest, steering the talk right where he wants it."),
    (3, None, '\'You are gravely mistaken.\' Max cuts in vividly in this beat and lands on "zabluzhdayetes" ("are mistaken", built on "zabluzhdatsya") to keep the statement grounded.'),
    (4, None, '\'Hello!\' Max politely extends this formal greeting while facing the guest using "zdravstvuyte" ("hello") — the polite Russian greeting that literally wishes the other person good health.'),
    (5, None, "'Are you writing this down?' The guest wonders frankly if there is more going on behind the scenes."),
    (6, None, '\'I will remember it.\' Max opens up pointedly around the guest and uses "zapomnyu" ("will remember", from "zapomnit") to make the point stick.'),
    (7, None, '\'Gratin, please. And rabbit for me.\' Pointing to the rabbit with Max, the guest centers the thought on "krolika" ("rabbit", from "krolik") without wasting a word.'),
    (8, None, "'A salad and still water.' The guest opens up quietly watching Max, leaving no doubt about where he stands."),
    (9, None, '\'And fresh orange juice.\' Mentioning the fresh juice in this beat, the guest centers the remark on "apelsinovyy" ("orange") without any extra fuss.'),
    (10, None, '\'What is this?\' Speaking plainly with the guest, Max links the Russian words directly in the present with no word for "am", "is", or "are" needed.'),
    (11, None, "'Beautiful!' Max counters candidly in their talk, testing the guest's reaction in the middle of the exchange."),
]
