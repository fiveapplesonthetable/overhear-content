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
INTRO = "The owner's wife, Kristina, has flown home early, and she storms into the restaurant demanding to know who a certain woman is. Listen in Russian first; the anger carries it."
OPENER = 'Now the showdown, line by line.'
TRANSITION = "And here's the showdown in full."
OUTRO = 'Max called Vika his girlfriend in front of everyone, and you followed along. See you next time!'
CLOSING = ('nagiyev', 'Всего хорошего!')
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
    (0, None, "'What are you doing here?' \"Delaesh'\", 'you do', is for someone you call \"ty\", here his wife. The owner sounds more scared than pleased."),
    (1, None, "'You're supposed to be in Monaco!' \"Dolzhna\", 'must', ends in -a because he's talking to a woman. To a man it's \"dolzhen\"."),
    (2, None, "'But I came back!' \"Vernulas'\", 'came back', ends in -las' for a woman; a man says \"vernulsya\". The opening a means 'but'."),
    (3, None, "'You sent me there on purpose.' \"Spetsial'no\", 'specially', is how Russians say 'on purpose'. \"Tuda\", 'there', is where she was sent."),
    (4, None, "'Who is this woman?' \"Eta\", 'this', matches \"zhenshchina\", 'woman'; a man is \"etot\". \"Kto eta zhenshchina\" has no 'is' at all."),
    (5, None, "'I don't know anything.' \"Ya nichego ne znayu\" needs both \"nichego\" and ne: 'I nothing not know'. Two negatives are normal in Russian."),
    (6, None, "'A colleague told me everything.' \"Mne\", 'to me', comes first for weight. \"Skazala\", 'told', points to a woman as the one who told her."),
    (7, None, "'She works here and sees everything.' \"Rabotaet\" and \"vidit\" both end in -t, the ending for 'he' or 'she'. \"Tut\" is a casual 'here'."),
    (8, None, "'May I say something?' \"Mozhno ya skazhu\", 'allowed I'll say', asks for the floor. It's short and polite."),
    (9, None, "'Viktoria Sergeyevna is my girlfriend.' In writing a dash stands where English has 'is'. \"Moya devushka\", 'my girlfriend', is literally 'my girl'."),
    (10, None, "'We have a serious relationship.' \"U nas s ney\", 'at us with her', is 'she and I have'. It's the same pattern as Vika's \"u nas s toboy\", now in Max's mouth."),
    (11, None, "'Let your wife apologize to my girlfriend!' \"Pust'\", 'let', puts a demand on someone else. \"Izvinitsya\", 'apologize', is literally 'excuse oneself', hence the -sya."),
    (12, None, "'Let's go home, my dear.' \"Rodnaya\", 'dear', literally means 'my own, kin'. You heard \"rodnoy\" for a waiter at the start of the episode."),
    (13, None, "'Tomorrow we'll fly off to rest, okay?' \"Poletim\", 'we'll fly', comes from \"letet'\". \"Otdykhat'\", 'to rest', also covers going on holiday."),
]
