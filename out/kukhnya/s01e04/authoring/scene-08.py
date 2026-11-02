# Authoring module for kukhnya-s01e04-scene-08.
ID = 'kukhnya-s01e04-scene-08'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 4
SCENE = 8
TITLE = 'Ингредиенты для супа  (Ingredients for Soup)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'max': 'Макс', 'senya': 'Сеня'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.04'
SOURCE_FILE = 'sources/kukhnya/s01/e04.ru.dual.srt'
INTRO = "Max has been given his first real job, a cream soup, and Senya, the meat cook, hands him the ingredients and some advice. Max, as usual, promises it will be the best soup anyone has tasted. Here's the Russian first."
OPENER = "Let's go back to the soup station."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Max has the ingredients, the instructions and plenty of confidence. Notice how the phrase for oversalt starts with a part that means over, just like in English."
CLOSING = ('max', 'Пока!')
STORY = [
    ('senya', 'Вот твои сухарики, сливки и морковка.', 'Here are your croutons, cream, and carrot.', [(96, 'Вот твои хлебочки, сливки и морковка')], ''),
    ('max', 'Отлично, а где свежий лук?', 'Great, and where is the fresh onion?', [], ''),
    ('senya', 'Вот и лук, начинай варить суп.', 'Here is the onion, start boiling the soup.', [(97, 'вот и лук варим')], ''),
    ('max', 'Я сделаю самый вкусный крем-суп.', 'I will make the most delicious cream soup.', [], ''),
    ('senya', 'Главное, не пересоли бульон на плите.', 'The main thing is do not oversalt the broth on the stove.', [], ''),
    ('max', 'Не волнуйся, я знаю точный рецепт.', 'Do not worry, I know the exact recipe.', [], ''),
    ('senya', 'Сначала мелко нарежь лук и морковь.', 'First chop the onion and carrot finely.', [], ''),
    ('max', 'Я нарежу овощи ровными кусочками.', 'I will cut the vegetables into even pieces.', [], ''),
    ('senya', 'Затем добавь масло и тёплые сливки.', 'Then add butter and warm cream.', [], ''),
    ('max', 'Всё будет готово вовремя, Сеня.', 'Everything will be ready on time, Senya.', [], ''),
    ('senya', 'Я приду и проверю твоё блюдо.', 'I will come and check your dish.', [], ''),
    ('max', 'Ты будешь приятно удивлён этим супом!', 'You will be pleasantly surprised by this soup!', [], ''),
]
WALK = [
    (0, None, [
        "'Here are your croutons, cream, and carrot.' ",
        ('senya', 'сухарики,'),
        ' are little croutons, built from the expression for dry. ',
        ('senya', 'сливки'),
        ', the term for cream, only exists as a group of things, and ',
        ('senya', 'морковка.'),
        ' gives the everyday word for one carrot.'
    ]),
    (1, None, [
        "The little word for 'and' moves on to the next item. ",
        ' moves on to the next item. ',
        ('max', 'свежий лук?'),
        ' translates to fresh onion, and ',
        ('max', 'лук?'),
        ' stands for onions in general.'
    ]),
    (2, None, [
        "'Here is the onion, start boiling the soup.' ",
        ('senya', 'варить'),
        ' is cooking in water, so you use it for soup, eggs and coffee. ',
        ('senya', 'начинай'),
        ' is the Russian term for the instruction to begin.'
    ]),
    (3, None, [
        "'I will make the most delicious cream soup.' ",
        ('max', 'самый вкусный'),
        ' translates to the most tasty, made with ',
        ('max', 'самый'),
        ' in front. ',
        ('max', 'крем-суп.'),
        ', the term for cream soup, is borrowed.'
    ]),
    (4, None, [
        "'The main thing is do not oversalt the broth on the stove.' ",
        ('senya', 'пересоли'),
        ' is built from a starting part meaning over, plus the Russian term for to salt. The same starting part gives the term for overfry.'
    ]),
    (5, None, [
        "'Do not worry, I know the exact recipe.' ",
        ('max', 'Не волнуйся,'),
        " is the familiar way to say don't worry. ",
        ('max', 'точный рецепт.'),
        ' translates to exact recipe.'
    ]),
    (6, None, [
        "'First chop the onion and carrot finely.' ",
        ('senya', 'мелко'),
        ', meaning finely, is built from the phrase for small. ',
        ('senya', 'нарежь'),
        ' is built from a starting piece plus the expression for to cut.'
    ]),
    (7, None, [
        "'I will cut the vegetables into even pieces.' ",
        ('max', 'ровными кусочками.'),
        ' literally translates to with even little pieces, with the ending sounds standing in for with.'
    ]),
    (8, None, [
        "'Then add butter and warm cream.' An instruction to one person: ",
        ('senya', 'добавь'),
        ', meaning add, is built from the Russian expression for to add. ',
        ('senya', 'масло'),
        ', the term for butter, covers both butter and oil, and ',
        ('senya', 'сливки'),
        ', the Russian term for cream, is always a group of things, which is why the describing word ends the way it does.'
    ]),
    (9, None, [
        "'Everything will be ready on time, Senya.' ",
        ('max', 'будет готово'),
        ' translates to will be ready, with an ending to match ',
        ('max', 'Всё'),
        '. ',
        ('max', 'вовремя,'),
        ', the word for in time, is written as one word.'
    ]),
    (10, None, [
        "'I will come and check your dish.' ",
        ('senya', 'приду'),
        ' and ',
        ('senya', 'проверю'),
        " are single action words for things happening later. The first translates to I'll come, and the second translates to I'll check."
    ]),
    (11, None, [
        "'You will be pleasantly surprised by this soup!' ",
        ('max', 'удивлён'),
        ' translates to surprised when talking about a man. ',
        ('max', 'этим супом!'),
        ' translates to by this soup, using the ending sounds for by.'
    ]),
]
