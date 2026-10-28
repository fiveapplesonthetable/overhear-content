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
    (0, None, '\'They even closed the restaurant for us.\' Touching on the restaurant to Eleonora, the guest chooses "restoran" ("restaurant") so Eleonora gets the point right away.'),
    (1, None, '\'Please take a seat.\' Eleonora casually extends this courtesy word while facing the guest using "pozhaluysta" ("please") — the all-purpose Russian politeness word that covers both "please" and "you\'re welcome".'),
    (2, None, "'Yes, first I will order some ribs.' The guest fires back right away without holding back, keeping the focus on what actually matters here."),
    (3, None, '\'There are no ribs on my menu.\' Pointing to the ribs before the guest, Barinov reaches for the Russian word "rebryshek" ("ribs", built from "ryobryshko") right at the center of the line.'),
    (4, None, '\'Especially since he still has not paid for yesterday\'s meal.\' Barinov reacts calmly around the guest and centers the thought on "vcherashneye" ("yesterday", from "vcherashniy") without wasting a word.'),
    (5, None, "'Either you cook in silence, or you will have problems.' The guest reacts honestly toward Barinov, without trying to dress up how he really feels."),
    (6, None, '\'You are the one with digestion problems.\' Addressing the digestion around the guest, Barinov reaches for the Russian word "pishchevareniyem" ("digestion", built from "pishchevareniye") right at the center of the line.'),
    (7, None, "'Either you fire him, or I shut down the restaurant!' The guest steps in quietly around Barinov, grounding the moment in plain reality."),
    (8, None, "'You know, it really is time for me to go.' Eleonora reacts boldly around the guest, refusing to let the moment slip past."),
    (9, None, '\'I stopped by to say that the mayor is dissatisfied with you.\' Showing how dissatisfied things are to the guest, Eleonora puts the weight on "nedovolen" ("dissatisfied", from "nedovolnyy") as the exchange unfolds.'),
    (10, None, "'And he is removing you from office.' Eleonora replies right away beside the guest, letting the remark speak for itself."),
    (11, None, "'What do you mean removing me, I do not understand?' The guest questions briskly before Eleonora can change the subject."),
]
