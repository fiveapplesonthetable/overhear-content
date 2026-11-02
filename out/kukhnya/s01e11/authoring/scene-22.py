# Authoring module for kukhnya-s01e11-scene-22.
ID = 'kukhnya-s01e11-scene-22'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 11
SCENE = 22
TITLE = 'Мудрый совет  (Wise Advice)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kostya': 'Костя', 'rodion': 'Родион'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.11'
SOURCE_FILE = 'sources/kukhnya/s01/e11.ru.dual.srt'
INTRO = 'At the bar, the soup eater tastes his bouillabaisse, and he notices that Kostya is washing the same glass again. Kostya tells him why. Listen out for the little words.'
OPENER = "Let's see how it's put together."
TRANSITION = 'Now it should sound clearer.'
OUTRO = "The old customer gives Kostya a simple lesson: it is his life and his decision. Whether he'll listen is another matter. See you soon."
CLOSING = ('rodion', 'Пока!')
STORY = [
    ('rodion', 'Этот суп действительно очень вкусный и горячий.', 'This soup is really very tasty and hot.', [(290, 'Хорош супец.')], ''),
    ('rodion', 'Костя, скажи честно, что с тобой случилось?', 'Kostya, tell honestly, what happened with you?', [(291, 'Костя, что с тобой?')], ''),
    ('kostya', 'Всё нормально, я просто вытираю эту рюмку.', 'Everything is fine, I am simply wiping this glass.', [(292, 'Все нормально.'), (293, 'Эта рюмка уже полчаса трет.')], ''),
    ('rodion', 'Ты моешь её уже целых полчаса.', 'You have been washing it for a whole half hour already.', [(293, 'Эта рюмка уже полчаса трет.')], ''),
    ('kostya', 'У Насти за столом сидит важный критик.', "An important critic is sitting at Nastya's table.", [(295, 'У Насти за столиком сидит тип очень важный.'), (296, 'Критик.')], ''),
    ('kostya', 'Этот наглый мужчина грубо пристаёт к ней.', 'This insolent man is rudely hitting on her.', [(297, 'Он пристает к ней.')], ''),
    ('kostya', 'Я боюсь сделать что-нибудь плохое для ресторана.', 'I am afraid of doing something bad for the restaurant.', [(298, 'А я сделать ничего не могу. Он же критик.'), (299, 'Не дай бог, что-нибудь плохое про наш ресторан напишет.')], ''),
    ('rodion', 'Понимаешь, проблема совсем не в этом критике.', 'You see, the problem is not at all in this critic.', [(301, 'Понимаешь, проблема тут не в том, кто он')], ''),
    ('rodion', 'Главный вопрос здесь в том, кто ты.', 'The main question here is in who you are.', [(301, 'а кто ты.')], ''),
    ('rodion', 'Передай мне соль, пожалуйста, юный друг.', 'Pass me the salt, please, young friend.', [(303, 'Дай, пожалуйста, соль.')], ''),
    ('rodion', 'Дворник он или критик — это совсем неважно.', 'Whether he is a janitor or a critic—that is completely unimportant.', [(305, 'А там уже дворник он или критик, это довольно-таки вторично.')], ''),
    ('rodion', 'Позволяешь ты обижать свою девушку или нет?', 'Do you allow someone to insult your girlfriend or not?', [(304, 'Позволяешь ты ему это делать или нет?')], ''),
    ('rodion', 'Жизнь твоя, и только ты принимаешь решение!', 'The life is yours, and only you make the decision!', [(307, 'Ну что, жизнь твоя, девушка твоя.'), (308, 'И решение твоя.')], ''),
]
WALK = [
    (0, None, ["'This soup is really very tasty and hot.' We will examine this part: ", ('rodion', 'действительно'), ' is really, truly. ', ('rodion', 'вкусный'), ' is tasty, and comes from taste. The guest is happy with the soup, and he says so.']),
    (1, None, ["'Kostya, tell honestly, what happened with you?' Now we can consider this part: ", ('rodion', 'скажи'), ('rodion', 'честно'), ' is the usual way to ask for the truth. ', ('rodion', 'с'), ('rodion', 'тобой'), ' means with you. The guest uses familiar address with the bartender, as a regular does.']),
    (2, None, ["'Everything is fine, I am simply wiping this glass.' Now let's focus on the phrase: ", ('kostya', 'рюмку'), ' is a small glass, the kind for spirits. ', ('kostya', 'вытираю'), ' means I am wiping. His mind is elsewhere.']),
    (3, None, ["'You have been washing it for a whole half hour already.' The language uses the present for something still going on: ", ('rodion', 'моешь'), ('rodion', 'её'), ('rodion', 'уже'), ('rodion', 'полчаса'), ' means you wash it already half an hour. ', ('rodion', 'целых'), ' means whole, and adds the exasperation.']),
    (4, None, ["'An important critic is sitting at Nastya's table.' Let's analyze this line: ", ('kostya', 'У'), ('kostya', 'Насти'), ('kostya', 'за'), ('kostya', 'столом'), ' means at Nastya, at the table, meaning at her table. Kostya finally admits what is on his mind.']),
    (5, None, ["'This insolent man is rudely hitting on her.' To pester someone, you say to pester plus the person, so ", ('kostya', 'пристаёт'), ('kostya', 'к'), ('kostya', 'ней'), ' means is pestering her, often with unwanted advances. ', ('kostya', 'наглый'), ' is insolent, and ', ('kostya', 'грубо'), " means rudely. Kostya's anger shows."]),
    (6, None, ["'I am afraid of doing something bad for the restaurant.' Now we can analyze this line: ", ('kostya', 'что'), '-', ('kostya', 'нибудь'), " means something, and has the 'any' ending. ", ('kostya', 'боюсь'), ('kostya', 'сделать'), ' means I am afraid to do. Kostya is torn between love and loyalty.']),
    (7, None, ["'You see, the problem is not at all in this critic.' We will inspect the phrase: ", ('rodion', 'Понимаешь'), ' means you understand, and is the way of saying you see. The phrasing is the problem is in something: ', ('rodion', 'не'), ('rodion', 'в'), ('rodion', 'этом'), ('rodion', 'критике'), ' means not in this critic. The guest is about to say something wise.']),
    (8, None, ["'The main question here is in who you are.' Let's inspect the sentence: ", ('rodion', 'в'), ('rodion', 'том'), ('rodion', 'кто'), ('rodion', 'ты'), ' means in that, who you are, and is the frame for the point is who you are. The guest, a stranger, holds up a mirror to the bartender.']),
    (9, None, ["'Pass me the salt, please, young friend.' Let us analyze the sentence: ", ('rodion', 'Передай'), ' means pass, or hand something on. ', ('rodion', 'соль'), ' means salt. The guest breaks off his own wisdom to ask for salt.']),
    (10, None, ["'Whether he is a janitor or a critic—that is completely unimportant.' Word for word, ", ('rodion', 'Дворник'), ('rodion', 'он'), ('rodion', 'или'), ('rodion', 'критик'), " means janitor he or critic, with no 'whether' at the start. A janitor sweeps the yard, and ", ('rodion', 'неважно'), ' means not important, run together.']),
    (11, None, ["'Do you allow someone to insult your girlfriend or not?' The verb comes first: ", ('rodion', 'Позволяешь'), ('rodion', 'ты'), ' means allow you, for a pointed question. ', ('rodion', 'обижать'), ' means to insult or to hurt. ', ('rodion', 'или'), ('rodion', 'нет'), ' means or not.']),
    (12, None, ["'The life is yours, and only you make the decision!' Let's analyze the phrase: ", ('rodion', 'Жизнь'), ('rodion', 'твоя'), " means life yours, and has no 'is'. And you accept a decision, ", ('rodion', 'принимаешь'), ('rodion', 'решение'), ' rather than make one. The guest finishes his sermon.']),
]
