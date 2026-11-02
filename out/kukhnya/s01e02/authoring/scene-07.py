# Authoring module for kukhnya-s01e02-scene-07.
ID = 'kukhnya-s01e02-scene-07'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 2
SCENE = 7
TITLE = 'Тоже мне бармен  (Some Bartender You Are)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'max': 'Макс', 'sasha': 'Саша'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.02'
SOURCE_FILE = 'sources/kukhnya/s01/e02.ru.dual.srt'
INTRO = "Max's bartending career has not gone well. There is spilled milk all over the counter, and Sasha, a waitress, arrives and is not impressed. Here is the exchange in Russian first."
OPENER = 'Back to the spilled milk.'
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'Max has been sent back to the kitchen, and the coffee machine is safe at last. You\'ve learned a good Russian jab for "some ... you are".'
STORY = [
    ('sasha', 'Что ты тут вообще делаешь?', 'What are you even doing here?', [], ''),
    ('max', 'Я просто варю кофе для гостей.', 'I am just brewing coffee for the guests.', [], ''),
    ('sasha', 'Ты разлил молоко на всю стойку!', 'You spilled milk all over the counter!', [], ''),
    ('max', 'Я хотел показать красивый фокус.', 'I wanted to show a neat trick.', [], ''),
    ('sasha', 'Тоже мне бармен!', 'Some bartender you are!', [(108, 'Тоже мне бармен')], ''),
    ('max', 'У каждого мастера бывают ошибки.', 'Every master makes mistakes.', [], ''),
    ('sasha', 'Проваливай, давай, я сама всё сделаю.', 'Get lost, go on, I will do everything myself.', [(109, 'Проваливай, давай, я сама сделаю')], ''),
    ('max', 'Ладно, я лучше пойду на кухню.', 'All right, I had better go to the kitchen.', [], ''),
    ('sasha', 'И больше никогда не трогай кофемашину!', 'And never touch the coffee machine again!', [], ''),
    ('max', 'Кухня мне точно ближе, чем этот бар.', 'The kitchen is definitely closer to my heart than this bar.', [], ''),
    ('sasha', 'Вот и иди помогать поварам.', 'Then go help the cooks.', [], ''),
    ('max', 'Уже ухожу, шеф бара!', 'Leaving already, bar boss!', [], ''),
]
WALK = [
    (0, None, [
        "'What are you even doing here?' The word for 'even' or 'at all' is ",
        ('sasha', 'вообще'),
        ", and it gives the question an edge. The casual word for 'here' is ",
        ('sasha', 'тут'),
        "."
    ]),
    (1, None, [
        "'I am just brewing coffee for the guests.' The action word ",
        ('max', 'варю'),
        " translates to 'brewing', the same boiling action as in the last scene. After the little word for 'for', ",
        ('max', 'для'),
        ", the guests become ",
        ('max', 'гостей.'),
        "."
    ]),
    (2, None, [
        "'You spilled milk all over the counter!' The word for 'spilled' is ",
        ('sasha', 'разлил'),
        ". It is built from 'apart' and 'poured', so the milk went everywhere."
    ]),
    (3, None, [
        "'I wanted to show a neat trick.' ",
        ('max', 'хотел показать'),
        " translates to 'wanted to show', two action words side by side. The word for a trick, as in a magic trick, is ",
        ('max', 'фокус.'),
        "."
    ]),
    (4, None, [
        "'Some bartender you are!' The phrase ",
        ('sasha', 'Тоже мне'),
        " in front of a naming word is Russian for 'some ... you are!'. It is literally 'also to me', and you can put almost any naming word after it."
    ]),
    (5, None, [
        "'Every master makes mistakes.' It literally translates to 'at every master there happen mistakes'. The action word ",
        ('max', 'бывают'),
        " means 'happen from time to time', and ",
        ('max', 'У каждого'),
        " translates to 'at each'."
    ]),
    (6, None, [
        "'Get lost, go on, I will do everything myself.' The action word ",
        ('sasha', 'Проваливай,'),
        " translates to a rude 'scram', built from falling through. The word for 'myself', ",
        ('sasha', 'сама'),
        ", ends in an 'a' sound because Sasha is a woman."
    ]),
    (7, None, [
        "'All right, I had better go to the kitchen.' ",
        ('max', 'я лучше пойду'),
        " translates to 'I better will go'. The word for 'better', ",
        ('max', 'лучше'),
        ", is the same one Max used to turn down a seat."
    ]),
    (8, None, [
        "'And never touch the coffee machine again!' The phrase ",
        ('sasha', 'больше никогда не'),
        " literally translates to 'more never not', with two negative words, and Russian is happy with that. The word for 'coffee machine' is ",
        ('sasha', 'кофемашину!'),
        ", built from 'coffee' and 'machine' stuck together."
    ]),
    (9, None, [
        "'The kitchen is definitely closer to my heart than this bar.' Max never actually says 'heart'. He says the kitchen is 'closer to me', with ",
        ('max', 'мне'),
        " doing the work of 'to me', and ",
        ('max', 'чем'),
        " brings in the thing he compares it with, the word for 'than'."
    ]),
    (10, None, [
        "'Then go help the cooks.' ",
        ('sasha', 'Вот и иди'),
        " translates to 'well, go then'. The word for 'to the cooks', ",
        ('sasha', 'поварам.'),
        ", has a special ending that means 'to' for a group."
    ]),
    (11, None, [
        "'Leaving already, bar boss!' Said halfway out the door: ",
        ('max', 'ухожу,'),
        " translates to 'I am leaving' right now, exactly like the English. In ",
        ('max', 'шеф бара!'),
        ", the word for 'bar' picks up an extra ending that means 'of'."
    ]),
]
CLOSING = ("max", "Пока!")
