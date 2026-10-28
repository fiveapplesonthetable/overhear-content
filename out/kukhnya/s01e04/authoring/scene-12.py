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
INTRO = 'Senya is next in the chair, and he breaks down before the machine is even switched on. Instead of answering about the rival restaurant, he starts confessing to every bit of food he has ever taken from the kitchen. Here is the Russian first.'
OPENER = 'Now the confession.'
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'Barinov stares at his sobbing cook and decides what to do next. You\'ve heard "klyanus\'", "I swear", which is a good one to know.'
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
    (0, None, '\'Chef, please, do not turn on the device!\' "Ne vklyuchayte" is "don\'t switch on", with the polite -te. "Pribor" is a device or gauge.'),
    (1, None, '\'Why are you shaking so hard?\' "Ty chego" is a spoken "why are you". "Drozhish\'" is "you tremble", and "sil\'no" is "strongly".'),
    (2, None, '\'I will tell you everything honestly myself!\' "Sam" is "myself", here "of my own accord". "Rasskazhu" is "I\'ll tell", and "chestno" is "honestly".'),
    (3, None, '\'I took that fish after the banquet!\' "Vzyal ya" is "took I", with "ya" last for emphasis. "Posle banketa" is "after the banquet".'),
    (4, None, '\'And I took that venison away too!\' "Olenina", venison, is from "olen\'", deer. "Unyos" is "carried off", with "u-" for away.'),
    (5, None, '\'And half a kilo of expensive caviar?\' "Polkilo" is "pol-", half, plus "kilo". After it, "dorogaya ikra" becomes "dorogoy ikry".'),
    (6, None, '\'No, Chef, I did not take the caviar!\' Senya puts "ikru" first for stress: the caviar, I did not take. "Ne bral" is "didn\'t take".'),
    (7, None, '\'Forgive me, please, Chef!\' "Prostite menya" is "forgive me" with the polite -te.'),
    (8, None, '\'I do not care about your venison!\' "Mne plevat\'" is "to me to spit", a blunt "I couldn\'t care less". "Na tvoyu oleninu" is what he spits on.'),
    (9, None, '\'Did you go to the neighboring restaurant?\' The same question Fedya got: "khodil", went and came back.'),
    (10, None, '\'No, Chef, I swear to you!\' "Klyanus\'" is "I swear", with -s\'. "Vam" is "to you", polite.'),
    (11, None, '\'Tell the truth, yes or no?\' "Govori pravdu" is "speak the truth", with "pravda" becoming "pravdu" as the object.'),
    (12, None, '\'No! I am loyal only to you!\' "Predan" is the man\'s short "devoted". "Tol\'ko vam" is "only to you".'),
]
