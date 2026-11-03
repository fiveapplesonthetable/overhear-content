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
OUTRO = "Barinov's line 'my place is at the stove' suits anyone who'd rather stay in their own corner, and 'live broadcast' is what flashes in the corner of a Russian TV screen during a live show. See you next time."
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
    (0, None, ["'Dima, why did you call me here?' Questioning why he was brought here, the chef uses ", ('barinov', 'позвал'), ' for called or summoned, showing he did not just wander in.']),
    (1, None, ["'You will perform on television, Viktor.' To tell him about his upcoming appearance, Nagiyev uses ", ('nagiyev', 'выступать'), ' for perform, putting him in the spotlight.']),
    (2, None, ["'I am a head chef, not a famous actor!' Feeling proud of his real job, Barinov refers to himself as a ", ('barinov', 'шеф-повар'), ', which combines boss and cook.']),
    (3, None, ["'You are the main face of our expensive restaurant.' The owner tries to flatter him with ", ('nagiyev', 'лицо'), ', meaning face or representative of the place.']),
    (4, None, ["'My place is in the kitchen at the stove.' Refusing the spotlight, he firmly points to the ", ('barinov', 'плиты'), ', his trusty cooking stove back at work.']),
    (5, None, ["'The viewers want to see a real chef.' Pointing out the audience watching at home, Nagiyev uses ", ('nagiyev', 'Зрители'), ' for the viewers tuning in.']),
    (6, None, ["'Let me go back to Claude Monet.' Begging to leave the TV studio, he adds ", ('barinov', 'обратно'), ' to ask to go straight back.']),
    (7, None, ["'Stop arguing and go forward.' Pushing him towards the bright cameras, Nagiyev says ", ('nagiyev', 'вперёд'), ' to get him moving ahead.']),
    (8, None, ["'Will that Sokolova perform there?' Hearing about his female rival, he quickly adds ", ('barinov', 'эта'), ' before her name to sound dismissive.']),
    (9, None, ["'Yes, Elena Sokolova from Arcobaleno restaurant.' Confirming her workplace, the TV host says ", ('nagiyev', 'из'), ' to simply mean out of or from.']),
    (10, None, ["'I will prove my high caliber to everyone.' Suddenly feeling quite competitive, he wants to show ", ('barinov', 'всем'), ', meaning everyone who is watching.']),
    (11, None, ["'Now that is a great attitude, chef!' Happy with this sudden change of heart, Nagiyev praises his ", ('nagiyev', 'настрой'), ' or fighting spirit.']),
    (12, None, ["'Live broadcast begins right now.' Reminding him they are completely out of time, he mentions the ", ('barinov', 'эфир'), ', which means the live air.']),
]
