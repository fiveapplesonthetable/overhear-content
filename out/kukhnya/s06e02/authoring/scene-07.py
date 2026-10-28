ID = 'kukhnya-s06e02-scene-07'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 2
SCENE = 7
TITLE = "Шалфей в галантине и визит префекта  (Sage in the Galantine and the Prefect's Visit)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = 'ru-en'
VOICES = {"narrator": "sky", "chef": "anja", "nastya": "angelina"}
LABELS = {"chef": "Шеф", "nastya": "Настя"}
SOURCE_NAME = 'Кухня (Kukhnya) S6.02'
SOURCE_FILE = 'sources/kukhnya/s06/e02.ru.srt'

INTRO = 'Back in the kitchen, Barinov explodes when Senya improvises with sage in his signature galantine, right before Nastya runs in to report that the district prefect is demanding pork ribs from the old menu.'

STORY = [
    ('nastya', 'Шеф, я немного шалфей добавил, попробуйте.', 'Chef, I added a little sage, try it.', [(111, 'шалфей добавил'), (112, 'Попробуйте')], 'adapted'),
    ('chef', 'Ты шалфей добавил?', 'You added sage?', [(112, 'Шалфей добавил?')], 'adapted'),
    ('chef', 'Это же блюдо Виктора Баринова!', 'This is a dish by Viktor Barinov!', [(114, 'Виктора Баринова')], 'adapted'),
    ('nastya', 'Шеф, мы можем ребрышки из старого меню приготовить?', 'Chef, can we prepare ribs from the old menu?', [(116, 'Шеф, мы можем ребрышки из старого меню')], 'adapted'),
    ('nastya', 'Там просто префект пришел, требует ребрышки.', 'The prefect just arrived out there and demands ribs.', [(117, 'Там просто префект пришел, требует ребрышки')], 'exact'),
    ('nastya', 'Он сказал, что половину слов в меню не понял.', 'He said that he did not understand half the words on the menu.', [(119, 'потому что половину слов он не понял')], 'adapted'),
    ('chef', 'У меня проверка из мэрии?', 'Do I have an inspection from city hall?', [(121, 'У меня проверка из мэрии')], 'adapted'),
    ('chef', 'Николай Марьянович, мое почтение!', 'Nikolai Maryanovich, my respects!', [(123, 'Николай Марьянович, мое почтение')], 'exact'),
    ('nastya', 'Здорово, Витя, кормить будешь?', 'Hello, Vitya, are you going to feed me?', [(124, 'Здорово, Витя. Что, кормить будешь?')], 'adapted'),
    ('chef', 'Я рад предложить вам блюда из моего авторского меню.', 'I am glad to offer you dishes from my auteur menu.', [(126, 'Я рад предложить вам блюда из моего авторского меню')], 'exact'),
    ('chef', 'Вы не волнуйтесь, все будет вкусно и быстро.', 'Do not worry, everything will be delicious and fast.', [(130, 'вы не волнуйтесь, все будет вкусно и быстро')], 'adapted'),
    ('chef', 'Выбирайте блюдо.', 'Choose a dish.', [(131, 'Выбирайте блюдо')], 'exact'),
]

OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."

WALK = [
    (0, None, "'Chef, I added a little sage, try it.' Senya anchors the line on 'Chef Barinov', while 'try' completes the thought."),
    (1, None, "'You added sage?' In spoken Russian, the words stay in their normal statement order and Chef Barinov's rising voice at the end turns the line into a question."),
    (2, None, "'This is a dish by Viktor Barinov!' Chef Barinov anchors the line on 'this', while 'dish' completes the thought. Nastya answers right away."),
    (3, None, "'Chef, can we prepare ribs from the old menu?' Here the Russian phrasing highlights 'Chef Barinov' before landing on 'to prepare'."),
    (4, None, "'The prefect just arrived out there and demands ribs.' The meaning hinges on 'there' working together with 'ribs' in spoken Russian."),
    (5, None, "'He said that he did not understand half the words on the menu.' The '-l' ending on the verb meaning 'understood' places the action in the masculine past tense. Chef Barinov answers right away."),
    (6, None, "'Do I have an inspection from city hall?' Here the Russian phrasing highlights 'at' before landing on 'city hall'."),
    (7, None, "'Nikolai Maryanovich, my respects!' Notice how Russian expresses 'Nikolai' and 'respect' with crisp inflection rather than helper words."),
    (8, None, "'Hello, Vitya, are you going to feed me?' Spoken Russian keeps this brisk, leaning on 'great' and finishing on 'will'. Chef Barinov answers right away."),
    (9, None, "'I am glad to offer you dishes from my auteur menu.' Chef Barinov anchors the line on 'I', while 'menu' completes the thought."),
    (10, None, "'Do not worry, everything will be delicious and fast.' Chef Barinov anchors the line on 'you', while 'quickly' completes the thought."),
    (11, None, "'Choose a dish.' The grammar packs 'choose' and 'dish' into a tight, idiomatic kitchen exchange."),
]

TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'Confident that his haute cuisine will win the prefect over, Barinov rushes back to the kitchen to plate his tiny masterpieces. Until next time!'
CLOSING = ("chef", "Увидимся!")
