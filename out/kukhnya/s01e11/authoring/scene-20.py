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
INTRO = 'In the kitchen of Claude Monet, Victoria rushes to Chef Viktor with alarming news: the restaurant critic has rejected his fresh salad and is demanding hot soup immediately. Victoria urges Viktor to give the critic a soup meant for another guest, but the proud chef adamantly refuses to break the rules. Listen to their conversation in Russian first, then we will break down each line in English.'
OPENER = "Now let's go back through the exchange around Rejecting the Salad line by line and unpack how the Russian works."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "In the kitchen, Victoria urges Chef Viktor to give the complaining critic another customer's soup, but Viktor refuses to bypass ordinary guests. Next time you watch the episode, listen for the Russian expressions for 'to be enough' and 'kitchen' — you will catch every word right away. See you next time!"
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('vika', 'Виктор Петрович, у нас срочная проблема!', 'Viktor Petrovich, we have an urgent problem!', [], ''),
    ('barinov', 'Вика, не кричи на кухне.', 'Vika, do not shout in the kitchen.', [], ''),
    ('vika', 'Критик за столиком отказался от салата.', 'The critic at the table refused the salad.', [(273, 'Критик отказался от блюда.')], ''),
    ('barinov', 'Почему? Мой салат был свежий.', 'Why? My salad was fresh.', [], ''),
    ('vika', 'Он говорит, что не ест траву.', 'He says that he does not eat grass.', [(266, 'Настенька, я траву не ем.')], ''),
    ('vika', 'Он требует горячий суп прямо сейчас.', 'He demands hot soup right now.', [(276, 'но он хочет супа побыстрее.')], ''),
    ('barinov', 'Пусть сначала сделает нормальный заказ.', 'Let him make a normal order first.', [(278, 'Пробивайте чек, и только после этого мы будем готовить.')], ''),
    ('vika', 'Отдайте ему суп с первого стола!', 'Give him the soup from table one!', [(279, 'Отдай ему этот суп.')], ''),
    ('barinov', 'Ты в своём уме, Вика?', 'Are you out of your mind, Vika?', [(279, 'Ты в своем уме?')], ''),
    ('barinov', 'Этот суп ждёт другой человек.', 'Another person is waiting for this soup.', [(280, 'Нет. Этот суп для другого гостя.')], ''),
    ('vika', 'Но критик напишет ужасный отзыв!', 'But the critic will write a terrible review!', [], ''),
    ('barinov', 'С меня хватит этих капризов.', 'I have had enough of these whims.', [(277, 'Все, с меня хватит. Пусть ждет.')], ''),
    ('barinov', 'Пусть ждёт суп по очереди.', 'Let him wait for soup in turn.', [(277, 'Пусть ждет.')], ''),
]
WALK = [
    (0, None, "'Viktor Petrovich, we have an urgent problem!' Vika rushes in to announce an urgent problem to the chef. She is panicking about the situation."),
    (1, None, "'Vika, do not shout in the kitchen.' Barinov calmly tells the manager not to shout in his kitchen. He hates loud noises while cooking."),
    (2, None, "'The critic at the table refused the salad.' Vika explains that the famous critic rejected his salad order. This is a very bad sign."),
    (3, None, "'He says that he does not eat grass.' Vika repeats the guest's rude words about not eating grass. He is being incredibly picky."),
    (4, None, "'He demands hot soup right now.' Vika says the man demands hot soup immediately instead. He wants it right this second."),
    (5, None, "'Give him the soup from table one!' Vika begs the chef to just give him the soup meant for another table. She wants to fix the problem fast."),
    (6, None, "'Are you out of your mind, Vika?' Barinov asks if she has lost her mind. He is shocked by her crazy suggestion."),
    (7, None, "'Another person is waiting for this soup.' Barinov points out that another customer is waiting for that exact bowl. It belongs to someone else."),
    (8, None, "'But the critic will write a terrible review!' Vika reminds him about the terrible review they might get. She thinks they should prioritize this VIP."),
    (9, None, "'Let him wait for soup in turn.' Barinov stubbornly refuses and says the man can wait his turn. He treats everyone exactly the same."),
]
