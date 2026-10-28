# Authoring module for kukhnya-s05e01-scene-04.
ID = 'kukhnya-s05e01-scene-04'
SHOW = 'kukhnya'
SEASON = 5
EPISODE = 1
SCENE = 4
TITLE = 'Мужской разговор и фрау Краус  (Man-to-Man Advice and Frau Kraus)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'denis': 'Денис', 'mikhail': 'Михаил', 'senya': 'Сеня'}
SOURCE_NAME = 'Кухня (Kukhnya) S5.01'
SOURCE_FILE = 'sources/kukhnya/s05/e01.ru.srt'
INTRO = 'While Denis asks Senya how to handle his jealousy over Katya, Chef Barinov pursues Mikhail into the hotel lobby where Mikhail is greeting Frau Kraus. Listen closely to the Russian dialogue.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "And that wraps up the lobby encounter with Frau Kraus. Pay attention to how Russian uses the base form with the indirect form for 'how should I react'. See you next time!"
CLOSING = ('mikhail', 'Хорошего дня!')
STORY = [
    ('denis', 'Давай по дороге обсудим.', "Let's discuss it on the way.", [(50, 'Давай по дороге обсудим')], 'verbatim'),
    ('denis', 'А как мне реагировать?', 'And how should I react?', [(51, 'а как мне реагировать?')], 'verbatim'),
    ('denis', 'Я же её люблю.', 'After all, I love her.', [(51, 'Я же ее люблю')], 'verbatim'),
    ('denis', 'Это нормально ревновать, нет?', 'Is it normal to be jealous, or not?', [(52, 'Это нормально ревновать, нет?')], 'verbatim'),
    ('senya', 'Конечно, это нормально.', 'Of course it is normal.', [(53, 'Конечно, нормально')], 'adapted'),
    ('senya', 'У них ревнуешь — плохо.', 'With them, if you are jealous, it is bad.', [(54, 'У них ревнуешь плохо')], 'verbatim'),
    ('denis', 'И как мне быть?', 'And what should I do?', [(56, 'И как быть?')], 'adapted'),
    ('senya', 'Возьми, подойди к нему.', 'Go ahead and walk up to him.', [(57, 'Возьми, подойди к нему')], 'verbatim'),
    ('mikhail', 'Пойми, Витя, завтра открытие.', 'Understand, Vitya, the opening is tomorrow.', [(60, 'Пойми, Витя, завтра открытие')], 'verbatim'),
    ('mikhail', 'Наш отель должен удивить гостей.', 'Our hotel must surprise the guests.', [(61, 'Наш отель должен удивить гостей')], 'verbatim'),
    ('senya', 'Ресторан наш не трогай.', 'Do not touch our restaurant.', [(63, 'Ресторан не трогай')], 'adapted'),
    ('mikhail', 'Как вы провели эту ночь?', 'How did you spend this night?', [(68, 'Как вы провели эту ночь?')], 'verbatim'),
    ('mikhail', 'О, вижу, что получили.', 'Oh, I see that you received it.', [(71, 'О, вижу, что получили')], 'verbatim'),
    ('mikhail', 'Он только что расстался с другом.', 'He just broke up with his friend.', [(75, 'Он только что расстался')], 'adapted'),
]
WALK = [
    (0, None, '\'Let\'s discuss it on the way.\' Emphasizing the road beside Senya, Denis lands on "doroge" ("road", built on "doroga") to keep the statement grounded.'),
    (1, None, '\'And how should I react?\' Answering readily in front of Senya, Denis puts the question word "kak" right at the start so Senya hears the focus immediately.'),
    (2, None, "'After all, I love her.' Denis counters sharply in their talk, without trying to dress up how he really feels."),
    (3, None, '\'Is it normal to be jealous, or not?\' Denis fires back quietly in front of Senya and lands on "normalno" ("fine, OK") as the key everyday word here.'),
    (4, None, '\'Of course it is normal.\' Senya briskly uses this confirmation in front of Denis using "konechno" ("of course") — spoken with a soft "shn" sound in everyday Moscow Russian to mean "of course, certainly".'),
    (5, None, "'With them, if you are jealous, it is bad.' Senya steps in candidly without a pause, grounding the moment in plain reality."),
    (6, None, '\'And what should I do?\' Leaning in directly during the talk, Denis puts the question word "kak" right at the start so Senya hears the focus immediately.'),
    (7, None, "'Go ahead and walk up to him.' Jumping in dryly right here, spoken Russian compresses the whole thought into just 4 words, skipping the extra helper words English needs."),
    (8, None, "'Understand, Vitya, the opening is tomorrow.' Pointing to the opening on the spot, Mikhail lets Senya see exactly where things stand."),
    (9, None, '\'Our hotel must surprise the guests.\' Touching on his hotel to Senya, Mikhail leans on "dolzhen" ("has to, must") to give the whole sentence its punch.'),
    (10, None, "'Do not touch our restaurant.' Pointing to his restaurant in this beat, spoken Russian compresses the whole thought into just 4 words, skipping the extra helper words English needs."),
    (11, None, "'How did you spend this night?' Mikhail prompts earnestly before Senya can change the subject."),
    (12, None, '\'Oh, I see that you received it.\' Mikhail speaks up briskly right here and puts the weight on "poluchili" ("received", from "poluchit") as the exchange unfolds.'),
    (13, None, '\'He just broke up with his friend.\' Looking over promptly before Senya, the "-sya" ending on "rasstalsya" ("broke up, parted ways") marks an action that unfolds mutually or turns back on the speaker.'),
]
