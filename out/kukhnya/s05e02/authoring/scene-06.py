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
    (0, None, '\'You cannot imagine what trouble I am in.\' Barinov reminds Mikhail that Mikhail cannot imagine what trouble he is before the moment passes. Using the informal "you" shows how direct and unfiltered their kitchen relationship is.'),
    (1, None, "'Alright, thank you very much, everyone.' Over the room and the hotel, Mikhail answers Barinov without a second thought."),
    (2, None, '\'What is happening over there right now?\' By wondering what happening over there right now is, Mikhail presses Barinov for a straight answer. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (3, None, '\'We have a small problem in the room.\' Vika mentions that they have a small problem in the room so Barinov sees what is at stake. In Russian you say "by me" or "with us" rather than "I have", so the situation sits right with the person.'),
    (4, None, "'The fire alarm went off up there.' Claiming that the fire alarm went off up there sounds confident, even if Barinov has doubts."),
    (5, None, "'Our head chef went in there.' Pointing out that their head went in there gives Barinov a sobering reality check."),
    (6, None, '\'What did he do in there again?\' By asking what he do in there again, Mikhail presses Barinov for a straight answer. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (7, None, "'Have you completely lost your mind?' With the kitchen and hotel hanging in the air, Mikhail puts Barinov on the spot."),
    (8, None, '\'I was simply doing your job for you.\' Noting that he was simply doing Mikhail\'s job for Mikhail keeps Barinov\'s side of the story simple and clear. Using the informal "you" shows how direct and unfiltered their kitchen relationship is.'),
    (9, None, "'It is very cold here in the room.' Even though it is very cold here in the room, Barinov keeps a steady face in front of Mikhail."),
    (10, None, "'What is going on here at all?' Here wondering what going on here at all is shows Mikhail looking for the real truth."),
    (11, None, '\'Have you never heard about the holiday?\' Asking whether Mikhail never heard about the holiday cuts straight through the tension between Barinov and Mikhail. Russian stacks "never" or "nothing" together with "not", doubling the refusal for extra weight.'),
]
