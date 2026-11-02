# Authoring module for kukhnya-s01e04-scene-19.
ID = 'kukhnya-s01e04-scene-19'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 4
SCENE = 19
TITLE = 'Обед для персонала  (Staff Lunch)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'max': 'Макс', 'senya': 'Сеня'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.04'
SOURCE_FILE = 'sources/kukhnya/s01/e04.ru.dual.srt'
INTRO = "The staff are hungry, and Max is in charge of lunch. Senya asks when it will be ready, and Max promises a special soup that is nothing like the usual slop. Here's the Russian first."
OPENER = 'Now the wait for lunch.'
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'Max promises an unforgettable lunch, and the cooks aren\'t sure whether to be pleased or worried. Notice the phrase for "finger-licking".'
CLOSING = ('max', 'Пока!')
STORY = [
    ('senya', 'Макс, мы сегодня обедать будем?', 'Max, are we going to have lunch today?', [(264, 'Мы сегодня есть')], ''),
    ('max', 'Конечно, всё уже почти готово!', 'Of course, everything is already almost ready!', [(265, 'Все готово')], ''),
    ('senya', 'Мы все очень хотим есть.', 'We all really want to eat.', [(264, 'Вообще будем')], ''),
    ('max', 'Подождите ещё пару минут.', 'Wait a couple more minutes.', [(265, 'Будете, будете')], ''),
    ('senya', 'Что ты нам приготовил сегодня?', 'What did you prepare for us today?', [], ''),
    ('max', 'Я сварил особенный суп-пюре.', 'I cooked a special purée soup.', [(267, 'Суппюре')], ''),
    ('senya', 'Обычный суп был бы лучше.', 'A regular soup would be better.', [], ''),
    ('max', 'Вы все пальчики оближете!', 'You will all lick your fingers!', [(266, 'пальчики оближите')], ''),
    ('senya', 'Надеюсь, это можно есть.', 'I hope this is edible.', [], ''),
    ('max', 'Вы такого никогда не пробовали.', 'You have never tasted such a thing.', [(267, 'никогда не пробовали')], ''),
    ('senya', 'Главное, чтобы было вкусно.', 'The main thing is that it is tasty.', [], ''),
    ('max', 'Это не то обычное месиво.', 'This is not that usual slop.', [(268, 'Не то месиво')], ''),
    ('senya', 'Ладно, неси скорее на стол!', 'Alright, bring it quickly to the table!', [], ''),
    ('max', 'Сейчас я вас всех удивлю!', 'Now I will surprise you all!', [], ''),
]
WALK = [
    (0, None, ["'Max, are we going to have lunch today?' The Russian expression for 'to have lunch' is ", ('senya', "обедать"), ", built from lunch. Senya puts it before ", ('senya', "будем?"), ", meaning we will, which stresses the lunch."]),
    (1, None, ["'Of course, everything is already almost ready!' The Russian term for 'almost' is ", ('max', "почти"), ". ", ('max', "готово!"), " matches the shape of ", ('max', "всё"), ", meaning everything."]),
    (2, None, ["'We all really want to eat.' ", ('senya', "хотим есть."), " translates to 'we want to eat', which is the usual phrase for 'we're hungry'."]),
    (3, None, ["'Wait a couple more minutes.' The Russian expression for 'wait' aimed at several people is ", ('max', "Подождите"), ". ", ('max', "ещё пару минут."), " translates to 'another couple of minutes'."]),
    (4, None, ["'What did you prepare for us today?' ", ('senya', "нам"), ", literally 'to us', does the job of 'for us'. ", ('senya', "приготовил"), " translates to 'prepared' when said of a man."]),
    (5, None, ["'I cooked a special purée soup.' ", ('max', "сварил"), " is built from the action word for boil, with a prefix showing it is finished. ", ('max', "суп-пюре."), " is a borrowed combination."]),
    (6, None, ["'A regular soup would be better.' ", ('senya', "бы"), " is the little word for 'would', so ", ('senya', "был бы лучше."), " translates to 'would be better'."]),
    (7, None, ["'You will all lick your fingers!' A cook's promise: ", ('max', "пальчики оближете!"), ", literally 'you'll lick your little fingers', is the Russian phrase for 'finger-licking good'. ", ('max', "пальчики"), " is built from the normal word for fingers."]),
    (8, None, ["'I hope this is edible.' The phrase for 'I hope', ", ('senya', "Надеюсь,"), ", shares a root with the name for hope. ", ('senya', "можно есть."), " literally means 'it is possible to eat', meaning edible."]),
    (9, None, ["'You have never tasted such a thing.' ", ('max', "никогда не пробовали."), " doubles the negative. After it, the describing word for 'such a thing' takes its 'of' form, ", ('max', "такого"), "."]),
    (10, None, ["'The main thing is that it is tasty.' ", ('senya', "чтобы"), " translates to 'so that', and the action word after it goes into the past, as in ", ('senya', "чтобы было вкусно."), "."]),
    (11, None, ["'This is not that usual slop.' The expression for 'slop', ", ('max', "месиво."), ", is built from the action word to knead. The describing word ", ('max', "обычное"), " matches its shape."]),
    (12, None, ["'Alright, bring it quickly to the table!' The action word for carry while walking gives us its command to one person, ", ('senya', "неси"), ". ", ('senya', "на стол!"), ", literally 'onto the table', uses the little word for a surface."]),
    (13, None, ["'Now I will surprise you all!' ", ('max', "удивлю!"), ", meaning I'll surprise, has the word for a marvel at its root. ", ('max', "вас всех"), " translates to 'all of you'."]),
]
