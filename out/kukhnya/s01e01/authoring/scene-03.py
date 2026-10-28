# Authoring module for kukhnya-s01e01-scene-03.
ID = 'kukhnya-s01e01-scene-03'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 1
SCENE = 3
TITLE = 'Ночной разговор  (Night Conversation)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'max': 'Макс', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.01'
SOURCE_FILE = 'sources/kukhnya/s01/e01.ru.dual.srt'
INTRO = "It's late now, and Max and Vika are lying awake in the dark, talking quietly. She asks whether he really loves cooking, and he tells her what food means to him. Here's the conversation in Russian first."
OPENER = "Let's look at the pieces."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'Quiet, warm talk like this is full of words you can reuse, and "good night" is the one to keep. In the morning the mood changes completely.'
CLOSING = ('max', 'Пока!')
STORY = [
    ('vika', 'Макс, ты уже почти засыпаешь?', 'Max, are you almost falling asleep?', [], ''),
    ('max', 'Нет, я просто любуюсь тобой.', 'No, I am simply admiring you.', [], ''),
    ('vika', 'Ты правда так сильно любишь готовить?', 'Do you really love cooking so much?', [], ''),
    ('max', 'Еда — это настоящая любовь и страсть!', 'Food is true love and passion!', [(23, 'это')], ''),
    ('vika', 'Ты говоришь о еде как поэт.', 'You speak about food like a poet.', [], ''),
    ('max', 'Хорошая еда дарит людям огромное счастье.', 'Good food gives people immense happiness.', [], ''),
    ('vika', 'В каком ресторане у тебя собеседование?', 'At which restaurant is your interview?', [], ''),
    ('max', 'В самом лучшем французском ресторане Москвы.', 'In the very best French restaurant in Moscow.', [], ''),
    ('vika', 'Наш город полон удивительных совпадений.', 'Our city is full of surprising coincidences.', [], ''),
    ('max', 'Я рад, что встретил тебя сегодня.', 'I am glad that I met you today.', [], ''),
    ('vika', 'Ложись спать, тебе надо хорошо отдохнуть.', 'Go to sleep, you need to rest well.', [], ''),
    ('max', 'Спокойной ночи, прекрасная Вика.', 'Good night, beautiful Vika.', [], ''),
    ('vika', 'Спокойной ночи, мой храбрый повар.', 'Good night, my brave cook.', [], ''),
]
WALK = [
    (0, None, '\'Max, are you almost falling asleep?\' "Zasypayesh\'" is built from "son", sleep, plus a prefix meaning "start", so it\'s "starting to sleep". Her "pochti", "almost", makes the question teasing.'),
    (1, None, '\'No, I am simply admiring you.\' "Lyubuyus\'" is "I enjoy looking at", and what you look at has to change shape: "ty" turns into "toboy". The "-s\'" on the end is a little "self", a piece Russian attaches to many verbs.'),
    (2, None, '\'Do you really love cooking so much?\' "Lyubish\' gotovit\'" is "you love to cook": two words and no "to" between them. "Pravda", "truth", is doing the work of "really" again.'),
    (3, None, '\'Food is true love and passion!\' The dash is standing in for "is". "Lyubov\'" is "love", related to "lyublyu", "I love", and "nastoyashchaya" means "real" or "genuine".'),
    (4, None, '\'You speak about food like a poet.\' "O yede" is "about food", and "yeda" gets an -e after "o". "Kak poet" is "like a poet", and as you can see "poet" looks just like English.'),
    (5, None, '\'Good food gives people immense happiness.\' "Darit" means "gives", and it grows from "dar", a gift, so good food literally hands out a gift. "Lyudyam" is "to people": "lyudi" is irregular, and this is its "to" form.'),
    (6, None, '\'At which restaurant is your interview?\' "U tebya", "at you", is the friendly twin of "u vas". "V kakom restorane" is "in which restaurant", and both "kakom" and "restorane" change their endings after "v".'),
    (7, None, '\'In the very best French restaurant in Moscow.\' "Samom luchshem" is the "very best" again, with the "in" ending. "Moskvy" is "of Moscow", so the name drops its -a and takes -y.'),
    (8, None, '\'Our city is full of surprising coincidences.\' "Sovpadeniye" is a coincidence, and it\'s built from "so-", together, and "padat\'", to fall: things that fall together. "Polon" is "full of", and a woman would say "polna".'),
    (9, None, '\'I am glad that I met you today.\' A man says "rad", and a woman says "rada". "Vstretil" ends in -l because Max is a man. Past tense in Russian wears the speaker\'s gender.'),
    (10, None, '\'Go to sleep, you need to rest well.\' "Lozhis\' spat\'" is "lie down to sleep". "Tebe nado", "to you necessary", is just like "mne nuzhna" from the bar: the one who needs gets the "to" form.'),
    (11, None, '\'Good night, beautiful Vika.\' "Spokoynoy nochi" is literally "of a quiet night", with "I wish you" left out. It\'s a ready-made phrase, so you can just say it.'),
    (12, None, '\'Good night, my brave cook.\' Vika has another word for brave: "khrabryy", a touch more heroic than the "smelyy" she used earlier. Russian often has several words for a quality.'),
]
