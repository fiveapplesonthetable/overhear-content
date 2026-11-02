# Authoring module for kukhnya-s01e06-scene-22.
ID = 'kukhnya-s01e06-scene-22'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 6
SCENE = 22
TITLE = 'Счёт за трюфели  (The Truffle Bill)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.06'
SOURCE_FILE = 'sources/kukhnya/s01/e06.ru.dual.srt'
INTRO = "The inspection is over, and at Claude Monet the truffles are back, returned by a homeless man called Rodion. Now Barinov wants to know how they ended up in the bin, and Max has to explain that where he comes from, a truffle is a sweet. It's in Russian first."
OPENER = "Let's go back through the confession. Max has a very good excuse, and Barinov has a very big bill."
TRANSITION = 'Now the confession from the top.'
OUTRO = 'Max\'s excuse is worth keeping: "v Voronezhe tryufeli", "eto tolko konfety", in Voronezh truffles are just sweets. It\'s the most honest line in the episode. See you next time.'
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('barinov', 'Макс, почему редкие трюфели оказались на помойке?', 'Max, why did rare truffles end up in the dumpster?', [], ''),
    ('max', 'Шеф, извините меня, пожалуйста!', 'Chef, forgive me, please!', [(298, 'Шеф, извините')], ''),
    ('max', 'Я раньше никогда не видел трюфелей.', 'I have never seen truffles before.', [(298, 'я никогда не видел трюфелей')], ''),
    ('barinov', 'Как ты мог выбросить такое сокровище?', 'How could you throw away such a treasure?', [], ''),
    ('max', 'В Воронеже трюфели — это только конфеты!', 'In Voronezh, truffles are only candies!', [(299, 'В Воронеже трюфеля это только конфеты.')], ''),
    ('barinov', 'Конфеты? Это самый дорогой гриб!', 'Candies? This is the most expensive mushroom!', [(300, 'Трюфели?')], ''),
    ('max', 'Я подумал, что они испортились.', 'I thought that they had spoiled.', [], ''),
    ('barinov', 'Хорошо, что бездомный вернул их нам.', 'Good thing the homeless man returned them to us.', [(293, 'Кто-то выбросил дивные трюфели')], ''),
    ('barinov', 'Ладно, я сегодня очень добрый.', 'Alright, I am very kind today.', [(301, 'Ладно, я сегодня добрый.')], ''),
    ('barinov', 'Мы успешно прошли сложную проверку.', 'We successfully passed the difficult inspection.', [(302, 'Мы проверку прошли.')], ''),
    ('barinov', 'Но счёт за его ужин оплатишь ты.', 'But you will pay the bill for his dinner.', [(302, 'счет за ужин Родиона Сергеевича надо будет оплатить')], ''),
    ('max', 'Двадцать две тысячи рублей?!', 'Twenty-two thousand roubles?!', [(303, 'Двадцать две тысячи?')], ''),
    ('barinov', 'Вот так ты запомнишь этот урок!', 'This is how you will remember this lesson!', [], ''),
]
WALK = [
    (0, None, ["'Max, why did rare truffles end up in the dumpster?' You can hear how he says ", ('barinov', 'оказались'), ', meaning ended up or found themselves in.']),
    (1, None, ["'Chef, forgive me, please!' Notice the polite way he uses ", ('max', 'извините'), ', to ask his boss to forgive him.']),
    (2, None, ["'I have never seen truffles before.' It is quite common to hear ", ('max', 'никогда'), ', meaning never, used alongside other similar words.']),
    (3, None, ["'How could you throw away such a treasure?' Listen carefully to the word for treasure, ", ('barinov', 'сокровище'), ', which he thinks the truffles certainly are.']),
    (4, None, ["'In Voronezh, truffles are only candies!' He mentions his hometown by saying ", ('max', 'Воронеже'), ', where these expensive mushrooms are just sweets.']),
    (5, None, ["'Candies? This is the most expensive mushroom!' The chef is shocked and uses ", ('barinov', 'дорогой'), ', pointing out how incredibly expensive they are.']),
    (6, None, ["'I thought that they had spoiled.' Max explains his honest mistake with ", ('max', 'испортились'), ', meaning that the food had gone bad.']),
    (7, None, ["'Good thing the homeless man returned them to us.' We learn that a homeless man, ", ('barinov', 'бездомный'), ', actually brought the expensive ingredients back inside.']),
    (8, None, ["'Alright, I am very kind today.' Barinov claims he is feeling quite ", ('barinov', 'добрый'), ', showing some rare kindness and mercy today.']),
    (9, None, ["'We successfully passed the difficult inspection.' He is happy because they successfully ", ('barinov', 'прошли'), ', making it through a very tough inspection.']),
    (10, None, ["'But you will pay the bill for his dinner.' The chef still wants someone to pay the ", ('barinov', 'счёт'), ', meaning the final bill for the meal.']),
    (11, None, ["'Twenty-two thousand roubles?!' Max can hardly believe it is twenty-two ", ('max', 'тысячи'), ', a massive amount for a simple mistake.']),
    (12, None, ["'This is how you will remember this lesson!' To finish, the chef hopes Max will ", ('barinov', 'запомнишь'), ', and remember this very expensive life lesson.']),
]
