# Authoring module for kukhnya-s01e06-scene-10.
ID = 'kukhnya-s01e06-scene-10'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 6
SCENE = 10
TITLE = 'Срочная уборка  (An Urgent Cleanup)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'lyova': 'Лёва'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.06'
SOURCE_FILE = 'sources/kukhnya/s01/e06.ru.dual.srt'
INTRO = "Panic strikes Claude Monet as word spreads that a health inspector has just entered the restaurant. Chef Viktor Barinov and his faithful sous-chef Lyova scramble across the kitchen, shouting orders to hide violations before the doors open. Let's listen to their frantic exchange in Russian first."
OPENER = "Let's examine how the kitchen staff organizes a rapid emergency cleanup."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Now you know how Russian restaurant staff urgently cleans up before a health check. Listen for these fast-paced commands next time you watch the episode. Next time you watch the episode, listen for the Russian expressions for 'to throw' and 'fast' — you will catch every word right away. See you next time!"
CLOSING = ('lyova', 'Пока!')
STORY = [
    ('barinov', 'Не спим, Лёва, у нас проверка!', 'Wake up, Lyova, we have an inspection!', [(156, 'Не спим, Лёва, у нас проверка')], ''),
    ('lyova', 'Шеф, инспектор уже заходит в зал!', 'Chef, the inspector is already entering the hall!', [], ''),
    ('barinov', 'Быстро убирайте всё лишнее со столов.', 'Quickly clear everything extra off the tables.', [], ''),
    ('lyova', 'Куда спрятать эти старые продукты?', 'Where to hide these old products?', [], ''),
    ('barinov', 'Неси всё это прямо в холодильник.', 'Carry all this straight into the refrigerator.', [(153, 'порозилку')], ''),
    ('lyova', 'А что делать с грязными фартуками?', 'And what to do with dirty aprons?', [], ''),
    ('barinov', 'Лёва, немедленно бросай их в стирку!', 'Lyova, immediately throw them into the wash!', [(155, 'Лёва, стирку')], ''),
    ('lyova', 'Я уже отправил Сеню за тряпками.', 'I already sent Senya for cloths.', [], ''),
    ('barinov', 'Вытрите пол, он слишком скользкий!', 'Wipe the floor, it is too slippery!', [], ''),
    ('lyova', 'Повара уже моют свои рабочие места.', 'The cooks are already washing their workstations.', [], ''),
    ('barinov', 'Кухня должна быть идеально чистой!', 'The kitchen must be ideally clean!', [], ''),
    ('lyova', 'Мы успеем всё сделать вовремя, шеф!', 'We will manage to do everything in time, chef!', [], ''),
    ('barinov', 'По местам, инспектор уже здесь!', 'To your stations, the inspector is already here!', [], ''),
]
WALK = [
    (0, None, "'Wake up, Lyova, we have an inspection!' Yelling at his sous-chef, Barinov jolts the kitchen into emergency mode."),
    (1, None, "'Quickly clear everything extra off the tables.' Barinov commands the crew to hide any messy evidence from sight."),
    (2, None, "'Lyova, immediately throw them into the wash!' Urgently, Barinov orders his deputy to ditch the dirty rags and aprons fast."),
    (3, None, "'Wipe the floor, it is too slippery!' Barinov barks a warning about the hazardous wet tiles."),
]
