# Authoring module for kukhnya-s01e05-scene-05.
ID = 'kukhnya-s01e05-scene-05'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 5
SCENE = 5
TITLE = 'Кулинарный спор  (A Culinary Bet)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'fedya': 'Федя', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.05'
SOURCE_FILE = 'sources/kukhnya/s01/e05.ru.dual.srt'
INTRO = "Max arrives late to the kitchen and gets scolded by Chef Viktor Barinov. To make matters worse, veteran fish cook Fedya insults Max's cooking skills, sparking an intense rivalry and a cooking bet. Listen to their fiery dialogue in Russian first, and then we will examine every line."
OPENER = "Let's examine this heated kitchen rivalry step by step."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'That concludes our fifth scene. In Kukhnya, pride and culinary rivalry can turn an ordinary morning into a fierce culinary competition. See you next time!'
CLOSING = ('max', 'До встречи!')
STORY = [
    ('max', 'Доброе утро, шеф!', 'Good morning, Chef!', [(69, 'Доброе утро, шеф')], ''),
    ('barinov', 'Огузок, ты постоянно опаздываешь на работу.', 'Runt, you are constantly late for work.', [(69, 'Агузик'), (70, 'Ты постоянно'), (71, 'ты опять опоздал')], ''),
    ('max', 'Шеф, мне не выдали форму вовремя.', 'Chef, they did not issue my uniform on time.', [(72, 'мне'), (72, 'форму не выдало')], ''),
    ('barinov', 'Хватит оправданий, быстро иди работать!', 'Enough excuses, quickly go to work!', [(68, 'За работу')], ''),
    ('fedya', 'Ты так же плохо шутишь, как и готовишь.', 'You joke as badly as you cook.', [(78, 'Ты так же'), (78, 'шутишь, как и готовишь')], ''),
    ('max', 'Я не понял твоей шутки, Федя.', "I didn't understand your joke, Fedya.", [(79, 'Не понял')], ''),
    ('fedya', 'Это обычное состояние для твоего мозга.', 'This is a normal state for your brain.', [(79, 'привычное состояние для твоего мозга')], ''),
    ('max', 'Ты хочешь сказать, что я плохо готовлю?', 'Do you want to say that I cook badly?', [(80, 'он сказал, что я'), (82, 'ты хочешь сказать')], ''),
    ('fedya', 'Да, именно это я и говорю.', 'Yes, that is exactly what I say.', [], ''),
    ('max', 'А ты думаешь, ты готовишь лучше меня?', 'And do you think you cook better than me?', [(82, 'ты лучше готовишь')], ''),
    ('fedya', 'Уж точно намного лучше тебя!', 'Certainly much better than you!', [(83, 'уж не хуже')], ''),
    ('max', 'Тогда давай устроим кулинарный спор!', "Then let's make a culinary bet!", [(84, 'Спорим')], ''),
    ('fedya', 'Спорим, огузок! Я легко тебя выиграю!', 'Wanna bet, runt! I will easily beat you!', [(84, 'Спорим')], ''),
    ('max', 'Посмотрим, кто из нас лучший повар!', 'We will see which of us is the best cook!', [], ''),
]
WALK = [
    (0, None, "'Good morning, Chef!' Max greets the boss nervously as he arrives late."),
    (1, None, "'Runt, you are constantly late for work.' Barinov loudly calls out the rookie for his poor punctuality."),
    (2, None, "'Chef, they did not issue my uniform on time.' Max tries to blame the delay on a wardrobe issue."),
    (3, None, "'Enough excuses, quickly go to work!' Barinov cuts off the excuses and orders him to his station."),
    (4, None, "'You joke as badly as you cook.' Fedya throws a sharp insult at the new guy's abilities."),
    (5, None, "'I didn't understand your joke, Fedya.' Max defensively pretends not to get the dig."),
    (6, None, "'This is a normal state for your brain.' Fedya mocks his intelligence with another zinger."),
    (7, None, "'Do you want to say that I cook badly?' Max challenges the veteran's assessment of his skills."),
    (8, None, "'Yes, that is exactly what I say.' Fedya bluntly confirms his low opinion."),
    (9, None, "'And do you think you cook better than me?' Max questions whether the veteran is actually any better."),
    (10, None, "'Certainly much better than you!' Fedya confidently asserts his culinary superiority."),
    (11, None, "'Then let's make a culinary bet!' Max proposes a formal challenge to settle the matter."),
    (12, None, "'Wanna bet, runt! I will easily beat you!' Fedya eagerly accepts the challenge, predicting an easy win."),
    (13, None, "'We will see which of us is the best cook!' Max vows to prove his worth on the line."),
]
