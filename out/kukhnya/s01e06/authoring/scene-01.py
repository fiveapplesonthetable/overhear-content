# Authoring module for kukhnya-s01e06-scene-01.
ID = 'kukhnya-s01e06-scene-01'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 6
SCENE = 1
TITLE = 'Путь на тарелку  (The Journey to the Plate)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kostya': 'Костя', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.06'
SOURCE_FILE = 'sources/kukhnya/s01/e06.ru.dual.srt'
INTRO = "Kukhnya means The Kitchen. It's a Russian comedy about Claude Monet, a smart Moscow restaurant where the chef, Barinov, rules the kitchen and everyone else survives as best they can. This is from episode six. Before the evening rush, Max, the young cook, and Kostya, the bartender he shares a flat with, look out at the guests and talk about what they never see. You'll hear it in Russian first, and it's fine to miss words."
OPENER = "Now slowly. It's a calm scene, so the sentences are short and nearly all of them are worth keeping."
TRANSITION = 'Here it is again in one go. It should feel more familiar now.'
OUTRO = 'Keep "kazhdyy vecher", every evening, and "kazhdoe blyudo", every dish: one word for \'every\', with its ending changed to fit. See you next time.'
CLOSING = ('kostya', 'Пока!')
STORY = [
    ('kostya', 'Макс, посмотри на гостей в зале.', 'Max, look at the guests in the dining room.', [], ''),
    ('max', 'Они заказывают наши фирменные блюда.', 'They are ordering our specialty dishes.', [(1, 'заказываете любимое блюдо')], ''),
    ('kostya', 'Люди приходят сюда каждый вечер.', 'People come here every evening.', [(1, 'Когда вы приходите в ресторан')], ''),
    ('max', 'Каждый выбирает своё любимое блюдо.', 'Everyone chooses their favorite dish.', [(1, 'любимое блюдо')], ''),
    ('kostya', 'Они не думают о пути еды.', "They do not think about the food's journey.", [(2, 'вы наверняка не задумываетесь, какой путь')], ''),
    ('max', 'Какое блюдо проходит длинный путь?', 'Which dish travels a long way?', [(2, 'путь оно проделывает')], ''),
    ('kostya', 'Каждое блюдо начинает путь на рынке.', 'Every dish begins its journey at the market.', [(3, 'чтобы оказаться у вас на тарелке')], ''),
    ('max', 'Потом повара готовят заказ на кухне.', 'Then the cooks prepare the order in the kitchen.', [], ''),
    ('kostya', 'Вся кухня работает ради одной тарелки.', 'The whole kitchen works for one plate.', [], ''),
    ('max', 'Повара очень спешат и нервничают.', 'The cooks rush very much and get nervous.', [], ''),
    ('kostya', 'А гости видят только вкусный результат.', 'And guests only see the delicious result.', [], ''),
    ('max', 'Для них это настоящий праздник вкуса.', 'For them this is a real celebration of taste.', [], ''),
    ('kostya', 'Скоро начнётся наш обычный рабочий вечер.', 'Soon our usual working evening will begin.', [], ''),
]
WALK = [
    (0, None, ["'Max, look at the guests in the dining room.' Notice how the dining room is called ", ('kostya', 'зале'), ', which usually means a large hall.']),
    (1, None, ["'They are ordering our specialty dishes.' The chefs take great pride in their specialty or signature items, known as ", ('max', 'фирменные'), '.']),
    (2, None, ["'People come here every evening.' You will hear the word for every, ", ('kostya', 'каждый'), ', used here to describe their daily routine.']),
    (3, None, ["'Everyone chooses their favorite dish.' When talking about a favorite thing, you can use the word ", ('max', 'любимое'), ', which comes from the word for love.']),
    (4, None, ["'They do not think about the food's journey.' It is interesting that the word for journey or path is ", ('kostya', 'пути'), ', describing where the food has been.']),
    (5, None, ["'Which dish travels a long way?' To emphasize that the distance is long, the cook says ", ('max', 'длинный'), ' before the word for path.']),
    (6, None, ["'Every dish begins its journey at the market.' Everything starts at the fresh food market, which is called ", ('kostya', 'рынке'), ' in this sentence.']),
    (7, None, ["'Then the cooks prepare the order in the kitchen.' The magic happens back in the kitchen, referred to as ", ('max', 'кухне'), ' by the staff.']),
    (8, None, ["'The whole kitchen works for one plate.' All this effort is done for the sake of the guest, expressed with ", ('kostya', 'ради'), '.']),
    (9, None, ["'The cooks rush very much and get nervous.' Things get very busy and intense, so they use the word ", ('max', 'очень'), ' to mean very much.']),
    (10, None, ["'And guests only see the delicious result.' The diners only experience the delicious end product, with delicious being ", ('kostya', 'вкусный'), '.']),
    (11, None, ["'For them this is a real celebration of taste.' A wonderful meal feels like a real celebration or holiday, translated as ", ('max', 'праздник'), '.']),
    (12, None, ["'Soon our usual working evening will begin.' Before long, the evening shift will start, which is why they say ", ('kostya', 'Скоро'), ' for soon.']),
]
