# Authoring module for kukhnya-s01e08-scene-01.
ID = 'kukhnya-s01e08-scene-01'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 8
SCENE = 1
TITLE = 'Лицо ресторана  (The Face of the Restaurant)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'nagiyev': 'Нагиев'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.08'
SOURCE_FILE = 'sources/kukhnya/s01/e08.ru.dual.srt'
INTRO = "This is Kukhnya, which means The Kitchen: a Russian comedy set in Claude Monet, a smart Moscow restaurant where the head chef, Viktor Barinov, rules with a loud voice. In episode eight the restaurant's owner, Dmitry Nagiyev, has brought Barinov to a television studio for a live cooking show. The chef would rather be at his own stove, and then he hears that his rival is on the programme too. It comes first in Russian, and it's fine if you miss a few words."
OPENER = "Let's take it again slowly. Nagiyev is smooth, and Barinov keeps looking for a way out."
TRANSITION = "Here's the whole conversation once more, at full speed."
OUTRO = "Barinov's line moyo mesto u plity, 'my place is at the stove', suits anyone who'd rather stay in their own corner. And pryamoy efir, 'live broadcast', is what you'll see in the corner of a Russian TV screen during a live show. See you next time."
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('barinov', 'Дима, зачем ты позвал меня сюда?', 'Dima, why did you call me here?', [(1, 'Дим, ну в каком хрен я здесь')], ''),
    ('nagiyev', 'Ты будешь выступать на телевидении, Виктор.', 'You will perform on television, Viktor.', [(3, 'Ты не только повар, ты лицо нашего ресторана')], ''),
    ('barinov', 'Я шеф-повар, а не известный актёр!', 'I am a head chef, not a famous actor!', [(2, 'Я же не актер, я повар')], ''),
    ('nagiyev', 'Ты главное лицо нашего дорогого ресторана.', 'You are the main face of our expensive restaurant.', [(3, 'ты лицо нашего ресторана')], ''),
    ('barinov', 'Моё место на кухне у плиты.', 'My place is in the kitchen at the stove.', [], ''),
    ('nagiyev', 'Зрители хотят видеть настоящего шефа.', 'The viewers want to see a real chef.', [(4, 'этим лицом светить')], ''),
    ('barinov', 'Отпусти меня обратно в Клод Моне.', 'Let me go back to Claude Monet.', [(5, 'Давай в ресторан поеду')], ''),
    ('nagiyev', 'Перестань спорить и иди вперёд.', 'Stop arguing and go forward.', [(10, 'Все, в тени живот и вперед')], ''),
    ('barinov', 'Там будет выступать эта Соколова?', 'Will that Sokolova perform there?', [(17, 'Елена Соколова')], ''),
    ('nagiyev', 'Да, Елена Соколова из ресторана Аркабалено.', 'Yes, Elena Sokolova from Arcobaleno restaurant.', [(16, 'шеф-повар ресторана Арка Баляна'), (17, 'Елена Соколова')], ''),
    ('barinov', 'Я докажу всем свой высокий класс.', 'I will prove my high caliber to everyone.', [], ''),
    ('nagiyev', 'Вот это отличный настрой, шеф!', 'Now that is a great attitude, chef!', [], ''),
    ('barinov', 'Прямой эфир начинается прямо сейчас.', 'Live broadcast begins right now.', [(19, 'Итак, мы начинаем')], ''),
]
WALK = [
    (0, None, "'Dima, why did you call me here?' Barinov calls him Dima, the friendly short form of Dmitry, which tells you how close the two men are. The word pozval, 'you called', also covers 'you invited', as when someone asks you over."),
    (1, None, "'You will perform on television, Viktor.' Here budesh vystupat means 'you will be performing': budu, budesh and the rest, put before vystupat, talk about an activity that will go on for a while. On television is na televidenii, with -ii for the place."),
    (2, None, "'I am a head chef, not a famous actor!' Russian builds 'X, not Y' with the little word a: shef-povar, a ne akter. The title shef-povar, literally 'chef-cook', is the formal name for a head chef."),
    (3, None, "'You are the main face of our expensive restaurant.' Just as in English, litso, 'face', can mean the person who represents a company. The word dorogoy means both 'expensive' and 'dear', and here it's the price that counts."),
    (4, None, "'My place is in the kitchen at the stove.' Russian drops 'is' in the present, so the line is simply moyo mesto na kukhne, 'my place in the kitchen'. After u, 'by', plita becomes plity."),
    (5, None, "'The viewers want to see a real chef.' The word zriteli, 'viewers', is built on an old word for seeing, zret. As the one being seen, a male chef takes -a: nastoyashchego shefa."),
    (6, None, "'Let me go back to Claude Monet.' The command otpusti, 'let me go', is what you'd say to a boss when asking to leave. With obratno, 'back', it means returning to where you came from."),
    (7, None, "'Stop arguing and go forward.' After perestan, 'stop', comes the basic form of the action: perestan sporit. And idi vperyod, 'go forward', is a push to get on with it."),
    (8, None, "'Will that Sokolova perform there?' Putting eta, 'this', in front of a surname sounds dismissive, like 'that Sokolova woman'. The -a at the end of Sokolova marks a woman's surname."),
    (9, None, "'Yes, Elena Sokolova from Arcobaleno restaurant.' After iz, 'out of, from', restoran becomes restorana. The name Arcobaleno is Italian for 'rainbow', and as a foreign word it never changes."),
    (10, None, "'I will prove my high caliber to everyone.' Although dokazhu, 'I will prove', looks like a present form, it points to one result in the future. The word svoy, 'my own', refers back to whoever is acting, here Barinov himself."),
    (11, None, "'Now that is a great attitude, chef!' At the start of a sentence, vot eto points at something and approves of it, 'now that's...'. The word nastroy, 'attitude', shares a root with nastroyeniye, 'mood'."),
    (12, None, "'Live broadcast begins right now.' TV people call a live show pryamoy efir, literally 'straight air'. The same root turns up in pryamo seychas, 'right now', so there's no more time to argue."),
]
