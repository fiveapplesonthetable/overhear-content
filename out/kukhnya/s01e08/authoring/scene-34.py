# Authoring module for kukhnya-s01e08-scene-34.
ID = 'kukhnya-s01e08-scene-34'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 8
SCENE = 34
TITLE = 'Неудачные дубли  (Outtakes and Bloopers)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'kostya': 'Костя', 'nastya': 'Настя'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.08'
SOURCE_FILE = 'sources/kukhnya/s01/e08.ru.dual.srt'
INTRO = "This is the last scene of the episode, and it plays like the closing montage of a show. At Claude Monet, Kostya, one of the cooks, works up the courage to ask Nastya out, while Barinov shouts about football. Here it is in Russian first."
OPENER = "Let's go through the finale. A date gets made, and Barinov gets loud."
TRANSITION = "Now the final scene from the top."
OUTRO = "That's the end of the episode. You've heard how to invite someone to the cinema — 'will you go to the movies with me?' — and how a Russian football fan roots for a team, literally 'to be sick for' them. Thanks for listening, and see you next time."
CLOSING = ('nastya', 'Пока')
STORY = [
    ('kostya', 'Настя, прекрати так громко смеяться на кухне!', 'Nastya, stop laughing so loudly in the kitchen!', [], ''),
    ('nastya', 'Костя, ты сегодня очень сердитый и смешной.', 'Kostya, you are very angry and funny today.', [], ''),
    ('kostya', 'Я просто устал после долгой тяжёлой смены.', 'I am simply tired after a long hard shift.', [], ''),
    ('nastya', 'Ты всегда сердишься без всякой причины.', 'You always get angry without any reason.', [], ''),
    ('kostya', 'Пойдёшь со мной сегодня вечером в кино?', 'Will you go to the cinema with me tonight?', [(379, 'Пойдешь к кино?')], ''),
    ('nastya', 'Ну ты настоящий чудак, конечно пойду!', 'Well you are a real oddball, of course I will go!', [(380, 'Ну ты придурок.')], ''),
    ('kostya', 'Тогда встречаемся в семь часов около метро.', "Then we meet at seven o'clock near the metro.", [(381, 'Ладно, пойдем. Тогда до вечера.')], ''),
    ('barinov', 'Кто опять трогал мою любимую кастрюлю?!', 'Who touched my favorite pot again?!', [(382, 'Подонки!')], ''),
    ('barinov', 'Ты за кого сегодня болел на матче?!', 'Who were you rooting for today at the match?!', [(383, 'Ты за кого болел? Ты за кого болел?')], ''),
    ('kostya', 'Шеф опять кричит про свой любимый футбол.', 'The chef is shouting again about his favorite football.', [], ''),
    ('nastya', 'Он всегда так громко переживает за Спартак.', 'He always worries so loudly about Spartak.', [], ''),
    ('barinov', 'Футбол — это самое главное в жизни!', 'Football is the most important thing in life!', [], ''),
    ('kostya', 'Пойдём скорее отсюда, пока он спокоен.', "Let's go quickly from here while he is calm.", [], ''),
    ('nastya', 'Да, идём скорее смотреть весёлый фильм!', "Yes, let's go quickly to watch a fun movie!", [], ''),
]
WALK = [
    (0, None, ["'Nastya, stop laughing so loudly in the kitchen!' Kostya tells her to stop laughing, using the word ", ('kostya', 'смеяться'), ' for to laugh.']),
    (1, None, ["'Kostya, you are very angry and funny today.' Nastya calls him angry and funny, with ", ('nastya', 'сердитый'), ' meaning angry.']),
    (2, None, ["'I am simply tired after a long hard shift.' The cook says he is tired, and ", ('kostya', 'устал'), ' literally says he got tired.']),
    (3, None, ["'You always get angry without any reason.' She points out he gets mad, and ", ('nastya', 'сердишься'), ' is related to the word for angry.']),
    (4, None, ["'Will you go to the cinema with me tonight?' He invites her out by asking ", ('kostya', 'Пойдёшь'), ', which means will you go.']),
    (5, None, ["'Well you are a real oddball, of course I will go!' Calling him a real oddball with ", ('nastya', 'чудак'), ', she agrees to go with him.']),
    (6, None, ["'Then we meet at seven o'clock near the metro.' They plan to meet at seven, using ", ('kostya', 'встречаемся'), ' for we meet.']),
    (7, None, ["'Who touched my favorite pot again?!' Barinov demands to know who touched his favorite pot, using ", ('barinov', 'трогал'), ' for touched.']),
    (8, None, ["'Who were you rooting for today at the match?!' Our loud boss asks who someone rooted for, where ", ('barinov', 'болел'), ' means rooted or was ill for.']),
    (9, None, ["'The chef is shouting again about his favorite football.' Mentioning the constant shouting about football, ", ('kostya', 'опять'), ' shows it happens again.']),
    (10, None, ["'He always worries so loudly about Spartak.' Noticing that he always worries loudly, she uses ", ('nastya', 'переживает'), ' to describe how he worries.']),
    (11, None, ["'Football is the most important thing in life!' Football is the most important thing, and ", ('barinov', 'главное'), ' signifies the main or important part.']),
    (12, None, ["'Let's go quickly from here while he is calm.' Suggesting they leave while he is ", ('kostya', 'спокоен'), ', meaning calm, they prepare to go.']),
    (13, None, ["'Yes, let's go quickly to watch a fun movie!' Agreeing to quickly go watch a ", ('nastya', 'весёлый'), ' movie, they look forward to a fun time.']),
]
