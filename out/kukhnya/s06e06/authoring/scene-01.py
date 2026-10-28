ID = 'kukhnya-s06e06-scene-01'
SHOW = "kukhnya"
SEASON = 6
EPISODE = 6
SCENE = 1
TITLE = 'Приглашение в Париж  (Invitation to Paris)'
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {'narrator': 'sky', 'anya': 'alisa', 'gost': 'anja', 'denis': 'angelina'}
LABELS = {'anya': 'Катя', 'gost': 'Гость', 'denis': 'Денис'}
SOURCE_NAME = "Кухня (Kukhnya) S6.06"
SOURCE_FILE = 'sources/kukhnya/s06/e06.ru.srt'

INTRO = 'Welcome to episode six of Kukhnya season six. Over a romantic dinner, Olivier invites Katya to fly to Paris with him, while Denis and Nikita watch jealously from across the dining room.'

STORY = [
    ('gost', 'Тебе ещё не надоела серая Москва?', 'Are you not tired of gray Moscow yet?', [(1, 'тебе не надоело эта серая Москва')], 'adapted'),
    ('gost', 'Может, поедешь со мной в Париж?', 'Maybe you will go to Paris with me?', [(2, 'Может, со мной в Париж')], 'adapted'),
    ('gost', 'Там мы найдём тебе хорошую работу.', 'There we will find you a good job.', [(3, 'Там, Париж. Найдем тебе работу')], 'adapted'),
    ('gost', 'Или тебя здесь что-то держит?', 'Or is something keeping you here?', [(4, 'Или тебя здесь что-то держат')], 'adapted'),
    ('anya', 'Нет, меня здесь ничего не держит.', 'No, nothing is keeping me here.', [(5, 'Ну, нет')], 'adapted'),
    ('anya', 'А ты случайно не слишком торопишься?', 'Are you not rushing things a bit too much?', [(6, 'А ты не слишком торопишься')], 'adapted'),
    ('gost', 'Я целую тебя впервые за пять лет.', 'I am kissing you for the first time in five years.', [(7, 'Я целую тебя впервые за пять лет знакомства')], 'adapted'),
    ('gost', 'По-моему, я уже жутко опаздываю.', 'In my opinion, I am already terribly late.', [(8, 'По-моему, я жутко опаздываю')], 'adapted'),
    ('anya', 'Слышишь, это сработала пожарная сигнализация.', 'Listen, the fire alarm has gone off.', [(9, 'Это пожарная сигнализация')], 'adapted'),
    ('anya', 'Нам сейчас срочно надо идти на улицу.', 'We urgently need to go outside right now.', [(10, 'Надо идти')], 'adapted'),
    ('denis', 'Прости, пожалуйста, я совсем случайно.', 'Forgive me, please, it was completely accidental.', [(12, 'Прости, пожалуйста')], 'adapted'),
    ('gost', 'Ничего страшного, это просто красное вино.', 'No big deal, it is just red wine.', [(12, 'Ничего, ничего, ничего')], 'adapted'),
]

OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."

WALK = [
    (0, None, "'Are you not tired of gray Moscow yet?' the guest anchors the line on 'to you', while 'gray' completes the thought."),
    (1, None, "'Maybe you will go to Paris with me?' The meaning hinges on 'maybe' working together with 'me' in spoken Russian."),
    (2, None, "'There we will find you a good job.' the guest addresses the listener with the informal singular 'you' alongside 'work'."),
    (3, None, "'Or is something keeping you here?' In Russian, the idea of 'or' flows naturally into 'holds' without extra filler words."),
    (4, None, "'No, nothing is keeping me here.' In Russian, the idea of 'no' flows naturally into 'holds' without extra filler words."),
    (5, None, "'Are you not rushing things a bit too much?' Notice how Russian expresses 'and' and 'to be in a hurry' with crisp inflection rather than helper words. the guest answers right away."),
    (6, None, "'I am kissing you for the first time in five years.' the guest anchors the line on 'I', while 'years' completes the thought."),
    (7, None, "'In my opinion, I am already terribly late.' the guest brings out the contrast between 'in my opinion' and 'I' in a few short words."),
    (8, None, "'Listen, the fire alarm has gone off.' Notice how Russian expresses 'to hear' and 'alarm system' with crisp inflection rather than helper words."),
    (9, None, "'We urgently need to go outside right now.' The grammar packs 'us' and 'street' into a tight, idiomatic kitchen exchange."),
    (10, None, "'Forgive me, please, it was completely accidental.' The meaning hinges on 'forgive' working together with 'by chance' in spoken Russian."),
    (11, None, "'No big deal, it is just red wine.' In Russian, the idea of 'nothing' flows naturally into 'wine' without extra filler words."),
]

TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "Denis's desperate attempt to ruin the date with a fire alarm and spilled wine only brings Katya and Olivier closer together. See you in the next scene."
CLOSING = ('anya', 'Пойдём быстрее на свежий воздух.')
