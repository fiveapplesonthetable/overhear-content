# Authoring module for kukhnya-s01e04-scene-12.
ID = 'kukhnya-s01e04-scene-12'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 4
SCENE = 12
TITLE = 'Чистосердечное признание  (A Full Confession)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'senya': 'Сеня'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.04'
SOURCE_FILE = 'sources/kukhnya/s01/e04.ru.dual.srt'
INTRO = 'Senya is next in the chair, and he breaks down before the machine is even switched on. Instead of answering about the rival restaurant, he starts confessing to every bit of food he has ever taken from the kitchen. Here is the Russian first.'
OPENER = 'Now the confession.'
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Barinov stares at his sobbing cook and decides what to do next. You've heard the phrase for I swear, which is a good one to know."
CLOSING = ('senya', 'Пока!')
STORY = [
    ('senya', 'Шеф, пожалуйста, не включайте прибор!', 'Chef, please, do not turn on the device!', [(146, 'Шеф, пожалуйста')], ''),
    ('barinov', 'Ты чего так сильно дрожишь?', 'Why are you shaking so hard?', [], ''),
    ('senya', 'Я сам вам всё честно расскажу!', 'I will tell you everything honestly myself!', [(146, 'Я все расскажу')], ''),
    ('senya', 'Эту рыбу после банкета взял я!', 'I took that fish after the banquet!', [(147, 'Эту рыбу'), (147, 'после банкета, я взял')], ''),
    ('senya', 'И ту оленину тоже унёс я!', 'And I took that venison away too!', [(148, 'И ту оленину'), (148, 'тоже я унес')], ''),
    ('barinov', 'А полкило дорогой икры?', 'And half a kilo of expensive caviar?', [(149, 'А полкило икры')], ''),
    ('senya', 'Нет, шеф, икру я не брал!', 'No, Chef, I did not take the caviar!', [(150, 'Нет')], ''),
    ('senya', 'Простите меня, пожалуйста, шеф!', 'Forgive me, please, Chef!', [(151, 'Простите меня, шеф')], ''),
    ('barinov', 'Мне плевать на твою оленину!', 'I do not care about your venison!', [], ''),
    ('barinov', 'Ты ходил в соседний ресторан?', 'Did you go to the neighboring restaurant?', [(152, 'Это ты ходил в соседний ресторан')], ''),
    ('senya', 'Нет, шеф, клянусь вам!', 'No, Chef, I swear to you!', [(153, 'Нет')], ''),
    ('barinov', 'Говори правду, да или нет?', 'Tell the truth, yes or no?', [(150, 'нет')], ''),
    ('senya', 'Нет! Я предан только вам!', 'No! I am loyal only to you!', [(154, 'Нет')], ''),
]
WALK = [
    (0, None, ["'Chef, please, do not turn on the device!' The term for don't switch on is ", ('senya', "не включайте"), " ending with a polite sound. The Russian term for device or gauge is ", ('senya', "прибор!")]),
    (1, None, ["'Why are you shaking so hard?' A spoken phrase for why are you is ", ('barinov', "Ты чего"), " The phrase for you tremble is ", ('barinov', "дрожишь?"), " and the translation for strongly is ", ('barinov', "сильно")]),
    (2, None, ["'I will tell you everything honestly myself!' The Russian expression for myself, here meaning of my own accord, is ", ('senya', "сам"), " It is paired with ", ('senya', "расскажу!"), " which translates to I will tell, and ", ('senya', "честно"), " for honestly."]),
    (3, None, ["'I took that fish after the banquet!' The ending phrase ", ('senya', "взял я!"), " literally translates to took I, with the I placed last for emphasis. The phrase ", ('senya', "после банкета"), " means after the banquet."]),
    (4, None, ["'And I took that venison away too!' The expression for venison is ", ('senya', "оленину"), " which is built from the word for deer. The action word ", ('senya', "унёс"), " translates to carried off, with a starting sound that means away."]),
    (5, None, ["'And half a kilo of expensive caviar?' The Russian term for half a kilo is ", ('barinov', "полкило"), " built from half plus kilo. After it, the describing words for expensive caviar change their endings to ", ('barinov', "дорогой икры?")]),
    (6, None, ["'No, Chef, I did not take the caviar!' Senya puts the term for caviar, ", ('senya', "икру"), " first for stress: the caviar, I did not take. The phrase for did not take is ", ('senya', "не брал!")]),
    (7, None, ["'Forgive me, please, Chef!' The phrase ", ('senya', "Простите меня,"), " translates to forgive me, ending with a polite sound."]),
    (8, None, ["'I do not care about your venison!' The phrase ", ('barinov', "Мне плевать"), " literally translates to to me to spit, which is a blunt way to say I couldn't care less. He then says he spits on your venison, ", ('barinov', "на твою оленину!")]),
    (9, None, ["'Did you go to the neighboring restaurant?' The chef asks the same question he asked Fedya, using the term for went and came back, ", ('barinov', "ходил")]),
    (10, None, ["'No, Chef, I swear to you!' The word for I swear is ", ('senya', "клянусь"), " with a reflexive sound at the end. The Russian term for to you is the polite ", ('senya', "вам")]),
    (11, None, ["'Tell the truth, yes or no?' The phrase ", ('barinov', "Говори правду,"), " translates to speak the truth, with the phrase for truth changing its ending because it is the target of the action."]),
    (12, None, ["'No! I am loyal only to you!' The describing word ", ('senya', "предан"), " translates to devoted, in a short form for a man. The phrase ", ('senya', "только вам!"), " means only to you."]),
]
