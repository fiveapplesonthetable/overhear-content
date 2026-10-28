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
OUTRO = "The two of them rush off to tell the chef. Remember the difference: 'ogon' is a flame, 'pozhar' is a fire you call for help about. Bye for now."
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
    (0, None, "'This cigarette already tastes bitter.' 'Gorchit' is a verb, 'tastes bitter', made from 'gorkiy', bitter. 'Sigareta' is feminine, so 'this' is 'eta', and 'na vkus' is 'to the taste'."),
    (1, None, "'Just throw it out quickly into the trash bin.' The 'it' is 'her', since cigarettes are feminine in Russian. 'V urnu' is 'into the bin': 'urna' ends in 'u' because the cigarette is going into it."),
    (2, None, "'All right, I want to go to the bathroom.' 'Khochu' is 'I want', and the thing he wants follows it straight, 'to go'. 'V tualet' is 'to the toilet', and the word itself comes from the French 'toilette'."),
    (3, None, "'Wait, there is fire over there, friends!' 'Ogon' is fire, the flames themselves. 'Druzya' is 'friends', an irregular plural of 'drug', a friend."),
    (4, None, "'The neighboring restaurant is burning right now!' 'Sosedniy' is 'neighbouring', from 'sosed', neighbour. 'Gorit' is 'is burning', and Russian uses the plain present for something going on right now."),
    (5, None, "'Are you sure that this is a real fire?' 'Uveren' is 'sure', with a man's bare ending. 'Pozhar' is a fire as a disaster, a building on fire, while 'ogon' is just flame. Fedya switches to 'pozhar' to ask if it's the serious kind."),
    (6, None, "'Of course, look at this black smoke.' 'Posmotri na' is 'look at', with 'na' doing the job of 'at'. 'Chyornyy dym' is 'black smoke', and both are masculine."),
    (7, None, "'People are running out of the building onto the street.' 'Vybegayut' is 'they run out', from 'vy', 'out', and 'begat', 'run'. 'Na ulitsu' is 'onto the street', and the 'u' ending shows direction."),
    (8, None, "'We urgently need to tell the boss about this.' 'Nam nado' is literally 'to us it's needed', so the people who need it are in the 'to' form, 'nam'. 'Shefu' is 'to the chef', with the same 'to' ending, 'u'."),
    (9, None, "'Yes, he must know about this fire.' 'Pro' is a casual 'about', while Senya used the neutral 'ob' a line ago. 'Dolzhen' is 'must', and 'znat', to know, follows in its basic form."),
    (10, None, "'Drop the cigarette and let's go inside faster.' 'Poshli' looks like 'they went', but in speech it's an invitation, 'let's go'. Say it to friends. 'Brosay' is an order, and it can mean 'drop' or 'throw'."),
    (11, None, "'I am running after you, open the door.' 'After you' is literally 'behind you', in the form with 'oy' on the end. 'Otkryvay' is 'open!', the 'ty' form, said to one friend."),
]
