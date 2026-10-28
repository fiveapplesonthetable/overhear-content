# Authoring module for kukhnya-s01e07-scene-14.
ID = 'kukhnya-s01e07-scene-14'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 7
SCENE = 14
TITLE = 'Командная работа  (Teamwork)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'lyova': 'Лёва'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.07'
SOURCE_FILE = 'sources/kukhnya/s01/e07.ru.dual.srt'
INTRO = 'Just before dinner service at Claude Monet, Chef Barinov has lost his sense of taste. For once he is not shouting. Lyova, his deputy, steps forward to say the team will do the tasting for him. Listen to it in Russian.'
OPENER = "Let's go slowly. Lyova is reassuring, Barinov is gloomy, and it's a very gentle scene for a kitchen."
TRANSITION = 'Now the whole scene without stopping.'
OUTRO = "Keep 'we won't let you down' for when someone is counting on you; Lyova means every word. Until the next scene."
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('lyova', 'Шеф, не переживайте вы так сильно!', 'Chef, do not worry so much!', [(303, 'Шеф, не переживайте так')], ''),
    ('barinov', 'Как не переживать? Я потерял вкус!', 'How not to worry? I lost my sense of taste!', [], ''),
    ('lyova', 'Всё обязательно будет хорошо и спокойно.', 'Everything will definitely be fine and calm.', [(304, 'Все будет нормально')], ''),
    ('barinov', 'Я не могу приготовить фирменный соус.', 'I cannot prepare the signature sauce.', [(305, 'Я не могу сделать соус')], ''),
    ('lyova', 'Мы вам поможем, вся команда с вами!', 'We will help you, the whole team is with you!', [(306, 'мы вам поможем'), (306, 'мы с вами')], ''),
    ('barinov', 'Но вы не знаете точный рецепт.', 'But you do not know the exact recipe.', [], ''),
    ('lyova', 'Управляйте нами, командуйте каждым нашим шагом!', 'Direct us, command our every step!', [(307, 'Управляйте нами')], ''),
    ('barinov', 'Бульон уже сварился для этого соуса?', 'Has the broth already boiled for this sauce?', [(307, 'бульон сварился')], ''),
    ('lyova', 'Бульон готов, и свежие овощи нарезаны.', 'The broth is ready, and fresh vegetables are chopped.', [], ''),
    ('barinov', 'Кто же будет пробовать готовое блюдо?', 'Who then will taste the finished dish?', [], ''),
    ('lyova', 'Мы будем сами всё внимательно пробовать!', 'We will taste everything carefully ourselves!', [(309, 'мы будем сами все пробовать')], ''),
    ('barinov', 'Тогда за работу, у нас всё получится!', 'To work then, everything will turn out well for us!', [(310, 'Все получится')], ''),
    ('lyova', 'Конечно, шеф, мы вас не подведём!', 'Of course, Chef, we will not let you down!', [(311, 'Конечно')], ''),
]
WALK = [
    (0, None, "'Chef, do not worry so much!' Ne perezhivayte is the polite command 'don't worry'. Lyova adds vy after it, which Russians do to sound warmer."),
    (1, None, '\'How not to worry? I lost my sense of taste!\' "Kak ne perezhivat\'", \'how not to worry\', is Barinov\'s \'how could I not?\'. "Vkus" is both taste and the sense of taste.'),
    (2, None, '\'Everything will definitely be fine and calm.\' "Budet khorosho", \'it will be good\', uses the adverb khorosho, not an adjective. "Obyazatel\'no", \'definitely\', comes from obyazan, \'obliged\', the word Barinov used to the owner.'),
    (3, None, '\'I cannot prepare the signature sauce.\' "Firmennyy" sous is the very sauce Nagiyev came to taste. Ne mogu, \'I can\'t\', is from moch\'.'),
    (4, None, '\'We will help you, the whole team is with you!\' "Pomoch\'", to help, needs vam, \'to you\', since you give help to someone. S vami, \'with you\', uses the \'with\' ending of vy.'),
    (5, None, '\'But you do not know the exact recipe.\' "Tochnyy", \'exact\', comes from tochka, a point or dot. "Retsept" means a recipe and also a doctor\'s prescription.'),
    (6, None, '\'Direct us, command our every step!\' "Upravlyat\'" and komandovat\' both put what is being run into the \'with\' form: nami, \'us\', and kazhdym nashim shagom, \'our every step\'.'),
    (7, None, '\'Has the broth already boiled for this sauce?\' "Svarilsya", \'has boiled\', ends in -sya because the broth cooked by itself. "Bul\'on" is the French bouillon.'),
    (8, None, '\'The broth is ready, and fresh vegetables are chopped.\' "Narezany", \'chopped\', has plural -y to match ovoshchi, vegetables. "Gotov", \'ready\', is the short masculine form, to match bul\'on.'),
    (9, None, '\'Who then will taste the finished dish?\' Zhe after kto adds impatience, like \'who on earth\'. "Gotovoye", \'finished\', is the full neuter form of gotov, to match blyudo.'),
    (10, None, '\'We will taste everything carefully ourselves!\' "Sami", \'ourselves\', is the plural of sam. "Budem probovat\'" is the ongoing future, budem plus the infinitive: \'we will be tasting\'.'),
    (11, None, "'To work then, everything will turn out well for us!' Za rabotu, 'to work', is a set call to get started. U nas vsyo poluchitsya, 'at us all will turn out', means 'we'll manage'."),
    (12, None, "'Of course, Chef, we will not let you down!' Ne podvedyom, 'we won't let you down', echoes the ne podvedite Nagiyev said to the chef. Vas is the polite 'you' for the chef."),
]
