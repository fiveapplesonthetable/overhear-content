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
    (0, None, '\'What are you even doing here?\' The word "vobshche" adds "even" or "at all" and gives the question an edge. "Tut" is the casual "here".'),
    (1, None, '\'I am just brewing coffee for the guests.\' "Brewing" is the same cooking word as in the last scene. After "for", "guests" changes to a new shape.'),
    (2, None, '\'You spilled milk all over the counter!\' You can hear the pieces in "razlil": "raz-", apart, and "lil", poured. So the milk went everywhere.'),
    (3, None, '\'I wanted to show a neat trick.\' Two verbs side by side: "wanted" and "to show". The last word is "trick", as in a magic trick, and Max sounds proud.'),
    (4, None, '\'Some bartender you are!\' "Tozhe mne" in front of a noun is Russian for "some ... you are!". It\'s literally "also to me", and you can put almost any noun after it.'),
    (5, None, '\'Every master makes mistakes.\' The verb means "happen from time to time". Max puts it as "at every master there happen mistakes", which is more elegant than "makes".'),
    (6, None, '\'Get lost, go on, I will do everything myself.\' The first word is a rude "scram", close to "fall through". Sasha is a woman, so "myself" ends in -a.'),
    (7, None, '\'All right, I had better go to the kitchen.\' "I\'d better" is "better I\'ll go" in Russian, which is shorter than the English.'),
    (8, None, '\'And never touch the coffee machine again!\' Count the negatives: "more never not". Russian happily stacks them. The last word is "coffee" and "machine" stuck together.'),
    (9, None, '\'The kitchen is definitely closer to my heart than this bar.\' Max says "closer to me", and "than" is a small word. He is telling Sasha where he belongs.'),
    (10, None, '\'Then go help the cooks.\' "To the cooks" has the ending that means "to". The first two words are "so go", like "well, go then".'),
    (11, None, '\'Leaving already, bar boss!\' "Boss of the bar" is built with the second word in the "of" form. Max is making a joke at Sasha\'s expense.'),
]
