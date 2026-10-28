# Authoring module for kukhnya-s01e07-scene-15.
ID = 'kukhnya-s01e07-scene-15'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 7
SCENE = 15
TITLE = 'Правда отменяется  (The Truth Is Canceled)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.07'
SOURCE_FILE = 'sources/kukhnya/s01/e07.ru.dual.srt'
INTRO = "In the kitchen at Claude Monet, the lying is over, and Max, the young cook, has made a dish for Chef Barinov to judge. For once the chef likes it, and Max can't resist a remark about his smile. Start with the Russian."
OPENER = 'Slowly now. Notice how Barinov swings from praise to a shout in the space of a line.'
TRANSITION = 'Now the whole exchange in one go.'
OUTRO = "After all the shouting, the scene ends on 'thank you very much, chef'. Take that one with you."
CLOSING = ('max', 'Пока!')
STORY = [
    ('max', 'Шеф, попробуйте, пожалуйста, это горячее блюдо.', 'Chef, please taste this hot dish.', [], ''),
    ('barinov', 'Давай сюда тарелку, я сейчас попробую.', 'Give the plate here, I will taste it now.', [], ''),
    ('barinov', 'Очень вкусно, можно подавать гостям.', 'Very tasty, we can serve it to the guests.', [(313, 'Очень вкусно. Можно подавать')], ''),
    ('max', 'Неужели вы говорите мне чистую правду?', 'Are you really telling me the pure truth?', [(312, 'Правда')], ''),
    ('barinov', 'Да, блюдо получилось действительно великолепным.', 'Yes, the dish turned out truly magnificent.', [], ''),
    ('max', 'Шеф, вы сейчас так радостно улыбаетесь!', 'Chef, you are smiling so joyfully now!', [(314, 'Не улыбайтесь так')], ''),
    ('barinov', 'А что, повар уже не может улыбнуться?', 'Why, can a cook no longer smile?', [], ''),
    ('max', 'Не улыбайтесь так, вы похожи на клоуна.', 'Do not smile like that, you look like a clown.', [(314, 'вы похожи на бесеного класса')], ''),
    ('barinov', 'Замолчи сейчас же, наглый огузок!', 'Be quiet right now, insolent rump!', [(315, 'Заткнись')], ''),
    ('barinov', 'С этого момента вся правда отменяется!', 'From this moment on, all truth is canceled!', [(316, 'с этого момента правда отменяется')], ''),
    ('max', 'Я вас понял, возвращаемся к работе.', 'I understood you, we return to work.', [], ''),
    ('barinov', 'И ещё одно важное слово, Максим.', 'And one more important word, Maxim.', [(317, 'И еще')], ''),
    ('barinov', 'Спасибо за отличную работу на кухне.', 'Thank you for the excellent work in the kitchen.', [(318, 'Спасибо')], ''),
    ('max', 'Спасибо вам большое, шеф!', 'Thank you very much, chef!', [], ''),
]
WALK = [
    (0, None, '\'Chef, please taste this hot dish.\' "Poprobuyte" is the polite command of poprobovat\', the right form for a boss. "Goryacheye" ends in -eye to match blyudo, a neuter word.'),
    (1, None, '\'Give the plate here, I will taste it now.\' "Davay" here means \'give\', a casual \'hand it over\'. "Syuda" is \'to here\', with movement, since the plate has to travel.'),
    (2, None, '\'Very tasty, we can serve it to the guests.\' "Mozhno", \'it\'s allowed\', covers \'we can\' and \'one may\'. "Gostyam", \'to the guests\', is the \'to\' plural of gost\'.'),
    (3, None, '\'Are you really telling me the pure truth?\' "Neuzheli", \'really?\', shows surprise with some doubt. "Chistuyu pravdu" is the honest truth the cooks promised to tell.'),
    (4, None, '\'Yes, the dish turned out truly magnificent.\' "Poluchilos\'" has -o because blyudo is neuter. As with the sauce, the word that follows ends in -ym: velikolepnym.'),
    (5, None, '\'Chef, you are smiling so joyfully now!\' "Ulybaetes\'" is the vy form Max owes his boss, from ulybat\'sya, with -sya shortened to -s\'. "Radostno", \'joyfully\', grows out of radost\', joy.'),
    (6, None, '\'Why, can a cook no longer smile?\' A chto at the start is a challenging \'so what?\'. "Ulybnut\'sya" is the one-time partner of ulybat\'sya, so it means \'give a smile\'.'),
    (7, None, '\'Do not smile like that, you look like a clown.\' "Pokhozh na", \'similar to\', gives you \'look like\'. After na a clown, being alive, takes -a: klouna.'),
    (8, None, '\'Be quiet right now, insolent rump!\' "Zamolchi" adds za-, \'start\', to molchat\', to be silent. "Seychas zhe", \'right now\', adds zhe for insistence.'),
    (9, None, '\'From this moment on, all truth is canceled!\' "Otmenyaetsya", \'is canceled\', uses -sya to make the verb passive. S etogo momenta, \'from this moment\', works for any announcement.'),
    (10, None, "'I understood you, we return to work.' Ya vas ponyal, 'I understood you', is a common 'got it' to a boss. K rabote, 'to work', changes rabota to rabote."),
    (11, None, '\'And one more important word, Maxim.\' Barinov switches to Max\'s full name to sound serious. "Eshchyo odno", \'one more\', is literally \'still one\'.'),
    (12, None, '\'Thank you for the excellent work in the kitchen.\' "Spasibo za", \'thanks for\', puts the thing into its object form: otlichnuyu rabotu. "Otlichno" is also the top mark at school.'),
    (13, None, '\'Thank you very much, chef!\' "Spasibo vam bol\'shoye" means \'big thanks to you\', and the vam makes it warmer. "Bol\'shoye" agrees with spasibo, which is neuter.'),
]
