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
INTRO = "It is contest day in the kitchen of Claude Monet. Barinov has asked the cooks for a new seasonal dish, and Senya steps up first. We'll hear it in Russian first."
OPENER = "Now let's take it step by step."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Senya has won before anyone else has even served. When you rewatch, notice how Barinov asks 'what is this?' with an extra word, as if the dish might bite. See you next time!"
CLOSING = ('senya', 'Пока!')
STORY = [
    ('senya', 'Шеф, попробуйте новое блюдо.', 'Chef, try the new dish.', [(121, 'Попробуйте сезонное блюдо')], ''),
    ('barinov', 'Что? Какое ещё блюдо?', 'What? What dish?', [(122, 'Что?')], ''),
    ('senya', 'Вы же вчера дали нам задание.', 'Yesterday you gave us an assignment.', [(123, 'вы же вчера дали задание')], ''),
    ('barinov', 'Ладно, давай будем пробовать.', 'All right, let us try it.', [(125, 'пробовать')], ''),
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
    (0, None, "'Chef, try the new dish.' The command is the polite one, with the 'po' prefix that means 'try some'. 'New' ends in 'oe' for the neuter 'dish'."),
    (1, None, "'What? What dish?' The second 'what' is 'which' with a little 'else' attached. Together they mean 'what dish on earth?'."),
    (2, None, "'But yesterday you gave us an assignment.' The small word 'zhe' means 'but', reminding him. 'Assignment' is built from the verb for 'to set'."),
    (3, None, "'All right, let's try it.' 'Davay' with 'we will be' and the plain 'try' is a casual way to say 'let's'. Barinov uses the casual form with Senya."),
    (4, None, "'And what is this?' The two words 'what such' make it more pointed, as in 'what exactly is this?'. A bit suspicious, and a bit curious."),
    (5, None, "'It's tender meat with thin ham.' 'With' makes 'ham' take an 'oy' ending, and 'thin' follows it. 'Tender' and 'meat' both end in 'oe'."),
    (6, None, "'Very tasty, I like this recipe!' 'Tasty' ends in 'o' when it describes a thing. 'I like' is 'to me pleases', so the recipe does the pleasing."),
    (7, None, "'Congratulations, your dish is now on the menu.' The word for 'menu' never changes its ending, even after 'in'. It is a borrowed word that stays put."),
    (8, None, "'Chef, wait, this is completely unfair!' 'Unfair' is 'not' plus 'honestly', stuck together. 'Completely' is a handy intensifier."),
    (9, None, "'Thank you very much, Chef, I'm very glad!' The short form for 'glad' ends in a bare consonant for a man. 'Thanks' is a neuter noun, so 'big' ends in 'oe'."),
    (10, None, "'Congratulations on your win, colleague.' Russians say 'I congratulate with victory', using the little word for 'with'. 'Colleague' ends in 'a' but is masculine."),
    (11, None, "'Chef, what about our dishes?' The opening words, 'and how then', protest politely. 'Dishes' is plural, with an 'a' ending."),
    (12, None, "'I don't need anything else, I've found it.' Russian has 'more nothing not needed', which makes three negatives in a row. 'Found' ends in the masculine 'l'."),
]
