# Authoring module for kukhnya-s01e05-scene-21.
ID = 'kukhnya-s01e05-scene-21'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 5
SCENE = 21
TITLE = 'Запара в голове  (Rush in the Head)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'fedya': 'Федя', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.05'
SOURCE_FILE = 'sources/kukhnya/s01/e05.ru.dual.srt'
INTRO = "Still in the Claude Monet kitchen, Max is drowning in orders, and Fedya, who was teasing him a minute ago, steps over to his station. What he teaches isn't a cooking trick. It's a rule about panic. Listen in Russian first."
OPENER = "Let's take it slowly. Fedya talks like a coach."
TRANSITION = 'Now let it flow, breath and all.'
OUTRO = "Fedya's rule, that the rush is only in your head, works in an office as well as in a kitchen. A breath in and a breath out will help too."
CLOSING = ('fedya', 'Пока!')
STORY = [
    ('fedya', 'Ладно, новичок, отойди немного в сторону.', 'Alright, newcomer, step aside a little.', [(306, 'Ладно')], ""),
    ('fedya', 'Подвинься давай, я помогу тебе.', 'Move over, come on, I will help you.', [(307, 'Подвинься давай.')], ""),
    ('max', 'Федя, спасибо, у меня ничего не получается!', 'Fedya, thank you, nothing is working out for me!', [], ""),
    ('fedya', 'Сейчас главное — полностью успокоиться.', 'Right now the main thing is to completely calm down.', [(308, 'Нужно расслабиться.')], ""),
    ('fedya', 'Сделай глубокий вдох.', 'Take a deep breath.', [(308, 'Вдох.')], ""),
    ('fedya', 'А теперь медленный выдох.', 'And now a slow exhale.', [(309, 'Выдох.')], ""),
    ('fedya', 'И навсегда запомни главное правило.', 'And forever remember the main rule.', [(310, 'И запомнить.')], ""),
    ('fedya', 'Запара бывает не на кухне.', 'The rush does not happen in the kitchen.', [(311, 'на кухне.')], ""),
    ('fedya', 'Настоящая запара всегда только в голове!', 'The real rush is always only in your head!', [(312, 'Запара в голове.')], ""),
    ('max', 'Но заказы идут каждую минуту!', 'But orders keep coming every minute!', [], ""),
    ('fedya', 'Делай каждое блюдо по очереди.', 'Make each dish in turn.', [], ""),
    ('max', 'Хорошо, я понял твой совет.', 'Alright, I understood your advice.', [], ""),
    ('fedya', 'Тогда начинай готовить спокойно!', 'Then begin to cook calmly!', [], ""),
]
WALK = [
    (0, None, ["'Alright, newcomer, step aside a little.' Fedya calls Max ", ('fedya', 'новичок,'), " the newbie: 'new' plus an ending that turns it into a person. ", ('fedya', 'в'), ('fedya', 'сторону.'), " to the side, ends in -u because he's sending Max somewhere."]),
    (1, None, ["'Move over, come on, I will help you.' , 'move over', has the reflexive ", ('fedya', 'Подвинься'), " ending because you move yourself. ", ('fedya', 'давай,'), " tacked on after a command works as a nudge: 'come on'."]),
    (2, None, ["'Fedya, thank you, nothing is working out for me!' is literally 'at me nothing comes ", ('max', 'у'), ('max', 'меня'), ('max', 'ничего'), ('max', 'не'), ('max', 'получается!'), " out'. Use it whenever nothing you try works."]),
    (3, None, ["'Right now the main thing is to completely calm down.' , 'the main thing', is an ", ('fedya', 'главное'), " adjective used as a noun. ", ('fedya', 'полностью'), ", 'completely', comes from the word for 'full'."]),
    (4, None, ["'Take a deep breath.' , 'a breath in', starts with ", ('fedya', 'вдох.'), " the prefix for 'in'. ", ('fedya', 'глубокий'), ", 'deep', is the same word you'd use for deep water."]),
    (5, None, ["'And now a slow exhale.' , 'a breath out', starts with ", ('fedya', 'выдох.'), " the prefix for 'out'. The words for breathing in and out share a root, and only the prefix changes."]),
    (6, None, ["'And forever remember the main rule.' , 'forever', joins 'on' and ", ('fedya', 'навсегда'), " 'always'. ", ('fedya', 'запомни'), ", 'remember', shares a root with the word for 'memory'."]),
    (7, None, ["'The rush does not happen in the kitchen.' is kitchen slang for a rush, ", ('fedya', 'Запара'), ' and the whole scene hangs on it. ', ('fedya', 'не'), ' goes right before ', ('fedya', 'на'), ('fedya', 'кухне.'), " so the 'not' is about the place."]),
    (8, None, ["'The real rush is always only in your head!' , 'in the head', has the ", ('fedya', 'в'), ('fedya', 'голове!'), " head', has the place ending. Russian doesn't say 'your' here; the head is understood to be yours."]),
    (9, None, ["'But orders keep coming every minute!' Russian says orders ", ('max', 'идут'), ", 'go', where English has 'come'. ", ('max', 'каждую'), ('max', 'минуту!'), ' takes the feminine accusative endings because it says how often.']),
    (10, None, ["'Make each dish in turn.' For a routine, Russians use an imperfective command like ", ('fedya', 'Делай'), ", 'make'. ", ('fedya', 'по'), ('fedya', 'очереди.'), ' in turn, is built on the word for a queue, so the dishes go out one after another like people in a line.']),
    (11, None, ["'Alright, I understood your advice.' , 'advice', can also mean a ", ('max', 'совет.'), " dvice', can also mean a council, the one in 'Soviet'. ", ('max', 'я'), ('max', 'понял'), ' is what a man says; a woman would use the feminine past form.']),
    (12, None, ["'Then begin to cook calmly!' , 'calmly', is the adverb ", ('fedya', 'спокойно!'), " form. ", ('fedya', 'начинай'), ", 'start', goes straight into ", ('fedya', 'готовить'), ", 'to cook'."]),
]
