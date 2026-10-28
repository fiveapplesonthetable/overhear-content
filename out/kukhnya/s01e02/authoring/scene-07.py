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
INTRO = 'At the bar counter of Claude Monet, Max has made a mess while attempting to brew coffee. Waitress Sasha arrives, surveys the spilled milk, and orders him away from the machine. Listen to their playful conversation in Russian first, and then we will review it in English.'
OPENER = "Let's review this encounter at the bar line by line."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'Relieved of his bartending duties, Max heads back to the kitchen, leaving coffee preparation to the professionals. See you next time!'
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
    (0, None, "'What are you even doing here?' Sasha asks Max with deep skepticism as she enters the bar area."),
    (1, None, "'I am just brewing coffee for the guests.' Max defends his unauthorized attempt to operate the coffee machine."),
    (2, None, "'You spilled milk all over the counter!' Sasha points out the messy puddle on the wooden bar surface."),
    (3, None, "'I wanted to show a neat trick.' Max explains his failed bottle routine with a guilty smile."),
    (4, None, "'Some bartender you are!' Sasha mocks his nonexistent bartending credentials."),
    (5, None, "'Every master makes mistakes.' Max offers a humorous justification for the little accident."),
    (6, None, "'Get lost, go on, I will do everything myself.' Sasha takes over the coffee machine to serve the patrons."),
    (7, None, "'All right, I had better go to the kitchen.' Max recognizes that his bartending career has come to an end."),
    (8, None, "'And never touch the coffee machine again!' Sasha firmly establishes the boundaries of the restaurant floor."),
    (9, None, "'The kitchen is definitely closer to my heart than this bar.' Max finds solace in his true culinary calling."),
    (10, None, "'Then go help the cooks.' Sasha sends him back where he belongs before Chef notices his absence."),
    (11, None, "'Leaving already, bar boss!' Max departs with a playful salute before retreating to the kitchen."),
]
