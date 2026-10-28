# Authoring module for kukhnya-s01e02-scene-18.
ID = 'kukhnya-s01e02-scene-18'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 2
SCENE = 18
TITLE = 'Матч на кухне  (Match in the Kitchen)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'senya': 'Сеня'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.02'
SOURCE_FILE = 'sources/kukhnya/s01/e02.ru.dual.srt'
INTRO = "Chef Viktor is in his office, glued to the television. It's the big Moscow derby, his beloved Spartak against CSKA, and the cook Senya wants to know when dinner service starts. The chef doesn't want to hear about food. Here's the Russian first."
OPENER = "Let's run through the match."
TRANSITION = "Now let's listen to the conversation again without interruption."
OUTRO = 'Barinov would rather watch Spartak than cook. Keep "pora", "it\'s time", which Senya used twice to get him back to the stove.'
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('senya', 'Шеф, пора начинать готовить горячие блюда?', 'Chef, is it time to start preparing hot dishes?', [], ''),
    ('barinov', 'Тихо, Сеня! Сейчас идёт решающий матч!', 'Quiet, Senya! A decisive match is on right now!', [], ''),
    ('senya', 'Кто сегодня играет на этом матче?', 'Who is playing in this match today?', [], ''),
    ('barinov', 'Наш великий Спартак играет против ЦСКА!', 'Our great Spartak is playing against CSKA!', [], ''),
    ('senya', 'И какой сейчас счёт в игре?', 'And what is the score in the game now?', [], ''),
    ('barinov', 'Пока ничья, но мы должны победить!', 'A draw so far, but we must win!', [], ''),
    ('senya', 'Смотрите, мяч летит к их воротам!', 'Look, the ball is flying toward their goal!', [], ''),
    ('barinov', 'У чужой штрафной площади ЦСКА держит оборону.', 'Near the opponent penalty area CSKA is holding defense.', [(209, 'держит оборону')], ''),
    ('senya', 'Нападающий Спартака получает быстрый пас.', 'The Spartak forward receives a fast pass.', [], ''),
    ('barinov', 'Давай, Ари с мячом сильно бьёт!', 'Come on, Ari with the ball shoots hard!', [(210, 'бьет')], ''),
    ('senya', 'Вратарь с трудом ловит этот мяч.', 'The goalkeeper catches this ball with difficulty.', [], ''),
    ('barinov', 'Какой опасный и красивый был момент!', 'What a dangerous and beautiful moment it was!', [], ''),
    ('senya', 'А теперь пора вернуться к нашей кухне.', 'And now it is time to return to our kitchen.', [], ''),
]
WALK = [
    (0, None, '\'Chef, is it time to start preparing hot dishes?\' "Pora" is "it\'s time", and it takes the plain "nachinat\'", to start. In "goryachiye blyuda", hot dishes, "blyudo" becomes "blyuda" for more than one.'),
    (1, None, '\'Quiet, Senya! A decisive match is on right now!\' "Tikho" is "quiet". In Russian a match "idyot", goes, and "reshayushchiy", decisive, is the match that "reshayet", decides, it all.'),
    (2, None, '\'Who is playing in this match today?\' "Igrayet", plays, is the everyday verb for games. "Na etom matche" puts an -e on "match".'),
    (3, None, '\'Our great Spartak is playing against CSKA!\' "Protiv" is "against". "Velikiy" is the grand word for "great", and "nash", our, shows the chef is a fan.'),
    (4, None, '\'And what is the score in the game now?\' "Schyot", score, is also the restaurant bill, as in "schyot, pozhaluysta". "V igre" is "in the game".'),
    (5, None, '\'A draw so far, but we must win!\' "Nich\'ya", a draw, is literally "nobody\'s". "Poka", so far, is the same word as "bye", and "dolzhny pobedit\'" is "must win".'),
    (6, None, '\'Look, the ball is flying toward their goal!\' "Vorota", goal, is always plural, because it\'s really "gates". "Letit" is "flies".'),
    (7, None, '\'Near the opponent penalty area CSKA is holding defense.\' "Shtrafnaya ploshchad\'" is the penalty area, and "ploshchad\'" is also a town square. "Derzhit oboronu" is "holds the defence".'),
    (8, None, '\'The Spartak forward receives a fast pass.\' "Napadayushchiy", forward, is "the attacking one", from "napadat\'". "Poluchayet" is "receives", and "pas" is borrowed from English.'),
    (9, None, '\'Come on, Ari with the ball shoots hard!\' "Davay" is a friendly "come on!". "S myachom", with the ball, ends in -om, and "b\'yot", hits, is how Russians describe a shot.'),
    (10, None, '\'The goalkeeper catches this ball with difficulty.\' "Vratar\'" is the goalkeeper, from "vorota", the goal: the gatekeeper. "With difficulty" is literally "with labour".'),
    (11, None, '\'What a dangerous and beautiful moment it was!\' "Kakoy" begins the exclamation, "what a". "Byl", was, is masculine because "moment" is.'),
    (12, None, '\'And now it is time to return to our kitchen.\' "Pora" again, now with "vernut\'sya", to return. In "k nashey kukhne", "k" changes both words.'),
]
