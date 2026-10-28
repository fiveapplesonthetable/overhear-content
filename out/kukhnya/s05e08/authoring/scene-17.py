ID = 'kukhnya-s05e08-scene-17'
SHOW = "kukhnya"
SEASON = 5
EPISODE = 8
SCENE = 17
TITLE = "Обман переводчика  (The Interpreter's Deception)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {'narrator': 'sky', 'anya': 'alisa', 'gost': 'anja', 'nastya': 'angelina'}
LABELS = {'anya': 'Костя', 'gost': 'Гость', 'nastya': 'Настя'}
SOURCE_NAME = "Кухня (Kukhnya) S5.08"
SOURCE_FILE = 'sources/kukhnya/s05/e08.ru.srt'

INTRO = "Convinced that Nastya is with the sheikh, Kostya barges into an upstairs suite with Max, Senya, and Fedya—only to find the sheikh's interpreter in a robe with waitress Alisa, who thought she was meeting the sheikh."

STORY = [
    ('anya', 'Где Настя?', 'Where is Nastya?', [(181, 'Где Настя')], 'adapted'),
    ('gost', 'Я не знаю.', 'I do not know.', [(181, 'Я не знаю')], 'adapted'),
    ('anya', 'Ты Настя?', 'Are you Nastya?', [(182, 'Ты Настя')], 'adapted'),
    ('nastya', 'Нет, я Алиса.', 'No, I am Alisa.', [(182, 'Я Алиса')], 'adapted'),
    ('gost', 'А что вообще такое?', 'And what is going on anyway?', [(183, 'А что такое')], 'adapted'),
    ('gost', 'Официантки идут к шейху, а попадают ко мне.', 'The waitresses go to see the sheikh, and end up with me.', [(185, 'Официантки идут к шейху, попадают ко мне')], 'adapted'),
    ('nastya', 'То есть с шейхом ты меня не познакомишь?', 'So you are not going to introduce me to the sheikh?', [(186, 'То есть с шейхом ты меня не познакомишь')], 'adapted'),
    ('anya', 'То есть Насти у вас не было, так?', 'So Nastya was not here with you, right?', [(187, 'у вас не было, так')], 'adapted'),
    ('gost', 'Нет, она мне отказала.', 'No, she turned me down.', [(188, 'Нет, она мне отказала')], 'adapted'),
    ('anya', 'Значит, Настя мне не изменяла!', 'That means Nastya did not cheat on me!', [(188, 'она мне отказала')], 'adapted'),
    ('nastya', 'Как ты мог меня так обмануть?', 'How could you deceive me like that?', [(186, 'ты меня не познакомишь')], 'adapted'),
    ('gost', 'Тише, сюда идёт сам шейх!', 'Quiet, the sheikh himself is coming this way!', [(185, 'к шейху')], 'adapted'),
]

OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."

WALK = [
    (0, None, "'Where is Nastya?' In Russian, the idea of 'where' flows naturally into 'Nastya' without extra filler words."),
    (1, None, "'I do not know.' Spoken Russian keeps this brisk, leaning on 'I' and finishing on 'know'. Kostya answers right away."),
    (2, None, "'Are you Nastya?' Here the Russian phrasing highlights 'you' before landing on 'Nastya'."),
    (3, None, "'No, I am Alisa.' In Russian, the idea of 'no' flows naturally into 'Alisa' without extra filler words."),
    (4, None, "'And what is going on anyway?' Notice how Russian expresses 'and' and 'such' with crisp inflection rather than helper words."),
    (5, None, "'The waitresses go to see the sheikh, and end up with me.' Notice how Russian expresses 'waitresses' and 'to me' with crisp inflection rather than helper words."),
    (6, None, "'So you are not going to introduce me to the sheikh?' The negative particle sits right before the verb meaning 'there is' to negate the statement."),
    (7, None, "'So Nastya was not here with you, right?' The negative particle sits right before the verb meaning 'there is' to negate the statement. the guest answers right away."),
    (8, None, "'No, she turned me down.' the guest brings out the contrast between 'no' and 'she' in a few short words."),
    (9, None, "'That means Nastya did not cheat on me!' Kostya anchors the line on 'so', while 'to cheat' completes the thought."),
    (10, None, "'How could you deceive me like that?' Here the Russian phrasing highlights 'how' before landing on 'to deceive'. the guest answers right away."),
    (11, None, "'Quiet, the sheikh himself is coming this way!' the guest anchors the line on 'quieter', while 'sheikh' completes the thought."),
]

TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'Just as Alisa starts hitting the lying interpreter, the sheikh himself walks into the room demanding to know what is happening. See you in the next scene.'
CLOSING = ('anya', 'Настя сказала мне чистую правду!')
