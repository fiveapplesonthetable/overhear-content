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
    (0, None, "'Chef, you need to go to the kitchen urgently.' During the lunch rush, Lyova bursts into the office and tells the chef he is needed in the kitchen."),
    (1, None, "'Lyova, don't you see I am busy?' Sitting on the floor with toys, Barinov asks if Lyova cannot see that he is busy."),
    (2, None, "'Guests in the dining room are waiting for special dishes.' Lyova stresses that diners in the hall are waiting for special dishes."),
    (3, None, "'I am playing with my daughter right now.' Viktor waves the orders away, saying he is right in the middle of playing with his daughter."),
    (4, None, "'But this is an important order from the chef.' Lyova protests that the table specifically requested the head chef's cooking."),
    (5, None, "'You are a wonderful cook and will manage yourself.' Barinov flatters his sous-chef, telling Lyova he is a great cook who can handle it himself."),
    (6, None, "'They want specifically your signature meat.' Lyova explains that the guests asked for Viktor's signature meat dish."),
    (7, None, "'Cook our usual tasty meat yourself.' Viktor tells him to just cook their standard meat recipe on his own."),
    (8, None, "'And what if the guests do not like the taste?' Nervous about complaints, Lyova asks what to do if the guests notice a difference in taste."),
    (9, None, "'Add a little salt and fresh pepper.' Viktor jokingly advises him to just toss in a pinch of salt and fresh pepper."),
    (10, None, "'Chef, real chaos is starting in the kitchen.' Lyova warns that without the chef at the pass, real chaos is breaking out in the kitchen."),
    (11, None, "'Close the door and establish order there.' Refusing to budge, Barinov tells him to shut the office door and restore order out there."),
    (12, None, "'Alright, chef, I will do everything myself.' Defeated, Lyova sighs and promises to handle everything himself."),
]
