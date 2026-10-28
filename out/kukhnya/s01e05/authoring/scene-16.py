# Authoring module for kukhnya-s01e05-scene-16.
ID = 'kukhnya-s01e05-scene-16'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 5
SCENE = 16
TITLE = 'Укромный уголок  (A Secluded Corner)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kostya': 'Костя', 'nastya': 'Настя'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.05'
SOURCE_FILE = 'sources/kukhnya/s01/e05.ru.dual.srt'
INTRO = 'Back at Claude Monet, Nastya the waitress leads Kostya, the bartender, into a quiet corner of the storeroom. She needs his help with a plan, and nobody else can hear it. Listen in Russian first.'
OPENER = "Let's slow it down. Nastya whispers, Kostya is curious, and the lines stay short."
TRANSITION = 'Once more, all the way through.'
OUTRO = 'Hold on to "obeshchayu", \'I promise\', and "ya ves vo vnimanii", \'I\'m all ears\'. Kostya still has no idea what he\'s just agreed to.'
CLOSING = ('nastya', 'Пока!')
STORY = [
    ('nastya', 'Всё, тут нам никто не помешает.', 'There, nobody will bother us here.', [(207, 'никто не помешает')], ''),
    ('kostya', 'Настя, зачем мы сюда пришли?', 'Nastya, why did we come here?', [], ''),
    ('nastya', 'Нам нужно тихо поговорить без свидетелей.', 'We need to talk quietly without witnesses.', [], ''),
    ('kostya', 'Здесь действительно очень тихо и спокойно.', 'It is indeed very quiet and peaceful here.', [], ''),
    ('nastya', 'Ты готов мне немного помочь?', 'Are you ready to help me a little?', [], ''),
    ('kostya', 'Конечно, я всегда рад помочь тебе.', 'Of course, I am always glad to help you.', [], ''),
    ('nastya', 'Только пообещай никому ничего не рассказывать.', 'Only promise not to tell anyone anything.', [], ''),
    ('kostya', 'Обещаю, это будет наша общая тайна.', 'I promise, this will be our shared secret.', [], ''),
    ('nastya', 'Отлично, тогда слушай меня очень внимательно.', 'Great, then listen to me very carefully.', [], ''),
    ('kostya', 'Я весь во внимании, говори скорее.', 'I am all ears, speak quickly.', [], ''),
    ('nastya', 'Мы разыграем один очень хитрый спектакль!', 'We will play out a very clever show!', [], ''),
    ('kostya', 'Ну да, я пока ничего не понимаю.', 'Well yeah, I do not understand anything yet.', [(208, 'Ну да')], ''),
    ('nastya', 'Скоро ты сам всё отлично поймёшь!', 'Soon you will understand everything perfectly yourself!', [], ''),
]
WALK = [
    (0, None, '\'There, nobody will bother us here.\' "Vsyo" here means \'right, that\'s it\', not \'everything\'. "Nikto ne pomeshaet" keeps the "ne" even with "nikto", \'nobody\'.'),
    (1, None, '\'Nastya, why did we come here?\' "Zachem" asks about the purpose, \'what for\'. "Syuda" is \'here\' in the sense of \'to here\', for movement, and "prishli" is \'came\' on foot.'),
    (2, None, '\'We need to talk quietly without witnesses.\' "Nam nuzhno" is literally \'to us it\'s needed\'. "Bez", \'without\', turns "svideteli", \'witnesses\', into "bez svideteley".'),
    (3, None, '\'It is indeed very quiet and peaceful here.\' There\'s no \'is\' in the Russian, just "zdes ochen tikho i spokoyno". "Tikho" and "spokoyno" end in -o, the form for \'it\'s quiet\' and \'it\'s calm\'.'),
    (4, None, '\'Are you ready to help me a little?\' "Gotov", \'ready\', has no ending because it\'s said to a man; to Nastya it would be "gotova". "Pomoch" takes \'to me\', "mne", as if you give help to someone.'),
    (5, None, '\'Of course, I am always glad to help you.\' A man says "rad", a woman "rada". "Pomoch tebe", \'to help you\', mirrors Nastya\'s "pomoch mne".'),
    (6, None, '\'Only promise not to tell anyone anything.\' "Poobeshchay" is the command \'promise\'. Then come the stacked negatives, "nikomu nichego ne rasskazyvat", literally \'to nobody nothing not tell\'.'),
    (7, None, '\'I promise, this will be our shared secret.\' "Obeshchayu", \'I promise\', answers Nastya\'s "poobeshchay", \'promise me\'. "Obshchaya" means \'shared\' or \'common\'; "tayna" is a secret.'),
    (8, None, '\'Great, then listen to me very carefully.\' "Otlichno" is \'great\' or \'excellent\', and "togda" is \'then\'. "Vnimatelno", \'carefully\', grows from "vnimanie", \'attention\'.'),
    (9, None, '\'I\'m all ears, speak quickly.\' "Ya ves vo vnimanii", word for word \'I\'m all in attention\', is the Russian version of \'all ears\'. "Govori skoree" means \'talk faster\', so \'go on, quick\'.'),
    (10, None, '\'We will play out a very clever show!\' "Razygraem", from "razygrat", means staging a prank on someone. "Spektakl" is a stage play, and "khitryy" here means \'cunning\'.'),
    (11, None, '\'Well yeah, I don\'t understand anything yet.\' "Poka" here means \'so far\' or \'yet\', the same word as the casual \'bye\'. "Nichego ne ponimayu" puts \'nothing\' and \'not\' together.'),
    (12, None, '\'Soon you will understand everything perfectly yourself!\' "Sam", \'yourself\', adds weight, like \'on your own\'. "Poymyosh" is the perfective future of "ponyat", so it means the moment when it all clicks.'),
]
