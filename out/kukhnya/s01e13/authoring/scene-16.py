# Authoring module for kukhnya-s01e13-scene-16.
ID = 'kukhnya-s01e13-scene-16'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 13
SCENE = 16
TITLE = 'Утро после клуба  (The Morning After the Club)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'max': 'Макс', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.13'
SOURCE_FILE = 'sources/kukhnya/s01/e13.ru.dual.srt'
INTRO = "Vika wakes up in a flat she doesn't know and quickly works out whose it is. Max has an explanation, and she doesn't like it. Listen to it in Russian before we pick it apart."
OPENER = 'The morning-after argument again, one line at a time.'
TRANSITION = 'Now the argument in full.'
OUTRO = "Vika wants out, and Max points her to the chair. Notice how the verb for lies is used for anything left on a table or a chair. Catch you next time."
CLOSING = ('vika', 'Пока!')
STORY = [
    ('vika', 'Где я нахожусь? Что это такое?', 'Where am I? What is this?', [(221, 'где я?')], ''),
    ('vika', 'Ты опять затащил меня сюда?', 'Did you drag me here again?', [(222, 'меня опять')], 'adapted: kept the drag, dropped the bed'),
    ('max', 'Конечно, связал и принёс сюда сам.', 'Of course, tied you up and brought you here myself.', [(223, 'Насильно связал и затащил')], ''),
    ('vika', 'Не смейся надо мной, говори правду.', 'Do not laugh at me, tell the truth.', [], ''),
    ('max', 'Ты сама позвонила мне ночью из клуба.', 'You called me yourself at night from the club.', [(224, 'Ты что, не помнишь, что мне сама позвонила?')], ''),
    ('vika', 'Я не могла сделать такую глупость.', 'I could not do such a foolish thing.', [], ''),
    ('max', 'Ты плакала в трубку в три часа.', "You were crying into the phone at three o'clock.", [(226, 'Как я могу спать 3 часа ночи?')], ''),
    ('vika', 'Что я тебе тогда говорила, Макс?', 'What was I telling you then, Max?', [], ''),
    ('max', 'Ты очень просила забрать тебя домой.', 'You were begging me to take you home.', [], ''),
    ('vika', 'Ты просто воспользовался моей минутной слабостью.', 'You simply took advantage of my momentary weakness.', [(216, 'просто')], ''),
    ('max', 'Я просто спас тебя от неприятностей.', 'I simply saved you from trouble.', [], ''),
    ('vika', 'Мне нужно срочно уйти отсюда, Макс.', 'I need to leave here urgently, Max.', [], ''),
    ('max', 'Твоя одежда лежит на том стуле.', 'Your clothes are lying on that chair.', [], ''),
]
WALK = [
    (0, None, ["'Where am I? What is this?' Vika asks ", ('vika', 'нахожусь'), ', which is the usual Russian expression for finding yourself somewhere. The extra word ', ('vika', 'такое'), ' makes the second question urgent.']),
    (1, None, ["'Did you drag me here again?' The prefix on ", ('vika', 'затащил'), ' adds the feel of pulling someone in. Here we see the direction kind of here, ', ('vika', 'сюда'), ', meaning to here.']),
    (2, None, ["'Of course, tied you up and brought you here myself.' It is obviously a joke. Tied up is ", ('max', 'связал'), ", and myself, in a man's form, is ", ('max', 'сам'), '. Carried here is ', ('max', 'принёс'), '.']),
    (3, None, ["'Do not laugh at me, tell the truth.' Russians laugh over somebody, so the wording is ", ('vika', 'надо'), ('vika', 'мной'), ', and the ending on ', ('vika', 'смейся'), ' makes it laugh oneself. Truth, ', ('vika', 'правду'), ', changes form as the thing being told.']),
    (4, None, ["'You called me yourself at night from the club.' In Russian a woman's verb takes an extra ending, so ", ('max', 'позвонила'), ' tells you Vika is the caller. At night, ', ('max', 'ночью'), ', comes from night.']),
    (5, None, ["'I could not do such a foolish thing.' A foolish thing is ", ('vika', 'глупость'), ', from foolish, so ', ('vika', 'такую'), ('vika', 'глупость'), ' says such a stupidity. ', ('vika', 'могла'), ' ends with an extra sound for a woman.']),
    (6, None, ["'You were crying into the phone at three o'clock.' Russian says into the receiver, since ", ('max', 'трубку'), " means pipe, and a phone used to look like one. At three o'clock is ", ('max', 'в'), ('max', 'три'), ('max', 'часа'), ': after three, hour becomes ', ('max', 'часа'), '.']),
    (7, None, ["'What was I telling you then, Max?' The verb ", ('vika', 'говорила'), " has a woman's ending, and it means was saying. Then is ", ('vika', 'тогда'), ', and to you is ', ('vika', 'тебе'), '.']),
    (8, None, ["'You were begging me to take you home.' Russians use ", ('max', 'просила'), ' for begging. To pick up is ', ('max', 'забрать'), ', and homewards is ', ('max', 'домой'), '.']),
    (9, None, ["'You simply took advantage of my momentary weakness.' Used is ", ('vika', 'воспользовался'), '. Of a minute is ', ('vika', 'минутной'), ', meaning momentary. Weakness, ', ('vika', 'слабость'), ', comes from weak.']),
    (10, None, ["'I simply saved you from trouble.' Trouble, ", ('max', 'неприятностей'), ', is the opposite of pleasant, so it means an unpleasantness. Here it is plural.']),
    (11, None, ["'I need to leave here urgently, Max.' Need happens to you in Russian, so ", ('vika', 'Мне'), ('vika', 'нужно'), ' means to me it is needed. The verb ', ('vika', 'уйти'), ' starts with the prefix for away.']),
    (12, None, ["'Your clothes are lying on that chair.' Russians use lies, ", ('max', 'лежит'), ', for things on flat surfaces, where English says is. On that chair is ', ('max', 'на'), ('max', 'том'), ('max', 'стуле'), ', and clothes, ', ('max', 'одежда'), ', is always singular.']),
]
