# Authoring module for kukhnya-s01e06-scene-14.
ID = 'kukhnya-s01e06-scene-14'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 6
SCENE = 14
TITLE = 'Торг здесь неуместен  (Bargaining Is Inappropriate)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kostya': 'Костя', 'rodion': 'Родион'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.06'
SOURCE_FILE = 'sources/kukhnya/s01/e06.ru.dual.srt'
INTRO = "In the staff changing room at Claude Monet, Rodion has the truffles and the upper hand. He wants a proper lunch in the restaurant, and Kostya is trying to talk him out of it. It's in Russian first."
OPENER = 'Slowly now. Rodion speaks like a gentleman, and Kostya gets more nervous with every line.'
TRANSITION = 'Now the bargaining from the start.'
OUTRO = 'Rodion speaks with old-world elegance even in the staff changing room, refusing to haggle and naming his price for the truffles: a proper meal in the dining room. See you next time.'
CLOSING = ('rodion', 'Пока!')
STORY = [
    ('kostya', 'Подожди, давай мы просто заплатим деньги.', "Wait, let's just pay you money.", [(197, 'мы тебе денег заплатим')], ''),
    ('rodion', 'Торг здесь совершенно неуместен, молодой человек.', 'Bargaining is completely inappropriate here, young man.', [(198, 'Торг здесь неуместен')], ''),
    ('kostya', 'Но это же очень дорогой ресторан!', 'But this is a very expensive restaurant!', [], ''),
    ('rodion', 'Я прекрасно знаю этот прекрасный ресторан.', 'I know this fine restaurant perfectly well.', [(199, 'Я обедаю в этом ресторане')], ''),
    ('kostya', 'Администратор сразу выгонит тебя на улицу.', 'The administrator will throw you out into the street immediately.', [], ''),
    ('rodion', 'В приличном костюме меня никто не узнает.', 'In a decent suit nobody will recognize me.', [], ''),
    ('kostya', 'А если ты случайно испортишь чужую одежду?', "And what if you accidentally ruin someone else's clothes?", [(196, 'если')], ''),
    ('rodion', 'Я обещаю вести себя крайне аккуратно.', 'I promise to behave extremely neatly.', [(198, 'Торг здесь неуместен')], ''),
    ('kostya', 'Где именно спрятаны наши пропавшие трюфели?', 'Where exactly are our missing truffles hidden?', [], ''),
    ('rodion', 'Вы получите трюфели сразу после обеда.', 'You will receive the truffles right after lunch.', [(200, 'Вы получаете')], ''),
    ('kostya', 'Шеф сильно разозлится, если узнает правду.', 'The Chef will get very angry if he finds out the truth.', [(196, 'не молчи')], ''),
    ('rodion', 'Тогда пожелайте мне приятного аппетита, Константин.', 'Then wish me bon appétit, Konstantin.', [], ''),
]
WALK = [
    (0, None, ["'Wait, let's just pay you money.' Notice how the young man uses the word ", ('kostya', 'деньги'), ' to refer to the cash they are willing to hand over.']),
    (1, None, ["'Bargaining is completely inappropriate here, young man.' The older gentleman firmly starts with the word ", ('rodion', 'Торг'), ' to show that negotiating is absolutely out of the question.']),
    (2, None, ["'But this is a very expensive restaurant!' He emphasizes the high prices using ", ('kostya', 'дорогой'), ' to mean expensive.']),
    (3, None, ["'I know this fine restaurant perfectly well.' This sophisticated character chooses the word ", ('rodion', 'прекрасно'), ' to describe how perfectly well he knows the place.']),
    (4, None, ["'The administrator will throw you out into the street immediately.' Listen closely for the strong expression ", ('kostya', 'выгонит'), ' meaning someone will be thrown out or chased away.']),
    (5, None, ["'In a decent suit nobody will recognize me.' Pay attention to the absolute denial in ", ('rodion', 'никто'), ' meaning not a single person.']),
    (6, None, ["'And what if you accidentally ruin someone else's clothes?' Catch the specific word for someone else's things, ", ('kostya', 'чужую'), ', which he uses to talk about the clothes.']),
    (7, None, ["'I promise to behave extremely neatly.' He adds extra weight to his promise with ", ('rodion', 'крайне'), ' to say he will be extremely careful.']),
    (8, None, ["'Where exactly are our missing truffles hidden?' The panic in his voice is clear around ", ('kostya', 'пропавшие'), ' when asking about the missing items.']),
    (9, None, ["'You will receive the truffles right after lunch.' Make sure you hear the term for lunch, ", ('rodion', 'обеда'), ', which is his ultimate goal in this negotiation.']),
    (10, None, ["'The Chef will get very angry if he finds out the truth.' He brings up the terrifying reality of the truth, ", ('kostya', 'правду'), ', being discovered by the boss.']),
    (11, None, ["'Then wish me bon appétit, Konstantin.' The concluding thought begins with the word ", ('rodion', 'Тогда'), ' meaning in that case.']),
]
