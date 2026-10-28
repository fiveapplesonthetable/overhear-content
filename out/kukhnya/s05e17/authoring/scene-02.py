# Authoring module for kukhnya-s05e17-scene-02.
ID = 'kukhnya-s05e17-scene-02'
SHOW = 'kukhnya'
SEASON = 5
EPISODE = 17
SCENE = 2
TITLE = 'Другая Гончарова  (The Other Goncharova)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'doctor': 'Врач', 'max': 'Макс', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S5.17'
SOURCE_FILE = 'sources/kukhnya/s05/e17.ru.srt'
INTRO = 'Max bursts into the delivery room without shoe covers expecting to see Vika, only to find another patient named Goncharova. When he finally reaches Vika by phone, she surprises him.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'Baffled that Vika is back at the restaurant instead of the maternity ward, Max heads straight to the hotel. See you next time!'
CLOSING = ('vika', 'До завтра!')
STORY = [
    ('doctor', 'Эй, наденьте бахилы немедленно!', 'Hey, put on shoe covers immediately!', [(14, 'Эй')], 'adapted'),
    ('max', 'Вика, это ты здесь?', 'Vika, is that you here?', [(16, 'Вика')], 'adapted'),
    ('doctor', 'Нет, меня зовут Маша.', 'No, my name is Masha.', [(17, 'Нет, Маша')], 'adapted'),
    ('max', 'Подождите, а где Гончарова?', 'Wait, where is Goncharova?', [(18, 'Где Гончарова')], 'adapted'),
    ('doctor', 'Я тоже Гончарова.', 'I am Goncharova too.', [(18, 'Я Гончарова')], 'adapted'),
    ('max', 'А где другая Гончарова?', 'And where is the other Goncharova?', [(19, 'А другая Гончарова')], 'adapted'),
    ('doctor', 'Ребёнок никак рождаться не хочет.', 'The baby just does not want to be born yet.', [(21, 'никак рождаться не хочет')], 'adapted'),
    ('max', 'Алло, Вика, а ты где?', 'Hello, Vika, where are you?', [(22, 'Алло, Вика, а ты где')], 'adapted'),
    ('vika', 'Я сейчас на работе.', 'I am at work right now.', [(23, 'На работе')], 'adapted'),
    ('max', 'Ты разве ещё не рожаешь?', 'Are you not giving birth yet?', [(24, 'не рожаешь')], 'adapted'),
    ('vika', 'Нет, я очень занята.', 'No, I am very busy.', [(24, 'Я занята')], 'adapted'),
    ('max', 'Я сейчас приеду в отель.', 'I am coming to the hotel right now.', [(23, 'На работе')], 'adapted'),
]
WALK = [
    (0, None, "'Hey, put on shoe covers immediately!' Focusing on the shoe covers to Max, spoken Russian compresses the whole thought into just 4 words, skipping the extra helper words English needs."),
    (1, None, "'Vika, is that you here?' Max inquires firmly about what Vika just brought up."),
    (2, None, '\'No, my name is Masha.\' The doctor continues boldly at once and brings in "zovut" ("call", from "zvat") as the key Russian word here.'),
    (3, None, '\'Wait, where is Goncharova?\' Replying candidly with the doctor, Max puts the question word "gde" right at the start so the doctor hears the focus immediately.'),
    (4, None, "'I am Goncharova too.' The doctor proceeds wryly with a sigh, keeping the focus on what actually matters here."),
    (5, None, '\'And where is the other Goncharova?\' Making clear how different things are on the spot, Max brings in "drugaya" ("different, other", from "drugoy") as the key Russian word here.'),
    (6, None, '\'The baby just does not want to be born yet.\' Pointing to the child with Max, the doctor pairs the negative word with "ne" ("not"), since Russian naturally doubles its negatives for emphasis.'),
    (7, None, "'Hello, Vika, where are you?' Max inquires earnestly if there is more going on behind the scenes."),
    (8, None, '\'I am at work right now.\' Discussing the work during the talk, Vika leans on "rabote" ("work", a form of "rabota") to give the remark its edge.'),
    (9, None, '\'Are you not giving birth yet?\' Speaking warmly in the exchange, Max starts the question with "razve" ("really?") to push back against what he just heard.'),
    (10, None, "'No, I am very busy.' Vika proceeds evenly beside Max, refusing to let the moment slip past."),
    (11, None, '\'I am coming to the hotel right now.\' Mentioning the hotel with Vika, Max chooses "priyedu" ("will come, visit", from the root "priyekhat") so Vika hears the exact meaning.'),
]
