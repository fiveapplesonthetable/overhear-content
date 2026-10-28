# Authoring module for kukhnya-s03e20-scene-01.
ID = 'kukhnya-s03e20-scene-01'
SHOW = 'kukhnya'
SEASON = 3
EPISODE = 20
SCENE = 1
TITLE = 'Всадник и падение с лошади  (The Horseman and Falling off the Horse)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'max': 'Макс', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S3.20'
SOURCE_FILE = 'sources/kukhnya/s03/e20.ru.srt'
INTRO = 'Welcome to Episode Twenty, the Season Three finale. Desperate to win Vika back, Max rides into the courtyard on a white horse to propose—gets thrown off when she refuses, and wakes up in the hospital claiming he lost two years of memory!'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'Vika stares at Max in disbelief as he claims to remember nothing after their very first morning together two years ago. Until next time!'
CLOSING = ('max', 'До завтра!')
STORY = [
    ('max', 'Вика, выходи, пожалуйста, за меня замуж!', 'Vika, please marry me!', [(1, 'Выходи за меня замуж')], 'adapted'),
    ('vika', 'Макс, ты зачем вообще на лошадь залез?', 'Max, why on earth did you climb onto a horse?', [(1, 'Ты зачем на лошадь залез')], 'adapted'),
    ('max', 'Вика, с самого первого дня нашей встречи!', 'Vika, from the very first day of our meeting!', [(2, 'с самого первого дня нашей встречи')], 'adapted'),
    ('vika', 'Макс, можешь не продолжать, мой ответ нет!', 'Max, you need not continue, my answer is no!', [(4, 'Макс, можешь не продолжать'), (5, 'Мой ответ нет')], 'adapted'),
    ('max', 'Почему нет? Вика, постой, пожалуйста!', 'Why no? Vika, wait, please!', [(6, 'Почему'), (7, 'постой')], 'adapted'),
    ('max', 'Подождите, а как я вообще здесь оказался?', 'Wait a second, how on earth did I end up here?', [(8, 'Как я здесь оказался')], 'adapted'),
    ('vika', 'Ты только что сильно упал с лошади.', 'You just fell hard off a horse.', [(9, 'Ты упал с лошади')], 'adapted'),
    ('vika', 'У тебя сейчас сильно болит голова?', 'Does your head hurt badly right now?', [(11, 'Болит голова')], 'adapted'),
    ('max', 'Вика, прости, что я сбежал от тебя утром.', 'Vika, forgive me for running away from you in the morning.', [(12, 'Вика, прости меня'), (13, 'за то, что я сбежал от тебя утром')], 'adapted'),
    ('max', 'Я просто сегодня утром на собеседование опоздал.', 'I was just late for a job interview this morning.', [(14, 'Я просто на собеседование опоздал')], 'adapted'),
    ('vika', 'Куда ты сбежал? На какое ещё собеседование?', 'Where did you run away to? To what job interview?', [(15, 'Куда сбежал'), (15, 'собеседование')], 'adapted'),
    ('max', 'Когда я с квартиры сбежал, ты вазу разбила.', 'When I ran out of the apartment, you smashed a vase.', [(19, 'Когда я с квартиры сбежал, ты еще в вазу разбила')], 'adapted'),
    ('max', 'Я помню, как мы познакомились в клубе.', 'I remember how we met at the club.', [(21, 'Я помню, как мы познакомились в клубе')], 'adapted'),
    ('max', 'Я переночевал у тебя и побежал устраиваться на работу.', 'I spent the night at your place and ran off to apply for a job.', [(22, 'Я переночевал у тебя, а потом побежал устраиваться на работу')], 'adapted'),
]
WALK = [
    (0, None, '\'Vika, please marry me!\' Max pushes back boldly in this beat and puts the weight on "vykhodi" ("go out, marry", from "vykhodit") as the exchange unfolds.'),
    (1, None, '\'Max, why on earth did you climb onto a horse?\' Pointing to a horse around Max, Vika drops in "voobshche" ("in general, altogether") to sum up the whole situation at once.'),
    (2, None, "'Vika, from the very first day of our meeting!' Max speaks bluntly hearing Vika, making his position completely clear."),
    (3, None, '\'Max, you need not continue, my answer is no!\' Focusing on her answer around Max, Vika uses "prodolzhat" ("to continue") to carry the main weight of the thought.'),
    (4, None, '\'Why no? Vika, wait, please!\' Pressing on plainly with Vika, Max puts the question word "pochemu" right at the start so Vika hears the focus immediately.'),
    (5, None, "'Wait a second, how on earth did I end up here?' Max prompts plainly to see how Vika will answer on the spot."),
    (6, None, '\'You just fell hard off a horse.\' Touching on a horse in this beat, Vika reaches for the Russian word "loshadi" ("from the horse", built from "loshad") right at the center of the line.'),
    (7, None, '\'Does your head hurt badly right now?\' Talking about the head before Max, Vika uses "u tebya" (literally "by you") where English says "you have" or "your".'),
    (8, None, "'Vika, forgive me for running away from you in the morning.' Max speaks openly with a shrug, without trying to dress up how he really feels."),
    (9, None, '\'I was just late for a job interview this morning.\' Underscoring a job interview during the talk, Max lands on "sobesedovaniye" ("interview") as the key everyday word here.'),
    (10, None, '\'Where did you run away to? To what job interview?\' Stepping in earnestly on the spot, Vika puts the question word "kuda" right at the start so Max hears the focus immediately.'),
    (11, None, "'When I ran out of the apartment, you smashed a vase.' Max follows up frankly without a pause, leaving no doubt about where he stands."),
    (12, None, '\'I remember how we met at the club.\' Focusing on the club at once, Max chooses "poznakomilis" ("met", from the root "poznakomitsya") so Vika hears the exact meaning.'),
    (13, None, '\'I spent the night at your place and ran off to apply for a job.\' Addressing a job right here, Max uses "u tebya" (literally "by you") where English says "you have" or "your".'),
]
