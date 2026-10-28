# Authoring module for kukhnya-s01e18-scene-12.
ID = 'kukhnya-s01e18-scene-12'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 18
SCENE = 12
TITLE = 'Умная и красивая  (Smart and Beautiful)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'nagiyev': 'Нагиев', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.18'
SOURCE_FILE = 'sources/kukhnya/s01/e18.ru.dual.srt'
INTRO = 'Nagiyev has just announced that his wife Kristina will run the restaurant. Barinov asks what he means, and Nagiyev lists her qualifications, which turn out to include working there for a year. Listen for how short that list is.'
OPENER = 'Now the list of qualifications, one by one.'
TRANSITION = "Here's the whole introduction again, straight through."
OUTRO = 'The staff greet their new boss, though not warmly. Keep "upravlenie", management, from "upravlyat", to run. See you next time!'
CLOSING = ('nagiyev', 'Всего хорошего!')
STORY = [
    ('barinov', 'В смысле?', 'What do you mean?', [(254, 'смысле?')], ''),
    ('nagiyev', 'Ну, в прямом смысле.', 'Well, in the literal sense.', [(255, 'Ну, в прямом')], ''),
    ('nagiyev', 'Она умная и красивая.', 'She is smart and beautiful.', [(255, 'Она умная, красивая')], ''),
    ('barinov', 'Но это ведь сложная работа.', 'But this is difficult work.', [], ''),
    ('nagiyev', 'Она изучала управление ресторанами.', 'She studied restaurant management.', [(256, 'по управлению ресторанами')], ''),
    ('nagiyev', 'А потом она здесь работала.', 'And then she worked here.', [(257, 'Потом она здесь работала')], ''),
    ('max', 'Она работала в нашем ресторане?', 'Did she work in our restaurant?', [(257, 'она здесь работала')], ''),
    ('nagiyev', 'Да, она работала здесь целый год.', 'Yes, she worked here for a whole year.', [(258, 'Целый год')], ''),
    ('barinov', 'Да, я хорошо помню это время.', 'Yes, I remember that time well.', [], ''),
    ('nagiyev', 'В общем, прошу любить и жаловать.', 'In short, please welcome and respect her.', [(259, 'В общем, прошу любить и жаловать')], ''),
    ('nagiyev', 'Вот ваше новое начальство.', 'Here is your new boss.', [(260, 'Ваше новое начальство')], ''),
    ('barinov', 'Ну, добро пожаловать, Кристина.', 'Well, welcome, Kristina.', [], ''),
]
WALK = [
    (0, None, '\'What do you mean?\' "V smysle?", \'in the sense?\', is how Russians ask you to explain yourself.'),
    (1, None, '\'Well, literally.\' "V pryamom smysle", \'in the direct sense\'. "Pryamoy" also means straight.'),
    (2, None, '\'She\'s smart and beautiful.\' "Umnaya" and "krasivaya" both end in "-aya", for a woman.'),
    (3, None, '\'But it\'s a hard job, isn\'t it?\' "Ved" pushes for agreement: \'you know it is\'. "Rabota", work, is feminine, so hard is "slozhnaya".'),
    (4, None, '\'She studied restaurant management.\' "Upravlenie", management, is "upravlyat", to run, turned into a thing. "Restoranami", of restaurants, keeps the \'by\' form that "upravlyat" asks for.'),
    (5, None, '\'And then she worked here.\' "Rabotala", she worked: the "-la" on the end says a woman did it.'),
    (6, None, '\'She worked in our restaurant?\' "V nashem restorane": after "v", in, both words shift, "nash" to "nashem", "restoran" to "restorane".'),
    (7, None, '\'Yes, she worked here a whole year.\' "Tselyy god", a whole year. Russian needs no word for \'for\' with a stretch of time.'),
    (8, None, '\'Yes, I remember that time well.\' "Vremya", time, looks feminine but is neuter, so \'that\' is "eto".'),
    (9, None, '\'Anyway, please make her welcome.\' "Proshu lyubit i zhalovat", \'I ask you to love and favour\', is a set phrase for introducing someone new.'),
    (10, None, '\'Here\'s your new boss.\' "Nachalstvo" means the bosses, the management, as one neuter word, so new is "novoe". "Vashe", your, speaks to the whole staff.'),
    (11, None, '\'Well, welcome, Kristina.\' "Dobro pozhalovat" is the fixed welcome. The "nu" in front makes it sound reluctant.'),
]
