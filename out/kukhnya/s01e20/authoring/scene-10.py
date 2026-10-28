# Authoring module for kukhnya-s01e20-scene-10.
ID = 'kukhnya-s01e20-scene-10'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 20
SCENE = 10
TITLE = 'Дима ждёт  (Dima is Waiting)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'hostess': 'Хостес'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.20'
SOURCE_FILE = 'sources/kukhnya/s01/e20.ru.dual.srt'
INTRO = "At the start of the day, the hostess finds Chef Barinov and tells him that the restaurant's owner is waiting for him. Barinov wonders what he wants. We'll hear it in Russian first."
OPENER = "Let's go over it one line at a time."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Barinov goes to find out, and asks for coffee to be brought. 'Excited', 'vzvolnovannyy', comes from 'wave', which makes sense. See you next time!"
CLOSING = ('barinov', 'До свидания!')
STORY = [
    ('hostess', 'Здравствуйте.', 'Hello.', [(152, 'Здравствуйте.')], ''),
    ('barinov', 'Доброе утро.', 'Good morning.', [], ''),
    ('hostess', 'Шеф, вас ожидают.', 'Chef, they are waiting for you.', [], ''),
    ('barinov', 'Кто меня ждет?', 'Who is waiting for me?', [], ''),
    ('hostess', 'Дмитрий Владимирович вас ждёт.', 'Dmitry Vladimirovich is waiting for you.', [], ''),
    ('barinov', 'Нагиев здесь?', 'Nagiyev is here?', [], ''),
    ('hostess', 'Да, он за своим столом.', 'Yes, he is at his table.', [], ''),
    ('barinov', 'Что он хочет?', 'What does he want?', [], ''),
    ('hostess', 'Я не знаю.', 'I do not know.', [], ''),
    ('barinov', 'Обычно он сначала звонит.', 'He usually calls first.', [], ''),
    ('hostess', 'Он кажется очень взволнованным.', 'He seems very excited.', [], ''),
    ('barinov', 'Хорошо, я иду.', 'Okay, I am coming.', [], ''),
    ('barinov', 'Принеси ему немного кофе.', 'Bring him some coffee.', [], ''),
]
WALK = [
    (0, None, "'Hello.' The long formal hello, with a silent 'v' at the start. The hostess uses the polite form."),
    (1, None, "'Good morning.' 'Morning' is neuter, so 'good' ends in 'oe'. A short, friendly reply."),
    (2, None, "'Chef, they're waiting for you.' 'You' goes first, as 'vas'. 'They await' has no 'they'."),
    (3, None, "'Who's waiting for me?' 'Who' comes first. 'Waits' ends in 't', for 'he'."),
    (4, None, "'Dmitry Vladimirovich is waiting for you.' She uses his first name and patronymic. 'You' is the polite form."),
    (5, None, "'Is Nagiyev here?' There's no 'is'. The question lives on the rising voice."),
    (6, None, "'Yes, he's at his table.' 'Behind his own table' is how Russian says 'at his table'. 'His own' points back to the owner."),
    (7, None, "'What does he want?' 'He wants' is irregular. 'What' sits at the front."),
    (8, None, "'I don't know.' One of the shortest sentences you can say. 'I know' ends in 'u'."),
    (9, None, "'He usually rings first.' 'Usually' ends in 'o'. 'First' is a single word."),
    (10, None, "'He seems very agitated.' 'Seems' is one word, and 'agitated' comes from 'wave'. It ends in 'ym' because it follows 'seems'."),
    (11, None, "'Okay, I'm coming.' 'I go' is a short word with a 'u' ending. A quick reply."),
    (12, None, "'Bring him some coffee.' 'Bring' is the casual command. 'To him' is 'emu', and coffee never changes."),
]
