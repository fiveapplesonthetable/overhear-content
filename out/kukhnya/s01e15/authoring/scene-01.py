# Authoring module for kukhnya-s01e15-scene-01.
ID = 'kukhnya-s01e15-scene-01'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 15
SCENE = 1
TITLE = 'Новая жизнь втроём  (A New Life for Three)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kostya': 'Костя', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.15'
SOURCE_FILE = 'sources/kukhnya/s01/e15.ru.dual.srt'
INTRO = "This is Kukhnya, a comedy set in the kitchen of Claude Monet, a smart restaurant in Moscow. This episode is all about who lives where. Nastya has just moved into the flat that Max shares with Kostya, and everybody pretends that nothing has changed. We start on the sofa with two grown men and a video game. First in Russian, and don't worry about missing words."
OPENER = 'Now the same scene, slowly, a line at a time.'
TRANSITION = 'And all of it again, with no stops.'
OUTRO = "Nastya is cooking dinner while the boys carry on shooting. Life with three in the flat is about to get more complicated. Until next time."
CLOSING = ('kostya', 'Пока!')
STORY = [
    ('max', 'Неделю назад к нам переехала Настя.', 'Nastya moved in with us a week ago.', [(1, 'неделю назад к нам переехала')], ''),
    ('kostya', 'Да, теперь мы живём здесь втроём.', 'Yes, now we live here as three.', [], ''),
    ('max', 'Наша жизнь от этого почти не изменилась.', 'Our life barely changed from that.', [(2, 'наша жизнь от этого практически не изменилась')], ''),
    ('kostya', 'Мы всё так же играем вместе.', 'We still play together just the same.', [], ''),
    ('max', 'Костян, давай скорее, стреляй в них!', 'Kostya, hurry up, shoot at them!', [(3, 'Костян, давай скорее')], ''),
    ('kostya', 'Я выбираю своё новое оружие.', 'I am choosing my new weapon.', [], ''),
    ('max', 'Меня тут с трёх сторон окружили!', 'They surrounded me from three sides here!', [(3, 'меня тут с трех сторон')], ''),
    ('kostya', 'Держись, я уже бегу на помощь!', 'Hold on, I am already running to help!', [], ''),
    ('max', 'Отличная работа, это наша победа!', 'Great work, this is our victory!', [], ''),
    ('kostya', 'Мы отличная команда в этой игре.', 'We are a great team in this game.', [], ''),
    ('max', 'Главное, чтобы Настя нам не мешала.', 'The main thing is that Nastya does not disturb us.', [], ''),
    ('kostya', 'Она готовит вкусный ужин на кухне.', 'She is cooking a tasty dinner in the kitchen.', [], ''),
]
WALK = [
    (0, None, ["'Nastya moved in with us a week ago.' Notice how ", ('max', 'Неделю'), ('max', 'назад'), ' puts the time first, then back. ', ('max', 'переехала'), ' has a prefix for going across by transport, and it takes a matching ending since Nastya is the one who moved.']),
    (1, None, ["'Yes, now we live here as three.' Let's consider the speech: ", ('kostya', 'втроём'), ' is a single word for the three of us together. With two people it is similar, and you will hear both a lot.']),
    (2, None, ["'Our life barely changed from that.' We will consider the phrase: ", ('max', 'почти'), ('max', 'не'), ' means almost not, which is how Russian says barely. In ', ('max', 'изменилась'), ', the ending shows that life is feminine, and that it changed itself.']),
    (3, None, ["'We still play together just the same.' Now we can break down the phrase: ", ('kostya', 'всё'), ('kostya', 'так'), ('kostya', 'же'), ' reads as all so same, ordinary Russian for just as before. ', ('kostya', 'играем'), ' means we play, and it covers video games as well as football.']),
    (4, None, ["'Kostya, hurry up, shoot at them!' Max calls him ", ('max', 'Костян'), ', a chummy form that you would only use with a mate. After the term for at, ', ('max', 'них'), ' gets an extra sound in front.']),
    (5, None, ["'I am choosing my new weapon.' The term for weapon, ", ('kostya', 'оружие'), ', is neuter, so both ', ('kostya', 'своё'), ' and ', ('kostya', 'новое'), ' have matching endings. ', ('kostya', 'выбираю'), ' is the ongoing kind of choose, showing he is still at it.']),
    (6, None, ["'They surrounded me from three sides here!' We can inspect the sentence: ", ('max', 'окружили'), ' is in the plural past, with no they in front. Russian drops the subject like this when it does not matter who did it. The term for me, ', ('max', 'Меня'), ', comes first.']),
    (7, None, ["'Hold on, I am already running to help!' We can look at the dialogue: ", ('kostya', 'Держись'), ' means hold yourself, and the ending adds that yourself. ', ('kostya', 'на'), ('kostya', 'помощь'), ' means onto help, the set expression for to the rescue.']),
    (8, None, ["'Great work, this is our victory!' The word for victory, ", ('max', 'победа'), ', is feminine, so our is ', ('max', 'наша'), '. You will hear the term every May, when Russia marks Victory Day.']),
    (9, None, ["'We are a great team in this game.' Let us analyze the speech: ", ('kostya', 'в'), ('kostya', 'этой'), ('kostya', 'игре'), ' means in this game, where the ending changes to show location. Notice there is no are anywhere.']),
    (10, None, ["'The main thing is that Nastya does not disturb us.' Let's analyze the sentence: ", ('max', 'Главное'), ', ', ('max', 'чтобы'), ' is a handy opener meaning the main thing is that. After this, the action ', ('max', 'мешала'), ' takes its past form, even though it means the present.']),
    (11, None, ["'She is cooking a tasty dinner in the kitchen.' Let us focus on this part: ", ('kostya', 'на'), ('kostya', 'кухне'), ' means on the kitchen, where English says in. The evening meal, ', ('kostya', 'ужин'), ', is masculine, which is why tasty has a matching ending.']),
]
