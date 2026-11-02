# Authoring module for kukhnya-s01e02-scene-11.
ID = 'kukhnya-s01e02-scene-11'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 2
SCENE = 11
TITLE = 'Визит к столу  (A Visit to the Table)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'ainura': 'Айнура', 'barinov': 'Шеф', 'elena': 'Елена'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.02'
SOURCE_FILE = 'sources/kukhnya/s01/e02.ru.dual.srt'
INTRO = 'Ainura, who cleans the kitchen, calls the chef out to the dining room, where a guest is waiting: Elena Sokolova, head chef of a rival restaurant called Arcobaleno. She has tasted the fricassee, and she has opinions. This is the Russian first.'
OPENER = "Now let's see what she really says."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'Elena leaves with a compliment that sounds like an insult, or the other way round. Keep the formal goodbye she ends her visit with, which you can use anywhere.'
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('ainura', 'Шеф! Шеф! Вас зовут в зал!', 'Chef! Chef! You are being called to the dining hall!', [(149, 'Шеф! Шеф!')], ''),
    ('barinov', 'Что ещё? Кто меня там ждёт?', 'What else? Who is waiting for me there?', [(150, 'Что еще')], ''),
    ('ainura', 'Та симпатичная дама из соседнего ресторана.', 'That pretty lady from the neighboring restaurant.', [(150, 'симпатичная'), (150, 'соседнего ресторана')], ''),
    ('barinov', 'Чем я могу быть полезен?', 'How can I be of service?', [(155, 'Чем могу быть полезен')], ''),
    ('elena', 'Я только что попробовала ваше фрикасе.', 'I have just tasted your fricassee.', [(156, 'Попробовала ваше фрикассе')], ''),
    ('barinov', 'Ну, и как вам наше блюдо?', 'Well, and how did you like our dish?', [(157, 'Ну, и как вам')], ''),
    ('elena', 'Вы знаете, оно мне очень понравилось.', 'You know, I liked it very much.', [(159, 'оно мне понравилось')], ''),
    ('barinov', 'Да? Это мой старый фирменный рецепт.', 'Really? This is my old signature recipe.', [(160, 'Хороший рецепт')], ''),
    ('barinov', 'Куропатка оставалась, а выбрасывать было жалко.', 'Partridge was left over, and it was a shame to throw it out.', [(161, 'Куропатка оставалась, а выбрасывать жалко')], ''),
    ('elena', 'Понятно. Приятно уйти от вас живой.', 'Understood. It is pleasant to leave your place alive.', [(162, 'поняла'), (164, 'уйти от вас в добром здравии')], ''),
    ('barinov', 'Как? Вы уже уходите из ресторана?', 'What? Are you already leaving the restaurant?', [(165, 'Как? Уже уходите')], ''),
    ('elena', 'Ваше блюдо от шефа готовилось слишком долго.', "Your chef's special took far too long to prepare.", [(167, 'Ваше блюдо от шефа очень долго готовилось')], ''),
    ('elena', 'До свидания, шеф-повар.', 'Goodbye, head chef.', [(168, 'До свидания')], ''),
]
WALK = [
    (0, None, [
        '\'Chef! Chef! You are being called to the dining hall!\' The phrase ',
        ('ainura', 'Вас зовут в зал!'),
        ', literally translates to "you they call to the hall". The action word ',
        ('ainura', 'зовут'),
        ', "they call", names nobody, which is the usual way to say you\'re wanted. Ainura uses ',
        ('ainura', 'Вас'),
        ', the polite word for "you", for her boss.'
    ]),
    (1, None, [
        '\'What else? Who is waiting for me there?\' ',
        ('barinov', 'Что ещё?'),
        ' translates to "what else?", an impatient "what now?". The word for "waits" is ',
        ('barinov', 'ждёт?'),
        ', and ',
        ('barinov', 'там'),
        ' means "there".'
    ]),
    (2, None, [
        '\'That pretty lady from the neighboring restaurant.\' The describing word ',
        ('ainura', 'симпатичная'),
        ' looks like "sympathetic" but really translates to nice-looking or likeable. A false friend worth knowing.'
    ]),
    (3, None, [
        '\'How can I be of service?\' Russian literally says ',
        ('barinov', 'Чем я могу быть полезен?'),
        ', "with what can I be useful". The word ',
        ('barinov', 'полезен?'),
        ' is a shorter version of the describing word for useful, and a woman would say it differently.'
    ]),
    (4, None, [
        '\'I have just tasted your fricassee.\' The phrase ',
        ('elena', 'только что'),
        ' translates to "only what", and together they mean "just now". The ending on the action word ',
        ('elena', 'попробовала'),
        ' shows Elena is a woman.'
    ]),
    (5, None, [
        '\'Well, and how did you like our dish?\' The little word ',
        ('barinov', 'Ну,'),
        ' is the "well..." of Russian. ',
        ('barinov', 'как вам'),
        ' literally translates to "how to you", which is how Russians ask what you thought of something.'
    ]),
    (6, None, [
        '\'You know, I liked it very much.\' The phrase ',
        ('elena', 'Вы знаете,'),
        ', "you know", is a filler, just as in English. ',
        ('elena', 'оно мне очень понравилось.'),
        ' literally translates to "it to me pleased", with an ending on the action word to match the fricassee.'
    ]),
    (7, None, [
        '\'Really? This is my old signature recipe.\' The describing word ',
        ('barinov', 'фирменный'),
        ', signature, is built from the word for a company, so it translates to "of the house". ',
        ('barinov', 'старый фирменный рецепт.'),
        ' translates to "old recipe".'
    ]),
    (8, None, [
        '\'Partridge was left over, and it was a shame to throw it out.\' The word for to throw out, ',
        ('barinov', 'выбрасывать'),
        ', is built from a little word meaning out. ',
        ('barinov', 'жалко.'),
        ' translates to "it\'s a pity", all in one word.'
    ]),
    (9, None, [
        '\'Understood. It is pleasant to leave your place alive.\' The word for alive, ',
        ('elena', 'живой.'),
        ', is built from the same root as the word for quick from the knife scene. It has a specific ending because Elena is a woman. A joke with a sting.'
    ]),
    (10, None, [
        '\'What? Are you already leaving the restaurant?\' The word ',
        ('barinov', 'как'),
        ' translates to "how", but here it shows surprise, like "what?". In the phrase ',
        ('barinov', 'из ресторана?'),
        ', meaning "out of the restaurant", the little word for "out of" changes the ending of the word for restaurant.'
    ]),
    (11, None, [
        '\'Your chef\'s special took far too long to prepare.\' The action word ',
        ('elena', 'готовилось'),
        ', meaning "was being cooked", has an ending that makes it sound as if the dish cooked itself. ',
        ('elena', 'слишком долго.'),
        ' translates to "too long".'
    ]),
    (12, None, [
        '\'Goodbye, head chef.\' The formal goodbye ',
        ('elena', 'До свидания,'),
        ' literally translates to "until meeting", and it\'s the standard formal goodbye. Use it with anyone you don\'t know well.'
    ]),
]
