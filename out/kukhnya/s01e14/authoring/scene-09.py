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
OUTRO = "Kostya sets off for the dining room with the plates and a message from the kitchen. Remember 'priyatnogo appetita', the Russian bon appetit. Talk soon."
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
    (0, None, "'Kostya, the new order for the guests is ready.' 'Gotov', ready, matches 'zakaz', order, which is masculine. A dish, 'blyudo', would be 'gotovo', and a pizza 'gotova'."),
    (1, None, "'Great, show me these beautiful plates.' 'Pokazhi' is the order 'show!'. 'Eti krasivye tarelki' is all plural: 'eto' becomes 'eti', and 'tarelka', plate, becomes 'tarelki'."),
    (2, None, "'Here is a delicious French steak and hot fish.' 'Vot' is 'here is', for pointing at something. 'Ryba', fish, is feminine, so 'hot' is 'goryachaya'; 'steyk' is masculine and takes 'vkusny'."),
    (3, None, "'This dish looks very appetizing and expensive.' After 'vyglyadit', looks, Russian uses the 'o' words, 'appetitno' and 'dorogo', literally 'looks appetizingly and expensively'."),
    (4, None, "'I cooked this rare recipe for a long time.' 'Gotovil' is the kind of past that describes a process, so with 'dolgo', for a long time, it means 'I spent ages cooking'."),
    (5, None, "'Our guests in the hall are very hungry.' 'Golodnye' ends in 'ye' to match the plural 'gosti'. 'Zal', the hall or dining room, becomes 'v zale', in the hall."),
    (6, None, "'Then carry these plates right now.' 'Nesi' is 'carry!' when you carry by hand on foot. 'Pryamo seychas' is literally 'straight now', so 'this minute'."),
    (7, None, "'I will quickly take the hot food to the guests.' 'Otnesu' has 'ot', away, for 'carry over'. 'Gostyam' is 'to the guests', with the plural 'yam' ending meaning 'to'."),
    (8, None, "'Be sure to wish them bon appetit.' 'Priyatnogo appetita' is literally 'of pleasant appetite'. 'Pozhelat', to wish, puts what you wish into the 'of' form."),
    (9, None, "'Of course, I will do everything very politely.' 'Vezhlivo', politely, is the 'o' form of 'vezhlivy', polite. 'Vsyo sdelayu' is 'everything I'll do', with 'vsyo' first."),
    (10, None, "'Say that the chef cooked for them.' 'Ikh', them, gains an 'n' after little words like 'dlya', for: 'dlya nikh'. The same happens to 'nego' and 'ney'."),
    (11, None, "'Good, I will pass on your warm words.' 'Peredam' is 'I'll pass on'. Kostya calls Max 'ty', so it's 'tvoi tyoplye slova', with 'tvoi', your, in the plural for 'slova', words."),
    (12, None, "'Go quickly, the guests are already waiting for the order!' 'Skoree' is literally 'sooner', and 'idi skoree' is the everyday 'hurry up'. 'Zhdut zakaz' has no word for 'for'."),
]
