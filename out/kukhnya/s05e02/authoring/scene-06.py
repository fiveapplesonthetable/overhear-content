# Authoring module for kukhnya-s05e02-scene-06.
ID = 'kukhnya-s05e02-scene-06'
SHOW = 'kukhnya'
SEASON = 5
EPISODE = 2
SCENE = 6
TITLE = 'Пожарная тревога в номере 205  (Fire Alarm in Room 205)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'mikhail': 'Михаил', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S5.02'
SOURCE_FILE = 'sources/kukhnya/s05/e02.ru.srt'
INTRO = "Right at the end of Eleonora's speech, the hotel fire alarm goes off in room 205, where Chef Barinov has lit a bonfire to 'warm up' the freezing guests and get even with Mikhail. Listen to the chaos."
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "And that finishes the fire-alarm prank in room 205. Notice how Barinov repeats Mikhail's exact words—'I was simply doing your job for you'. See you next time!"
CLOSING = ('mikhail', 'Пока!')
STORY = [
    ('barinov', 'Ты не представляешь, как я попал.', 'You cannot imagine what trouble I am in.', [(57, 'не представляешь, как я попал')], 'verbatim'),
    ('mikhail', 'Ладно, всем большое спасибо.', 'Alright, thank you very much, everyone.', [(58, 'Ладно'), (59, 'Всем спасибо')], 'adapted'),
    ('mikhail', 'Что там сейчас происходит?', 'What is happening over there right now?', [(60, 'Что происходит')], 'adapted'),
    ('vika', 'В номере у нас небольшая проблемка.', 'We have a small problem in the room.', [(61, 'проблемка')], 'adapted'),
    ('vika', 'Там сработала пожарная сигнализация.', 'The fire alarm went off up there.', [(61, 'сработала пожарная сигнализация')], 'verbatim'),
    ('vika', 'Туда наш шеф пришёл.', 'Our head chef went in there.', [(61, 'там шеф пришел')], 'adapted'),
    ('mikhail', 'Что он там опять сделал?', 'What did he do in there again?', [(62, 'Что?')], 'adapted'),
    ('mikhail', 'Ты что, совсем с ума сошёл?', 'Have you completely lost your mind?', [(64, 'что? Совсем?')], 'adapted'),
    ('barinov', 'Я просто делал за тебя твою работу.', 'I was simply doing your job for you.', [(64, 'Я просто делал за тебя твою работу')], 'verbatim'),
    ('barinov', 'Здесь в номере очень холодно.', 'It is very cold here in the room.', [(65, 'Здесь очень холодно')], 'adapted'),
    ('mikhail', 'Что здесь вообще происходит?', 'What is going on here at all?', [(66, 'Что происходит?')], 'adapted'),
    ('barinov', 'Вы никогда не слышали о празднике?', 'Have you never heard about the holiday?', [(67, 'Вы никогда не слышали о'), (67, 'празднике')], 'adapted'),
]
WALK = [
    (0, None, "'You cannot imagine what trouble I am in.' Barinov fires back openly facing Mikhail, testing Mikhail's reaction in the middle of the exchange."),
    (1, None, '\'Alright, thank you very much, everyone.\' Mikhail smoothly directs this word of thanks without hesitation using "spasibo" ("thank you") — the everyday word for "thank you", which grew out of the old blessing "spasi Bog" ("God save you").'),
    (2, None, '\'What is happening over there right now?\' Jumping in firmly before Vika, Mikhail puts the question word "chto" right at the start so Vika hears the focus immediately.'),
    (3, None, "'We have a small problem in the room.' Vika pushes back pointedly with a smile, testing Mikhail's reaction in the middle of the exchange."),
    (4, None, '\'The fire alarm went off up there.\' Emphasizing the fire alarm around Mikhail, Vika reaches for the Russian word "signalizatsiya" ("alarm") right at the heart of the line.'),
    (5, None, "'Our head chef went in there.' Holding firm earnestly during the talk, spoken Russian compresses the whole thought into just 4 words, skipping the extra helper words English needs."),
    (6, None, "'What did he do in there again?' Mikhail challenges frankly while looking straight at Vika here."),
    (7, None, '\'Have you completely lost your mind?\' Addressing the mind in front of Barinov, Mikhail centers the thought on "soshyol" ("gone", from "soyti") without wasting a word.'),
    (8, None, '\'I was simply doing your job for you.\' Returning to the job on the spot, Barinov uses the little word "prosto" ("simply, just") to make the point sound effortless.'),
    (9, None, "'It is very cold here in the room.' Barinov cuts in boldly without a pause, bringing things back to earth after the buildup."),
    (10, None, '\'What is going on here at all?\' Mikhail continues warmly beside Barinov and centers the remark on "proiskhodit" ("is going on") without any extra fuss.'),
    (11, None, '\'Have you never heard about the holiday?\' Dwelling on the festival in front of Mikhail, Barinov pairs the negative word with "ne" ("not"), since Russian naturally doubles its negatives for emphasis.'),
]
