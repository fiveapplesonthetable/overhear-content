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
INTRO = "Welcome to Kukhnya, a comedy about the kitchen of Claude Monet, a smart Moscow restaurant. In this episode, the head chef turns up drunk before an important dinner, and a very nervous Lyova has to take charge. We start earlier, in Vika's flat, where Max wakes up in a playful mood and Vika has a busy day to get through. First in Russian, and you don't need to catch everything."
OPENER = 'Now the same scene, slowly, a line at a time.'
TRANSITION = 'And the whole morning once more.'
OUTRO = 'Max goes off to make the coffee, and Vika goes off to work. It is a quiet start to a day that is going to get very loud. Until next time.'
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
    ('vika', 'Пока ты не сходишь в душ.', 'Before you go take a shower.', [(3, 'Пока ты не сходишь в душ.')], ''),
]
WALK = [
    (0, None, "'Vika, are you awake already today?' English asks 'are you awake', but Russian asks 'have you woken up', and uses a past form for it. The 'las' on the end shows Vika is a woman."),
    (1, None, "'Yes, I have not been sleeping for a long time.' Literally, 'for a long time I don't sleep'. A plain present covers what English needs 'have been' for, and 'davno' carries the 'long time'."),
    (2, None, "'Why did you get up so early?' Getting up is literally 'standing up', built on the verb 'to stand'. 'Rano' is early."),
    (3, None, "'I have a lot of things today.' 'Del' is 'of things' or 'of affairs', which is the plural of 'delo' with the ending chopped off. It follows 'many', as Russian puts the counted thing in a special shape."),
    (4, None, "'And what about our tasty breakfast?' 'A kak zhe' is a handy opener for 'what about...?' when you suddenly remember something. 'Zavtrak' is masculine, so 'tasty' ends in 'y'."),
    (5, None, "'You can prepare it yourself.' In Russian a breakfast is a 'he', so the 'it' comes out as 'him'. You hear 'cook him yourself', which is odd to English ears."),
    (6, None, "'Now I am Spider-Man!' 'Chelovek-pauk' is literally 'man-spider', with a hyphen. There's no 'am' in the sentence. 'Seychas' means 'now', and Max shouts it."),
    (7, None, "'Very funny, but I need to go.' 'Smeshno' is 'funny', with no 'is' and no 'it'. 'Mne nado' is 'to me it's necessary', and 'idti' is 'to go on foot'."),
    (8, None, "'I am going to get you!' The sentence has no action word: 'seychas ya tebya', literally 'now I you'. Russians leave out the verb when a threat is obvious, like English 'I'll get you!'."),
    (9, None, "'Max, stop this immediately!' Vika's order is the friendly kind, but 'nemedlenno' is formal, literally 'without delay'. The mix of the two makes it sound firm."),
    (10, None, "'Alright, I am going to brew coffee for us.' Russians boil their coffee, so the word they use is 'varit'. Put 'I go' in front and you have 'I'm off to make some'."),
    (11, None, "'Before you go take a shower.' 'Poka ty ne skhodish' is literally 'until you don't go', with a 'ne' that English would never add. Russian often puts 'ne' into time clauses like this."),
]
