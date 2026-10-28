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
OUTRO = 'Max promises an unforgettable lunch, and the cooks aren\'t sure whether to be pleased or worried. Notice "pal\'chiki oblizhete", the Russian for "finger-licking".'
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
    (0, None, '\'Max, are we going to have lunch today?\' "Obedat\'" is "to have lunch", from "obed". Senya puts it before "budem", we will, which stresses lunch.'),
    (1, None, '\'Of course, everything is already almost ready!\' "Pochti" is "almost". "Gotovo" ends in -o to agree with "vsyo".'),
    (2, None, '\'We all really want to eat.\' "Khotim yest\'", we want to eat, is the usual way to say "we\'re hungry".'),
    (3, None, '\'Wait a couple more minutes.\' "Podozhdite" is "wait" for several people. "Yeshchyo paru minut" is "another couple of minutes".'),
    (4, None, '\'What did you prepare for us today?\' "Nam", to us, does the job of "for us". "Prigotovil" is the man\'s "prepared".'),
    (5, None, '\'I cooked a special purée soup.\' "Svaril" is "varit\'", to boil, with "s-" for finished. "Sup-pyure" is a borrowed compound.'),
    (6, None, '\'A regular soup would be better.\' "By" is the little word for "would": "byl by luchshe", would be better.'),
    (7, None, '\'You will all lick your fingers!\' "Pal\'chiki oblizhete" is "you\'ll lick your little fingers", the Russian for finger-licking good.'),
    (8, None, '\'I hope this is edible.\' "Nadeyus\'", I hope, shares a root with "nadezhda", hope. "Mozhno yest\'" is "it\'s possible to eat", meaning edible.'),
    (9, None, '\'You have never tasted such a thing.\' "Nikogda ne probovali" doubles the negative. After it, "takoye" becomes the "of" form "takogo".'),
    (10, None, '\'The main thing is that it is tasty.\' "Chtoby" is "so that", and the verb after it goes into the past: "chtoby bylo vkusno".'),
    (11, None, '\'This is not that usual slop.\' "Mesivo", slop, is from "mesit\'", to knead. "Obychnoye", usual, is neuter to match.'),
    (12, None, '\'Alright, bring it quickly to the table!\' "Nesi" is "carry", from "nesti". "Na stol" is "onto the table".'),
    (13, None, '\'Now I will surprise you all!\' "Udivlyu", I\'ll surprise, has "divo", a marvel, at its root. "Vas vsekh" is "all of you".'),
]
