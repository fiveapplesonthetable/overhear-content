# Authoring module for kukhnya-s01e10-scene-34.
ID = 'kukhnya-s01e10-scene-34'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 10
SCENE = 34
TITLE = 'Проверка икры  (Checking the Caviar)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'fedya': 'Федя', 'senya': 'Сеня'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.10'
SOURCE_FILE = 'sources/kukhnya/s01/e10.ru.dual.srt'
INTRO = 'In the Claude Monet kitchen, Fedya and Senya finish preparing the caviar for the VIP table. Fedya inspects the bowl and worries they did not add enough dye, but Senya insists it looks perfectly authentic. Listen to their conversation in Russian first, then we will break down each line in English.'
OPENER = "Now let's go back through the exchange around Checking the Caviar line by line and unpack how the Russian works."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "In the kitchen, Fedya worries they did not add enough black dye to the caviar, but Senya reassures him that it looks completely authentic before sending it to the dining room. Next time you watch the episode, listen for the Russian expressions for 'real' and 'suddenly' — you will catch every word right away. See you next time!"
CLOSING = ('senya', 'Пока!')
STORY = [
    ('fedya', 'Сеня, подойди сюда на секунду.', 'Senya, come over here for a second.', [], ''),
    ('senya', 'Что такое, Федя? Всё готово?', 'What is it, Fedya? Is everything ready?', [], ''),
    ('fedya', 'Мне кажется, мы её не докрасили.', 'I think we did not finish dyeing it.', [(244, 'Мне кажется, мы её не докрасили.')], ''),
    ('senya', 'Да брось, она абсолютно чёрная!', 'Come on, it is completely black!', [], ''),
    ('fedya', 'А вдруг шеф увидит светлые икринки?', 'What if Chef sees light caviar eggs?', [], ''),
    ('senya', 'Никто ничего подозрительного не заметит.', 'Nobody will notice anything suspicious.', [], ''),
    ('senya', 'Если бы икра не была настоящей,', 'If the caviar were not like real caviar,', [(245, 'Если бы икра не была похожа на настоящую,')], ''),
    ('senya', 'ты бы сам её сейчас не пробовал.', 'you would not be tasting it yourself right now.', [(246, 'Сеня бы ее не спер.')], ''),
    ('fedya', 'Ладно, ладно, ты меня убедил.', 'All right, all right, you convinced me.', [], ''),
    ('senya', 'Тогда зови официанта, пора подавать блюдо.', 'Then call the waiter, it is time to serve the dish.', [], ''),
    ('fedya', 'Официант, забирай заказ на первый стол!', 'Waiter, take the order for table one!', [], ''),
    ('senya', 'Давай, выносим икру в зал.', 'Come on, let us bring the caviar into the hall.', [(248, 'выносим икру.')], ''),
]
WALK = [
    (0, None, "'Senya, come over here for a second.' Before sending the caviar out, Fedya calls Senya over for one last check."),
    (1, None, "'I think we did not finish dyeing it.' Squinting at the bowl, Fedya worries that they missed a few yellow spots."),
    (2, None, "'Come on, it is completely black!' Senya waves the concern away, insisting the roe is pitch black."),
    (3, None, "'What if Chef sees light caviar eggs?' Fedya asks nervously what will happen if the chef spots any pale grains."),
    (4, None, "'Nobody will notice anything suspicious.' Senya assures him that nobody is going to notice anything odd."),
    (5, None, "'All right, all right, you convinced me.' Reluctantly convinced, Fedya gives in."),
    (6, None, "'Then call the waiter, it is time to serve the dish.' Senya tells him to call the waiter over because it is time to serve the VIP table."),
    (7, None, "'Come on, let us bring the caviar into the hall.' With a deep breath, they send the dyed caviar out into the dining room. Now listen to the full conversation once more."),
]
