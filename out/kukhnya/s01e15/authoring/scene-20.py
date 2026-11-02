# Authoring module for kukhnya-s01e15-scene-20.
ID = 'kukhnya-s01e15-scene-20'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 15
SCENE = 20
TITLE = 'Ожидание Макса  (Waiting for Max)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'ilya': 'Илья', 'senya': 'Сеня'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.15'
SOURCE_FILE = 'sources/kukhnya/s01/e15.ru.dual.srt'
INTRO = 'The kitchen staff are wondering whether Max will come back to work. Ilya and Senya talk it over. Hear it in Russian first.'
OPENER = 'One last time, slowly.'
TRANSITION = 'And the last scene of the episode, once more.'
OUTRO = 'Everyone is sure Max will turn up. Does the chef agree? That was the last scene of the episode, so see you in the next one.'
CLOSING = ('senya', 'Пока!')
STORY = [
    ('ilya', 'Тебя это тоже волнует?', 'Does this worry you too?', [(372, 'Тебя это тоже воспринимает?')], ''),
    ('senya', 'Что именно?', 'What exactly?', [], ''),
    ('ilya', 'Например, Макс придёт или нет?', 'For example, will Max come or not?', [(373, 'Например, зайдет Макс или нет?')], ''),
    ('senya', 'Я думаю, он придёт.', 'I think he will come.', [], ''),
    ('ilya', 'Он любит нашу кухню.', 'He loves our kitchen.', [], ''),
    ('senya', 'И он любит работать.', 'And he loves to work.', [], ''),
    ('ilya', 'А как же шеф?', 'And what about the chef?', [], ''),
    ('senya', 'Шеф его простит.', 'The chef will forgive him.', [], ''),
    ('ilya', 'Они помирятся.', 'They will make peace.', [], ''),
    ('senya', 'Конечно помирятся.', 'Of course they will make peace.', [], ''),
    ('ilya', 'Тогда всё будет хорошо.', 'Then everything will be fine.', [], ''),
    ('senya', 'Да, просто ждём.', 'Yes, we are just waiting.', [], ''),
]
WALK = [
    (0, None, ["'Does this worry you too?' Russian makes the worried person the focus, so you takes the ", ('ilya', 'Тебя'), ' form. The term meaning too is ', ('ilya', 'тоже'), '.']),
    (1, None, ["'What exactly?' The term ", ('senya', 'именно'), ' means exactly or namely, and ', ('senya', 'Что'), ('senya', 'именно'), ' asks for the specific thing.']),
    (2, None, ["'For example, will Max come or not?' Now we can break down the dialogue: ", ('ilya', 'Например'), ' means for example. We hear ', ('ilya', 'или'), ('ilya', 'нет'), ' ends a yes-or-no question.']),
    (3, None, ["'I think he will come.' No will needed as ", ('senya', 'придёт'), ' is a completed action, so its shape already points ahead. Here we have ', ('senya', 'Я'), ('senya', 'думаю'), ' sits in front, just like I think in English.']),
    (4, None, ["'He loves our kitchen.' Notice meaning kitchen becomes ", ('ilya', 'кухню'), ' because it is what he loves, and the term meaning our changes to ', ('ilya', 'нашу'), ' to match.']),
    (5, None, ["'And he loves to work.' We can consider this line: ", ('senya', 'любит'), ('senya', 'работать'), ' uses two verbs together. It is the most natural way to say you like doing something.']),
    (6, None, ["'And what about the chef?' Let's consider the words: ", ('ilya', 'А'), ('ilya', 'как'), ('ilya', 'же'), ' translates to and how then, a handy way to ask what about.']),
    (7, None, ["'The chef will forgive him.' The term ", ('senya', 'простит'), ' means will forgive, and ', ('senya', 'его'), ' is the expression for him. Senya is confident.']),
    (8, None, ["'They will make peace.' The word ", ('ilya', 'помирятся'), ' comes out of peace, with an ending for with each other. It also means world.']),
    (9, None, ["'Of course they will make peace.' Senya repeats the verb ", ('senya', 'помирятся'), ' as his answer. Russians do it all the time, instead of a flat yes.']),
    (10, None, ["'Then everything will be fine.' We will focus on this line: ", ('ilya', 'Тогда'), ' is then, in the sense in that case. Notice ', ('ilya', 'всё'), ('ilya', 'будет'), ('ilya', 'хорошо'), ' means all will be well.']),
    (11, None, ["'Yes, we are just waiting.' Now let's examine the dialogue: ", ('senya', 'ждём'), ' means we wait, and the Russian shape also covers we are waiting. Notice ', ('senya', 'просто'), ' is just.']),
]
