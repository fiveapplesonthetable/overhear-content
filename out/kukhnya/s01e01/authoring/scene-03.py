# Authoring module for kukhnya-s01e01-scene-03.
ID = 'kukhnya-s01e01-scene-03'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 1
SCENE = 3
TITLE = 'Ночной разговор  (Night Conversation)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'max': 'Макс', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.01'
SOURCE_FILE = 'sources/kukhnya/s01/e01.ru.dual.srt'
INTRO = "It's late now, and Max and Vika are lying awake in the dark, talking quietly. She asks whether he really loves cooking, and he tells her what food means to him. Here's the conversation in Russian first."
OPENER = "Let's look at the pieces."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'Quiet, warm talk like this is full of words you can reuse, and "good night" is the one to keep. In the morning the mood changes completely.'
CLOSING = ('max', 'Пока!')
STORY = [
    ('vika', 'Макс, ты уже почти засыпаешь?', 'Max, are you almost falling asleep?', [], ''),
    ('max', 'Нет, я просто любуюсь тобой.', 'No, I am simply admiring you.', [], ''),
    ('vika', 'Ты правда так сильно любишь готовить?', 'Do you really love cooking so much?', [], ''),
    ('max', 'Еда — это настоящая любовь и страсть!', 'Food is true love and passion!', [(23, 'это')], ''),
    ('vika', 'Ты говоришь о еде как поэт.', 'You speak about food like a poet.', [], ''),
    ('max', 'Хорошая еда дарит людям огромное счастье.', 'Good food gives people immense happiness.', [], ''),
    ('vika', 'В каком ресторане у тебя собеседование?', 'At which restaurant is your interview?', [], ''),
    ('max', 'В самом лучшем французском ресторане Москвы.', 'In the very best French restaurant in Moscow.', [], ''),
    ('vika', 'Наш город полон удивительных совпадений.', 'Our city is full of surprising coincidences.', [], ''),
    ('max', 'Я рад, что встретил тебя сегодня.', 'I am glad that I met you today.', [], ''),
    ('vika', 'Ложись спать, тебе надо хорошо отдохнуть.', 'Go to sleep, you need to rest well.', [], ''),
    ('max', 'Спокойной ночи, прекрасная Вика.', 'Good night, beautiful Vika.', [], ''),
    ('vika', 'Спокойной ночи, мой храбрый повар.', 'Good night, my brave cook.', [], ''),
]
WALK = [
    (0, None, ['\'Max, are you almost falling asleep?\' ', ('vika', 'засыпаешь'), ' is "you\'re falling asleep", and it shares its root with the verb for to sleep, which comes back at the end of this scene. ', ('vika', 'почти'), ', "almost", makes the question a gentle tease.']),
    (1, None, ['\'No, I am simply admiring you.\' ', ('max', 'любуюсь'), ' is "I enjoy looking at", and what you look at has to change shape: the word for "you" turns into ', ('max', 'тобой'), '. The final ending is a little "self" that Russian attaches to many verbs.']),
    (2, None, ['\'Do you really love cooking so much?\' ', ('vika', 'любишь готовить'), ' is "you love to cook", just two words with no "to" between them. ', ('vika', 'правда'), ', "truth", is standing in for "really", as it did when they first met.']),
    (3, None, ['\'Food is true love and passion!\' The dash is standing in for "is". ', ('max', 'любовь'), ' is "love", related to the verb for "I love", and ', ('max', 'настоящая'), ' means "real" or "genuine".']),
    (4, None, ['\'You speak about food like a poet.\' ', ('vika', 'о еде'), ' is "about food", and the word for food gets an ending after the word for "about". ', ('vika', 'как поэт'), ' is "like a poet", and as you can see the word for poet looks just like English.']),
    (5, None, ['\'Good food gives people immense happiness.\' ', ('max', 'дарит'), ' means "gives", and it grows from the word for a gift, so good food literally hands out a gift. ', ('max', 'людям'), ' is "to people": the word for people is irregular, and this is its "to" form.']),
    (6, None, ['\'At which restaurant is your interview?\' ', ('vika', 'у тебя'), ', "at you", is the friendly twin of the polite form you heard earlier. After "in", both words of "which restaurant" change: ', ('vika', 'в каком ресторане'), '.']),
    (7, None, ['\'In the very best French restaurant in Moscow.\' ', ('max', 'В самом лучшем'), ', "the very best", changes its form after "in". ', ('max', 'Москвы'), ' means "of Moscow": the name of the city drops its final letter and takes a new ending.']),
    (8, None, ['\'Our city is full of surprising coincidences.\' ', ('vika', 'совпадений'), ', a coincidence, is built from a prefix meaning "together", and the verb meaning "to fall": things that fall together. ', ('vika', 'полон'), ', "full", is in the masculine form to match the word for city.']),
    (9, None, ['\'I am glad that I met you today.\' A man says ', ('max', 'Я рад'), ', "I\'m glad", and a woman says the feminine version. ', ('max', 'встретил'), ', "met", works the same way: in the past tense, Russian verbs show whether the speaker is a man or a woman.']),
    (10, None, ['\'Go to sleep, you need to rest well.\' ', ('vika', 'Ложись спать'), ' is "lie down to sleep". ', ('vika', 'тебе надо'), ', "to you necessary", is just like the phrase from the bar: the one who needs gets the "to" form.']),
    (11, None, ['\'Good night, beautiful Vika.\' ', ('max', 'Спокойной ночи'), ' is literally "of a quiet night", with "I wish you" left out. It\'s a ready-made phrase, so you can just say it.']),
    (12, None, ['\'Good night, my brave cook.\' Vika has another word for brave: ', ('vika', 'храбрый'), ', a touch more heroic than the word she used earlier. Russian often has several words for a quality.']),
]
