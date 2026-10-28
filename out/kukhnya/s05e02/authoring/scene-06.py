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
    (0, None, '\'You cannot imagine what trouble I am in.\' Barinov shows an easygoing stance as the scene unfolds, joining "predstavlyayesh" ("can you imagine") to "kak" ("how") so every word pulls its weight.'),
    (1, None, '\'Alright, thank you very much, everyone.\' Mikhail projects a playful course straight away, using "bolshoye" (from "bolshoy", "big, very much") alongside "spasibo" ("thank you") to shape the meaning.'),
    (2, None, '\'What is happening over there right now?\' Mikhail probes frankly during the talk, pairing "seychas" ("now") with "tam" ("there") so the "-sya" ending carries the action.'),
    (3, None, '\'We have a small problem in the room.\' Vika picks a thoughtful stance in the conversation, weaving "nomere" ("in the hotel room") together with "nebolshaya" ("small") just the way native speakers do.'),
    (4, None, '\'The fire alarm went off up there.\' Vika shows a resolute bearing with Barinov, leaning on "tam" ("there") before closing the thought with "srabotala" ("went off, triggered").'),
    (5, None, '\'Our head chef went in there.\' Vika shares a lively tone with Mikhail, weaving "tuda" ("there") together with "prishyol" ("came, have come") just the way native speakers do.'),
    (6, None, '\'What did he do in there again?\' Mikhail queries sharply on the spot, putting "tam" ("there") alongside "opyat" ("again") in a tight, everyday turn of phrase.'),
    (7, None, '\'Have you completely lost your mind?\' Mikhail presses dryly as the talk turns, anchoring the Russian line on "sovsem" ("at all") and "uma" ("mind") without extra filler.'),
    (8, None, '\'I was simply doing your job for you.\' Barinov offers a sharp posture in the room, building the phrase around "prosto" ("just") and "delal" ("were doing") for a crisp, natural delivery.'),
    (9, None, '\'It is very cold here in the room.\' Barinov sets a sharp stance in this beat, linking "zdes" ("here") directly with "nomere" ("in the hotel room"), since Russian drops "is" and "are" in the present.'),
    (10, None, '\'What is going on here at all?\' Mikhail queries firmly with Barinov now, combining "zdes" ("here") and "voobshche" ("at all") so the key meaning lands right away.'),
    (11, None, '\'Have you never heard about the holiday?\' Barinov queries wryly across the room, combining "nikogda" ("never") and "slyshali" ("did you hear") so the key meaning lands right away.'),
]
