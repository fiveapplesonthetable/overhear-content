# Authoring module for kukhnya-s06e03-scene-04.
ID = 'kukhnya-s06e03-scene-04'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 3
SCENE = 4
TITLE = 'Вызов на футбольный матч  (Challenge to a Football Match)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'denis': 'Денис', 'nagiyev': 'Нагиев', 'nikita': 'Никита'}
SOURCE_NAME = 'Кухня (Kukhnya) S6.03'
SOURCE_FILE = 'sources/kukhnya/s06/e03.ru.srt'
INTRO = 'Back in the hotel courtyard, Nikita tells Denis he might as well go home since Nagiyev is filming all day, and the bored chefs challenge the waiters to a game of football.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "Stung by Nikita's taunt in front of Katya, Denis joins the football match while disaster strikes on Nagiyev's film set inside. See you next time!"
CLOSING = ('denis', 'До свидания!')
STORY = [
    ('nikita', 'Нагиев сегодня кино снимает.', 'Nagiyev is filming a movie today.', [(58, 'Нагиев кино снимает')], 'adapted'),
    ('nikita', 'Работы не будет, можешь идти домой.', 'There will be no work, you can go home.', [(59, 'не будет. Так что можешь домой')], 'adapted'),
    ('denis', 'Тебя забыл спросить.', 'I forgot to ask you.', [(60, 'Тебя забыл спросить')], 'exact'),
    ('denis', 'Да сколько можно?', 'How much longer can this go on?', [(62, 'Сколько можно')], 'adapted'),
    ('nagiyev', 'Извините, мы нечаянно.', 'Sorry, we did it accidentally.', [(63, 'Извините, мы нечаянно')], 'exact'),
    ('nagiyev', 'Слушай, кино Нагиева, и канализация засорилась.', "Listen, Nagiyev's movie is here, and the plumbing got clogged.", [(64, 'кино Нагиева и канализация засорилась')], 'adapted'),
    ('nagiyev', 'Не думаю, что это просто так.', 'I do not think that is a coincidence.', [(65, 'Не думаю')], 'adapted'),
    ('nagiyev', 'Я тут подумал, может, в футбол сыграем?', 'I was just thinking, maybe we should play football?', [(66, 'я тут подумал'), (67, 'может, в футбол сыграем?')], 'adapted'),
    ('denis', 'Не хочу я играть.', 'I do not want to play.', [(68, 'Не хочу')], 'adapted'),
    ('nikita', 'Да он просто испугался.', 'Why, he just got scared.', [(69, 'Да он просто испугался')], 'exact'),
    ('denis', 'Ладно, давай сыграем.', "Fine, let's play.", [(70, 'Давай, сыграем')], 'adapted'),
    ('nagiyev', 'А подайте мяч, пожалуйста.', 'Pass the ball, please.', [(71, 'А подайте мяч, пожалуйста')], 'exact'),
]
WALK = [
    (0, None, '\'Nagiyev is filming a movie today.\' Touching on the cinema in this beat, Nikita puts the emphasis on "segodnya" ("today") in the middle of the talk.'),
    (1, None, '\'There will be no work, you can go home.\' Mentioning the work with Denis, Nikita brings in "raboty" ("of work", from "rabota") as the key Russian word here.'),
    (2, None, "'I forgot to ask you.' Denis weighs in bluntly beside Nikita, to clear the air between them once and for all."),
    (3, None, '\'How much longer can this go on?\' Denis speaks up openly in front of Nagiyev and uses "mozhno" ("may, can") to carry the main weight of the thought.'),
    (4, None, '\'Sorry, we did it accidentally.\' Nagiyev warmly sends this polite apology beside Denis using "izvinite" ("excuse me") — the respectful form of "excuse me" or "sorry" used when stepping in or apologizing.'),
    (5, None, "'Listen, Nagiyev's movie is here, and the plumbing got clogged.' Nagiyev cuts in earnestly around Denis, so Denis knows he is not just making small talk."),
    (6, None, '\'I do not think that is a coincidence.\' Nagiyev counters smoothly at once and lands on "dumayu" ("I think", built on "dumat") to keep the statement grounded.'),
    (7, None, "'I was just thinking, maybe we should play football?' Mentioning the football around Denis, Nagiyev keeps normal statement word order here, turning the line into a question for Denis purely through rising pitch."),
    (8, None, "'I do not want to play.' Denis answers earnestly with Nagiyev, refusing to let the moment slip past."),
    (9, None, '\'Why, he just got scared.\' Nikita reacts calmly at once and uses "ispugalsya" ("got scared", from "ispugatsya") to make the point stick.'),
    (10, None, '\'Fine, let\'s play.\' Meeting Nikita warmly at this moment, Denis says "ladno" ("alright"), built from the old Russian root for harmony and order, used every day for "okay, fine".'),
    (11, None, '\'Pass the ball, please.\' Nagiyev quietly drops this courtesy word while facing Denis using "pozhaluysta" ("please") — the all-purpose Russian politeness word that covers both "please" and "you\'re welcome".'),
]
