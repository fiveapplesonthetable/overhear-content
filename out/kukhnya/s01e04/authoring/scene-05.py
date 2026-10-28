# Authoring module for kukhnya-s01e04-scene-05.
ID = 'kukhnya-s01e04-scene-05'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 4
SCENE = 5
TITLE = 'Обед для персонала  (Staff Lunch)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.04'
SOURCE_FILE = 'sources/kukhnya/s01/e04.ru.dual.srt'
INTRO = "The chef is fed up with Max's naps, but Max is fed up with peeling bananas. Barinov gives him his first real job: cooking staff lunch, with a warning about what happens if they don't like it. Here's the Russian first."
OPENER = "Let's go through the chef's offer."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'Max finally has a real assignment, even if it\'s a risky one. You\'ve heard "ty menya ponyal?", "did you understand me?", which is the classic boss line.'
CLOSING = ('max', 'До встречи!')
STORY = [
    ('barinov', 'Здесь не ночлежка, а работа!', 'This is not a shelter, but work!', [(37, 'Здесь не ночлежка, работа')], ''),
    ('max', 'Шеф, вы всё равно не даёте мне готовить.', "Chef, you still won't let me cook.", [(38, 'вы все равно мне готовить не даете')], ''),
    ('max', 'Я уже отклеил все этикетки от бананов.', 'I already peeled all labels from the bananas.', [(39, 'этикетки от бананов я уже')], ''),
    ('barinov', 'Хорошо, хочешь готовить — будешь готовить!', 'Fine, you want to cook — you will cook!', [(40, 'Хочешь готовить, будешь готовить')], ''),
    ('barinov', 'Внимание, повара ресторана!', 'Attention, cooks of the restaurant!', [(41, 'Внимание')], ''),
    ('barinov', 'Сегодня обед для персонала готовит наш огузок.', 'Today our Oguzok is cooking lunch for the staff.', [(42, 'Сегодня обед для персонала готовит')], ''),
    ('barinov', 'Это очень ответственное задание.', 'This is a very important assignment.', [(43, 'Это очень ответственное задание')], ''),
    ('barinov', 'Если им не понравится, они съедят тебя.', "If they don't like it, they will eat you.", [(44, 'Если им не понравится'), (44, 'съесть тебя')], ''),
    ('barinov', 'Ты меня понял?', 'Did you understand me?', [(45, 'Понял')], ''),
    ('max', 'Да, шеф, я всё понял.', 'Yes, Chef, I understood everything.', [(45, 'Понял')], ''),
    ('max', 'Я так мечтал готовить на кухне.', 'I dreamed so much of cooking in the kitchen.', [(47, 'Я так мечтал')], ''),
    ('barinov', 'Ну что, ты доволен?', 'Well, are you pleased?', [(49, 'Ну, ты доволен')], ''),
    ('max', 'Я очень рад, шеф, только выпью кофе.', 'I am very glad, Chef, just let me drink coffee.', [(49, 'Я очень рад, шеф, только')], ''),
    ('barinov', 'Быстро переодевайся, работаем!', "Quickly change clothes, let's get to work!", [(50, 'Переодевайся'), (51, 'Работаем')], ''),
]
WALK = [
    (0, None, '\'This is not a shelter, but work!\' "Nochlezhka" is a dosshouse, from "nochleg", a night\'s lodging. "Ne... a" is Russian for "not X but Y".'),
    (1, None, '\'Chef, you still won\'t let me cook.\' "Vsyo ravno" is "all the same", meaning still. "Ne dayote mne gotovit\'" is "you don\'t give me to cook", Russian for "won\'t let me".'),
    (2, None, '\'I already peeled all labels from the bananas.\' "Otkleil" is "ot-", off, with "kleit\'", to glue: unglued. "Etiketki" are labels, and "ot bananov" is "from the bananas".'),
    (3, None, '\'Fine, you want to cook — you will cook!\' The halves mirror each other: "khochesh\' gotovit\'", you want to cook, then "budesh\' gotovit\'", you will cook.'),
    (4, None, '\'Attention, cooks of the restaurant!\' "Vnimaniye" is "attention". "Povara", cooks, takes -a for its plural, and "restorana" is "of the restaurant".'),
    (5, None, '\'Today our Oguzok is cooking lunch for the staff.\' "Obed" is the midday meal. The subject, "nash oguzok", comes last, so the news lands at the end.'),
    (6, None, '\'This is a very important assignment.\' "Otvetstvennoye", responsible, has "otvet", answer, inside: a job you answer for. "Zadaniye" is something "zadano", set, for you.'),
    (7, None, '\'If they don\'t like it, they will eat you.\' "Im ne ponravitsya" is "to them it won\'t be pleasing". "S\'\'yedyat", they will eat up, has "s-" for finishing the whole thing.'),
    (8, None, '\'Did you understand me?\' "Ty menya ponyal?" is "you me understood?". "Ponyal" ends in -l for a man.'),
    (9, None, '\'Yes, Chef, I understood everything.\' Max repeats "ponyal" and adds "vsyo", everything.'),
    (10, None, '\'I dreamed so much of cooking in the kitchen.\' "Mechtal" is the man\'s past of "mechtat\'", to dream. "Tak" is "so much", and "na kukhne" is "in the kitchen".'),
    (11, None, '\'Well, are you pleased?\' "Dovolen", pleased, is the man\'s short form, and a woman says "dovol\'na". "Nu chto" is "well then".'),
    (12, None, '\'I am very glad, Chef, just let me drink coffee.\' "Rad" is "glad" for a man. "Vypyu", I\'ll drink, has "vy-" for drinking it up, and "tol\'ko" is "just".'),
    (13, None, '\'Quickly change clothes, let\'s get to work!\' "Pereodevaysya" is "pere-", again, plus "odevaysya", dress yourself: change. "Rabotayem", we work, serves as "let\'s work".'),
]
