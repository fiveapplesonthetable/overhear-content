# Authoring module for kukhnya-s01e01-scene-23.
ID = 'kukhnya-s01e01-scene-23'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 1
SCENE = 23
TITLE = 'Объективная оценка  (An Objective Opinion)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kostya': 'Костя', 'max': 'Макс', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.01'
SOURCE_FILE = 'sources/kukhnya/s01/e01.ru.dual.srt'
INTRO = "Max has finally plated a dish he's proud of. The bartender, Kostya, warns him the chef will never like it, and Max wants somebody honest to try it first. Then Vika arrives, and she wants the dish for her guests right now. Here it is in Russian first."
OPENER = "Let's go back and pick the lines apart."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'Vika walks off with the plate, and nobody knows how this will turn out. Notice how often Russians say "I\'ll do it myself", because you will hear it again.'
CLOSING = ('vika', 'Пока!')
STORY = [
    ('kostya', 'Здорово у тебя всё получается, Макс!', 'You are doing great at everything, Max!', [(307, 'Здорово у тебя получается')], ''),
    ('kostya', 'Жалко только, что шеф этого не оценит.', "Too bad only that the chef won't appreciate this.", [(308, 'Жалко только, что он этого не оценит')], ''),
    ('max', 'Но это мы с тобой ещё посмотрим.', 'We will see about that yet.', [(309, 'Но это мы еще посмотрим')], ''),
    ('kostya', 'Да он даже пробовать не станет!', "Why, he won't even taste it!", [(309, 'Да он даже не попробует')], ''),
    ('kostya', 'А если попробует, ему не понравится.', "And if he tastes it, he won't like it.", [(310, 'А если попробует, ему все равно не понравится')], ''),
    ('kostya', 'Я очень хорошо знаю нашего шефа.', 'I know our chef very well.', [(311, 'Я его знаю')], ''),
    ('max', 'Погоди, нам нужна более объективная оценка.', 'Wait, we need a more objective opinion.', [(312, 'Погоди'), (313, 'Тогда нам нужна более объективная оценка')], ''),
    ('max', 'Пусть кто-нибудь другой сначала попробует.', 'Let someone else taste it first.', [(314, 'И')], ''),
    ('vika', 'Сколько можно ждать горячее блюдо?', 'How long must one wait for the hot dish?', [], ''),
    ('vika', 'Всё приходится делать самой на этой кухне.', 'One has to do everything herself in this kitchen.', [(310, 'все')], ''),
    ('max', 'Я сейчас сам отнесу в зал.', 'I will carry it to the hall myself right now.', [], ''),
    ('vika', 'Отойди в сторону и иди работай!', 'Step aside and go back to work!', [], ''),
    ('max', 'Это блюдо сделано по всем правилам.', 'This dish is made according to all rules.', [], ''),
    ('vika', 'Клиенты давно ждут свой вкусный ужин.', 'The clients have been waiting for their delicious dinner for a long time.', [], ''),
]
WALK = [
    (0, None, ['\'You are doing great at everything, Max!\' ', ('kostya', 'Здорово'), ' is casual for "great", and it comes from ', ('kostya', 'Здоров'), ', health, as does the long hello. ', ('kostya', 'У тебя всё получается'), ' is "at you everything works out".']),
    (1, None, ['\'Too bad only that the chef won\'t appreciate this.\' ', ('kostya', 'Жалко'), ' says "what a pity" with no "it is". ', ('kostya', 'Оценит'), ', "will appreciate", comes from ', ('kostya', 'цен'), ', price.']),
    (2, None, ['\'We will see about that yet.\' ', ('max', 'Мы с тобой'), ' is "we with you", for "you and I". ', ('max', 'Ещё посмотрим'), ' is "we\'ll yet see", a defiant "we\'ll see about that".']),
    (3, None, ['\'Why, he won\'t even taste it!\' ', ('kostya', 'пробовать не станет'), ' is "will not become to taste", Russian for "won\'t go so far as to taste". The opening ', ('kostya', 'да'), ' adds a "come on" feeling.']),
    (4, None, ['\'And if he tastes it, he won\'t like it.\' Kostya uses the same liking pattern: ', ('kostya', 'ему'), ', "to him", plus ', ('kostya', 'не понравится'), ', it won\'t please. ', ('kostya', 'Попробует'), ', he\'ll try, needs no "he" in front, because the ', ('kostya', '-ет'), ' ending already says who.']),
    (5, None, ['\'I know our chef very well.\' ', ('kostya', 'Знаю'), ' is "I know", for people and facts. ', ('kostya', 'Нашего шефа'), ' is "our chef", both words in the object shape.']),
    (6, None, ['\'Wait, we need a more objective opinion.\' ', ('max', 'Более'), ' is "more", placed before a describing word: ', ('max', 'более объективная'), '. ', ('max', 'Оценка'), ' is "opinion", from ', ('max', 'оцен'), '.']),
    (7, None, ['\'Let someone else taste it first.\' Put ', ('max', 'пусть'), ' in front of a verb and you get "let him do it": ', ('max', 'пусть'), '... ', ('max', 'попробует'), ', let someone taste. ', ('max', 'Кто-нибудь'), ' is "someone, anyone", and adding ', ('max', 'другой'), ', other, gives "someone else".']),
    (8, None, ['\'How long must one wait for the hot dish?\' ', ('vika', 'Сколько можно'), ' is "how much is possible", Russian for "how long must we". ', ('vika', 'Ждать'), ' takes the dish directly, with no "for".']),
    (9, None, ['\'One has to do everything herself in this kitchen.\' ', ('vika', 'Приходится'), ' is "it falls to one", from ', ('vika', 'приходи'), ', to come. ', ('vika', 'Самой'), ' is "herself", in the form for a woman.']),
    (10, None, ['\'I will carry it to the hall myself right now.\' ', ('max', 'Отнесу'), ' is "I will carry away", with the prefix ', ('max', 'от-'), ' for \"away\".  ', ('max', 'В зал'), ' has no ending because he\'s going to it.']),
    (11, None, ['\'Step aside and go back to work!\' ', ('vika', 'Отойди в сторону'), ' is "step to the side". ', ('vika', 'Иди работай'), ' is two commands in a row, "go work", meaning "go and work".']),
    (12, None, ['\'This dish is made according to all rules.\' ', ('max', 'Сделано'), ' is "made", short and neuter to match ', ('max', 'блюдо'), '. ', ('max', 'По всем правилам'), ' is "according to all rules": the ', ('max', '-ам'), ' follows ', ('max', 'по'), '.']),
    (13, None, ['\'The clients have been waiting for their delicious dinner for a long time.\' ', ('vika', 'Давно ждут'), ' is "long they wait", and Russian uses the present for something that began a while ago. ', ('vika', 'Свой'), ' is "their own".']),
]
