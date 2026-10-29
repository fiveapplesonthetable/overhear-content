# Authoring module for kukhnya-s01e10-scene-10.
ID = 'kukhnya-s01e10-scene-10'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 10
SCENE = 10
TITLE = 'Срочный заём  (An Urgent Loan)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'kostya': 'Костя'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.10'
SOURCE_FILE = 'sources/kukhnya/s01/e10.ru.dual.srt'
INTRO = "Barinov still needs money for his bet. In the restaurant's busy middle of service, he catches Kostya, the bartender, with a dish to carry out. We'll hear it through once before I say a word about it."
OPENER = "I'll take you through it now."
TRANSITION = 'Everything again, from the beginning.'
OUTRO = "Kostya escapes with the dish and a promise to talk later. Barinov says he'll be back, and he means it. Until then."
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('kostya', 'Шеф, давайте уже быстрее заказ!', 'Chef, hurry up the order already!', [(77, 'давай уже быстрее.')], ''),
    ('kostya', 'Гость за пятым столиком ждёт.', 'The guest at table five is waiting.', [(78, 'за пятым столиком')], ''),
    ('barinov', 'Всё готово, можешь забирать блюдо.', 'Everything is ready, you can take the dish.', [(79, 'Все, можешь забирать.')], ''),
    ('kostya', 'Отлично, несу в зал.', 'Great, taking it to the dining room.', [(80, 'Отлично.')], ''),
    ('barinov', 'Стой, секунду, подожди меня здесь!', 'Wait, one second, wait for me here!', [(80, 'Стой, стой, стой, секунду. Подожди.')], ''),
    ('kostya', 'Шеф, мне надо сейчас работать.', 'Chef, I need to work right now.', [(81, 'Сейчас надо поделать.')], ''),
    ('barinov', 'Костя, скажи, как твои дела?', 'Kostya, tell me, how are your affairs?', [(82, 'Как дела?')], ''),
    ('kostya', 'Нормально, чаевые сегодня хорошие.', 'Fine, tips are good today.', [(83, 'Нормально.')], ''),
    ('barinov', 'Точно хорошие? Ты богатый человек!', 'Really good? You are a wealthy man!', [(83, 'Точно?')], ''),
    ('barinov', 'Мне просто занять немного нужно.', 'I just need to borrow a little.', [(84, 'Мне просто занять немного.')], ''),
    ('kostya', 'Шеф, вы хотите мои чаевые?', 'Chef, you want my tips?', [], ''),
    ('barinov', 'Всего пару тысяч до утра!', 'Only a couple of thousand until morning!', [], ''),
    ('kostya', 'Шеф, давайте попозже поговорим!', 'Chef, let us talk later!', [(85, 'Давай попозже поговорим.')], ''),
    ('barinov', 'Ладно, иди, но я вернусь!', 'All right, go, but I will return!', [(86, 'Ладно.')], ''),
]
WALK = [
    (0, None, '\'Chef, hurry up the order already!\' Kostya says "davayte", "give", in front of "bystree", "faster": that\'s how Russians say "come on". The -te is polite. "Uzhe", "already", adds the impatience.'),
    (1, None, '\'The guest at table five is waiting.\' Russians sit "za", "behind", a table: "za pyatym stolikom". "Stolik" is the small version of "stol", and it\'s the usual word for a restaurant table.'),
    (2, None, '\'Everything is ready, you can take the dish.\' "Mozhesh zabirat" is "you can take away", with the casual "ty". "Zabirat" is "brat", "take", with za-, for picking something up. Barinov is brisk, and almost kind.'),
    (3, None, '\'Great, taking it to the dining room.\' "Nesu" is "I carry": Russian has one word for carrying in your hands, "nesti", and another for just going, "idti". "V zal" is "to the hall", the dining room.'),
    (4, None, '\'Wait, one second, wait for me here!\' "Stoy!", "stand!", is how Barinov says "stop". Then "podozhdi menya", "wait me", with no "for". "Sekundu" is "one second".'),
    (5, None, '\'Chef, I need to work right now.\' "Mne nado", "to me it\'s necessary", is the casual "I have to". "Rabotat" is "to work". Kostya tries to leave politely, and the chef doesn\'t let him.'),
    (6, None, '\'Kostya, tell me, how are your affairs?\' "Skazhi" is "tell", said to one person. "Kak tvoi dela" is the casual "how are things", now with a motive behind it. Barinov is oiling the way.'),
    (7, None, '\'Fine, tips are good today.\' "Chaevye", "tips", grows out of "chay", "tea", so it\'s "tea money". "Normalno" is "fine". Kostya gives the answer a borrower likes best.'),
    (8, None, '\'Really good? You are a wealthy man!\' Barinov picks up Kostya\'s own word, "khoroshie", and throws it back as a question with "tochno", "really?". Then "ty bogaty chelovek", with no verb for "are". Barinov flatters, as he did with Fedya.'),
    (9, None, '\'I just need to borrow a little.\' "Zanyat", "to borrow", is spelled like "zanyat", "busy", and they\'re related. To lend, Russians say "dat v dolg", "give into debt". Barinov says "nemnogo", but he means thousands.'),
    (10, None, '\'Chef, you want my tips?\' Kostya says "vy khotite", the polite "you want". There\'s no question word, only the voice rising at the end. "Moi chaevye" is "my tips".'),
    (11, None, '\'Only a couple of thousand until morning!\' "Vsego paru tysyach", "in all a pair of thousands", is "just a couple of thousand". "Do utra" is "until morning": after "do", "utro" becomes "utra".'),
    (12, None, '\'Chef, let us talk later!\' "Popozzhe" is "pozzhe", "later", softened with po- to "a bit later". "Davayte pogovorim" is the polite "let\'s talk". Kostya wants to run.'),
    (13, None, '\'All right, go, but I will return!\' "Vernus" has -s, the short -sya, meaning "come back"; "verne" without it was "give back". "Idi" is "go". Barinov warns him that he\'ll be back.'),
]
