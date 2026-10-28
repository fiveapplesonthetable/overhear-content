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
INTRO = "In the kitchen of Claude Monet, the cooks present their creations for the new seasonal menu to Chef Barinov. Senya steps forward first with his veal and ham dish, hoping to win the competition before anyone else gets a chance. Let's listen to the tasting in Russian first."
OPENER = "Now let's examine this conversation line by line."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Having found a seasonal special on the very first try, Chef Barinov calls off the rest of the tasting and leaves Senya basking in his victory. Next time you watch the episode, listen for the Russian expressions for 'to try' and 'new' — you will catch every word right away. See you next time!"
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
    (0, None, "'Chef, try the new dish.' Senya eagerly presents his culinary creation to the boss."),
    (1, None, "'What? What dish?' Barinov acts confused, pretending he forgot about the competition."),
    (2, None, "'Yesterday you gave us an assignment.' Senya reminds him of the assignment given the day before."),
    (3, None, "'All right, let us try it.' Barinov agrees to give the plate a try."),
    (4, None, "'And what is this?' Barinov asks his chef to explain what is on the plate."),
    (5, None, "'This is tender meat with thin ham.' Senya proudly describes the combination of tender meat and thin ham."),
    (6, None, "'Very tasty, I like this recipe!' Barinov loves the recipe, praising its fantastic taste."),
    (7, None, "'Congratulations, your dish is now on the menu.' Barinov declares the dish a winner and adds it to the menu."),
    (8, None, "'Chef, wait, this is completely unfair!' Fedya complains loudly that the immediate decision is completely unfair."),
    (9, None, "'Thank you very much, Chef, I am very glad!' Senya ignores the complaint, thanking the boss profusely."),
    (10, None, "'Congratulations on the victory, colleague.' Fedya sarcastically congratulates his coworker on the victory."),
    (11, None, "'Chef, what about our dishes?' Fedya asks about the fate of the remaining dishes."),
    (12, None, "'I do not need anything else, I found it.' Barinov dismisses the rest of the staff, completely satisfied with his choice."),
]
