# Authoring module for kukhnya-s01e01-scene-01.
ID = 'kukhnya-s01e01-scene-01'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 1
SCENE = 1
TITLE = 'Знакомство в клубе  (Meeting at the Club)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'max': 'Макс', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.01'
SOURCE_FILE = 'sources/kukhnya/s01/e01.ru.dual.srt'
INTRO = 'This is Kukhnya, which simply means "the kitchen": a Russian comedy about a hot-tempered head chef and the cooks and waiters who survive him, in a smart Moscow restaurant called Claude Monet. The first episode starts the night before the new cook turns up. Maksim Lavrov, called Max, has just arrived in the city, and outside a nightclub he steps in to help a woman called Vika and gets punched for his trouble. You\'ll hear their first conversation in Russian before we pick it apart, so don\'t worry about catching every word.'
OPENER = 'Now slowly, one line at a time.'
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'So Max opens the series with a sore nose and a coffee date. If the Russian felt fast, that\'s normal: "u menya" and "u vas", "at me" and "at you", will keep coming back.'
CLOSING = ('max', 'Пока!')
STORY = [
    ('max', 'Девушка, с вами всё в порядке?', 'Miss, are you all right?', [(13, 'Слышь, мужик, ты как сейчас девушку ведёшь')], ''),
    ('vika', 'Да, спасибо за вашу помощь.', 'Yes, thank you for your help.', [], ''),
    ('vika', 'Ой, кажется, у вас сломан нос!', 'Oh, it looks like your nose is broken!', [(15, 'А мне кажется, у меня нос сломан')], ''),
    ('max', 'Мой нос — это мой главный инструмент.', 'My nose is my main instrument.', [(16, 'Это же мой инструмент')], ''),
    ('vika', 'Почему нос так важен для вас?', 'Why is your nose so important to you?', [], ''),
    ('max', 'Завтра у меня важное собеседование на работу.', 'Tomorrow I have an important job interview.', [(14, 'мне просто на собеседование завтра')], ''),
    ('vika', 'Кем вы хотите устроиться на работу?', 'What job do you want to get?', [(17, 'А ты кем устраиваешься')], ''),
    ('max', 'Я хочу работать поваром в ресторане.', 'I want to work as a cook in a restaurant.', [(18, 'поваром в ресторан')], ''),
    ('vika', 'Правда? Я тоже работаю в ресторане!', 'Really? I work in a restaurant too!', [(19, 'А я тоже в ресторане работаю'), (20, 'Да ну? Да')], ''),
    ('max', 'Значит, у нас с тобой много общего.', 'So you and I have a lot in common.', [(21, 'У нас с тобой много общего')], ''),
    ('vika', 'Ты очень милый и смелый парень.', 'You are a very sweet and brave guy.', [], ''),
    ('max', 'Может быть, пойдём выпьем вместе кофе?', 'Maybe we should go drink coffee together?', [], ''),
    ('vika', 'С большим удовольствием, пойдём скорее!', "With great pleasure, let's go quickly!", [], ''),
]
WALK = [
    (0, None, '\'Miss, are you all right?\' Russian has no neat word for "miss". Max calls out "devushka", which is simply "girl", and that\'s what people really say to a young woman they don\'t know. The rest is literally "with you, everything in order?", with the polite "you".'),
    (1, None, '\'Yes, thank you for your help.\' "Spasibo za" works like a little frame: "spasibo", then "za" for "for", then whatever you\'re thankful for. Swap in "kofe" and you\'ve thanked someone for the coffee.'),
    (2, None, '\'Oh, it looks like your nose is broken!\' There\'s no "have" in this sentence. Russian says "u vas", "at you", and then names the thing: at you, a broken nose. This is how Russians say who has something.'),
    (3, None, '\'My nose is my main instrument.\' Nothing in the Russian means "is". In the present tense Russian just leaves it out, and a dash sits in its place. "Eto", "this", is the little helper that holds the sentence together.'),
    (4, None, '\'Why is your nose so important to you?\' "Pochemu" is "why", and "tak" is "so". Vika is still saying "vy", so she keeps her distance from Max. They\'ve only just met.'),
    (5, None, '\'Tomorrow I have an important job interview.\' Same pattern as the nose: "u menya", "at me", is how Max says "I have". The long word for "interview" has "beseda", a chat, hiding in the middle, so it\'s a talk you sit down for.'),
    (6, None, '\'What job do you want to get?\' "Kem" is a special form of "who" that means "as whom". She\'s asking what role he wants, and the answer will have to wear a matching ending.'),
    (7, None, '\'I want to work as a cook in a restaurant.\' Here\'s the matching ending. "Povar" is a cook, and "povarom" is "as a cook". Russian has no word for "a", so the ending does that job. "V restorane" gets its own -e because of the "v", "in".'),
    (8, None, '\'Really? I work in a restaurant too!\' "Pravda" means "truth", so "really?" is literally "truth?". The small word "tozhe", "also", sits right after "I" and you\'ll hear it all day long.'),
    (9, None, '\'So you and I have a lot in common.\' Max has dropped "vy" and says "s toboy", "with you", in the friendly form. "U nas s toboy" is literally "at us with you", which is how Russian says "you and I have".'),
    (10, None, '\'You are a very sweet and brave guy.\' She uses the friendly "you" too. "Paren\'" is the casual word for "guy". "Milyy" is the everyday word for sweet, nice.'),
    (11, None, '\'Maybe we should go drink coffee together?\' "Mozhet byt\'" is "maybe", literally "can be". "Poydyom vypyem" has two verbs side by side, "let\'s go, let\'s drink", and Russian doesn\'t bother with an "and". "Vmeste" is "together".'),
    (12, None, '\'With great pleasure, let\'s go quickly!\' "S bolshim udovolstviem" is how you politely say yes to an invitation, literally "with big pleasure". "Skoreye" is "faster", the word you\'d use to hurry someone along.'),
]
