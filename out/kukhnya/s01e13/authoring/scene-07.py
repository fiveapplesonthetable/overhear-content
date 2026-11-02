# Authoring module for kukhnya-s01e13-scene-07.
ID = 'kukhnya-s01e13-scene-07'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 13
SCENE = 7
TITLE = 'Разбитое зеркало  (A Broken Mirror)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'eleonora': 'Элеонора', 'nastya': 'Настя'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.13'
SOURCE_FILE = 'sources/kukhnya/s01/e13.ru.dual.srt'
INTRO = "Somebody has broken the side mirror on Barinov's car, and his ex-wife Eleonora is the first to point it out. He doesn't take it well. Hear it in Russian first."
OPENER = 'Back to the start, and then on to what Nastya makes of it.'
TRANSITION = 'And the whole scene without stopping.'
OUTRO = "Barinov and Eleonora are now even, and Nastya is sure it isn't over. Listen for 'even', the word that settles a score. Talk soon."
CLOSING = ('nastya', 'Пока!')
STORY = [
    ('eleonora', 'Виктор Петрович, у вас тут зеркало сломанное.', 'Viktor Petrovich, you have a broken mirror here.', [(93, 'вас тут зеркало сломанное')], ''),
    ('barinov', 'Да надо же!', 'Well, would you look at that!', [(94, 'Да надо же')], ''),
    ('barinov', 'А вы не заметили?', "Didn't you notice?", [(94, 'А вы не заметили')], ''),
    ('barinov', 'Что у вас тоже?', 'That yours is too?', [(94, 'что у вас тоже')], ''),
    ('eleonora', 'У меня? Как? Где?', 'Mine? How? Where?', [(95, 'У меня'), (95, 'Как'), (96, 'Где')], ''),
    ('barinov', 'Ну вот же.', 'Right there.', [(97, 'Ну вот же')], ''),
    ('barinov', 'Теперь мы квиты.', "Now we're even.", [(99, 'Теперь мы квиты')], ''),
    ('nastya', 'Костя, ты видел?', 'Kostya, did you see?', [], ''),
    ('nastya', 'Он разбивает зеркало её машины.', 'He smashes the mirror on her car.', [(100, 'зеркало ее машины')], ''),
    ('nastya', 'А она типа не при делах.', 'And she acts like she had nothing to do with it.', [(101, 'А она'), (101, 'типа не при делах')], ''),
    ('nastya', 'Я уверена.', 'I am sure.', [], ''),
    ('nastya', 'Это просто так не закончится.', "This won't just blow over.", [(91, 'это')], ''),
]
WALK = [
    (0, None, ["'Viktor Petrovich, you have a broken mirror here.' Let us break down this line: ", ('eleonora', 'у'), ('eleonora', 'вас'), ('eleonora', 'тут'), " is courteous Russian for 'you have'. ", ('eleonora', 'сломанное'), " puts a special ending on 'broken' to go with 'mirror'."]),
    (1, None, ["'Well, would you look at that!' Let us inspect this part: ", ('barinov', 'надо'), ('barinov', 'же'), " is an old idiom meaning 'well I never!' It's made out of the word for 'necessary', and the little ", ('barinov', 'же'), ' that adds feeling.']),
    (2, None, ["'Didn't you notice?' Barinov keeps the polite ", ('barinov', 'вы'), ' with his ex-wife. ', ('barinov', 'заметили'), ", noticed, ends in the past ending that goes with polite 'you' even for one person."]),
    (3, None, ["'That yours is too?' It is only 'at you also', which is Russian for 'yours too'. ", ('barinov', 'тоже'), ' is the part to take away.']),
    (4, None, ["'Mine? How? Where?' Three question words fire in a row, with no action word between them. ", ('eleonora', 'У'), ('eleonora', 'меня'), " is Russian for 'mine', and the other two are 'how' and 'where'."]),
    (5, None, ["'Right there.' Three tiny words, ", ('barinov', 'Ну'), ('barinov', 'вот'), ('barinov', 'же'), ", pile up to mean 'look, right there'. The little ", ('barinov', 'же'), ' adds the weight, and ', ('barinov', 'вот'), ' is the pointing word.']),
    (6, None, ["'Now we're even.' We can break down this part: ", ('barinov', 'квиты'), " reuses the term in the English 'quits', and it means the same. ", ('barinov', 'Теперь'), " is 'now', and ", ('barinov', 'мы'), " is 'we'."]),
    (7, None, ["'Kostya, did you see?' A man's ", ('nastya', 'видел'), " takes a special ending. A woman's would end differently, and the question stays the same."]),
    (8, None, ["'He smashes the mirror on her car.' The action word ", ('nastya', 'разбивает'), ' means smashing to bits, and the everyday word for breaking is for a mechanism. ', ('nastya', 'её'), ('nastya', 'машины'), " has a special ending that means 'of'."]),
    (9, None, ["'And she acts like she had nothing to do with it.' Let's consider the speech: ", ('nastya', 'типа'), " is casual speech for 'sort of' or 'like'. ", ('nastya', 'не'), ('nastya', 'при'), ('nastya', 'делах'), ", or 'not at the deals', is slang for 'nothing to do with it'."]),
    (10, None, ["'I am sure.' The extra sound at the end of ", ('nastya', 'уверена'), ' tells you Nastya is speaking, since a man would say it without. Two words are all it takes.']),
    (11, None, ["'This won't just blow over.' Let's look at this line: ", ('nastya', 'просто'), ('nastya', 'так'), " is 'just like that'. ", ('nastya', 'закончится'), " means 'will end', reflecting back because things end by themselves."]),
]
