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
    (0, None, '\'I am Max Lavrov.\' Max aims the thought beside the guest: notice how Russian needs no word for "am", "is", or "are" in the present — placing the words side by side says it all.'),
    (1, None, "'I used to work as a cook, now I am a waiter.' Max follows up boldly in this moment, grounding the moment in plain reality."),
    (2, None, "'Working as a waiter is not easy at all.' Max stands firm decisively on the spot, before the guest can change the subject."),
    (3, None, '\'You are gravely mistaken.\' Max highlights this telling element with the guest: "zabluzhdayetes" means "are mistaken" (from "zabluzhdatsya"), giving the line its exact edge.'),
    (4, None, '\'Hello!\' Max drops this point with candor: the full polite greeting "zdravstvuyte" literally wishes the other person good health, setting a respectful tone right at the start.'),
    (5, None, "'Are you writing this down?' The guest wonders frankly how Max expects that to work in practice."),
    (6, None, '\'I will remember it.\' Max frames one colorful term on cue: "zapomnyu" means "will remember" (from "zapomnit"), giving the line its exact edge.'),
    (7, None, '\'Gratin, please. And rabbit for me.\' The guest delivers that answer at once: dropping in "pozhaluysta" ("please") keeps the request polite on the surface even in a brisk exchange.'),
    (8, None, "'A salad and still water.' The guest follows up quietly in this moment, testing Max's reaction in the middle of the exchange."),
    (9, None, '\'And fresh orange juice.\' The guest highlights one pointed detail with Max: "apelsinovyy" means "orange", and it carries the main weight of what the guest is saying.'),
    (10, None, '\'What is this?\' Max delivers the comment calmly now: notice how Russian needs no word for "am", "is", or "are" in the present — placing the words side by side says it all.'),
    (11, None, "'Beautiful!' Max fires back candidly before the guest, bringing things back to earth after the buildup."),
]
