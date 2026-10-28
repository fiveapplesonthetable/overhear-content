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
    ('vika', 'Отдай ему суп с первого стола!', 'Give him the soup from table one!', [(279, 'Отдай ему этот суп.')], ''),
    ('barinov', 'Ты в своём уме, Вика?', 'Are you out of your mind, Vika?', [(279, 'Ты в своем уме?')], ''),
    ('barinov', 'Этот суп ждёт другой человек.', 'Another person is waiting for this soup.', [(280, 'Нет. Этот суп для другого гостя.')], ''),
    ('vika', 'Но критик напишет ужасный отзыв!', 'But the critic will write a terrible review!', [], ''),
    ('barinov', 'С меня хватит этих капризов.', 'I have had enough of these whims.', [(277, 'Все, с меня хватит. Пусть ждет.')], ''),
    ('barinov', 'Пусть ждёт суп по очереди.', 'Let him wait for soup in turn.', [(277, 'Пусть ждет.')], ''),
]
WALK = [
    (0, None, '\'Vitya, we have an urgent problem!\' Vitya is the short, friendly form of Viktor; Vika knows the chef very well. "Srochnaya", "urgent", ends in -aya to match "problema".'),
    (1, None, '\'Vika, do not shout in the kitchen.\' "Ne krichi" is the command Alisa gave her father: "Papa, ne krichi na povarov". Barinov is the one who shouts the most. "Na kukhne" is "on the kitchen".'),
    (2, None, '\'The critic at the table refused the salad.\' "Otkazalsya ot salata" is "refused from the salad". Here it ends in -lsya, the man\'s form of Vika\'s "otkazalas" about the woman guest.'),
    (3, None, '\'Why? My salad was fresh.\' "Byl", "was", is the past of "to be", which Russian drops in the present. "Svezhy" is "fresh". Barinov is hurt.'),
    (4, None, '\'He says that he does not eat grass.\' "Travu" is "trava", "grass", the critic\'s word for the salad. "Ne est" is "doesn\'t eat". Vika quotes him word for word.'),
    (5, None, '\'He demands hot soup right now.\' "Trebuet", "demands", is a firm word: the critic orders and does not ask. "Goryachy sup" is "hot soup".'),
    (6, None, '\'Let him make a normal order first.\' "Pust" is "let him", followed by "sdelaet", "he will make". "Snachala" is "first". "Normalny" is easy.'),
    (7, None, '\'Give him the soup from table one!\' "Otday", "give away", is the plain command for "ty", the "you" Vika uses with the chef. "S pervogo stola" is "from the first table".'),
    (8, None, '\'Are you out of your mind, Vika?\' Russian says "ty v svoyom ume?", "are you in your own mind?", with "svoyom" for "own". It\'s the standard "have you lost it". Barinov uses "ty" with her.'),
    (9, None, '\'Another person is waiting for this soup.\' The Russian puts the waiting person last: "etot sup zhdyot drugoy chelovek", "this soup waits another person". The word order puts weight on him.'),
    (10, None, '\'But the critic will write a terrible review!\' "Otzyv", "review", is related to "otozvatsya", "to respond". "Napishet" is "will write".'),
    (11, None, '\'I have had enough of these whims.\' Russian says "s menya khvatit", "from me is enough". "Kaprizy", "whims", becomes "kaprizov" after it.'),
    (12, None, '\'Let him wait for soup in turn.\' "Po ocheredi" is "in turn", from "ochered", "a queue". "Pust zhdyot" is "let him wait". Barinov\'s rule is first come, first served.'),
]
