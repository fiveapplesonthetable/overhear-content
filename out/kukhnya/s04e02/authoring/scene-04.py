ID = "kukhnya-s04e02-scene-04"
SHOW = "kukhnya"
SEASON = 4
EPISODE = 2
SCENE = 4
TITLE = 'Утренний поход в магазин  (Morning Trip to the Store)'
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {'narrator': 'sky', 'anya': 'alisa', 'vika': 'angelina', 'denis': 'anja'}
LABELS = {'anya': 'Макс', 'vika': 'Вика', 'denis': 'Денис'}
SOURCE_NAME = "Кухня (Kukhnya) S4.02"
SOURCE_FILE = 'sources/kukhnya/s04/e02.ru.srt'

INTRO = "The next morning, Vika notices Denis's bed is empty and hopes he went home, until Denis walks in with groceries and mud on his clothes. Let's listen to the scene in Russian first."

STORY = [
    ('vika', 'А где Денис?', 'Where is Denis?', [(40, 'А где Денис?')], ''),
    ('anya', 'Домой уехал.', 'He went back home.', [(41, 'Домой уехал.')], ''),
    ('anya', 'Сказал, Москва деревня, а Воронеж город возможностей.', 'He said Moscow is a village and Voronezh is a city of opportunity.', [(42, 'Сказал, Москва деревня, а Воронеж город возможностей.')], ''),
    ('anya', 'Будешь? Может, присоединишься?', 'Want some? Maybe you will join me?', [(43, 'Будешь? Может, присоединишься?')], ''),
    ('denis', 'Масло, хлеб купил.', 'I bought butter and bread.', [(44, 'Масло, хлеб купил.')], ''),
    ('denis', 'Цена у вас, конечно.', 'Your prices here are something else, of course.', [(45, 'Цена у вас, конечно.')], ''),
    ('denis', 'Макс, я тут машину помог толкнуть.', 'Max, I helped push a car out there.', [(46, 'Макс, я тут машину помог толкнуть.')], ''),
    ('denis', 'Есть полотенца?', 'Are there any towels?', [(47, 'Есть полотенца?')], ''),
    ('anya', 'В ванной.', 'In the bathroom.', [(47, 'В ванной.')], ''),
    ('vika', 'Ну, где ты ходишь?', 'Well, where have you been wandering?', [(48, 'Ну, где ты ходишь?')], ''),
    ('denis', 'Я в магазине был.', 'I was at the grocery store.', [(49, 'Я в магазине был.')], ''),
    ('vika', 'У меня нет слов.', 'I have no words.', [(50, 'У меня нет слов.')], ''),
]

OPENER = 'Time to unpack every phrase from the exchange you just heard.'

WALK = [
    (0, None, "'Where is Denis?' Vika raises the pitch on the key word to turn this short Russian clause into a direct question."),
    (1, None, "'He went back home.' Max keeps the sentence short and direct, relying on Russian case endings to show how the words connect."),
    (2, None, "'He said Moscow is a village and Voronezh is a city of opportunity.' In spoken Russian, Max omits unnecessary linking verbs so the key idea lands immediately."),
    (3, None, "'Want some? Maybe you will join me?' Max uses natural conversational word order here to highlight the most important part of the reply."),
    (4, None, "'I bought butter and bread.' The past-tense verb ending marks the grammatical gender and number of the subject directly."),
    (5, None, "'Your prices here are something else, of course.' Denis keeps the sentence short and direct, relying on Russian case endings to show how the words connect."),
    (6, None, "'Max, I helped push a car out there.' Notice how Denis pairs a modal word or finite verb with an infinitive to express the action."),
    (7, None, "'Are there any towels?' Denis raises the pitch on the key word to turn this short Russian clause into a direct question."),
    (8, None, "'In the bathroom.' Max keeps the sentence short and direct, relying on Russian case endings to show how the words connect."),
    (9, None, "'Well, where have you been wandering?' In spoken Russian, Vika omits unnecessary linking verbs so the key idea lands immediately."),
    (10, None, "'I was at the grocery store.' Denis uses natural conversational word order here to highlight the most important part of the reply."),
    (11, None, "'I have no words.' Vika uses natural conversational word order here to highlight the most important part of the reply."),
]

TRANSITION = "Now let's replay the complete scene in Russian without interruption."

OUTRO = "That finishes Denis's muddy morning return from the grocery store. Those short everyday questions about where someone has been come up constantly. See you in the next scene."
CLOSING = ('vika', 'У меня нет слов.')
CLOSING_TRANS = 'I have no words.'
