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
OUTRO = 'Senya has won before anyone else has even served. Next time you\'re handed something odd, try "a eto chto takoe?", and what on earth is this? See you next time!'
CLOSING = ('barinov', 'Всё, всем пока!')
STORY = [
    ('senya', 'Шеф, попробуйте новое блюдо.', 'Chef, try the new dish.', [(121, 'Попробуйте сезонное блюдо')], ''),
    ('barinov', 'Что? Какое ещё блюдо?', 'What? What dish?', [(122, 'Что?')], ''),
    ('senya', 'Вы же вчера дали нам задание.', 'Yesterday you gave us an assignment.', [(123, 'вы же вчера дали задание')], ''),
    ('barinov', 'Ну, давай попробуем.', "Well, let's try it.", [(125, 'пробовать')], ''),
    ('barinov', 'А это что такое?', 'And what is this?', [(126, 'Это что?')], ''),
    ('senya', 'Это нежное мясо с тонкой ветчиной.', 'This is tender meat with thin ham.', [(127, 'с тонкими ломтиками ветчины')], ''),
    ('barinov', 'Очень вкусно, мне нравится этот рецепт!', 'Very tasty, I like this recipe!', [], ''),
    ('barinov', 'Поздравляю, твоё блюдо теперь в меню.', 'Congratulations, your dish is now on the menu.', [(128, 'Поздравляю, инвалид, твое блюдо в меню')], ''),
    ('fedya', 'Шеф, подождите, это совсем нечестно!', 'Chef, wait, this is completely unfair!', [(129, 'Шеф, подождите, шеф, это не честно')], ''),
    ('senya', 'Спасибо большое, шеф, я очень рад!', 'Thank you very much, Chef, I am very glad!', [], ''),
    ('fedya', 'Поздравляю тебя с победой, коллега.', 'Congratulations on the victory, colleague.', [(131, 'Да, поздравляю, коллега')], ''),
    ('fedya', 'Шеф, а как же наши блюда?', 'Chef, what about our dishes?', [(133, 'Как же мы?')], ''),
    ('barinov', 'Мне больше ничего не нужно, я нашёл.', 'I do not need anything else, I found it.', [(133, 'я его нашёл')], ''),
]
WALK = [
    (0, None, '\'Chef, try the new dish.\' "Poprobuyte" is the polite "try", ending in "-yte" because Senya says "vy" to his boss.'),
    (1, None, '\'What? What dish?\' "Kakoe eshchyo" is literally "what else", and it sounds grumpy, as if one more dish is the last thing he needs.'),
    (2, None, '\'But yesterday you gave us a task.\' "Zhe" adds "but you did!", so Senya is reminding him. "Zadanie" is a task, the same word as a school assignment.'),
    (3, None, '\'Well, let\'s try it.\' "Davay poprobuem" is "let\'s try" said to one person; to the whole team he\'d say "davayte".'),
    (4, None, '\'And what is this?\' "Takoe" on the end of "chto" adds suspicion, like "what on earth is this?".'),
    (5, None, '\'This is tender meat with thin ham.\' "Nezhnoe", tender, matches "myaso", meat. After "s", with, "tonkaya vetchina" becomes "tonkoy vetchinoy".'),
    (6, None, '\'Very tasty, I like this recipe!\' "Mne nravitsya" is literally "to me it is pleasing": in Russian the recipe does the pleasing.'),
    (7, None, '\'Congratulations, your dish is on the menu now.\' "Pozdravlyayu", I congratulate, is how Russian says "congratulations". "Menyu" never changes its ending.'),
    (8, None, '\'Chef, wait, this is completely unfair!\' "Nechestno" is "ne", not, glued to "chestno", honestly.'),
    (9, None, '\'Thank you so much, chef, I\'m really glad!\' "Rad" means glad when a man says it; a woman would say "rada".'),
    (10, None, '\'Congratulations on your win, colleague.\' "Pozdravlyayu s" is "congratulations on", and "pobeda", victory, turns into "pobedoy" after "s".'),
    (11, None, '\'Chef, what about our dishes?\' "Kak zhe" shows up whenever someone feels forgotten: "a kak zhe my?", and what about us?'),
    (12, None, '\'I don\'t need anything else, I\'ve found it.\' "Nashyol", found, comes from "nayti", to find. "Bolshe nichego" is "nothing more".'),
]
