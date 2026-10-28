# Authoring module for kukhnya-s03e13-scene-12.
ID = 'kukhnya-s03e13-scene-12'
SHOW = 'kukhnya'
SEASON = 3
EPISODE = 13
SCENE = 12
TITLE = 'Мастер по кофемашинам  (The Coffee Machine Repairman)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'guest': 'Гость', 'kostya': 'Костя', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S3.13'
SOURCE_FILE = 'sources/kukhnya/s03/e13.ru.srt'
INTRO = 'As Max escorts the tipsy repairman out through the dining room, another technician arrives and asks for Vika to repair the video surveillance system. Listen to the full Russian conversation first, and then we will unpack each line.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "Max got the coffee machine repairman drunk while the real CCTV specialist walked right into Vika's office! See you next time!"
CLOSING = ('guest', 'Пока!')
STORY = [
    ('max', 'Ну что, Костя, как тут дела?', 'So, Kostya, how are things going here?', [(181, 'Ну что, как тут')], 'adapted'),
    ('kostya', 'Тишина, никто тобой не интересовался.', 'All quiet, nobody asked for you.', [(182, 'Тишина'), (182, 'никто не интересовался')], 'adapted'),
    ('guest', 'Девушка, дадите ручку поцеловать?', 'Miss, will you let me kiss your hand?', [(183, 'Дадите ручку')], 'adapted'),
    ('guest', 'А может быть, красивую ножку?', 'Or maybe your pretty little foot?', [(185, 'А ножку')], 'adapted'),
    ('max', 'Так, дружище, пойдём скорее на выход.', "Alright, buddy, let's head for the exit quickly.", [(187, 'Так, дружище')], 'adapted'),
    ('kostya', 'Здравствуйте, вы кого-то ищете?', 'Hello, are you looking for someone?', [(191, 'Здравствуйте')], 'adapted'),
    ('guest', 'Подскажите, где найти Викторию Сергеевну?', 'Could you tell me where to find Viktoria Sergeyevna?', [(189, 'где найти Викторию Сергеевну')], 'adapted'),
    ('guest', 'Я по поводу ремонта систем видеонаблюдения.', 'I am here about repairing the video surveillance system.', [(190, 'Я по поводу ремонта систем видеонаблюдения')], 'adapted'),
    ('kostya', 'Здравствуйте, Виктория вас уже ждёт.', 'Hello, Viktoria is already waiting for you.', [(191, 'Здравствуйте. Виктория вас уже ждет')], 'adapted'),
    ('max', 'Слушай, друг, а ты зачем приходил?', 'Listen, friend, why did you come here anyway?', [(193, 'Слушай, друг, а ты что вообще приходил')], 'adapted'),
    ('guest', 'Так вашу кофемашину ремонтировать!', 'To repair your coffee machine, of course!', [(194, 'Так вашу кофемашину ремонтировать')], 'adapted'),
    ('guest', 'А вы сами её починили, красавцы!', 'And you fixed it yourselves, well done!', [(195, 'сами ее починили'), (196, 'Красавцы')], 'adapted'),
]
WALK = [
    (0, None, "'So, Kostya, how are things going here?' Max questions plainly before Kostya can change the subject."),
    (1, None, '\'All quiet, nobody asked for you.\' Discussing the silence with Max, Kostya puts the weight on "interesovalsya" ("asked about", from "interesovatsya") as the exchange unfolds.'),
    (2, None, "'Miss, will you let me kiss your hand?' Discussing the girlfriend at once, the guest keeps normal statement word order here, turning the line into a question for Kostya purely through rising pitch."),
    (3, None, "'Or maybe your pretty little foot?' The guest presses sharply whether Max really thought this through."),
    (4, None, '\'Alright, buddy, let\'s head for the exit quickly.\' Discussing the buddy before the guest, Max uses "druzhishche" ("buddy") to carry the main weight of the thought.'),
    (5, None, '\'Hello, are you looking for someone?\' Kostya briskly delivers this formal greeting at the start of the beat using "zdravstvuyte" ("hello") — the polite Russian greeting that literally wishes the other person good health.'),
    (6, None, "'Could you tell me where to find Viktoria Sergeyevna?' The guest presses sharply whether Kostya really thought this through."),
    (7, None, '\'I am here about repairing the video surveillance system.\' Underscoring the video surveillance in front of Kostya, the guest centers the thought on "videonablyudeniya" ("video surveillance", from "videonablyudeniye") without wasting a word.'),
    (8, None, '\'Hello, Viktoria is already waiting for you.\' Kostya promptly uses this formal greeting in the exchange using "zdravstvuyte" ("hello") — the polite Russian greeting that literally wishes the other person good health.'),
    (9, None, "'Listen, friend, why did you come here anyway?' Max prompts evenly before the guest can change the subject."),
    (10, None, '\'To repair your coffee machine, of course!\' Focusing on the coffee machine before Max, the guest reaches for the Russian word "kofemashinu" ("coffee machine", built from "kofemashina") right at the center of the line.'),
    (11, None, "'And you fixed it yourselves, well done!' The guest fires back boldly with a shrug, watching Max's face to see how the news lands."),
]
