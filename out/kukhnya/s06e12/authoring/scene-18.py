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
    (0, None, '\'Ainura, tell me, will you have seconds of pasta today?\' Barinov probes honestly without hesitation, leaning on "skazhi" ("say") before closing the thought with "dobavku" ("seconds, extra portion").'),
    (1, None, '\'Oh, no, I will not, it turned out very untasty.\' Ainura shows a direct mood in the scene, combining "budu" ("will be") and "ochen" ("very much") so the key meaning lands right away.'),
    (2, None, '\'If you are looking for Misha, he is resting in a room.\' Ainura presents a brisk course in their talk, putting "ishchesh" ("to look for") alongside "otdykhayet" ("to rest, relax") in a tight, everyday turn of phrase.'),
    (3, None, '\'Sveta, listen, you must take the ring off right now.\' Denis adopts a measured line across the room, pairing "seychas" ("now") with "sveta" ("electricity") so the "-sya" ending carries the action.'),
    (4, None, '\'I know, forgive me for ruining the surprise.\' Ainura offers a natural posture in the scene, weaving "znayu" ("know") together with "prosti" ("sorry, forgive me") just the way native speakers do.'),
    (5, None, '\'Let us pretend as if I forgot everything.\' Ainura displays an easygoing tempo as the scene unfolds, putting "davay" ("let\'s") alongside "sdelayem" ("we\'ll do") in a tight, everyday turn of phrase.'),
    (6, None, '\'Sveta, understand, this ring is not for you at all.\' Denis maintains a warm approach right away, linking "sveta" ("electricity"), "poymi" ("understand"), and "koltso" ("ring") in one brisk exchange.'),
    (7, None, '\'Wait, how is it not for me, then who is it for?\' Ainura wonders boldly as the talk turns, linking "podozhdi" ("wait"), "kak" ("how"), and "eto" ("this") in one brisk exchange.'),
    (8, None, '\'Denis, well how much longer can we wait for you?\' Barinov questions earnestly in this moment, putting "skolko" ("how much, so much") alongside "yeshchyo" ("more, still") in a tight, everyday turn of phrase.'),
    (9, None, '\'Where is my ring that I bought for Nastya?\' Barinov questions decisively without hesitation, anchoring the Russian line on "gde" ("where") and "koltso" ("ring") without extra filler.'),
    (10, None, '\'Kostya, wait a minute, a small problem came up here.\' Denis takes a measured tempo in their talk, using "podozhdi" (from "podozhdat", "wait") alongside "minutu" ("a minute") to shape the meaning.'),
    (11, None, '\'It seems it is stuck and will not come off my finger at all!\' Ainura takes an easygoing rhythm across the room, joining "kazhetsya" ("it seems, I think") to "zastryalo" ("get stuck") so every word pulls its weight.'),
]
