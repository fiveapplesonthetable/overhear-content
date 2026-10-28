# Authoring module for kukhnya-s05e11-scene-04.
ID = 'kukhnya-s05e11-scene-04'
SHOW = 'kukhnya'
SEASON = 5
EPISODE = 11
SCENE = 4
TITLE = 'Пересоленный гратен  (The Oversalted Gratin)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'denis': 'Денис', 'lyova': 'Лёва'}
SOURCE_NAME = 'Кухня (Kukhnya) S5.11'
SOURCE_FILE = 'sources/kukhnya/s05/e11.ru.srt'
INTRO = 'In the kitchen, Artyom plates his gratin for Eleonora, but when Chef Barinov and Lyova taste it, the dish is terribly oversalted. Refusing to admit to Eleonora that he hired an incompetent cook, Viktor tells Artyom he has potential and secretly remakes the meal himself.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'That brings the kitchen tasting to a close. Notice how Chef Barinov softens his criticism and decides to cook the dishes himself to save face. See you next time!'
CLOSING = ('barinov', 'Хорошего дня!')
STORY = [
    ('barinov', 'Фартук можно взять там.', 'You can take an apron over there.', [(65, 'Фартук можно взять там')], 'adapted'),
    ('denis', 'Гратен! Сейчас принесу перепёлку.', 'The gratin! Right now I will bring the quail.', [(66, 'Гратен, сейчас принесу перепелку')], 'adapted'),
    ('barinov', 'Ну как?', 'Well, how is it?', [(67, 'Ну как')], 'adapted'),
    ('lyova', 'Отлично справился!', 'He handled it great!', [(68, 'отлично справился')], 'adapted'),
    ('barinov', 'Можно подумать, у тебя с первого раза получилось.', 'One might think you got it right the first time.', [(69, 'Можно подумать, у тебя'), (69, 'первый раз получилось')], 'adapted'),
    ('denis', 'Ну как гратен?', 'Well, how is the gratin?', [(70, 'Ну как, гратен')], 'adapted'),
    ('barinov', 'Для первого раза неплохо.', 'Not bad for the first time.', [(71, 'Для первого раза неплохо')], 'adapted'),
    ('barinov', 'Видно, что есть потенциал.', 'It is clear that there is potential.', [(72, 'Видно, что есть потенциал')], 'adapted'),
    ('barinov', 'Но чтобы не было вопросов, лучше я приготовлю сам.', 'But so there are no questions, I had better cook it myself.', [(73, 'чтобы не было вопросов, лучше я приготовлю сам')], 'adapted'),
    ('barinov', 'А ты отдохни пока.', 'And you rest for now.', [(74, 'а ты отдохни пока')], 'adapted'),
    ('denis', 'Спасибо, Виктор Петрович.', 'Thank you, Viktor Petrovich.', [], ''),
    ('lyova', 'Зачем вы его защищаете, шеф?', 'Why are you defending him, chef?', [(67, 'Ну как')], 'adapted'),
]
WALK = [
    (0, None, '\'You can take an apron over there.\' Mentioning an apron to Denis, Barinov reaches for the Russian word "fartuk" ("apron") right at the heart of the line.'),
    (1, None, "'The gratin! Right now I will bring the quail.' Focusing on the quail at once, spoken Russian compresses the whole thought into just 4 words, skipping the extra helper words English needs."),
    (2, None, "'Well, how is it?' Barinov inquires sharply whether Lyova really thought this through."),
    (3, None, '\'He handled it great!\' Lyova steps in candidly during the talk and brings in "spravilsya" ("to manage, to cope", from "spravitsya") as the key Russian word here.'),
    (4, None, '\'One might think you got it right the first time.\' Cutting in evenly beside Lyova, Barinov uses "u tebya" (literally "by you") where English says "you have" or "your".'),
    (5, None, "'Well, how is the gratin?' Denis wonders eagerly whether Barinov really thought this through."),
    (6, None, '\'Not bad for the first time.\' Barinov proceeds briskly around Denis and brings in "pervogo" ("first", from "pervyy") as the key Russian word here.'),
    (7, None, "'It is clear that there is potential.' Returning to the potential beside Denis, spoken Russian compresses the whole thought into just 4 words, skipping the extra helper words English needs."),
    (8, None, "'But so there are no questions, I had better cook it myself.' Barinov speaks lightly around Denis, steering the talk right where he wants it."),
    (9, None, '\'And you rest for now.\' Barinov briskly offers this casual farewell toward Denis using "poka" ("bye") — the quick everyday word for "bye for now" between people on close terms.'),
    (10, None, '\'Thank you, Viktor Petrovich.\' Denis promptly uses this word of thanks to Barinov using "spasibo" ("thank you") — the everyday word for "thank you", which grew out of the old blessing "spasi Bog" ("God save you").'),
    (11, None, "'Why are you defending him, chef?' Lyova inquires straight out while looking straight at Barinov here."),
]
