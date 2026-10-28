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
INTRO = 'The hostess spots Chef Viktor and delivers an important message from a celebrity, and we will listen to them in Russian first; do not worry about catching every single word.'
OPENER = "Now let's go back through the exchange around Dima is Waiting line by line and unpack how the Russian works."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "The chef heads out to the dining room to see what the celebrity wants. Next time you watch the episode, listen for the Russian expressions for 'kind' and 'morning' — you will catch every word right away. See you next time!"
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('hostess', 'Здравствуйте.', 'Hello.', [(152, 'Здравствуйте.')], ''),
    ('barinov', 'Доброе утро.', 'Good morning.', [], ''),
    ('hostess', 'Шеф, вас ожидают.', 'Chef, they are waiting for you.', [], ''),
    ('barinov', 'Кто меня ждет?', 'Who is waiting for me?', [], ''),
    ('hostess', 'Дима тебя ждет.', 'Dima is waiting for you.', [], ''),
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
    (0, None, "'Hello.' Hostess offers a standard greeting to the chef."),
    (1, None, "'Good morning.' Barinov replies with a standard morning greeting."),
    (2, None, "'Chef, they are waiting for you.' Stopping the chef by the kitchen doors, the hostess politely informs him that someone is waiting for him."),
    (3, None, "'Who is waiting for me?' Barinov demands to know exactly who is looking for him."),
    (4, None, "'Dima is waiting for you.' She clarifies that restaurant owner Dmitry Nagiyev is asking for him in the dining room."),
    (5, None, "'Nagiyev is here?' Barinov reacts with surprise that the owner is on the premises."),
    (6, None, "'Yes, he is at his table.' Pointing toward the hall, she confirms that Nagiyev is sitting at his usual corner table."),
    (7, None, "'What does he want?' Barinov questions the owner's motives for showing up unannounced."),
    (8, None, "'I do not know.' When Viktor asks what the boss wants, the hostess shrugs and admits she has no idea."),
    (9, None, "'He usually calls first.' Barinov points out this breaks Nagiyev's usual habit of calling ahead."),
    (10, None, "'He seems very excited.' Hostess notes that the owner appears quite worked up today."),
    (11, None, "'Okay, I am coming.' Barinov resigns himself to the meeting and says he will go."),
    (12, None, "'Bring him some coffee.' Barinov barks an order for coffee to placate the boss."),
]
