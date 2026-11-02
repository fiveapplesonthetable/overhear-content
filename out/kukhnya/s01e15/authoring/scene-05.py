# Authoring module for kukhnya-s01e15-scene-05.
ID = 'kukhnya-s01e15-scene-05'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 15
SCENE = 5
TITLE = 'Утренние сборы  (Morning Preparations)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'max': 'Макс', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.15'
SOURCE_FILE = 'sources/kukhnya/s01/e15.ru.dual.srt'
INTRO = "It's the early hours, and Max is slipping out of Vika's bed to go home and change before work. She wants him to stay a little longer. Here's how it sounds in Russian."
OPENER = "Now we go back through it slowly."
TRANSITION = 'Now the scene in one go.'
OUTRO = "Vika has put a big question to Max, and he has to think about it. Talk soon."
CLOSING = ('vika', 'Пока!')
STORY = [
    ('vika', 'Ну ты куда?', 'Where are you going?', [(25, 'Ну ты куда?')], ''),
    ('max', 'Мне пора.', 'I have to go.', [], ''),
    ('vika', 'Останься со мной ещё на одну минуту.', 'Stay with me for one more minute.', [], ''),
    ('max', 'Я не могу, я очень сильно спешу.', 'I cannot, I am rushing very much.', [], ''),
    ('vika', 'У тебя опять очень много важных дел?', 'Do you again have many important things?', [], ''),
    ('max', 'Надо заехать домой, принять душ, переодеться.', 'I need to stop by home, take a shower, change.', [], ''),
    ('vika', 'Слушай, тебе не надоело?', 'Listen, are you not tired of this?', [], ''),
    ('max', 'А что именно мне надоело?', 'And what exactly am I fed up with?', [(29, 'Что?')], 'adapted: Max turns her question round'),
    ('vika', 'Спать здесь, а принимать душ далеко отсюда.', 'Sleeping here, but taking a shower far from here.', [], ''),
    ('max', 'Да, это занимает очень много моего времени.', 'Yes, it takes a lot of my time.', [], ''),
    ('vika', 'Тогда зачем ты это делаешь каждый день?', 'Then why do you do this every day?', [], ''),
    ('max', 'Потому что там лежат все мои вещи.', 'Because all my things lie there.', [], ''),
    ('vika', 'Может быть, ты ко мне переедешь?', 'Maybe you should move in with me?', [], ''),
]
WALK = [
    (0, None, ["'Where are you going?' Let's analyze the sentence: ", ('vika', 'ты'), ('vika', 'куда'), ' is you where to, with no action word at all. In Russian the movement is understood.']),
    (1, None, ["'I have to go.' Just two words, ", ('max', 'Мне'), ('max', 'пора'), ', to me time. It is the standard way to say you must leave.']),
    (2, None, ["'Stay with me for one more minute.' We will consider the phrase: ", ('vika', 'Останься'), ' ends in a bit that means stay yourself. ', ('vika', 'на'), ('vika', 'одну'), ('vika', 'минуту'), ' uses the term for onto for a stretch of time, and one minute changes ending after it.']),
    (3, None, ["'I cannot, I am rushing very much.' Russian turns up the volume with ", ('max', 'очень'), ('max', 'сильно'), ', meaning very strongly, where English would just say in a real hurry. ', ('max', 'спешу'), ' is the I form of to hurry.']),
    (4, None, ["'Do you again have many important things?' Now let's examine the words: ", ('vika', 'дел'), ' is of affairs, so many important affairs ends in plural of forms. ', ('vika', 'У'), ('vika', 'тебя'), ' is at you, which she uses for do you have.']),
    (5, None, ["'I need to stop by home, take a shower, change.' Russians accept a shower, ", ('max', 'принять'), ('max', 'душ'), ', where English says take. ', ('max', 'переодеться'), ' is dress again, that is, change clothes.']),
    (6, None, ["'Listen, are you not tired of this?' Now we can analyze the dialogue: ", ('vika', 'тебе'), ('vika', 'не'), ('vika', 'надоело'), ' means to you has it not got boring. It is how Russians ask if you are fed up with this.']),
    (7, None, ["'And what exactly am I fed up with?' Max turns her question round. ", ('max', 'надоело'), ' keeps that same action word she used, and again the person who is fed up is ', ('max', 'мне'), ', to me.']),
    (8, None, ["'Sleeping here, but taking a shower far from here.' Vika uses no you at all: ", ('vika', 'Спать'), ' and ', ('vika', 'принимать'), ' stay in their basic form, like to sleep here, to shower there. ', ('vika', 'отсюда'), ' is from here.']),
    (9, None, ["'Yes, it takes a lot of my time.' Let's look at the speech: ", ('max', 'занимает'), ' means occupies, so the thing takes up your time. ', ('max', 'моего'), ('max', 'времени'), ' is of my time, with a matching ending.']),
    (10, None, ["'Then why do you do this every day?' Now we can consider the words: ", ('vika', 'зачем'), ' is what for, asking about the purpose. ', ('vika', 'каждый'), ('vika', 'день'), ', every day, needs no little word in front, unlike English on.']),
    (11, None, ["'Because all my things lie there.' Things lie, ", ('max', 'лежат'), ', in a place, as in the flat. Max gives a plain reason, which is the joke.']),
    (12, None, ["'Maybe you should move in with me?' We will inspect the speech: ", ('vika', 'Может'), ('vika', 'быть'), ' reads can be, so maybe. The term for to becomes ', ('vika', 'ко'), ' before ', ('vika', 'мне'), ', to make it easier to say. ', ('vika', 'переедешь'), ' reuses the same move in word as in the first scene.']),
]
