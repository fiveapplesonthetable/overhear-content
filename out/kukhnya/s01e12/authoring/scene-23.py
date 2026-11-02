# Authoring module for kukhnya-s01e12-scene-23.
ID = 'kukhnya-s01e12-scene-23'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 12
SCENE = 23
TITLE = 'Перемены к лучшему  (Changes for the Better)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kostya': 'Костя', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.12'
SOURCE_FILE = 'sources/kukhnya/s01/e12.ru.dual.srt'
INTRO = 'The evening is over, the restaurant is full of happy guests, and Max and Kostya stand at the bar, thinking about the changes of the day. Russian first, as always.'
OPENER = 'Slowly, at the pace of two tired friends.'
TRANSITION = 'And one last time, the whole chat.'
OUTRO = "That is the end of the episode, and Max has found his moral: every change is for the better. See you next time."
CLOSING = ('max', 'Пока!')
STORY = [
    ('kostya', 'Макс, зал ресторана снова полон людей.', 'Max, the dining hall is full of people again.', [], ''),
    ('max', 'Да, наш вечер закончился очень удачно.', 'Yes, our evening ended very successfully.', [], ''),
    ('max', 'И всё-таки перемены всегда неожиданно происходят.', 'Still, changes always happen unexpectedly.', [(286, 'И все-таки, как бы мы ни относились к переменам, они происходят.')], ''),
    ('kostya', 'Ты прав, жизнь постоянно меняется вокруг нас.', 'You are right, life constantly changes around us.', [], ''),
    ('max', 'Иногда мы получаем совсем не то.', 'Sometimes we get something completely different.', [(287, 'Иногда мы получаем совсем не то, что хотели.')], ''),
    ('max', 'Мы получаем не то, что хотели раньше.', 'We get not what we wanted before.', [(287, 'что хотели.')], ''),
    ('kostya', 'Но часто всё складывается даже лучше.', 'But often everything turns out even better.', [], ''),
    ('max', 'Порой мы убеждаемся, что были правы.', 'Sometimes we realize that we were right.', [(288, 'Порой убеждаемся в том, что были правы.')], ''),
    ('kostya', 'И наши старые друзья остаются рядом.', 'And our old friends remain by our side.', [], ''),
    ('max', 'А бывает, мы приходим в исходную точку.', 'And sometimes we arrive back at the starting point.', [(289, 'мы приходим в исходную точку.')], ''),
    ('kostya', 'Главное — не терять веру и надежду.', 'The main thing is not to lose faith and hope.', [], ''),
    ('max', 'Главное — верить во все перемены.', 'The main thing is to believe in all changes.', [(290, 'Главное верить')], ''),
    ('max', 'Все перемены в жизни ведут к лучшему!', 'All changes in life lead to the better!', [(290, 'все перемены в жизни к лучшему.')], ''),
]
WALK = [
    (0, None, ["'Max, the dining hall is full of people again.' Full of people is ", ('kostya', 'полон'), ('kostya', 'людей'), ', with the of form built into the ending. Again is ', ('kostya', 'снова'), '.']),
    (1, None, ["'Yes, our evening ended very successfully.' Ended is ", ('max', 'закончился'), ', meaning it ended itself. Successfully is ', ('max', 'удачно'), '.']),
    (2, None, ["'Still, changes always happen unexpectedly.' All the same is ", ('max', 'всё'), '-', ('max', 'таки'), ', and unexpectedly is ', ('max', 'неожиданно'), '. Happen is ', ('max', 'происходят'), '.']),
    (3, None, ["'You are right, life constantly changes around us.' Right is ", ('kostya', 'прав'), '. Changes is ', ('kostya', 'меняется'), ', meaning it changes by itself. Around us is ', ('kostya', 'вокруг'), ('kostya', 'нас'), '.']),
    (4, None, ["'Sometimes we get something completely different.' Something completely different is said as completely not that, ", ('max', 'совсем'), ('max', 'не'), ('max', 'то'), '. Sometimes is ', ('max', 'Иногда'), '.']),
    (5, None, ["'We get not what we wanted before.' Not what is ", ('max', 'не'), ('max', 'то'), ', ', ('max', 'что'), '. We wanted is ', ('max', 'хотели'), ', and earlier is ', ('max', 'раньше'), '.']),
    (6, None, ["'But often everything turns out even better.' Turns out literally says folds itself together, ", ('kostya', 'складывается'), '. Even better is ', ('kostya', 'даже'), ('kostya', 'лучше'), '.']),
    (7, None, ["'Sometimes we realize that we were right.' At times is ", ('max', 'Порой'), '. We become convinced is ', ('max', 'убеждаемся'), ', and we were right is ', ('max', 'были'), ('max', 'правы'), '.']),
    (8, None, ["'And our old friends remain by our side.' Friends is ", ('kostya', 'друзья'), '. Remain is ', ('kostya', 'остаются'), ', and nearby is ', ('kostya', 'рядом'), '.']),
    (9, None, ["'And sometimes we arrive back at the starting point.' It happens is ", ('max', 'бывает'), '. Starting point is ', ('max', 'исходную'), ('max', 'точку'), '.']),
    (10, None, ["'The main thing is not to lose faith and hope.' To lose is ", ('kostya', 'терять'), '. Faith and hope are ', ('kostya', 'веру'), ' and ', ('kostya', 'надежду'), ', taking an u at the end.']),
    (11, None, ["'The main thing is to believe in all changes.' In becomes ", ('max', 'во'), ' before all, so they do not jam together. To believe in is ', ('max', 'верить'), ('max', 'во'), '. The main thing is is ', ('max', 'Главное'), '.']),
    (12, None, ["'All changes in life lead to the better!' Towards the better is ", ('max', 'к'), ('max', 'лучшему'), '. Lead is ', ('max', 'ведут'), '.']),
]
