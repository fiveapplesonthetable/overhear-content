# Authoring module for kukhnya-s01e19-scene-17.
ID = 'kukhnya-s01e19-scene-17'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 19
SCENE = 17
TITLE = 'Моя девушка  (My Girlfriend)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kristina': 'Кристина', 'max': 'Макс', 'nagiyev': 'Нагиев'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.19'
SOURCE_FILE = 'sources/kukhnya/s01/e19.ru.dual.srt'
INTRO = "Kristina has come home early from Monaco, and she isn't happy. She marches into the restaurant and demands to know who a certain woman is. Max steps in with a surprising claim. We'll hear it in Russian first."
OPENER = "Let's replay it a line at a time."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Max has made a very public claim about Vika, and the owner and his wife head off for a holiday. As you listen again, notice 'izvinit'sya': in Russian you apologise by 'excusing yourself'. See you next time!"
CLOSING = ('nagiyev', 'До свидания!')
STORY = [
    ('nagiyev', 'Что ты здесь делаешь?', 'What are you doing here?', [(354, 'ты что здесь делаешь')], ''),
    ('nagiyev', 'Ты должна быть в Монако!', 'You are supposed to be in Monaco!', [(355, 'Ты в Монако должна')], ''),
    ('kristina', 'А я вернулась!', 'But I came back!', [(356, 'А я вернулась')], ''),
    ('kristina', 'Ты отправил меня туда специально.', 'You sent me there on purpose.', [(356, 'Ты мне специально туда отправил')], ''),
    ('kristina', 'Кто эта женщина, Дима?', 'Who is this woman, Dima?', [], ''),
    ('nagiyev', 'Я ничего не знаю.', "I don't know anything.", [], ''),
    ('kristina', 'Мне Саша все сказала.', 'Sasha told me everything.', [(359, 'Мне Саша сказала')], ''),
    ('kristina', 'Она тут работает и все видит.', 'She works here and sees everything.', [(359, 'она тут все видит, она тут работает')], ''),
    ('max', 'Можно я скажу?', 'Can I say something?', [(361, 'Можно я скажу')], ''),
    ('max', 'Виктория Сергеевна — моя девушка.', 'Victoria Sergeyevna is my girlfriend.', [(362, 'Виктория Сергеевна, моя девушка')], ''),
    ('max', 'У нас с ней серьезные отношения.', 'We have a serious relationship.', [(362, 'и у нас с ней серьезные отношения')], ''),
    ('max', 'Пусть ваша жена извинится перед моей девушкой!', 'Let your wife apologize to my girlfriend!', [(370, 'чтобы ваша же жена попросила прощения у моей девушки')], ''),
    ('nagiyev', 'Пойдем домой, моя родная.', "Let's go home, my dear.", [(367, 'Пойдем, моя родная, домой')], ''),
    ('nagiyev', 'Завтра полетим отдыхать, хорошо?', 'Tomorrow we will fly to rest, okay?', [(368, 'в Анага полетим')], ''),
]
WALK = [
    (0, None, "'What are you doing here?' The casual 'you' gives 'esh'. 'What' goes first."),
    (1, None, "'You're supposed to be in Monaco!' 'Must' ends in 'a' because Kristina is a woman. 'In Monaco' leaves 'Monaco' unchanged."),
    (2, None, "'But I came back!' 'Came back' ends in 'las', for a woman. The opening 'a' means 'but'."),
    (3, None, "'You sent me there on purpose.' 'Sent' ends in 'l' for the masculine speaker. 'On purpose' is a single word."),
    (4, None, "'Who is this woman?' 'This' ends in 'a' to match the feminine noun. There's no 'is'."),
    (5, None, "'I don't know anything.' 'Nothing' and 'not' are both there. 'I know' ends in 'u'."),
    (6, None, "'Sasha told me everything.' 'To me' comes first for emphasis. 'Told' ends in 'a' for a woman."),
    (7, None, "'She works here and sees everything.' 'Works' and 'sees' both end in 't' for 'she'. 'Everything' is the object of the second."),
    (8, None, "'May I say something?' The pattern is 'possible I will say'. 'Say' is a finished action."),
    (9, None, "'Viktoria Sergeyevna is my girlfriend.' The dash takes the place of 'is'. 'My girlfriend' is feminine."),
    (10, None, "'We have a serious relationship.' 'At us with her' is a Russian way of saying 'between us'. 'Relationship' is plural."),
    (11, None, "'Let your wife apologise to my girlfriend!' 'Apologise' means 'excuse oneself', which is why it ends in 'sya'. 'Before' is the small word used here for 'to'."),
    (12, None, "'Let's go home, my dear.' 'Let's go' is the 'we' form of going on foot. 'Dear' is a word that means 'own' or 'native'."),
    (13, None, "'Tomorrow we'll fly off to rest, okay?' 'We'll fly' is the 'we' form of the word for flying. 'Okay?' is a rising word, 'khorosho'."),
]
