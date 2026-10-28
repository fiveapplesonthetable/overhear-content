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
INTRO = "Early in the morning, Viktor takes Max along to the bustling fish market. Determined to teach his young apprentice a vital culinary skill, Viktor demonstrates how to detect stale fish from a vendor's subtle gestures. Let's listen to their lesson in Russian first."
OPENER = "Now let's examine the conversation line by line."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Having exposed the vendor's dishonest sales tactics, Viktor and Max continue through the market, ready to return to Claude Monet with fresh knowledge. Next time you watch the episode, listen for the Russian expressions for 'to come' and 'rotten' — you will catch every word right away. See you next time!"
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
    (0, None, "'I stepped in a rotten plum, chef.' Max admits his clumsy mistake of stepping on a 'rotten plum'."),
    (1, None, "'Quit whining, I am in a good mood.' Barinov shuts down the whining immediately, declaring he is in a good mood."),
    (2, None, "'Today you will learn the art of buying fish.' Barinov announces his intention to teach his apprentice the art of buying fish."),
    (3, None, "'How many days old is this fish, Max?' Barinov quizzes his student by asking how old the fish in front of them is."),
    (4, None, "'The seller says they brought it today.' Max relays what the market seller told him about the fresh delivery today."),
    (5, None, "'Watch closely, he pursed his lips.' Barinov instructs him to observe the seller carefully, pointing out the pursed lips."),
    (6, None, "'That means this fish is at least three days old.' Barinov interprets the body language to mean the fish is at least three days old."),
    (7, None, "'And now he scratched his nose.' Barinov points out another gesture as the seller scratches his nose."),
    (8, None, "'This fish is already five days old.' Barinov explains that the nose scratch adds two more days, making it five."),
    (9, None, "'And it was definitely frozen before.' Barinov points out that the fish has also been frozen before."),
    (10, None, "'Chef, you are a true master of your craft.' Max flatters his boss by calling him a true master."),
    (11, None, "'Learn from me while I am kind.' Barinov tells him to take advantage of his good mood and learn."),
    (12, None, "'Thank you for this important lesson, chef.' Max expresses his gratitude for the important lesson."),
]
