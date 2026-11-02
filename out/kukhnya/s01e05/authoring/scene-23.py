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
OUTRO = "Max ends with the phrase for 'time to rest', and after a day like that he's earned it. The phrase 'there are days' is a line you'll find a use for too."
CLOSING = ('max', 'Пока!')
STORY = [
    ('max', 'Бывают дни, когда всё идёт не так.', 'There are days when everything goes wrong.', [(314, 'бывают дни, когда у тебя все идет не так.')], ""),
    ('max', 'На кухне сегодня была настоящая запара.', 'In the kitchen today there was a real rush.', [], ""),
    ('max', 'Шеф кричал, а заказы не заканчивались.', 'The chef shouted, and the orders did not end.', [], ""),
    ('max', 'Но такие трудные дни всегда заканчиваются.', 'But such difficult days always end.', [(315, 'такие дни всегда заканчиваются.')], ""),
    ('max', 'Кому-то этот день принёс что-то новое.', 'To someone this day brought something new.', [(316, 'Кому-то этот день принес что-то новое.')], ""),
    ('max', 'Для кого-то всё остаётся по-старому.', 'For someone everything stays the same.', [(317, 'Для кого-то все остается по-старому.')], ""),
    ('kostya', 'Привет, Настя, рад тебя видеть.', 'Hi, Nastya, glad to see you.', [(318, 'Привет.')], ""),
    ('kostya', 'Надеюсь, твоя смена прошла хорошо.', 'I hope your shift went well.', [], ""),
    ('barinov', 'Семь тысяч рублей на Спартак!', 'Seven thousand rubles on Spartak!', [(319, 'Семь тысяч на Спартак.')], ""),
    ('barinov', 'Моя любимая команда обязательно победит!', 'My favorite team will definitely win!', [], ""),
    ('max', 'Кто-то искренне рад этому дню.', 'Someone is truly glad about this day.', [(320, 'Кто-то рад этому дню.')], ""),
    ('max', 'А я счастлив, что он закончился.', 'And I am happy that it ended.', [(321, 'А'), (322, 'я счастлив, что он закончился.')], ""),
    ('max', 'Завтра на кухне начнётся новая работа.', 'Tomorrow in the kitchen new work will begin.', [], ""),
    ('max', 'А сегодня пора немного отдохнуть.', 'And today it is time to rest a little.', [], ""),
]
WALK = [
    (0, None, ["'There are days when everything goes wrong.' from the verb for 'to be', ", ('max', 'Бывают'), " is 'there are', with a sense of 'it happens now and then'. ", ('max', 'идёт'), ('max', 'не'), ('max', 'так.'), " is literally 'goes not so'."]),
    (1, None, ["'In the kitchen today there was a real rush.' has the feminine past ending to ", ('max', 'была'), ' match the rush. ', ('max', 'настоящая'), ", 'real', is the same word that literally translates to 'true'."]),
    (2, None, ["'The chef shouted, and the orders did not end.' The little ", ('max', 'а'), " in the middle sets up a contrast, like 'while'. ", ('max', 'заканчивались.'), " is 'were coming to an end', and with the negation in front the orders just kept coming."]),
    (3, None, ["'But such difficult days always end.' All three words share a plural ending: ", ('max', 'такие'), ('max', 'трудные'), ('max', 'дни'), ' such hard days. ', ('max', 'трудные'), ' is related to the word for labour, and ', ('max', 'заканчиваются.'), ' they end, carries a reflexive suffix because the days end by themselves.']),
    (4, None, ["'To someone this day brought something new.' is 'someone' changed to mean 'to ", ('max', 'Кому-то'), " someone'. ", ('max', 'что-то'), ('max', 'новое.'), ", 'something new', has a neuter ending."]),
    (5, None, ["'For someone everything stays the same.' , 'the same as before', is ", ('max', 'по-старому.'), " literally 'in the old way'. After ", ('max', 'Для'), ", 'for', the word for 'someone' becomes ", ('max', 'кого-то'), '.']),
    (6, None, ["'Hi, Nastya, glad to see you.' Kostya says ", ('kostya', 'рад'), " as a man, and drops the 'I', as people often do in greetings. ", ('kostya', 'тебя'), " 'you', is the accusative after the verb 'to see'."]),
    (7, None, ["'I hope your shift went well.' , 'went' or 'passed', has the ", ('kostya', 'прошла'), " feminine ending to match the shift. ", ('kostya', 'хорошо.'), ", 'well', also does duty as 'good'."]),
    (8, None, ["'Seven thousand rubles on Spartak!' Spartak is a Moscow football club. After ", ('barinov', 'Семь'), ", 'seven', both words go into the genitive plural: ", ('barinov', 'тысяч'), ('barinov', 'рублей'), '.']),
    (9, None, ["'My favorite team will definitely win!' Since the team is feminine, both ", ('barinov', 'Моя'), ' and ', ('barinov', 'любимая'), ', favourite, take the feminine ending. ', ('barinov', 'победит!'), " has no word for 'will', yet it points to the future: a perfective verb in this form always does."]),
    (10, None, ["'Someone is truly glad about this day.' , 'sincerely', is the adverb ", ('max', 'искренне'), " form. ", ('max', 'рад'), ('max', 'этому'), ('max', 'дню.'), " is literally 'glad to this day'."]),
    (11, None, ["'And I am happy that it ended.' , 'happy', is the short form ", ('max', 'счастлив,'), " for a man. ", ('max', 'он'), ", 'it', refers to the day, which is masculine."]),
    (12, None, ["'Tomorrow in the kitchen new work will begin.' , expresses 'will begin', and the ", ('max', 'начнётся'), " reflexive suffix stays on the end. ", ('max', 'новая'), ' takes a feminine ending to match the work.']),
    (13, None, ["'And today it is time to rest a little.' , 'it's time', needs no 'is': ", ('max', 'пора'), " it's just 'time to rest'. ", ('max', 'отдохнуть.'), " shares a root with breathing in and out, so it's close to 'catch your breath'."]),
]
