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
INTRO = "The word has reached the kitchen: the sanitary inspector is in the building. Barinov and his sous-chef Lyova have minutes to hide everything. It's in Russian first, and it's fast."
OPENER = "Let's replay it slowly. Everything is a command, so it's a good lesson in orders."
TRANSITION = 'Here is the whole panic again.'
OUTRO = "You've just met a heap of useful commands: carry, throw, wipe, hide. They all work in your own kitchen too. See you next time."
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
    (0, None, "'Wake up, Lyova, we have an inspection!' 'We are not sleeping' is the Russian way to say 'get moving'. 'At us an inspection' is how you say 'we have'."),
    (1, None, "'Chef, the inspector is already entering the hall!' 'enters' has a prefix that means 'in' or 'dropping in'. 'Into the hall' takes the 'movement' shape."),
    (2, None, "'Quickly clear everything extra off the tables.' 'Clear away' is a group command. 'Extra' is a word that also means 'unnecessary', and 'off the tables' uses a short word meaning 'from'."),
    (3, None, "'Where to hide these old products?' There is no 'should' in the Russian, only 'where hide'. 'Where to' is the movement word."),
    (4, None, "'Carry all this straight into the refrigerator.' 'Carry' is the command for taking something on foot. 'Straight' is a short word that means 'directly'."),
    (5, None, "'And what to do with dirty aprons?' 'With dirty aprons' puts 'with' in front and an 'imi' ending on the plural. 'What to do' has no 'should' either."),
    (6, None, "'Lyova, immediately throw them into the wash!' Russian has one word for washing clothes and another for washing dishes. This one is for the laundry."),
    (7, None, "'I already sent Senya for cloths.' 'For' here means 'to fetch', and the cloths end in 'ami'. The name Senya has a changed ending because he is the one being sent."),
    (8, None, "'Wipe the floor, it is too slippery!' 'Wipe' is another group command. 'Too' is a single word, and 'slippery' comes from 'slide'."),
    (9, None, "'The cooks are already washing their workstations.' 'Wash' is for hands, floors and plates. 'Their own' points back at the cooks."),
    (10, None, "'The kitchen must be ideally clean!' 'Must be' is a feminine form to agree with 'kitchen'. 'Clean' ends in 'oy', the shape it takes after 'be'."),
    (11, None, "'We will manage to do everything in time, chef!' 'We will manage' is a nice word, and it means 'we'll have enough time'. 'In time' is a single word."),
    (12, None, "'To your stations, the inspector is already here!' 'To places' is a military-style call, and it has no verb. 'Here' is the word for where you are."),
]
