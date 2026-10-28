# Authoring module for kukhnya-s01e17-scene-07.
ID = 'kukhnya-s01e17-scene-07'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 17
SCENE = 7
TITLE = 'За встречу  (To Meeting Up)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kostya': 'Костя', 'max': 'Макс', 'nastya': 'Настя'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.17'
SOURCE_FILE = 'sources/kukhnya/s01/e17.ru.dual.srt'
INTRO = "Max has gone to fetch drinks, and Kostya and Nastya look around the bar. Kostya likes the place a bit too much. Then Max comes back with glasses, and it's time for a toast. Listen to the table talk in Russian first."
OPENER = "Let's go round the table again, line by line."
TRANSITION = 'Now the table talk once more, from the start.'
OUTRO = 'Kostya has a daydream about another job, and the glasses go up. "Za vstrechu", to meeting up, is the easiest Russian toast you can learn. See you next time!'
CLOSING = ('kostya', 'Ну, удачи нам!')
STORY = [
    ('kostya', 'Слушай, а хороший бар.', "Listen, it's a nice bar.", [], ''),
    ('kostya', 'Я бы здесь поработал.', 'I could work here.', [(86, 'бы здесь поработал.')], ''),
    ('nastya', 'Здесь? А как же наш ресторан?', 'Here? What about our restaurant?', [], ''),
    ('kostya', 'В смысле, если бы не было нашего ресторана.', "I mean, if we didn't have our restaurant.", [(87, 'В смысле, если бы не было нашего ресторана')], ''),
    ('kostya', 'Тогда я бы тут поработал.', "Then I'd work here.", [(87, 'я бы тут поработал')], ''),
    ('nastya', 'Ладно, верю.', 'Fine, I believe you.', [], ''),
    ('max', 'Ну что, а вот и веселье.', 'Well, here comes the fun.', [(88, 'Ну что, а вот и веселье.')], ''),
    ('max', 'Разбирайте бокалы.', 'Grab your glasses.', [(89, 'разбираем')], ''),
    ('kostya', 'Спасибо, Макс.', 'Thanks, Max.', [], ''),
    ('nastya', 'Ну что?', 'Well?', [(91, 'Ну что?')], ''),
    ('max', 'Давайте за встречу.', "Let's drink to meeting up.", [(92, 'Давайте за встречу.')], ''),
    ('kostya', 'За встречу!', 'To meeting up!', [], ''),
]
WALK = [
    (0, None, '\'Listen, this is a nice bar.\' "Slushay", listen, is the casual way friends open a thought. The little "a" just eases into it.'),
    (1, None, '\'I could work here.\' "By" turns "porabotal", worked, into "would work". "Ya by" is how Russian starts a daydream.'),
    (2, None, '\'Here? What about our restaurant?\' "A kak zhe" is literally "and how then", the set way to say "what about...?".'),
    (3, None, '\'I mean, if we didn\'t have our restaurant.\' "V smysle", literally "in the sense", is how Russians say "I mean". "Esli by ne bylo" is "if there weren\'t".'),
    (4, None, '\'Then I\'d work here.\' "Tut" and "zdes" both mean "here", and Kostya has now used one of each. "By" keeps it a wish, not a plan.'),
    (5, None, '\'Fine, I believe you.\' "Veryu" means "I believe", from "verit". "Ladno", fine, sounds a bit like she\'s humouring him.'),
    (6, None, '\'Well, here comes the fun.\' Max uses the same arrival phrase as Nastya did: "a vot i", and here is. "Vesele", fun, comes from "vesyolyy", cheerful.'),
    (7, None, '\'Grab your glasses.\' "Razbirayte" is literally "take apart": everyone helps themselves to one. "Bokaly" is the plural of "bokal", a wine glass.'),
    (8, None, '\'Thanks, Max.\' Plain "spasibo" and a name: in Russian the name usually goes at the end like this.'),
    (9, None, '\'Well?\' "Nu chto?" is literally "well, what?". Here it\'s a nudge: somebody say the toast.'),
    (10, None, '\'Let\'s drink to meeting up.\' "Za" is the toast word, and "vstrecha", meeting, turns into "vstrechu" after it. "Davayte" makes it "let\'s" for a group.'),
    (11, None, "'To meeting up!' Kostya repeats the toast, as everyone round a Russian table does."),
]
