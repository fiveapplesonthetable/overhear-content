# Authoring module for kukhnya-s01e17-scene-09.
ID = 'kukhnya-s01e17-scene-09'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 17
SCENE = 9
TITLE = 'Сезонное блюдо  (The Seasonal Dish)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'fedya': 'Федя', 'senya': 'Сеня'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.17'
SOURCE_FILE = 'sources/kukhnya/s01/e17.ru.dual.srt'
INTRO = 'It is contest day in the kitchen of Claude Monet. Barinov has asked the cooks for a new seasonal dish, and Senya steps up first. Here is the tasting in Russian.'
OPENER = "Let's go back to the tasting, slowly."
TRANSITION = 'Now the tasting again, without the pauses.'
OUTRO = 'Senya wins, the chef keeps his promise after one slip, and Fedya serves his chops to an empty room. Next time you\'re handed something odd, try "eto chto?", what is this? See you next time!'
CLOSING = ('barinov', 'Всё, всем пока!')
STORY = [
    ('senya', 'Шеф, попробуйте сезонное блюдо.', 'Chef, try the seasonal dish.', [(121, 'Попробуйте сезонное блюдо')], ''),
    ('barinov', 'Что?', 'What?', [(122, 'Что?')], ''),
    ('senya', 'Ну, вы же вчера дали задание.', 'Well, yesterday you gave us the task.', [(123, 'Ну, вы же вчера дали задание')], ''),
    ('barinov', 'Чтобы я с самого утра отравился?', 'So I get poisoned first thing in the morning?', [(124, 'чтобы я с самого утра отравился?')], ''),
    ('barinov', 'Ну, давайте что-то пробовать.', "Well, let's try something.", [(125, 'Ну, давайте что-то пробовать')], ''),
    ('barinov', 'Это что?', 'What is this?', [(126, 'Это что?')], ''),
    ('senya', 'Мясные рулеты из телятины с ветчиной.', 'Veal rolls with ham.', [(127, 'Мясные рулеты из телятины с тонкими ломтиками ветчины')], ''),
    ('barinov', 'Поздравляю, инвалид, твоё блюдо в меню.', 'Congratulations, cripple, your dish is on the menu.', [(128, 'Поздравляю, инвалид, твое блюдо в меню')], ''),
    ('senya', 'Шеф, подождите, это нечестно!', "Chef, wait, that's not fair!", [(129, 'Шеф, подождите, шеф, это не честно')], ''),
    ('senya', 'Вы же обещали не называть победителя инвалидом.', 'You promised not to call the winner a cripple.', [(130, 'Вы же обещали мне называть победителя инвалидом')], ''),
    ('barinov', 'Да, поздравляю, коллега.', 'Yes, congratulations, colleague.', [(131, 'Да, поздравляю, коллега')], ''),
    ('fedya', 'Шеф, а как же мы?', 'Chef, and what about us?', [(132, 'Шеф, а'), (133, 'Как же мы?')], ''),
    ('barinov', 'Не нужно, я его нашёл.', "No need, I've found it.", [(133, 'Не нужно было сезонное блюдо, я его нашёл')], ''),
    ('fedya', 'Бараньи котлеты по-бретонски со спаржей.', 'Breton lamb chops with asparagus.', [(134, 'Баранья котлеты по-бретонски со спаржей')], ''),
]
WALK = [
    (0, None, '\'Chef, try the seasonal dish.\' "Poprobuyte" is the polite "try", ending in "-yte" because Senya says "vy" to his boss. "Sezonnoe" matches "blyudo", dish.'),
    (1, None, '\'What?\' Just "chto", said flat, as if a dish at this hour is the last thing he wants.'),
    (2, None, '\'Well, yesterday you gave us the task.\' "Zhe" adds "but you did!", so Senya is reminding him. "Zadanie" is a task, the same word as a school assignment.'),
    (3, None, '\'So I get poisoned first thing in the morning?\' "Chtoby" is "so that", and the verb after it stays past: "otravilsya", got poisoned. "S samogo utra" is "from the very morning".'),
    (4, None, '\'Well, let\'s try something.\' "Davayte" is "let\'s" said to a group; to one person it would be "davay". "Chto-to" is "something".'),
    (5, None, '\'What is this?\' "Eto chto?" puts "this" first, which sounds blunter than "chto eto?".'),
    (6, None, '\'Veal rolls with ham.\' "Iz telyatiny" is "out of veal". After "s", with, "vetchina", ham, becomes "vetchinoy".'),
    (7, None, '\'Congratulations, cripple, your dish is on the menu.\' "Pozdravlyayu", I congratulate, is how Russian says "congratulations". "Menyu" never changes its ending.'),
    (8, None, '\'Chef, wait, that\'s not fair!\' "Nechestno" is "ne", not, glued to "chestno", honestly. "Podozhdite" is the polite "wait".'),
    (9, None, '\'You promised not to call the winner a cripple.\' After "nazyvat", to call, the name takes the instrumental: "invalid" becomes "invalidom".'),
    (10, None, '\'Yes, congratulations, colleague.\' "Kollega" ends in "-a" but works for a man too, so the chef can say it to Senya.'),
    (11, None, '\'Chef, and what about us?\' "Kak zhe" shows up whenever someone feels forgotten: "a kak zhe my?", and what about us?'),
    (12, None, '\'No need, I\'ve found it.\' "Nashyol", found, comes from "nayti", to find. "Ego", it, points back to the dish, because "blyudo" is not feminine.'),
    (13, None, '\'Breton lamb chops with asparagus.\' Fedya presents his dish anyway, to nobody. "Po-bretonski" is "the Breton way", like "po-russki", the Russian way. "So" is "s", with, before the "sp" of "sparzhey".'),
]
