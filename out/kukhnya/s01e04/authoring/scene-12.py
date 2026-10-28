# Authoring module for kukhnya-s01e04-scene-12.
ID = 'kukhnya-s01e04-scene-12'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 4
SCENE = 12
TITLE = 'Чистосердечное признание  (A Full Confession)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'senya': 'Сеня'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.04'
SOURCE_FILE = 'sources/kukhnya/s01/e04.ru.dual.srt'
INTRO = "Terrified of the lie detector machine in Barinov's office, line cook Senya completely breaks down before the sensors are even attached. Instead of answering questions about rival restaurant Arcobaleno, Senya frantically confesses to every scrap of food he ever pilfered from the kitchen. Let's listen to his hilarious confession in Russian first."
OPENER = "Let's replay a few lines to examine key phrases and vocabulary."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Barinov stares in disbelief at his sobbing cook before deciding what to do next. Next time you watch the episode, listen for the Russian expressions for 'banquet' and 'more' — you will catch every word right away. See you next time!"
CLOSING = ('senya', 'Пока!')
STORY = [
    ('senya', 'Шеф, пожалуйста, не включайте прибор!', 'Chef, please, do not turn on the device!', [(146, 'Шеф, пожалуйста')], ''),
    ('barinov', 'Ты чего так сильно дрожишь?', 'Why are you shaking so hard?', [], ''),
    ('senya', 'Я сам вам всё честно расскажу!', 'I will tell you everything honestly myself!', [(146, 'Я все расскажу')], ''),
    ('senya', 'Эту рыбу после банкета взял я!', 'I took that fish after the banquet!', [(147, 'Эту рыбу'), (147, 'после банкета, я взял')], ''),
    ('senya', 'И ту оленину тоже унёс я!', 'And I took that venison away too!', [(148, 'И ту оленину'), (148, 'тоже я унес')], ''),
    ('barinov', 'А полкило дорогой икры?', 'And half a kilo of expensive caviar?', [(149, 'А полкило икры')], ''),
    ('senya', 'Нет, шеф, икру я не брал!', 'No, Chef, I did not take the caviar!', [(150, 'Нет')], ''),
    ('senya', 'Простите меня, пожалуйста, шеф!', 'Forgive me, please, Chef!', [(151, 'Простите меня, шеф')], ''),
    ('barinov', 'Мне плевать на твою оленину!', 'I do not care about your venison!', [], ''),
    ('barinov', 'Ты ходил в соседний ресторан?', 'Did you go to the neighboring restaurant?', [(152, 'Это ты ходил в соседний ресторан')], ''),
    ('senya', 'Нет, шеф, клянусь вам!', 'No, Chef, I swear to you!', [(153, 'Нет')], ''),
    ('barinov', 'Говори правду, да или нет?', 'Tell the truth, yes or no?', [(150, 'нет')], ''),
    ('senya', 'Нет! Я предан только вам!', 'No! I am loyal only to you!', [(154, 'Нет')], ''),
]
WALK = [
    (0, None, "'Chef, please do not turn on the device!' Senya begs, sweating profusely before the machine is even attached."),
    (1, None, "'I took this fish after the banquet!' Panicking before the machine is even turned on, Senya blurts out a confession about the banquet fish."),
    (2, None, "'And the half-kilo of expensive caviar?' Chef Barinov presses, seizing the chance to uncover other thefts."),
    (3, None, "'Did you go to the neighboring restaurant?' Barinov demands, ignoring the petty food thefts to find the real secret. Now listen to the full office confession once more."),
]
