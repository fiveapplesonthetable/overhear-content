# Authoring module for kukhnya-s01e18-scene-15.
ID = 'kukhnya-s01e18-scene-15'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 18
SCENE = 15
TITLE = 'Ошибочная бутылка  (The Wrong Bottle)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'kostya': 'Костя', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.18'
SOURCE_FILE = 'sources/kukhnya/s01/e18.ru.dual.srt'
INTRO = 'Max discovers Senya was poisoned by their fake cognac. Viktor asks Kostya for a bottle of cognac and accidentally takes the fake one. Let us listen to their conversation in Russian first.'
OPENER = 'Now let us examine the conversation line by line.'
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Max discovers Senya was poisoned by their fake cognac. Viktor asks Kostya for a bottle of cognac and accidentally takes the fake one. Next time you watch the episode, listen for the Russian expressions for 'just' and 'horror' — you will catch every word right away. See you next time!"
CLOSING = ('max', 'Пока!')
STORY = [
    ('max', 'Костя, это просто ужас!', 'Kostya, this is just a nightmare!', [(285, 'просто')], ''),
    ('max', 'Сеня отравился нашим коньяком.', 'Senya got poisoned by our cognac.', [(281, 'что Сеня отравился этим коньяком.')], ''),
    ('kostya', 'О нет, что делать?', 'Oh no, what to do?', [], ''),
    ('barinov', 'Костя, дай мне бутылку коньяка.', 'Kostya, give me a bottle of cognac.', [(289, 'мне')], ''),
    ('barinov', 'Ту, которая стоит справа.', 'The one that stands on the right.', [], ''),
    ('kostya', 'Вот эту бутылку?', 'This bottle right here?', [(282, 'вот')], ''),
    ('barinov', 'Нет, дай мне другую. Да, эту.', 'No, give me another one. Yes, this one.', [(289, 'мне'), (289, 'мне')], ''),
    ('max', 'Шеф забрал наш коньяк!', 'Chef took our cognac!', [], ''),
    ('max', 'Надо забрать эту бутылку назад.', 'We need to take this bottle back.', [(291, 'Надо забрать бутылку, Костян.')], ''),
    ('kostya', 'Я не могу к нему подойти.', 'I can not approach him.', [(293, 'Я же не могу к ней подойти.')], ''),
    ('max', 'Давай, Костя, ты должен.', 'Come on, Kostya, you must.', [(294, 'Давай, Костян, давай, дружок.')], ''),
    ('max', 'Понятно, давай дальше.', "Got it, let's move on.", [], ''),
]
WALK = [
    (0, None, "'Kostya, this is just a nightmare!' Max panics completely, describing the situation as an absolute disaster."),
    (1, None, "'Senya got poisoned by our cognac.' He delivers the terrible news that their fake drink actually made someone sick."),
    (2, None, "'Oh no, what to do?' Kostya sounds incredibly worried, desperately asking for a quick solution."),
    (3, None, "'Kostya, give me a bottle of cognac.' Chef Barinov demands a drink, snapping an urgent command at the bartender."),
    (4, None, "'The one that stands on the right.' He specifically points out the exact one he wants from the shelf."),
    (5, None, "'This bottle right here?' Kostya tries to double check, hoping he can give him a safe option instead."),
    (6, None, "'No, give me another one. Yes, this one.' Chef Barinov rejects the offer and firmly points to the exact one he asked for."),
    (7, None, "'Chef took our cognac!' Max watches in horror as their boss walks away with the dangerous drink."),
    (8, None, "'We need to take this bottle back.' He realizes they have to fix this immediately before things get worse."),
    (9, None, "'I can not approach him.' Kostya nervously admits he is too scared to go up and take it away."),
    (10, None, "'Come on, Kostya, you must.' Max pushes him to act, insisting there is no other choice right now."),
    (11, None, "'Got it, let's move on.' Realizing the urgency, Max tells him to hurry up and handle the problem."),
]
