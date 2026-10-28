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
INTRO = "It is early morning, and Elena arrives looking for someone. A voice answers the door, and a short and slightly odd conversation follows. First the Russian, and don't worry about catching every word."
OPENER = "We'll take the lines one by one."
TRANSITION = 'Now it all together again, from the top.'
OUTRO = "The door opens, and the season comes to its end. Notice the verb 'dozvonitsya', which means 'to get through' on the phone, and is built from 'ring' with a prefix and 'sya'. See you next time!"
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
    (0, None, "'Hello.' This is the clipped version of the long hello, with half the letters dropped. It's what you say to someone at the door."),
    (1, None, "'Good morning.' The word for 'morning' is neuter, so the Russian for 'good' finishes with 'oe'. A plain greeting."),
    (2, None, "'Is that Max?' There's no verb, just 'this Max'. The question lives on the voice."),
    (3, None, "'Yes, that's me.' Russian says 'this I' where English says 'that's me'. 'I' stays in its plain form."),
    (4, None, "'I'm looking for him.' The Russian for 'look for' changes its consonants, so 'sk' turns into 'shch', and the word for 'him' takes the 'yego' form."),
    (5, None, "'I can't get through to him at home.' The Russian for 'get through' is built from 'ring' with a prefix and 'sya', and 'at home' is one word."),
    (6, None, "'Where is he?' There's no 'is', just 'where he'. A very short question."),
    (7, None, "'I don't know.' The Russian for 'I know' finishes with 'u', and the word for 'not' stands in front."),
    (8, None, "'Probably the keys are hanging there.' Russians say keys 'hang', and the Russian for 'probably' is one word on its own."),
    (9, None, "'So he's at home.' The Russian for 'it means' is used for 'so'. 'At home' needs no word for 'is'."),
    (10, None, "'Do you want to come in?' The word for 'come in' is the plain form, and the Russian for 'do you want' is the polite plural."),
    (11, None, "'Come in.' The polite command, ending in 'ite', is the usual invitation. Max says it simply."),
]
