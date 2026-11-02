# Authoring module for kukhnya-s01e14-scene-09.
ID = 'kukhnya-s01e14-scene-09'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 14
SCENE = 9
TITLE = 'Французские блюда  (French Dishes)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kostya': 'Костя', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.14'
SOURCE_FILE = 'sources/kukhnya/s01/e14.ru.dual.srt'
INTRO = 'In the kitchen, Max has finished the special French dishes. He calls Kostya to carry them to the VIP table. Listen to the two of them in Russian.'
OPENER = 'Slowly now, plate by plate.'
TRANSITION = 'Now the whole order again.'
OUTRO = "Kostya sets off for the dining room with the plates and a message from the kitchen. Remember the phrase for bon appetit. Talk soon."
CLOSING = ('max', 'Пока!')
STORY = [
    ('max', 'Костя, новый заказ для гостей готов.', 'Kostya, the new order for the guests is ready.', [], ''),
    ('kostya', 'Отлично, покажи мне эти красивые тарелки.', 'Great, show me these beautiful plates.', [], ''),
    ('max', 'Вот вкусный французский стейк и горячая рыба.', 'Here is a delicious French steak and hot fish.', [(169, 'Филиминьон по-фламански, лангусты а-ля Франце.')], ''),
    ('kostya', 'Это блюдо выглядит очень аппетитно и дорого.', 'This dish looks very appetizing and expensive.', [], ''),
    ('max', 'Я долго готовил этот редкий рецепт.', 'I cooked this rare recipe for a long time.', [], ''),
    ('kostya', 'Наши гости в зале очень голодные.', 'Our guests in the hall are very hungry.', [], ''),
    ('max', 'Тогда неси эти тарелки прямо сейчас.', 'Then carry these plates right now.', [], ''),
    ('kostya', 'Я быстро отнесу горячую еду гостям.', 'I will quickly take the hot food to the guests.', [], ''),
    ('max', 'Обязательно пожелай им приятного аппетита.', 'Be sure to wish them bon appétit.', [], ''),
    ('kostya', 'Конечно, я всё сделаю очень вежливо.', 'Of course, I will do everything very politely.', [], ''),
    ('max', 'Скажи, что шеф готовил для них.', 'Say that the chef cooked for them.', [], ''),
    ('kostya', 'Хорошо, я передам твои тёплые слова.', 'Good, I will pass on your warm words.', [], ''),
    ('max', 'Иди скорее, гости уже ждут заказ!', 'Go quickly, the guests are already waiting for the order!', [], ''),
]
WALK = [
    (0, None, ["'Kostya, the new order for the guests is ready.' We will inspect the words: ", ('max', 'готов'), ', ready, matches ', ('max', 'заказ'), ', order, which is masculine. A dish would be neuter, and a pizza feminine.']),
    (1, None, ["'Great, show me these beautiful plates.' Let's analyze this part: ", ('kostya', 'покажи'), " is the order 'show!'. ", ('kostya', 'эти'), ('kostya', 'красивые'), ('kostya', 'тарелки'), " is all plural: 'this' becomes these, and plate becomes ", ('kostya', 'тарелки'), '.']),
    (2, None, ["'Here is a delicious French steak and hot fish.' We will examine the dialogue: ", ('max', 'Вот'), " is 'here is', for pointing at something. ", ('max', 'рыба'), ", fish, is feminine, so 'hot' is ", ('max', 'горячая'), '; ', ('max', 'стейк'), ' is masculine and takes ', ('max', 'вкусный'), '.']),
    (3, None, ["'This dish looks very appetizing and expensive.' After ", ('kostya', 'выглядит'), ", looks, Russian uses the 'o' words, ", ('kostya', 'аппетитно'), ' and ', ('kostya', 'дорого'), ", meaning 'looks appetizingly and expensively'."]),
    (4, None, ["'I cooked this rare recipe for a long time.' Now we can look at the phrase: ", ('max', 'готовил'), ' is the kind of past that describes a process, so with ', ('max', 'долго'), ", for a long time, it means 'I spent ages cooking'."]),
    (5, None, ["'Our guests in the hall are very hungry.' We will consider the dialogue: ", ('kostya', 'голодные'), " ends in 'ye' to match the plural ", ('kostya', 'гости'), '. The hall or dining room becomes ', ('kostya', 'в'), ('kostya', 'зале'), ', in the hall.']),
    (6, None, ["'Then carry these plates right now.' We will focus on the phrase: ", ('max', 'неси'), " is 'carry!' when you carry by hand on foot. ", ('max', 'прямо'), ('max', 'сейчас'), " reads 'straight now', so 'this minute'."]),
    (7, None, ["'I will quickly take the hot food to the guests.' Let's focus on the speech: ", ('kostya', 'отнесу'), " has the away prefix for 'carry over'. ", ('kostya', 'гостям'), " means 'to the guests', with that plural ending meaning 'to'."]),
    (8, None, ["'Be sure to wish them bon appétit.' Let's break down the phrase: ", ('max', 'приятного'), ('max', 'аппетита'), " says 'of pleasant appetite'. To wish puts what you wish into the 'of' form."]),
    (9, None, ["'Of course, I will do everything very politely.' Now let's break down the words: ", ('kostya', 'вежливо'), ", politely, is the 'o' form of polite. ", ('kostya', 'всё'), ('kostya', 'сделаю'), " is 'everything I will do', with ", ('kostya', 'всё'), ' first.']),
    (10, None, ["'Say that the chef cooked for them.' Them gains an 'n' after little words like ", ('max', 'для'), ', for: ', ('max', 'для'), ('max', 'них'), '. The same happens to him and her.']),
    (11, None, ["'Good, I will pass on your warm words.' Now let's examine the speech: ", ('kostya', 'передам'), " is 'I will pass on'. Kostya calls Max the informal 'you', so it is ", ('kostya', 'твои'), ('kostya', 'тёплые'), ('kostya', 'слова'), ', with ', ('kostya', 'твои'), ', your, in the plural for ', ('kostya', 'слова'), ', words.']),
    (12, None, ["'Go quickly, the guests are already waiting for the order!' We can consider the words: ", ('max', 'скорее'), " means 'sooner', and ", ('max', 'Иди'), ('max', 'скорее'), " carries an everyday 'hurry up'. ", ('max', 'ждут'), ('max', 'заказ'), " drops 'for'."]),
]
