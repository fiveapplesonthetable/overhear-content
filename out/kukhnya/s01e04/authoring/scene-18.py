# Authoring module for kukhnya-s01e04-scene-18.
ID = 'kukhnya-s01e04-scene-18'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 4
SCENE = 18
TITLE = 'Шеф против шефа  (Chef Against Chef)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'elena': 'Елена'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.04'
SOURCE_FILE = 'sources/kukhnya/s01/e04.ru.dual.srt'
INTRO = "Chef Barinov marches into the rival restaurant to find Elena Sokolova, determined to find out which of his cooks came to her for a job. Elena has no intention of telling him. Here's the Russian first."
OPENER = "Let's go through the standoff."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'Barinov leaves without a name, but he\'s determined to find the traitor himself. Take away "vsego vam dobrogo", the Russian way to say "all the best".'
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('barinov', 'У меня к вам совсем простой вопрос.', 'I have a very simple question for you.', [(251, 'простой вопрос')], ''),
    ('elena', 'Как у шеф-повара к шеф-повару?', 'From one head chef to another?', [(252, 'Как у шеф-повара к шеф-повару')], ''),
    ('barinov', 'Кто из моих поваров приходил к вам?', 'Which of my cooks came to see you?', [(253, 'Кто из моих людей')], ''),
    ('elena', 'Я не сдаю своих людей, Виктор.', 'I do not rat out my people, Viktor.', [(257, 'Не сдаю своих людей')], ''),
    ('barinov', 'Это мой повар, а не ваш!', 'He is my cook, not yours!', [(258, 'Это мой человек')], ''),
    ('elena', 'Он хочет работать на хорошей кухне.', 'He wants to work in a good kitchen.', [], ''),
    ('barinov', 'У меня лучшая кухня в этом городе!', 'I have the best kitchen in this city!', [], ''),
    ('elena', 'Тогда почему ваши люди ищут работу?', 'Then why are your people looking for work?', [], ''),
    ('barinov', 'Я обязательно узнаю его имя сам!', 'I will definitely find out his name myself!', [], ''),
    ('elena', 'Мне уже пора идти на кухню.', 'It is time for me to go to the kitchen.', [(261, 'Надо идти работать')], ''),
    ('elena', 'Вы сами выход отсюда найдёте?', 'Will you find the way out yourself?', [(262, 'Выход найдете')], ''),
    ('barinov', 'Найду, дорогу я отлично помню.', 'I will, I remember the way very well.', [(263, 'Найду')], ''),
    ('elena', 'Вот и отлично, всего вам доброго!', 'Wonderful then, all the best to you!', [(263, 'Ну и хорошо')], ''),
]
WALK = [
    (0, None, '\'I have a very simple question for you.\' Russian says "at me to you a question". "Prostoy" is "simple", from the same family as "prosto".'),
    (1, None, '\'From one head chef to another?\' "Kak u X k Y" is "like from X to Y", and both chefs take the matching "of" and "to" endings.'),
    (2, None, '\'Which of my cooks came to see you?\' The chef asks "which of my cooks", and "came to you" uses the repeated kind of coming, a visit. "K vam" is "to you".'),
    (3, None, '\'I do not rat out my people, Viktor.\' "Sdavat\'" is to hand over, and also to hand in an exam. "Svoikh lyudey" is "my own people", using the "own" word.'),
    (4, None, '\'He is my cook, not yours!\' "A ne vash" is "and not yours". The little "a ne" sets one claim against the other.'),
    (5, None, '\'He wants to work in a good kitchen.\' "Na khoroshey kukhne" is "in a good kitchen": the "on" word, then an "-ey" ending.'),
    (6, None, '\'I have the best kitchen in this city!\' "Luchshaya" is "the best", feminine, as "kukhnya" is. "V etom gorode" is "in this city", ending in -e.'),
    (7, None, '\'Then why are your people looking for work?\' "Ishchut" is "they look for", a relative of "ishchi". "Vashi" is "your", plural.'),
    (8, None, '\'I will definitely find out his name myself!\' "Yego imya" is "his name", and "yego" never changes. "Uznayu" is "I will find out".'),
    (9, None, '\'It is time for me to go to the kitchen.\' "Mne pora", "to me it\'s time", is the "pora" of "it\'s time to".'),
    (10, None, '\'Will you find the way out yourself?\' "Vykhod" is "vy-" plus "khod", going out. "Sami" is "yourselves", the plural of "sam".'),
    (11, None, '\'I will, I remember the way very well.\' Russians answer a question by repeating the verb: "naydu", "I\'ll find". "Dorogu" is "the road".'),
    (12, None, '\'Wonderful then, all the best to you!\' "Vsego dobrogo" is literally "of all good", a wish like "spokoynoy nochi". It\'s a polite goodbye, with a sting here.'),
]
