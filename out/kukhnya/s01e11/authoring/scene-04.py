# Authoring module for kukhnya-s01e11-scene-04.
ID = 'kukhnya-s01e11-scene-04'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 11
SCENE = 4
TITLE = 'Возвращение на кухню  (Return to the Kitchen)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.11'
SOURCE_FILE = 'sources/kukhnya/s01/e11.ru.dual.srt'
INTRO = 'Max has been sent to wash dishes, and he has taken the order literally. Barinov finds him sitting around and wants to know who suspended him. Here goes.'
OPENER = "Now let's take it slowly."
TRANSITION = 'Here it is, all together.'
OUTRO = 'Max is back at his station with a pile of tickets and a pan in his hands. He is a good deal happier than he was. See you in a moment.'
CLOSING = ('max', 'Пока!')
STORY = [
    ('barinov', 'Макс, ты что здесь прохлаждаешься?', 'Max, why are you slacking off here?', [(58, 'Ты что это здесь прохлаждаешься?')], ''),
    ('max', 'Что мне еще делать, шеф?', 'What else am I to do, chef?', [(59, 'Что мне еще делать, шеф?')], ''),
    ('max', 'Меня сегодня отстранили от работы.', 'I was suspended from work today.', [(60, 'Меня же сегодня отстранили от работы.')], ''),
    ('barinov', 'Кто тебя отстранил? Я?', 'Who suspended you? Me?', [(61, 'Кто тебя отстранил? Я?')], ''),
    ('max', 'Виктория Сергеевна сказала сидеть здесь.', 'Viktoria Sergeyevna told me to sit here.', [], ''),
    ('barinov', 'С каких пор ты её слушаешь?', 'Since when do you listen to her?', [(62, 'С каких пор ты стал слушать')], ''),
    ('barinov', 'На этой кухне главный только я!', 'In this kitchen, only I am the boss!', [], ''),
    ('max', 'Она обещала меня уволить, шеф.', 'She promised to fire me, chef.', [], ''),
    ('barinov', 'Увольнять поваров могу только я!', 'Only I can fire cooks!', [], ''),
    ('barinov', 'А ну марш на кухню!', 'Now march to the kitchen!', [(63, 'марш на кухне')], ''),
    ('barinov', 'Там тебя куча чеков дожидается.', 'A pile of orders is waiting for you there.', [(63, 'там тебе куча чеков дождается.')], ''),
    ('max', 'Спасибо, шеф, я бегу!', 'Thank you, chef, I am running!', [(64, 'Спасибо, шеф.')], ''),
    ('barinov', 'Стой, куда ты понес сковороду?', 'Wait, where are you carrying that pan?', [(65, 'Куда понес?')], ''),
    ('max', 'На рабочее место, шеф!', 'To the workstation, chef!', [], ''),
]
WALK = [
    (0, None, ["'Max, why are you slacking off here?' We can consider this line: ", ('barinov', 'прохлаждаешься'), " means 'cooling yourself off', from the noun for 'coolness', a relative of 'cold'. You can use it for someone taking it easy."]),
    (1, None, ["'What else am I to do, chef?' The expression is ", ('max', 'Что'), ('max', 'мне'), ('max', 'еще'), ('max', 'делать'), ", 'what to me still to do'. ", ('max', 'делать'), " is 'to do', in the dictionary form. It's the question of a worker who has been given no job."]),
    (2, None, ["'I was suspended from work today.' Now let's focus on the phrase: ", ('max', 'отстранили'), " is 'they moved aside', with nobody named: the ending says 'they' without saying who. ", ('max', 'от'), ('max', 'работы'), " is 'from work'."]),
    (3, None, ["'Who suspended you? Me?' Barinov repeats the verb, now as ", ('barinov', 'отстранил'), ", with a masculine ending. The pause between 'who' and 'I' is the joke. He cannot bear that anyone else makes decisions in his kitchen."]),
    (4, None, ["'Viktoria Sergeyevna told me to sit here.' First name plus father's name, ", ('max', 'Сергеевна'), ', is the polite way to name the art director. And ', ('max', 'сказала'), ('max', 'сидеть'), ", 'said to sit', needs no 'that' between."]),
    (5, None, ["'Since when do you listen to her?' The expression is ", ('barinov', 'С'), ('barinov', 'каких'), ('barinov', 'пор'), ", 'from which times', for 'since when'. ", ('barinov', 'слушаешь'), ", 'listen', means 'obey' here, as in English 'listen to your mother'."]),
    (6, None, ["'In this kitchen, only I am the boss!' Let's break down the phrase: ", ('barinov', 'главный'), ", 'main', is the chunk from 'who is the most important'. ", ('barinov', 'только'), ('barinov', 'я'), ", 'only I', puts the stress on him. ", ('barinov', 'На'), ('barinov', 'этой'), ('barinov', 'кухне'), " is 'on this kitchen'."]),
    (7, None, ["'She promised to fire me, chef.' Now let's look at this line: ", ('max', 'обещала'), ", 'promised', has a feminine ending, because a woman made the promise. ", ('max', 'уволить'), ", 'to fire', gives the term Alisa used when she threatened Lyova. ", ('max', 'меня'), " is 'me'."]),
    (8, None, ["'Only I can fire cooks!' Let us break down this line: ", ('barinov', 'Увольнять'), ", 'to fire', here is the form for doing it again and again, as a power. ", ('barinov', 'поваров'), " is the noun for 'cooks', as the ones being fired. ", ('barinov', 'могу'), " is 'I can'."]),
    (9, None, ["'Now march to the kitchen!' Now let's break down this line: ", ('barinov', 'А'), ('barinov', 'ну'), " is a push, something like 'come on, now'. ", ('barinov', 'марш'), " is a military 'march'. ", ('barinov', 'на'), ('barinov', 'кухню'), " is 'to the kitchen', the same as in Vika's order."]),
    (10, None, ["'A pile of orders is waiting for you there.' Let us inspect the sentence: ", ('barinov', 'куча'), ", 'heap', is everyday speech for 'lots'. The order slips are ", ('barinov', 'чеков'), ", 'checks'. ", ('barinov', 'дожидается'), " is 'waits until you come', from the verb 'to wait'."]),
    (11, None, ["'Thank you, chef, I am running!' We will look at the speech: ", ('max', 'бегу'), " is 'I run', said in the middle of the movement. You can say 'I run' for 'I'm on my way!'. Max is delighted."]),
    (12, None, ["'Wait, where are you carrying that pan?' Now let's consider the sentence: ", ('barinov', 'понес'), " means 'carried', with a prefix for setting off, so Barinov catches him in the act. The noun for pan becomes ", ('barinov', 'сковороду'), ', as the thing carried. ', ('barinov', 'Стой'), " is 'stop'."]),
    (13, None, ["'To the workstation, chef!' Let us break down the phrase: ", ('max', 'На'), ('max', 'рабочее'), ('max', 'место'), " means 'to the working place'. ", ('max', 'рабочее'), " comes from the noun for 'work'. Max keeps hold of the pan, and the scene ends."]),
]
