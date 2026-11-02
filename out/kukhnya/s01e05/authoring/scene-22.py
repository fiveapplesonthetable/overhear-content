# Authoring module for kukhnya-s01e05-scene-22.
ID = 'kukhnya-s01e05-scene-22'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 5
SCENE = 22
TITLE = 'Не торопись  (Take Your Time)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'fedya': 'Федя', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.05'
SOURCE_FILE = 'sources/kukhnya/s01/e05.ru.dual.srt'
INTRO = "Back at the fish station in the Claude Monet kitchen, Max is cooking with Fedya at his shoulder, using the advice he's just been given. This time the orders go out clean. Listen in Russian first."
OPENER = "Let's go back through it. The panic is gone, and the sentences are short and calm."
TRANSITION = 'Now the calm version, from first line to last.'
OUTRO = "Plenty of these kitchen words sound familiar: rhythm, sauce, process, and control. Add the Russian for 'well done' and 'take your time', and you can coach someone through a busy night."
CLOSING = ('max', 'Пока!')
STORY = [
    ('fedya', 'Вот так, Макс, держи правильный ритм.', 'Like that, Max, keep the right rhythm.', [], ""),
    ('max', 'Рыба почти готова на горячей сковороде.', 'The fish is almost ready on the hot pan.', [], ""),
    ('fedya', 'Отлично, аккуратно переложи рыбу на тарелку.', 'Great, carefully transfer the fish to the plate.', [], ""),
    ('max', 'Я добавляю свежую зелень и соус.', 'I add fresh greens and sauce.', [], ""),
    ('fedya', 'Молодец, не торопись.', 'Well done, take your time.', [(313, 'Молодец. Не торопись.')], ""),
    ('fedya', 'Каждое блюдо должно выглядеть красиво.', 'Each dish must look beautiful.', [], ""),
    ('max', 'Вдох и выдох, я спокоен.', 'Inhale and exhale, I am calm.', [], ""),
    ('fedya', 'Видишь, паника исчезает сама собой.', 'See, the panic disappears by itself.', [], ""),
    ('max', 'Теперь я контролирую весь этот процесс.', 'Now I control this entire process.', [], ""),
    ('fedya', 'Вот этот заказ готов к подаче.', 'This order is ready to serve.', [], ""),
    ('max', 'Официант уже может забирать тарелку.', 'The waiter can already take the plate.', [], ""),
    ('fedya', 'Ты отлично справляешься сегодня на смене.', 'You are doing great on the shift today.', [], ""),
    ('max', 'Спасибо, Федя, я готов к работе!', 'Thank you, Fedya, I am ready for work!', [], ""),
]
WALK = [
    (0, None, ["'Like that, Max, keep the right rhythm.' is borrowed, so it's easy to ", ('fedya', 'ритм.'), " catch. ", ('fedya', 'держи'), ", 'hold', also covers keeping a beat or a pace."]),
    (1, None, ["\'The fish is almost ready on the hot pan.\' has the feminine ending because \'fish\' is feminine. ", ('max', 'готова'), " After ", ('max', 'на'), ", the pan takes the prepositional ending: ", ('max', 'горячей'), ('max', 'сковороде.')]),
    (2, None, ["'Great, carefully transfer the fish to the plate.' starts with the prefix for 'across', ", ('fedya', 'переложи'), " so it's 'lay over'. ", ('fedya', 'рыбу'), ' the fish being moved, takes the accusative ending, and so does ', ('fedya', 'на'), ('fedya', 'тарелку.'), ' where it goes.']),
    (3, None, ["'I add fresh greens and sauce.' , 'greens' or 'herbs', is simply ", ('max', 'зелень'), " the word for 'green' turned into a thing. ", ('max', 'добавляю'), ", 'I add', has the 'I' form ending."]),
    (4, None, ["'Well done, take your time.' is the warm 'good job' you ", ('fedya', 'Молодец,'), " give someone younger or junior. ", ('fedya', 'не'), ('fedya', 'торопись.'), ", 'don't hurry', ends in the short form of the reflexive suffix."]),
    (5, None, ["'Each dish must look beautiful.' ends in a neuter vowel to ", ('fedya', 'должно'), ' match the dish. ', ('fedya', 'красиво.'), " is the adverb, so Russian literally says 'look beautifully'."]),
    (6, None, ["'Inhale and exhale, I am calm.' come back from Fedya's ", ('max', 'Вдох'), ('max', 'и'), ('max', 'выдох,'), " lesson. ", ('max', 'спокоен.'), ", 'calm', is the short form for a man; a woman would use the feminine."]),
    (7, None, ["'See, the panic disappears by itself.' , 'you see', is the usual ", ('fedya', 'Видишь,'), " 'see?'. ", ('fedya', 'сама'), ('fedya', 'собой.'), " literally 'itself by itself', expresses 'on its own', and the first word is feminine to match the panic."]),
    (8, None, ["'Now I control this entire process.' and ", ('max', 'контролирую'), ('max', 'процесс.'), ' are borrowed, with Russian endings. ', ('max', 'весь'), ('max', 'этот'), ", 'all this', piles up two words before the noun."]),
    (9, None, ["'This order is ready to serve.' has no ending because 'order' is ", ('fedya', 'готов'), " masculine. ", ('fedya', 'к'), ('fedya', 'подаче.'), ", 'for serving', uses the noun for serving, after the preposition with the dative ending."]),
    (10, None, ["'The waiter can already take the plate.' Like English 'can take', ", ('max', 'может'), " 'he can', is followed by a plain infinitive. ", ('max', 'забирать'), ' literally translates to coming to collect something and carrying it off, and ', ('max', 'тарелку.'), " plate, takes the accusative ending because it's the thing being taken."]),
    (11, None, ["'You are doing great on the shift today.' , 'you're coping', is how Russians ", ('fedya', 'справляешься'), " praise someone's work. ", ('fedya', 'на'), ('fedya', 'смене.'), ", 'on the shift', has the place ending."]),
    (12, None, ["'Thank you, Fedya, I am ready for work!' Max answers with the same ", ('max', 'готов'), ('max', 'к'), ('max', 'работе!'), ' he gave the chef earlier. This time he sounds as if he literally translates to it.']),
]
