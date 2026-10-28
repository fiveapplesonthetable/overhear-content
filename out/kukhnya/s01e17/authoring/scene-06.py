# Authoring module for kukhnya-s01e17-scene-06.
ID = 'kukhnya-s01e17-scene-06'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 17
SCENE = 6
TITLE = 'Двойное свидание  (Double date)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'max': 'Макс', 'nastya': 'Настя', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.17'
SOURCE_FILE = 'sources/kukhnya/s01/e17.ru.dual.srt'
INTRO = 'After a long day, Vika is in a lousy mood, and Max takes her to a bar to cheer her up. There they meet his friends Kostya and Nastya, which is a little awkward, since Vika is their boss at Claude Monet. Here are the introductions in Russian first.'
OPENER = 'Now back to the introductions, slowly.'
TRANSITION = 'Here are the introductions again, all together.'
OUTRO = 'Max has made the introductions and gone off for drinks, leaving his girlfriend with her own staff. Hold on to "poznakomtes", meet each other, for the next time you introduce your friends. See you next time!'
CLOSING = ('max', 'До скорого!')
STORY = [
    ('vika', 'Настроение паршивое.', "I'm in a lousy mood.", [(75, 'Настроение паршивое')], ''),
    ('vika', 'Хочется на пиццу.', 'I could go for pizza.', [(75, 'хочется на пиццу')], ''),
    ('max', 'Пойдём, я подниму тебе настроение.', "Come on, I'll cheer you up.", [(76, 'Сейчас мы будем повышать твое настроение.')], ''),
    ('nastya', 'Привет! А вот и мы.', 'Hi! Here we are.', [(77, 'Привет! А вот и мы.')], ''),
    ('max', 'А, познакомьтесь, это Вика.', 'Oh, meet Vika.', [(78, 'А, познакомьтесь, это Вика.')], ''),
    ('nastya', 'Вообще-то мы знакомы с Викторией Сергеевной.', 'Actually, we know Viktoria Sergeevna.', [(79, 'Вообще-то мы знакомы с Викторией Сергеевной.')], ''),
    ('max', 'Не-не-не, стоп. Это просто Вика, моя девушка.', "No, no, no, stop. She's just Vika, my girlfriend.", [(80, 'Не-не-не, стоп. Это просто Вика, моя девушка.')], ''),
    ('max', 'Вика, а это просто Настя и просто Костя, мои друзья.', 'Vika, this is just Nastya and just Kostya, my friends.', [(81, 'А это просто Настя и просто Костя, мои друзья.')], ''),
    ('max', 'Ну, с работы.', 'Well, from work.', [(82, 'Ну, с работы.')], ''),
    ('max', 'Ладно, садись.', 'All right, sit down.', [(83, 'Ладно, садись.')], ''),
    ('max', 'Садись сюда, поудобнее.', 'Sit here, make yourself comfortable.', [(83, 'Садись сюда, поудобнее.')], ''),
    ('max', 'А я пойду принесу выпить, окей?', "And I'll go get us something to drink, okay?", [(84, 'принесу выпить, окей?')], ''),
]
WALK = [
    (0, None, '\'I\'m in a lousy mood.\' Russian says "the mood is lousy": "nastroenie", mood, and "parshivoe", a casual word for lousy.'),
    (1, None, '\'I could go for pizza.\' "Khochetsya" is a softer "I want", with no "I" in it at all. "Na pitstsu" is literally "onto pizza", meaning out for pizza.'),
    (2, None, '\'Come on, I\'ll cheer you up.\' "Podnimu tebe nastroenie" is literally "I\'ll lift the mood for you". "Poydyom" is how friends say "let\'s go".'),
    (3, None, '\'Hi! Here we are.\' "A vot i my" is a set phrase for arriving somewhere: literally "and here also we".'),
    (4, None, '\'Oh, meet Vika.\' "Poznakomtes" means "get acquainted", and its "-tes" ending is for more than one person, since Max is talking to both friends.'),
    (5, None, '\'Actually, we already know Viktoria Sergeevna.\' "Voobshche-to", actually, is a gentle correction. After "znakomy s", acquainted with, her name changes to "Viktoriey Sergeevnoy".'),
    (6, None, '\'No, no, no, stop. She\'s just Vika, my girlfriend.\' "Devushka", girl, is also the usual word for girlfriend. "Prosto Vika", just Vika, drops the boss.'),
    (7, None, '\'Vika, this is just Nastya and just Kostya, my friends.\' Max puts "prosto", just, in front of each name, and "druzya" is the plural of "drug", friend.'),
    (8, None, '\'Well, from work.\' "S raboty" means "from work": "rabota" ends in "-y" after "s" when it means "from".'),
    (9, None, '\'All right, sit down.\' "Sadis" is the casual command for one person, so Max is now talking only to Vika.'),
    (10, None, '\'Sit here, get comfortable.\' "Poudobnee" comes from "udobno", comfortable, and means "more comfortably". Max is fussing over her.'),
    (11, None, '\'And I\'ll go get us something to drink, okay?\' "Prinesu vypit" is literally "I\'ll bring to drink". "Okey" is borrowed straight from English.'),
]
