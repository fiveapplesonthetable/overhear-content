# Authoring module for kukhnya-s01e05-scene-23.
ID = 'kukhnya-s01e05-scene-23'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 5
SCENE = 23
TITLE = 'Конец трудного дня  (End of a Difficult Day)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'kostya': 'Костя', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.05'
SOURCE_FILE = 'sources/kukhnya/s01/e05.ru.dual.srt'
INTRO = 'The evening shift at Claude Monet is finally over. Max has survived his first day as a fish cook, and he looks back on it and on the people around him, while we catch Kostya and Chef Barinov in passing. Listen in Russian first.'
OPENER = 'Now through it slowly. Most of this is Max thinking aloud, so the sentences are calm.'
TRANSITION = 'One last time, the end of the day.'
OUTRO = 'Max ends with "pora otdokhnut", \'time to rest\', and after a day like that he\'s earned it. "Byvayut dni", \'there are days\', is a line you\'ll find a use for too.'
CLOSING = ('max', 'Пока!')
STORY = [
    ('max', 'Бывают дни, когда всё идёт не так.', 'There are days when everything goes wrong.', [(314, 'бывают дни, когда у тебя все идет не так.')], ''),
    ('max', 'На кухне сегодня была настоящая запара.', 'In the kitchen today there was a real rush.', [], ''),
    ('max', 'Шеф кричал, а заказы не заканчивались.', 'The chef shouted, and the orders did not end.', [], ''),
    ('max', 'Но такие трудные дни всегда заканчиваются.', 'But such difficult days always end.', [(315, 'такие дни всегда заканчиваются.')], ''),
    ('max', 'Кому-то этот день принёс что-то новое.', 'To someone this day brought something new.', [(316, 'Кому-то этот день принес что-то новое.')], ''),
    ('max', 'Для кого-то всё остаётся по-старому.', 'For someone everything stays the same.', [(317, 'Для кого-то все остается по-старому.')], ''),
    ('kostya', 'Привет, Настя, рад тебя видеть.', 'Hi, Nastya, glad to see you.', [(318, 'Привет.')], ''),
    ('kostya', 'Надеюсь, твоя смена прошла хорошо.', 'I hope your shift went well.', [], ''),
    ('barinov', 'Семь тысяч рублей на Спартак!', 'Seven thousand rubles on Spartak!', [(319, 'Семь тысяч на Спартак.')], ''),
    ('barinov', 'Моя любимая команда обязательно победит!', 'My favorite team will definitely win!', [], ''),
    ('max', 'Кто-то искренне рад этому дню.', 'Someone is truly glad about this day.', [(320, 'Кто-то рад этому дню.')], ''),
    ('max', 'А я счастлив, что он закончился.', 'And I am happy that it ended.', [(321, 'А'), (322, 'я счастлив, что он закончился.')], ''),
    ('max', 'Завтра на кухне начнётся новая работа.', 'Tomorrow in the kitchen new work will begin.', [], ''),
    ('max', 'А сегодня пора немного отдохнуть.', 'And today it is time to rest a little.', [], ''),
]
WALK = [
    (0, None, '\'There are days when everything goes wrong.\' "Byvayut", from "byvat", is \'there are\', with a sense of \'it happens now and then\'. "Idyot ne tak" is literally \'goes not so\'.'),
    (1, None, '\'In the kitchen today there was a real rush.\' "Byla" has -a to match "zapara", which is feminine. "Nastoyashchaya", \'real\', is the same word that means \'true\'.'),
    (2, None, '\'The chef shouted, and the orders did not end.\' The little a in the middle sets up a contrast, like \'while\'. "Zakanchivalis" is \'were coming to an end\', and with the "ne" in front the orders just kept coming.'),
    (3, None, '\'But such difficult days always end.\' All three words share a plural ending: "takiye trudnyye dni", such hard days. "Trudnyye" is related to "trud", labour, and "zakanchivayutsya", they end, carries a "-sya" because the days end by themselves.'),
    (4, None, '\'To someone this day brought something new.\' "Komu-to" is "kto-to", \'someone\', changed to mean \'to someone\'. "Chto-to novoe", \'something new\', has neuter -oe.'),
    (5, None, '\'For someone everything stays the same.\' "Po-staromu", \'the same as before\', is literally \'in the old way\'. After "dlya", \'for\', "kto-to" becomes "kogo-to".'),
    (6, None, '\'Hi, Nastya, glad to see you.\' Kostya says "rad" as a man, and drops the "ya", as people often do in greetings. "Tebya", \'you\', is the accusative after "videt".'),
    (7, None, '\'I hope your shift went well.\' "Proshla", \'went\' or \'passed\', has -a to match "smena", \'shift\'. "Khorosho", \'well\', also does duty as \'good\'.'),
    (8, None, '\'Seven thousand rubles on Spartak!\' Spartak is a Moscow football club. After "sem", \'seven\', both words go into the genitive plural: "tysyach rubley".'),
    (9, None, '\'My favorite team will definitely win!\' Since "komanda", team, is feminine, both "moya" and "lyubimaya", favourite, take the feminine ending. "Pobedit" has no word for "will", yet it points to the future: a perfective verb in this form always does.'),
    (10, None, '\'Someone is truly glad about this day.\' "Iskrenne", \'sincerely\', is the adverb from "iskrenniy". "Rad etomu dnyu" is literally \'glad to this day\'.'),
    (11, None, '\'And I am happy that it ended.\' "Schastliv", \'happy\', is the short form for a man. On, \'it\', refers to "den", \'day\', which is masculine.'),
    (12, None, '\'Tomorrow in the kitchen new work will begin.\' "Nachnyotsya", \'will begin\', means \'will begin\', and the -sya stays on the end. "Novaya" ends in -aya to match "rabota".'),
    (13, None, '\'And today it is time to rest a little.\' "Pora", \'it\'s time\', needs no \'is\': it\'s just \'time to rest\'. "Otdokhnut" shares "dokh" with "vdokh" and "vydokh", so it\'s close to \'catch your breath\'.'),
]
