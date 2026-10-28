# Authoring module for kukhnya-s01e06-scene-11.
ID = 'kukhnya-s01e06-scene-11'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 6
SCENE = 11
TITLE = "Визит инспектора  (The Inspector's Visit)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'inspector': 'Инспектор', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.06'
SOURCE_FILE = 'sources/kukhnya/s01/e06.ru.dual.srt'
INTRO = "The sanitary inspector has finished with the dining room at Claude Monet, and Vika, the manager, walks him through to the kitchen. She is polite and confident. He is polite and very, very thorough. It's in Russian first, with a lot of formal language."
OPENER = 'Let\'s go back through it. Both of them use the polite "vy", and both talk like an official letter.'
TRANSITION = 'And now the tour from the start, without stopping.'
OUTRO = 'This was Russian at its most formal: "prokhodite", "proshu vas", "dobro pozhalovat". It\'s the opposite of the shouting in the kitchen, and it\'s what you\'ll hear at any office or front desk. See you next time.'
CLOSING = ('vika', 'Пока!')
STORY = [
    ('vika', 'Проходите, пожалуйста, вот и наша кухня.', 'Come in, please, here is our kitchen.', [(157, 'А вот и наша кухня'), (158, 'Прошу вас')], ''),
    ('inspector', 'По залу у меня претензий нет.', 'Regarding the hall, I have no complaints.', [(158, 'по залу у меня никаких претензий нет')], ''),
    ('vika', 'Мы строго следим за чистотой везде.', 'We strictly monitor cleanliness everywhere.', [], ''),
    ('inspector', 'Теперь посмотрим на вашу кухню внимательно.', "Now let's look at your kitchen carefully.", [(159, 'Посмотрим вашу кухню')], ''),
    ('vika', 'У нас здесь работают лучшие повара.', 'We have the best cooks working here.', [], ''),
    ('inspector', 'Меня интересуют только санитарные правила.', 'I am interested only in sanitary rules.', [], ''),
    ('vika', 'Все сотрудники носят чистую форму.', 'All employees wear a clean uniform.', [], ''),
    ('inspector', 'Я сам проверю каждое рабочее место.', 'I myself will check every workstation.', [], ''),
    ('vika', 'Наш шеф-повар лично всё контролирует.', 'Our head chef personally oversees everything.', [], ''),
    ('inspector', 'На кухне нельзя нарушать правила.', 'In the kitchen one must not violate rules.', [], ''),
    ('vika', 'Вы можете увидеть всё сами.', 'You can see everything yourself.', [], ''),
    ('inspector', 'Тогда начинаем полную санитарную проверку.', 'Then we begin a full sanitary inspection.', [], ''),
    ('vika', 'Добро пожаловать на нашу кухню!', 'Welcome to our kitchen!', [], ''),
]
WALK = [
    (0, None, '\'Come in, please, here is our kitchen.\' "Prokhodite", come through, is what a host says to wave a guest further in. "Vot" i, \'and here is\', points at something you\'ve been heading for.'),
    (1, None, '\'Regarding the hall, I have no complaints.\' "Po zalu", \'as for the hall\', is "po" with -u added to "zal". After "net", no, "pretenzii", complaints, becomes "pretenziy".'),
    (2, None, '\'We strictly monitor cleanliness everywhere.\' "Sledim za", \'we watch over\', takes "za", and "chistota" changes to "chistotoy" after it. "Strogo", strictly, is from "strogiy", strict.'),
    (3, None, '\'Now let\'s look at your kitchen carefully.\' "Posmotrim", let\'s look, uses the \'we\' ending to mean \'let\'s\'. "Na vashu kukhnyu", at your kitchen, has -u twice because it\'s what he\'s looking at.'),
    (4, None, '\'We have the best cooks working here.\' "Rabotayut luchshie povara" is \'work the best cooks\', with the subject coming last. "Povara", cooks, is the plural of "povar", with the stress at the end.'),
    (5, None, '\'I am interested only in sanitary rules.\' "Menya interesuyut" is \'me interest\', so the rules do the interesting and he is the object. That\'s why it\'s "menya", not "ya".'),
    (6, None, '\'All employees wear a clean uniform.\' "Sotrudniki", staff, is the formal word, built from so-, with, and "trud", labour. "Nosyat", they wear, is from "nosit", which also means \'to carry around\'.'),
    (7, None, '\'I myself will check every workstation.\' "Sam", myself, is a way of saying he won\'t take anyone\'s word for it. "Kazhdoe", every, ends in -oe to match "mesto", place.'),
    (8, None, '\'Our head chef personally oversees everything.\' "Lichno", personally, is from "lichnyy", personal. "Kontroliruet", he oversees, is a borrowed word with the regular -et ending for \'he\'.'),
    (9, None, '\'In the kitchen one must not violate rules.\' "Nelzya", \'not allowed\', is followed by a plain verb: "nelzya narushat", mustn\'t break. It\'s the word you\'ll see on prohibition signs.'),
    (10, None, '\'You can see everything yourself.\' "Vy mozhete", you can, is the polite form. "Sami", yourself, is plural because it goes with "vy", even for one person.'),
    (11, None, '\'Then we begin a full sanitary inspection.\' "Nachinaem", we begin, ends in -em, the \'we\' ending. "Polnuyu" and "sanitarnuyu" both end in -uyu to match "proverku".'),
    (12, None, '\'Welcome to our kitchen!\' "Dobro pozhalovat", welcome, is a fixed phrase you\'ll see on signs at every town gate. It\'s "na kukhnyu", not v, because Russians work \'on\' a kitchen.'),
]
