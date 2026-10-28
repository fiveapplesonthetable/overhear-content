# Authoring module for kukhnya-s01e06-scene-19.
ID = 'kukhnya-s01e06-scene-19'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 6
SCENE = 19
TITLE = 'Заказ на трюфели  (The Truffle Order)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'max': 'Макс', 'nastya': 'Настя'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.06'
SOURCE_FILE = 'sources/kukhnya/s01/e06.ru.dual.srt'
INTRO = "In the kitchen at Claude Monet, Barinov needs a truffle for table seven, and Max knows exactly where the truffles are not: they went out with the rubbish. He grabs Nastya, the waitress, and begs her to talk the guest out of it. It's in Russian first."
OPENER = "Let's replay it. Barinov shouts, Max panics, and Nastya keeps her head."
TRANSITION = 'And now the panic over the truffle, straight through.'
OUTRO = 'Max gave you "mne nuzhna pomoshch", I need help, and "skazhi gostyu", tell the guest, and Nastya gave you "ne mogu", I can\'t. Useful when you\'re covering up a mistake. See you next time.'
CLOSING = ('max', 'Пока!')
STORY = [
    ('barinov', 'Огузок, тащи сюда скорее один трюфель!', 'Rump, bring one truffle here quickly!', [(238, 'Агузок, тащи сюда один трюфель')], ''),
    ('barinov', 'Седьмой столик заказал салат с трюфелями.', 'Table seven ordered a salad with truffles.', [(237, 'салат с трюфелями за седьмой столик')], ''),
    ('max', 'Шеф, я сейчас всё быстро принесу.', 'Chef, I will bring everything quickly now.', [], ''),
    ('max', 'Настя, стой, мне срочно нужна помощь!', 'Nastya, stop, I urgently need help!', [(239, 'Слушай, Настя')], ''),
    ('nastya', 'Что случилось, Макс? Что такое?', 'What happened, Max? What is it?', [], ''),
    ('max', 'Скажи гостю, что трюфели сегодня плохие.', 'Tell the guest that the truffles are bad today.', [(239, 'трюфеля сегодня не очень')], ''),
    ('max', 'Пусть он закажет любое другое блюдо!', 'Let him order any other dish!', [(240, 'что-нибудь другое заказали')], ''),
    ('nastya', 'Нет, я не могу так сказать.', 'No, I cannot say that.', [(241, 'Не, не могу')], ''),
    ('nastya', 'Гость пришёл специально ради этого салата.', 'The guest came especially for this salad.', [(241, 'пришел сюда специально ради этого блюда')], ''),
    ('max', 'Но у меня нет этого трюфеля!', 'But I do not have this truffle!', [], ''),
    ('nastya', 'Он очень строгий и важный человек.', 'He is a very strict and important person.', [], ''),
    ('nastya', 'Кстати, он просил передать тебе записку.', 'By the way, he asked to give you a note.', [(242, 'просил тебе вот это передать')], ''),
    ('max', 'О нет, это катастрофа для кухни!', 'Oh no, this is a disaster for the kitchen!', [], ''),
    ('nastya', 'Торопись, шеф уже очень сильно злится.', 'Hurry, the chef is already getting very angry.', [], ''),
]
WALK = [
    (0, None, '\'Rump, bring one truffle here quickly!\' Oguzok, rump, is a cut of beef and Barinov\'s rude nickname for Max. "Tashchi", haul it, is a rougher word than "nesi".'),
    (1, None, '\'Table seven ordered a salad with truffles.\' Russians number tables with "sedmoy", seventh, so it\'s \'the seventh table\'. "S tryufelyami", with truffles, has -ami after s.'),
    (2, None, '\'Chef, I will bring everything quickly now.\' "Prinesu", I\'ll bring, is pri-, here, plus "nesti", carry. It\'s a future form, so it\'s a promise.'),
    (3, None, '\'Nastya, stop, I urgently need help!\' "Stoy", stop, is the order form of "stoyat", to stand, so it\'s literally \'stand still\'. "Pomoshch", help, is feminine, which is why it\'s "nuzhna" with -a.'),
    (4, None, '\'What happened, Max? What is it?\' "Chto sluchilos" is the standard \'what happened?\'. "Chto takoe", \'what\'s up?\', is said with a worried rise.'),
    (5, None, '\'Tell the guest that the truffles are bad today.\' "Gost", guest, becomes "gostyu", \'to the guest\', the one being told. "Plokhie", bad, has the plural -ie for "tryufeli".'),
    (6, None, '\'Let him order any other dish!\' "Pust", let, plus a future verb is how you say \'let him do it\'. "Lyuboe", any, ends in -oe to match "blyudo".'),
    (7, None, '\'No, I cannot say that.\' "Ne mogu", I can\'t, is from "moch", can. "Tak skazat", \'say so\', is how you\'d say \'say that\' here.'),
    (8, None, '\'The guest came especially for this salad.\' "Radi", for the sake of, changes "salat" to "salata". "Spetsialno" is easy: \'specially\'.'),
    (9, None, '\'But I do not have this truffle!\' After "net", "etot tryufel" becomes "etogo tryufelya", both words changing. That\'s what "u menya net" always does to the missing thing.'),
    (10, None, '\'He is a very strict and important person.\' "Chelovek", person, is masculine, but Russians use it for women too. "Strogiy", strict, is the same word as in "strogo", strictly.'),
    (11, None, '\'By the way, he asked to give you a note.\' "Kstati", by the way, is how Russians change the subject. "Peredat", to pass on, is what you do with a note or a message.'),
    (12, None, '\'Oh no, this is a disaster for the kitchen!\' "Katastrofa" sounds just like it looks. "Dlya kukhni", for the kitchen, changes "kukhnya" to "kukhni".'),
    (13, None, '\'Hurry, the chef is already getting very angry.\' "Toropis", hurry, ends in -s, the short form of -sya. "Zlitsya", to be angry, is from "zloy", angry, with -sya on the end.'),
]
