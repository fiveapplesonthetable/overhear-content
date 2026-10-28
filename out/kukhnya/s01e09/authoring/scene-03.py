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
INTRO = "In his private office at Claude Monet, Chef Viktor Barinov is supposed to be managing the kitchen during a busy lunch service. When sous-chef Lyova rushes in with urgent orders from VIP guests, Barinov bluntly dismisses him, insisting that spending quality time with his visiting daughter comes before any restaurant dish. Let's listen to their conversation in Russian first."
OPENER = "Now let's examine Lyova and Chef Barinov's office exchange line by line."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Leaving Chef Barinov happily playing games with Alisa behind closed doors, a flustered Lyova returns to the line to manage the rush and prepare the specialty dishes on his own. Next time you watch the episode, listen for the Russian expressions for 'dish' and 'important' — you will catch every word right away. See you next time!"
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
    (0, None, "'Chef, you need to go to the kitchen urgently.' Russian omits the present-tense verb 'to be' here, linking 'chef' directly with 'necessary', pairing it with 'urgently' and 'kitchen'."),
    (1, None, "'Lyova, don't you see I am busy?' Chef Barinov turns a statement into a question purely through rising intonation on the word meaning 'see', followed by 'busy'."),
    (2, None, "'Guests in the dining room are waiting for special dishes.' The phrasing opens with 'guests' before bringing in 'dining room' and 'are waiting for' to make the point clear."),
    (3, None, "'I am playing with my daughter right now.' Chef Barinov expresses this naturally by combining the word for 'now' with 'am playing' and 'daughter'."),
    (4, None, "'But this is an important order from the chef.' Russian omits the present-tense verb 'to be' here, linking 'important' directly with 'order', followed by 'chef'."),
    (5, None, "'You are a wonderful cook and will manage yourself.' Here Chef Barinov anchors the line on the word meaning 'wonderful' and builds the thought around 'cook' and 'will manage'."),
    (6, None, "'They want specifically your signature meat.' Notice how naturally this everyday Russian phrase expresses the speaker's point."),
    (7, None, "'Cook our usual tasty meat yourself.' Chef Barinov leads with the direct command form meaning 'cook', pairing it with 'usual' and 'tasty'."),
    (8, None, "'And what if the guests do not like the taste?' Lyova turns a statement into a question purely through rising intonation on the word meaning 'to the guests', pairing it with 'appeal to' and 'taste'."),
    (9, None, "'Add a little salt and fresh pepper.' Chef Barinov leads with the direct command form meaning 'add', pairing it with 'a little' and 'salt'."),
    (10, None, "'Chef, real chaos is starting in the kitchen.' The phrasing opens with 'chef' before bringing in 'kitchen' and 'is starting' to make the point clear."),
    (11, None, "'Close the door and establish order there.' Chef Barinov leads with the direct command form meaning 'close', pairing it with 'door' and 'establish'."),
    (12, None, "'Alright, chef, I will do everything myself.' Lyova puts the word for 'alright' together with 'chef' and 'will do' in a crisp, natural spoken turn of phrase."),
]
