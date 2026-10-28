# Authoring module for kukhnya-s01e17-scene-01.
ID = 'kukhnya-s01e17-scene-01'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 17
SCENE = 1
TITLE = 'Уроки на рынке  (Market Lessons)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'senya': 'Сеня', 'seller': 'Продавец'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.17'
SOURCE_FILE = 'sources/kukhnya/s01/e17.ru.dual.srt'
INTRO = "Welcome to Kukhnya, which means 'The Kitchen', a Russian comedy set in Claude Monet, a smart Moscow restaurant. Chef Viktor Barinov rules the kitchen, and Senya is one of the cooks he loves to boss around. This morning Barinov drags Senya to the market to teach him how to tell whether a fish is fresh. Listen to the lesson in Russian first, and watch how much Barinov reads from one face."
OPENER = "Now let's take it slowly, and see how Barinov reads a fish seller."
TRANSITION = 'Now the market lesson again, start to finish.'
OUTRO = 'Barinov has read the seller like a book, and the seller is not pleased about it. Remember that Russians give an age with \'to\': "etoy rybe pyat dney", to this fish, five days. See you next time!'
CLOSING = ('senya', 'До свидания!')
STORY = [
    ('senya', 'Я наступил в гнилую сливу, шеф.', 'I stepped in a rotten plum, chef.', [(1, 'Я только чувствую, что я в гнилую сливу наступил.')], ''),
    ('barinov', 'Хватит ныть, у меня хорошее настроение.', 'Quit whining, I am in a good mood.', [(2, 'Хватит ныть. У меня хорошее настроение.')], ''),
    ('barinov', 'Сегодня ты узнаешь искусство покупать рыбу.', 'Today you will learn the art of buying fish.', [(3, 'Поэтому ты познаешь сейчас древнее искусство покупать на рынке.')], ''),
    ('barinov', 'Как ты думаешь, сколько дней этой рыбе?', 'How many days old do you think this fish is?', [(4, 'Как ты думаешь, сколько дней этой треске?')], ''),
    ('barinov', 'Не так. Учись у меня.', 'Not like that. Learn from me.', [(5, 'Да не так.'), (6, 'Учись.')], ''),
    ('seller', 'Один день. Сегодня привезли.', 'One day. It came in today.', [(7, 'Один. Сегодня привезли.')], ''),
    ('barinov', 'Смотри внимательно, он поджал губы.', 'Watch closely, he pursed his lips.', [(8, 'Смотри внимательно.'), (10, 'Смотри, губы поджал.')], ''),
    ('barinov', 'Значит, этой рыбе минимум три дня.', 'That means this fish is at least three days old.', [(11, 'Это значит, что рыбе не менее трех дней.')], ''),
    ('seller', 'Какие три? Ей максимум два.', 'Three? Come on, it is two at most.', [(12, 'Да какие три? Ну, ей максимум два.')], ''),
    ('barinov', 'А сейчас он почесал нос.', 'And now he scratched his nose.', [(13, 'О, нос почесал.')], ''),
    ('barinov', 'Этой рыбе уже пять дней.', 'This fish is already five days old.', [(13, 'Это значит, что рыбе не меньше пяти дней.')], ''),
    ('barinov', 'И её точно замораживали раньше.', 'And it was definitely frozen before.', [(14, 'Да еще ее замораживали.')], ''),
]
WALK = [
    (0, None, '\'I stepped in a rotten plum, chef.\' "Sliva", plum, becomes "slivu" after "v" when you step into it, and "gnilaya", rotten, follows it to "gniluyu".'),
    (1, None, '\'Quit whining, I\'m in a good mood.\' "Khvatit" means "enough", and the next word stays in its dictionary form: "khvatit nyt", enough whining. "U menya khoroshee nastroenie" is literally "at me, a good mood".'),
    (2, None, '\'Today you will learn the art of buying fish.\' Where English says "of buying", Russian just puts "pokupat", to buy, after "iskusstvo", art. "Ryba" becomes "rybu" as the thing being bought.'),
    (3, None, '\'How many days old do you think this fish is?\' Russian gives the age to the fish: "etoy rybe" means "to this fish", so the question is literally "how many days to this fish?". "Kak ty dumaesh" is "how do you think", where English says "what".'),
    (4, None, '\'Not like that. Learn from me.\' "Ne tak" is simply "not so". "Uchis u menya" is literally "learn at me": "u" plus a person is where you pick something up.'),
    (5, None, '\'One day. It came in today.\' "Privezli" has no "they" in front of it. The plural ending on its own says that somebody delivered it.'),
    (6, None, '\'Watch closely, he pursed his lips.\' "Podzhal guby" is "pressed lips", with no "his". Russian rarely says whose body part it is when that\'s obvious.'),
    (7, None, '\'That means this fish is at least three days old.\' "Znachit", it means, opens a conclusion. After "tri" the word for days is "dnya"; from five upwards it turns into "dney".'),
    (8, None, '\'Three? It\'s two at most.\' "Kakie tri?", literally "what three?", brushes a number aside. "Ey" is "to her": the fish, "ryba", is feminine, so its age goes to "her".'),
    (9, None, '\'And now he scratched his nose.\' "Chesat" is to scratch, and "po-" on the front makes it one quick scratch: "pochesal". Again there\'s no "his" before "nos".'),
    (10, None, '\'This fish is already five days old.\' Here comes "pyat dney", five days, with the ending promised a moment ago. "Uzhe" means "already": the fish gets older with every gesture.'),
    (11, None, '\'And it was definitely frozen before.\' "Zamorazhivali" is "they froze", again with no "they". "Tochno", for sure, is a little word you\'ll hear constantly.'),
]
