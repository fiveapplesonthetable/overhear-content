# Authoring module for kukhnya-s01e20-scene-20.
ID = 'kukhnya-s01e20-scene-20'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 20
SCENE = 20
TITLE = 'Утро  (Morning)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'elena': 'Елена', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.20'
SOURCE_FILE = 'sources/kukhnya/s01/e20.ru.dual.srt'
INTRO = 'This is the final episode of the first season of Kukhnya, and everything is about to change. Elena comes to the apartment where Max and the Chef live early in the morning.'
OPENER = "Now let's go back through the conversation line by line."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Elena comes to the apartment where Max and the Chef live early in the morning. Next time you watch the episode, listen for the Russian expressions for 'kind' and 'morning' — you will catch every word right away. See you next time!"
CLOSING = ('elena', 'До свидания!')
STORY = [
    ('elena', 'Здрасте.', 'Hello.', [(330, 'Здрасте')], ''),
    ('elena', 'Доброе утро.', 'Good morning.', [(330, 'Доброе утро')], ''),
    ('elena', 'Это Макс?', 'Is this Max?', [], ''),
    ('max', 'Да, это я.', 'Yes, it is me.', [], ''),
    ('elena', 'Я ищу его.', 'I am looking for him.', [], ''),
    ('elena', 'Дома не могу ему дозвониться.', "At home I can't reach him.", [(331, 'дома не могу ему дозвониться')], ''),
    ('elena', 'Где он?', 'Where is he?', [], ''),
    ('max', 'Я не знаю.', "I don't know.", [(332, 'Не знаю')], ''),
    ('max', 'Наверное, ключи висят.', 'Probably, the keys are hanging.', [(332, 'Наверное, ключи висят')], ''),
    ('max', 'Значит, он дома.', 'So, he is home.', [(332, 'значит, дома')], ''),
    ('max', 'Вы хотите войти?', 'Do you want to come in?', [], ''),
    ('max', 'Проходите.', 'Come in.', [(333, 'Проходите')], ''),
]
WALK = [
    (0, None, "'Hello.' Elena offers a very casual, shortened greeting as she arrives at the apartment early in the morning."),
    (1, None, "'Good morning.' Elena follows up with a standard morning greeting."),
    (2, None, "'Is this Max?' She wants to make sure she is talking to the right person."),
    (3, None, "'Yes, it is me.' Max confirms his identity using a simple phrase that directly connects the word for this with himself."),
    (4, None, "'I am looking for him.' Elena states her purpose immediately, using a single action word to explain she is trying to find the Chef."),
    (5, None, "'At home I can't reach him.' Elena explains her early visit by noting she could not reach him by phone at his own place."),
    (6, None, "'Where is he?' Elena demands to know his location with a blunt, one-word question."),
    (7, None, "'I don't know.' Max answers honestly that he has no idea where his roommate is."),
    (8, None, "'Probably, the keys are hanging.' Max notices the keys are on the hook, guessing that this means the Chef has not left."),
    (9, None, "'So, he is home.' Max concludes logically that the Chef must be around, linking the word for means directly to at home."),
    (10, None, "'Do you want to come in?' Max politely asks if she would like to step inside, raising his voice at the end of the sentence to form the question."),
    (11, None, "'Come in.' Max invites her to enter by using a direct, formal request."),
]
