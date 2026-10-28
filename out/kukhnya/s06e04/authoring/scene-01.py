# Authoring module for kukhnya-s06e04-scene-01.
ID = 'kukhnya-s06e04-scene-01'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 4
SCENE = 1
TITLE = 'Классическая музыка и новость об инспекторе  (Classical Music and News of the Inspector)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'eleonora': 'Элеонора', 'louis': 'Луи'}
SOURCE_NAME = 'Кухня (Kukhnya) S6.04'
SOURCE_FILE = 'sources/kukhnya/s06/e04.ru.srt'
INTRO = 'Eleonora starts the morning by making the hotel staff listen to classical music to boost productivity, right before pastry chef Louis announces that a Michelin inspector is in Moscow!'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'With the entire hotel on high alert for a secret Michelin inspector, every foreign guest immediately becomes a suspect. Until next time!'
CLOSING = ('louis', 'Хорошего дня!')
STORY = [
    ('eleonora', 'Всем спасибо, урок окончен.', 'Thank you everyone, the session is over.', [(1, 'Всем спасибо'), (1, 'окончен')], 'adapted'),
    ('barinov', 'А мы теперь это каждое утро будем переживать?', 'Are we going to go through this every morning now?', [(2, 'каждое утро будем переживать?')], 'adapted'),
    ('eleonora', 'Исследования показали, что день надо начинать с классической музыки.', 'Studies showed that the day should start with classical music.', [(3, 'Исследования показали'), (3, 'день начинать с классической музыки')], 'adapted'),
    ('eleonora', 'Тогда производительность труда увеличивается.', 'Then labor productivity increases.', [(4, 'производительность труда увеличивается')], 'adapted'),
    ('barinov', 'Я просто идею не сразу понял.', 'I simply did not understand the idea right away.', [(7, 'Я просто идею не сразу понял')], 'exact'),
    ('louis', 'А мне захотелось, чтобы меня мама обняла.', 'And it made me want my mom to hug me.', [(8, 'захотелось'), (8, 'чтобы меня мама обняла')], 'adapted'),
    ('eleonora', 'Всем спасибо, работаем.', "Thank you everyone, let's get to work.", [(9, 'Всем спасибо'), (10, 'Работаем')], 'adapted'),
    ('louis', 'Элеонора Андреевна, мне написал отец.', 'Eleonora Andreyevna, my father wrote to me.', [(11, 'Андреевна, мне написал отец')], 'adapted'),
    ('louis', 'У них в ресторане был инспектор.', 'There was an inspector at their restaurant.', [(12, 'У них в ресторане был инспектор')], 'exact'),
    ('louis', 'Если он в Москве, то он и к нам зайдет.', 'If he is in Moscow, then he will stop by our place too.', [(13, 'Если он в Москве, то он и к нам зайдет')], 'exact'),
    ('barinov', 'Это наш шанс получить звезду!', 'This is our chance to get a star!', [(12, 'инспектор')], 'adapted'),
    ('eleonora', 'Будьте готовы сегодня!', 'Be ready today!', [(10, 'Работаем')], 'adapted'),
]
WALK = [
    (0, None, '\'Thank you everyone, the session is over.\' Eleonora gently voices this word of thanks beside Barinov using "spasibo" ("thank you") — the everyday word for "thank you", which grew out of the old blessing "spasi Bog" ("God save you").'),
    (1, None, "'Are we going to go through this every morning now?' Touching on the morning beside Eleonora, Barinov keeps normal statement word order here, turning the line into a question for Eleonora purely through rising pitch."),
    (2, None, "'Studies showed that the day should start with classical music.' Eleonora steps in bluntly around Barinov, without trying to dress up how she really feels."),
    (3, None, '\'Then labor productivity increases.\' Underscoring the productivity in this beat, Eleonora centers the remark on "proizvoditelnost" ("productivity") without any extra fuss.'),
    (4, None, '\'I simply did not understand the idea right away.\' Touching on the idea with Eleonora, Barinov uses the little word "prosto" ("simply, just") to make the point sound effortless.'),
    (5, None, "'And it made me want my mom to hug me.' Louis continues at once in this moment, keeping the focus on what actually matters here."),
    (6, None, '\'Thank you everyone, let\'s get to work.\' Eleonora briskly shares this word of thanks while facing Louis using "spasibo" ("thank you") — the everyday word for "thank you", which grew out of the old blessing "spasi Bog" ("God save you").'),
    (7, None, '\'Eleonora Andreyevna, my father wrote to me.\' Addressing his father right here, Louis leans on "otets" ("father") to give the whole sentence its punch.'),
    (8, None, "'There was an inspector at their restaurant.' Louis chimes in promptly during the talk, keeping the focus on what actually matters here."),
    (9, None, '\'If he is in Moscow, then he will stop by our place too.\' Louis reacts firmly at once and brings in "zaydet" ("will stop by", from "zayti") as the key Russian word here.'),
    (10, None, '\'This is our chance to get a star!\' Underscoring a star in front of Louis, Barinov brings in "zvezdu" ("star", from "zvezda") as the key Russian word here.'),
    (11, None, "'Be ready today!' Eleonora pushes back decisively with a nod, leaving no doubt about where she stands."),
]
