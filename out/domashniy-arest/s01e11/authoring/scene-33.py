# Authoring module for domashniy-arest-s01e11-scene-33.
ID = 'domashniy-arest-s01e11-scene-33'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 11
SCENE = 33
TITLE = 'Пьяный командир  (Eduard Looks for Marina)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'dean': 'Эдуард Владимирович', 'klavdia': 'Клавдия Викторовна', 'marina': 'Марина'}
SOURCE_NAME = 'Домашний арест, Сезон 1, Эпизод 11'
SOURCE_FILE = 'sources/domashniy-arest/s01/e11.ru.dual.srt'
INTRO = 'Inebriated and distraught over his fractured operation, FSB officer Eduard Valentinovich stumbles into the communal apartment corridor in search of Marina. Neighbor Klavdiya spitefully informs him that Marina is occupied with Arkady, sparking an emotional outburst.'
OPENER = "Let's explore the pathetic scene as the drunken commander confronts Marina."
TRANSITION = "Now let's listen to the drunken confrontation in the apartment corridor once more."
OUTRO = 'Eduard staggers away humiliated, while Marina stands firm in her newfound independence. See you next time!'
CLOSING = ('dean', 'Пока!')
STORY = [
    ('dean', 'Мариночка, открой скорее дверь!', 'Marinochka, open the door quickly!', [], 'adapted cue'),
    ('klavdia', 'Она сейчас сидит в туалете.', 'She is in the bathroom right now.', [(991, 'Она в туалете.')], 'exact cue'),
    ('klavdia', 'Она сидит там с Аркашкой.', 'She is sitting there with Arkashka.', [(992, 'С Аркашкой.')], 'adapted cue'),
    ('dean', 'Ой, как это трогательно!', 'Oh, how touching that is!', [], 'adapted cue'),
    ('marina', 'Эдик, ты опять пьяный пришёл?', 'Edik, did you come drunk again?', [], 'adapted cue'),
    ('marina', 'Иди скорее к себе домой.', 'Go to your home right away.', [], 'adapted cue'),
    ('dean', 'Я же долго воспитывал тебя!', 'I raised you for a long time!', [], 'adapted cue'),
    ('dean', 'Я обучал тебя буквально всему.', 'I taught you literally everything.', [], 'adapted cue'),
    ('marina', 'Перестань кричать на весь коридор.', 'Stop shouting across the whole hallway.', [], "Marina's rebuke"),
    ('dean', 'А ты оказалась неблагодарной женщиной!', 'And you turned out to be an ungrateful woman!', [], 'polite adaptation of cue'),
    ('marina', 'Я больше не буду работать на вас.', 'I will not work for you anymore.', [], "Marina's declaration"),
    ('dean', 'Ты разбила моё верное сердце!', 'You broke my faithful heart!', [], "Eduard's lament"),
    ('klavdia', 'Хватит шуметь, иди проспись, командир.', 'Enough making noise, go sleep it off, commander.', [], "Klavdiya's intervention"),
    ('dean', 'Я всё равно не забуду эту обиду.', 'I will not forget this insult anyway.', [], "Eduard's parting grudge"),
]
WALK = [
    (0, None, "'Marinochka, open the door quickly!' Drunk and sentimental, Eduard pounds on the door and uses the sweet nickname \"Marinochka\"."),
    (1, None, "'She is in the bathroom right now.' Klavdiya is only too happy to report where Marina is."),
    (2, None, "'She is sitting there with Arkashka.' Tossing in \"with Arkashka\" is pure neighborly mischief, designed to make Eduard explode."),
    (3, None, "'Oh, how touching that is!' Dripping with sarcasm, the jealous colonel tries to pretend he is amused."),
    (4, None, "'Edik, did you come drunk again?' Marina steps out and sizes him up in one glance."),
    (5, None, "'Go to your home right away.' She treats her former handler like an embarrassing guest who needs to leave."),
    (6, None, "'I raised you for a long time!' In his drunken self-pity, he talks as if he had raised her from childhood rather than recruited her."),
    (7, None, "'I taught you literally everything.' Every surveillance trick and career move she knows, he claims as his own creation."),
    (8, None, "'Stop shouting across the whole hallway.' In a communal apartment, a corridor shouting match brings every neighbor to their keyhole."),
    (9, None, "'And you turned out to be an ungrateful woman!' Behind the spy chief's bluster is a jilted man whose pride is hurt."),
    (10, None, "'I will not work for you anymore.' Switching to the cold formal \"vy\", she cuts her ties with him and the agency for good."),
    (11, None, "'You broke my faithful heart!' Hearing a hardened FSB officer complain about his \"faithful heart\" is comedy gold."),
    (12, None, "'Enough making noise, go sleep it off, commander.' Klavdiya has zero fear of the secret police when someone is making noise in her hallway."),
    (13, None, "'I will not forget this insult anyway.' Nursing his wounded ego, Eduard stumbles toward the exit."),
]
