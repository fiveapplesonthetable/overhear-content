# Authoring module for kukhnya-s01e14-scene-01.
ID = 'kukhnya-s01e14-scene-01'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 14
SCENE = 1
TITLE = 'Утренние игры  (Morning Games)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'max': 'Макс', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.14'
SOURCE_FILE = 'sources/kukhnya/s01/e14.ru.dual.srt'
INTRO = "Welcome to The Kitchen, a comedy about the kitchen of Claude Monet, a smart Moscow restaurant. In this episode, the head chef turns up drunk before an important dinner, and a very nervous Lyova has to take charge. We start earlier, in Vika's flat, where Max wakes up in a playful mood and Vika has a busy day ahead. Here is the scene; you do not need to catch everything."
OPENER = 'Now the same morning, slowly.'
TRANSITION = 'And the whole morning once more.'
OUTRO = "Max goes off to make the coffee, Vika gets ready for work, and the day that's about to get very loud starts quietly. Keep 'until' in your pocket. Bye for now."
CLOSING = ('vika', 'Пока!')
STORY = [
    ('max', 'Вика, ты уже проснулась сегодня?', 'Vika, are you awake already today?', [], ''),
    ('vika', 'Да, я уже давно не сплю.', 'Yes, I have not been sleeping for a long time.', [], ''),
    ('max', 'Почему ты так рано встала?', 'Why did you get up so early?', [], ''),
    ('vika', 'У меня сегодня очень много дел.', 'I have a lot of things today.', [], ''),
    ('max', 'А как же наш вкусный завтрак?', 'And what about our tasty breakfast?', [], ''),
    ('vika', 'Ты можешь приготовить его сам.', 'You can prepare it yourself.', [], ''),
    ('max', 'Сейчас я человек-паук!', 'Now I am Spider-Man!', [(1, 'человек-паук')], 'adapted: cleaned up the crude joke'),
    ('vika', 'Очень смешно, но мне надо идти.', 'Very funny, but I need to go.', [], ''),
    ('max', 'Сейчас я тебя!', 'I am going to get you!', [(2, 'Сейчас я тебя.')], 'adapted: shortened'),
    ('vika', 'Макс, прекрати это немедленно!', 'Max, stop this immediately!', [], ''),
    ('max', 'Хорошо, я иду варить нам кофе.', 'Alright, I am going to brew coffee for us.', [], ''),
    ('vika', 'Пока ты не сходишь в душ.', 'Not until you take a shower.', [(3, 'Пока ты не сходишь в душ.')], ''),
]
WALK = [
    (0, None, ["'Vika, are you awake already today?' The language asks 'have you woken up?', with the past form ", ('max', 'проснулась'), ". It has a feminine ending because the 'you' is a woman."]),
    (1, None, ["'Yes, I have not been sleeping for a long time.' Here we say 'already long I do not sleep'. With ", ('vika', 'давно'), ", meaning 'for a long time', the language keeps the plain present ", ('vika', 'не'), ('vika', 'сплю'), " where English needs 'have been'."]),
    (2, None, ["'Why did you get up so early?' Now we can look at this part: ", ('max', 'встала'), " means 'got up' or 'stood up'. It has a feminine ending since the question is to a woman."]),
    (3, None, ["'I have a lot of things today.' Now we can focus on the dialogue: ", ('vika', 'У'), ('vika', 'меня'), ('vika', 'сегодня'), ('vika', 'очень'), ('vika', 'много'), ('vika', 'дел'), " gives the everyday 'I have got lots to do'. After ", ('vika', 'много'), ", meaning 'a lot', the noun changes form to ", ('vika', 'дел'), '.']),
    (4, None, ["'And what about our tasty breakfast?' Now let's inspect this line: ", ('max', 'А'), ('max', 'как'), ('max', 'же'), " is a handy way to ask 'and what about...?' when you feel let down. Breakfast, ", ('max', 'завтрак'), ', is masculine, so the words ', ('max', 'наш'), ('max', 'вкусный'), ' match it.']),
    (5, None, ["'You can prepare it yourself.' Breakfast is masculine, so 'it' comes out as ", ('vika', 'его'), ", meaning 'him'. The term for yourself, ", ('vika', 'сам'), ', has no ending because a man will do the cooking.']),
    (6, None, ["'Now I am Spider-Man!' Now let's inspect the speech: ", ('max', 'человек'), '-', ('max', 'паук'), " means 'man-spider', joined with a hyphen. There is no 'am' here: the expression is just ", ('max', 'Сейчас'), ('max', 'я'), ('max', 'человек'), '-', ('max', 'паук'), '.']),
    (7, None, ["'Very funny, but I need to go.' Now let's analyze the dialogue: ", ('vika', 'смешно'), " on its own is a full reply meaning 'that is funny'. ", ('vika', 'мне'), ('vika', 'надо'), ('vika', 'идти'), " reads as 'to me it is necessary to go', which is the standard way to say you have to leave."]),
    (8, None, ["'I am going to get you!' There is no verb at all here: just ", ('max', 'Сейчас'), ('max', 'я'), ('max', 'тебя'), " which means 'now I you'. The action is obvious, so it is left out, making the same playful threat as 'I will get you!'."]),
    (9, None, ["'Max, stop this immediately!' Now we can consider the speech: ", ('vika', 'прекрати'), " is the order 'stop it!' to one person. ", ('vika', 'немедленно'), " combines 'not' and 'slowly'."]),
    (10, None, ["'Alright, I am going to brew coffee for us.' People ", ('max', 'варить'), ' coffee, the same cooking-by-boiling action used for soup. ', ('max', 'иду'), ('max', 'варить'), " means 'I am off to make', which puts two verbs together with no 'to' between them."]),
    (11, None, ["'Not until you take a shower.' We will look at the dialogue: ", ('vika', 'Пока'), ' and ', ('vika', 'не'), " together mean 'until', framing the expression as 'while you do not go to the shower'. The negative is not a real 'not'; it is simply part of the pattern."]),
]
