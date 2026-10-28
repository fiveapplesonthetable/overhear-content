# Authoring module for kukhnya-s01e03-scene-16.
ID = 'kukhnya-s01e03-scene-16'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 3
SCENE = 16
TITLE = 'Комплимент от шефа  (A Compliment from the Chef)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'vadim': 'Вадим'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.03'
SOURCE_FILE = 'sources/kukhnya/s01/e03.ru.dual.srt'
INTRO = "Chef Viktor Barinov personally brings a complimentary birthday course to a table of influential guests. The guest of honor is delighted and hints at useful connections, but the chef's perfectionism takes over upon tasting. Listen to their polite conversation in Russian first, then we will break down each line in English."
OPENER = 'Now let us go through each phrase to see how it works in Russian.'
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Chef Barinov refuses to let an over-peppered sauce ruin his reputation, whisking the plate away to be remade. Until then! Next time you watch the episode, listen for the Russian expressions for 'dish' and 'big' — you will catch every word right away. See you next time!"
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('barinov', 'Добрый вечер, дорогие гости нашего ресторана!', 'Good evening, dear guests of our restaurant!', [(280, 'Добрый вечер')], ''),
    ('vadim', 'Добрый вечер, шеф-повар!', 'Good evening, head chef!', [(280, 'Добрый вечер')], ''),
    ('barinov', 'Я принёс вам особенный сюрприз.', 'I brought you a special surprise.', [(283, 'маленький сюрприз')], ''),
    ('barinov', 'Это комплимент в честь дня рождения.', 'This is a compliment in honor of the birthday.', [(284, 'Это комплимент от шефа'), (284, 'дня рождения')], ''),
    ('vadim', 'Спасибо большое, всё выглядит очень вкусно!', 'Thank you very much, everything looks very delicious!', [(285, 'Все так вкусно')], ''),
    ('vadim', 'Я вижу, что вы отличный повар.', 'I see that you are an excellent cook.', [(286, 'я вижу')], ''),
    ('vadim', 'Я могу вам помочь в городе.', 'I can help you in the city.', [(287, 'могу вам кое-чем помочь')], ''),
    ('vadim', 'Позвоните мне завтра в любое время.', 'Call me tomorrow at any time.', [(288, 'Позвоните мне завтра')], ''),
    ('barinov', 'Спасибо, для меня это большая честь!', 'Thank you, this is a great honor for me!', [], ''),
    ('barinov', 'Подождите, я сначала сам попробую блюдо.', 'Wait, I will taste the dish myself first.', [(289, 'я сначала попробую')], ''),
    ('barinov', 'Ой, повар слишком сильно переперчил соус!', 'Oh, the cook put way too much pepper in the sauce!', [(290, 'Переперчел')], ''),
    ('vadim', 'А по-моему, получилось довольно вкусно.', 'And in my opinion, it turned out quite delicious.', [(293, 'По-моему, вкусно')], ''),
    ('barinov', 'Нет, я немедленно всё переделаю!', 'No, I will immediately redo everything!', [(292, 'Я переделаю и принесу')], ''),
    ('barinov', 'Я лично принесу вам идеальное блюдо.', 'I will personally bring you an ideal dish.', [(292, 'Я переделаю и принесу')], ''),
]
WALK = [
    (0, None, "'Good evening, dear guests of our restaurant!' Barinov greets the guests of the restaurant in the evening."),
    (1, None, "'Good evening, head chef!' Vadim returns the greeting to the head chef."),
    (2, None, "'I brought you a special surprise.' He announces he has brought a special surprise."),
    (3, None, "'This is a compliment in honor of the birthday.' Barinov explains this is a complimentary dish for the birthday celebration."),
    (4, None, "'Thank you very much, everything looks very delicious!' Vadim expresses gratitude and says everything looks delicious."),
    (5, None, "'I see that you are an excellent cook.' He compliments him as an excellent cook."),
    (6, None, "'I can help you in the city.' Vadim offers his help in the city."),
    (7, None, "'Call me tomorrow at any time.' He invites him to call tomorrow at any time."),
    (8, None, "'Thank you, this is a great honor for me!' Barinov thanks him, calling it a great honor."),
    (9, None, "'Wait, I will taste the dish myself first.' The chef asks them to wait while he tastes the dish first."),
    (10, None, "'Oh, the cook put way too much pepper in the sauce!' Barinov complains that the cook added way too much pepper to the sauce."),
    (11, None, "'And in my opinion, it turned out quite delicious.' Vadim thinks it actually turned out quite tasty."),
    (12, None, "'No, I will immediately redo everything!' He refuses and insists on redoing everything immediately."),
    (13, None, "'I will personally bring you an ideal dish.' Barinov promises to personally bring a perfect dish."),
]
