# Authoring module for kukhnya-s01e11-scene-02.
ID = 'kukhnya-s01e11-scene-02'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 11
SCENE = 2
TITLE = 'Тайный критик  (The Secret Critic)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.11'
SOURCE_FILE = 'sources/kukhnya/s01/e11.ru.dual.srt'
INTRO = "Meanwhile in the kitchen, Vika bursts in with news that the owner has just phoned. A restaurant critic will visit today, and nobody knows what he looks like. Let's hear it."
OPENER = "Now I'll walk you through it."
TRANSITION = 'One more run through, all the way.'
OUTRO = 'The kitchen is on alert, and Max has been exiled to the dishes. This is the sort of order that rarely lasts. Until we meet again.'
CLOSING = ('vika', 'Пока!')
STORY = [
    ('vika', 'Внимание всем! У меня важная информация.', 'Attention everyone! I have important information.', [(24, 'Внимание! У меня важная информация.')], ''),
    ('barinov', 'Вика, говори быстрее, у нас много заказов.', 'Vika, speak faster, we have a lot of orders.', [(25, 'У тебя минута')], ''),
    ('vika', 'Только что звонил сам Дмитрий Владимирович.', 'Dmitry Vladimirovich himself just called.', [(26, 'Звонил Дмитрий Владимирович.')], ''),
    ('barinov', 'И что сказал наш уважаемый хозяин?', 'And what did our respected owner say?', [(27, 'Сообщил, что')], ''),
    ('vika', 'К нам сегодня приедет ресторанный критик.', 'A restaurant critic will come to us today.', [(27, 'к нам сегодня заедет.'), (29, 'Ресторанный критик.')], ''),
    ('barinov', 'Мы накормим его вкусным горячим обедом.', 'We will feed him a delicious hot lunch.', [(30, 'в чем проблема?')], ''),
    ('vika', 'Никто не знает, как он выглядит.', 'Nobody knows what he looks like.', [(32, 'никто не знает, как он выглядит.')], ''),
    ('barinov', 'Значит, готовим каждое блюдо идеально точно.', 'That means we cook each dish with perfect precision.', [], ''),
    ('vika', 'И не пускай сегодня Макса на кухню.', 'And do not let Max into the kitchen today.', [(36, 'не допускай сегодня к работе')], ''),
    ('barinov', 'А почему новый повар не должен работать?', 'And why should the new cook not work?', [(36, 'новенького.'), (37, 'Это еще почему?')], ''),
    ('vika', 'Потому что этот парень приносит сплошные проблемы.', 'Because this guy brings constant problems.', [(38, 'Потому что это и сплошная')], ''),
    ('barinov', 'Хорошо, Макс будет мыть грязную посуду.', 'Fine, Max will wash dirty dishes.', [], ''),
    ('vika', 'Сегодня на кухне нужен полный порядок.', 'Today complete order is needed in the kitchen.', [(39, 'А мне сегодня проблемы не нужны.')], ''),
]
WALK = [
    (0, None, ["'Attention everyone! I have important information.' Now we can analyze the dialogue: ", ('vika', 'Внимание'), ('vika', 'всем'), " is 'attention to all', the call to a room here. Then ", ('vika', 'У'), ('vika', 'меня'), ", 'at me', stands for 'I have'. ", ('vika', 'информация'), ' is easy.']),
    (1, None, ["'Vika, speak faster, we have a lot of orders.' We can look at this line: ", ('barinov', 'быстрее'), " is 'quickly', with a suffix like English '-er'. After ", ('barinov', 'много'), ", 'many', the noun for orders becomes ", ('barinov', 'заказов'), ". Barinov uses the familiar 'you' with her."]),
    (2, None, ["'Dmitry Vladimirovich himself just called.' We will examine this line: ", ('vika', 'сам'), ", 'himself', is added for emphasis: the owner in person. ", ('vika', 'Только'), ('vika', 'что'), ", 'only what', is the wording for 'just now'. ", ('vika', 'звонил'), " is 'called' on the phone."]),
    (3, None, ["'And what did our respected owner say?' Let's break down the phrase: ", ('barinov', 'уважаемый'), ", 'respected', is from the same family as 'I respect', which Max said to Louis. ", ('barinov', 'хозяин'), ' is the owner, the man of the house.']),
    (4, None, ["'A restaurant critic will come to us today.' Now we can consider the words: ", ('vika', 'приедет'), ", 'will arrive', is the by-vehicle 'come'. ", ('vika', 'К'), ('vika', 'нам'), " is 'to us', to our place. And ", ('vika', 'ресторанный'), " turns 'restaurant' into a describing word: 'restaurant critic'."]),
    (5, None, ["'We will feed him a delicious hot lunch.' Now let's break down this line: ", ('barinov', 'накормим'), ", 'we will feed', stems from the noun for animal feed Barinov joked about with his winnings. The first part means 'fill up'. Barinov's whole plan is food."]),
    (6, None, ["'Nobody knows what he looks like.' Here we have is ", ('vika', 'Никто'), ('vika', 'не'), ('vika', 'знает'), ", 'nobody not knows', and both negatives are needed. ", ('vika', 'как'), ('vika', 'он'), ('vika', 'выглядит'), " is 'how he looks', the way to ask about appearance."]),
    (7, None, ["'That means we cook each dish with perfect precision.' We will inspect the phrase: ", ('barinov', 'Значит'), ", 'so', originally means 'it means'. Then ", ('barinov', 'идеально'), ('barinov', 'точно'), ", 'ideally exactly', piles up two similar words. ", ('barinov', 'готовим'), " is 'we cook'."]),
    (8, None, ["'And do not let Max into the kitchen today.' We can analyze the dialogue: ", ('vika', 'не'), ('vika', 'пускай'), ", 'don't let', is a relative of 'let him'. The name Max becomes ", ('vika', 'Макса'), " because he's the one being kept out. ", ('vika', 'на'), ('vika', 'кухню'), " is 'onto the kitchen'."]),
    (9, None, ["'And why should the new cook not work?' Now we can consider the dialogue: ", ('barinov', 'должен'), ", 'must', is a cousin of the noun for 'debt', what you owe. With ", ('barinov', 'не'), " it makes 'should not'. ", ('barinov', 'новый'), ('barinov', 'повар'), " is 'the new cook'."]),
    (10, None, ["'Because this guy brings constant problems.' Now we can consider the words: ", ('vika', 'сплошные'), ('vika', 'проблемы'), " is 'solid problems', meaning nothing but problems. ", ('vika', 'приносит'), ", 'brings', is the carrying word with a start that means 'arriving'. ", ('vika', 'парень'), " is 'guy'."]),
    (11, None, ["'Fine, Max will wash dirty dishes.' Let's focus on this line: ", ('barinov', 'будет'), ('barinov', 'мыть'), " is 'will wash'. ", ('barinov', 'грязную'), ('barinov', 'посуду'), " is 'dirty dishes', both getting a new ending because they're what gets washed. The dishes are the safest place for Max."]),
    (12, None, ["'Today complete order is needed in the kitchen.' There are several kinds of 'orders' here: one for food, one for a command, and here ", ('vika', 'порядок'), ' for tidiness and discipline. ', ('vika', 'нужен'), ", 'needed', matches it."]),
]
