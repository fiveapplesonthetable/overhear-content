ID = 'kukhnya-s04e15-scene-12'
SHOW = 'kukhnya'
SEASON = 4
EPISODE = 15
SCENE = 12
TITLE = "Допрос в полиции  (Police Interrogation)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = 'ru-en'
VOICES = {"narrator": "sky", "denis": "anja", "inspector": "angelina"}
LABELS = {"denis": "Денис", "inspector": "Инспектор"}
SOURCE_NAME = 'Кухня (Kukhnya) S4.15'
SOURCE_FILE = 'sources/kukhnya/s04/e15.ru.srt'

INTRO = "Inside the police station, Lieutenant Sudnik stares at the packets of white agar-agar powder and refuses to believe Denis's explanation that they are harmless kitchen ingredients. Just as things look bleak, a senior officer enters the room, apologizes for the misunderstanding, and sets Denis free."

STORY = [
    ('denis', 'Послушайте меня, эти порошки абсолютно легальные!', 'Listen to me, these powders are completely legal!', [(174, 'Это все легально. Вы')], 'adapted'),
    ('inspector', 'Вы все на допросе говорите одно и то же!', 'All of you say the exact same thing during interrogation!', [(174, 'Это все легально. Вы')], 'adapted'),
    ('inspector', 'Отвечай честно, как называется этот белый порошок?', 'Answer honestly, what is this white powder called?', [(176, 'Что это?')], 'adapted'),
    ('denis', 'Здесь написано, это обычный кулинарный агар-агар.', 'It is written here, this is ordinary culinary agar-agar.', [(177, 'Агар-агар.')], 'adapted'),
    ('inspector', 'Ого, какая-то очередная новая дрянь появилась!', 'Whoa, some new kind of junk has appeared!', [(178, 'Очередная новая дрянь появилась.')], 'adapted'),
    ('inspector', 'И что вы обычно с этим порошком делаете?', 'And what do you usually do with this powder?', [(179, 'Ну и что вы')], 'adapted'),
    ('denis', 'Я же говорю, мы готовим из него еду!', 'I am telling you, we cook food out of it!', [(180, 'Я же говорю, это')], 'adapted'),
    ('denis', 'Меня на кухне попросили быстро это купить.', 'They asked me in the kitchen to buy this quickly.', [(181, 'Меня попросили купить. Попросили.')], 'adapted'),
    ('denis', 'Так, задержанный гражданин, вы теперь полностью свободны!', 'All right, detained citizen, you are now completely free!', [(184, 'Задержанный, вы свободны.')], 'adapted'),
    ('denis', 'Извините нас, произошло очень глупое недоразумение.', 'Excuse us, a very foolish misunderstanding occurred.', [(186, 'Произошло недоразумение.')], 'adapted'),
    ('denis', 'Правда, вы меня сейчас отпускаете на работу?', 'Really, you are letting me go to work right now?', [(187, 'Спасибо. Как?')], 'adapted'),
    ('denis', 'Спасибо вам огромное, до свидания!', 'Thank you very much, goodbye!', [(189, 'Спасибо еще раз. Я')], 'adapted'),
]

OPENER = "Let's examine the police interrogation and Denis's sudden release."

WALK = [
    (0, None, "'Listen to me, these powders are completely legal!' Denis pairs 'listen' with 'legal' directly, since spoken Russian skips English filler words like 'the', 'a', and 'is'."),
    (1, None, "'All of you say the exact same thing during interrogation!' Notice how Russian puts 'same' and 'speak' together in a short, direct phrase where word endings show how the ideas connect."),
    (2, None, "'Answer honestly, what is this white powder called?' Here the inspector anchors the thought on 'answer' and finishes on 'powder', keeping the spoken rhythm brisk and natural."),
    (3, None, "'It is written here, this is ordinary culinary agar-agar.' Denis names the seaweed gelatin used in molecular cuisine."),
    (4, None, "'Whoa, some new kind of junk has appeared!' Unfamiliar with haute cuisine, the officer assumes it is a new street drug."),
    (5, None, "'And what do you usually do with this powder?' Notice how Russian puts 'usual' and 'are doing' together in a short, direct phrase where word endings show how the ideas connect."),
    (6, None, "'I am telling you, we cook food out of it!' Here Denis anchors the thought on 'speak' and finishes on 'food', keeping the spoken rhythm brisk and natural."),
    (7, None, "'They asked me in the kitchen to buy this quickly.' In everyday Russian, 'kitchen' flows straight into 'to buy' without extra linking words."),
    (8, None, "'All right, detained citizen, you are now completely free!' A senior detective walks in and orders Denis released using a plural short adjective."),
    (9, None, "'Excuse us, a very foolish misunderstanding occurred.' The neuter past verb agrees with the neuter noun meaning misunderstanding."),
    (10, None, "'Really, you are letting me go to work right now?' Denis can hardly believe his good fortune."),
    (11, None, "'Thank you very much, goodbye!' Denis grabs his bag of powders and bolts out the door."),
]

TRANSITION = "Now let's hear the complete police station scene again at full speed."
OUTRO = 'Thrilled to have his molecular powders back, Denis races back to Claude Monet—unaware that the police just let him go so they could follow him to his boss. See you next time!'
CLOSING = ("denis", "До завтра!")
