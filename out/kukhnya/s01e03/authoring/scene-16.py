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
INTRO = 'The chef brings a complimentary dish to the birthday table himself, and the guest, Vadim, is charmed, even offering to help him in the city. Then Barinov tastes the sauce and cannot bear what he finds. Here is the Russian first.'
OPENER = "Let's go through the table talk."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'The chef whisks the plate away, because even a free dish has to be perfect. Take away the start piece meaning "over" and "again", which you have now met in two different action words.'
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
    (0, None, [
        '\'Good evening, dear guests of our restaurant!\' The phrase for "good evening", ',
        ('barinov', 'Добрый вечер,'),
        ' acts like the word for evening. The word for "dear", ',
        ('barinov', 'дорогие'),
        ' also translates to "expensive", and ',
        ('barinov', 'нашего ресторана!'),
        ' literally means "of our restaurant".'
    ]),
    (1, None, [
        '\'Good evening, head chef!\' Vadim gives back the same greeting. The word for "head chef", ',
        ('vadim', 'шеф-повар!'),
        ' is built from the word for "boss" and the word for "cook", making it a formal title.'
    ]),
    (2, None, [
        '\'I brought you a special surprise.\' The word for "brought", ',
        ('barinov', 'принёс'),
        ' is a shape for a man. ',
        ('barinov', 'вам'),
        ' translates to "to you", and ',
        ('barinov', 'сюрприз.'),
        ' comes directly from French.'
    ]),
    (3, None, [
        "'This is a compliment in honor of the birthday.' In a restaurant, ",
        ('barinov', 'комплимент'),
        ' translates to a free dish from the kitchen. The phrase for "birthday", ',
        ('barinov', 'дня рождения.'),
        ' literally means "day of birth", taking a special shape after ',
        ('barinov', 'в честь'),
        ' which translates to "in honor of".'
    ]),
    (4, None, [
        "'Thank you very much, everything looks very delicious!' The phrase ",
        ('vadim', 'Спасибо большое,'),
        ' literally means "thanks big". After the action word for "looks", ',
        ('vadim', 'выглядит'),
        ' the word for "delicious", ',
        ('vadim', 'вкусно!'),
        ' takes a special shape at the end.'
    ]),
    (5, None, [
        "'I see that you are an excellent cook.' The phrase ",
        ('vadim', 'Я вижу, что'),
        ' translates to "I see that". The word for "excellent", ',
        ('vadim', 'отличный'),
        ' is built from the action word for standing out.'
    ]),
    (6, None, [
        "'I can help you in the city.' The phrase ",
        ('vadim', 'вам помочь'),
        ' translates to "help to you", pointing the action at someone. The phrase ',
        ('vadim', 'в городе.'),
        ' literally means "in the city", changing the ending of the place.'
    ]),
    (7, None, [
        '\'Call me tomorrow at any time.\' The action word for "call", ',
        ('vadim', 'Позвоните'),
        ' is built from the sound of a ring. ',
        ('vadim', 'в любое время.'),
        ' translates to "at any time", and ',
        ('vadim', 'завтра'),
        ' is the word for "tomorrow".'
    ]),
    (8, None, [
        '\'Thank you, this is a great honor for me!\' The word for "honor", ',
        ('barinov', 'честь!'),
        ' is the same one used earlier. ',
        ('barinov', 'для меня'),
        ' translates to "for me", and ',
        ('barinov', 'большая'),
        ' takes a matching shape.'
    ]),
    (9, None, [
        '\'Wait, I will taste the dish myself first.\' The action word for "wait", ',
        ('barinov', 'Подождите,'),
        ' has a polite ending. The word for "first", ',
        ('barinov', 'сначала'),
        ' is built from the idea of a beginning, and ',
        ('barinov', 'сам'),
        ' translates to "myself".'
    ]),
    (10, None, [
        "'Oh, the cook put way too much pepper in the sauce!' The action word ",
        ('barinov', 'переперчил'),
        ' is built from a start piece meaning "over" and the word for pepper. ',
        ('barinov', 'слишком сильно'),
        ' literally means "too strongly".'
    ]),
    (11, None, [
        "'And in my opinion, it turned out quite delicious.' The phrase ",
        ('vadim', 'по-моему,'),
        ' literally means "by mine", which translates to "in my opinion". The word for "quite", ',
        ('vadim', 'довольно'),
        ' is built from the feeling of being pleased.'
    ]),
    (12, None, [
        "'No, I will immediately redo everything!' The action word ",
        ('barinov', 'переделаю!'),
        ' uses the start piece for "over again" to mean redoing something. The word for "immediately", ',
        ('barinov', 'немедленно'),
        ' is built from "not" and "slowly".'
    ]),
    (13, None, [
        '\'I will personally bring you an ideal dish.\' The word for "bring", ',
        ('barinov', 'принесу'),
        ' is a different shape of the action we saw earlier. ',
        ('barinov', 'лично'),
        ' translates to "personally", and ',
        ('barinov', 'идеальное блюдо.'),
        ' literally means "ideal dish".'
    ]),
]
