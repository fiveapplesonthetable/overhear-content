# Authoring module for kukhnya-s01e17-scene-05.
ID = 'kukhnya-s01e17-scene-05'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 17
SCENE = 5
TITLE = 'Сезонное меню  (Seasonal menu)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.17'
SOURCE_FILE = 'sources/kukhnya/s01/e17.ru.dual.srt'
INTRO = 'Vika has given Barinov a deadline for a new seasonal dish, and he has no idea what to cook. So he calls the kitchen together and announces a contest, with a prize for the winner. Max asks the awkward questions. Here is the announcement in Russian.'
OPENER = "Let's take Barinov's announcement one line at a time."
TRANSITION = 'Now the announcement once more, without stopping.'
OUTRO = 'A bonus at the end of the month and no insults until then: that\'s the whole deal. "Srazu" means "right away", and both Max and Barinov lean on it. See you next time!'
CLOSING = ('barinov', 'Всё, до завтра!')
STORY = [
    ('barinov', 'У меня объявление.', 'I have an announcement.', [(63, 'У меня объявление.')], ''),
    ('barinov', 'Нужно сезонное блюдо.', 'We need a seasonal dish.', [(64, 'Для нашего меню нужно сезонное блюдо от шефа.')], ''),
    ('max', 'Шеф, подождите.', 'Chef, wait.', [(65, 'Шеф, шеф, шеф, шеф, шеф, подождите.')], ''),
    ('max', 'Вы же говорили, что не будете придумывать.', "You said you wouldn't come up with it.", [(66, 'Подождите, а вы же говорили, что никогда не будете придумывать сезонных блюд.')], ''),
    ('barinov', 'А я и не буду.', "And I won't be.", [(68, 'А я и не буду.')], ''),
    ('barinov', 'Будете вы.', 'You will.', [(68, 'Будете вы.')], ''),
    ('barinov', 'Победитель получит премию.', 'The winner gets a bonus.', [(69, 'чье блюдо войдет в меню, получит премию,')], ''),
    ('barinov', 'И я не буду называть его инвалидом.', "And I won't call him disabled.", [(70, 'и целую неделю я не буду называть того инвалидом.')], ''),
    ('max', 'А премия сразу?', 'And the bonus is right away?', [(71, 'А премия сразу или в конце месяца?')], ''),
    ('barinov', 'Премия в конце месяца.', 'The bonus is at the end of the month.', [(71, 'Премия в конце месяца.')], ''),
    ('barinov', 'Но инвалидом перестану называть сразу.', "But I'll stop calling you disabled right away.", [(72, 'Но инвалидом перестану называть сразу.')], ''),
    ('max', 'Все поняли. Да, шеф!', 'Everyone understood. Yes, Chef!', [(73, 'Все инвалиды поняли. Да, шеф!')], ''),
]
WALK = [
    (0, None, '\'I have an announcement.\' "U menya", literally "at me", is how Russian says "I have". "Obyavlenie" is the announcement itself.'),
    (1, None, '\'We need a seasonal dish.\' "Nuzhno blyudo" is literally "needed, a dish". There\'s no "we" at all, just the thing that\'s needed.'),
    (2, None, '\'Chef, wait.\' "Podozhdite" is the polite command, with "-ite" for "vy". A friend would just hear "podozhdi".'),
    (3, None, '\'But you said you wouldn\'t be the one coming up with it.\' "Zhe" adds a tone of "but you did say!". "Ne budete pridumyvat" is "budete", you will, plus the plain form of "come up with".'),
    (4, None, '\'And I won\'t.\' "A ya i ne budu" is literally "and I also won\'t be": the little "i" here means "indeed".'),
    (5, None, '\'You will.\' "Budete vy" puts "vy" last, which is where Russian puts the word it wants to stress.'),
    (6, None, '\'The winner gets a bonus.\' "Premiya" is a bonus at work, and it turns into "premiyu" as the thing received. "Pobeditel", winner, comes from "pobeda", victory.'),
    (7, None, '\'And I won\'t call him a cripple.\' Barinov\'s favourite insult is "invalid", and after "nazyvat", to call someone something, it picks up "-om": "invalidom".'),
    (8, None, '\'And is the bonus right away?\' Max starts with "a", and, which turns it into a follow-up question. "Srazu" means "right away".'),
    (9, None, '\'The bonus comes at the end of the month.\' "V kontse mesyatsa": "konets", end, becomes "kontse", and "mesyats", month, becomes "mesyatsa".'),
    (10, None, '\'But I\'ll stop calling you a cripple right away.\' "Perestanu" is "I\'ll stop", and the plain "nazyvat" follows it. "Srazu" comes back as the punchline.'),
    (11, None, '\'Everyone got it? Yes, chef!\' "Vse ponyali" is literally "all understood", and "Da, shef!" is the kitchen\'s standard reply.'),
]
