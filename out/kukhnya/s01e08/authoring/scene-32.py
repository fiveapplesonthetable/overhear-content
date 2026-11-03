# Authoring module for kukhnya-s01e08-scene-32.
ID = 'kukhnya-s01e08-scene-32'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 8
SCENE = 32
TITLE = 'Весь мир против нас  (The Whole World Against Us)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.08'
SOURCE_FILE = 'sources/kukhnya/s01/e08.ru.dual.srt'
INTRO = "Barinov is in his office at Claude Monet again, and now he suspects everyone of plotting against him. Max, the young cook, is there too, and he reflects on why some people feel the whole world is against them. Here it is in Russian first."
OPENER = "Let's go through the paranoia. Barinov accuses, and Max calmly disagrees."
TRANSITION = "Now the scene in one go."
OUTRO = "Max's 'yes, Chef' — literally 'I am listening, Chef' — is the line to keep: it's how a Russian kitchen, or the military, answers 'right away'. See you next time."
CLOSING = ('max', 'Пока!')
STORY = [
    ('barinov', 'Кругом одни предатели и шпионы!', 'Traitors and spies are all around!', [], ''),
    ('max', 'Шеф, никто против вас не замышляет зла.', 'Chef, nobody is plotting evil against you.', [], ''),
    ('barinov', 'Ты ничего не понимаешь в людях, огузок!', 'You understand nothing about people, runt!', [], ''),
    ('max', 'Люди часто сами создают себе проблемы.', 'People often create problems for themselves.', [], ''),
    ('max', 'Третьи ошибочно думают, что весь мир против них.', 'Others mistakenly think the whole world is against them.', [(362, 'Третьи ошибочно думают, что весь мир настроен против них.')], ''),
    ('barinov', 'Они просто завидуют моему великому таланту!', 'They are simply jealous of my great talent!', [], ''),
    ('max', 'Но постоянные подозрения только портят жизнь.', 'But constant suspicions only ruin life.', [], ''),
    ('barinov', 'Осторожность на кухне никогда не бывает лишней.', 'Caution in the kitchen is never unnecessary.', [], ''),
    ('max', 'Иногда полезно просто доверять своим поварам.', 'Sometimes it is useful to simply trust your cooks.', [], ''),
    ('barinov', 'Я доверяю только своей родной сковородке.', 'I trust only my own frying pan.', [], ''),
    ('max', 'С таким настроением трудно радоваться жизни.', 'With such a mood it is hard to enjoy life.', [], ''),
    ('barinov', 'Хватит читать мне лекции, иди нарезать лук!', 'Enough lecturing me, go chop onions!', [], ''),
    ('max', 'Слушаюсь, шеф, уже бегу на кухню.', 'Right away, chef, I am already running to the kitchen.', [], ''),
    ('max', 'Страх мешает людям видеть правду вокруг.', 'Fear prevents people from seeing the truth around them.', [], ''),
]
WALK = [
    (0, None, ["'Traitors and spies are all around!' The expression ", ('barinov', 'предатели'), ' simply means traitors in this context.']),
    (1, None, ["'Chef, nobody is plotting evil against you.' When plotting something bad, you use ", ('max', 'замышляет'), ' to express that evil intent.']),
    (2, None, ["'You understand nothing about people, runt!' The head chef throws the insult ", ('barinov', 'огузок'), ' at his young cook, which originally refers to a cut of beef.']),
    (3, None, ["'People often create problems for themselves.' To talk about making or creating, ", ('max', 'создают'), ' captures the idea of bringing something into existence.']),
    (4, None, ["'Others mistakenly think the whole world is against them.' If something is done by mistake, ", ('max', 'ошибочно'), ' captures that incorrect assumption perfectly.']),
    (5, None, ["'They are simply jealous of my great talent!' Feeling jealous of someone else brings ", ('barinov', 'завидуют'), ' into the conversation as they express envy.']),
    (6, None, ["'But constant suspicions only ruin life.' Having constant doubts and mistrust makes ", ('max', 'подозрения'), ' fit perfectly for these suspicions.']),
    (7, None, ["'Caution in the kitchen is never unnecessary.' Being careful is important, which is why ", ('barinov', 'Осторожность'), ' is mentioned as a necessary trait.']),
    (8, None, ["'Sometimes it is useful to simply trust your cooks.' It is highly beneficial to just ", ('max', 'доверять'), ' the people working for you in the kitchen.']),
    (9, None, ["'I trust only my own frying pan.' The older chef is attached to his ", ('barinov', 'сковородке'), ', relying heavily on that frying pan.']),
    (10, None, ["'With such a mood it is hard to enjoy life.' A bad mood is described with ", ('max', 'настроением'), ' when things feel rather gloomy.']),
    (11, None, ["'Enough lecturing me, go chop onions!' We can hear the direct order to ", ('barinov', 'нарезать'), ' all the onions for the dish.']),
    (12, None, ["'Right away, chef, I am already running to the kitchen.' Saying yes and acknowledging orders uses ", ('max', 'Слушаюсь'), ' in a somewhat military fashion.']),
    (13, None, ["'Fear prevents people from seeing the truth around them.' Obstacles blocking the view are what ", ('max', 'мешает'), ' describes as it prevents seeing the truth.']),
]
