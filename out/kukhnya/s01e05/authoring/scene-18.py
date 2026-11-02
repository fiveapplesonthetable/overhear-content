# Authoring module for kukhnya-s01e05-scene-18.
ID = 'kukhnya-s01e05-scene-18'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 5
SCENE = 18
TITLE = 'Рыбный экзамен  (The Fish Exam)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.05'
SOURCE_FILE = 'sources/kukhnya/s01/e05.ru.dual.srt'
INTRO = "Back in the Claude Monet kitchen, Chef Barinov puts Max to a real test: tonight Max runs the fish station on his own. What Max doesn't know is that the chef plans to keep the orders coming. Listen in Russian first, and let a few words go by."
OPENER = "Let's walk through it. Barinov fires off orders, and Max says yes to every one."
TRANSITION = "Now try it at service speed."
OUTRO = "Kitchen Russian is short and fast. Max replies with brief phrases to say 'yes, chef' and 'I will cope', while Barinov demands him to 'prove it'."
CLOSING = ('max', 'Пока!')
STORY = [
    ('barinov', 'Все заказы по рыбе выполняешь ты!', 'You are handling all the fish orders!', [(243, 'все заказы по рыбе')], ""),
    ('max', 'Есть, шеф, я готов к работе!', 'Yes, Chef, I am ready to work!', [(244, 'Есть, шеф')], ""),
    ('barinov', 'Посмотрим, какой из тебя рыбный мастер.', 'Let us see what kind of fish master you are.', [], ""),
    ('max', 'Я приготовлю все блюда очень быстро.', 'I will prepare all dishes very quickly.', [], ""),
    ('barinov', 'Максим, прими заказ: две трески по-флорентийски!', 'Maxim, take the order: two cod Florentines!', [(256, 'две трески')], ""),
    ('max', 'Да, шеф, уже начинаю готовить.', 'Yes, Chef, I am already starting to cook.', [(257, 'Да, шеф')], ""),
    ('barinov', 'И ещё две порции трески с миндалём!', 'And two more portions of cod with almonds!', [], ""),
    ('max', 'Я же уже взял два блюда!', 'But I already took two dishes!', [(260, 'Я же уже взял два блюда')], ""),
    ('barinov', 'Не спорь, Федя как-то справлялся!', 'Do not argue, Fedya managed somehow!', [(261, 'Федя как-то справлялся')], ""),
    ('max', 'Мне не хватает свежей рыбы здесь.', 'I do not have enough fresh fish here.', [], ""),
    ('barinov', 'Ищи на складе и быстрее крутись!', 'Search in the storage and hustle faster!', [], ""),
    ('max', 'Я справлюсь со всеми заказами сам.', 'I will handle all orders myself.', [], ""),
    ('barinov', 'Вот и докажи это делом, огузок!', 'Prove it with action then, rump!', [], ""),
]
WALK = [
    (0, None, [
        "'You are handling all the fish orders!' comes at the very end, which ",
        ('barinov', 'ты!'),
        ' puts the weight on it: you and nobody else. ',
        ('barinov', 'заказы'), ('barinov', 'по'), ('barinov', 'рыбе'),
        " literally translates as 'orders on fish'."
    ]),
    (1, None, [
        "'Yes, Chef, I am ready to work!' is the soldier's reply to an ",
        ('max', 'Есть,'),
        " order, close to 'aye, sir'. ",
        ('max', 'готов'), ('max', 'к'), ('max', 'работе!'),
        ", meaning 'ready for work', has ",
        ('max', 'к'),
        " ('towards') and a changed ending on the word for work."
    ]),
    (2, None, [
        "'Let us see what kind of fish master you are.' The phrase ",
        ('barinov', 'какой'), ('barinov', 'из'), ('barinov', 'тебя'),
        " literally says 'what kind out of you', a set way to doubt someone's skill. The term ",
        ('barinov', 'рыбный'),
        " relates to fish and works like the adjective in 'fish dish'."
    ]),
    (3, None, [
        "'I will prepare all dishes very quickly.' The verb ",
        ('max', 'приготовлю'),
        ", 'I will prepare', promises the job will be done and finished. The phrase ",
        ('max', 'все'), ('max', 'блюда'),
        " refers to 'all dishes', with ",
        ('max', 'все'),
        " modifying the plural noun."
    ]),
    (4, None, [
        "'Maxim, take the order: two cod Florentines!' The word for 'two' is ",
        ('barinov', 'две'),
        ", used here for a feminine noun, followed by ",
        ('barinov', 'трески'),
        " for 'cod'. The phrase ",
        ('barinov', 'по-флорентийски!'),
        " indicates 'Florentine style'."
    ]),
    (5, None, [
        "'Yes, Chef, I am already starting to cook.' stands for ",
        ('max', 'уже'),
        " 'already'. ",
        ('max', 'начинаю'),
        ", 'I am starting', is followed straight away by ",
        ('max', 'готовить.'),
        " meaning 'to cook'."
    ]),
    (6, None, [
        "'And two more portions of cod with almonds!' means 'two more'. ",
        ('barinov', 'ещё'), ('barinov', 'две'),
        ' After ',
        ('barinov', 'с'),
        " ('with'), the word for almonds changes form: ",
        ('barinov', 'с'), ('barinov', 'миндалём!')
    ]),
    (7, None, [
        "'But I already took two dishes!' adds a note of protest, like ",
        ('max', 'же'),
        " 'after all'. Following ",
        ('max', 'два'),
        " ('two'), the noun changes form, creating ",
        ('max', 'два'), ('max', 'блюда!')
    ]),
    (8, None, [
        "'Do not argue, Fedya managed somehow!' is an order meaning 'do not ",
        ('barinov', 'Не'), ('barinov', 'спорь,'),
        " argue'. ",
        ('barinov', 'справлялся!'),
        ", 'was coping', describes how Fedya used to get through it, shift after shift."
    ]),
    (9, None, [
        "'I do not have enough fresh fish here.' expresses 'to me it is not ",
        ('max', 'Мне'), ('max', 'не'), ('max', 'хватает'),
        " enough'. The missing items are expressed as ",
        ('max', 'свежей'), ('max', 'рыбы'),
        "."
    ]),
    (10, None, [
        "'Search in the storage and hustle faster!' , 'in the storeroom', has an ",
        ('barinov', 'на'), ('barinov', 'складе'),
        ' ending that shows location. ',
        ('barinov', 'крутись!'),
        " translates to 'hustle', literally meaning 'spin yourself round'."
    ]),
    (11, None, [
        "'I will handle all orders myself.' is 'I will cope', a one-time ",
        ('max', 'справлюсь'),
        " promise set against Fedya's past actions. After ",
        ('max', 'со'),
        " ('with'), the plural ending changes: ",
        ('max', 'со'), ('max', 'всеми'), ('max', 'заказами'),
        "."
    ]),
    (12, None, [
        "'Prove it with action then, rump!' is the command ",
        ('barinov', 'докажи'),
        " 'prove'. ",
        ('barinov', 'делом,'),
        " literally translates to 'with a deed', and ",
        ('barinov', 'огузок!'),
        " ('rump') is the chef's nickname for Max."
    ]),
]
