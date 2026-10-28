# Authoring module for kukhnya-s01e18-scene-20.
ID = 'kukhnya-s01e18-scene-20'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 18
SCENE = 20
TITLE = 'Прощание  (Farewell)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'fedya': 'Федя', 'nagiyev': 'Нагиев', 'senya': 'Сеня'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.18'
SOURCE_FILE = 'sources/kukhnya/s01/e18.ru.dual.srt'
INTRO = 'Nagiyev has called in the kitchen staff to tell them they are being let go. Senya and Fedya talk it over, and then the payout arrives, and it is not what they hoped. Listen for the amount in the envelope.'
OPENER = 'Now the bad news, piece by piece.'
TRANSITION = 'And the whole farewell once more.'
OUTRO = 'The payout is smaller than anyone expected, and the rest is promised for later. Keep "raschyot", final pay, from "schitat", to count. See you next time!'
CLOSING = ('nagiyev', 'Удачи!')
STORY = [
    ('nagiyev', 'Ребята, нам придётся расстаться с вами.', 'Guys, we will have to part ways with you.', [(358, 'нам придётся расстаться с вами')], ''),
    ('senya', 'Куда вы собрались так рано?', 'Where are you off to so early?', [], ''),
    ('fedya', 'Нас уволили.', 'We got fired.', [(366, 'Нас уволили')], ''),
    ('senya', 'Как уволили? И меня тоже?', 'What do you mean, fired? Me too?', [(367, 'Тебя, кстати, тоже')], ''),
    ('fedya', 'Да, мы все уходим.', 'Yes, we are all leaving.', [], ''),
    ('senya', 'А что сказал шеф?', 'And what did the chef say?', [(369, 'а шеф')], ''),
    ('fedya', 'Шеф ничего не сделал.', 'The chef did nothing.', [], ''),
    ('fedya', 'Теперь мы без работы.', 'Now we are out of work.', [(371, 'шагаем именно в пропасть')], ''),
    ('senya', 'Что нам теперь делать?', 'What do we do now?', [(372, 'самоуверенности')], ''),
    ('fedya', 'Не знаю, пойдём домой.', 'I do not know, let us go home.', [], ''),
    ('nagiyev', 'Вот ваш расчёт.', 'Here is your payout.', [(374, 'Вот расчет')], ''),
    ('senya', 'Только двадцать тысяч?', 'Only twenty thousand?', [(375, '20 тысяч')], ''),
    ('nagiyev', 'Остальное будет в конце месяца.', 'The rest will be at the end of the month.', [(376, 'Остальное в конце месяца')], ''),
]
WALK = [
    (0, None, '\'Guys, we\'ll have to part with you.\' "Nam pridyotsya", \'to us it will come\': we\'ll have to. "Rasstatsya s vami", to part with you.'),
    (1, None, '\'Where are you all off to so early?\' "Kuda" is where to; where at would be "gde". "Sobralis", set off, is literally \'gathered yourselves\'.'),
    (2, None, '\'We got fired.\' "Uvolili", they fired, names nobody: someone fired "nas", us.'),
    (3, None, '\'What do you mean, fired? Me too?\' "Kak uvolili?", \'how fired?\', is how Russians question bad news.'),
    (4, None, '\'Yes, we\'re all leaving.\' "Vse", everyone, is different from "vsyo", everything. "Ukhodim", we\'re leaving: "u-" again means away.'),
    (5, None, '\'And what did the chef say?\' "A" opens a new question: and what about. "Shef" came from French.'),
    (6, None, '\'The chef did nothing.\' "Nichego ne sdelal", \'nothing not did\': the double \'not\' is normal Russian.'),
    (7, None, '\'Now we\'re out of work.\' "Bez", without, turns "rabota" into "raboty".'),
    (8, None, '\'What do we do now?\' "Chto nam delat?", \'what to us to do?\': the "nam" carries the \'we\'.'),
    (9, None, '\'I don\'t know, let\'s go home.\' "Poydyom", let\'s go. "Domoy" is homeward; at home is "doma".'),
    (10, None, '\'Here\'s your pay-off.\' "Raschyot", the final pay, comes from "schitat", to count: everything is settled up.'),
    (11, None, '\'Only twenty thousand?\' "Dvadtsat" is "dva", two, plus a worn-down \'ten\': two tens.'),
    (12, None, '\'The rest will come at the end of the month.\' "Ostalnoe", the rest, from "ostatsya", to remain. "V kontse mesyatsa", at the end of the month.'),
]
