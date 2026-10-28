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
INTRO = "It's prep time at Claude Monet, with knives going on every board. Barinov walks past, inspects the chopping, and then talks to Max about where good cooking starts: at the market. It's in Russian first, and you can leave the odd word."
OPENER = 'Slowly now. Barinov is giving orders, which means a lot of useful commands.'
TRANSITION = 'And the whole prep talk again.'
OUTRO = "You've heard 'first', 'faster' and 'without mistakes', which is a decent description of a trainee's day. Barinov's last order is the kind that sticks. See you next time."
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
    (0, None, "'So, cooks, chop all the vegetables.' The command starts with 'na' and ends in 'te', which is for a group. 'Vegetables' is a plural that ends in 'i'."),
    (1, None, "'Chef, we are already chopping onions.' 'We chop' ends in 'em'. 'onion' also means 'a bow', as in bow and arrow."),
    (2, None, "'Chop faster, guests will come soon.' This is the same word 'chop', now as a group command. 'Will come' is the future of 'arrive'."),
    (3, None, "'And where will we get fresh meat?' 'Where' asks about a place, not a direction. 'Will take' is the Russian way to say 'will get'."),
    (4, None, "'First a cook selects the best products.' 'First' is made from 'from' and 'beginning', so 'from the start'. 'Best' ends in 'ie', to match the plural 'products'."),
    (5, None, "'Do we buy meat in a shop?' Again no word for 'do', just the rising voice. 'In a shop' ends in 'e' for the place."),
    (6, None, "'No, I choose everything myself at the market.' 'Myself' sits before the action it stresses. The market takes 'na', not 'v', which is why it says 'on the market'."),
    (7, None, "'Do you personally inspect every piece?' Max says 'you' politely, so the action ends in 'ete'. 'Personally' is built from 'personal'."),
    (8, None, "'A real chef does not trust strangers.' 'Trust' is built from 'faith', so it is 'to give faith to'. 'Strangers' is made from 'someone else's', with an ending for 'to'."),
    (9, None, "'May I go with you?' 'Is it possible to me' is the standard way to ask permission. 'With you' is the polite 'you', in the 'with' form."),
    (10, None, "'You will stay in the kitchen peeling potatoes.' 'You will stay' ends in 'sya'. 'potato' here is the everyday one."),
    (11, None, "'I dreamed of selecting the best products.' 'Dreamed' is built from 'a dream'. The 'l' at the end shows the speaker is a man."),
    (12, None, "'First learn to cut without mistakes!' 'Learn' ends in 'sya', so it is 'teach yourself'. 'Without mistakes' puts the ending 'ok' on 'mistake'."),
]
