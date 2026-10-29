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
OUTRO = 'So Max opens the series with a sore nose and a coffee date. If the Russian felt fast, that\'s normal: "u menya" and "u vas", "at me" and "at you", will keep coming back, and they\'ll soon feel easy. See you next time.'
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
    (0, None, '\'Miss, are you all right?\' Russian has no neat word for "miss". Max calls out "devushka", literally "girl", and that\'s really what people say to a young woman they don\'t know. The rest is "with you, everything in order?", with the polite "vy" you use for a stranger.'),
    (1, None, '\'Yes, thank you for your help.\' "Spasibo za" is a frame you can reuse: "spasibo", then "za", "for", then whatever you\'re thankful for. "Spasibo za kofe" thanks someone for the coffee.'),
    (2, None, '\'Oh, it looks like your nose is broken!\' There\'s no "have" in this sentence. Russian says "u vas", "at you", and then names the thing: at you, a broken nose. That little "u" is how Russians say who has something, and you\'ll hear it all through this scene.'),
    (3, None, '\'My nose is my main instrument.\' Nothing in the Russian means "is". In the present tense Russian simply leaves it out, and "eto", "this", often fills the gap: "my nose, this is my main instrument".'),
    (4, None, '\'Why is your nose so important to you?\' The short "vazhen" is the form of "vazhnyy", important, that you use after the thing you\'re describing: the nose, so important. "Dlya vas", "for you", keeps the polite "you": Vika is still keeping a stranger at arm\'s length.'),
    (5, None, '\'Tomorrow I have an important job interview.\' Same pattern as the nose: "u menya", "at me", is how Max says "I have". The long word for "interview", "sobesedovaniye", has "beseda", a talk, hiding inside it.'),
    (6, None, '\'What job do you want to get?\' "Kem" is a form of "kto", "who", that means "as whom". So Vika literally asks "as whom do you want to get a job?", and the answer has to come back in the same "as" form.'),
    (7, None, '\'I want to work as a cook in a restaurant.\' Here\'s that answer. "Povar" is a cook, and "povarom" is "as a cook": the "-om" ending does the job of English "as". "V restorane", "in a restaurant", adds an -e to "restoran" after "v".'),
    (8, None, '\'Really? I work in a restaurant too!\' "Pravda" means "truth", so her "really?" is, word for word, "truth?". "Tozhe", "too", is a word you\'ll hear all day: "ya tozhe" is "me too".'),
    (9, None, '\'So you and I have a lot in common.\' Max switches from the polite "vy" to the friendly "ty" here. "U nas s toboy" is "at us with you", the friendly way to say "you and I have", and "mnogo obshchego" is "a lot in common".'),
    (10, None, '\'You are a very sweet and brave guy.\' Now Vika says "ty" as well. "Paren\'" is the casual word for a guy, and "milyy" is the everyday word for sweet or nice.'),
    (11, None, '\'Maybe we should go drink coffee together?\' "Mozhet byt\'" is "maybe", literally "can be". Then come two verbs side by side, "poydyom, vypyem", "let\'s go, let\'s drink", with no "and" between them. That\'s a very common way to suggest doing something together.'),
    (12, None, '\'With great pleasure, let\'s go quickly!\' "S bol\'shim udovol\'stviyem", "with great pleasure", is the warm way to accept an invitation. "Skoreye" means "quicker", and on its own it\'s how you hurry someone along.'),
]
