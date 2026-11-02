# Authoring module for kukhnya-s01e15-scene-17.
ID = 'kukhnya-s01e15-scene-17'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 15
SCENE = 17
TITLE = 'Желание переехать  (Desire to Move In)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'max': 'Макс', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.15'
SOURCE_FILE = 'sources/kukhnya/s01/e15.ru.dual.srt'
INTRO = "Max has made up his mind, and he arrives at Vika's flat. He wants to move in with her, and he has trouble saying why. Hear it in Russian first."
OPENER = 'Slowly, once more.'
TRANSITION = 'Now the scene in one go.'
OUTRO = "Max has finally said what he wants. Vika's answer comes next."
CLOSING = ('vika', 'Пока!')
STORY = [
    ('vika', 'Привет, Макс.', 'Hi, Max.', [(335, 'Привет.')], ''),
    ('max', 'Привет.', 'Hi.', [(335, 'Привет.')], ''),
    ('max', 'Я хочу переехать к тебе.', 'I want to move to your place.', [(336, 'Я хочу переехать к тебе.')], ''),
    ('vika', 'Тебе негде жить?', 'Do you have nowhere to live?', [(337, 'Что, негде жить?')], ''),
    ('max', 'Нет, у меня миллион вариантов.', 'No, I have a million options.', [(337, 'Да нет, просто...'), (338, 'Да миллион вариантов.')], ''),
    ('max', 'Костя зовёт меня назад.', 'Kostya is calling me back.', [(338, 'Просто Костя назад зовет,')], ''),
    ('max', 'Лёва тоже приглашает жить.', 'Leva is also inviting me to live.', [(338, 'Лёва тоже приглашает,')], ''),
    ('max', 'Но я готов жить с тобой.', 'But I am ready to live with you.', [(339, 'Но я готов жить с тобой.')], ''),
    ('vika', 'Что ты хочешь сказать?', 'What do you want to say?', [], ''),
    ('max', 'Я хочу жить с тобой.', 'I want to live with you.', [(340, 'В смысле, хочу.')], ''),
    ('max', 'Я не хочу быть без тебя.', 'I do not want to be without you.', [(341, 'В смысле, не хочу без тебя.')], ''),
    ('vika', 'Это очень приятно слышать.', 'That is very pleasant to hear.', [], ''),
    ('max', 'Правда?', 'Really?', [], ''),
    ('vika', 'Да, я тебе верю.', 'Yes, I believe you.', [], ''),
]
WALK = [
    (0, None, ["'Hi, Max.' Let us analyze the dialogue: ", ('vika', 'Привет'), ' marks the casual hello, and it is what Russians say to friends. She adds his name.']),
    (1, None, ["'Hi.' Max answers with the same word. Russians usually return ", ('max', 'Привет'), ' with the same greeting.']),
    (2, None, ["'I want to move to your place.' The expression ", ('max', 'к'), ('max', 'тебе'), ' is how Russian says to your place, and ', ('max', 'переехать'), ' means to move house.']),
    (3, None, ["'Do you have nowhere to live?' Now we can focus on this part: ", ('vika', 'негде'), ' means there is nowhere. Add ', ('vika', 'жить'), ' and you have nowhere to live, with no you or have needed.']),
    (4, None, ["'No, I have a million options.' The word ", ('max', 'миллион'), ' stays the same, and the thing counted takes a matching ending in ', ('max', 'вариантов'), '. Notice ', ('max', 'у'), ('max', 'меня'), ' means at me.']),
    (5, None, ["'Kostya is calling me back.' The verb ", ('max', 'зовёт'), ' means calls, in the sense of calling someone to come. The term ', ('max', 'назад'), ' means back, and ', ('max', 'меня'), ' is me.']),
    (6, None, ["'Leva is also inviting me to live.' The word ", ('max', 'приглашает'), ' means invites, followed by ', ('max', 'жить'), ' in its basic shape. The word ', ('max', 'тоже'), ' means also.']),
    (7, None, ["'But I am ready to live with you.' We can inspect the sentence: ", ('max', 'готов'), " means ready with no ending, which is the man's form. We hear ", ('max', 'жить'), ('max', 'с'), ('max', 'тобой'), ' follows directly.']),
    (8, None, ["'What do you want to say?' She asks him directly. It is how to ask what are you getting at in Russian."]),
    (9, None, ["'I want to live with you.' The expression ", ('max', 'Я'), ('max', 'хочу'), ('max', 'жить'), ('max', 'с'), ('max', 'тобой'), ' puts want, to live, and with you together.']),
    (10, None, ["'I do not want to be without you.' Now let's inspect this line: ", ('max', 'без'), ('max', 'тебя'), ' means without you. The verb ', ('max', 'быть'), ' means to be.']),
    (11, None, ["'That is very pleasant to hear.' The term ", ('vika', 'приятно'), ' means pleasant, and Russian needs no is here. The verb ', ('vika', 'слышать'), ' means to hear.']),
    (12, None, ["'Really?' This single word ", ('max', 'Правда'), ' is the same as truth. Max can hardly believe it.']),
    (13, None, ["'Yes, I believe you.' Now we can look at this part: ", ('vika', 'тебе'), ('vika', 'верю'), ' puts you in a to form, since in Russian you believe to somebody.']),
]
