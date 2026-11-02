# Authoring module for kukhnya-s01e11-scene-19.
ID = 'kukhnya-s01e11-scene-19'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 11
SCENE = 19
TITLE = 'Проблемный гость  (A Difficult Guest)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kostya': 'Костя', 'nastya': 'Настя'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.11'
SOURCE_FILE = 'sources/kukhnya/s01/e11.ru.dual.srt'
INTRO = 'Kostya wants to make up with Nastya after a quarrel, but she has something worse on her mind. A man at her table is making her life difficult. Listen to who says what.'
OPENER = "Let's take the lines one by one."
TRANSITION = "Let's play it through again."
OUTRO = "Nastya pleads with Kostya to stay out of it, and the critic is the reason. Kostya's patience is not endless. That's it for this one."
CLOSING = ('nastya', 'Пока!')
STORY = [
    ('kostya', 'Настя, ну прости меня за вчерашнее.', 'Nastya, please forgive me for yesterday.', [(232, 'Ну, прости меня.')], ''),
    ('nastya', 'Костя, сейчас вообще не до этого.', 'Kostya, now is really not the time.', [(233, 'Костя, давай потом поговорим, ладно?'), (234, 'Сейчас вообще не до этого.')], ''),
    ('kostya', 'Что случилось? У тебя проблемы?', 'What happened? Do you have problems?', [], ''),
    ('nastya', 'У меня за столиком проблемный гость.', 'I have a difficult guest at the table.', [(234, 'У меня гость проблемный.')], ''),
    ('kostya', 'Он что, хамит тебе?', 'Is he being rude to you?', [(235, 'Чего? Он что, хамит тебя, что ли?')], ''),
    ('nastya', 'Хуже. Он постоянно пристаёт ко мне.', 'Worse. He is constantly bothering me.', [(236, 'Он пристает ко мне.')], ''),
    ('kostya', 'Что? Я сейчас пойду разберусь!', 'What? I will go sort it out right now!', [(237, 'Чего? Сейчас я пойду с ним поговорю.')], ''),
    ('nastya', 'Костя, стой! Не ходи туда.', 'Kostya, stop! Do not go there.', [(238, 'Костя, не ходи никуда, ладно?')], ''),
    ('kostya', 'Почему я должен стоять и смотреть?', 'Why should I stand and watch?', [], ''),
    ('nastya', 'Этот человек — важный ресторанный критик.', 'This man is an important restaurant critic.', [(239, 'Это критик.')], ''),
    ('kostya', 'И что он может сделать?', 'And what can he do?', [], ''),
    ('nastya', 'Он может написать ужасную статью.', 'He can write a terrible article.', [(240, 'Потом знаешь, какую статью может написать на наш ресторан?')], ''),
    ('nastya', 'Сделай заказ быстрее, я пойду в зал.', 'Make the order faster, I will go to the hall.', [(241, 'Так что давай лучше сделай мне заказ побыстрее, и все.')], ''),
]
WALK = [
    (0, None, ["'Nastya, please forgive me for yesterday.' Now we can examine the dialogue: ", ('kostya', 'за'), ('kostya', 'вчерашнее'), ' is for the yesterday thing, a describing word used as a noun. ', ('kostya', 'ну'), ' in front softens it. ', ('kostya', 'прости'), ' is forgive.']),
    (1, None, ["'Kostya, now is really not the time.' Now we can look at the phrase: ", ('nastya', 'не'), ('nastya', 'до'), ('nastya', 'этого'), ' means not up to this, which is the idiom for being in no mood for this. ', ('nastya', 'вообще'), ' adds weight, meaning not at all.']),
    (2, None, ["'What happened? Do you have problems?' We will consider this line: ", ('kostya', 'У'), ('kostya', 'тебя'), ('kostya', 'проблемы'), ' is at you problems, which is the usual pattern for do you have. Kostya drops his own apology at once.']),
    (3, None, ["'I have a difficult guest at the table.' We can consider the words: ", ('nastya', 'проблемный'), ('nastya', 'гость'), ' is problem guest, which is the literal Russian. ', ('nastya', 'за'), ('nastya', 'столиком'), ' is at the little table, with the term for behind.']),
    (4, None, ["'Is he being rude to you?' Now let's examine this line: ", ('kostya', 'хамит'), ' comes from the term for a boor, so it means to behave boorishly. ', ('kostya', 'тебе'), ' is to you. ', ('kostya', 'Он'), ('kostya', 'что'), ' is what, is he.']),
    (5, None, ["'Worse. He is constantly bothering me.' Let us examine the speech: ", ('nastya', 'пристаёт'), ' is pesters, meaning to keep at someone. ', ('nastya', 'ко'), ('nastya', 'мне'), ' is to me. ', ('nastya', 'Хуже'), ' is worse, the term from the hungover guest.']),
    (6, None, ["'What? I will go sort it out right now!' Kostya says ", ('kostya', 'пойду'), ('kostya', 'разберусь'), ", meaning I'll go sort out, without an and. ", ('kostya', 'разберусь'), ' is the term Barinov used when he stormed off to the dining room.']),
    (7, None, ["'Kostya, stop! Do not go there.' After the negative, Russian prefers to use ", ('nastya', 'Не'), ('nastya', 'ходи'), ' for do not go. ', ('nastya', 'туда'), ' is to there, and ', ('nastya', 'стой'), ' is stop.']),
    (8, None, ["'Why should I stand and watch?' Now let's look at this part: ", ('kostya', 'должен'), ' means must, and is related to the word for debt. ', ('kostya', 'стоять'), ('kostya', 'и'), ('kostya', 'смотреть'), ' is to stand and to watch. Kostya cannot see why he should stand still.']),
    (9, None, ["'This man is an important restaurant critic.' The dash stands in for is. ", ('nastya', 'важный'), ' is important. Nastya names the problem in one sentence.']),
    (10, None, ["'And what can he do?' Short and sharp. Putting ", ('kostya', 'И'), ('kostya', 'что'), ', meaning and what, up front turns it into a shrug of a challenge, and ', ('kostya', 'может'), ', meaning he can, needs a second verb, here ', ('kostya', 'сделать'), ', meaning to do.']),
    (11, None, ["'He can write a terrible article.' Notice for article becomes ", ('nastya', 'статью'), ' and is feminine, so ', ('nastya', 'ужасную'), ' has a feminine ending. ', ('nastya', 'написать'), ' has a prefix, which makes write a finished job.']),
    (12, None, ["'Make the order faster, I will go to the hall.' Let us break down the speech: ", ('nastya', 'Сделай'), ('nastya', 'заказ'), ' is make the order, here the drinks for her table. ', ('nastya', 'быстрее'), ' is faster. ', ('nastya', 'в'), ('nastya', 'зал'), ' is to the hall.']),
]
