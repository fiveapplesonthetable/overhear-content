# Authoring module for kukhnya-s01e01-scene-24.
ID = 'kukhnya-s01e01-scene-24'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 1
SCENE = 24
TITLE = 'Это моя кухня  (This Is My Kitchen)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'max': 'Макс', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.01'
SOURCE_FILE = 'sources/kukhnya/s01/e01.ru.dual.srt'
INTRO = "A guest in the dining room has suddenly fallen ill, and Chef Barinov realizes it was after eating the dish Max swapped in without asking. The chef explodes at Max. Then a phone call arrives, and everything changes. Here's the Russian first."
OPENER = 'Now the chaos, line by line.'
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'Max got away with it by pure luck, and the chef is furious about that too. Pay attention to "this is my kitchen", because it\'s the chef\'s signature line.'
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('vika', 'Шеф, в зале гостю стало очень плохо!', 'Chef, a guest in the hall became very ill!', [(324, 'гость отравился.')], ''),
    ('barinov', 'Что случилось? Это не моё блюдо!', 'What happened? This is not my dish!', [(326, 'Что случилось?'), (329, 'Это не мое блюдо.')], ''),
    ('max', 'Шеф, это блюдо приготовил я.', 'Chef, I cooked this dish.', [(332, 'Это мое блюдо.')], ''),
    ('max', 'Я заменил ваше блюдо на своё.', 'I replaced your dish with mine.', [(333, 'Я заменил ваше блюдо на свое.')], ''),
    ('barinov', 'Ты вообще как посмел такое сделать?', 'How did you dare do such a thing?', [(340, 'Ты вообще как посмел')], ''),
    ('barinov', 'Запомни раз и навсегда: это моя кухня!', 'Remember once and for all: this is my kitchen!', [(342, 'Это моя кухня!')], ''),
    ('barinov', 'Ты поставил под угрозу жизнь человека!', "You endangered a human being's life!", [(343, 'поставил под угрозу жизни,')], ''),
    ('barinov', 'Пошёл вон отсюда прямо сейчас!', 'Get out of here right now!', [(346, 'Пошел вон!')], ''),
    ('barinov', 'Алло? Да, Дима, я слушаю.', "Hello? Yes, Dima, I'm listening.", [(346, 'Алло.'), (347, 'Да, Дима.')], ''),
    ('barinov', 'Какие новости из больницы, говори скорее.', 'What news from the hospital, speak quickly.', [(348, 'для тебя хорошие новости.')], ''),
    ('barinov', 'Что? Врачи обнаружили у него аневризму?', 'What? The doctors discovered an aneurysm in him?', [(349, 'обнаружили аневризму,')], ''),
    ('barinov', 'Значит, это спасло ему жизнь?', 'Does that mean this saved his life?', [(352, 'ты ему жизнь спас.')], ''),
    ('max', 'Шеф, так значит, никто не умер?', 'Chef, does that mean nobody died?', [], ''),
    ('barinov', 'Молчи, сегодня тебе просто невероятно повезло.', 'Keep quiet, today you were simply incredibly lucky.', [], ''),
]
WALK = [
    (0, None, '\'Chef, a guest in the hall became very ill!\' Russian says "to the guest it became badly": "stalo plokho", with "gostyu" in the "to" form. There\'s no "feels" in it, and "stalo" is neuter because nobody is doing it.'),
    (1, None, '\'What happened? This is not my dish!\' "Sluchilos\'" is "happened", neuter again. "Moyo blyudo" is "my dish", and "moyo" is the neuter "my".'),
    (2, None, '\'Chef, I cooked this dish.\' Russian puts the news last, so "ya" comes at the end: "this dish cooked I". That is how Max says it was him.'),
    (3, None, '\'I replaced your dish with mine.\' "Zamenil" is "replaced", from "menyat\'", to change. "Na svoyo" is "with my own", so Russian doesn\'t have to repeat the word "dish".'),
    (4, None, '\'How did you dare do such a thing?\' "Kak posmel" is "how dared", the same "posmel" as Vika used. "Takoye" is "such a thing", ending in -oye.'),
    (5, None, '\'Remember once and for all: this is my kitchen!\' "Zapomni" is a command built on "pomnit\'", to remember. "Raz i navsegda" is literally "once and forever".'),
    (6, None, '\'You endangered a human being\'s life!\' "Postavil pod ugrozu" is "put under threat", a stock phrase for "endangered". "Zhizn\' cheloveka" is "life of a person", with an -a for "of".'),
    (7, None, '\'Get out of here right now!\' "Poshyol" is "went", used as a rude command. "Von" is "out" here, and "otsyuda" is "from here", the partner of "syuda".'),
    (8, None, '\'Hello? Yes, Dima, I\'m listening.\' "Allo" is borrowed, like English "hello". "Ya slushayu" is "I am listening", Russian for "go ahead". Dima is Nagiyev\'s friendly name.'),
    (9, None, '\'What news from the hospital, speak quickly.\' "Novosti" is "news", and it\'s always plural in Russian. "Bol\'nitsa" has "bol\'", pain, inside it. "Govori" is "speak".'),
    (10, None, '\'What? The doctors discovered an aneurysm in him?\' "U nego" is "at him", the "at me" pattern with "him", and "nego" gets its "n" after "u". "Anevrizmu" is the object, with -u.'),
    (11, None, '\'Does that mean this saved his life?\' "Spaslo" is "saved", from the same root as "spasibo" and "spasayesh\'". "Yemu zhizn\'" is "to him life", for "his life".'),
    (12, None, '\'Chef, does that mean nobody died?\' "Nikto ne umer" is "nobody didn\'t die", correct Russian with its double negative. "Umer" is a man\'s "died", and it has no -l.'),
    (13, None, '\'Keep quiet, today you were simply incredibly lucky.\' "Tebe povezlo" is "to you it was lucky": luck happens to a person. "Neveroyatno" is "ne" plus "veroyatno", probable: improbable.'),
]
