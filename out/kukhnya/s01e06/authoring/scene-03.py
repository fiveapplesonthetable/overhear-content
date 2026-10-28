# Authoring module for kukhnya-s01e06-scene-03.
ID = 'kukhnya-s01e06-scene-03'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 6
SCENE = 3
TITLE = 'Секрет лучших продуктов  (The Secret of the Best Products)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.06'
SOURCE_FILE = 'sources/kukhnya/s01/e06.ru.dual.srt'
INTRO = "In the prep area of Claude Monet, knives click against cutting boards as cooks chop vegetables for dinner service. Chef Viktor Barinov inspects their technique and reminds young Max that culinary greatness begins long before cooking, with selecting the finest raw products at the market. Let's listen to their exchange in Russian first."
OPENER = "Now let's examine Barinov and Max's prep discussion line by line."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Leaving Max to master chopping onions and peeling potatoes, Chef Barinov sets off for the morning market to inspect Timur's meat and negotiate for fresh delicacies. Next time you watch the episode, listen for the Russian expressions for 'fast' and 'to take' — you will catch every word right away. See you next time!"
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('barinov', 'Так, повара, нарежьте все овощи.', 'So, cooks, chop all the vegetables.', [(5, 'Режут')], ''),
    ('max', 'Шеф, мы уже режем лук.', 'Chef, we are already chopping onions.', [(5, 'Режут')], ''),
    ('barinov', 'Режьте быстрее, гости скоро придут.', 'Chop faster, guests will come soon.', [], ''),
    ('max', 'А где мы возьмём свежее мясо?', 'And where will we get fresh meat?', [], ''),
    ('barinov', 'Сначала повар выбирает лучшие продукты.', 'First a cook selects the best products.', [(6, 'Но сначала для вашего блюда выбирают лучшие продукты')], ''),
    ('max', 'Мы покупаем мясо в магазине?', 'Do we buy meat in a shop?', [], ''),
    ('barinov', 'Нет, я сам выбираю всё на рынке.', 'No, I choose everything myself at the market.', [(6, 'выбирают лучшие продукты')], ''),
    ('max', 'Вы лично проверяете каждый кусок?', 'Do you personally inspect every piece?', [], ''),
    ('barinov', 'Настоящий шеф не доверяет чужим людям.', 'A real chef does not trust strangers.', [], ''),
    ('max', 'Можно мне поехать с вами?', 'May I go with you?', [], ''),
    ('barinov', 'Ты останешься на кухне чистить картошку.', 'You will stay in the kitchen peeling potatoes.', [], ''),
    ('max', 'Я мечтал выбирать лучшие продукты.', 'I dreamed of selecting the best products.', [], ''),
    ('barinov', 'Сначала научись резать без ошибок!', 'First learn to cut without mistakes!', [(5, 'Режут')], ''),
]
WALK = [
    (0, None, "'So, cooks, chop all the vegetables.' Clapping his hands, Barinov barks orders at the kitchen staff to speed up their prep work."),
    (1, None, "'Chef, we are already chopping onions.' Max tries to show they are already on top of the chopping tasks."),
    (2, None, "'Chop faster, guests will come soon.' Demanding a quicker pace, Barinov notes the dinner rush is approaching."),
    (3, None, "'And where will we get fresh meat?' Max asks where the restaurant sources its primary protein."),
    (4, None, "'First a cook selects the best products.' Explaining a fundamental rule, Barinov stresses starting with top-tier ingredients."),
    (5, None, "'Do we buy meat in a shop?' Max naively assumes they just go to a regular commercial supplier."),
    (6, None, "'No, I choose everything myself at the market.' Proudly, Barinov states he personally handpicks their supplies."),
    (7, None, "'Do you personally inspect every piece?' Max is impressed by the chef's hands-on approach to quality control."),
    (8, None, "'A real chef does not trust strangers.' Revealing his paranoid but effective philosophy, Barinov scoffs at trusting suppliers."),
    (9, None, "'May I go with you?' Eagerly, Max asks to tag along on the important market run."),
    (10, None, "'You will stay in the kitchen peeling potatoes.' Barinov bluntly assigns him to the most tedious prep job instead."),
    (11, None, "'I dreamed of selecting the best products.' He sighs, Max expresses disappointment at being left behind with the peeling."),
    (12, None, "'First learn to cut without mistakes!' Barinov firmly tells him to master the basics before dreaming of higher duties."),
]
