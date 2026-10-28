# Authoring module for kukhnya-s01e16-scene-06.
ID = 'kukhnya-s01e16-scene-06'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 16
SCENE = 6
TITLE = 'Звонок в инспекцию  (Call to the Inspection)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'senya': 'Сеня'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.16'
SOURCE_FILE = 'sources/kukhnya/s01/e16.ru.dual.srt'
INTRO = 'In the kitchen, Barinov stands at the window with a smug smile. Senya, one of the cooks, asks what is so funny, and the chef points across the courtyard, where inspectors have just turned up at Arcobaleno, the restaurant next door. Listen for who really made the call.'
OPENER = "Let's look closely at the view from the window."
TRANSITION = 'And the whole scene again, as the two of them enjoy it.'
OUTRO = "The rival restaurant is in trouble, and the kitchen at Claude Monet is enjoying every second. When you rewatch, keep an ear out for 'budet' and 'budut', the words for 'will be' that turn up all over the show. See you next time!"
CLOSING = ('barinov', 'Ну, удачи им!')
STORY = [
    ('senya', 'Шеф, чему вы улыбаетесь?', 'Chef, what are you smiling at?', [], ''),
    ('barinov', 'Посмотри во двор на соседний ресторан.', 'Look into the courtyard at the neighboring restaurant.', [], ''),
    ('senya', 'Ого, к ним приехала проверка!', 'Wow, an inspection has come to them!', [], ''),
    ('barinov', 'Да, это миграционная служба.', 'Yes, it is the migration service.', [], ''),
    ('senya', 'Это вы им позвонили?', 'Was it you who called them?', [], ''),
    ('barinov', 'Нет, это Нагиев позвонил.', 'No, it was Nagiyev who called.', [], ''),
    ('senya', 'А что теперь будет?', 'And what will happen now?', [], ''),
    ('barinov', 'Сейчас они побегают!', 'Now they are in for a workout!', [(51, 'Сейчас вы побегаете.')], ''),
    ('senya', 'Елена Павловна будет злиться.', 'Elena Pavlovna will be angry.', [], ''),
    ('barinov', 'Так им и надо.', 'It serves them right.', [], ''),
    ('senya', 'Вот это месть!', 'Now that is revenge!', [], ''),
    ('barinov', 'В следующий раз подумают.', 'Next time they will think twice.', [], ''),
    ('senya', 'Давайте посмотрим в окно!', "Let's watch out the window!", [], ''),
]
WALK = [
    (0, None, "'Chef, what are you smiling at?' You smile 'to' something in Russian, so 'what' becomes 'chemu', 'to what'. 'Ulybaetes' is the polite 'vy' form, from Senya to his boss."),
    (1, None, "'Look into the courtyard at the neighboring restaurant.' 'Vo dvor' means 'into the courtyard': 'v' becomes 'vo' before the cluster 'dv' so it is easier to say."),
    (2, None, "'Wow, an inspection has come to them!' 'Ogo' means 'wow'. 'K nim', 'to them', is 'oni', 'they', after 'k', with an n added at the front."),
    (3, None, "'Yes, it is the migration service.' 'Sluzhba', 'service', is the word in the names of many state bodies; the people behind it are often called simply 'migratsionka'."),
    (4, None, "'Was it you who called them?' Putting 'eto vy' at the front, 'it is you', points at the person. 'Zvonit' takes 'to': you ring 'im', 'to them', not 'them'."),
    (5, None, "'No, it was Nagiyev who called.' The same trick, 'eto' plus a name, now points at Nagiyev. 'Pozvonil', 'called', ends in '-l' because Nagiyev is a man."),
    (6, None, "'And what will happen now?' 'Budet', 'will be', on its own means 'will happen'. 'Chto budet?' is the everyday 'what's going to happen?'"),
    (7, None, "'Now they are in for a workout!' 'Pobegat' is built from 'begat', 'to run about', plus 'po-', 'for a while'. 'Seychas oni pobegayut' is a gleeful threat: they'll be run off their feet."),
    (8, None, "'Elena Pavlovna will be angry.' 'Budet zlitsya' is 'will be' plus 'zlitsya', 'to be angry'. 'Zloy' means 'angry' or 'mean', and the same root is in 'zlost', 'anger'."),
    (9, None, "'It serves them right.' 'Tak im i nado' is a fixed saying, word for word 'so to them and needed'. Learn it whole."),
    (10, None, "'Now that is revenge!' 'Vot eto' in front of a word means 'now that's a real one'. 'Vot eto pashtet!' would be 'now that's a pâté!'"),
    (11, None, "'Next time they will think twice.' 'V sleduyushchiy raz' means 'next time', and it is the partner of 'v proshly raz', 'last time'. 'Podumayut', 'they'll think', needs no 'they' in front."),
    (12, None, "'Let's watch out the window!' 'Davayte' plus 'we' form, 'posmotrim', is the polite way to say 'let's'. With a friend it would be 'davay posmotrim'."),
]
