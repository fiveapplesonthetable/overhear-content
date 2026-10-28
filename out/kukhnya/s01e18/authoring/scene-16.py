# Authoring module for kukhnya-s01e18-scene-16.
ID = 'kukhnya-s01e18-scene-16'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 18
SCENE = 16
TITLE = 'Неуклюжий бармен  (The Clumsy Bartender)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'kostya': 'Костя'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.18'
SOURCE_FILE = 'sources/kukhnya/s01/e18.ru.dual.srt'
INTRO = "Kostya walks up to Barinov's table at the restaurant with a plan: swap the wrong bottle for a safe one without explaining why. Barinov has no patience for it. Listen for how fast the chef runs out of it."
OPENER = 'Now the bottle swap, up close.'
TRANSITION = 'Now hear him get sent packing, start to end.'
OUTRO = 'Kostya has to go away empty-handed, and the chef is left with the bottle. Remember "idi otsyuda", \'go from here\', a rude way to tell someone to leave. See you next time!'
CLOSING = ('kostya', 'Всего хорошего!')
STORY = [
    ('kostya', 'Извините, приятного вам вечера.', 'Excuse me, have a pleasant evening.', [(295, 'Извини, приятного вечера.')], ''),
    ('barinov', 'Что тебе нужно от меня?', 'What do you need from me?', [(296, 'Че тебе надо?')], ''),
    ('kostya', 'Мне нужна эта бутылка.', 'I need this bottle.', [(297, 'Я бутылку...')], ''),
    ('barinov', 'О чём ты говоришь?', 'What are you talking about?', [(298, 'это... Чего я бутылка?')], ''),
    ('kostya', 'Я возьму эту бутылку.', 'I will take this bottle.', [(299, 'Я вот эту вот возьму,')], ''),
    ('kostya', 'А вам поставлю другую.', 'And I will put another one for you.', [(299, 'а эту поставлю.')], ''),
    ('barinov', 'Тебе что, совсем нечего делать?', 'Do you have absolutely nothing to do?', [(300, 'Тебе заняться нечем?')], ''),
    ('kostya', 'Нет, я просто хочу дать другую.', 'No, I just want to give another one.', [(300, 'Нет, я вот эту вот возьму, а эту поставлю.')], ''),
    ('barinov', 'Не трогай ничего, иди отсюда!', 'Do not touch anything, get out of here!', [(301, 'Иди отсюда.')], ''),
    ('kostya', 'Но я должен её забрать.', 'But I must take it.', [], ''),
    ('barinov', 'Я сказал, иди отсюда!', 'I said, get out of here!', [], ''),
    ('kostya', 'Хорошо, извините, я пойду.', 'All right, sorry, I will go.', [], ''),
]
WALK = [
    (0, None, '\'Excuse me, have a pleasant evening.\' A wish hides an unspoken \'I wish you\', so the evening takes the \'of\' endings: "priyatnogo vechera".'),
    (1, None, '\'What do you want from me?\' "Chto tebe nuzhno?", \'what to you is needed?\'. "Ot menya", from me.'),
    (2, None, '\'I need this bottle.\' "Nuzhna" matches the bottle, which is feminine; for a knife it would be "nuzhen".'),
    (3, None, '\'What are you on about?\' To the bartender the chef says "ty govorish"; to the new boss it was "vy govorite".'),
    (4, None, '\'I\'ll take this bottle.\' "Vozmu", I\'ll take, belongs to "vzyat", even though the two look quite different.'),
    (5, None, '\'And I\'ll put another one out for you.\' "Postavlyu" is literally \'I\'ll stand\': bottles are stood, not laid. "Vam", for you, is polite.'),
    (6, None, '\'Have you got nothing better to do?\' "Nechego delat", nothing to do: "ne" and "chego" fused into one word.'),
    (7, None, '\'No, I just want to give you another one.\' "Prosto", just, simply. "Dat", to give.'),
    (8, None, '\'Don\'t touch anything, get out of here!\' Russian stacks the \'not\': "ne trogay nichego", \'don\'t touch nothing\'. "Otsyuda", from here.'),
    (9, None, '\'But I have to take it.\' "Eyo", her: the bottle is a she in Russian.'),
    (10, None, '\'I said, get out!\' "Idi", go!, is the friendly-form command from "idti", to go on foot. Said twice, it\'s an order.'),
    (11, None, '\'All right, sorry, I\'ll go.\' "Izvinite" is the polite sorry; to a friend it would be "izvini".'),
]
