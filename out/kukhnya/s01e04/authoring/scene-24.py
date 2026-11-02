# Authoring module for kukhnya-s01e04-scene-24.
ID = 'kukhnya-s01e04-scene-24'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 4
SCENE = 24
TITLE = 'Шанс остаться  (A Chance to Stay)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'max': 'Макс', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.04'
SOURCE_FILE = 'sources/kukhnya/s01/e04.ru.dual.srt'
INTRO = "Outside the restaurant, Vika catches up with Max as he is about to leave for good. She tells him she has spoken to the chef, and that he can stay. Here's the Russian first."
OPENER = 'Now the good news.'
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Max has a second chance and Vika gets the last word. If you take one thing from this scene, notice how she uses the words for 'while' and 'not' around the action word to mean 'before'."
CLOSING = ('max', 'Пока!')
STORY = [
    ('vika', 'Макс, подожди минуту!', 'Max, wait a minute!', [(331, 'Макс!')], ''),
    ('max', 'Вика? Что случилось?', 'Vika? What happened?', [], ''),
    ('vika', 'Ты никуда не уходишь.', 'You are not leaving anywhere.', [], ''),
    ('max', 'Но шеф только что меня уволил.', 'But the chef just fired me.', [], ''),
    ('vika', 'Я поговорила с шефом.', 'I spoke with the chef.', [], ''),
    ('max', 'И что он тебе сказал?', 'And what did he tell you?', [], ''),
    ('vika', 'Он разрешил тебе остаться на кухне.', 'He allowed you to stay in the kitchen.', [], ''),
    ('max', 'Правда? Ты меня спасла!', 'Really? You saved me!', [], ''),
    ('vika', 'Только больше не совершай глупых ошибок.', 'Just do not make stupid mistakes anymore.', [], ''),
    ('max', 'Обещаю, я буду работать очень старательно.', 'I promise, I will work very diligently.', [], ''),
    ('vika', 'Возвращайся на свое рабочее место.', 'Return to your work station.', [], ''),
    ('max', 'Спасибо огромное за твою помощь, Вика!', 'Thank you very much for your help, Vika!', [], ''),
    ('vika', 'Иди, пока шеф не передумал.', 'Go, before the chef changes his mind.', [], ''),
    ('max', 'У меня появился второй шанс!', 'I got a second chance!', [], ''),
]
WALK = [
    (0, None, [
        "'Max, wait a minute!' The term for the familiar 'wait' is ",
        ('vika', 'подожди'),
        " The word for 'minute', ",
        ('vika', 'минуту!'),
        " ends in an 'oo' sound to show a length of time."
    ]),
    (1, None, [
        "'Vika? What happened?' The phrase that translates to 'what has happened' is ",
        ('max', 'Что случилось?')
    ]),
    (2, None, [
        "'You are not leaving anywhere.' The action word for 'you are leaving' is ",
        ('vika', 'уходишь.'),
        " Notice that she says ",
        ('vika', 'никуда не'),
        " which literally translates to 'nowhere not'."
    ]),
    (3, None, [
        "'But the chef just fired me.' The phrase for 'just now' is ",
        ('max', 'только что'),
        " which literally translates to 'only what'. The term for 'fired', ",
        ('max', 'уволил.'),
        " ends in an 'L' sound because the chef is a man."
    ]),
    (4, None, [
        "'I spoke with the chef.' The Russian term for 'spoke', ",
        ('vika', 'поговорила'),
        " is built from a prefix for 'talk' and ends with an 'ah' sound because Vika is a woman. The phrase for 'with the chef' is ",
        ('vika', 'с шефом.')
    ]),
    (5, None, [
        "'And what did he tell you?' The Russian expression for 'to you' is ",
        ('max', 'тебе'),
        " He says ",
        ('max', 'тебе сказал?'),
        " which translates to 'to you said'."
    ]),
    (6, None, [
        "'He allowed you to stay in the kitchen.' The word for 'allowed', ",
        ('vika', 'разрешил'),
        " is built from the same root as the term for 'permission'. The phrase ",
        ('vika', 'тебе остаться'),
        " translates to 'to you to stay'."
    ]),
    (7, None, [
        "'Really? You saved me!' The word for 'saved', ",
        ('max', 'спасла!'),
        " ends in an 'ah' sound because it refers to Vika. The term for 'really' is ",
        ('max', 'Правда?')
    ]),
    (8, None, [
        "'Just do not make stupid mistakes anymore.' The action word for 'commit' is ",
        ('vika', 'совершай'),
        " The Russian expression for 'mistakes' is ",
        ('vika', 'ошибок.'),
        " The phrase ",
        ('vika', 'больше не'),
        " translates to 'anymore not'."
    ]),
    (9, None, [
        "'I promise, I will work very diligently.' The phrase for 'diligently', ",
        ('max', 'старательно.'),
        " is built from an action word meaning 'to try hard'. The phrase ",
        ('max', 'буду работать'),
        " translates to 'I will work'."
    ]),
    (10, None, [
        "'Return to your work station.' The Russian expression for 'return' is ",
        ('vika', 'Возвращайся'),
        " The phrase ",
        ('vika', 'рабочее место.'),
        " literally translates to 'working place'."
    ]),
    (11, None, [
        "'Thank you very much for your help, Vika!' The phrase ",
        ('max', 'Спасибо огромное'),
        " translates to 'huge thanks'. The naming word for 'help', ",
        ('max', 'помощь,'),
        " is related to the action word for 'to help'."
    ]),
    (12, None, [
        "'Go, before the chef changes his mind.' The words ",
        ('vika', 'пока шеф'),
        " and ",
        ('vika', 'не'),
        " surround the action word to mean 'before'. The Russian expression for 'changes his mind', ",
        ('vika', 'передумал.'),
        " is built from a prefix meaning 're' and the action word for 'thought'."
    ]),
    (13, None, [
        "'I got a second chance!' The phrase ",
        ('max', 'У меня появился'),
        " literally translates to 'at me appeared', which is how you express getting something new. The phrase for 'second chance' is ",
        ('max', 'второй шанс!')
    ]),
]
