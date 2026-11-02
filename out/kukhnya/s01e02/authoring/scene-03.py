# Authoring module for kukhnya-s01e02-scene-03.
ID = 'kukhnya-s01e02-scene-03'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 2
SCENE = 3
TITLE = "Ошибка природы  (Freak of Nature)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = 'ru-en'
LABELS = {"barinov": "Шеф", "nastya": "Настя"}
SOURCE_NAME = 'Кухня (Kukhnya) S1.02'
SOURCE_FILE = 'sources/kukhnya/s01/e02.ru.dual.srt'
INTRO = "Nastya, the waitress, runs into the kitchen with an urgent question for Chef Barinov: what do you call a woman who is a head chef? His answer is not kind, and her reply is the punchline. A head chef from the restaurant next door is sitting in the dining room. Let's listen in Russian first."
OPENER = "Let's go through it again, line by line."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Next time you watch, look at the chef's face when she says it. See you next time!"
CLOSING = ("barinov", "Пока!")
STORY = [
    ('barinov', 'Настя, ты меня когда-нибудь доведёшь!', 'Nastya, you will drive me crazy one of these days!', [(23, 'Настя, я из тебя когда-нибудь инфаркт получил')], ''),
    ('barinov', 'Нельзя так неожиданно вбегать на кухню.', 'One must not run into the kitchen so unexpectedly.', [], ''),
    ('nastya', 'Шеф, у меня очень срочный вопрос.', 'Chef, I have a very urgent question.', [], ''),
    ('nastya', 'Как правильно называется шеф-повар женщина?', 'What is the correct term for a female chef?', [(24, 'как правильно называется шеф-повар женщина')], ''),
    ('barinov', 'Женщина шеф-повар — это ошибка природы.', 'A female head chef is a freak of nature.', [(25, 'Ошибка природы')], ''),
    ('nastya', 'Почему вы так несправедливо говорите?', 'Why do you speak so unfairly?', [], ''),
    ('barinov', 'Потому что настоящая кухня — мужское дело!', "Because a real kitchen is a man's business!", [], ''),
    ('nastya', 'Тогда у нас сидит ошибка природы.', 'Then a freak of nature is sitting in our hall.', [(26, 'у нас в зале сидит ошибка природы')], ''),
    ('barinov', 'Где именно сидит эта женщина?', 'Where exactly is this woman sitting?', [], ''),
    ('nastya', 'Она сидит в нашем главном зале.', 'She is sitting in our main dining hall.', [(26, 'у нас в зале')], ''),
    ('barinov', 'Откуда пришла эта странная гостья?', 'Where did this strange guest come from?', [], ''),
    ('nastya', 'Это шеф-повар из соседнего ресторана!', 'This is the head chef from the neighboring restaurant!', [(26, 'из соседнего ресторана')], ''),
    ('barinov', 'Что конкуренты забыли в моём ресторане?', 'What do the rivals want in my restaurant?', [], ''),
]
WALK = [
    (0, None, ["'Nastya, you will drive me crazy one of these days!' He's already in a mood. The term for \"one of these days\" ", ('barinov', "когда-нибудь"), " means \"someday\", and said like this it's a warning."]),
    (1, None, ["'One must not run into the kitchen so unexpectedly.' The house rule: you don't burst into his kitchen. There is no \"you\" in the Russian, just the term for \"it is not allowed\", ", ('barinov', "Нельзя"), ", which is how rules are stated."]),
    (2, None, ["'Chef, I have a very urgent question.' Nastya doesn't flinch. In Russian she literally says ", ('nastya', "у меня"), ", which translates to \"at me\" rather than \"I have\": the question sits with her."]),
    (3, None, ["'What is the correct term for a female chef?' Nastya asks it innocently. The term for \"head chef\", ", ('nastya', "шеф-повар"), ", has no obvious female version, which is exactly what sets him off."]),
    (4, None, ["'A female head chef is a freak of nature.' Barinov's answer, and it's a harsh one. ", ('barinov', "ошибка природы."), " translates to \"freak of nature\" and is a real Russian expression for something that shouldn't exist."]),
    (5, None, ["'Why do you speak so unfairly?' She uses the formal word for \"you\", ", ('nastya', "вы"), ", even while disagreeing, which is how a waitress objects to her boss."]),
    (6, None, ["'Because a real kitchen is a man's business!' His reasoning is that a kitchen is ", ('barinov', "мужское дело!"), ", which literally means a man's business. He sounds very sure, and he is about to be proved wrong."]),
    (7, None, ["'Then a freak of nature is sitting in our hall.' Now Nastya takes his own words and hands them back. The little word for \"then\", ", ('nastya', "Тогда"), ", is where she starts to smile."]),
    (8, None, ["'Where exactly is this woman sitting?' He bites at once. The term for \"exactly\", ", ('barinov', "именно"), ", sharpens the question: where, precisely?"]),
    (9, None, ["'She is sitting in our main dining hall.' Nastya stays calm and plain. The describing word for \"main\", ", ('nastya', "главном"), ", makes the news worse for him."]),
    (10, None, ["'Where did this strange guest come from?' The chef has switched from sneering to suspicion. The term for \"strange\" is ", ('barinov', "странная"), ", but he is no longer laughing."]),
    (11, None, ["'This is the head chef from the neighboring restaurant!' There is the punchline: the woman in the dining room is a head chef from next door. The term for \"neighboring\", ", ('nastya', "соседнего"), ", makes it the very thing he just insulted."]),
    (12, None, ["'What do the rivals want in my restaurant?' Barinov's first thought is spying. The phrase ", ('barinov', "в моём ресторане?"), " translates to \"in my restaurant\" and says it all: this place is his."]),
]
