# Authoring module for kukhnya-s01e16-scene-13.
ID = 'kukhnya-s01e16-scene-13'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 16
SCENE = 13
TITLE = 'В поисках ключа  (In Search of the Key)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'inspector': 'Инспектор', 'senya': 'Сеня'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.16'
SOURCE_FILE = 'sources/kukhnya/s01/e16.ru.dual.srt'
INTRO = 'Major Lanovsky has been called to the kitchen, and the staff are on edge, because one of the cooks without papers, Fedya, is hiding in the walk-in fridge. Barinov and Senya whisper, and then the inspector arrives and asks for the fridge to be opened. Here is the Russian first.'
OPENER = "Let's go over it slowly."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "The fridge is about to be opened, and Barinov is nowhere near ready. Remember the way the inspector asks politely, with a phrase that literally means 'be kind'. See you next time!"
CLOSING = ('inspector', 'Пока!')
STORY = [
    ('barinov', 'Инспектор здесь.', 'The inspector is here.', [], ''),
    ('senya', 'Я знаю.', 'I know.', [], ''),
    ('barinov', 'Он хочет проверить кухню.', 'He wants to check the kitchen.', [], ''),
    ('senya', 'Пусть проверяет.', 'Let him check.', [], ''),
    ('barinov', 'Он ищет нелегалов.', 'He is looking for illegals.', [], ''),
    ('senya', 'У нас их нет.', 'We do not have them.', [], ''),
    ('barinov', 'Где Федя?', 'Where is Fedya?', [], ''),
    ('senya', 'Он в холодильнике.', 'He is in the fridge.', [], ''),
    ('barinov', 'Отлично.', 'Excellent.', [], ''),
    ('inspector', 'Виктор Петрович, будьте любезны.', 'Viktor Petrovich, would you be so kind.', [(168, 'Виктор Петрович, будьте любезны, откройте, пожалуйста, холодильник.')], ''),
    ('inspector', 'Откройте, пожалуйста, холодильник.', 'Open the fridge, please.', [(168, 'Виктор Петрович, будьте любезны, откройте, пожалуйста, холодильник.')], ''),
    ('inspector', 'Я жду.', 'I am waiting.', [], ''),
]
WALK = [
    (0, None, "'The inspector is here.' There is no 'is' in the Russian. The ending of 'here' has a soft 'zd' sound that is easy to say once you stop worrying about it."),
    (1, None, "'I know.' One word does the work of two, because the ending already says 'I'. It's the shortest possible answer, which suits Senya."),
    (2, None, "'He wants to check the kitchen.' 'Wants' is one of the irregular ones, so the 'he' form looks different from the 'I' form. The kitchen takes a 'u' ending, since it's what gets checked."),
    (3, None, "'Let him check.' The opening word is 'let', and it just goes before the plain 'he checks'. It's a handy little frame for 'let them' or 'may it be'."),
    (4, None, "'He is looking for illegals.' The 'ne' at the front of 'legal' works just like 'un' or 'il' in English, so the word is built in front of your eyes. The 'ov' ending is the plural 'of' form that 'look for' wants."),
    (5, None, "'We don't have them.' Literally 'at us them not'. 'Not' here is the 'there isn't' word, and 'them' comes before it."),
    (6, None, "'Where is Fedya?' The name is a short, friendly one, the kind you'd use for a mate. Again, there's no 'is' in it."),
    (7, None, "'He is in the fridge.' 'In' plus an 'e' ending on the fridge says where he is. Barinov doesn't need to say more, since the fridge is the whole problem."),
    (8, None, "'Excellent.' It's the top mark in a Russian school, a five out of five, so it carries a bit of pride. Here it's said through a gritted smile."),
    (9, None, "'Viktor Petrovich, would you be so kind.' The phrase is literally 'be kind', in the polite plural command. It's what a very formal person says before asking for something."),
    (10, None, "'Open the fridge, please.' The command ends in 'yte', which is the polite way to order someone around. 'Please' is a long, friendly-sounding word, and it also means 'you're welcome'."),
    (11, None, "'I'm waiting.' It's just one word, no 'I', and no 'am'. Three words from the inspector would be more polite, but he says one, and it is more menacing."),
]
