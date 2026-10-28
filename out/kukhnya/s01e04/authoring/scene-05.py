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
    ('barinov', 'Сегодня обед для персонала готовит наш огузок.', 'Today our runt is cooking lunch for the staff.', [(42, 'Сегодня обед для персонала готовит')], ''),
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
    (0, None, '\'This is not a shelter, but work!\' "Nochlezhka" is a place to sleep for the night, from "noch\'", night, and "lech\'", to lie down. "Ne... a" is the Russian "not X but Y".'),
    (1, None, '\'Chef, you still won\'t let me cook.\' "Vsyo ravno" is "all the same" or "still". "Ne dayote mne gotovit\'" is "you don\'t give me to cook", the Russian for "you don\'t let me".'),
    (2, None, '\'I already peeled all labels from the bananas.\' "Otkleil" has "ot-", off, in front of "kleit\'", to stick, so it means "unstuck". "Etiketki" is the borrowed "label".'),
    (3, None, '\'Fine, you want to cook — you will cook!\' The two halves mirror each other: "khochesh\' gotovit\'", "budesh\' gotovit\'". The chef is turning Max\'s wish against him.'),
    (4, None, '\'Attention, cooks of the restaurant!\' "Vnimaniye" is "attention". "Povara" is the plural of "cook", with the odd "-a" plural.'),
    (5, None, '\'Today our runt is cooking lunch for the staff.\' "Obed" is the midday meal. The cook comes at the end, so the news is saved for last.'),
    (6, None, '\'This is a very important assignment.\' "Otvetstvennoye" comes from "otvet", an answer, so it\'s a job you answer for. "Zadaniye" is an assignment, something "set" for you.'),
    (7, None, '\'If they don\'t like it, they will eat you.\' The joke is built from "to them it won\'t please" and "they will eat up". The "s-" on the front of "eat" means all of it, so Max would be eaten whole.'),
    (8, None, '\'Did you understand me?\' "Ponyal" is "understood", and the -l marks a man. The chef uses the friendly "you", as usual.'),
    (9, None, '\'Yes, Chef, I understood everything.\' Max repeats "ponyal" and adds "vsyo", everything. It\'s the answer a boss wants.'),
    (10, None, '\'I dreamed so much of cooking in the kitchen.\' "Mechtal" is a man\'s past of "to dream", and "tak" makes it "so". "Na kukhne" is "in the kitchen".'),
    (11, None, '\'Well, are you pleased?\' "Dovolen" is "content", and a woman would say "dovol\'na".'),
    (12, None, '\'I am very glad, Chef, just let me drink coffee.\' "Rad" is "glad", short for a man. "Vypyu" has the "vy-" that means "drink up".'),
    (13, None, '\'Quickly change clothes, let\'s get to work!\' Barinov tells Max to change with a word that starts "pere-", re-, and ends "-sya", yourself: re-dress yourself. Then "we work" does the job of "let\'s work".'),
]
