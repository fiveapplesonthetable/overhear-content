# Authoring module for kukhnya-s06e06-scene-01.
ID = 'kukhnya-s06e06-scene-01'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 6
SCENE = 1
TITLE = 'Приглашение в Париж  (Invitation to Paris)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'denis': 'Денис', 'guest': 'Гость', 'katya': 'Катя'}
SOURCE_NAME = 'Кухня (Kukhnya) S6.06'
SOURCE_FILE = 'sources/kukhnya/s06/e06.ru.srt'
INTRO = 'Welcome to episode six of Kukhnya season six. Over a romantic dinner, Olivier invites Katya to fly to Paris with him, while Denis and Nikita watch jealously from across the dining room.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "Denis's desperate attempt to ruin the date with a fire alarm and spilled wine only brings Katya and Olivier closer together. Until next time!"
CLOSING = ('katya', 'Хорошего дня!')
STORY = [
    ('guest', 'Тебе ещё не надоела серая Москва?', 'Are you not tired of gray Moscow yet?', [(1, 'тебе не надоело эта серая Москва')], 'adapted'),
    ('guest', 'Может, поедешь со мной в Париж?', 'Maybe you will go to Paris with me?', [(2, 'Может, со мной в Париж')], 'adapted'),
    ('guest', 'Там мы найдём тебе хорошую работу.', 'There we will find you a good job.', [(3, 'Там, Париж. Найдем тебе работу')], 'adapted'),
    ('guest', 'Или тебя здесь что-то держит?', 'Or is something keeping you here?', [(4, 'Или тебя здесь что-то держат')], 'adapted'),
    ('katya', 'Нет, меня здесь ничего не держит.', 'No, nothing is keeping me here.', [(5, 'Ну, нет')], 'adapted'),
    ('katya', 'А ты случайно не слишком торопишься?', 'Are you not rushing things a bit too much?', [(6, 'А ты не слишком торопишься')], 'adapted'),
    ('guest', 'Я целую тебя впервые за пять лет.', 'I am kissing you for the first time in five years.', [(7, 'Я целую тебя впервые за пять лет знакомства')], 'adapted'),
    ('guest', 'По-моему, я уже жутко опаздываю.', 'In my opinion, I am already terribly late.', [(8, 'По-моему, я жутко опаздываю')], 'adapted'),
    ('katya', 'Слышишь, это сработала пожарная сигнализация.', 'Listen, the fire alarm has gone off.', [(9, 'Это пожарная сигнализация')], 'adapted'),
    ('katya', 'Нам сейчас срочно надо идти на улицу.', 'We urgently need to go outside right now.', [(10, 'Надо идти')], 'adapted'),
    ('denis', 'Прости, пожалуйста, я совсем случайно.', 'Forgive me, please, it was completely accidental.', [(12, 'Прости, пожалуйста')], 'adapted'),
    ('guest', 'Ничего страшного, это просто красное вино.', 'No big deal, it is just red wine.', [(12, 'Ничего, ничего, ничего')], 'adapted'),
]
WALK = [
    (0, None, '\'Are you not tired of gray Moscow yet?\' Describing how gray things are in front of Katya, the guest centers the thought on "seraya" ("gray", from "seryy") without wasting a word.'),
    (1, None, "'Maybe you will go to Paris with me?' Looking over candidly during the talk, the guest keeps normal statement word order here, turning the line into a question for Katya purely through rising pitch."),
    (2, None, "'There we will find you a good job.' The guest jumps in plainly with a smile, to clear the air between them once and for all."),
    (3, None, '\'Or is something keeping you here?\' The guest weighs in boldly right here and centers the thought on "derzhit" ("keeps", from "derzhat") without wasting a word.'),
    (4, None, '\'No, nothing is keeping me here.\' Jumping in naturally at once, Katya pairs the negative word with "ne" ("not"), since Russian naturally doubles its negatives for emphasis.'),
    (5, None, "'Are you not rushing things a bit too much?' Katya asks firmly what the guest is actually getting at here."),
    (6, None, '\'I am kissing you for the first time in five years.\' The guest pushes back briskly beside Katya and centers the remark on "vpervyye" ("for the first time") without any extra fuss.'),
    (7, None, '\'In my opinion, I am already terribly late.\' The guest continues frankly right here and puts the weight on "opazdyvayu" ("am running late", from "opazdyvat") as the exchange unfolds.'),
    (8, None, "'Listen, the fire alarm has gone off.' Katya reacts dryly with a smile, without trying to dress up how she really feels."),
    (9, None, '\'We urgently need to go outside right now.\' Talking about the street before Denis, Katya puts the weight on "ulitsu" ("street", from "ulitsa") as the exchange unfolds.'),
    (10, None, '\'Forgive me, please, it was completely accidental.\' Denis politely uses this personal apology to Katya using "prosti" ("forgive me") — the close, informal way to say "forgive me" or "I\'m sorry" to someone dear.'),
    (11, None, "'No big deal, it is just red wine.' The guest continues dryly hearing Denis, to clear the air between them once and for all."),
]
