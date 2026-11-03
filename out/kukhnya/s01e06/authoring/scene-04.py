# Authoring module for kukhnya-s01e06-scene-04.
ID = 'kukhnya-s01e06-scene-04'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 6
SCENE = 4
TITLE = 'Баранина и трюфели  (Mutton and Truffles)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'timur': 'Тимур'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.06'
SOURCE_FILE = 'sources/kukhnya/s01/e06.ru.dual.srt'
INTRO = "Out at the back of Claude Monet, Chef Barinov meets Timur, who sells him meat and anything else he can lay his hands on. They haggle over a lamb, and then Timur brings out something much more expensive. It's in Russian first."
OPENER = "Let's take it line by line. Bargaining is a good place to pick up prices and numbers."
TRANSITION = 'Now the whole deal again, start to finish.'
OUTRO = "Timur's haggling trick of raising the price instead of lowering it is classic market theatre, and Barinov still walks away with prized truffles in hand. See you next time."
CLOSING = ('barinov', 'До встречи!')
STORY = [
    ('barinov', 'Скажи честно, этот баран умер от старости?', 'Tell me honestly, did this sheep die of old age?', [(7, 'Скажи честно, Тимур, ведь этот баран умер от старости')], ''),
    ('timur', 'Зачем обижаешь? Это молодой и вкусный ягнёнок!', 'Why insult me? This is a young and tasty lamb!', [(8, 'зачем обижаешь'), (9, 'молодой и вкусный ягненок')], ''),
    ('barinov', 'У меня на кухне уже хватает баранов.', 'I already have enough sheep in the kitchen.', [(12, 'у меня такие бараны')], ''),
    ('timur', 'Подожди, посмотри вот это отличное мясо!', 'Wait, look at this excellent meat!', [(13, 'подожди. Вот, посмотри вот этого'), (14, 'на этом мясе')], ''),
    ('timur', 'Клянусь, это самое лучшее свежее мясо!', 'I swear, this is the best fresh meat!', [(14, 'Клянусь'), (14, 'на этом мясе')], ''),
    ('barinov', 'Да, этот ягнёнок действительно хороший.', 'Yes, this lamb is really good.', [(15, 'Да, это хороший')], ''),
    ('barinov', 'Хорошо, я беру это мясо.', 'Fine, I will take this meat.', [(17, 'Хорошо, беру')], ''),
    ('timur', 'Шеф, дорогой, а трюфели тебе надо?', 'Chef, my dear, do you need truffles?', [(18, 'Шеф, брат, трюфеля надо')], ''),
    ('barinov', 'Ты опять предлагаешь мне контрабанду?', 'Are you offering me contraband again?', [(20, 'ты опять'), (21, 'Контрабанду мне предлагаешь')], ''),
    ('barinov', 'Конечно надо! Почём ты их продаёшь?', 'Of course I do! How much are you selling them for?', [(21, 'Конечно, надо'), (22, 'Почем')], ''),
    ('timur', 'Тебе по-братски всего шестьсот евро за килограмм.', 'For you as a friend, only six hundred euros per kilogram.', [(22, 'Тебе по-братски всего'), (22, '600 евро за килограмм')], ''),
    ('barinov', 'Отлично, я беру эти трюфели!', 'Great, I will take these truffles!', [(23, 'беру, давай')], ''),
    ('timur', 'Тогда цена выросла до семисот евро!', 'Then the price has risen to seven hundred euros!', [(23, 'Тогда 700')], ''),
    ('barinov', 'Тимур, не наглей и отдавай товар!', "Timur, don't get cheeky and hand over the goods!", [(24, 'Тимур, не наглей')], ''),
]
WALK = [
    (0, None, ["'Tell me honestly, did this sheep die of old age?' Let's begin with the word for sheep, ", ('barinov', 'баран'), ', which is often used as a playful insult to call someone a blockhead.']),
    (1, None, ["'Why insult me? This is a young and tasty lamb!' Notice how the seller points out that it is a very young lamb, calling it ", ('timur', 'ягнёнок'), ', finishing with a sound often used for baby animals.']),
    (2, None, ["'I already have enough sheep in the kitchen.' The chef complains about his cooks, saying there is already plenty, or ", ('barinov', 'хватает'), ', of them in his kitchen.']),
    (3, None, ["'Wait, look at this excellent meat!' If you want to tell someone to hold on a moment, say ", ('timur', 'Подожди'), ', just like the merchant does to stop the chef from leaving.']),
    (4, None, ["'I swear, this is the best fresh meat!' Listen closely to the merchant making a strong promise with ", ('timur', 'Клянусь'), ', meaning I swear, which you might hear often at any local market.']),
    (5, None, ["'Yes, this lamb is really good.' When you agree that something is truly excellent, the word ", ('barinov', 'действительно'), ' adds a strong sense of reality to your statement.']),
    (6, None, ["'Fine, I will take this meat.' Once a decision is finally made, the buyer simply states ", ('barinov', 'беру'), ' to declare that they are taking the item.']),
    (7, None, ["'Chef, my dear, do you need truffles?' Pay attention to this friendly address, ", ('timur', 'дорогой'), ', which means dear but can also describe something very expensive.']),
    (8, None, ["'Are you offering me contraband again?' A hint of annoyance shows through when the chef says ", ('barinov', 'опять'), ' to complain that this is happening yet another time.']),
    (9, None, ["'Of course I do! How much are you selling them for?' The most natural market way to ask for a price is ", ('barinov', 'Почём'), ', asking how much something costs piece by piece.']),
    (10, None, ["'For you as a friend, only six hundred euros per kilogram.' Offering a special discount to a friend, the seller uses ", ('timur', 'по-братски'), ' to suggest he is treating the buyer like a brother.']),
    (11, None, ["'Great, I will take these truffles!' Showing great enthusiasm for the deal, the chef exclaims ", ('barinov', 'Отлично'), ' to show that everything is perfectly fine.']),
    (12, None, ["'Then the price has risen to seven hundred euros!' Seeing the sudden interest, the merchant notes that the price has grown, using ", ('timur', 'выросла'), ' to raise the cost immediately.']),
    (13, None, ["'Timur, don't get cheeky and hand over the goods!' Telling someone not to be too cheeky or brazen involves the word ", ('barinov', 'наглей'), ', putting a firm stop to the rising price trick.']),
]
