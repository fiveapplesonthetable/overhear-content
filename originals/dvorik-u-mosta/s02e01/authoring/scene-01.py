# Authoring module for dvorik-u-mosta-s02e01-scene-01.
ID = 'dvorik-u-mosta-s02e01-scene-01'
SHOW = 'dvorik-u-mosta'
SEASON = 2
EPISODE = 1
SCENE = 1
TITLE = 'Девятый ключ  (The Ninth Key)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kira': 'Кира', 'matvey': 'Матвей', 'yaroslav': 'Ярослав'}
INTRO = "It is early Saturday morning at the Bridge Courtyard Inn in St Petersburg, just hours after Matvey carried a dusty cedar box stamped 'Room 9' up from the cellar. Kira and Yaroslav lean over the front desk as Matvey turns the tiny brass key. Listen to the scene first."
OPENER = "Welcome to Season 2. Let's open the cedar box again, one line at a time."
TRANSITION = "Now let's listen to the whole scene again from start to finish."
OUTRO = "Inside the cedar box sits a heavy door key and a floor plan pointing straight behind the hallway bookcase. Don't worry if a word or two went past quickly; they return right away. See you next time."
CLOSING = ('kira', 'До встречи!')
STORY = [
    ('yaroslav', 'Поворачивай ключ медленно, Матвей. У меня сердце стучит!', 'Turn the key slowly, Matvey. My heart is pounding!'),
    ('matvey', 'Спокойно, шеф. Латунный замок из подвала никогда не ломается.', 'Easy, boss. A brass lock from the cellar never breaks.'),
    ('kira', 'Щёлкнуло! Подними деревянную крышку, Матвей!', 'It clicked! Lift the wooden lid, Matvey!'),
    ('matvey', 'Внутри большой ключ от двери, синий план и открытки.', 'Inside there is a big door key, a blue plan and postcards.'),
    ('yaroslav', 'Прочитайте, что написано на синей бумаге! Где мои очки?', 'Read what is written on the blue paper! Where are my glasses?'),
    ('kira', 'У вас на лбу, Ярослав Ильич. Как вчера вечером.', 'On your forehead, Yaroslav Ilyich. Just like last night.'),
    ('yaroslav', 'Ага! Смотрите: «Первый этаж. Номер девять. Зимний сад».', "Aha! Look: 'Ground floor. Room nine. Winter garden.'"),
    ('kira', 'Подождите, у нас на первом этаже есть зимний сад?', 'Wait, we have a winter garden on the ground floor?'),
    ('matvey', 'Посмотрите на стрелку. Она за книжным шкафом в коридоре.', 'Look at the arrow. It is behind the bookcase in the hallway.'),
    ('yaroslav', 'Этот тяжёлый шкаф стоит у стены уже двадцать лет!', 'That heavy bookcase has stood by the wall for twenty years!'),
    ('kira', 'Значит, за старыми книгами есть девятая дверь!', 'So behind the old books there is a ninth door!'),
    ('matvey', 'Сначала глоток кофе, а потом двигаем книги.', 'First a sip of coffee, and then we move the books.'),
]
WALK = [
    (0, None, ["'Turn the key slowly, Matvey. My heart is pounding!' Yaroslav talks to Matvey with the casual command ", (None, 'Поворачивай'), ", which asks for a turning that keeps going, nice and slow."]),
    (1, None, ["'Easy, boss. A brass lock from the cellar never breaks.' Matvey's calming word ", (None, 'Спокойно,'), " is simply 'calmly', and on its own it works like 'easy' or 'relax'."]),
    (2, None, ["'It clicked! Lift the wooden lid, Matvey!' Russian has a whole verb for the sound, ", (None, 'Щёлкнуло!'), " literally 'it clicked', with no subject at all."]),
    (3, None, ["'Inside there is a big door key, a blue plan and postcards.' A key 'from' the door: ", (None, 'ключ от двери'), " is how Russian says which lock a key belongs to."]),
    (4, None, ["'Read what is written on the blue paper! Where are my glasses?' His favourite question again: ", (None, 'Где мои очки?'), " Glasses are always plural in Russian, so it is 'my' in the plural too."]),
    (5, None, ["'On your forehead, Yaroslav Ilyich. Just like last night.' Kira doesn't say 'your forehead'. ", (None, 'У вас на лбу'), " is 'at you, on the forehead', and that is the natural way to place something on a person."]),
    (6, None, ["'Aha! Look: Ground floor. Room nine. Winter garden.' A glass sunroom has a lovely name here: ", (None, 'Зимний сад'), ", a 'winter garden', where plants stay warm all year."]),
    (7, None, ["'Wait, we have a winter garden on the ground floor?' Careful with floors: ", (None, 'на первом этаже'), " is the 'first floor', because Russians start counting at street level."]),
    (8, None, ["'Look at the arrow. It is behind the bookcase in the hallway.' A bookcase is a 'book cupboard': ", (None, 'книжным шкафом'), " joins the word for book with the word for cupboard."]),
    (9, None, ["'That heavy bookcase has stood by the wall for twenty years!' Where English says 'has stood', Russian keeps it simple with ", (None, 'стоит'), " plus 'already twenty years'."]),
    (10, None, ["'So behind the old books there is a ninth door!' Kira draws her conclusion with ", (None, 'Значит,'), " a one-word 'so' or 'that means' you can start any guess with."]),
    (11, None, ["'First a sip of coffee, and then we move the books.' Matvey's rule from Season 1 is back: ", (None, 'Сначала'), " something hot, and only after that, the work."]),
]
