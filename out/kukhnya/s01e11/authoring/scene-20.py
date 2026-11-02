# Authoring module for kukhnya-s01e11-scene-20.
ID = 'kukhnya-s01e11-scene-20'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 11
SCENE = 20
TITLE = 'Отказ от салата  (Rejecting the Salad)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.11'
SOURCE_FILE = 'sources/kukhnya/s01/e11.ru.dual.srt'
INTRO = "The critic at Nastya's table has sent back the salad, and now he wants soup. Vika brings the demand to the kitchen, and Barinov has his own rules. Here they are, in Russian."
OPENER = "Let's go through it again, line by line."
TRANSITION = 'And now without my interruptions.'
OUTRO = 'The chef will not serve the critic ahead of the others, and Vika can do nothing about it. In his kitchen, the queue is the law. See you next time.'
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('vika', 'Витя, у нас срочная проблема!', 'Vitya, we have an urgent problem!', [], ''),
    ('barinov', 'Вика, не кричи на кухне.', 'Vika, do not shout in the kitchen.', [], ''),
    ('vika', 'Критик за столиком отказался от салата.', 'The critic at the table refused the salad.', [(273, 'Критик отказался от блюда.')], ''),
    ('barinov', 'Почему? Мой салат был свежий.', 'Why? My salad was fresh.', [], ''),
    ('vika', 'Он говорит, что не ест траву.', 'He says that he does not eat grass.', [(266, 'Настенька, я траву не ем.')], ''),
    ('vika', 'Он требует горячий суп прямо сейчас.', 'He demands hot soup right now.', [(276, 'но он хочет супа побыстрее.')], ''),
    ('barinov', 'Пусть сначала сделает нормальный заказ.', 'Let him make a normal order first.', [(278, 'Пробивайте чек, и только после этого мы будем готовить.')], ''),
    ('vika', 'Витя, ты в своём уме?', 'Vitya, are you out of your mind?', [(279, 'Ты в своем уме?')], ''),
    ('vika', 'Отдай ему суп с первого стола!', 'Give him the soup from table one!', [(279, 'Отдай ему этот суп.')], ''),
    ('barinov', 'Этот суп ждёт другой человек.', 'Another person is waiting for this soup.', [(280, 'Нет. Этот суп для другого гостя.')], ''),
    ('vika', 'Но критик напишет ужасный отзыв!', 'But the critic will write a terrible review!', [], ''),
    ('barinov', 'С меня хватит этих капризов.', 'I have had enough of these whims.', [(277, 'Все, с меня хватит. Пусть ждет.')], ''),
    ('barinov', 'Пусть ждёт суп по очереди.', 'Let him wait for soup in turn.', [(277, 'Пусть ждет.')], ''),
]
WALK = [
    (0, None, ["'Vitya, we have an urgent problem!' Vitya is the short, friendly form of Viktor, as Vika knows the chef very well. ", ('vika', 'срочная'), ', meaning urgent, has a feminine ending to match ', ('vika', 'проблема'), '.']),
    (1, None, ["'Vika, do not shout in the kitchen.' We can consider the speech: ", ('barinov', 'не'), ('barinov', 'кричи'), ' is the command Alisa gave her father not to shout. Barinov is the one who shouts the most. ', ('barinov', 'на'), ('barinov', 'кухне'), ' is on the kitchen.']),
    (2, None, ["'The critic at the table refused the salad.' Now let's focus on this line: ", ('vika', 'отказался'), ('vika', 'от'), ('vika', 'салата'), ' is refused from the salad. Here ', ('vika', 'отказался'), " has the masculine ending, matching the man's form of the verb Vika used about the woman guest."]),
    (3, None, ["'Why? My salad was fresh.' Now we can inspect the speech: ", ('barinov', 'был'), ' means was, which is the past tense of to be, which Russian drops in the present. ', ('barinov', 'свежий'), ' is fresh. Barinov is hurt.']),
    (4, None, ["'He says that he does not eat grass.' We can focus on the speech: ", ('vika', 'траву'), " is grass, the critic's word for the salad. ", ('vika', 'не'), ('vika', 'ест'), " is doesn't eat. Vika quotes him word for word."]),
    (5, None, ["'He demands hot soup right now.' Now we can look at this part: ", ('vika', 'требует'), ' means demands, and is a firm word, as the critic orders and does not ask. ', ('vika', 'горячий'), ('vika', 'суп'), ' is hot soup.']),
    (6, None, ["'Let him make a normal order first.' We can examine the words: ", ('barinov', 'Пусть'), ' is let him, followed by ', ('barinov', 'сделает'), ', he will make. ', ('barinov', 'сначала'), ' is first, and ', ('barinov', 'нормальный'), ' is normal.']),
    (7, None, ["'Vitya, are you out of your mind?' Russian says ", ('vika', 'ты'), ('vika', 'в'), ('vika', 'своём'), ('vika', 'уме'), ', meaning are you in your own mind, with ', ('vika', 'своём'), ' for own. It is the standard have you lost it phrase. Vika uses the informal ', ('vika', 'ты'), ' with the chef.']),
    (8, None, ["'Give him the soup from table one!' We can examine the speech: ", ('vika', 'Отдай'), ' is give away, which is the plain command used with the informal you. ', ('vika', 'с'), ('vika', 'первого'), ('vika', 'стола'), ' is from the first table.']),
    (9, None, ["'Another person is waiting for this soup.' The Russian puts the waiting person last, saying ", ('barinov', 'Этот'), ('barinov', 'суп'), ('barinov', 'ждёт'), ('barinov', 'другой'), ('barinov', 'человек'), ', meaning this soup waits another person. The term order puts weight on him.']),
    (10, None, ["'But the critic will write a terrible review!' Let's examine the speech: ", ('vika', 'отзыв'), ' means review, and is related to the verb to respond. ', ('vika', 'напишет'), ' is will write.']),
    (11, None, ["'I have had enough of these whims.' Russian says ", ('barinov', 'С'), ('barinov', 'меня'), ('barinov', 'хватит'), ', meaning from me is enough. The word for whims becomes ', ('barinov', 'капризов'), ' after it.']),
    (12, None, ["'Let him wait for soup in turn.' Think of a shop queue. The term for line becomes ", ('barinov', 'по'), ('barinov', 'очереди'), ' when it means taking turns. ', ('barinov', 'Пусть'), ' turns ', ('barinov', 'ждёт'), ', he waits, into an order about someone else: let him wait.']),
]
