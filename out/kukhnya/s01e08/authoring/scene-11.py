# Authoring module for kukhnya-s01e08-scene-11.
ID = 'kukhnya-s01e08-scene-11'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 8
SCENE = 11
TITLE = 'Комплимент от шефа  (A Compliment from the Chef)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'elena': 'Елена', 'fedya': 'Федя'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.08'
SOURCE_FILE = 'sources/kukhnya/s01/e08.ru.dual.srt'
INTRO = "Elena is running Barinov's kitchen at Claude Monet for the day. She stops beside Fedya, one of the cooks, and praises the way he fries fish. Fedya is not used to compliments. It's in Russian first."
OPENER = 'Slowly now. Each compliment from Elena gets a suspicious answer from Fedya, until he gives in.'
TRANSITION = 'Now the whole conversation again, in one go.'
OUTRO = "Fedya's line, 'nobody ever told me such words', is a warm way to accept a rare compliment. And 'at first sight' works just as well for culinary talent as it does for love. See you next time."
CLOSING = ('fedya', 'Пока!')
STORY = [
    ('elena', 'Федя, скажите, вы случайно учились во Франции?', 'Fedya, tell me, did you by chance study in France?', [(125, 'Федя, вы учились во Франции')], ''),
    ('fedya', 'Делать мне больше нечего, чем учиться там!', 'Like I had nothing better to do than study there!', [(126, 'Дел с меня больше нечего')], ''),
    ('elena', 'У вас просто потрясающая техника обжарки рыбы.', 'You have simply amazing technique for frying fish.', [(127, 'просто такую обжарку делают только в Лионе')], ''),
    ('fedya', 'Я просто жарю рыбу на горячей сковороде.', 'I simply fry fish on a hot pan.', [], ''),
    ('elena', 'Такую обжарку делают только в Лионе у Бокюза.', "They only do such searing in Lyon at Bocuse's.", [(127, 'только в Лионе у мэтра Бакёза')], ''),
    ('fedya', 'Вы серьёзно сравниваете меня с французским мастером?', 'Are you seriously comparing me to a French master?', [], ''),
    ('elena', 'Абсолютно серьёзно, у вас редкий природный дар.', 'Absolutely seriously, you have a rare natural gift.', [(128, 'у вас природный дар')], ''),
    ('fedya', 'Мне никогда раньше не говорили таких слов.', 'Nobody ever told me such words before.', [], ''),
    ('elena', 'Настоящий талант всегда виден с первого взгляда.', 'True talent is always visible at first sight.', [], ''),
    ('fedya', 'Спасибо большое за такую высокую оценку, шеф.', 'Thank you very much for such high praise, Chef.', [], ''),
    ('elena', 'Продолжайте готовить, гости будут в полном восторге.', 'Continue cooking, the guests will be in complete delight.', [], ''),
    ('fedya', 'Обещаю сделать самое вкусное блюдо сегодня!', 'I promise to make the most delicious dish today!', [], ''),
]
WALK = [
    (0, None, ["'Fedya, tell me, did you by chance study in France?' To soften her question, Elena adds ", ('elena', 'случайно'), ', which means by chance.']),
    (1, None, ["'Like I had nothing better to do than study there!' Fedya replies with the sarcastic phrase ", ('fedya', 'нечего'), ', meaning there is nothing to do.']),
    (2, None, ["'You have simply amazing technique for frying fish.' The word for frying or searing is ", ('elena', 'обжарки'), ', coming from the action of cooking on all sides.']),
    (3, None, ["'I simply fry fish on a hot pan.' When cooking in a hot pan, he says ", ('fedya', 'жарю'), ', which means I fry.']),
    (4, None, ["'They only do such searing in Lyon at Bocuse's.' To say at the place of someone, she says ", ('elena', 'у'), ', similar to saying at the house of.']),
    (5, None, ["'Are you seriously comparing me to a French master?' Asking if she means it, he uses ", ('fedya', 'серьёзно'), ', meaning seriously or in earnest.']),
    (6, None, ["'Absolutely seriously, you have a rare natural gift.' Praising his rare and natural talent, she uses ", ('elena', 'дар'), ', which translates to a gift.']),
    (7, None, ["'Nobody ever told me such words before.' Because nobody ever told him this before, he says ", ('fedya', 'никогда'), ', meaning never.']),
    (8, None, ["'True talent is always visible at first sight.' She notes that true talent is always ", ('elena', 'виден'), ', which means visible or apparent.']),
    (9, None, ["'Thank you very much for such high praise, Chef.' Expressing gratitude for the high praise, he mentions ", ('fedya', 'оценку'), ', which usually refers to a grade or mark.']),
    (10, None, ["'Continue cooking, the guests will be in complete delight.' Telling him to carry on cooking, she says ", ('elena', 'Продолжайте'), ', the polite way to say continue.']),
    (11, None, ["'I promise to make the most delicious dish today!' He makes a bold promise using ", ('fedya', 'Обещаю'), ', which translates directly to I promise.']),
]
