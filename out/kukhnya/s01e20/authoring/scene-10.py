# Authoring module for kukhnya-s01e20-scene-10.
ID = 'kukhnya-s01e20-scene-10'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 20
SCENE = 10
TITLE = 'Дима ждёт  (Dima is Waiting)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'hostess': 'Хостес'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.20'
SOURCE_FILE = 'sources/kukhnya/s01/e20.ru.dual.srt'
INTRO = "Back at the restaurant, Barinov has let the owner's calls ring all morning, and now he walks in. Here it is in Russian."
OPENER = 'Here are the lines up close.'
TRANSITION = 'And the whole exchange again.'
OUTRO = 'So Barinov goes to face the owner. Most Russian names have a friendly short form, and Dima is the one for Dmitry. See you next time!'
CLOSING = ('hostess', 'Удачи!')
STORY = [
    ('hostess', 'Здравствуйте.', 'Hello.', [(152, 'Здравствуйте.')], ''),
    ('barinov', 'Доброе утро.', 'Good morning.', [], ''),
    ('hostess', 'Дима тебя ждёт.', 'Dima is waiting for you.', [(153, 'Дима тебя ждет.')], ''),
    ('barinov', 'Дима? Он здесь?', 'Dima? He is here?', [], ''),
    ('hostess', 'Да, он за своим столом.', 'Yes, he is at his table.', [], ''),
    ('barinov', 'Что он хочет?', 'What does he want?', [], ''),
    ('hostess', 'Я не знаю.', 'I do not know.', [], ''),
    ('barinov', 'Хорошо, я иду.', 'Okay, I am coming.', [], ''),
]
WALK = [
    (0, None, "'Hello.' This is the long polite hello, zdravstvuyte, and in speech the first v is silent: zdrastvuyte."),
    (1, None, "'Good morning.' Russian says dobroe utro. The word utro, 'morning', is neuter, so dobroe, 'good', ends in -oe."),
    (2, None, "'Dima's waiting for you.' The name Dima is the friendly short form of Dmitry, and here it means the owner. The word tebya, 'you', comes before zhdyot, 'is waiting'."),
    (3, None, "'Dima? He's here?' Russian drops 'is' here: on zdes is literally 'he here'."),
    (4, None, "'Yes, he's at his table.' Russian says za stolom, literally 'behind the table', for sitting at one."),
    (5, None, "'What does he want?' The word khochet, 'he wants', comes from khotet, 'to want', which shifts its sounds: khochu is 'I want'."),
    (6, None, "'I don't know.' Russian puts ne, 'not', straight in front of the action: ya ne znayu."),
    (7, None, "'Okay, I'm coming.' Russian says ya idu, literally 'I am going', where English says 'I'm coming'."),
]
