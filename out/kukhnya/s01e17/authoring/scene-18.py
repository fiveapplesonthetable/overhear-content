ID = "kukhnya-s01e17-scene-18"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 17
SCENE = 18
TITLE = "Ты труп  (You are a corpse)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Кухня (Kukhnya) S1.17"
SOURCE_FILE = "sources/kukhnya/s01/e17.ru.dual.srt"
VOICES = {'narrator': 'sky', 'anya': 'alisa', 'senya': 'anja'}
LABELS = {'anya': 'Viktor', 'senya': 'Senya'}

INTRO = 'Viktor confronts Senya in the kitchen about the stolen recipe. We will hear it in Russian first, do not worry about catching every word.'
OPENER = "Let's walk through it. Viktor is furious."
TRANSITION = "Now let's hear the scene once more."
OUTRO = 'Senya is in big trouble. See you next time.'

STORY = [
    ('anya', 'Ты был там?', 'Were you there?', [(290, 'Ты что, был там в Аркабалена?')], 'Simplified'),
    ('senya', 'Нет, конечно.', 'No, of course not.', [(291, 'Нет, конечно.')], ''),
    ('anya', 'Рулеты из телятины с ветчиной.', 'Veal rolls with ham.', [(292, 'Песные рулеты из телятины с тонкими ломтиками ветчины.')], 'Simplified'),
    ('senya', 'Я не понимаю.', 'I do not understand.', [], ''),
    ('anya', 'Ты украл мой рецепт.', 'You stole my recipe.', [], ''),
    ('senya', 'Я ничего не брал.', 'I took nothing.', [], ''),
    ('anya', 'Ну, Сеня, ты труп.', 'Well, Senya, you are a corpse.', [(293, 'Ну, Сеня, ты трупа.')], 'Simplified'),
    ('senya', 'Шеф, это не я!', 'Chef, it is not me!', [], ''),
    ('anya', 'Кто тогда?', 'Who then?', [], ''),
    ('senya', 'Может быть, Федя.', 'Maybe Fedya.', [], ''),
    ('anya', 'Я тебе не верю.', 'I do not believe you.', [], ''),
    ('senya', 'Честное слово!', 'Honest word!', [], ''),
]

WALK = [
    (0, None, "'Were you there?' Viktor interrogates his cook."),
    (1, None, "'No, of course not.' Senya quickly denies everything."),
    (2, None, "'Veal rolls with ham.' Viktor reads the exact dish name."),
    (3, None, "'I do not understand.' Senya pretends not to know what he means."),
    (4, None, "'You stole my recipe.' The chef accuses him of espionage."),
    (5, None, "'I took nothing.' He defends his innocence."),
    (6, None, "'Well, Senya, you are a corpse.' Viktor threatens him with dire consequences."),
    (7, None, "'Chef, it is not me!' The cook pleads with his boss."),
    (8, None, "'Who then?' Viktor demands a name."),
    (9, None, "'Maybe Fedya.' He tries to pass the blame to his friend."),
    (10, None, "'I do not believe you.' The chef refuses to buy his story."),
    (11, None, "'Honest word!' He swears he is telling the truth."),
]

CLOSING = ('anya', 'Это конец.')
