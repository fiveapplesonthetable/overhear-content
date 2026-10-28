# Authoring module for kukhnya-s06e02-scene-07.
ID = 'kukhnya-s06e02-scene-07'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 2
SCENE = 7
TITLE = "Шалфей в галантине и визит префекта  (Sage in the Galantine and the Prefect's Visit)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'nastya': 'Настя', 'senya': 'Сеня'}
SOURCE_NAME = 'Кухня (Kukhnya) S6.02'
SOURCE_FILE = 'sources/kukhnya/s06/e02.ru.srt'
INTRO = 'Back in the kitchen, Barinov explodes when Senya improvises with sage in his signature galantine, right before Nastya runs in to report that the district prefect is demanding pork ribs from the old menu.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'Confident that his haute cuisine will win the prefect over, Barinov rushes back to the kitchen to plate his tiny masterpieces. Until next time!'
CLOSING = ('barinov', 'Увидимся!')
STORY = [
    ('senya', 'Шеф, я немного шалфей добавил, попробуйте.', 'Chef, I added a little sage, try it.', [(111, 'шалфей добавил'), (112, 'Попробуйте')], 'adapted'),
    ('barinov', 'Ты шалфей добавил?', 'You added sage?', [(112, 'Шалфей добавил?')], 'adapted'),
    ('barinov', 'Это же блюдо Виктора Баринова!', 'This is a dish by Viktor Barinov!', [(114, 'Виктора Баринова')], 'adapted'),
    ('nastya', 'Шеф, мы можем ребрышки из старого меню приготовить?', 'Chef, can we prepare ribs from the old menu?', [(116, 'Шеф, мы можем ребрышки из старого меню')], 'adapted'),
    ('nastya', 'Там просто префект пришел, требует ребрышки.', 'The prefect just arrived out there and demands ribs.', [(117, 'Там просто префект пришел, требует ребрышки')], 'exact'),
    ('nastya', 'Он сказал, что половину слов в меню не понял.', 'He said that he did not understand half the words on the menu.', [(119, 'потому что половину слов он не понял')], 'adapted'),
    ('barinov', 'У меня проверка из мэрии?', 'Do I have an inspection from city hall?', [(121, 'У меня проверка из мэрии')], 'adapted'),
    ('barinov', 'Николай Марьянович, мое почтение!', 'Nikolai Maryanovich, my respects!', [(123, 'Николай Марьянович, мое почтение')], 'exact'),
    ('senya', 'Здорово, Витя, кормить будешь?', 'Hello, Vitya, are you going to feed me?', [(124, 'Здорово, Витя. Что, кормить будешь?')], 'adapted'),
    ('barinov', 'Я рад предложить вам блюда из моего авторского меню.', 'I am glad to offer you dishes from my auteur menu.', [(126, 'Я рад предложить вам блюда из моего авторского меню')], 'exact'),
    ('barinov', 'Вы не волнуйтесь, все будет вкусно и быстро.', 'Do not worry, everything will be delicious and fast.', [(130, 'вы не волнуйтесь, все будет вкусно и быстро')], 'adapted'),
    ('barinov', 'Выбирайте блюдо.', 'Choose a dish.', [(131, 'Выбирайте блюдо')], 'exact'),
]
WALK = [
    (0, None, '\'Chef, I added a little sage, try it.\' Highlighting a sage on the spot, Senya leans on "shalfey" ("sage") to give the whole sentence its punch.'),
    (1, None, "'You added sage?' Pressing on candidly right here, Barinov keeps normal statement word order here, turning the line into a question for Senya purely through rising pitch."),
    (2, None, "'This is a dish by Viktor Barinov!' Barinov fires back promptly with a smile, watching Nastya's face to see how the news lands."),
    (3, None, '\'Chef, can we prepare ribs from the old menu?\' Emphasizing the ribs in the exchange, Nastya reaches for the Russian word "rebryshki" ("ribs", built from "ryobryshko") right at the center of the line.'),
    (4, None, '\'The prefect just arrived out there and demands ribs.\' Dwelling on the ribs during the talk, Nastya uses the little word "prosto" ("simply, just") to make the point sound effortless.'),
    (5, None, "'He said that he did not understand half the words on the menu.' Nastya replies lightly in this moment, watching Barinov's face to see how the news lands."),
    (6, None, '\'Do I have an inspection from city hall?\' Focusing on the test right here, Barinov puts the emphasis on "proverka" ("a test") in the middle of the talk.'),
    (7, None, "'Nikolai Maryanovich, my respects!' Checking on the respect on the spot, spoken Russian compresses the whole thought into just 4 words, skipping the extra helper words English needs."),
    (8, None, "'Hello, Vitya, are you going to feed me?' Senya challenges evenly about what Barinov just brought up."),
    (9, None, '\'I am glad to offer you dishes from my auteur menu.\' Explaining how glad he is at once, Barinov puts the weight on "avtorskogo" ("author\'s, signature", from "avtorskiy") as the exchange unfolds.'),
    (10, None, '\'Do not worry, everything will be delicious and fast.\' Opening up firmly before Senya, the "-sya" ending on "volnuytes" ("worry") marks an action that unfolds mutually or turns back on the speaker.'),
    (11, None, "'Choose a dish.' Barinov speaks lightly with a shrug, before Senya can change the subject."),
]
