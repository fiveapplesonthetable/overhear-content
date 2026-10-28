# Authoring module for domashniy-arest-s01e09-scene-33.
ID = 'domashniy-arest-s01e09-scene-33'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 9
SCENE = 33
TITLE = 'Рейтинг растёт  (The Rating Is Rising)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'pasha': 'Паша', 'slavik': 'Славик'}
SOURCE_NAME = 'Домашний арест, Сезон 1, Эпизод 9'
SOURCE_FILE = 'sources/domashniy-arest/s01/e09.ru.dual.srt'
INTRO = 'At campaign headquarters, mayoral candidate Pavel Osipenko sits in total despair, believing that his election campaign is already doomed. Campaign aide Slava enters the office with surprising new polling figures that completely reverse the situation.'
OPENER = "Let's examine how sudden political fortunes shift Osipenko from gloom to triumph."
TRANSITION = "Now let's listen to Slava delivering the victorious polling results once more."
OUTRO = "Osipenko's despair vanishes in an instant as he realizes he has a fighting chance to win. See you next time!"
CLOSING = ('pasha', 'Пока!')
STORY = [
    ('slavik', 'Можно войти, Павел?', 'May I come in, Pavel?', [(904, 'Можно?')], 'adapted cue'),
    ('pasha', 'Какая у нас сейчас ситуация?', 'What is our situation right now?', [(906, 'Тут такая ситуация, Павел.'), (907, 'Какая ситуация?')], 'adapted cues'),
    ('pasha', 'Мы сейчас в полной яме.', 'We are in a complete pit right now.', [], 'clean adaptation of cue 908'),
    ('slavik', 'Я бы так не сказал.', 'I would not say that.', [(910, 'Я бы так не сказал.')], 'exact cue'),
    ('slavik', 'Ваш рейтинг снова резко растёт вверх!', 'Your rating is sharply rising again!', [(911, 'Ваш рейтинг снова резко растет вверх.')], 'adapted cue'),
    ('pasha', 'Это твои глупые шутки?', 'Are these your silly jokes?', [], 'adapted cue 912'),
    ('slavik', 'Нет, это не шутки.', 'No, these are not jokes.', [(913, 'Нет, это не шутки.')], 'exact cue'),
    ('slavik', 'Люди отвернулись от Самсонова.', 'People turned away from Samsonov.', [(914, 'от Самсонова')], 'adapted cue'),
    ('slavik', 'Они думают, что он продался.', 'They think that he sold out.', [(917, 'Люди думают, что народный кандидат продался.')], 'adapted cue'),
    ('slavik', 'Отношение народа к губернатору очень плохое.', "The people's attitude toward the governor is very bad.", [(918, 'Отношение народа к губернатору')], 'adapted cue'),
    ('slavik', 'Встреча подорвала доверие к Самсонову.', 'The meeting undermined trust in Samsonov.', [(920, 'Встреча подорвала доверие к Самсонову.')], 'exact cue'),
    ('slavik', 'По последним данным, ваш рейтинг выше.', 'According to latest data, your rating is higher.', [(927, 'По последним данным, ваш рейтинг')], 'adapted cue'),
    ('slavik', 'Рейтинги поднялись на семь процентов!', 'Ratings have risen by seven percent!', [(930, 'Рейтинги поднялись')], 'adapted cue'),
    ('pasha', 'Да! Это отличная новость!', 'Yes! This is excellent news!', [(931, 'Да.')], 'expanded cue'),
]
WALK = [
    (0, None, "'May I come in, Pavel?' Knocking cautiously on the office door, Slavik asks if he can step inside."),
    (1, None, "'What is our situation right now?' Osipenko asks for a realistic summary of the campaign status."),
    (2, None, "'We are in a complete pit right now.' A descriptive idiom conveying total political ruin."),
    (3, None, "'I would not say that.' With a quiet smile, Slavik politely pushes back against Pasha's doom and gloom."),
    (4, None, "'Your rating is sharply rising again!' He breaks the shock news that Pasha's poll numbers are shooting back up."),
    (5, None, "'Are these your silly jokes?' Osipenko cannot believe good news and suspects mockery."),
    (6, None, "'No, these are not jokes.' A firm statement confirming the factual truth of the poll results."),
    (7, None, "'People turned away from Samsonov.' Literally 'turned away from,' the phrase shows voters abandoning Samsonov in droves."),
    (8, None, "'They think that he sold out.' Appearing on television alongside the hated governor made voters think Samsonov sold out."),
    (9, None, "'The people's attitude toward the governor is very bad.' A clear assessment of general public sentiment."),
    (10, None, "'The meeting undermined trust in Samsonov.' That one friendly meeting with Viktor Stepanovich torpedoed Samsonov's honest image."),
    (11, None, "'According to latest data, your rating is higher.' According to the freshest numbers, Pasha has pulled ahead in the race."),
    (12, None, "'Ratings have risen by seven percent!' A specific numerical increase marking significant momentum."),
    (13, None, "'Yes! This is excellent news!' An enthusiastic exclamation celebrating an unexpected breakthrough."),
]
