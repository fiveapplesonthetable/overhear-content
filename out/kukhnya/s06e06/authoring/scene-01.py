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
    (0, None, '\'Are you not tired of gray Moscow yet?\' The guest spotlights one sharp term toward Denis: "yeshchyo" means "more, still", and it carries the main weight of what the guest is saying.'),
    (1, None, "'Maybe you will go to Paris with me?' The guest drops this point with ease: Russian keeps the exact word order of a normal statement here, turning it into a question for Katya purely through rising pitch at the end."),
    (2, None, "'There we will find you a good job.' The guest weighs in plainly hearing Denis, before Denis can change the subject."),
    (3, None, '\'Or is something keeping you here?\' The guest underscores this vivid piece in reply: "derzhit" means "keeps" (from "derzhat"), giving the line its exact edge.'),
    (4, None, '\'No, nothing is keeping me here.\' Katya shares that line plainly here: Russian happily doubles the negative here — pairing "never" or "nothing" with "ne" ("not") — which is the only natural way to say it.'),
    (5, None, "'Are you not rushing things a bit too much?' Katya asks firmly how the guest expects that to work in practice."),
    (6, None, '\'I am kissing you for the first time in five years.\' The guest underscores one clear word in earnest: "vpervyye" means "for the first time", and it carries the main weight of what the guest is saying.'),
    (7, None, "'In my opinion, I am already terribly late.' The guest weighs in boldly on the spot, to clear the air between them once and for all."),
    (8, None, "'Listen, the fire alarm has gone off.' Katya holds firm dryly as things stand, letting the remark speak for itself."),
    (9, None, '\'We urgently need to go outside right now.\' Katya chooses one concrete touch in reply: "ulitsu" means "street" (from "ulitsa"), giving the line its exact edge.'),
    (10, None, '\'Forgive me, please, it was completely accidental.\' Denis shares this point right away: adding "sovsem" ("completely, at all") pushes the statement all the way, leaving zero room for doubt.'),
    (11, None, "'No big deal, it is just red wine.' The guest answers dryly with a shrug, keeping the focus on what actually matters here."),
]
