# Authoring module for kukhnya-s01e09-scene-03.
ID = 'kukhnya-s01e09-scene-03'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 9
SCENE = 3
TITLE = 'Занят с дочерью  (Busy with His Daughter)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'lyova': 'Лёва'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.09'
SOURCE_FILE = 'sources/kukhnya/s01/e09.ru.dual.srt'
INTRO = "Barinov has shut himself in his office with Alisa, and he is playing with her. Lyova, his sous-chef, who tends to stutter when he's stressed, comes in with a problem from the dining room. Here is what they say, in Russian first."
OPENER = "Let's go back through it slowly."
TRANSITION = 'And now the whole conversation, one more time through.'
OUTRO = 'Lyova leaves with the door shut behind him and the kitchen on his shoulders. Barinov goes back to playing. Catch you next time.'
CLOSING = ('lyova', 'Пока!')
STORY = [
    ('lyova', 'Шеф, вам нужно срочно на кухню.', 'Chef, you need to go to the kitchen urgently.', [], ''),
    ('barinov', 'Лёва, не видишь, я занят?', "Lyova, don't you see I am busy?", [(85, 'не видишь, я занят.')], ''),
    ('lyova', 'Гости в зале ждут особые блюда.', 'Guests in the dining room are waiting for special dishes.', [(84, 'два блюда от шефа')], ''),
    ('barinov', 'Я сейчас играю с моей дочерью.', 'I am playing with my daughter right now.', [(86, 'Я с дочерью играю.')], ''),
    ('lyova', 'Но это важный заказ от шефа.', 'But this is an important order from the chef.', [(84, 'блюда от шефа')], ''),
    ('barinov', 'Ты прекрасный повар и справишься сам.', 'You are a wonderful cook and will manage yourself.', [], ''),
    ('lyova', 'Они хотят именно ваше фирменное мясо.', 'They want specifically your signature meat.', [], ''),
    ('barinov', 'Приготовь наше обычное вкусное мясо сам.', 'Cook our usual tasty meat yourself.', [], ''),
    ('lyova', 'А если гостям не понравится вкус?', 'And what if the guests do not like the taste?', [], ''),
    ('barinov', 'Добавь немного соли и свежего перца.', 'Add a little salt and fresh pepper.', [], ''),
    ('lyova', 'Шеф, на кухне начинается настоящий хаос.', 'Chef, real chaos is starting in the kitchen.', [], ''),
    ('barinov', 'Закрой дверь и наведите там порядок.', 'Close the door and establish order there.', [], ''),
    ('lyova', 'Хорошо, шеф, я всё сделаю сам.', 'Alright, chef, I will do everything myself.', [], ''),
]
WALK = [
    (0, None, '\'Chef, you need to go to the kitchen urgently.\' Lyova says "vam", the polite "to you", and "nuzhno", "it\'s needed". Together it\'s "to you it\'s needed urgently to the kitchen". He doesn\'t even say "go". The direction is enough.'),
    (1, None, '\'Lyova, don\'t you see I am busy?\' Barinov says "ty" to him, as a boss does. "Zanyat" is "busy", and there\'s no word for "am". In Russian you simply say "I busy", and that\'s the whole sentence.'),
    (2, None, '\'Guests in the dining room are waiting for special dishes.\' Russian says "wait dishes", with no "for" at all. The dining room is "zal", which really means "hall". Lyova lists the problem as calmly as he can.'),
    (3, None, '\'I am playing with my daughter right now.\' "Seychas" is "right now". Barinov says "with my daughter", and the word for daughter changes its ending after "with", as "you" did earlier. He thinks this settles it.'),
    (4, None, '\'But this is an important order from the chef.\' Lyova pushes back, politely. "Zakaz", "order", is a word from the banquet scene, and "vazhny" is "important". The order comes from the chef himself, so he can hardly say no.'),
    (5, None, '\'You are a wonderful cook and will manage yourself.\' Barinov flatters him. "Spravishsya" is the same "manage" verb Louis used. It\'s a compliment and a brush-off in one, and "sam", "yourself", closes the door.'),
    (6, None, '\'They want specifically your signature meat.\' Lyova says "vashe", the polite "your". "Firmenny", "signature", comes from the Russian for company, so it means the house speciality. "Imenno", "specifically", you\'ve heard before.'),
    (7, None, '\'Cook our usual tasty meat yourself.\' "Prigotov" is a bare command, "prepare", with no "you". It\'s the same verb as in the first scene. And he says "our" meat, as if the dish belonged to the whole kitchen.'),
    (8, None, '\'And what if the guests do not like the taste?\' Russian turns this round: "if the taste will not please to the guests". The guests are the ones it\'s pleasing to. Lyova worries aloud, and "esli" is the "if".'),
    (9, None, '\'Add a little salt and fresh pepper.\' Barinov\'s idea of expert advice is almost an insult. "Nemnogo" is "a little", literally "not much". "Soli" and "pertsa" are "of salt" and "of pepper", the "some of" ending.'),
    (10, None, '\'Chef, real chaos is starting in the kitchen.\' "Khaos" you can read at once. Russian says "on the kitchen", not "in", and "nastoyashchy" is "real", the term for the real thing.'),
    (11, None, '\'Close the door and establish order there.\' "Zakroy" is another bare command, "close", and "navedi poryadok" is "bring order". Barinov doesn\'t want to hear the kitchen at all. He wants the door shut.'),
    (12, None, '\'Alright, chef, I will do everything myself.\' "Khorosho" means "good", and here it\'s a tired "all right then". "Vsyo sdelayu" is "everything I\'ll do". Lyova gives in. He is loyal, and the kitchen is his now.'),
]
