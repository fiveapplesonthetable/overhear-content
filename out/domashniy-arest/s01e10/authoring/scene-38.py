# Authoring module for domashniy-arest-s01e10-scene-38.
ID = 'domashniy-arest-s01e10-scene-38'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 10
SCENE = 38
TITLE = 'Задержание в лесу  (Singing and Hitting)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'grisha': 'Дядя Гриша', 'kostik': 'Костик', 'lyova': 'Лёва'}
SOURCE_NAME = 'Домашний арест, Сезон 1, Эпизод 10'
SOURCE_FILE = 'sources/domashniy-arest/s01/e10.ru.dual.srt'
INTRO = 'In a remote forest clearing outside Sinyaozersk, Uncle Grisha and Kostik confront their captive hostage Sokolov. When Sokolov desperately claims to be an undercover FSB officer on official duty, Grisha dismisses the threat with scathing mockery.'
OPENER = "Let's examine how the amateur kidnappers react to their hostage's dramatic claims."
TRANSITION = "Now let's listen to the standoff in the forest clearing once more."
OUTRO = 'Uncle Grisha remains utterly convinced that their captive is merely an eccentric impostor. See you next time!'
CLOSING = ('grisha', 'Пока!')
STORY = [
    ('kostik', 'Ты слышал странный хруст в кустах?', 'Did you hear a strange crunch in the bushes?', [(1110, 'Хруст слышал?')], 'adapted cue'),
    ('grisha', 'Это просто пробежала дикая собака.', 'That was just a wild dog running past.', [(1111, 'Да это собака.')], 'adapted cue'),
    ('lyova', 'Вы все немедленно арестованы!', 'You are all immediately under arrest!', [(1120, 'Вы все арестованы')], 'adapted cue'),
    ('lyova', 'Здесь работает Федеральная Служба Безопасности!', 'The Federal Security Service is operating here!', [(1120, 'работает ФСБ.')], 'expanded cue'),
    ('grisha', 'Очень плохо вы работаете, парень.', 'You work very poorly, young man.', [(1121, 'Хреново работает.')], 'polite adaptation of cue'),
    ('lyova', 'Наши секретные сотрудники скоро найдут вас!', 'Our secret operatives will find you soon!', [(1114, 'наши')], 'adapted cue'),
    ('grisha', 'Замолчи и перестань нас пугать.', 'Shut up and stop frightening us.', [(1112, 'замолчи')], 'polite adaptation of cue'),
    ('kostik', 'Дядя Гриша, а вдруг он настоящий офицер?', 'Uncle Grisha, what if he is a real officer?', [(1108, 'гриша')], 'adapted cue'),
    ('grisha', 'Костик, ты снова удивляешь своей глупостью.', 'Kostik, you surprise me again with your foolishness.', [], 'adapted cue'),
    ('grisha', 'Кто возьмёт такого маленького человека туда?', 'Who would take such a small man there?', [], 'adapted cue'),
    ('kostik', 'Но у него есть настоящее удостоверение!', 'But he has a real identification card!', [], 'adapted cue'),
    ('grisha', 'Такую бумажку можно купить в любом переходе.', 'You can buy such a paper in any underpass.', [], 'adapted cue'),
    ('lyova', 'Вы заплатите за это преступление сполна!', 'You will pay in full for this crime!', [], "hostage's warning"),
    ('grisha', 'Сиди тихо и не открывай рот.', 'Sit quietly and do not open your mouth.', [], "Grisha's final command"),
]
WALK = [
    (0, None, "'Did you hear a strange crunch in the bushes?' Kostik gets startled by suspicious forest noises."),
    (1, None, "'That was just a wild dog running past.' Grisha shrugs off the noise with mundane explanations."),
    (2, None, "'You are all immediately under arrest!' Sokolov attempts to establish authority while bound."),
    (3, None, "'The Federal Security Service is operating here!' A formal declaration citing the major security agency."),
    (4, None, "'You work very poorly, young man.' Grisha unimpressed mocks the agent's bungled operation."),
    (5, None, "'Our secret operatives will find you soon!' A threat warning of inevitable law enforcement retribution."),
    (6, None, "'Shut up and stop frightening us.' A command telling the captive to cease empty intimidation."),
    (7, None, "'Uncle Grisha, what if he is a real officer?' Kostik shows naive credulity toward the hostage's words."),
    (8, None, "'Kostik, you surprise me again with your foolishness.' Grisha expresses constant exasperation with his partner."),
    (9, None, "'Who would take such a small man there?' Grisha dismisses the captive based on his unimposing stature."),
    (10, None, "'But he has a real identification card!' Kostik points out the official-looking badge in his possession."),
    (11, None, "'You can buy such a paper in any underpass.' Grisha claims fake identification is easily purchased."),
    (12, None, "'You will pay in full for this crime!' The captive promises severe consequences for their illegal actions."),
    (13, None, "'Sit quietly and do not open your mouth.' A stern command ordering total silence from the captive."),
]
