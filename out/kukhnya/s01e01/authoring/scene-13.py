# Authoring module for kukhnya-s01e01-scene-13.
ID = 'kukhnya-s01e01-scene-13'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 1
SCENE = 13
TITLE = 'Ужин для конкурентов  (Dinner for Competitors)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'nagiyev': 'Нагиев'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.01'
SOURCE_FILE = 'sources/kukhnya/s01/e01.ru.dual.srt'
INTRO = "In the dining room, the owner, Nagiyev, has a worry for his chef. Rival restaurant people are coming to dinner tonight, and he needs Barinov to impress them. Barinov, as ever, thinks it's easy. Here's the talk in Russian first."
OPENER = "Now let's pick through it."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'The owner is nervous, the chef is sure of himself, and both of them are being a bit unreasonable. You\'ve heard how Russians say "I\'ll fire you", and how a chef keeps his word.'
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('nagiyev', 'Виктор, нам нужно срочно поговорить о работе.', 'Viktor, we need to urgently talk about work.', [(89, 'тебе пора завязывать')], ''),
    ('barinov', 'Дима, ресторан полон и все гости довольны.', 'Dima, the restaurant is full and all guests are happy.', [(90, 'Дима ресторан полон гости довольны')], ''),
    ('nagiyev', 'Сегодня вечером я пригласил к нам конкурентов.', 'Tonight I invited competitors over to our place.', [(92, 'Я сегодня вечером конкурентов приглашаю')], ''),
    ('barinov', 'Зачем ты зовёшь этих странных людей?', 'Why are you inviting these strange people?', [(94, 'Каких еще конкурентов')], ''),
    ('nagiyev', 'Наш сосед открывает новый ресторан за стеной.', 'Our neighbor is opening a new restaurant next door.', [(94, 'за стеной у нас открываются')], ''),
    ('barinov', 'Мы приготовим для них самое лучшее блюдо.', 'We will prepare the very best dish for them.', [(105, 'будешь удивлять')], ''),
    ('nagiyev', 'Они привели нового шеф-повара прямо из Индии.', 'They brought a new chef straight from India.', [(98, 'Приведет своего нового шеф-повара'), (99, 'Из Индии говорит привез')], ''),
    ('barinov', 'Лучше бы они нашли повара из Таджикистана.', 'They would have done better finding a cook from Tajikistan.', [(101, 'А че они из Таджикистана')], ''),
    ('nagiyev', 'Ты должен очень сильно удивить наших гостей.', 'You must greatly surprise our guests.', [(105, 'будешь удивлять')], ''),
    ('barinov', 'Моя авторская кухня поразит абсолютно всех.', 'My signature cuisine will amaze absolutely everyone.', [(100, 'порвет всех')], ''),
    ('nagiyev', 'Если ты ошибёшься, я тебя сразу уволю.', 'If you make a mistake, I will fire you immediately.', [(93, 'Облажаешься я тебя уволю')], ''),
    ('barinov', 'Не волнуйся, шеф всегда держит своё слово.', 'Do not worry, the chef always keeps his word.', [(91, 'Будет наоборот')], ''),
]
WALK = [
    (0, None, ['\'Viktor, we need to urgently talk about work.\' ', ('nagiyev', 'Нам нужно'), ' is "to us needed", the same pattern as ', ('nagiyev', 'нам нужно'), '. ', ('nagiyev', 'поговорить'), ' is "to have a talk", and ', ('nagiyev', 'о работе'), ' is "about work", with ', ('nagiyev', '-е'), ' after ', ('nagiyev', 'о'), '.']),
    (1, None, ['\'Dima, the restaurant is full and all guests are happy.\' That name is a short, friendly form of Dmitry, which Barinov uses with his boss. ', ('barinov', 'полон'), ' is "full", and ', ('barinov', 'довольны'), ' is "satisfied", plural in ', ('barinov', '-ы'), '.']),
    (2, None, ['\'Tonight I invited competitors over to our place.\' ', ('nagiyev', 'Сегодня вечером'), ' is "this evening", with ', ('nagiyev', 'вечером'), ' taking ', ('nagiyev', '-ом'), ', as parts of the day often do. ', ('nagiyev', 'пригласил'), ' is a one-time "invited", and ', ('nagiyev', 'конкурентов'), ' is borrowed.']),
    (3, None, ['\'Why are you inviting these strange people?\' ', ('barinov', 'Зачем'), ' is "what for", a different question from ', ('barinov', 'Зачем'), ', which asks the reason. ', ('barinov', 'этих странных людей'), ' is plural. ', ('barinov', 'людей'), ' is the irregular word for "people".']),
    (4, None, ['\'Our neighbor is opening a new restaurant next door.\' ', ('nagiyev', 'сосед'), ' is neighbour, and ', ('nagiyev', 'за стеной'), ' is literally "behind the wall", Russian for "next door". ', ('nagiyev', 'открывает'), ' is "opens".']),
    (5, None, ['\'We will prepare the very best dish for them.\' ', ('barinov', 'Приготовим'), ' is "we will prepare", one word. ', ('barinov', 'Для них'), ' is "for them", and Russian puts an "n" on "them" after little words like ', ('barinov', 'для'), '.']),
    (6, None, ['\'They brought a new chef straight from India.\' ', ('nagiyev', 'Привели'), ' is "brought", but for a person, by leading. For a thing it would be ', ('nagiyev', 'привели'), '. ', ('nagiyev', 'Шеф-повар'), ' is "chef" and "cook" stuck together.']),
    (7, None, ['\'They would have done better finding a cook from Tajikistan.\' ', ('barinov', 'Лучше'), ' is "better", a cousin of ', ('barinov', 'Лучше'), ', best. The small word ', ('barinov', 'бы'), ' is what makes the sentence "would have".']),
    (8, None, ['\'You must greatly surprise our guests.\' ', ('nagiyev', 'должен'), ' is "must" in the form for a man; said to a woman it would be ', ('nagiyev', 'должен'), '. ', ('nagiyev', 'удивить'), ', "to surprise", shares a root with ', ('nagiyev', 'удивить'), ', "surprising", from the night scene.']),
    (9, None, ['\'My signature cuisine will amaze absolutely everyone.\' ', ('barinov', 'авторская кухня'), ' is "author\'s cuisine", a phrase for a chef\'s own style, as if the chef were a writer. ', ('barinov', 'поразит'), ' is "will amaze".']),
    (10, None, ['\'If you make a mistake, I will fire you immediately.\' ', ('nagiyev', 'Если'), ' is "if". ', ('nagiyev', 'ошибёшься'), ', "you make a mistake", is the verb behind ', ('nagiyev', 'ошибёшься'), ', a mistake. ', ('nagiyev', 'уволю'), ' is "I will fire", one word.']),
    (11, None, ['\'Do not worry, the chef always keeps his word.\' ', ('barinov', 'Не волнуйся'), ' is "don\'t worry", a command with "self". Barinov calls himself ', ('barinov', 'шеф'), ' in the third person. ', ('barinov', 'держит своё слово'), ' is "holds the word", the same "hold" as "hold the menu".']),
]
