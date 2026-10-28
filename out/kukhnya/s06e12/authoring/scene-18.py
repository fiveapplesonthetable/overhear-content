# Authoring module for kukhnya-s06e12-scene-18.
ID = 'kukhnya-s06e12-scene-18'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 12
SCENE = 18
TITLE = 'Горькая правда для Светы  (The Bitter Truth for Sveta)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'ainura': 'Айнура', 'barinov': 'Шеф', 'denis': 'Денис'}
SOURCE_NAME = 'Кухня (Kukhnya) S6.12'
SOURCE_FILE = 'sources/kukhnya/s06/e12.ru.srt'
INTRO = 'In the kitchen, Ainura bluntly tells Fedya that his pasta was terrible and told Barinov that Mikhail is resting in room 205. In the locker room, Denis gently tells Sveta that she has to take the ring off because it was bought for Nastya, not for her.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "With Kostya's anniversary ring stuck fast on Sveta's finger, the three of them have no choice but to walk out to Nastya's table together. See you next time!"
CLOSING = ('denis', 'До свидания!')
STORY = [
    ('barinov', 'Айнура, скажи, ты добавку макарон сегодня будешь?', 'Ainura, tell me, will you have seconds of pasta today?', [(294, 'Айнур'), (295, 'Добавку будешь')], 'adapted'),
    ('ainura', 'Ой, нет, не буду, очень уж невкусно получилось.', 'Oh, no, I will not, it turned out very untasty.', [(295, 'Ой, нет, не буду'), (296, 'Невкусно получилось')], 'adapted'),
    ('ainura', 'Если ты ищешь Мишу, то он отдыхает в номере.', 'If you are looking for Misha, he is resting in a room.', [(298, 'если ты про Мишу, то он, видимо, отдыхает в')], 'adapted'),
    ('denis', 'Света, послушай, ты должна сейчас же снять кольцо.', 'Sveta, listen, you must take the ring off right now.', [(299, 'его снять')], 'adapted'),
    ('ainura', 'Я знаю, прости меня, что я испортила сюрприз.', 'I know, forgive me for ruining the surprise.', [(300, 'Я знаю, прости'), (301, 'Испортила сюрприз')], 'adapted'),
    ('ainura', 'А давай сделаем вид, как будто я всё забыла.', 'Let us pretend as if I forgot everything.', [(302, 'А давай как будто... Как будто все забыла')], 'adapted'),
    ('denis', 'Света, пойми, это кольцо вообще не для тебя.', 'Sveta, understand, this ring is not for you at all.', [(303, 'Света, оно не для тебя')], 'adapted'),
    ('ainura', 'Подожди, как это не для меня, а для кого?', 'Wait, how is it not for me, then who is it for?', [(304, 'А для кого')], 'adapted'),
    ('barinov', 'Денис, ну сколько нам ещё тебя ждать можно?', 'Denis, well how much longer can we wait for you?', [(305, 'ну сколько ждать можно')], 'adapted'),
    ('barinov', 'Где моё кольцо, которое я купил для Насти?', 'Where is my ring that I bought for Nastya?', [(306, 'Где кольцо, Настя')], 'adapted'),
    ('denis', 'Костя, подожди минуту, тут возникла небольшая проблема.', 'Kostya, wait a minute, a small problem came up here.', [(306, 'Где кольцо')], 'adapted'),
    ('ainura', 'Кажется, оно застряло и совсем не снимается с пальца!', 'It seems it is stuck and will not come off my finger at all!', [(303, 'оно не для тебя')], 'adapted'),
]
WALK = [
    (0, None, "'Ainura, tell me, will you have seconds of pasta today?' Barinov inquires eagerly to see how Ainura will answer on the spot."),
    (1, None, '\'Oh, no, I will not, it turned out very untasty.\' Ainura fires back calmly with Barinov and lands on "poluchilos" ("worked out", built on "poluchitsya") to keep the statement grounded.'),
    (2, None, "'If you are looking for Misha, he is resting in a room.' Ainura follows up sharply watching Denis, making her position completely clear."),
    (3, None, "'Sveta, listen, you must take the ring off right now.' Denis answers plainly with Ainura, making his position completely clear."),
    (4, None, '\'I know, forgive me for ruining the surprise.\' Addressing the surprise in front of Denis, Ainura chooses "syurpriz" ("surprise") so Denis gets the point right away.'),
    (5, None, '\'Let us pretend as if I forgot everything.\' Turning to the view right here, Ainura starts with "davay" ("come on, let\'s") to invite Denis right into the action.'),
    (6, None, "'Sveta, understand, this ring is not for you at all.' Denis answers warmly around Ainura, keeping the focus on what actually matters here."),
    (7, None, '\'Wait, how is it not for me, then who is it for?\' Ainura follows up directly around Barinov and leans on "podozhdi" ("wait", a form of "podozhdat") to give the remark its edge.'),
    (8, None, '\'Denis, well how much longer can we wait for you?\' Speaking dryly in front of Denis, Barinov leans on "mozhno" ("it is possible, one may"), which carries the whole predicate in Russian without needing "it is".'),
    (9, None, "'Where is my ring that I bought for Nastya?' Barinov challenges briskly to see how Denis will answer on the spot."),
    (10, None, '\'Kostya, wait a minute, a small problem came up here.\' Pointing to a minute right here, Denis puts the weight on "nebolshaya" ("small", from "nebolshoy") as the exchange unfolds.'),
    (11, None, '\'It seems it is stuck and will not come off my finger at all!\' Dwelling on the fingers to Denis, Ainura adds "sovsem" ("completely, at all") so the statement leaves zero room for doubt.'),
]
