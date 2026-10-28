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
    (0, None, "'You cannot imagine what trouble I am in.' Barinov steps in openly without holding back, steering the talk right where he wants it."),
    (1, None, '\'Alright, thank you very much, everyone.\' Mikhail stresses one pointed touch at once: "bolshoye" means "big, very much" (from "bolshoy"), giving the line its exact edge.'),
    (2, None, '\'What is happening over there right now?\' Mikhail hands over that point without fuss: putting the question word "chto" right at the front of the line lets Barinov hear the point of the question on the very first beat.'),
    (3, None, "'We have a small problem in the room.' Vika holds firm pointedly with Mikhail, refusing to let the moment slip past."),
    (4, None, '\'The fire alarm went off up there.\' Vika picks one direct piece in earnest: "signalizatsiya" means "alarm", and it carries the main weight of what Vika is saying.'),
    (5, None, "'Our head chef went in there.' Vika aims that reply with ease: spoken Russian trims this down to just 4 words, dropping the extra helper words that English has to spell out."),
    (6, None, "'What did he do in there again?' Mikhail challenges frankly while looking straight at Barinov here."),
    (7, None, '\'Have you completely lost your mind?\' Mikhail spotlights one sharp element on cue: "soshyol" means "gone" (from "soyti"), giving the line its exact edge.'),
    (8, None, '\'I was simply doing your job for you.\' Barinov frames this warning plainly here: the little word "prosto" ("simply, just") works like a shrug in the sentence, making a big claim sound effortless.'),
    (9, None, "'It is very cold here in the room.' Barinov answers boldly to be clear, so Vika knows he is not just making small talk."),
    (10, None, '\'What is going on here at all?\' Mikhail features this telling term on cue: "proiskhodit" means "is going on", and it carries the main weight of what Mikhail is saying.'),
    (11, None, '\'Have you never heard about the holiday?\' Barinov states this answer for Vika: Russian happily doubles the negative here — pairing "never" or "nothing" with "ne" ("not") — which is the only natural way to say it.'),
]
