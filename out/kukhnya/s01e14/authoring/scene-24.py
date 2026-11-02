# Authoring module for kukhnya-s01e14-scene-24.
ID = 'kukhnya-s01e14-scene-24'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 14
SCENE = 24
TITLE = 'Храбрый круассан  (The Brave Croissant)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'max': 'Макс', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.14'
SOURCE_FILE = 'sources/kukhnya/s01/e14.ru.dual.srt'
INTRO = 'Max goes to the bar, where Vika has a drink waiting for him. In this kitchen, people are croissants or sticks of celery, and Max wants to know which he is.'
OPENER = 'Again, slowly.'
TRANSITION = 'Now the scene in one piece.'
OUTRO = 'Vika gives Max a nickname, and the night ends warmly at the bar. One more talk is waiting in the office. Until next time.'
CLOSING = ('vika', 'Пока!')
STORY = [
    ('max', 'А я кто?', 'And what am I?', [(313, 'А я кто')], ''),
    ('max', 'Круассан или сельдерей?', 'A croissant or celery?', [(313, 'Круассан или сельдерей')], ''),
    ('vika', 'Ну, конечно, круассан.', 'Well, of course a croissant.', [(314, 'Ну, конечно, круассан')], ''),
    ('max', 'Почему круассан?', 'Why a croissant?', [], ''),
    ('max', 'Я же не ем мучное.', "I don't eat flour products.", [(315, 'Я же не ем мучную')], ''),
    ('vika', 'Ты спас наш ресторан.', 'You saved our restaurant.', [], ''),
    ('vika', 'Ты молодец, Макс.', 'You did great, Max.', [], ''),
    ('max', 'Я просто сделал свою работу.', 'I just did my job.', [], ''),
    ('vika', 'Нет, это было круто.', 'No, it was cool.', [], ''),
    ('vika', 'Ты очень помог мне.', 'You helped me a lot.', [], ''),
    ('vika', 'Спасибо тебе.', 'Thank you.', [(316, 'Спасибо тебе')], ''),
    ('vika', 'Мой храбрый круассан.', 'My brave croissant.', [(316, 'мой храбрый круассан')], ''),
]
WALK = [
    (0, None, ["'And what am I?' Literally and I who? Russian uses ", ('max', 'кто'), ', meaning who, for a person even here, where English says what.']),
    (1, None, ["'A croissant or celery?' We can analyze the words: ", ('max', 'Круассан'), ' is French and celery is borrowed too, so both are easy to guess. ', ('max', 'или'), ' means or.']),
    (2, None, ["'Well, of course a croissant.' Vika answers with the noun alone, no you are. ", ('vika', 'Ну'), ', meaning well, softens it.']),
    (3, None, ["'Why a croissant?' Let's break down the words: ", ('max', 'Почему'), ' is why. Inside it is a form of the word for what.']),
    (4, None, ["'I don't eat flour products.' Now let's inspect the words: ", ('max', 'мучное'), ', floury things, comes from the term for flour. ', ('max', 'не'), ('max', 'ем'), ' is I do not eat, and ', ('max', 'же'), ' adds after all.']),
    (5, None, ["'You saved our restaurant.' We can break down the dialogue: ", ('vika', 'спас'), ' is saved, which echoes the word Kostya used about Max. ', ('vika', 'наш'), ('vika', 'ресторан'), ' does not change its ending here, even though it is the thing being saved.']),
    (6, None, ["'You did great, Max.' Russians say ", ('vika', 'молодец'), ', meaning you are a fine fellow, to anyone who did well.']),
    (7, None, ["'I just did my job.' We can analyze the phrase: ", ('max', 'свою'), ('max', 'работу'), " is my own job. The term for one's own replaces my when it belongs to the subject."]),
    (8, None, ["'No, it was cool.' Let's examine the dialogue: ", ('vika', 'круто'), ' is slang for cool, but its plain meaning is steeply, as in a steep hill.']),
    (9, None, ["'You helped me a lot.' Let us examine the phrase: ", ('vika', 'помог'), ('vika', 'мне'), ' means helped to me. ', ('vika', 'очень'), ('vika', 'помог'), ', literally very helped, is how Russian says helped a lot.']),
    (10, None, ["'Thank you.' Now we can inspect the words: ", ('vika', 'Спасибо'), ('vika', 'тебе'), ' means thanks to you. With someone you speak to formally, it would change.']),
    (11, None, ["'My brave croissant.' Let us analyze the sentence: ", ('vika', 'храбрый'), ', meaning brave, has the masculine ending because ', ('vika', 'круассан'), ' is masculine. Now it is a pet name.']),
]
