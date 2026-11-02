# Authoring module for kukhnya-s01e04-scene-09.
ID = 'kukhnya-s01e04-scene-09'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 4
SCENE = 9
TITLE = 'Приступай к работе  (Get to Work)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.04'
SOURCE_FILE = 'sources/kukhnya/s01/e04.ru.dual.srt'
INTRO = 'At the stove, Chef Barinov checks that Max has understood the order for the soup. He warns him against mistakes, and then tells him to stop talking and get started. Here is the Russian first.'
OPENER = "Now let's listen to the chef's checking."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Max is on his own at the soup station, with the chef watching. Notice the expression for 'enough', one of the chef's favourite words."
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('barinov', 'Лавров, ты всё понял по заказу?', 'Lavrov, did you understand everything about the order?', [(98, 'ты все понял')], ''),
    ('max', 'Да, шеф, я всё отлично понял!', 'Yes, Chef, I understood everything perfectly!', [(99, 'Да')], ''),
    ('barinov', 'Суп должен быть идеальным и горячим.', 'The soup must be ideal and hot.', [], ''),
    ('max', 'Я использую лучшие овощи и сливки.', 'I use the best vegetables and cream.', [], ''),
    ('barinov', 'Наши гости не терпят глупых ошибок.', 'Our guests do not tolerate foolish mistakes.', [], ''),
    ('max', 'Я гарантирую безупречный вкус этого блюда.', 'I guarantee the flawless taste of this dish.', [], ''),
    ('barinov', 'Хватит болтать языком, Лавров.', 'Stop chattering away, Lavrov.', [], ''),
    ('barinov', 'Ну приступай скорее к работе!', 'Well get to work quickly!', [(99, 'Ну приступай')], ''),
    ('max', 'Уже начинаю готовить прямо сейчас, шеф!', 'Already starting to cook right now, Chef!', [], ''),
    ('barinov', 'И внимательно следи за этой плитой!', 'And watch this stove attentively!', [], ''),
    ('max', 'Я не отойду от неё никуда!', 'I will not step away from it anywhere!', [], ''),
    ('barinov', 'Посмотрим, какой ты повар на деле.', 'We will see what kind of cook you are in practice.', [], ''),
]
WALK = [
    (0, None, ["'Lavrov, did you understand everything about the order?' Barinov calls Max by his surname, ", ('barinov', 'Лавров,'), ", as a stern boss does. The phrase ", ('barinov', 'по заказу?'), " literally translates to 'on the order', meaning about it."]),
    (1, None, ["'Yes, Chef, I understood everything perfectly!' The expression for 'understood everything perfectly', ", ('max', 'отлично понял!'), ", ends with an L sound, showing that a man is speaking. The translation for 'perfectly', ", ('max', 'отлично'), ", is built from the describing word for 'excellent'."]),
    (2, None, ["'The soup must be ideal and hot.' The phrase for 'must be' is ", ('barinov', 'должен быть'), ", and after it both describing words have special endings: ", ('barinov', 'идеальным'), " and ", ('barinov', 'горячим.'), "."]),
    (3, None, ["'I use the best vegetables and cream.' The expression for 'I use', ", ('max', 'использую'), ", is built from the term for 'benefit'. The describing word for 'the best', ", ('max', 'лучшие'), ", is plural to match the vegetables and cream."]),
    (4, None, ["'Our guests do not tolerate foolish mistakes.' The expression for 'they put up with', ", ('barinov', 'терпят'), ", comes from the action word for 'to endure'. After the negative little word ", ('barinov', 'не'), ", the phrase for mistakes takes the 'of' form ", ('barinov', 'ошибок.'), ", and foolish becomes ", ('barinov', 'глупых'), "."]),
    (5, None, ["'I guarantee the flawless taste of this dish.' The word for 'flawless', ", ('max', 'безупречный'), ", is built from the translation for 'without' plus 'reproach'. The phrase ", ('max', 'этого блюда.'), " translates to 'of this dish'."]),
    (6, None, ["'Stop chattering away, Lavrov.' The translation for 'enough', ", ('barinov', 'Хватит'), ", is an action word meaning 'it suffices'. The phrase ", ('barinov', 'болтать языком,'), " literally translates to 'to wag with the tongue', and the expression for tongue also means language."]),
    (7, None, ["'Well get to work quickly!' The term for 'set about' is ", ('barinov', 'приступай'), ", and ", ('barinov', 'к работе!'), " puts an extra 'e' sound on the Russian term for work. The word ", ('barinov', 'скорее'), " literally translates to 'quicker'."]),
    (8, None, ["'Already starting to cook right now, Chef!' The action word ", ('max', 'начинаю'), " simply translates to 'I start', which also covers 'I am starting'. The phrase ", ('max', 'прямо сейчас,'), " means 'right now'."]),
    (9, None, ["'And watch this stove attentively!' The phrase ", ('barinov', 'следи за'), " literally translates to 'follow behind', meaning keep an eye on. After the little word meaning \'behind\', the stove changes to ", ('barinov', 'плитой!'), ", and the expression for 'this' changes to ", ('barinov', 'этой'), "."]),
    (10, None, ["'I will not step away from it anywhere!' The phrase ", ('max', 'от неё'), " translates to 'from her', since the stove has feminine gender, with an extra N sound added. The word ", ('max', 'отойду'), " is 'I will step away', and ", ('max', 'никуда!'), " doubles the negative meaning 'nowhere'."]),
    (11, None, ["'We will see what kind of cook you are in practice.' One action word does the work of 'we will see': ", ('barinov', 'Посмотрим,'), ", with no separate word for 'we' needed. The phrase ", ('barinov', 'на деле.'), " literally translates to 'in the deed', meaning in practice, as opposed to in words."]),
]
