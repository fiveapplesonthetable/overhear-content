# Authoring module for kukhnya-s01e02-scene-18.
ID = 'kukhnya-s01e02-scene-18'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 2
SCENE = 18
TITLE = 'Матч на кухне  (Match in the Kitchen)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'senya': 'Сеня'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.02'
SOURCE_FILE = 'sources/kukhnya/s01/e02.ru.dual.srt'

INTRO = "Chef Viktor is in his office, glued to the television. It's the big Moscow derby, his beloved Spartak against CSKA, and the cook Senya wants to know when dinner service starts. The chef doesn't want to hear about food. Here's the Russian first."
OPENER = "Let's run through the match."
TRANSITION = "Now let's listen to the conversation again without interruption."
OUTRO = "Barinov would rather watch Spartak than cook. Keep the word for \"it's time\", which Senya used twice to get him back to the stove."

STORY = [
    ('senya', 'Шеф, пора начинать готовить горячие блюда?', 'Chef, is it time to start preparing hot dishes?', [], ''),
    ('barinov', 'Тихо, Сеня! Сейчас идёт решающий матч!', 'Quiet, Senya! A decisive match is on right now!', [], ''),
    ('senya', 'Кто сегодня играет в этом матче?', 'Who is playing in this match today?', [], ''),
    ('barinov', 'Наш великий Спартак играет против ЦСКА!', 'Our great Spartak is playing against CSKA!', [], ''),
    ('senya', 'И какой сейчас счёт в игре?', 'And what is the score in the game now?', [], ''),
    ('barinov', 'Пока ничья, но мы должны победить!', 'A draw so far, but we must win!', [], ''),
    ('senya', 'Смотрите, мяч летит к их воротам!', 'Look, the ball is flying toward their goal!', [], ''),
    ('barinov', 'У своей штрафной площади ЦСКА держит оборону.', 'CSKA is holding the defence near its own penalty area.', [(209, 'держит оборону')], ''),
    ('senya', 'Нападающий Спартака получает быстрый пас.', 'The Spartak forward receives a fast pass.', [], ''),
    ('barinov', 'Давай, Ари с мячом сильно бьёт!', 'Come on, Ari with the ball shoots hard!', [(210, 'бьет')], ''),
    ('senya', 'Вратарь с трудом ловит этот мяч.', 'The goalkeeper catches this ball with difficulty.', [], ''),
    ('barinov', 'Какой опасный и красивый был момент!', 'What a dangerous and beautiful moment it was!', [], ''),
    ('senya', 'А теперь пора вернуться к нашей кухне.', 'And now it is time to return to our kitchen.', [], ''),
]

WALK = [
    (0, None, [
        "'Chef, is it time to start preparing hot dishes?' The word for \"it's time\" is ",
        ('senya', 'пора'),
        " and it takes the action word to start, ",
        ('senya', 'начинать'),
        " In the phrase for hot dishes, ",
        ('senya', 'горячие блюда?'),
        " the word ",
        ('senya', 'блюда?'),
        " changes its ending for more than one."
    ]),
    (1, None, [
        "'Quiet, Senya! A decisive match is on right now!' The word for quiet is ",
        ('barinov', 'Тихо,'),
        " In Russian a match literally goes, ",
        ('barinov', 'идёт'),
        " and the word for decisive, ",
        ('barinov', 'решающий'),
        " is the match that decides it all."
    ]),
    (2, None, [
        "'Who is playing in this match today?' The word for plays, ",
        ('senya', 'играет'),
        " is the action word used for games. The phrase for in this match is ",
        ('senya', 'в этом матче?'),
        " a game is something you play in, so it uses the little word for in, and the word for match changes its ending."
    ]),
    (3, None, [
        "'Our great Spartak is playing against CSKA!' The word for against is ",
        ('barinov', 'против'),
        " The grand word for great is ",
        ('barinov', 'великий'),
        " and the word for our, ",
        ('barinov', 'Наш'),
        " shows the chef is a fan."
    ]),
    (4, None, [
        "'And what is the score in the game now?' The word for score, ",
        ('senya', 'счёт'),
        " translates to the restaurant bill too. The phrase for in the game is ",
        ('senya', 'в игре?')
    ]),
    (5, None, [
        "'A draw so far, but we must win!' The word for a draw, ",
        ('barinov', 'ничья,'),
        " is literally nobody's. The word for so far, ",
        ('barinov', 'Пока'),
        " translates to bye in other contexts, and the phrase for must win is ",
        ('barinov', 'должны победить!')
    ]),
    (6, None, [
        "'Look, the ball is flying toward their goal!' The word for goal, ",
        ('senya', 'воротам!'),
        " is always used as more than one, because it literally translates to gates. The action word for flies is ",
        ('senya', 'летит')
    ]),
    (7, None, [
        "'CSKA is holding the defence near its own penalty area.' The word for one's own is ",
        ('barinov', 'своей'),
        " The phrase for the penalty area is ",
        ('barinov', 'штрафной площади'),
        " built from the word for a town square. The phrase for holds the defence is ",
        ('barinov', 'держит оборону.')
    ]),
    (8, None, [
        "'The Spartak forward receives a fast pass.' The word for forward, ",
        ('senya', 'Нападающий'),
        " is literally the attacking one. The action word for receives is ",
        ('senya', 'получает'),
        " and the word for pass, ",
        ('senya', 'пас.'),
        " is built from English."
    ]),
    (9, None, [
        "'Come on, Ari with the ball shoots hard!' The word for come on, ",
        ('barinov', 'Давай,'),
        " is a friendly encouragement. The phrase for with the ball, ",
        ('barinov', 'с мячом'),
        " changes its ending, and the action word for hits, ",
        ('barinov', 'бьёт!'),
        " is literally how they describe a shot."
    ]),
    (10, None, [
        "'The goalkeeper catches this ball with difficulty.' The word for the goalkeeper, ",
        ('senya', 'Вратарь'),
        " is built from the word for the goal, meaning the gatekeeper. The phrase for with difficulty, ",
        ('senya', 'с трудом'),
        " translates to with labour."
    ]),
    (11, None, [
        "'What a dangerous and beautiful moment it was!' The word for what a, ",
        ('barinov', 'какой'),
        " begins the exclamation. The action word for was, ",
        ('barinov', 'был'),
        " is masculine because the word for moment is."
    ]),
    (12, None, [
        "'And now it is time to return to our kitchen.' The word for it's time appears again, ",
        ('senya', 'пора'),
        " now with the action word to return, ",
        ('senya', 'вернуться'),
        " In the phrase for to our kitchen, ",
        ('senya', 'к нашей кухне.'),
        " the little word for to changes the endings of the next words."
    ]),
]
CLOSING = ("barinov", "Счастливо!")
