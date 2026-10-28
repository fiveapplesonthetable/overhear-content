# Authoring module for kukhnya-s01e16-scene-06.
ID = 'kukhnya-s01e16-scene-06'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 16
SCENE = 6
TITLE = 'Звонок в инспекцию  (Call to the Inspection)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'senya': 'Сеня'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.16'
SOURCE_FILE = 'sources/kukhnya/s01/e16.ru.dual.srt'
INTRO = 'In the kitchen of Claude Monet, Chef Viktor stands by the window with a triumphant grin. Senya notices his cheerful mood and asks what is going on. Viktor points to the courtyard, where migration inspectors are descending upon Arcobaleno. Let us listen to their conversation in Russian first.'
OPENER = "Now let us examine Viktor and Senya's conversation at the window line by line."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Satisfied with his successful revenge on Elena Pavlovna, Viktor watches happily as the migration raid throws the rival restaurant into complete disarray. Next time you watch the episode, listen for the Russian expressions for 'why' and 'cheerfully' — you will catch every word right away. See you next time!"
CLOSING = ('senya', 'Пока!')
STORY = [
    ('senya', 'Шеф, почему вы так весело улыбаетесь?', 'Chef, why are you smiling so cheerfully?', [], ''),
    ('barinov', 'Посмотри во двор на соседний ресторан.', 'Look into the courtyard at the neighboring restaurant.', [], ''),
    ('senya', 'Туда только что приехала строгая проверка!', 'A strict inspection just arrived over there!', [], ''),
    ('barinov', 'Да, это специальная служба пришла туда.', 'Yes, that is a special service arriving.', [], ''),
    ('senya', 'Вы сами позвонили в эту инспекцию?', 'Did you call this inspection yourself?', [], ''),
    ('barinov', 'Конечно, они должны уважать правила порядка.', 'Of course, they must respect the rules of order.', [], ''),
    ('senya', 'Теперь их повара будут сильно бегать.', 'Now their cooks will be running around a lot.', [], ''),
    ('barinov', 'Пусть они быстро бегают вокруг здания!', 'Let them quickly run around the building!', [(51, 'Сейчас вы побегаете.')], ''),
    ('senya', 'Елена Павловна будет очень сильно злиться.', 'Elena Pavlovna will be extremely furious.', [], ''),
    ('barinov', 'Она не должна была ставить машину здесь.', 'She should not have parked her car here.', [], ''),
    ('senya', 'Это действительно очень жестокая маленькая месть.', 'This is indeed very cruel little revenge.', [], ''),
    ('barinov', 'Это справедливый урок для наглых соседей.', 'This is a fair lesson for insolent neighbors.', [], ''),
    ('senya', 'Тогда давайте спокойно смотреть в окно!', 'Then let us calmly watch out the window!', [], ''),
]
WALK = [
    (0, None, "'Chef, why are you smiling so cheerfully?' Senya wonders aloud why his boss is looking so visibly happy today."),
    (1, None, "'Look into the courtyard at the neighboring restaurant.' Pointing outside, the chef tells his colleague to observe the place next door."),
    (2, None, "'A strict inspection just arrived over there!' Noticing the commotion, the cook points out that a serious checkup is happening across the way."),
    (3, None, "'Yes, that is a special service arriving.' Confirming the observation, the boss mentions that a specific government agency has shown up."),
    (4, None, "'Did you call this inspection yourself?' Senya puts two and two together, asking if his boss is the one who made the phone call."),
    (5, None, "'Of course, they must respect the rules of order.' Barinov casually admits to it, suggesting that people need to learn how to follow the rules."),
    (6, None, "'Now their cooks will be running around a lot.' The cook pictures the chaos, imagining how frantic the kitchen staff over there must be."),
    (7, None, "'Let them quickly run around the building!' Laughing it off, the chef seems to enjoy the thought of his rivals scrambling in a panic."),
    (8, None, "'Elena Pavlovna will be extremely furious.' Thinking of the neighboring boss, the cook predicts she will be absolutely livid."),
    (9, None, "'She should not have parked her car here.' Brushing off the concern, the chef simply says she brought it on herself by parking poorly."),
    (10, None, "'This is indeed very cruel little revenge.' Senya notes that this payback is a bit harsh, though he seems amused by it."),
    (11, None, "'This is a fair lesson for insolent neighbors.' Standing by his actions, the boss insists it is a fitting punishment for their arrogant behavior."),
    (12, None, "'Then let us calmly watch out the window!' Relaxing into the moment, the cook suggests they just sit back and enjoy the show."),
]
