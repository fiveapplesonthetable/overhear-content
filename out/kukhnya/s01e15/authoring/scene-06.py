# Authoring module for kukhnya-s01e15-scene-06.
ID = 'kukhnya-s01e15-scene-06'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 15
SCENE = 6
TITLE = 'Трудный разговор  (A Difficult Conversation)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'max': 'Макс', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.15'
SOURCE_FILE = 'sources/kukhnya/s01/e15.ru.dual.srt'
INTRO = "Still in Vika's flat, Max answers her question. He would like to move in, he says, but there is Kostya and the rent to think about. Vika isn't convinced. Hear it in Russian first."
OPENER = 'Their conversation, slowly.'
TRANSITION = 'Here is the conversation again.'
OUTRO = "Max promises to talk to Kostya today. Vika has heard excuses before, and she'll want to know how that talk goes. Speak soon."
CLOSING = ('vika', 'Пока!')
STORY = [
    ('max', 'Понимаешь, я не могу к тебе переехать.', 'You see, I cannot move in with you.', [(32, 'Понимаешь, я не могу к тебе переехать.')], ''),
    ('vika', 'Почему ты не хочешь жить со мной?', 'Why do you not want to live with me?', [], ''),
    ('max', 'Мы с Костей вместе за квартиру платим.', 'Kostya and I pay for the flat together.', [(33, 'Мы с Костей вместе за квартиру платим.')], ''),
    ('vika', 'Это просто глупая отговорка.', 'That is just a silly excuse.', [], ''),
    ('max', 'Один он её не потянет.', 'He cannot afford it on his own.', [(34, 'Один он ее не потянет.')], ''),
    ('vika', 'Макс, если ты не хочешь жить со мной, так и скажи.', 'Max, if you do not want to live with me, just say so.', [(35, 'Макс, если ты не хочешь жить со мной, так и скажи.')], ''),
    ('max', 'Да я хочу. Это Костя не хочет.', 'I do want to. It is Kostya who does not want to.', [(36, 'Да я хочу. Это Костян не хочет.')], 'adapted: Костя for the slangy Костян'),
    ('vika', 'Тогда поговори с ним сегодня.', 'Then talk to him today.', [], ''),
    ('max', 'Я его понимаю. Но я с ним поговорю.', 'I understand him. But I will talk to him.', [(37, 'Я его понимаю. Но я с ним поговорю обязательно.')], 'adapted: обязательно dropped'),
    ('vika', 'Ты обещаешь?', 'Do you promise?', [], ''),
    ('max', 'Обещаю.', 'I promise.', [(38, 'Обещаю.')], ''),
]
WALK = [
    (0, None, ["'You see, I cannot move in with you.' Let us look at the dialogue: ", ('max', 'Понимаешь'), " softens the statement, like 'you see'. ", ('max', 'к'), ('max', 'тебе'), " means 'to you', and when talking about moving it means 'to your place'."]),
    (1, None, ["'Why do you not want to live with me?' Now let's analyze the words: ", ('vika', 'со'), ('vika', 'мной'), " is 'with me'. The usual word for 'with' changes to make it easier to say. ", ('vika', 'жить'), ', to live, follows ', ('vika', 'хочешь'), ' without changing.']),
    (2, None, ["'Kostya and I pay for the flat together.' Russian says ", ('max', 'Мы'), ('max', 'с'), ('max', 'Костей'), ", 'we with Kostya', for 'Kostya and I'. When talking about paying for something, the flat becomes ", ('max', 'за'), ('max', 'квартиру'), '.']),
    (3, None, ["'That is just a silly excuse.' We can consider this part: ", ('vika', 'отговорка'), ' is an excuse, coming from the idea of talking your way out of something. It matches with ', ('vika', 'глупая'), " for 'silly'."]),
    (4, None, ["'He cannot afford it on his own.' Now let's consider the speech: ", ('max', 'не'), ('max', 'потянет'), " usually means 'won't pull', an everyday way to say 'cannot afford'. ", ('max', 'Один'), ', alone, comes first for emphasis.']),
    (5, None, ["'Max, if you do not want to live with me, just say so.' Now let's examine this part: ", ('vika', 'так'), ('vika', 'и'), ('vika', 'скажи'), " is a set phrase for 'then just say it'. ", ('vika', 'если'), " is 'if'."]),
    (6, None, ["'I do want to. It is Kostya who does not want to.' The ", ('max', 'Да'), " here pushes back, like 'but I do'. ", ('max', 'Это'), ('max', 'Костя'), ('max', 'не'), ('max', 'хочет'), " points the finger, meaning 'it is Kostya who does not'."]),
    (7, None, ["'Then talk to him today.' Now we can focus on the sentence: ", ('vika', 'поговори'), ' is a command to have a talk. ', ('vika', 'с'), ('vika', 'ним'), " is 'with him', where 'he' changes to fit after 'with'."]),
    (8, None, ["'I understand him. But I will talk to him.' Let us break down this line: ", ('max', 'его'), " is 'him'. ", ('max', 'поговорю'), " means 'I will have a talk', pointing ahead to the future."]),
    (9, None, ["'Do you promise?' In Russian a statement becomes a question just by rising at the end, without changing word order."]),
    (10, None, ["'I promise.' Let us look at this line: ", ('max', 'Обещаю'), " is one word, and its ending already means 'I', so nobody says the term for 'I'."]),
]
