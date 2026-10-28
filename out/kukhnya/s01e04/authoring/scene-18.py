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
    (0, None, '\'I have a very simple question for you.\' "U menya k vam vopros" is "at me to you a question". "Prostoy" is "simple", the adjective behind "prosto".'),
    (1, None, '\'From one head chef to another?\' "Kak u shef-povara k shef-povaru" is "as at a head chef to a head chef", with -a for "at" and -u for "to".'),
    (2, None, '\'Which of my cooks came to see you?\' "Kto iz moikh povarov" is "who of my cooks". "Prikhodil", came, describes a trip there and back, which makes it a visit.'),
    (3, None, '\'I do not rat out my people, Viktor.\' "Sdavat\'" is to hand over, to the police or to an examiner. "Svoikh lyudey" is "my own people".'),
    (4, None, '\'He is my cook, not yours!\' "A ne vash" is "and not yours". The little "a" sets one claim against the other.'),
    (5, None, '\'He wants to work in a good kitchen.\' Russians work "na kukhne", on the kitchen. "Khoroshey" takes -ey to match.'),
    (6, None, '\'I have the best kitchen in this city!\' "Luchshaya", best, is feminine for "kukhnya". "V etom gorode" is "in this city".'),
    (7, None, '\'Then why are your people looking for work?\' "Ishchut" is "they look for", from "iskat\'". "Vashi lyudi" is "your people".'),
    (8, None, '\'I will definitely find out his name myself!\' "Obyazatel\'no" is "definitely". "Yego", his, never changes, and "uznayu" is "I\'ll find out".'),
    (9, None, '\'It is time for me to go to the kitchen.\' "Mne pora" is "to me it\'s time". "Na kukhnyu" takes -u for heading there.'),
    (10, None, '\'Will you find the way out yourself?\' "Vykhod", exit, is "vy-", out, plus "khod", a going. "Sami", yourself, is the polite plural of "sam".'),
    (11, None, '\'I will, I remember the way very well.\' Russian answers by repeating the verb, "naydu", I\'ll find. "Dorogu" is "doroga", road, as the object.'),
    (12, None, '\'Wonderful then, all the best to you!\' "Vsego dobrogo" is "of all good", a wish in the "of" form. It is a polite goodbye.'),
]
