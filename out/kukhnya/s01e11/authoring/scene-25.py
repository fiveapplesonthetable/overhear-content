# Authoring module for kukhnya-s01e11-scene-25.
ID = 'kukhnya-s01e11-scene-25'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 11
SCENE = 25
TITLE = "Отзыв критика  (The Critic's Review)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'mama': 'Мама', 'nagiyev': 'Нагиев'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.11'
SOURCE_FILE = 'sources/kukhnya/s01/e11.ru.dual.srt'
INTRO = "The day ends in an odd way. A woman storms in to tell the chef how disappointed she is, and then the critic's review is read out. Hear it first, then we'll pick it apart."
OPENER = "We'll go slowly this time."
TRANSITION = "This time you'll hear more."
OUTRO = "Nine out of ten, and Kostya's name in the review. That is how the episode ends: the critic was a fair man, after all. Carry on listening, and see you soon."
CLOSING = ('nagiyev', 'Пока!')
STORY = [
    ('mama', 'Витя, я выражаю тебе своё крайнее возмущение!', 'Vitya, I express to you my extreme outrage!', [(324, 'Чтобы выразить тебе свое крайнее возмущение.')], ''),
    ('mama', 'Я глубоко разочарована плохим сервисом в ресторане.', 'I am deeply disappointed by the bad service in the restaurant.', [(326, 'И глубоко разочарована.')], ''),
    ('barinov', 'Мама, не кричи здесь, мы заняты работой.', 'Mom, do not shout here, we are busy with work.', [], ''),
    ('mama', 'Чтобы в двенадцать часов ровно был дома!', "Be home at twelve o'clock sharp!", [(334, 'В 12 часов, чтобы был дома.')], ''),
    ('nagiyev', 'Шеф, скорее включай телевизор, там кулинарный критик!', 'Chef, turn on the TV quickly, the food critic is on!', [], ''),
    ('barinov', 'Неужели критик уже выпустил свой разгромный отзыв?', 'Has the critic already released his devastating review?', [], ''),
    ('nagiyev', 'Он говорит, что наше главное достоинство — принципиальность.', 'He says that our main virtue is integrity.', [(340, 'Главным достоинством ресторана является особая принципиальность всего коллектива.')], ''),
    ('barinov', 'Правда? А что он сказал про кухню?', 'Really? And what did he say about the kitchen?', [], ''),
    ('nagiyev', 'Он назвал всю нашу еду просто восхитительной!', 'He called all our food simply delicious!', [(346, 'Она здесь просто восхитительна')], ''),
    ('nagiyev', 'А бармена Костю он назвал настоящим профессионалом.', 'And he called bartender Kostya a real professional.', [(347, 'Отдельно я бы отметил бармена Константина.'), (348, 'Это не просто профессионал своего дела, но еще и очень хороший человек.')], ''),
    ('nagiyev', 'Критик поставил ресторану девять баллов из десяти!', 'The critic gave the restaurant nine points out of ten!', [(349, 'В целом я бы поставил этому ресторану 9 баллов из 10.')], ''),
    ('barinov', 'Девять из десяти? Это же невероятный успех!', 'Nine out of ten? That is an incredible success!', [(350, '9 из 10.')], ''),
    ('nagiyev', 'Витя, срочно верни Костю обратно на работу!', 'Vitya, urgently bring Kostya back to work!', [(351, 'Бармена надо вернуть.')], ''),
]
WALK = [
    (0, None, ["'Vitya, I express to you my extreme outrage!' Now let's inspect this part: ", ('mama', 'выражаю'), ' means I express, and is official language she uses to scold. ', ('mama', 'возмущение'), ' is outrage. She calls him Vitya, the short form of Viktor.']),
    (1, None, ["'I am deeply disappointed by the bad service in the restaurant.' We can analyze the sentence: ", ('mama', 'разочарована'), ' means disappointed, and has the feminine ending. ', ('mama', 'плохим'), ('mama', 'сервисом'), ' has the ending for by means of. She keeps up the formal act.']),
    (2, None, ["'Mom, do not shout here, we are busy with work.' He says ", ('barinov', 'Мама'), ', the everyday word for mother, which grown men use too. ', ('barinov', 'заняты'), ' means busy. ', ('barinov', 'не'), ('barinov', 'кричи'), " means don't shout."]),
    (3, None, ["'Be home at twelve o'clock sharp!' After so that, the verb takes its past form, ", ('mama', 'был'), ', though the order is for the future. ', ('mama', 'ровно'), ' means exactly or sharp. ', ('mama', 'дома'), ' is at home.']),
    (4, None, ["'Chef, turn on the TV quickly, the food critic is on!' Now we can inspect this part: ", ('nagiyev', 'включай'), ' means turn on. Nagiyev calls him chef but uses familiar address, as an old friend.']),
    (5, None, ["'Has the critic already released his devastating review?' We can break down the sentence: ", ('barinov', 'выпустил'), ' means released, and is related to episode. ', ('barinov', 'разгромный'), ' means devastating, and grows from the term for a rout. Barinov fears the worst.']),
    (6, None, ["'He says that our main virtue is integrity.' Let's focus on the speech: ", ('nagiyev', 'достоинство'), ' means virtue, and is also the term for dignity. ', ('nagiyev', 'принципиальность'), ' means integrity, and stems from principle.']),
    (7, None, ["'Really? And what did he say about the kitchen?' Let us break down the speech: ", ('barinov', 'Правда'), ' means truth, and is how people ask really. ', ('barinov', 'про'), ('barinov', 'кухню'), ' is about the kitchen. Barinov wants to hear about his own domain.']),
    (8, None, ["'He called all our food simply delicious!' After called, the praise changes its ending: ", ('nagiyev', 'восхитительной'), ' means delightful, and is a grand word. Nagiyev reads the praise with relish.']),
    (9, None, ["'And he called bartender Kostya a real professional.' The ending changes again in ", ('nagiyev', 'настоящим'), ('nagiyev', 'профессионалом'), '. The critic noticed Kostya, the man who was about to be fired.']),
    (10, None, ["'The critic gave the restaurant nine points out of ten!' They say put a mark: ", ('nagiyev', 'поставил'), ' means gave or put. ', ('nagiyev', 'из'), ('nagiyev', 'десяти'), ' means out of ten, using from. Nagiyev announces the score like a sports result.']),
    (11, None, ["'Nine out of ten? That is an incredible success!' Now we can break down the dialogue: ", ('barinov', 'невероятный'), ' means incredible, and grows from the word to believe. Barinov repeats the score, delighted.']),
    (12, None, ["'Vitya, urgently bring Kostya back to work!' Let's break down the phrase: ", ('nagiyev', 'верни'), ' means give back, and covers returning things and people. ', ('nagiyev', 'обратно'), ' is back, and ', ('nagiyev', 'срочно'), ' is urgently. Nagiyev gives the order that ends the episode.']),
]
