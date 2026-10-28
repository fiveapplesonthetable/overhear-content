# Authoring module for kukhnya-s01e07-scene-05.
ID = 'kukhnya-s01e07-scene-05'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 7
SCENE = 5
TITLE = 'Встреча на рынке  (Meeting at the Market)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'elena': 'Елена'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.07'
SOURCE_FILE = 'sources/kukhnya/s01/e07.ru.dual.srt'
INTRO = "Chef Barinov of Claude Monet has gone to the food market for the day's vegetables, and who should he run into at the next stall but Elena Pavlovna, who is about to open a rival restaurant? They are exquisitely polite for about ten seconds. First the scene in Russian."
OPENER = "Let's go back. Both of them use the polite 'you' and the father's name, which makes the insults land harder."
TRANSITION = 'Now the whole market encounter again.'
OUTRO = "The fight is about who is best, and it's told through apples. 'We'll see' and 'learn while I'm kind' are two good lines to keep. See you next time."
CLOSING = ('barinov', 'До встречи!')
STORY = [
    ('elena', 'Доброе утро, шеф Виктор Петрович!', 'Good morning, Chef Viktor Petrovich!', [(41, 'Доброе утро, Виктор Петрович')], ''),
    ('barinov', 'Доброе утро, Елена Павловна.', 'Good morning, Elena Pavlovna.', [(42, 'Не уверен, Елена Павловна')], ''),
    ('elena', 'Зачем вы пришли на этот рынок?', 'Why did you come to this market?', [(43, 'А что вас сюда занесло')], ''),
    ('barinov', 'Я выбираю самые лучшие свежие овощи.', 'I am choosing the best fresh vegetables.', [(44, 'А, помидорки')], ''),
    ('barinov', 'А вы решили сварить мужу борщ?', 'And did you decide to make your husband borscht?', [(45, 'Решили-таки мужу борщ сварить')], ''),
    ('elena', 'Нет, я открываю новый дорогой ресторан.', 'No, I am opening a new expensive restaurant.', [(46, 'У нас скоро открытие ресторана')], ''),
    ('elena', 'Я сама готовлю новое меню.', 'I am preparing a new menu myself.', [(46, 'вот готовлю новое меню')], ''),
    ('barinov', 'В ваш ресторан никто не пойдёт!', 'Nobody will go to your restaurant!', [(47, 'К вам же никто ходить не будет')], ''),
    ('elena', 'Мы ещё посмотрим, чья кухня лучше!', 'We will see whose kitchen is better!', [(49, 'Это мы еще посмотрим')], ''),
    ('barinov', 'Мой ресторан всегда будет первым!', 'My restaurant will always be first!', [(49, 'Это мы еще посмотрим')], ''),
    ('elena', 'Тогда попробуйте эти красивые яблоки.', 'Then try these beautiful apples.', [(50, 'ну попробуйте яблочки'), (52, 'Красивые')], ''),
    ('elena', 'Ой, какие кислые эти яблоки!', 'Oh, how sour these apples are!', [(53, 'Боже мой, какая кислятина')], ''),
    ('barinov', 'Надо уметь выбирать хорошие фрукты!', 'One must know how to choose good fruit!', [(54, 'Попробуйте хорошие яблоки')], ''),
    ('barinov', 'Учитесь, пока я добрый шеф!', 'Learn while I am a kind chef!', [(55, 'Ну')], ''),
]
WALK = [
    (0, None, "'Good morning, Chef Viktor Petrovich!' First name plus father's name is the respectful way to address someone. Petrovich means 'son of Pyotr'."),
    (1, None, "'Good morning, Elena Pavlovna.' For a woman the father's name ends in -ovna or -evna, so Pavlovna is 'daughter of Pavel'. Barinov answers in the same formal style."),
    (2, None, "'Why did you come to this market?' Polite vy takes a plural verb even for one person, so it's vy prishli. Na rynok, 'to the market', uses na, not v, the way Russians go na rabotu, to work."),
    (3, None, '\'I am choosing the best fresh vegetables.\' "Samye luchshie", \'the very best\', stacks \'most\' on top of \'best\' for emphasis. Every word in the phrase ends in -ie, the plural, to match ovoshchi.'),
    (4, None, '\'And did you decide to make your husband borscht?\' "Muzhu", \'for the husband\', is muzh with -u for the person who benefits. "Svarit\'" means to cook by boiling, which is how borscht gets made.'),
    (5, None, '\'No, I am opening a new expensive restaurant.\' "Otkryvayu", \'I\'m opening\', is from otkryvat\', the same verb you\'d use for a door or a shop. "Novyy" and dorogoy match restoran, which is masculine.'),
    (6, None, '\'I am preparing a new menu myself.\' Sama, \'myself\', is the woman\'s form; Barinov would say sam. "Gotovlyu", \'I\'m preparing\', is just as often plain \'I cook\'.'),
    (7, None, '\'Nobody will go to your restaurant!\' "Nikto ne poydyot" is \'nobody not will go\': with nikto the ne is required. V vash restoran uses v for going into a place.'),
    (8, None, '\'We will see whose kitchen is better!\' My yeshchyo posmotrim, literally \'we will still see\', is the standard \'we\'ll see about that\'. "Chya", \'whose\', is feminine to agree with kukhnya.'),
    (9, None, "'My restaurant will always be first!' After budet, 'will be', the word pervyy changes to pervym. That -ym ending is common after forms of 'to be'."),
    (10, None, '\'Then try these beautiful apples.\' "Poprobuyte", \'try\', ends in -yte, the polite command. One apple is yabloko; several are yabloki.'),
    (11, None, '\'Oh, how sour these apples are!\' In an exclamation, kakie, \'what kind of\', works like \'how\'. "Kislyy", sour, is related to kislota, acid.'),
    (12, None, '\'One must know how to choose good fruit!\' Nado, \'it is necessary\', plus a verb is the simplest way to say \'one must\'. "Umet\'" means to know how, as a skill, unlike znat\', to know a fact.'),
    (13, None, '\'Learn while I am a kind chef!\' Here poka is \'while\', the same poka you use for \'bye\'. "Uchites\'", \'learn\', ends in -tes\', the polite vy ending.'),
]
