# Authoring module for kukhnya-s06e02-scene-10.
ID = 'kukhnya-s06e02-scene-10'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 2
SCENE = 10
TITLE = 'Катя отшивает обоих  (Katya Rejects Both of Them)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'denis': 'Денис', 'katya': 'Катя', 'nikita': 'Никита'}
SOURCE_NAME = 'Кухня (Kukhnya) S6.02'
SOURCE_FILE = 'sources/kukhnya/s06/e02.ru.srt'
INTRO = "At the party, Nikita asks to drink with Katya and gets a sarcastic toast about her mother's advice; moments later, Denis tries his luck and gets toasted as a runaway coward."
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'Still unaware that they are both pining for Katya, Nikita and Denis bond over their stubborn girlfriends. See you next time!'
CLOSING = ('denis', 'Пока!')
STORY = [
    ('nikita', 'Катя, я могу с тобой выпить?', 'Katya, may I have a drink with you?', [(160, 'Катя, я могу с тобой выпить?')], 'exact'),
    ('katya', 'Давай за мою маму и за ее мудрые советы.', "Let's drink to my mom and her wise advice.", [(161, 'Давай за мою маму и за ее мудрые советы')], 'exact'),
    ('katya', 'Ведь ты без них никуда, свободен.', 'After all, you are nowhere without them, dismissed.', [(162, 'Ведь ты без них никуда'), (163, 'Свободен')], 'adapted'),
    ('denis', 'Катя, привет.', 'Katya, hi.', [(164, 'Катя. Привет')], 'exact'),
    ('katya', 'Тоже выпить со мной хочешь, да?', 'You want to have a drink with me too, right?', [(165, 'Тоже выпить со мной хочешь, да?')], 'exact'),
    ('katya', 'За тех, которые сбегают, выпьешь?', 'To those who run away, will you drink?', [(167, 'которые сбегают'), (168, 'Выпьешь?')], 'adapted'),
    ('denis', 'Нет, за это не буду.', 'No, I will not drink to that.', [(168, 'Нет')], 'adapted'),
    ('katya', 'А я выпью, у тебя это очень хорошо получается.', 'Well I will drink, you are very good at that.', [(169, 'А я выпью'), (170, 'Ведь у тебя это очень хорошо получается')], 'adapted'),
    ('denis', 'Она права, я виноват.', 'She is right, I am at fault.', [(171, 'Она права, я виноват')], 'exact'),
    ('nikita', 'Это не повод так долго обижаться.', 'That is no reason to stay offended for so long.', [(172, 'не повод так долго обижаться')], 'adapted'),
    ('denis', 'Я не понял, она у нас работает?', 'I do not understand, does she work here with us?', [(174, 'Я не понял, она у нас работает?')], 'exact'),
    ('nikita', 'Моя тоже тут работает.', 'Mine works here too.', [(175, 'Моя тоже')], 'adapted'),
]
WALK = [
    (0, None, '\'Katya, may I have a drink with you?\' Nikita speaks up vividly around Katya and uses "vypit" ("to drink") to carry the main weight of the thought.'),
    (1, None, '\'Let\'s drink to my mom and her wise advice.\' Focusing on the mother in front of Nikita, Katya starts with "davay" ("come on, let\'s") to invite Nikita right into the action.'),
    (2, None, "'After all, you are nowhere without them, dismissed.' Katya steps in right away without a pause, keeping the focus on what actually matters here."),
    (3, None, '\'Katya, hi.\' Denis plainly shares this casual greeting right on cue using "privet" ("hi") — the everyday informal hello used between friends and close coworkers.'),
    (4, None, "'You want to have a drink with me too, right?' Replying firmly beside Denis, Katya keeps normal statement word order here, turning the line into a question for Denis purely through rising pitch."),
    (5, None, "'To those who run away, will you drink?' Katya wonders deadpan why things suddenly took this turn between them."),
    (6, None, "'No, I will not drink to that.' Denis pushes back at once in this moment, before Katya can change the subject."),
    (7, None, '\'Well I will drink, you are very good at that.\' Jumping in firmly around Denis, Katya uses "u tebya" (literally "by you") where English says "you have" or "your".'),
    (8, None, "'She is right, I am at fault.' Denis replies steadily toward Katya, making his position completely clear."),
    (9, None, '\'That is no reason to stay offended for so long.\' Mentioning the reason in the exchange, Nikita leans on "obizhatsya" ("feel offended") to give the whole sentence its punch.'),
    (10, None, "'I do not understand, does she work here with us?' Holding firm plainly during the talk, Denis keeps normal statement word order here, turning the line into a question for Nikita purely through rising pitch."),
    (11, None, "'Mine works here too.' Nikita pushes back steadily without a pause, leaving no doubt about where he stands."),
]
