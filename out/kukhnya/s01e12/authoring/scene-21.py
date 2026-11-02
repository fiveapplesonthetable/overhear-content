# Authoring module for kukhnya-s01e12-scene-21.
ID = 'kukhnya-s01e12-scene-21'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 12
SCENE = 21
TITLE = 'Пожар напротив  (Fire Across the Street)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'fedya': 'Федя', 'senya': 'Сеня'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.12'
SOURCE_FILE = 'sources/kukhnya/s01/e12.ru.dual.srt'
INTRO = 'The cooks are outside on a smoke break when something catches their eye: the new restaurant next door is on fire. This is what Senya and Fedya say, in Russian first.'
OPENER = 'Slowly now, from the cigarette to the door.'
TRANSITION = 'Once again, the whole scene, without stopping.'
OUTRO = "The two of them rush off to tell the chef. Remember the difference between a simple flame and a fire you call for help about. Bye for now."
CLOSING = ('fedya', 'Пока!')
STORY = [
    ('senya', 'Эта сигарета уже горчит на вкус.', 'This cigarette already tastes bitter.', [(278, 'Горчит уже.')], ''),
    ('senya', 'Да выбрось её скорее в урну.', 'Just throw it out quickly into the trash bin.', [(278, 'Да выбрось ее.')], ''),
    ('fedya', 'Ладно, я хочу пойти в туалет.', 'All right, I want to go to the bathroom.', [(279, 'Ладно, я в туалет хочу.')], ''),
    ('fedya', 'Подожди, там огонь, друзья!', 'Wait, there is fire over there, friends!', [(280, 'Там это огонь, друзья.')], 'adapted: dropped the filler word'),
    ('senya', 'Соседний ресторан горит прямо сейчас!', 'The neighboring restaurant is burning right now!', [], ''),
    ('fedya', 'Ты уверен, что это настоящий пожар?', 'Are you sure that this is a real fire?', [], ''),
    ('senya', 'Конечно, посмотри на этот чёрный дым.', 'Of course, look at this black smoke.', [], ''),
    ('fedya', 'Люди выбегают из здания на улицу.', 'People are running out of the building onto the street.', [], ''),
    ('senya', 'Нам надо срочно сказать об этом шефу.', 'We urgently need to tell the boss about this.', [], ''),
    ('fedya', 'Да, он должен знать про этот огонь.', 'Yes, he must know about this fire.', [], ''),
    ('senya', 'Бросай сигарету и пошли быстрее внутрь.', "Drop the cigarette and let's go inside faster.", [], ''),
    ('fedya', 'Я бегу за тобой, открывай дверь.', 'I am running after you, open the door.', [], ''),
]
WALK = [
    (0, None, ["'This cigarette already tastes bitter.' Let us analyze the phrase: ", ('senya', 'горчит'), ' means tastes bitter. Notice how cigarette is ', ('senya', 'сигарета'), ', and ', ('senya', 'Эта'), ' is this. Finally, ', ('senya', 'на'), ('senya', 'вкус'), ' means to the taste.']),
    (1, None, ["'Just throw it out quickly into the trash bin.' The it here is her, ", ('senya', 'её'), ', referring to the cigarette. Into the bin is ', ('senya', 'в'), ('senya', 'урну'), ', with an u at the end since the cigarette is going into it.']),
    (2, None, ["'All right, I want to go to the bathroom.' We will inspect this line: ", ('fedya', 'хочу'), ' is I want, and the thing he wants follows straight after as ', ('fedya', 'пойти'), ', to go. To the toilet is ', ('fedya', 'в'), ('fedya', 'туалет'), '.']),
    (3, None, ["'Wait, there is fire over there, friends!' Here fire, meaning the flames themselves, is ", ('fedya', 'огонь'), '. Friends is ', ('fedya', 'друзья'), '.']),
    (4, None, ["'The neighboring restaurant is burning right now!' Neighboring is ", ('senya', 'Соседний'), ', and is burning is ', ('senya', 'горит'), ', using the plain present for something going on right now.']),
    (5, None, ["'Are you sure that this is a real fire?' Sure is ", ('fedya', 'уверен'), ', said by a man. Fedya switches to ', ('fedya', 'пожар'), ' to ask if it is a serious fire, rather than just flame.']),
    (6, None, ["'Of course, look at this black smoke.' Look at is ", ('senya', 'посмотри'), ('senya', 'на'), ', and black smoke is ', ('senya', 'чёрный'), ('senya', 'дым'), '.']),
    (7, None, ["'People are running out of the building onto the street.' They run out is ", ('fedya', 'выбегают'), '. Onto the street is ', ('fedya', 'на'), ('fedya', 'улицу'), ', carrying an u at the end since that is where they are heading.']),
    (8, None, ["'We urgently need to tell the boss about this.' We need comes out as to us it is needed, ", ('senya', 'Нам'), ('senya', 'надо'), '. To the chef is ', ('senya', 'шефу'), ', ending with a u.']),
    (9, None, ["'Yes, he must know about this fire.' A casual way to say about is ", ('fedya', 'про'), '. Must is ', ('fedya', 'должен'), ', and to know follows straight after as ', ('fedya', 'знать'), '.']),
    (10, None, ["'Drop the cigarette and let's go inside faster.' An invitation like let's go is ", ('senya', 'пошли'), ', used with friends. The order to drop or throw is ', ('senya', 'Бросай'), '.']),
    (11, None, ["'I am running after you, open the door.' After you comes out as behind you, ", ('fedya', 'за'), ('fedya', 'тобой'), '. Open is ', ('fedya', 'открывай'), ', said to a friend.']),
]
