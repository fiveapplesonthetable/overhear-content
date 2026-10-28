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
    (0, None, '\'Good morning, Andrey Mikhailovich, did you call for me?\' Questioning whether Andrey Mikhailovich did the inspector calls for him is how Barinov tests the inspector\'s story. Notice how he sticks to the formal "you", keeping a professional line between them.'),
    (1, None, "'Yes, Viktor Petrovich, meet Sergey Vladimirovich.' Adding that Barinov should meet Sergey Vladimirovich fills in the missing piece for Barinov."),
    (2, None, '\'Starting today he is your new boss.\' Pointing out that starting today he is Barinov\'s new boss gives Barinov a sobering reality check. Notice how he sticks to the formal "you", keeping a professional line between them.'),
    (3, None, '\'Sergey is the best manager in our entire chain.\' The inspector explains that Sergey is the best manager in their entire chain, keeping his voice calm and direct. Russian drops "is" in the present, setting the two halves of the thought side by side.'),
    (4, None, "'We had to call him in to save our profitability.' Realizing that they had to call him in to save their profitability changes how the inspector handles the situation."),
    (5, None, '\'Our profit is higher than in any European restaurant!\' Insisting that their profit is higher than in any European restaurant shows Barinov is not backing down. Russian expresses having something as "by me is", keeping the phrase short and grounded.'),
    (6, None, '\'Hello, Seryozha! Hello to you too, darling!\' With the boss and kitchen at stake, Max reacts without holding back. Speaking with the close, informal "you" strips away any polite distance between them.'),
    (7, None, "'Wait a second, did the two of you already see each other yesterday?' The inspector asks whether a second did the two of Barinov already see each other yesterday, refusing to let the point slide."),
    (8, None, "'Yes, Olya helped me with the hotel yesterday.' Saying that Olya helped him with the hotel yesterday is how Max sets the tone with Barinov."),
    (9, None, '\'Olga, tell me, is it fashionable to walk around like that now?\' Wondering if someone tell him is it fashionable to walk around like that now shows Barinov caught off guard. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (10, None, "'Look, you are missing one earring in your ear.' Adding that the inspector is missing one earring in the inspector's ear fills in the missing piece for the inspector."),
    (11, None, "'Andrey, put it in your pocket, or I will lose this one too.' Max tells Barinov that Andrey put it in Barinov's pocket or he will lose this one without dressing it up."),
    (12, None, '\'It is time for me to go, it turns out we have to save profitability!\' Insisting that it is time for him to go it turns out they have to save profitability shows Barinov is not backing down. There is no "you" needed in the Russian here: one short word states the rule for everyone in the room.'),
]
