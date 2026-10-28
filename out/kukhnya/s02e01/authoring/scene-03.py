# Authoring module for kukhnya-s02e01-scene-03.
ID = 'kukhnya-s02e01-scene-03'
SHOW = 'kukhnya'
SEASON = 2
EPISODE = 1
SCENE = 3
TITLE = 'Начало смены  (Start of the Shift)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'max': 'Макс', 'senya': 'Сеня'}
SOURCE_NAME = 'Кухня (Kukhnya) S2.01'
SOURCE_FILE = 'sources/kukhnya/s02/e01.ru.dual.srt'
INTRO = 'In the kitchen of Claude Monet, Chef Viktor is furious after the new owner confiscated all of his alcohol. As the restaurant opens for service, Viktor barks orders at Max and Senya to begin cooking immediately. Let us listen to their kitchen exchange in Russian first.'
OPENER = 'Now let us examine the start of the kitchen shift line by line.'
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Despite losing his prized alcohol stash to the new owner, Chef Viktor channels his anger into strict discipline as the kitchen team begins the busy shift. Next time you watch the episode, listen for the Russian expressions for 'cook' and 'fast' — you will catch every word right away. See you next time!"
CLOSING = ('max', 'Пока!')
STORY = [
    ('barinov', 'Повара, быстро встаньте все на свои места!', 'Cooks, quickly stand at your places, everyone!', [], ''),
    ('barinov', 'Сейчас наш ресторан открывает двери для гостей.', 'Right now our restaurant is opening its doors for guests.', [], ''),
    ('barinov', 'Приступайте сразу к своей работе на кухне!', 'Get started immediately with your work in the kitchen!', [(95, 'Приступайте.')], ''),
    ('senya', 'Шеф, почему вы сегодня такой очень злой?', 'Chef, why are you so very angry today?', [], ''),
    ('barinov', 'Новый хозяин забрал весь мой дорогой алкоголь!', 'The new owner took away all my expensive alcohol!', [], ''),
    ('max', 'Он действительно запретил вам пить на работе?', 'Did he really forbid you to drink at work?', [], ''),
    ('barinov', 'Да, теперь на кухне действует сухой закон.', 'Yes, now a dry law is in effect in the kitchen.', [], ''),
    ('senya', 'Без вина вам будет трудно готовить блюда.', 'Without wine it will be hard for you to cook dishes.', [], ''),
    ('barinov', 'Хватит болтать, начинайте резать свежее мясо!', 'Enough chatting, start cutting the fresh meat!', [], ''),
    ('max', 'Я уже приготовил вкусный соус для рыбы.', 'I already prepared a delicious sauce for the fish.', [], ''),
    ('senya', 'А я сейчас поставлю горячий суп на плиту.', 'And I will now put the hot soup on the stove.', [], ''),
    ('barinov', 'Сегодня каждое наше блюдо должно быть идеальным.', 'Today every dish of ours must be ideal.', [], ''),
    ('max', 'Хорошо, шеф, мы сделаем всё очень быстро!', 'Fine, chef, we will do everything very quickly!', [], ''),
]
WALK = [
    (0, None, "'Cooks, quickly stand at your places, everyone!' Barinov barks at the cooks to take their stations at once."),
    (1, None, "'Right now our restaurant is opening its doors for guests.' The dining room doors are opening and the first guests are arriving."),
    (2, None, "'Get started immediately with your work in the kitchen!' Viktor orders everyone to dive straight into their kitchen prep."),
    (3, None, "'Chef, why are you so very angry today?' Senya cautiously asks why the chef is in such a foul mood today."),
    (4, None, "'The new owner took away all my expensive alcohol!' Barinov fumes that the new owner confiscated his entire stash of fine liquor."),
    (5, None, "'Did he really forbid you to drink at work?' Max asks in disbelief whether Igor really banned him from drinking at work."),
    (6, None, "'Yes, now a dry law is in effect in the kitchen.' Viktor grimly calls the new rule a total 'dry law' in the kitchen."),
    (7, None, "'Without wine it will be hard for you to cook dishes.' Senya jokes that cooking without wine is going to be tough for the chef."),
    (8, None, "'Enough chatting, start cutting the fresh meat!' Barinov snaps at them to stop chatting and start slicing the fresh meat."),
    (9, None, "'I already prepared a delicious sauce for the fish.' Max reports that his fish sauce is already prepped and ready."),
    (10, None, "'And I will now put the hot soup on the stove.' Senya quickly adds that he is putting the hot soup on the stove right now."),
    (11, None, "'Today every dish of ours must be ideal.' With the new boss watching, Viktor demands perfection on every single plate."),
    (12, None, "'Fine, chef, we will do everything very quickly!' Max promises that the team will get everything out fast."),
]
