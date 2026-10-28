# Authoring module for kukhnya-s06e15-scene-10.
ID = 'kukhnya-s06e15-scene-10'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 15
SCENE = 10
TITLE = 'Знакомство в баре  (Meeting at the Bar)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'guest': 'Гость', 'kostya': 'Костя'}
SOURCE_NAME = 'Кухня (Kukhnya) S6.15'
SOURCE_FILE = 'sources/kukhnya/s06/e15.ru.srt'
INTRO = "At the bar, Kostya tries to pick out a nice woman of his father's generation and introduces a polite lady named Valentina to the table. However, he makes a hilarious misunderstanding by introducing Valentina to his own seat while his father steps away!"
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'Kostya realizes to his horror that his father already walked away and left him on a date with Valentina himself. See you next time!'
CLOSING = ('kostya', 'Пока!')
STORY = [
    ('kostya', 'Папа, а может быть, вон та?', 'Dad, what about that one over there?', [(158, 'Может, вон та')], 'adapted'),
    ('guest', 'Нет, худые женщины часто бывают злые.', 'No, thin women are often mean.', [(159, 'Худые, злые')], 'adapted'),
    ('kostya', 'Хорошо, значит, нам нужна очень добрая.', 'Good, so we need a very kind one.', [(161, 'Хорошо'), (162, 'Значит, нам нужна добрая')], 'adapted'),
    ('kostya', 'Вон та женщина, по-моему, очень добрая.', 'That woman over there, in my opinion, is very kind.', [(163, 'по-моему, очень добрая')], 'adapted'),
    ('guest', 'Слушай, а она мне не старовата?', 'Listen, is she not a bit too old for me?', [(164, 'А она не старовата')], 'adapted'),
    ('kostya', 'Ну, в принципе, это отличный вариант.', 'Well, in principle, this is a great option.', [(166, 'это вариант')], 'adapted'),
    ('kostya', 'Познакомьтесь, пожалуйста, вы ему очень понравились.', 'Meet him, please, he liked you very much.', [(168, 'Познакомьтесь'), (169, 'Вы ему очень понравились')], 'adapted'),
    ('guest', 'Меня зовут Валентина, мне очень приятно.', 'My name is Valentina, very pleased to meet you.', [(170, 'Валентина, очень приятно')], 'adapted'),
    ('kostya', 'Я помогаю вам в последний раз.', 'I am helping you for the last time.', [(174, 'в первый и последний раз')], 'adapted'),
    ('kostya', 'Ладно, мне пора, а вы отдыхайте.', 'Alright, I have to go, and you two relax.', [(175, 'пора'), (176, 'Отдыхайте')], 'adapted'),
    ('guest', 'Константин, скажите, а чем вы занимаетесь?', 'Konstantin, tell me, what do you do for a living?', [(178, 'Константин, а чем вы занимаетесь')], 'adapted'),
    ('kostya', 'Кажется, я сегодня занимаюсь всякой ерундой.', 'It seems I am doing all kinds of nonsense today.', [(179, 'всякой')], 'adapted'),
]
WALK = [
    (0, None, '\'Dad, what about that one over there?\' Highlighting the dad right here, Kostya chooses "papa" ("Dad") so the guest gets the point right away.'),
    (1, None, '\'No, thin women are often mean.\' Discussing the woman in front of Kostya, the guest lands on "zhenshchiny" ("woman", built on "zhenshchina") to keep the statement grounded.'),
    (2, None, "'Good, so we need a very kind one.' Kostya cuts in right away watching the guest, shifting the mood of the conversation in a single beat."),
    (3, None, '\'That woman over there, in my opinion, is very kind.\' Pointing to the woman on the spot, Kostya lands on "zhenshchina" ("woman") as the key everyday word here.'),
    (4, None, "'Listen, is she not a bit too old for me?' Weighing in frankly with Kostya, the guest keeps normal statement word order here, turning the line into a question for Kostya purely through rising pitch."),
    (5, None, "'Well, in principle, this is a great option.' Kostya jumps in firmly in this moment, without trying to dress up how he really feels."),
    (6, None, '\'Meet him, please, he liked you very much.\' Kostya chimes in earnestly to the guest and lands on "poznakomtes" ("get acquainted", built on "poznakomitsya") to keep the statement grounded.'),
    (7, None, '\'My name is Valentina, very pleased to meet you.\' The guest speaks pointedly with Kostya and leans on "priyatno" ("pleasant") to give the whole sentence its punch.'),
    (8, None, "'I am helping you for the last time.' Kostya weighs in evenly in this moment, grounding the moment in plain reality."),
    (9, None, '\'Alright, I have to go, and you two relax.\' Kostya replies candidly in the exchange and brings in "otdykhayte" ("rest", from "otdykhat") as the key Russian word here.'),
    (10, None, '\'Konstantin, tell me, what do you do for a living?\' Turning boldly right here, the "-sya" ending on "zanimayetes" ("are busy with") marks an action that unfolds mutually or turns back on the speaker.'),
    (11, None, "'It seems I am doing all kinds of nonsense today.' Kostya steps in quietly on the spot, refusing to let the moment slip past."),
]
