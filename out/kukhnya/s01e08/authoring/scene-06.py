# Authoring module for kukhnya-s01e08-scene-06.
ID = 'kukhnya-s01e08-scene-06'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 8
SCENE = 6
TITLE = 'Новый шеф на кухне  (A New Chef in the Kitchen)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'elena': 'Елена'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.08'
SOURCE_FILE = 'sources/kukhnya/s01/e08.ru.dual.srt'
INTRO = "Elena Sokolova, chef of the Italian restaurant Arcobaleno, has bet Barinov that she can last a shift in his kitchen. The next morning she turns up at Claude Monet, and Barinov presents her to his cooks. It's in Russian first."
OPENER = 'Slowly now. Barinov makes the introductions, and within a minute Elena is giving the orders.'
TRANSITION = 'Now the whole first service again, at normal speed.'
OUTRO = "Two of Elena's lines are worth keeping: vsem vsyo ponyatno?, 'is everything clear to everyone?', which works in any meeting, and sledit za kachestvom, 'to watch over quality', her motto for the whole shift. See you next time."
CLOSING = ('barinov', 'До встречи!')
STORY = [
    ('barinov', 'Внимание всем, на кухне важный гость!', 'Attention everyone, in the kitchen is an important guest!', [(84, 'У кухни, внимание, это Елена Павловна')], ''),
    ('barinov', 'Это шеф Елена Павловна Соколова.', 'This is Chef Elena Pavlovna Sokolova.', [(84, 'это Елена Павловна')], ''),
    ('elena', 'Здравствуйте, дорогие повара ресторана.', 'Hello, dear chefs of the restaurant.', [], ''),
    ('barinov', 'Сегодня она работает вместе с нами.', 'Today she works together with us.', [(85, 'Она будет сегодня')], ''),
    ('elena', 'Надеюсь, вы умеете готовить вкусно и быстро.', 'I hope you know how to cook tasty and fast.', [(80, 'ты уже час готовишь')], ''),
    ('barinov', 'Мои ребята умеют абсолютно всё!', 'My guys know how to do absolutely everything!', [(82, 'а не работали')], ''),
    ('elena', 'Тогда почему Лёва варит суп уже час?', 'Then why has Lyova been cooking soup for an hour already?', [(80, 'ты уже час готовишь')], ''),
    ('barinov', 'Лёва, отвечай шефу быстро и чётко!', 'Lyova, answer the chef quickly and clearly!', [(81, 'Заснул, что ли')], ''),
    ('elena', 'Так, официант принёс первый большой заказ.', 'Right, the waiter brought the first big order.', [(87, 'Заказ')], ''),
    ('elena', 'Одна телятина, треска и свежий салат!', 'One veal, cod, and fresh salad!', [(89, 'Телятина по трюфельным соусам, одна треска')], ''),
    ('barinov', 'Всем всё понятно? Начинайте готовить!', 'Is everything clear to everyone? Start cooking!', [(91, 'Всем все понятно')], ''),
    ('elena', 'Я лично проверю каждое готовое блюдо.', 'I will personally check every finished dish.', [(92, 'Хорошо')], ''),
    ('barinov', 'Не командуйте слишком громко, Елена.', "Don't boss around too loudly, Elena.", [(85, 'ну вы все сами слышали')], ''),
    ('elena', 'Настоящий шеф всегда следит за качеством!', 'A true chef always watches over quality!', [(85, 'ну вы все сами слышали')], ''),
]
WALK = [
    (0, None, "'Attention everyone, in the kitchen is an important guest!' A typical announcement opens with vnimaniye vsem, literally 'attention to all'. To say 'in the kitchen', Russian uses na: na kukhne."),
    (1, None, "'This is Chef Elena Pavlovna Sokolova.' Her middle name, Pavlovna, says her father is called Pavel, and using it is the respectful way to present her. The title shef stays the same for a woman."),
    (2, None, "'Hello, dear chefs of the restaurant.' Elena opens with zdravstvuyte, the polite or plural hello, from the same root as zdorovye, 'health'. The -a in restorana gives 'of the restaurant'."),
    (3, None, "'Today she works together with us.' After s, 'with', my becomes nami: vmeste s nami. Russian uses the present rabotayet for today's plan, as English can with 'she works'."),
    (4, None, "'I hope you know how to cook tasty and fast.' For skills Russian uses umet, here umeyete, 'you know how'; znat is for knowing facts. Both vkusno and bystro end in -o because they describe how the cooking is done."),
    (5, None, "'My guys know how to do absolutely everything!' A boss calls his team rebyata, 'guys', a warm word. He answers her word for word, with umeyut, the 'they' form of the umet she just used."),
    (6, None, "'Then why has Lyova been cooking soup for an hour already?' For something still going on, Russian keeps the present: varit sup uzhe chas, 'boils soup already an hour'. The word varit is for cooking in water: soup, pasta or potatoes."),
    (7, None, "'Lyova, answer the chef quickly and clearly!' The person you answer gets a 'to' ending, so shef becomes shefu. And chotko, 'crisply', is what a boss wants from a report."),
    (8, None, "'Right, the waiter brought the first big order.' At the start of a sentence, tak means 'right then', a word for taking charge. The past prinyos, 'he brought', is unusual because it has no -l at the end."),
    (9, None, "'One veal, cod, and fresh salad!' A kitchen order needs nothing but the dishes: odna telyatina, one portion of veal. The word telyatina comes from telyonok, 'a calf'."),
    (10, None, "'Is everything clear to everyone? Start cooking!' Literally 'to all everything clear', vsem vsyo ponyatno is how a boss checks that the team has followed. With -ayte on the end, nachinayte is addressed to the whole kitchen."),
    (11, None, "'I will personally check every finished dish.' Elena's proveryu, 'I will check', means one complete check for each dish. The word gotovoye can be 'ready' or 'cooked', from the same root as gotovit, 'to cook'."),
    (12, None, "'Don't boss around too loudly, Elena.' With -yte, komanduyte is the polite command from komandovat, 'to give orders'. Barinov says vy to Elena all through the shift, even when she annoys him."),
    (13, None, "'A true chef always watches over quality!' After sledit za, 'to keep an eye on', kachestvo becomes kachestvom. The word nastoyashchiy, 'real, true', is for the genuine article."),
]
