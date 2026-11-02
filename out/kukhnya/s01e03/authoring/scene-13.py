# Authoring module for kukhnya-s01e03-scene-13.
ID = 'kukhnya-s01e03-scene-13'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 3
SCENE = 13
TITLE = 'Секретное лекарство  (The Secret Medicine)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'senya': 'Сеня'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.03'
SOURCE_FILE = 'sources/kukhnya/s01/e03.ru.dual.srt'
INTRO = 'Barinov is still angry with the judge who took away his licence, and he and the cook Senya have a plan for her birthday dinner. Senya has brought a strong "remedy", and the chef wants to know exactly what it does. Here\'s the Russian first.'
OPENER = "Let's follow the plan."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'Barinov plans to deliver his revenge himself. You have heard the phrase "don\'t be afraid", which is a useful command.'
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('barinov', 'Сеня, ты принёс то особое средство?', 'Senya, did you bring that special remedy?', [], ''),
    ('senya', 'Да, шеф, это сильное средство.', 'Yes, chef, this is a strong remedy.', [], ''),
    ('senya', 'Это вообще новое мощное лекарство.', 'This is brand new powerful medicine.', [(258, 'Это вообще новое')], ''),
    ('barinov', 'Как быстро оно начинает действовать?', 'How quickly does it start to act?', [], ''),
    ('senya', 'Очень быстро, шеф, буквально сразу.', 'Very quickly, chef, literally right away.', [], ''),
    ('senya', 'Одна таблетка решает все ваши проблемы.', 'One pill solves all your problems.', [(259, 'Одна таблетка')], ''),
    ('barinov', 'И какой будет точный эффект?', 'And what will be the exact effect?', [], ''),
    ('senya', 'Обещаю, клиент от унитаза не отойдёт!', 'I promise, the customer will not leave the toilet!', [(259, 'клиент от унитаза не отойдет')], ''),
    ('barinov', 'Отлично, судья запомнит этот юбилей!', 'Excellent, the judge will remember this anniversary!', [], ''),
    ('senya', 'Мы добавим таблетку в её суп?', 'Shall we add the pill into her soup?', [], ''),
    ('barinov', 'Нет, положим порошок прямо на гуся.', 'No, we will put the powder directly on the goose.', [], ''),
    ('senya', 'Главное, чтобы другие гости не отравились.', 'The main thing is that other guests do not get poisoned.', [], ''),
    ('barinov', 'Не бойся, я сделаю всё лично.', 'Do not fear, I will do everything personally.', [], ''),
]
WALK = [
    (0, None, (
        "'Senya, did you bring that special remedy?' The word for brought, ",
        ('barinov', 'принёс'),
        ", is a man's action word for carrying here. The word for any means or remedy is the basis for \"that special means\", ",
        ('barinov', 'то особое средство?')
    )),
    (1, None, (
        "'Yes, chef, this is a strong remedy.' The word for strong, ",
        ('senya', 'сильное'),
        ", is built from the word for strength. It has an \"it\" shape because it matches ",
        ('senya', 'средство.')
    )),
    (2, None, (
        "'This is brand new powerful medicine.' Translates to \"totally new\", ",
        ('senya', 'вообще новое'),
        ". The word for powerful, ",
        ('senya', 'мощное'),
        ", is built from the word for power, and a drug from the pharmacy is ",
        ('senya', 'лекарство.')
    )),
    (3, None, (
        "'How quickly does it start to act?' The word for it, ",
        ('barinov', 'оно'),
        ", has an \"it\" shape to match the medicine. Translates to \"begins to act\", ",
        ('barinov', 'начинает действовать?')
    )),
    (4, None, (
        "'Very quickly, chef, literally right away.' The word for literally, ",
        ('senya', 'буквально'),
        ", has the word for letter inside it, just as the English word literally does. Translates to \"at once\", ",
        ('senya', 'сразу.')
    )),
    (5, None, (
        "'One pill solves all your problems.' The word for one, ",
        ('senya', 'Одна'),
        ", has a \"girl\" shape because ",
        ('senya', 'таблетка'),
        " does. The word for solves is ",
        ('senya', 'решает'),
        ", and translates to \"all your problems\", ",
        ('senya', 'все ваши проблемы.')
    )),
    (6, None, (
        "'And what will be the exact effect?' With a \"boy\" shape to match the effect, ",
        ('barinov', 'какой'),
        " asks \"what kind of\". Translates to \"will be\", ",
        ('barinov', 'будет'),
        ", which is all that is needed for things happening later. The word for exact is ",
        ('barinov', 'точный'),
        "."
    )),
    (7, None, (
        "'I promise, the customer will not leave the toilet!' The word for \"I promise\" is ",
        ('senya', 'Обещаю,'),
        " and after the linking word ",
        ('senya', 'от'),
        ", the toilet becomes ",
        ('senya', 'унитаза'),
        ". Translates to \"won't step away from\", ",
        ('senya', 'не отойдёт!')
    )),
    (8, None, (
        "'Excellent, the judge will remember this anniversary!' The word for will remember, ",
        ('barinov', 'запомнит'),
        ", uses a starting piece for fixing something in memory. The word for a round-number birthday or anniversary is ",
        ('barinov', 'юбилей!')
    )),
    (9, None, (
        "'Shall we add the pill into her soup?' The word for \"we'll add\" is ",
        ('senya', 'добавим'),
        ". The word for her, ",
        ('senya', 'её'),
        ", never changes its ending, and translates to \"into the soup\" (if we remove \"her\"), using the linking word ",
        ('senya', 'в'),
        " before ",
        ('senya', 'суп?')
    )),
    (10, None, (
        "'No, we will put the powder directly on the goose.' Translates to \"we'll lay\", ",
        ('barinov', 'положим'),
        ", for putting something down flat. The word for powder is ",
        ('barinov', 'порошок'),
        ", and onto the goose is ",
        ('barinov', 'на гуся.')
    )),
    (11, None, (
        "'The main thing is that other guests do not get poisoned.' Translates to \"the main thing, so that\", ",
        ('senya', 'Главное, чтобы'),
        ". The word for \"got poisoned\", ",
        ('senya', 'отравились.'),
        ", has an ending for more than one person, and it follows the \"so that\" word in a shape for things that already happened."
    )),
    (12, None, (
        "'Do not fear, I will do everything personally.' Translates to the friendly command \"don't be afraid\", ",
        ('barinov', 'Не бойся,'),
        " and translates to \"I'll do everything\", ",
        ('barinov', 'сделаю всё'),
        ". The word for personally is ",
        ('barinov', 'лично.')
    )),
]
