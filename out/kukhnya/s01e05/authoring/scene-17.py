# Authoring module for kukhnya-s01e05-scene-17.
ID = 'kukhnya-s01e05-scene-17'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 5
SCENE = 17
TITLE = 'Невинный обман  (An Innocent Deception)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kostya': 'Костя', 'nastya': 'Настя'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.05'
SOURCE_FILE = 'sources/kukhnya/s01/e05.ru.dual.srt'
INTRO = 'Still in the Claude Monet storeroom, Nastya has second thoughts. Using Kostya to get back at Max feels wrong, and she tells him so. Kostya is far too kind to take offence, and he has an idea of his own. Listen in Russian first.'
OPENER = 'Slowly now. Nastya owns up, Kostya reassures her, and together they settle on a plan.'
TRANSITION = "Here's the storeroom talk again, nonstop."
OUTRO = 'Two lines worth keeping: Nastya\'s "I can\'t do it like this", and Kostya\'s "I\'m ready for anything".'
CLOSING = ('nastya', 'Пока!')
STORY = [
    ('nastya', 'Костя, подожди, я так не могу.', 'Kostya, wait, I cannot do this.', [(209, 'Костя, подожди'), (210, 'Я так не могу')], ""),
    ('kostya', 'Что случилось, Настя, что не так?', 'What happened, Nastya, what is wrong?', [], ""),
    ('nastya', 'Я хотела отомстить Максиму через тебя.', 'I wanted to get back at Maxim through you.', [(211, 'чтобы отомстить Максиму')], ""),
    ('kostya', 'Макс вполне заслуживает хорошего урока, знаешь.', 'Max fully deserves a good lesson, you know.', [(212, 'он вообще заслуживает')], ""),
    ('nastya', 'Я не могу принять такую жертву.', 'I cannot accept such a sacrifice.', [(214, 'не могу принять от тебя такой жертвы')], ""),
    ('kostya', 'И что же нам теперь делать?', 'And what are we to do now?', [], ""),
    ('nastya', 'Давай просто всем скажем про нас.', 'Let us simply tell everyone about us.', [(215, 'всем скажем')], ""),
    ('kostya', 'А на самом деле ничего нет?', 'And in reality there is nothing?', [(216, 'А на самом деле ничего')], ""),
    ('nastya', 'Да, это будет только наш секрет.', 'Yes, this will be only our secret.', [], ""),
    ('kostya', 'Хорошо, пусть Макс немного поревнует.', 'Fine, let Max be slightly jealous.', [], ""),
    ('nastya', 'Костя, спасибо, ты просто самый классный!', 'Kostya, thank you, you are simply the best!', [(218, 'такой классный')], ""),
    ('kostya', 'Для тебя я готов на всё.', 'For you I am ready for anything.', [], ""),
    ('nastya', 'Мой заказ готов, я побегу работать!', "My order is ready, I'll run back to work!", [(219, 'заказ готов')], ""),
]
WALK = [
    (0, None, ['\'Kostya, wait, I cannot do this.\' corresponds to \'wait\' for someone you ', ('nastya', 'подожди'), ' address informally. ', ('nastya', 'я'), ('nastya', 'так'), ('nastya', 'не'), ('nastya', 'могу'), ", meaning literally \'I so not can\', translates to \'I can\'t do it like this\'."]),
    (1, None, ['\'What happened, Nastya, what is wrong?\' is the standard phrasing for \'what ', ('kostya', 'Что'), ('kostya', 'случилось'), " happened?\'. ", ('kostya', 'что'), ('kostya', 'не'), ('kostya', 'так'), " translates literally as \'what not so\', with no \'is\' included at all."]),
    (2, None, ['\'I wanted to get back at Maxim through you.\' Nastya uses Max\'s full name, ', ('nastya', 'Максиму'), ', which sounds colder. ', ('nastya', 'отомстить'), ', \'to take revenge\', directs the action towards the person you\'re getting back at: ', ('nastya', 'отомстить'), ('nastya', 'Максиму'), '.']),
    (3, None, ['\'Max fully deserves a good lesson, you know.\' , ', ('kostya', 'заслуживает'), ' \'deserves\', requires the genitive case here, resulting in ', ('kostya', 'хорошего'), ('kostya', 'урока'), '. ', ('kostya', 'знаешь'), ' at the end functions like the English \'you know\'.']),
    (4, None, ['\'I cannot accept such a sacrifice.\' The base word for \'sacrifice\' can also mean \'victim\', depending on context. Here it takes the form ', ('nastya', 'жертву'), ' as the object she won\'t accept.']),
    (5, None, ['\'And what are we to do now?\' translates literally as \'what then to ', ('kostya', 'что'), ('kostya', 'же'), ('kostya', 'нам'), ('kostya', 'делать'), ' us to do\', using ', ('kostya', 'нам'), ', \'to us\', instead of \'we\'. The small word ', ('kostya', 'же'), ' adds a note of \'so then\'.']),
    (6, None, ['\'Let us simply tell everyone about us.\' , originating from ', ('nastya', 'Давай'), ' \'give\', turns what follows into \'let\'s\': ', ('nastya', 'Давай'), ('nastya', 'скажем'), '. ', ('nastya', 'всем'), ', \'to everyone\', is built from the word for \'all\', while ', ('nastya', 'про'), ('nastya', 'нас'), ' expresses \'about us\'.']),
    (7, None, ['\'And in reality there is nothing?\' , literally \'on the very ', ('kostya', 'на'), ('kostya', 'самом'), ('kostya', 'деле'), " deed\', signifies \'actually\' or \'in reality\'. ", ('kostya', 'ничего'), ('kostya', 'нет'), " stands for \'there is nothing\'."]),
    (8, None, ['\'Yes, this will be only our secret.\' sounds almost identical to its English ', ('nastya', 'секрет'), ' counterpart. ', ('nastya', 'будет'), ', \'will be\', occupies the slot that \'is\' leaves empty in the present tense.']),
    (9, None, ['\'Fine, let Max be slightly jealous.\' means ', ('kostya', 'пусть'), ' \'let\', as in \'let him\'. ', ('kostya', 'поревнует'), ' begins with a prefix indicating that the action is done for a little while.']),
    (10, None, ['\'Kostya, thank you, you are simply the best!\' , ', ('nastya', 'классный'), ' \'great\', is a casual descriptor derived from the word for \'class\'. Pairing it with ', ('nastya', 'самый'), ' produces ', ('nastya', 'самый'), ('nastya', 'классный'), ', elevating it to \'the very best\'.']),
    (11, None, ['\'For you I am ready for anything.\' , \'for ', ('kostya', 'Для'), ('kostya', 'тебя'), " you\', is placed first for emphasis. ", ('kostya', 'готов'), ('kostya', 'на'), ('kostya', 'всё'), ", taking the accusative case, conveys \'ready for anything\'."]),
    (12, None, ['\'My order is ready, I\'ll run back to work!\' here ', ('nastya', 'готов'), ' describes ', ('nastya', 'заказ'), ', a masculine noun, so it shares the same bare form Kostya used about himself. ', ('nastya', 'побегу'), ', \'I\'ll run\', is the perfective form of the verb meaning \'to run\'.']),
]
