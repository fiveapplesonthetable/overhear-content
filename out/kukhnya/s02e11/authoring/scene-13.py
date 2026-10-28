# Authoring module for kukhnya-s02e11-scene-13.
ID = 'kukhnya-s02e11-scene-13'
SHOW = 'kukhnya'
SEASON = 2
EPISODE = 11
SCENE = 13
TITLE = 'Секрет настоящего Шефа  (The Secret of a True Chef)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'max': 'Макс', 'nastya': 'Настя'}
SOURCE_NAME = 'Кухня (Kukhnya) S2.11'
SOURCE_FILE = 'sources/kukhnya/s02/e11.ru.srt'
INTRO = 'Visiting the hospital with fresh food, Lyova confesses to Viktor Petrovich that the diplomatic trick backfired and the kitchen is still in chaos. Barinov explains that the only way to keep line cooks in check is to be a ruthless bastard, something gentle Lyova struggles to do.'
OPENER = "Now let's go back through the conversation line by line."
TRANSITION = "Alright, let's hear the whole conversation once more from start to finish."
OUTRO = 'That wraps up this scene as lyova visits Chef Barinov in the hospital to admit that the reconciliation trick failed, and Barinov explains that to command the kitchen, a chef must act like a ruthless tyrant. Until next time!'
CLOSING = ('max', 'Хорошего дня!')
STORY = [
    ('max', 'Здравствуйте, Петрович.', 'Hello, Petrovich.', [(218, 'Здравствуйте, Петрович')], ''),
    ('barinov', 'Да. Здравствуйте.', 'Yes. Hello.', [(218, 'Да. Здравствуйте')], ''),
    ('nastya', 'Как здоровье?', 'How is your health?', [(219, 'Как здоровье')], ''),
    ('max', 'Вот спасибо.', 'Thank you very much.', [(221, 'Вот спасибо')], ''),
    ('barinov', 'А то у меня вся постель в крошках.', 'Otherwise my whole bed is full of crumbs.', [(222, 'А то у меня вся постель в крошках')], ''),
    ('nastya', 'Как дела на кухне?', 'How are things going in the kitchen?', [(224, 'Как дела на кухне')], ''),
    ('max', 'Ты шутишь, что ли, совсем?', 'Are you completely joking or what?', [(226, 'что ли совсем')], 'adapted'),
    ('barinov', 'Вообще-то у меня только один способ действовал.', 'Actually, only one method ever worked for me.', [(227, 'Вообще-то у меня только один способ действовал')], ''),
    ('nastya', 'Понимаешь, Лёва, чтобы быть настоящим шефом.', 'You see, Lyova, in order to be a real head chef.', [(228, 'Понимаешь, Лёва, чтобы быть настоящим шефом')], ''),
    ('max', 'Какой? Понимаешь?', 'Which method? You see?', [(228, 'Какой? Понимаешь')], ''),
    ('barinov', 'Надо быть настоящей гнидой.', 'You have to be a real bastard.', [(229, 'Надо быть настоящей гнидой')], ''),
    ('nastya', 'А гнидой Лёва быть нелегко.', 'And being a bastard, Lyova, is not easy.', [(230, 'А гнидой Лёва быть нелегко')], ''),
    ('max', 'Ладно, иди работай.', 'All right, go back to work.', [(231, 'Ладно, иди работай')], ''),
]
WALK = [
    (0, None, "'Hello, Petrovich.' Around the truth and moment, Max sets a calm, everyday tone with Barinov."),
    (1, None, "'Yes. Hello.' With the truth and conversation in play, Barinov keeps this short reply brisk and direct."),
    (2, None, '\'How is your health?\' By asking how Barinov\'s health is, Nastya presses Barinov for a straight answer. In Russian, she does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (3, None, "'Thank you very much.' With the secret and hospital in play, Max keeps this short reply brisk and direct."),
    (4, None, '\'Otherwise my whole bed is full of crumbs.\' Claiming that otherwise his whole bed is full of crumbs sounds confident, even if Max has doubts. Russian expresses having something as "by me is", keeping the phrase short and grounded.'),
    (5, None, '\'How are things going in the kitchen?\' Here asking how things going in the kitchen are shows Nastya looking for the real truth. In Russian, she does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (6, None, "'Are you completely joking or what?' By checking whether Barinov completely joking, Max presses Barinov for a straight answer."),
    (7, None, '\'Actually, only one method ever worked for me.\' Realizing that only one method ever worked for him changes how Barinov handles the situation. Russian expresses having something as "by me is", keeping the phrase short and grounded.'),
    (8, None, "'You see, Lyova, in order to be a real head chef.' Turning from the secret to the work, Nastya keeps the exchange moving."),
    (9, None, "'Which method? You see?' Turning from the chaos to the conversation, Max asks Barinov directly."),
    (10, None, '\'You have to be a real bastard.\' Admitting that Max has to be a real bastard shows Barinov being honest for a change. There is no "you" needed in the Russian here: one short word states the rule for everyone in the room.'),
    (11, None, "'And being a bastard, Lyova, is not easy.' Saying that being a bastard Lyova is not easy is how Nastya sets the tone with Barinov."),
    (12, None, "'All right, go back to work.' Around the hospital and shift, Max sets a calm, everyday tone with Barinov."),
]
