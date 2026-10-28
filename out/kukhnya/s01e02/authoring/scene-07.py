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
OUTRO = 'Max has been sent back to the kitchen, and the coffee machine is safe at last. You\'ve learned a good Russian jab: "tozhe mne", "some ... you are".'
CLOSING = ('sasha', 'Пока!')
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
    (0, None, '\'What are you even doing here?\' "Voobshche" adds "even" or "at all" and gives the question an edge. "Tut" is the casual "here".'),
    (1, None, '\'I am just brewing coffee for the guests.\' "Varyu" is the same boiling verb as "vari kofe" in the last scene. After "dlya", for, "gosti" becomes "gostey".'),
    (2, None, '\'You spilled milk all over the counter!\' You can hear the pieces in "razlil": "raz-", apart, and "lil", poured. So the milk went everywhere.'),
    (3, None, '\'I wanted to show a neat trick.\' "Khotel pokazat\'" is "wanted to show", two verbs side by side. "Fokus" is a trick, as in a magic trick.'),
    (4, None, '\'Some bartender you are!\' "Tozhe mne" in front of a noun is Russian for "some ... you are!". It\'s literally "also to me", and you can put almost any noun after it.'),
    (5, None, '\'Every master makes mistakes.\' Russian puts it as "at every master there happen mistakes". "Byvayut" means "happen from time to time", and "u kazhdogo" is "at each".'),
    (6, None, '\'Get lost, go on, I will do everything myself.\' "Provalivay" is a rude "scram", from "provalit\'sya", to fall through. "Sama", "myself", ends in -a because Sasha is a woman.'),
    (7, None, '\'All right, I had better go to the kitchen.\' "Ya luchshe poydu" is "I better will go", the same "luchshe" Max used to turn down a seat.'),
    (8, None, '\'And never touch the coffee machine again!\' "Bol\'she nikogda ne" is "more never not": "nikogda" and "ne" both say no, and Russian is happy with that. "Kofemashina" is "coffee" and "machine" stuck together.'),
    (9, None, '\'The kitchen is definitely closer to my heart than this bar.\' "Mne blizhe" is "to me closer". "Chem" is "than", and "tochno" is "definitely".'),
    (10, None, '\'Then go help the cooks.\' "Vot i idi" is "well, go then". "Povaram", "to the cooks", has the "-am" ending that means "to" for a group.'),
    (11, None, '\'Leaving already, bar boss!\' "Uzhe ukhozhu" is "already I\'m leaving". "Shef bara" is "chef of the bar": "bar" adds an -a for "of".'),
]
