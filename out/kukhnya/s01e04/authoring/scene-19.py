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
    (0, None, '\'Max, are we going to have lunch today?\' "Obedat\'" is "to have lunch", from "obed". Russian puts the verb first, as "have-lunch will we?".'),
    (1, None, '\'Of course, everything is already almost ready!\' "Pochti" is "almost". "Gotovo" ends in -o to agree with "vsyo", everything.'),
    (2, None, '\'We all really want to eat.\' Russians say "we want to eat" for "we\'re hungry". "Khotim" is "we want".'),
    (3, None, '\'Wait a couple more minutes.\' "Podozhdite" is "wait", aimed at someone you address as "vy". "Paru" is "a couple", and "yeshchyo" is "more".'),
    (4, None, '\'What did you prepare for us today?\' "Nam" is "to us", Russian\'s way to say "for us". "Prigotovil" is a man\'s "prepared".'),
    (5, None, '\'I cooked a special purée soup.\' "Svaril" has "s-", done, in front of "varit\'", to boil. "Sup-pyure" is borrowed from French.'),
    (6, None, '\'A regular soup would be better.\' "By" is the little word that makes "would": "byl by luchshe", "would be better".'),
    (7, None, '\'You will all lick your fingers!\' "Pal\'chiki oblizhete" is literally "you\'ll lick the little fingers", and it\'s the exact Russian for "finger-licking". "Pal\'chiki" is "little fingers".'),
    (8, None, '\'I hope this is edible.\' "Mozhno" is "it\'s possible", so "mozhno yest\'" means "can be eaten". Senya is not convinced.'),
    (9, None, '\'You have never tasted such a thing.\' Max claims they have never tasted such a thing: "never not tried", the double negative, and "such" in its "of" form.'),
    (10, None, '\'The main thing is that it is tasty.\' "Chtoby" is "so that", and Russians put the next word in the past, "bylo", to express a hope. "Vkusno" is "tasty".'),
    (11, None, '\'This is not that usual slop.\' "Mesivo" is a rude word for a mush or slop, from "mesit\'", to knead. "Obychnoye" is "usual".'),
    (12, None, '\'Alright, bring it quickly to the table!\' "Nesi" is "carry", a relative of "prinesu". "Na stol" is "onto the table", with no ending for movement.'),
    (13, None, '\'Now I will surprise you all!\' "Udivlyu" is "I will surprise", and the root is "udivitel\'nyy", surprising. "Vas vsekh" is "all of you".'),
]
