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
INTRO = 'In the hallway, Chef Viktor Barinov spots Max sitting idle after Victoria suspended him. Furious that someone else is giving orders to his cooks, Viktor fiercely asserts his kitchen authority and sends Max back to work. Listen to their conversation in Russian first, and then we will examine each sentence.'
OPENER = 'Now, let us examine the vocabulary and phrasing of this energetic backstage encounter.'
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "A lively scene demonstrating Chef Barinov's fiery defiance of restaurant management. Next time you watch the episode, listen for the Russian expressions for 'to run' and 'always' — you will catch every word right away. See you next time!"
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
    (0, None, "'Max, why are you slacking off here?' Barinov demands to know why his cook is slacking off here. He says 'prokhlazhdaeshsya', meaning chilling out. He expects everyone to be working."),
    (1, None, "'What else am I to do, chef?' Max asks the chef what else he is supposed to do. He sounds helpless. He is just following orders."),
    (2, None, "'I was suspended from work today.' Max explains he was suspended from work today. He uses 'otstranili', which means they removed him. He is not allowed to cook."),
    (3, None, "'Who suspended you? Me?' Barinov asks who suspended him and points out it was not him. He is confused and a bit angry. He asks 'kto' meaning who."),
    (4, None, "'Viktoria Sergeyevna told me to sit here.' Max tells him the director told him to sit here. He is just following her rules. 'Skazala sidet' means told to sit."),
    (5, None, "'Since when do you listen to her?' Barinov asks since when the young man listens to her. He is annoyed. 'S kakikh por' means since what times."),
    (6, None, "'In this kitchen, only I am the boss!' Barinov proudly states that in this kitchen, only he is the boss. He is asserting his authority. 'Glavnyy' means the main one."),
    (7, None, "'She promised to fire me, chef.' Max mentions she promised to fire him. He is worried about his job. 'Obeshchala' means she promised."),
    (8, None, "'Only I can fire cooks!' Barinov insists that only he can fire cooks. He wants to show the director does not control the kitchen. 'Uvolnyat' means to fire."),
    (9, None, "'Now march to the kitchen!' Barinov orders him to march to the kitchen right now. He says 'marsh' just like the English word. He wants his cook back to work."),
    (10, None, "'A pile of orders is waiting for you there.' Barinov says a pile of orders is waiting for him there. 'Kucha chekov' literally means a pile of receipts. They are busy."),
    (11, None, "'Thank you, chef, I am running!' Max thanks the chef and says he is running. He is happy to be back. 'Ya begu' means I am running."),
    (12, None, "'Wait, where are you carrying that pan?' Barinov stops him and asks where he is carrying that pan. He notices his cook has something. 'Kuda' means where to."),
    (13, None, "'To the workstation, chef!' Max replies he is taking it to his workstation. He is ready to cook. 'Rabochee mesto' is his working place."),
]
