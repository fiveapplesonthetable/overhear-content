ID = 'kukhnya-s06e02-scene-19'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 2
SCENE = 19
TITLE = "Увольнение префекта  (The Prefect Is Dismissed)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = 'ru-en'
VOICES = {"narrator": "sky", "guest": "anja", "eleonora": "angelina"}
LABELS = {"guest": "Гость", "eleonora": "Элеонора"}
SOURCE_NAME = 'Кухня (Kukhnya) S6.02'
SOURCE_FILE = 'sources/kukhnya/s06/e02.ru.srt'

INTRO = 'When the arrogant prefect demands that Eleonora fire Barinov on the spot or have her restaurant shut down, the deputy mayor calmly announces the real reason he asked to meet the prefect today.'

STORY = [
    ('guest', 'Даже ресторан для нас закрыли.', 'They even closed the restaurant for us.', [(321, 'Даже ресторан для нас закрыли')], 'exact'),
    ('eleonora', 'Присаживайтесь, пожалуйста.', 'Please take a seat.', [(322, 'Присаживайтесь')], 'adapted'),
    ('guest', 'Да, сначала закажу ребрышек.', 'Yes, first I will order some ribs.', [(324, 'Да, сначала закажу'), (325, 'ребрышек')], 'adapted'),
    ('guest', 'В моем меню нет ребрышек.', 'There are no ribs on my menu.', [(326, 'В моем меню нет ребрышек')], 'exact'),
    ('guest', 'Тем более он еще за вчерашнее не заплатил.', "Especially since he still has not paid for yesterday's meal.", [(327, 'Тем более он еще за вчерашнее не заплатил')], 'exact'),
    ('guest', 'Либо ты молча готовишь, либо у тебя будут проблемы.', 'Either you cook in silence, or you will have problems.', [(329, 'Либо ты молча готовишь, либо у тебя будут проблемы')], 'exact'),
    ('guest', 'Проблемы у тебя с пищеварением.', 'You are the one with digestion problems.', [(330, 'Проблемы у тебя с пищеварением')], 'exact'),
    ('guest', 'Либо ты его увольняешь, либо я закрываю ресторан!', 'Either you fire him, or I shut down the restaurant!', [(333, 'я закрываю твою')], 'adapted'),
    ('eleonora', 'Вы знаете, мне все-таки пора.', 'You know, it really is time for me to go.', [(336, 'Вы знаете, мне все-таки пора')], 'exact'),
    ('eleonora', 'Я заехал сказать, что мэр вами недоволен.', 'I stopped by to say that the mayor is dissatisfied with you.', [(338, 'заехал сказать'), (339, 'что мэр вами недоволен')], 'adapted'),
    ('eleonora', 'И он отстраняет вас от должности.', 'And he is removing you from office.', [(339, 'и отстраняет вас от должности')], 'adapted'),
    ('guest', 'Как отстраняет, я что-то не понял?', 'What do you mean removing me, I do not understand?', [(341, 'Как отстраняет? Я что-то не понял')], 'exact'),
]

OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."

WALK = [
    (0, None, "'They even closed the restaurant for us.' Here the Russian phrasing highlights 'even' before landing on 'to close'."),
    (1, None, "'Please take a seat.' The meaning hinges on 'take a seat' working together with 'please' in spoken Russian."),
    (2, None, "'Yes, first I will order some ribs.' Spoken Russian keeps this brisk, leaning on 'yes' and finishing on 'ribs'. Chef Barinov answers right away."),
    (3, None, "'There are no ribs on my menu.' Notice how Russian expresses 'my' and 'ribs' with crisp inflection rather than helper words."),
    (4, None, "'Especially since he still has not paid for yesterday's meal.' Chef Barinov anchors the line on 'that', while 'to pay' completes the thought."),
    (5, None, "'Either you cook in silence, or you will have problems.' The grammar packs 'either' and 'problems' into a tight, idiomatic kitchen exchange. Chef Barinov answers right away."),
    (6, None, "'You are the one with digestion problems.' Chef Barinov anchors the line on 'problems', while 'digestion' completes the thought."),
    (7, None, "'Either you fire him, or I shut down the restaurant!' The grammar packs 'either' and 'restaurant' into a tight, idiomatic kitchen exchange."),
    (8, None, "'You know, it really is time for me to go.' Notice how Russian expresses 'you' and 'it's time' with crisp inflection rather than helper words."),
    (9, None, "'I stopped by to say that the mayor is dissatisfied with you.' The grammar packs 'I' and 'dissatisfied' into a tight, idiomatic kitchen exchange."),
    (10, None, "'And he is removing you from office.' The meaning hinges on 'and' working together with 'post' in spoken Russian."),
    (11, None, "'What do you mean removing me, I do not understand?' the guest anchors the line on 'how', while 'understood' completes the thought."),
]

TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'With the corrupt prefect stripped of his post right at the table, Eleonora no longer has to fear his threats. Until next time!'
CLOSING = ("eleonora", "До встречи!")
