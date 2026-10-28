# Authoring module for kukhnya-s01e01-scene-23.
ID = 'kukhnya-s01e01-scene-23'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 1
SCENE = 23
TITLE = 'Объективная оценка  (An Objective Opinion)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kostya': 'Костя', 'max': 'Макс', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.01'
SOURCE_FILE = 'sources/kukhnya/s01/e01.ru.dual.srt'
INTRO = 'In the bustling kitchen of Claude Monet, new recruit Max proudly plates an intricate dish. Barman Kostya warns him that the temperamental head chef Viktor Barinov will never appreciate his efforts, prompting Max to seek an objective taster before dining room manager Vika suddenly sweeps in.'
OPENER = "Let's see how Max prepares his special dish in the restaurant kitchen."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Vika takes the plate to the dining room while Max and Kostya exchange nervous glances. Next time you watch the episode, listen for the Russian expressions for 'dish' and 'more' — you will catch every word right away. See you next time!"
CLOSING = ('vika', 'Пока!')
STORY = [
    ('kostya', 'Здорово у тебя всё получается, Макс!', 'You are doing great at everything, Max!', [(307, 'Здорово у тебя получается')], ''),
    ('kostya', 'Жалко только, что шеф этого не оценит.', "Too bad only that the chef won't appreciate this.", [(308, 'Жалко только, что он этого не оценит')], ''),
    ('max', 'Но это мы с тобой ещё посмотрим.', 'We will see about that yet.', [(309, 'Но это мы еще посмотрим')], ''),
    ('kostya', 'Да он даже пробовать не станет!', "Why, he won't even taste it!", [(309, 'Да он даже не попробует')], ''),
    ('kostya', 'А если попробует, ему не понравится.', "And if he tastes it, he won't like it.", [(310, 'А если попробует, ему все равно не понравится')], ''),
    ('kostya', 'Я очень хорошо знаю нашего шефа.', 'I know our chef very well.', [(311, 'Я его знаю')], ''),
    ('max', 'Погоди, нам нужна более объективная оценка.', 'Wait, we need a more objective opinion.', [(312, 'Погоди'), (313, 'Тогда нам нужна более объективная оценка')], ''),
    ('max', 'Пусть кто-нибудь другой сначала попробует.', 'Let someone else taste it first.', [(314, 'И')], ''),
    ('vika', 'Сколько можно ждать горячее блюдо?', 'How long must one wait for the hot dish?', [], ''),
    ('vika', 'Всё приходится делать самой на этой кухне.', 'One has to do everything herself in this kitchen.', [(310, 'все')], ''),
    ('max', 'Я сейчас сам отнесу в зал.', 'I will carry it to the hall myself right now.', [], ''),
    ('vika', 'Отойди в сторону и иди работай!', 'Step aside and go back to work!', [], ''),
    ('max', 'Это блюдо сделано по всем правилам.', 'This dish is made according to all rules.', [], ''),
    ('vika', 'Клиенты давно ждут свой вкусный ужин.', 'The clients have been waiting for their delicious dinner for a long time.', [], ''),
]
WALK = [
    (0, None, "'You are doing great at everything, Max!' Kostya praises the young cook's impressive culinary effort."),
    (1, None, "'Too bad only that the chef won't appreciate this.' He warns that their boss will inevitably reject it out of spite."),
    (2, None, "'We will see about that yet.' Max refuses to accept defeat before the tasting even happens."),
    (3, None, "'Why, he won't even taste it!' Kostya predicts the stubborn boss will not even take a bite."),
    (4, None, "'And if he tastes it, he won't like it.' He adds that even if the chef tries it, he will lie about the flavor."),
    (5, None, "'I know our chef very well.' Kostya emphasizes his long history dealing with the erratic boss."),
    (6, None, "'Wait, we need a more objective opinion.' Max realizes he must find a neutral party to judge his food."),
    (7, None, "'Let someone else taste it first.' He plots to bypass the boss for a fair evaluation."),
    (8, None, "'How long must one wait for the hot dish?' Vika storms in demanding the overdue main course."),
    (9, None, "'One has to do everything herself in this kitchen.' She bitterly complains about having to manage the cooks constantly."),
    (10, None, "'I will carry it to the hall myself right now.' Max seizes the opportunity to serve his own creation."),
    (11, None, "'Step aside and go back to work!' Vika harshly shoves the rookie out of her way."),
    (12, None, "'This dish is made according to all rules.' Max tries to defend his plate as a perfectly executed recipe."),
    (13, None, "'The clients have been waiting for their delicious dinner for a long time.' Vika snatches the food, entirely focused on her impatient VIP guests."),
]
