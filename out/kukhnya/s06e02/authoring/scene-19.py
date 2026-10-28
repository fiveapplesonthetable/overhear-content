# Authoring module for kukhnya-s06e02-scene-19.
ID = 'kukhnya-s06e02-scene-19'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 2
SCENE = 19
TITLE = 'Увольнение префекта  (The Prefect Is Dismissed)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'eleonora': 'Элеонора', 'guest': 'Гость'}
SOURCE_NAME = 'Кухня (Kukhnya) S6.02'
SOURCE_FILE = 'sources/kukhnya/s06/e02.ru.srt'
INTRO = 'When the arrogant prefect demands that Eleonora fire Barinov on the spot or have her restaurant shut down, the deputy mayor calmly announces the real reason he asked to meet the prefect today.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'With the corrupt prefect stripped of his post right at the table, Eleonora no longer has to fear his threats. Until next time!'
CLOSING = ('eleonora', 'До встречи!')
STORY = [
    ('guest', 'Даже ресторан для нас закрыли.', 'They even closed the restaurant for us.', [(321, 'Даже ресторан для нас закрыли')], 'exact'),
    ('eleonora', 'Присаживайтесь, пожалуйста.', 'Please take a seat.', [(322, 'Присаживайтесь')], 'adapted'),
    ('guest', 'Да, сначала закажу ребрышек.', 'Yes, first I will order some ribs.', [(324, 'Да, сначала закажу'), (325, 'ребрышек')], 'adapted'),
    ('barinov', 'В моем меню нет ребрышек.', 'There are no ribs on my menu.', [(326, 'В моем меню нет ребрышек')], 'exact'),
    ('barinov', 'Тем более он еще за вчерашнее не заплатил.', "Especially since he still has not paid for yesterday's meal.", [(327, 'Тем более он еще за вчерашнее не заплатил')], 'exact'),
    ('guest', 'Либо ты молча готовишь, либо у тебя будут проблемы.', 'Either you cook in silence, or you will have problems.', [(329, 'Либо ты молча готовишь, либо у тебя будут проблемы')], 'exact'),
    ('barinov', 'Проблемы у тебя с пищеварением.', 'You are the one with digestion problems.', [(330, 'Проблемы у тебя с пищеварением')], 'exact'),
    ('guest', 'Либо ты его увольняешь, либо я закрываю ресторан!', 'Either you fire him, or I shut down the restaurant!', [(333, 'я закрываю твою')], 'adapted'),
    ('eleonora', 'Вы знаете, мне все-таки пора.', 'You know, it really is time for me to go.', [(336, 'Вы знаете, мне все-таки пора')], 'exact'),
    ('eleonora', 'Я заехал сказать, что мэр вами недоволен.', 'I stopped by to say that the mayor is dissatisfied with you.', [(338, 'заехал сказать'), (339, 'что мэр вами недоволен')], 'adapted'),
    ('eleonora', 'И он отстраняет вас от должности.', 'And he is removing you from office.', [(339, 'и отстраняет вас от должности')], 'adapted'),
    ('guest', 'Как отстраняет, я что-то не понял?', 'What do you mean removing me, I do not understand?', [(341, 'Как отстраняет? Я что-то не понял')], 'exact'),
]
WALK = [
    (0, None, '\'They even closed the restaurant for us.\' The guest highlights one telling choice toward Barinov: "restoran" means "restaurant", and it carries the main weight of what the guest is saying.'),
    (1, None, '\'Please take a seat.\' Eleonora drops the thought with ease: dropping in "pozhaluysta" ("please") keeps the request polite on the surface even in a brisk exchange.'),
    (2, None, "'Yes, first I will order some ribs.' The guest counters right away in this moment, steering the talk right where he wants it."),
    (3, None, '\'There are no ribs on my menu.\' Barinov anchors one concrete word at once: "rebryshek" means "ribs" (from "ryobryshko"), giving the line its exact edge.'),
    (4, None, "'Especially since he still has not paid for yesterday's meal.' Barinov fires back briskly facing Eleonora, testing Eleonora's reaction in the middle of the exchange."),
    (5, None, "'Either you cook in silence, or you will have problems.' The guest opens up honestly during the talk, letting the remark speak for itself."),
    (6, None, '\'You are the one with digestion problems.\' Barinov leans on one vivid choice for Eleonora: "pishchevareniyem" means "digestion" (from "pishchevareniye"), giving the line its exact edge.'),
    (7, None, '\'Either you fire him, or I shut down the restaurant!\' The guest stresses one vivid term for Eleonora: "uvolnyayesh" means "to fire, to dismiss" (from "uvolnyat"), giving the line its exact edge.'),
    (8, None, "'You know, it really is time for me to go.' Eleonora follows up boldly without any doubt, before Barinov can change the subject."),
    (9, None, '\'I stopped by to say that the mayor is dissatisfied with you.\' Eleonora centers one loaded word at once: "nedovolen" means "dissatisfied" (from "nedovolnyy"), giving the line its exact edge.'),
    (10, None, '\'And he is removing you from office.\' Eleonora frames one telling touch in earnest: "otstranyayet" means "suspends, removes" (from "otstranyat"), giving the line its exact edge.'),
    (11, None, "'What do you mean removing me, I do not understand?' The guest questions briskly where this conversation is heading next."),
]
