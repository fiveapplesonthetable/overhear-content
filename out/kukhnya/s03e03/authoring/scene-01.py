# Authoring module for kukhnya-s03e03-scene-01.
ID = 'kukhnya-s03e03-scene-01'
SHOW = 'kukhnya'
SEASON = 3
EPISODE = 3
SCENE = 1
TITLE = 'Суеверные официанты  (Superstitious Waiters)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'guest': 'Гость', 'max': 'Макс', 'nastya': 'Настя'}
SOURCE_NAME = 'Кухня (Kukhnya) S3.03'
SOURCE_FILE = 'sources/kukhnya/s03/e03.ru.srt'
INTRO = 'In Episode Three of Season Three, Max explains that waiters are even more superstitious than athletes: spill a pinch of salt at a table, and a quarrel with the guest is practically guaranteed.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "And that finishes our opening scene. Listen for how the waitress's prophecy about spilled salt immediately comes true. Until next time!"
CLOSING = ('nastya', 'До завтра!')
STORY = [
    ('max', 'Спортсмены — самые суеверные люди в мире?', 'Are athletes the most superstitious people in the world?', [(1, 'Спортсмены'), (1, 'люди в мире')], 'adapted'),
    ('max', 'Ничего подобного. Самые суеверные люди — официанты.', 'Nothing of the sort. The most superstitious people are waiters.', [(2, 'Ничего подобного'), (2, 'люди – официанты')], 'adapted'),
    ('nastya', 'Ваш салат.', 'Your salad.', [(3, 'Ваш салат')], ''),
    ('guest', 'Соль просыпала. Ничего страшного.', 'I spilled the salt. No big deal.', [(4, 'Соль просыпала'), (5, 'Ничего страшного')], 'adapted'),
    ('nastya', 'Как это ничего страшного?', 'What do you mean, no big deal?', [(6, 'ничего страшного')], 'adapted'),
    ('nastya', 'Мы теперь с вами обязательно поссоримся.', 'Now you and I will definitely quarrel.', [(6, 'Мы теперь с вами обязательно поссоримся')], ''),
    ('guest', 'Девушка, я не собираюсь с вами ссориться.', 'Miss, I have no intention of quarreling with you.', [(7, 'Девушка, я не собираюсь с вами ссориться')], ''),
    ('guest', 'Вы куда смотрите? Сперва соль, потом вино!', 'Where are you looking? First salt, then wine!', [(9, 'куда смотрите? Сперва соль, потом')], 'adapted'),
    ('guest', 'Позовите администратора!', 'Call the manager!', [(10, 'администратора')], 'adapted'),
    ('nastya', 'Я же говорила, что поссоримся.', 'I told you we would quarrel.', [(10, 'Я же говорила, что поссоримся')], ''),
    ('max', 'Спасибо. До свидания. Ждём вас снова.', 'Thank you. Goodbye. We look forward to seeing you again.', [(11, 'Спасибо'), (12, 'До свидания. Ждем вас снова')], 'adapted'),
    ('max', 'Официанты верят во все приметы.', 'Waiters believe in all omens.', [(13, 'Официанты верят во все'), (13, 'приметы')], 'adapted'),
]
WALK = [
    (0, None, '\'Are athletes the most superstitious people in the world?\' Max checks briskly without holding back, leaning on "sportsmeny" ("athletes") before closing the thought with "samyye" ("most, very").'),
    (1, None, '\'Nothing of the sort. The most superstitious people are waiters.\' Max sustains an earnest manner in the conversation, putting "podobnogo" ("of the sort") alongside "samyye" ("most, very") in a tight, everyday turn of phrase.'),
    (2, None, '\'Your salad.\' Nastya strikes a thoughtful tempo with the guest, pairing "salat" ("salad") with "vash" ("your, yours") to get the point across in plain spoken Russian.'),
    (3, None, '\'I spilled the salt. No big deal.\' The guest keeps a grounded angle in the room, putting "sol" ("salt") alongside "prosypala" ("spilled") in a tight, everyday turn of phrase.'),
    (4, None, '\'What do you mean, no big deal?\' Nastya questions boldly at this point, combining "kak" ("how") and "strashnogo" ("terrible, serious") so the key meaning lands right away.'),
    (5, None, '\'Now you and I will definitely quarrel.\' Nastya sets a resolute posture in their talk, pairing "teper" ("now") with "obyazatelno" ("surely, without fail") to get the point across in plain spoken Russian.'),
    (6, None, '\'Miss, I have no intention of quarreling with you.\' The guest conveys a warm tack during the exchange, weaving "devushka" ("girlfriend") together with "sobirayus" ("am planning") just the way native speakers do.'),
    (7, None, '\'Where are you looking? First salt, then wine!\' The guest checks naturally without holding back, linking "kuda" ("where to"), "smotrite" ("look"), and "sperva" ("first") in one brisk exchange.'),
    (8, None, '\'Call the manager!\' The guest holds a firm note beside Max, joining "pozovite" ("call") to "administratora" ("administrator") so every word pulls its weight.'),
    (9, None, '\'I told you we would quarrel.\' Nastya picks an earnest attitude as they talk, pairing "possorimsya" ("will quarrel") with "govorila" ("said") so the "-sya" ending carries the action.'),
    (10, None, '\'Thank you. Goodbye. We look forward to seeing you again.\' Max keeps a calm tempo in the room, leaning on "spasibo" ("thank you") before closing the thought with "svidaniya" ("meeting").'),
    (11, None, '\'Waiters believe in all omens.\' Max picks an emphatic tempo as the scene unfolds, putting "ofitsianty" ("waiters") alongside "veryat" ("believe") in a tight, everyday turn of phrase.'),
]
