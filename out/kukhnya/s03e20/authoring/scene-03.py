# Authoring module for kukhnya-s03e20-scene-03.
ID = 'kukhnya-s03e20-scene-03'
SHOW = 'kukhnya'
SEASON = 3
EPISODE = 20
SCENE = 3
TITLE = 'Кризисный менеджер и потерянная серёжка  (The Crisis Manager and the Lost Earring)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'inspector': 'Инспектор', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S3.20'
SOURCE_FILE = 'sources/kukhnya/s03/e20.ru.srt'
INTRO = "At Claude Monet, Andrey Mikhailovich introduces Chef Barinov to his new boss: crisis manager Sergey Vladimirovich from St. Petersburg. When Andrey's wife Olya walks in, Chef notices she is missing one earring."
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "Chef Barinov files away the curious detail of Olya's missing earring as the new crisis manager takes over the kitchen. Until next time!"
CLOSING = ('barinov', 'Хорошего дня!')
STORY = [
    ('barinov', 'Доброе утро, Андрей Михайлович, вы меня звали?', 'Good morning, Andrey Mikhailovich, did you call for me?', [(47, 'Доброе утро, звали')], 'adapted'),
    ('inspector', 'Да, Виктор Петрович, знакомьтесь: это Сергей Владимирович.', 'Yes, Viktor Petrovich, meet Sergey Vladimirovich.', [(48, 'Да, Виктор Петрович, знакомьтесь'), (49, 'Это Сергей Владимирович')], 'adapted'),
    ('inspector', 'С сегодняшнего дня это ваш новый начальник.', 'Starting today he is your new boss.', [(49, 'ваш новый начальник')], 'adapted'),
    ('inspector', 'Сергей — лучший менеджер всей нашей сети.', 'Sergey is the best manager in our entire chain.', [(51, 'Сергей лучший'), (51, 'нашей сети')], 'adapted'),
    ('inspector', 'Пришлось вызвать его спасать нашу рентабельность.', 'We had to call him in to save our profitability.', [(52, 'Пришлось вызвать его'), (52, 'спасать нашу рентабельность')], 'adapted'),
    ('barinov', 'У нас прибыль выше, чем в любом европейском ресторане!', 'Our profit is higher than in any European restaurant!', [(54, 'выше, чем в любом европейском ресторане')], 'adapted'),
    ('max', 'Здравствуйте, Серёжа! Тебе тоже привет, дорогая!', 'Hello, Seryozha! Hello to you too, darling!', [(55, 'Здравствуйте. Серёжа, привет'), (56, 'Тебе привет, дорогая')], 'adapted'),
    ('inspector', 'Подождите, а вы что, вчера уже виделись?', 'Wait a second, did the two of you already see each other yesterday?', [(58, 'А вы что, уже виделись')], 'adapted'),
    ('max', 'Да, Оля вчера помогла мне с гостиницей.', 'Yes, Olya helped me with the hotel yesterday.', [(59, 'Да, Оля помогла мне с гостиницей')], 'adapted'),
    ('barinov', 'Ольга, скажите, а сейчас так модно ходить?', 'Olga, tell me, is it fashionable to walk around like that now?', [(61, 'А сейчас так модно')], 'adapted'),
    ('barinov', 'Посмотрите, у вас одной серёжки в ухе нет.', 'Look, you are missing one earring in your ear.', [(62, 'У тебя одной серёжки нет')], 'adapted'),
    ('max', 'Андрей, положи её к себе, а то и эту потеряю.', 'Andrey, put it in your pocket, or I will lose this one too.', [(63, 'положи-ка ее к себе'), (64, 'эту тоже потеряю')], 'adapted'),
    ('barinov', 'Мне пора идти, оказывается, надо спасать рентабельность!', 'It is time for me to go, it turns out we have to save profitability!', [(65, 'но надо идти'), (66, 'Оказывается, нам надо спасать рентабельность')], 'adapted'),
]
WALK = [
    (0, None, "'Good morning, Andrey Mikhailovich, did you call for me?' Barinov quizzes bluntly how the inspector expects that to work in practice."),
    (1, None, '\'Yes, Viktor Petrovich, meet Sergey Vladimirovich.\' The inspector favors one practical choice for Max: "znakomtes" means "meet" (from "znakomitsya"), giving the line its exact edge.'),
    (2, None, '\'Starting today he is your new boss.\' The inspector states the remark with warmth: notice how Russian needs no word for "am", "is", or "are" in the present — placing the words side by side says it all.'),
    (3, None, "'Sergey is the best manager in our entire chain.' The inspector reacts frankly without a pause, making his position completely clear."),
    (4, None, '\'We had to call him in to save our profitability.\' The inspector points to this key element in earnest: "rentabelnost" means "profitability", and it carries the main weight of what the inspector is saying.'),
    (5, None, '\'Our profit is higher than in any European restaurant!\' Barinov offers the comment at once: the phrase "u nas" literally means "by us" or "at our place", the standard Russian way to talk about what a group or couple shares.'),
    (6, None, "'Hello, Seryozha! Hello to you too, darling!' Max replies frankly in their talk, so Barinov knows he is not just making small talk."),
    (7, None, '\'Wait a second, did the two of you already see each other yesterday?\' The inspector emphasizes this clear word with Max: "podozhdite" means "wait" (from "podozhdat"), giving the line its exact edge.'),
    (8, None, "'Yes, Olya helped me with the hotel yesterday.' Max steps in dryly without holding back, bringing things back to earth after the buildup."),
    (9, None, "'Olga, tell me, is it fashionable to walk around like that now?' Barinov quizzes sharply what Max is actually getting at here."),
    (10, None, '\'Look, you are missing one earring in your ear.\' Barinov spotlights one familiar detail in earnest: "seryozhki" means "earring" (from "seryozhka"), giving the line its exact edge.'),
    (11, None, "'Andrey, put it in your pocket, or I will lose this one too.' Max holds firm pointedly with a nod, making his position completely clear."),
    (12, None, "'It is time for me to go, it turns out we have to save profitability!' Barinov stands firm sharply in this moment, watching the inspector's face to see how the news lands."),
]
