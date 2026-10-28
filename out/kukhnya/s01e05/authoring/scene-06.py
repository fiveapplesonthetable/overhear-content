# Authoring module for kukhnya-s01e05-scene-06.
ID = 'kukhnya-s01e05-scene-06'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 5
SCENE = 6
TITLE = 'Кулинарная битва  (A Culinary Battle)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'fedya': 'Федя', 'max': 'Макс', 'senya': 'Сеня'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.05'
SOURCE_FILE = 'sources/kukhnya/s01/e05.ru.dual.srt'
INTRO = 'Meat cook Senya organizes a kitchen betting pool as fish cook Fedya and rookie Max prepare for a head-to-head culinary duel. With cod as the secret ingredient, the entire kitchen wagers on the outcome. Listen to the lively conversation in Russian first, and then we will examine every line.'
OPENER = "Let's examine this exciting kitchen showdown step by step."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'That concludes our sixth scene. In Kukhnya, cooking contests between proud chefs are always filled with fierce banter and high stakes. See you next time!'
CLOSING = ('max', 'До встречи!')
STORY = [
    ('senya', 'Итак, повара, делаем ставки и записываемся!', 'So, cooks, place bets and sign up!', [(85, 'Итак, ставим и записываемся')], ''),
    ('senya', 'Сейчас Федя и Макс приготовят по блюду.', 'Now Fedya and Max will prepare a dish each.', [(86, 'Сейчас Федя'), (86, 'будут готовить по одному блюду')], ''),
    ('senya', 'А шеф попробует и выберет победителя.', 'And the chef will taste and choose the winner.', [(87, 'А шеф попробует'), (87, 'кто из них победил')], ''),
    ('max', 'Какой главный продукт для нашего блюда?', 'What is the main ingredient for our dish?', [(88, 'Выбираем главный продукт для блюда')], ''),
    ('senya', 'Главный продукт сегодняшнего конкурса — треска!', "The main ingredient of today's contest is cod!", [(88, 'главный продукт')], ''),
    ('fedya', 'Тебе конец, огузок!', 'You are finished, runt!', [(89, 'И конец')], ''),
    ('fedya', 'Я готовил всю рыбу в океане!', 'I have cooked all the fish in the ocean!', [(89, 'Я готовил всю рыбу, которая плавает в океане')], ''),
    ('max', 'Рыбу я тоже умею готовить.', 'I also know how to cook fish.', [], ''),
    ('fedya', 'Посмотрим на твои жалкие умения.', 'We will see your pathetic skills.', [], ''),
    ('senya', 'Кто ставит пятьсот рублей на Федю?', 'Who bets five hundred rubles on Fedya?', [(95, 'пятьсот рублей'), (95, 'для ставки')], ''),
    ('fedya', 'Все повара на кухне ставят на меня.', 'All the cooks in the kitchen bet on me.', [(90, 'Спасибо')], ''),
    ('max', 'А я всё равно докажу свой талант!', 'And I will prove my talent anyway!', [], ''),
    ('senya', 'Время пошло, начинаем готовить прямо сейчас!', 'Time has started, begin cooking right now!', [], ''),
    ('max', 'Я сделаю самый лучший соус.', 'I will make the best sauce.', [], ''),
]
WALK = [
    (0, None, "'So, cooks, place bets and sign up!' Senya acts as the bookmaker for the kitchen showdown."),
    (1, None, "'Now Fedya and Max will prepare a dish each.' Senya lays out the rules for the upcoming duel."),
    (2, None, "'And the chef will taste and choose the winner.' Senya explains how the winner will be chosen."),
    (3, None, "'What is the main ingredient for our dish?' Max asks for the parameters of the challenge."),
    (4, None, "'The main ingredient of today's contest is cod!' Senya reveals the mandatory ingredient to everyone."),
    (5, None, "'You are finished, runt!' Fedya arrogantly tells his opponent to give up now."),
    (6, None, "'I have cooked all the fish in the ocean!' Fedya brags about his vast experience with seafood."),
    (7, None, "'I also know how to cook fish.' Max calmly asserts his own competence."),
    (8, None, "'We will see your pathetic skills.' Fedya scoffs at the rookie's supposed abilities."),
    (9, None, "'Who bets five hundred rubles on Fedya?' Senya tries to drum up more action for the betting pool."),
    (10, None, "'All the cooks in the kitchen bet on me.' Fedya revels in the universal support of his colleagues."),
    (11, None, "'And I will prove my talent anyway!' Max stays determined despite being the underdog."),
    (12, None, "'Time has started, begin cooking right now!' Senya officially kicks off the cooking competition."),
    (13, None, "'I will make the best sauce.' Max confidently promises to deliver a winning component."),
]
