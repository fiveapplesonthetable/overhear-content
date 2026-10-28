# Authoring module for domashniy-arest-s01e12-scene-02.
ID = 'domashniy-arest-s01e12-scene-02'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 12
SCENE = 2
TITLE = 'Нападение на обитель  (Attack on the Monastery)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'grigory': 'Отец Григорий', 'kostik': 'Костик'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.12'
SOURCE_FILE = 'sources/domashniy-arest/s01/e12.ru.dual.srt'
INTRO = "Suddenly, alarms echo through the monastery courtyard as enemy invaders break through the gates. Monk Konstantin urges Father Grigory to flee, but Father Grigory knows time has run out. He orders Konstantin to take the precious handwritten chronicle and hide it safely in the cellar. Let's listen to their tense exchange in Russian first."
OPENER = "Now let's examine Father Grigory and Konstantin's escape conversation line by line."
TRANSITION = "Now let's listen to the monastery attack scene again without interruption."
OUTRO = 'Konstantin runs to hide the priceless chronicle deep underground. See you next time!'
CLOSING = ('kostik', 'Пока!')
STORY = [
    ('kostik', 'Господи, Иисусе Христе, спаси нас!', 'Lord Jesus Christ, save us!', [(29, 'Господи, судьи Христи')], 'adapted'),
    ('kostik', 'Отец Григорий, нам надо бежать!', 'Father Grigory, we must run!', [(30, 'Бежим, отец Григорий, бежим')], ''),
    ('grigory', 'Куда же нам теперь бежать?', 'Where can we run now?', [(31, 'Куда игра')], 'adapted'),
    ('kostik', 'Враги уже ворвались в монастырь!', 'The enemies have already broken into the monastery!', [], 'new'),
    ('grigory', 'Мы уже никуда не убежим.', "We won't escape anywhere now.", [], 'adapted'),
    ('kostik', 'Они поджигают наши деревянные стены!', 'They are setting our wooden walls on fire!', [], 'adapted'),
    ('grigory', 'Спасай скорее священную книгу!', 'Save the sacred book quickly!', [], 'adapted'),
    ('kostik', 'А как же вы, отец Григорий?', 'And what about you, Father Grigory?', [(30, 'отец')], ''),
    ('grigory', 'Обо мне не думай сейчас.', "Don't think about me right now.", [], 'new'),
    ('grigory', 'Иди немедленно и прячь летопись!', 'Go immediately and hide the chronicle!', [], 'adapted'),
    ('kostik', 'Я спрячу её в каменном подвале!', 'I will hide it in the stone cellar!', [], 'new'),
    ('grigory', 'Сохрани память для наших потомков!', 'Preserve the memory for our descendants!', [], 'adapted'),
    ('kostik', 'Я сберегу эту книгу навсегда!', 'I will save this book forever!', [], 'new'),
]
WALK = [
    (0, None, "'Lord Jesus Christ, save us!' The quiet scriptorium is shattered by screams outside, and Konstantin's first instinct is a frantic prayer."),
    (1, None, "'Father Grigory, we must run!' Panic takes over as the young monk tries to pull his frail mentor toward the door."),
    (2, None, "'Where can we run now?' Old and realistic, Grigory hears the raiders in the courtyard and knows the gates are already lost."),
    (3, None, '\'The enemies have already broken into the monastery!\' The Russian word for "broken in" paints a violent picture of attackers storming through the doors.'),
    (4, None, '\'We won\'t escape anywhere now.\' Russian stacks the negatives here—"nowhere" and "not" together—making the elder\'s resignation sound final.'),
    (5, None, "'They are setting our wooden walls on fire!' Through the window he sees the torches go up against the timber fortifications."),
    (6, None, "'Save the sacred book quickly!' If the monks cannot survive, the chronicle they spent their lives copying has to."),
    (7, None, '\'And what about you, Father Grigory?\' Even in terror, Konstantin cannot bear the thought of leaving his teacher behind. "A kak zhe" is how Russians ask "but what about...?" when someone is being forgotten.'),
    (8, None, '\'Don\'t think about me right now.\' Putting "about me" at the very start of the sentence lets Grigory brush his own life aside.'),
    (9, None, "'Go immediately and hide the chronicle!' There is no time for tears or goodbyes; the elder barks two short orders to get him moving."),
    (10, None, "'I will hide it in the stone cellar!' Wooden walls burn, so the underground stone vault is the one place the manuscript might survive."),
    (11, None, "'Preserve the memory for our descendants!' Grigory sees eight centuries ahead: without this book, no one will know their monastery ever stood."),
    (12, None, "'I will save this book forever!' Clutching the heavy parchment to his chest, Konstantin gives his mentor a parting vow."),
]
