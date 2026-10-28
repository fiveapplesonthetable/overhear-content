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
    (0, None, "'They even closed the restaurant for us.' Around the restaurant and office, the guest sets a calm, everyday tone with Barinov."),
    (1, None, "'Please take a seat.' Here telling Barinov to take a seat sets up the next turn in their exchange."),
    (2, None, "'Yes, first I will order some ribs.' Realizing that first he will order some ribs changes how the guest handles the situation."),
    (3, None, "'There are no ribs on my menu.' Noting that there are no ribs on his menu keeps Barinov's side of the story simple and clear."),
    (4, None, "'Especially since he still has not paid for yesterday's meal.' Even though especially since he still has not paid for yesterday meal, Barinov keeps a steady face in front of Eleonora."),
    (5, None, '\'Either you cook in silence, or you will have problems.\' Admitting that either Barinov cooks in silence or Barinov will have problems shows the guest being honest for a change. In Russian you say "by me" or "with us" rather than "I have", so the situation sits right with the person.'),
    (6, None, "'You are the one with digestion problems.' Noting that Eleonora is the one with digestion problems keeps Barinov's side of the story simple and clear."),
    (7, None, '\'Either you fire him, or I shut down the restaurant!\' Insisting that either Barinov fires him or he shuts down the restaurant shows the guest is not backing down. Using the informal "you" shows how direct and unfiltered their kitchen relationship is.'),
    (8, None, '\'You know, it really is time for me to go.\' Adding that it really is time for her to go fills in the missing piece for Barinov. There is no "you" needed in the Russian here: one short word states the rule for everyone in the room.'),
    (9, None, "'I stopped by to say that the mayor is dissatisfied with you.' Eleonora tells Barinov that she stopped by to say that the mayor is dissatisfied with Barinov without dressing it up."),
    (10, None, '\'And he is removing you from office.\' Since he is removing Barinov from office, Eleonora does not waste words on excuses. Notice how she sticks to the formal "you", keeping a professional line between them.'),
    (11, None, '\'What do you mean removing me, I do not understand?\' By asking what Barinov means removing him he does not understand, the guest presses Barinov for a straight answer. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
]
