# Authoring module for kukhnya-s06e11-scene-01.
ID = 'kukhnya-s06e11-scene-01'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 11
SCENE = 1
TITLE = 'Утро после праздника  (The Morning After the Party)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'denis': 'Денис', 'fedya': 'Федя', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S6.11'
SOURCE_FILE = 'sources/kukhnya/s06/e11.ru.srt'
INTRO = "Welcome to Episode Eleven of Kukhnya Season Six. The morning after Senya's wild birthday party, Fedya teases Denis about his tequila-fueled kiss with Sveta, and seconds later Sveta announces that she just broke up with her boyfriend Misha because of Denis."
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "Denis is horrified to learn Sveta dumped her boyfriend over a staged kiss, while in the dining room Barinov spots his arch-rival at Eleonora's table. Until next time!"
CLOSING = ('denis', 'Хорошего дня!')
STORY = [
    ('fedya', 'Там сейчас свежее мясо должны привезти, проконтролируй.', 'They are supposed to deliver fresh meat there right now, go check it.', [(3, 'Там все мясо должны привезти')], 'adapted'),
    ('denis', 'Сеня, вчера вечеринка у тебя получилась отличная.', 'Senya, your party yesterday turned out great.', [(4, 'вчера получилась')], 'adapted'),
    ('fedya', 'Денис, расскажи, как у тебя со Светой?', 'Denis, tell me, how are things with you and Sveta?', [(6, 'как у тебя со Светкой')], 'adapted'),
    ('denis', 'Никак, это было просто чтобы Катя поревновала.', 'Nothing at all, that was just to make Katya jealous.', [(7, 'Никак'), (10, 'Это просто, чтобы Катя')], 'adapted'),
    ('fedya', 'Видел я вчера, как у вас после текилы было.', 'I saw yesterday how it was with you two after tequila.', [(8, 'Видел я, как у вас после текилы было никак')], 'adapted'),
    ('denis', 'Да правда ничего у нас с ней нет.', 'Honestly there is nothing going on between her and me.', [(11, 'Ничего у нас нет')], 'adapted'),
    ('vika', 'Всё, Миша, пока, не звони мне больше.', 'That is it, Misha, bye, do not call me anymore.', [(11, 'Все, Миша, пока'), (12, 'Не звони мне больше')], 'adapted'),
    ('denis', 'Привет, Света, с кем ты сейчас говорила?', 'Hi, Sveta, who were you talking to just now?', [(13, 'Привет'), (14, 'С кем болтала')], 'adapted'),
    ('vika', 'Со своим парнем, точнее его уже нет.', 'With my boyfriend, or rather he is gone now.', [(15, 'С парнем'), (17, 'Уже нет')], 'adapted'),
    ('vika', 'Вчера я пришла домой и не смогла врать.', 'Yesterday I came home and could not lie to him.', [(18, 'Вчера я пришла домой, поняла, что не могу ему врать')], 'adapted'),
    ('vika', 'Я рассказала о нашем поцелуе, и мы расстались.', 'I told him about our kiss, and we broke up.', [(19, 'Рассказала о нашем поцелуи, и мы расстались')], 'adapted'),
    ('vika', 'Но я думаю, это даже к лучшему.', 'But I think that is even for the best.', [(20, 'Ну, это даже к лучшему')], 'adapted'),
    ('fedya', 'Слушай, а Света знает, что у вас ничего нет?', 'Listen, does Sveta know that there is nothing between you two?', [(22, 'Светка-то знает, что у вас ничего нет')], 'adapted'),
]
WALK = [
    (0, None, '\'They are supposed to deliver fresh meat there right now, go check it.\' Fedya takes a candid course for Denis, leaning on "tam" ("there") before closing the thought with "seychas" ("now").'),
    (1, None, '\'Senya, your party yesterday turned out great.\' Denis displays a warm tone right away, combining "u tebya" (literally "by you") with "vchera" ("yesterday") rather than a separate word for "have".'),
    (2, None, '\'Denis, tell me, how are things with you and Sveta?\' Fedya wonders plainly across the room, linking "rasskazhi" ("tell"), "kak" ("how"), and "denis" ("Denis") in one brisk exchange.'),
    (3, None, '\'Nothing at all, that was just to make Katya jealous.\' Denis maintains a candid manner as they talk, combining "nikak" ("in no way") and "bylo" ("was") so the key meaning lands right away.'),
    (4, None, '\'I saw yesterday how it was with you two after tequila.\' Fedya conveys a frank angle on the spot, linking "videl" ("saw, have seen"), "vchera" ("yesterday"), and "kak" ("how") in one brisk exchange.'),
    (5, None, '\'Honestly there is nothing going on between her and me.\' Denis establishes a grounded note toward Vika, anchoring the Russian line on "pravda" ("honestly") and "da" ("yes") without extra filler.'),
    (6, None, '\'That is it, Misha, bye, do not call me anymore.\' Vika takes a measured line beside Denis, anchoring the Russian line on "poka" ("bye") and "zvoni" ("call") without extra filler.'),
    (7, None, '\'Hi, Sveta, who were you talking to just now?\' Denis quizzes bluntly to make the point, linking "sveta" ("electricity"), "seychas" ("now"), and "govorila" ("said") in one brisk exchange.'),
    (8, None, '\'With my boyfriend, or rather he is gone now.\' Vika sustains a natural angle in their talk, joining "parnem" ("boyfriend, guy") to "tochneye" ("definitely") so every word pulls its weight.'),
    (9, None, '\'Yesterday I came home and could not lie to him.\' Vika maintains a measured position at this moment, building the phrase around "vchera" ("yesterday") and "prishla" ("came") for a crisp, natural delivery.'),
    (10, None, '\'I told him about our kiss, and we broke up.\' Vika projects a wry manner without hesitation, putting "rasskazala" ("told") alongside "potseluye" ("about the kiss") in a tight, everyday turn of phrase.'),
    (11, None, '\'But I think that is even for the best.\' Vika displays a grounded bearing in the conversation, putting "dumayu" ("I think") alongside "luchshemu" ("the best") in a tight, everyday turn of phrase.'),
    (12, None, '\'Listen, does Sveta know that there is nothing between you two?\' Fedya asks directly as the talk turns, weaving "slushay" ("listen") together with "sveta" ("electricity") just the way native speakers do.'),
]
