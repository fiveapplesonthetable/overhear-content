# Authoring module for kukhnya-s01e17-scene-07.
ID = 'kukhnya-s01e17-scene-07'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 17
SCENE = 7
TITLE = 'Неудачное знакомство  (An Unsuccessful Introduction)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'max': 'Макс', 'nastya': 'Настя', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.17'
SOURCE_FILE = 'sources/kukhnya/s01/e17.ru.dual.srt'
INTRO = "At the bar, Nastya and Kostya arrive and Max starts the introductions, which go wrong right away. Nastya and Vika already know each other from work, and Max is clearly trying to keep the peace. We'll hear it in Russian first."
OPENER = "Now we'll take it line by line."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Max heads off for drinks and leaves them to it, which is rarely a good idea. The line 'Vika and I' is said as 'we with Vika' in Russian, so keep an eye on that. See you next time!"
CLOSING = ('max', 'Пока!')
STORY = [
    ('nastya', 'Привет! А вот и мы.', 'Hi! Here we are.', [(86, 'бы здесь поработал.')], ''),
    ('max', 'А, познакомьтесь, это Вика.', 'Oh, meet Vika.', [], ''),
    ('nastya', 'Вообще-то мы знакомы с Викторией Сергеевной.', 'Actually, we know Victoria Sergeyevna.', [], ''),
    ('max', 'Не-не-не, стоп. Это просто Вика, моя девушка.', 'No, stop. She is just Vika, my girlfriend.', [], ''),
    ('max', 'Вика, а это просто Настя и Костя.', 'Vika, this is just Nastya and Kostya.', [], ''),
    ('vika', 'Ну, с работы.', 'Well, from work.', [], ''),
    ('max', 'Ладно, садитесь. Садитесь сюда.', 'All right, sit down. Sit here.', [], ''),
    ('max', 'Располагайтесь поудобнее.', 'Make yourself comfortable.', [], ''),
    ('max', 'А я пойду принесу выпить, окей?', 'I will go grab us something to drink, okay?', [], ''),
    ('nastya', 'Мы с Викой вместе работаем.', 'Vika and I work together.', [], ''),
    ('nastya', 'Мы просто коллеги.', 'We are just colleagues.', [], ''),
    ('max', 'Ну что, а вот и веселье.', 'Well, here comes the fun.', [], ''),
    ('max', 'Давайте выпьем!', 'Let us have a drink!', [], ''),
    ('max', 'Давайте за встречу.', "Let's drink to seeing each other.", [], ''),
]
WALK = [
    (0, None, "'Hi! Here we are.' 'Privet' is the casual hello. 'Here and we' is the way to announce yourself on arrival."),
    (1, None, "'Oh, meet Vika.' 'Get acquainted' is the Russian for 'meet', with the 'sya' ending. The little word 'this is' follows."),
    (2, None, "'Actually, we know Victoria.' Nastya uses the full formal name that Vika goes by at work. 'With' gives the name its 'ey' ending."),
    (3, None, "'No, stop. She is just Vika, my girlfriend.' The tripled 'no' is a Russian emphasis. 'Stop' is borrowed, and 'girlfriend' is the same as 'girl'."),
    (4, None, "'Vika, this is just Nastya and Kostya.' The opening 'a' means 'and' and switches the topic. 'Just' appears again, now with an apologetic tone."),
    (5, None, "'Well, from work.' 'From work' is a small word for 'from' plus work with a 'y' ending. Vika sounds a little cold."),
    (6, None, "'All right, sit down. Sit here.' 'Sit' ends in 'sya', so it's 'seat yourselves'. 'Here' means 'to here' because they're moving to the table."),
    (7, None, "'Make yourselves comfortable.' The 'po' in front of 'comfortably' makes it 'a bit more comfortably'. The command itself is the polite plural."),
    (8, None, "'I'll go and get us a drink, okay?' 'I'll go, I'll bring' are two verbs in a row, with no 'and'. 'Okay' is borrowed straight from English."),
    (9, None, "'Vika and I work together.' Russian says 'we with Vika' for 'Vika and I', and the name takes an 'oy' ending after 'with'. It's a common pattern that surprises English speakers."),
    (10, None, "'We are just colleagues.' 'Colleagues' is plural, and the word is borrowed. Though it ends in 'a' in the singular, the word applies to a man or a woman."),
    (11, None, "'Well, here comes the fun.' The opening words are 'and here', which turns up everywhere. The word for 'fun' comes from the word for 'cheerful'."),
    (12, None, "'Let's have a drink!' 'Let's' is made from the polite plural of 'give' plus a 'we' form. That 'we' form of a finished verb is how to say 'let's do it'."),
    (13, None, "'Let's drink to the meeting.' A toast formula, with 'for' standing in for 'to'. Max repeats it to move the evening forward."),
]
