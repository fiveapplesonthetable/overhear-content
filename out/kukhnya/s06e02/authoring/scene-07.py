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
    (0, None, '\'Chef, I added a little sage, try it.\' Senya features one vivid piece for Barinov: "poprobuyte" means "try, taste" (from "poprobovat"), giving the line its exact edge.'),
    (1, None, "'You added sage?' Barinov shares the remark plainly here: Russian keeps the exact word order of a normal statement here, turning it into a question for Senya purely through rising pitch at the end."),
    (2, None, "'This is a dish by Viktor Barinov!' Barinov fires back promptly beside Nastya, steering the talk right where he wants it."),
    (3, None, '\'Chef, can we prepare ribs from the old menu?\' See how Nastya reminds Senya plainly here — the Russian word "rebryshki" ("ribs", built from "ryobryshko") does the heavy lifting.'),
    (4, None, '\'The prefect just arrived out there and demands ribs.\' Nastya states the comment facing Barinov: the little word "prosto" ("simply, just") works like a shrug in the sentence, making a big claim sound effortless.'),
    (5, None, "'He said that he did not understand half the words on the menu.' Nastya speaks lightly without holding back, testing Senya's reaction in the middle of the exchange."),
    (6, None, '\'Do I have an inspection from city hall?\' Barinov colors one practical choice toward Nastya: "proverka" means "a test", and it carries the main weight of what Barinov is saying.'),
    (7, None, "'Nikolai Maryanovich, my respects!' Barinov puts this point around Senya: spoken Russian trims this down to just 4 words, dropping the extra helper words that English has to spell out."),
    (8, None, "'Hello, Vitya, are you going to feed me?' Senya challenges evenly where this conversation is heading next."),
    (9, None, '\'I am glad to offer you dishes from my auteur menu.\' Barinov underscores this clear touch on cue: "avtorskogo" means "author\'s, signature" (from "avtorskiy"), giving the line its exact edge.'),
    (10, None, '\'Do not worry, everything will be delicious and fast.\' Barinov shapes that thought toward Nastya: the "-sya" ending on "volnuytes" ("worry") turns the action inward or makes it happen between people naturally.'),
    (11, None, "'Choose a dish.' Barinov proceeds lightly toward Senya, bringing things back to earth after the buildup."),
]
