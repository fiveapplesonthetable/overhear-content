# Authoring module for kukhnya-s01e14-scene-26.
ID = 'kukhnya-s01e14-scene-26'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 14
SCENE = 26
TITLE = 'Выводы  (Conclusions)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.14'
SOURCE_FILE = 'sources/kukhnya/s01/e14.ru.dual.srt'
INTRO = "The evening is over, and Max has some thoughts about responsibility. Barinov's conclusion is much more practical."
OPENER = 'Slowly, from the thought to the toast.'
TRANSITION = 'And the last scene, once more in full.'
OUTRO = "That's the end of the episode. Max has his moral, Barinov has his promise, and the glasses are about to be filled. See you back in the kitchen."
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('max', 'Ответственность — странная штука.', 'Responsibility is a strange thing.', [], ''),
    ('max', 'С одной стороны, мы её боимся.', 'On the one hand, we are afraid of it.', [], ''),
    ('max', 'А с другой стороны...', 'And on the other hand...', [], ''),
    ('max', 'Именно благодаря ей завоёвываем уважение.', 'It is what earns us respect.', [], ''),
    ('max', 'И становимся ближе друг к другу.', 'And brings us closer together.', [], ''),
    ('max', 'Совершая безответственные поступки...', 'When we act irresponsibly...', [(371, 'А совершая безответственные поступки')], ''),
    ('max', 'Мы делаем правильные выводы.', 'We draw the right conclusions.', [(371, 'делаем правильные выводы')], ''),
    ('barinov', 'Всё, на работе больше не пью.', "That's it, I won't drink at work anymore.", [(372, 'Все, на работе больше не пью')], ''),
    ('barinov', 'Я решил.', "I've decided.", [], ''),
    ('barinov', 'Точно не пью.', "I definitely won't drink.", [], ''),
    ('barinov', 'Но это надо отметить.', 'But we should celebrate that.', [(374, 'Это надо отметить')], ''),
    ('barinov', 'Наливай!', 'Pour!', [], ''),
]
WALK = [
    (0, None, ["'Responsibility is a strange thing.' We can break down the phrase: ", ('max', 'Ответственность'), ' grows from the term for answer, so it is answerability. ', ('max', 'штука'), ' is a casual word for thing.']),
    (1, None, ["'On the one hand, we are afraid of it.' Now we can consider the speech: ", ('max', 'С'), ('max', 'одной'), ('max', 'стороны'), ' word-for-word means from one side. ', ('max', 'боимся'), ' is the verb for being afraid, which never appears without its ending.']),
    (2, None, ["'And on the other hand...' Let's examine this line: ", ('max', 'с'), ('max', 'другой'), ('max', 'стороны'), ', from the other side, completes the pair.']),
    (3, None, ["'It is what earns us respect.' Now we can consider the sentence: ", ('max', 'благодаря'), ('max', 'ей'), ' is thanks to it, from the verb to thank. ', ('max', 'завоёвываем'), ' literally says we conquer, the verb you would use for winning a war.']),
    (4, None, ["'And brings us closer together.' We can inspect the dialogue: ", ('max', 'друг'), ('max', 'к'), ('max', 'другу'), ', friend to friend, is the fixed phrase for each other. ', ('max', 'ближе'), ' is closer.']),
    (5, None, ["'When we act irresponsibly...' We can look at this line: ", ('max', 'безответственные'), ' is without plus the responsibility word. ', ('max', 'Совершая'), ' means while committing.']),
    (6, None, ["'We draw the right conclusions.' Russians make conclusions, so we hear ", ('max', 'делаем'), ', where English draws them. ', ('max', 'правильные'), ', meaning right, has the plural ending to match.']),
    (7, None, ["'That's it, I won't drink at work anymore.' Now we can analyze the dialogue: ", ('barinov', 'Всё'), ', meaning all, closes the topic. ', ('barinov', 'больше'), ('barinov', 'не'), ' is no more, and ', ('barinov', 'на'), ('barinov', 'работе'), ' is at work.']),
    (8, None, ["'I've decided.' We can break down the dialogue: ", ('barinov', 'решил'), " is a man's past form, making it a done deal. A woman would add an A."]),
    (9, None, ["'I definitely won't drink.' Now let's look at the dialogue: ", ('barinov', 'Точно'), ' is exactly, and here it means definitely. ', ('barinov', 'не'), ('barinov', 'пью'), ' is present, but it works as a promise for the future.']),
    (10, None, ["'But we should celebrate that.' We can analyze the sentence: ", ('barinov', 'надо'), ('barinov', 'отметить'), ' literally means it is needed to mark it, which is typical Russian for let us celebrate.']),
    (11, None, ["'Pour!' Let's examine the sentence: ", ('barinov', 'Наливай'), " is the command from the same verb as Nastya's she will pour. It is what you say to whoever has the bottle."]),
]
