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
INTRO = "Max wakes up in Vika's apartment and tries to be playful, but Vika is focused on her day. Let's listen closely to their exchange in Russian first, and then walk through each line together."
OPENER = "Now let's go back through the exchange around Morning Games line by line and unpack how the Russian works."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Max heads to the shower while Vika prepares for her busy day at the restaurant. Next time you watch the episode, listen for the Russian expressions for 'wake up' and 'today' — you will catch every word right away. See you next time!"
CLOSING = ('vika', 'Пока!')
STORY = [
    ('max', 'Вика, ты уже проснулась сегодня?', 'Vika, are you awake already today?', [], ''),
    ('vika', 'Да, я уже давно не сплю.', 'Yes, I have not been sleeping for a long time.', [], ''),
    ('max', 'Почему ты так рано встала?', 'Why did you get up so early?', [], ''),
    ('vika', 'У меня сегодня очень много дел.', 'I have a lot of things today.', [], ''),
    ('max', 'А как же наш вкусный завтрак?', 'And what about our tasty breakfast?', [], ''),
    ('vika', 'Ты можешь приготовить его сам.', 'You can prepare it yourself.', [], ''),
    ('vika', 'И Макс, я озабоченный человек-паук.', 'And Max, I am a horny Spider-Man.', [(1, 'И Макс, я озабоченный человек-паук.')], ''),
    ('vika', 'Очень смешно, но мне надо идти.', 'Very funny, but I need to go.', [], ''),
    ('max', 'Сейчас я тебя. Какой я тебя?', 'I will get you now. What am I getting you?', [(2, 'Сейчас я тебя. Какой я тебя?')], ''),
    ('vika', 'Макс, прекрати это немедленно!', 'Max, stop this immediately!', [], ''),
    ('max', 'Хорошо, я иду варить нам кофе.', 'Alright, I am going to brew coffee for us.', [], ''),
    ('vika', 'Пока ты не сходишь в душ.', 'Before you go take a shower.', [(3, 'Пока ты не сходишь в душ.')], ''),
]
WALK = [
    (0, None, "'Vika, are you awake already today?' Max asks Vika playfully if she is up. He tries to start the morning with a joke."),
    (1, None, "'Yes, I have not been sleeping for a long time.' Vika shuts him down quickly. She informs him she has been awake for a while."),
    (2, None, "'Why did you get up so early?' Max wonders why she is up so early. He still wants to relax in bed."),
    (3, None, "'I have a lot of things today.' Vika explains she is very busy today. She does not have time for games."),
    (4, None, "'And what about our tasty breakfast?' Max tries to tempt her with breakfast. He hopes food will change her mind."),
    (5, None, "'You can prepare it yourself.' Vika tells him to make it himself. She is completely focused on getting ready."),
    (6, None, "'And Max, I am a horny Spider-Man.' Vika makes a silly joke about being spider-man. He is trying his best to charm her."),
    (7, None, "'Very funny, but I need to go.' Vika is not amused. She calls it funny but insists she has to leave."),
    (8, None, "'I will get you now. What am I getting you?' Max playfully threatens to grab her. He pretends to be a monster."),
    (9, None, "'Max, stop this immediately!' Vika commands him to stop. She tells him to quit playing around right now."),
    (10, None, "'Alright, I am going to brew coffee for us.' Max finally gives up. He agrees to go make coffee for them both."),
    (11, None, "'Before you go take a shower.' Vika gives him a strict condition. She tells him to take a shower first."),
]
