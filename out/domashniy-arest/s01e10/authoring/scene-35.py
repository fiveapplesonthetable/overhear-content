# Authoring module for domashniy-arest-s01e10-scene-35.
ID = 'domashniy-arest-s01e10-scene-35'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 10
SCENE = 35
TITLE = 'Разговор в машине  (Driving with the Captive)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'grisha': 'Дядя Гриша', 'kostik': 'Костик'}
SOURCE_NAME = 'Домашний арест, Сезон 1, Эпизод 10'
SOURCE_FILE = 'sources/domashniy-arest/s01/e10.ru.dual.srt'
INTRO = "Following a chaotic kidnapping in the village, Kostik and Uncle Grisha speed down the road in their captive's car. Trapped inside the speeding vehicle, the two bungling criminals bicker endlessly over driving habits and mutual disrespect."
OPENER = "Let's explore the comical argument between two small-time criminals on the road."
TRANSITION = "Now let's listen to the bickering exchange inside the car from start to finish once more."
OUTRO = 'Kostik focuses on driving while Grisha keeps a watchful eye on their captive. See you next time!'
CLOSING = ('kostik', 'Пока!')
STORY = [
    ('grisha', 'Куда ты так быстро гонишь машину?', 'Where are you driving the car so fast?', [], 'opening setup'),
    ('kostik', 'Я просто хочу скорее доехать.', 'I simply want to arrive faster.', [], "Kostik's excuse"),
    ('grisha', 'Ты всегда создаёшь нам большие проблемы.', 'You always create big problems for us.', [(1034, 'сам ували.')], 'adapted cue'),
    ('kostik', 'Почему ты сразу начинаешь ругаться?', 'Why do you start cursing right away?', [(1035, 'Чего ты в обидки сразу лезешь?')], 'adapted cue'),
    ('kostik', 'Мне надоели твои постоянные упрёки!', 'I am sick of your constant reproaches!', [(1036, 'Потому что надоела тетя Гриша.')], 'adapted cue'),
    ('kostik', 'Каждый день ты повторяешь одно и то же.', 'Every day you repeat the same thing.', [(1037, 'Каждый день одно и то же.')], 'exact cue'),
    ('kostik', 'Ты говоришь, что Костик — глупый человек.', 'You say that Kostik is a foolish person.', [(1038, 'Костик дебил')], 'polite adaptation of cue'),
    ('grisha', 'А разве это не чистая правда?', "And isn't that the pure truth?", [(1039, 'Вот это тебе не понравилось.')], 'adapted cue'),
    ('grisha', 'Ты лучше тормози перед поворотом!', 'You better slow down before the turn!', [(1040, 'А ты тормози!')], 'adapted cue'),
    ('kostik', 'У меня была отличная умная мысль.', 'I had an excellent clever thought.', [(1041, 'А пресс нормальная мысль.')], 'adapted cue'),
    ('grisha', 'Какая у тебя может быть мысль?', 'What thought could you possibly have?', [], "Grisha's skeptical reaction"),
    ('kostik', 'Мы должны напугать нашего пленника.', 'We must frighten our captive.', [(1042, 'Давай доставай.')], 'explanatory adaptation'),
    ('grisha', 'Хватит болтать, смотри на дорогу!', 'Stop chattering, look at the road!', [], "Grisha's order"),
    ('kostik', 'Хорошо, я внимательно слежу за дорогой.', 'Alright, I am watching the road carefully.', [], "Kostik's concession"),
]
WALK = [
    (0, None, "'Where are you driving the car so fast?' After accidentally grabbing agent Sokolov in the dark, they speed off and Grisha yells at the driver."),
    (1, None, "'I simply want to arrive faster.' Rattled by the kidnapping, Kostik has his foot floored on the gas pedal."),
    (2, None, "'You always create big problems for us.' Everything that goes wrong on this job gets blamed on Kostik."),
    (3, None, "'Why do you start cursing right away?' Behind the wheel, the younger crook bristles at being scolded non-stop."),
    (4, None, "'I am sick of your constant reproaches!' Literally \"your constant reproaches have bored me\", as Kostik finally snaps back."),
    (5, None, "'Every day you repeat the same thing.' \"Odno i to zhe\" is the everyday Russian phrase for \"the exact same thing over and over\"."),
    (6, None, "'You say that Kostik is a foolish person.' Referring to himself in the third person shows how wounded his pride is."),
    (7, None, "'And isn't that the pure truth?' Instead of apologizing, Grisha calmly doubles down on the insult."),
    (8, None, "'You better slow down before the turn!' Seeing a sharp bend ahead, Grisha grabs the dashboard."),
    (9, None, "'I had an excellent clever thought.' Still trying to prove he has brains, Kostik pitches his own idea."),
    (10, None, "'What thought could you possibly have?' Grisha's dry reply leaves zero doubt about what he thinks of Kostik's intellect."),
    (11, None, "'We must frighten our captive.' With their prisoner tied up in the car, Kostik wants to play the tough interrogator."),
    (12, None, "'Stop chattering, look at the road!' Right now, not crashing the getaway car comes first."),
    (13, None, "'Alright, I am watching the road carefully.' Muttering to himself, Kostik turns his eyes back to the headlights."),
]
