# Authoring module for kukhnya-s01e17-scene-01.
ID = 'kukhnya-s01e17-scene-01'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 17
SCENE = 1
TITLE = 'Уроки на рынке  (Market Lessons)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.17'
SOURCE_FILE = 'sources/kukhnya/s01/e17.ru.dual.srt'
INTRO = "Welcome to Kukhnya, which means 'The Kitchen', a Russian comedy set in Claude Monet, a smart Moscow restaurant. Chef Viktor Barinov rules the kitchen, and young Max Lavrov is the cook he loves to boss around. This morning Barinov drags Max to the market to teach him how to tell whether a fish is fresh. First the Russian, and don't worry about catching every word."
OPENER = "Now we'll go back through it slowly."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Barinov has read the seller like a book, and Max is impressed, at least for now. Remember that Russians give an age with 'to': 'to this fish, five days'. See you next time!"
CLOSING = ('max', 'Пока!')
STORY = [
    ('max', 'Я наступил в гнилую сливу, шеф.', 'I stepped in a rotten plum, chef.', [(1, 'Я только чувствую, что я в гнилую сливу наступил.')], ''),
    ('barinov', 'Хватит ныть, у меня хорошее настроение.', 'Quit whining, I am in a good mood.', [(2, 'Хватит ныть. У меня хорошее настроение.')], ''),
    ('barinov', 'Сегодня ты узнаешь искусство покупать рыбу.', 'Today you will learn the art of buying fish.', [(3, 'Поэтому ты познаешь сейчас древнее искусство покупать на рынке.')], ''),
    ('barinov', 'Сколько дней этой рыбе, Макс?', 'How many days old is this fish, Max?', [(4, 'Как ты думаешь, сколько дней этой треске?')], ''),
    ('max', 'Продавец говорит, что привезли сегодня.', 'The seller says they brought it today.', [(7, 'Один. Сегодня привезли.')], ''),
    ('barinov', 'Смотри внимательно, он поджал губы.', 'Watch closely, he pursed his lips.', [(8, 'Смотри внимательно.'), (10, 'Смотри, губы поджал.')], ''),
    ('barinov', 'Значит, этой рыбе минимум три дня.', 'That means this fish is at least three days old.', [(11, 'Это значит, что рыбе не менее трех дней.')], ''),
    ('barinov', 'А сейчас он почесал нос.', 'And now he scratched his nose.', [(13, 'О, нос почесал.')], ''),
    ('barinov', 'Этой рыбе уже пять дней.', 'This fish is already five days old.', [(13, 'Это значит, что рыбе не меньше пяти дней.')], ''),
    ('barinov', 'И её точно замораживали раньше.', 'And it was definitely frozen before.', [(14, 'Да еще ее замораживали.')], ''),
    ('max', 'Шеф, вы настоящий мастер своего дела.', 'Chef, you are a true master of your craft.', [], ''),
    ('barinov', 'Учись у меня, пока я добрый.', 'Learn from me while I am kind.', [], ''),
    ('max', 'Спасибо за этот важный урок, шеф.', 'Thank you for this important lesson, chef.', [], ''),
]
WALK = [
    (0, None, "'I stepped in a rotten plum, chef.' 'Rotten' comes from the verb for rotting, and the plum ends in 'u' because Max stepped into it. The 'l' on the end of 'stepped' says it's a man speaking."),
    (1, None, "'Quit whining, I'm in a good mood.' The opening word means 'enough' and is followed by the plain 'whine', a slangy one. 'At me good mood' is how Russian says 'I'm in a good mood'."),
    (2, None, "'Today you will learn the art of buying fish.' 'Art' is followed by the plain 'to buy', with no 'of' in between. 'Fish' takes a 'u' ending as the thing being bought."),
    (3, None, "'How many days old is this fish, Max?' Russian gives an age with 'to': literally 'to this fish how many days'. After 'how many', 'days' takes a special plural."),
    (4, None, "'The seller says they brought it today.' 'They brought' has the 'li' ending with no 'they', which is how Russian says 'it was brought'. The verb is the one for bringing by vehicle."),
    (5, None, "'Watch closely, he pursed his lips.' 'Watch' is a casual command, and 'closely' is a describing word ending in 'o'. 'Lips' is always plural in Russian."),
    (6, None, "'That means this fish is at least three days old.' The first word is 'it means', used here as 'so' or 'in other words'. After 'three', 'days' changes again, to a shorter form."),
    (7, None, "'And now he scratched his nose.' The 'po' on the front of 'scratch' means he did it briefly. Barinov reads a scratch of the nose like a confession."),
    (8, None, "'This fish is already five days old.' After 'five' the days switch back to the longer form, just like after 'how many'. Two, three or four days take the short one, and five or more take the long."),
    (9, None, "'And it was definitely frozen before.' 'They froze' is built on the word for frost, and again has no 'they'. 'Definitely' and 'before' are tiny words, easy to lift into other sentences."),
    (10, None, "'Chef, you're a real master of your craft.' 'Real' is also 'present', as in the present moment. 'Of your own business' is a phrase for a trade, and 'business' is a very common one."),
    (11, None, "'Learn from me while I'm kind.' 'While' is spelled and said like the casual 'bye', so it does double duty. 'From me' uses the same little word as 'at me'."),
    (12, None, "'Thank you for this important lesson, chef.' 'Thanks for' needs a small word for 'for', then the lesson with its masculine endings. It's the polite, schoolboy thanks."),
]
