# Authoring module for kukhnya-s01e02-scene-12.
ID = 'kukhnya-s01e02-scene-12'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 2
SCENE = 12
TITLE = "Гнев шеф-повара  (The Head Chef's Wrath)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'fedya': 'Федя', 'senya': 'Сеня'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.02'
SOURCE_FILE = 'sources/kukhnya/s01/e02.ru.dual.srt'
INTRO = 'Elena has told Barinov the fricassee was fine, and the chef marches back to the kitchen anyway, furious that his knife is gone and his kitchen has been used without him. He lies about what the guest said, and Senya and Fedya start to blame each other. Here it is in Russian first.'
OPENER = "Let's hear the blame game again."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'Barinov sends them all out, and he is still fuming when they go. The phrase to keep is "khvatit", which means "enough".'
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('barinov', 'Вы украли мой любимый японский нож!', 'You stole my favorite Japanese knife!', [(169, 'нож мой сперли')], ''),
    ('barinov', 'И вы совершенно испортили моё блюдо!', 'And you completely ruined my dish!', [(169, 'блюдо мое испохабили')], ''),
    ('barinov', 'А вы все быстро вышли отсюда!', 'And all of you get out of here quickly!', [(170, 'А вы все вышли')], ''),
    ('senya', 'Шеф, мы хотели как лучше!', 'Chef, we were only trying to help!', [(171, 'Шеф'), (172, 'Мы как лучше хотели')], ''),
    ('barinov', 'Мне плевать, чего вы там хотели!', 'I do not care what you were trying to do!', [(173, 'Да мне плевать, что вы хотели')], ''),
    ('barinov', 'Знаете, что гостья сказала про фрикасе?', 'Do you know what the guest said about the fricassee?', [(174, 'Знаете, что она сказала про ваше фрикассе')], ''),
    ('fedya', 'Она была в полном восторге?', 'Was she completely delighted?', [], ''),
    ('barinov', 'Она сказала, что оно отвратительно!', 'She said that it was disgusting!', [(175, 'Что оно отвратительно')], ''),
    ('senya', 'Шеф, а я им сразу говорил!', 'Chef, I told them right away!', [(176, 'Шеф, а я им сразу сказал')], ''),
    ('fedya', 'Это Сеня готовил этот ужасный соус!', 'It was Senya who made that terrible sauce!', [], ''),
    ('senya', 'Нет, Федя сам жарил эту куропатку!', 'No, Fedya roasted that partridge himself!', [], ''),
    ('barinov', 'Хватит спорить! Вы все плохие повара!', 'Stop arguing! You are all terrible cooks!', [(178, 'Вы инвалиды')], ''),
    ('barinov', 'Убирайтесь с моей кухни прямо сейчас!', 'Get out of my kitchen right now!', [], ''),
]
WALK = [
    (0, None, '\'You stole my favorite Japanese knife!\' The "u-" at the front of "stole" is the "away" prefix. It ends in "-li" because the chef is speaking to several people.'),
    (1, None, '\'And you completely ruined my dish!\' "Ruined" is "spoiled", plus a prefix, and "completely" is "sovershenno".'),
    (2, None, '\'And all of you get out of here quickly!\' "Went out" is used as an order, which Russians do all the time. "Here" is in the "from here" form.'),
    (3, None, '\'Chef, we were only trying to help!\' Word for word it\'s "we wanted as better", the stock excuse for good intentions.'),
    (4, None, '\'I do not care what you were trying to do!\' Literally "to me to spit", a rude way to say "I couldn\'t care less". The last words are "what you there wanted".'),
    (5, None, '\'Do you know what the guest said about the fricassee?\' A rising voice turns "you know" into a question. The woman guest has her own feminine form, and "about" is a casual short word.'),
    (6, None, '\'Was she completely delighted?\' "In full delight" is a nice phrase to reuse, and "was" ends in -a for a woman.'),
    (7, None, '\'She said that it was disgusting!\' "Disgusting" is a long word. "It" refers to the fricassee, which is a neuter word. "That" is the same word as "what".'),
    (8, None, '\'Chef, I told them right away!\' "Im" is the "to them" form of "they", and "srazu" is "right away".'),
    (9, None, '\'It was Senya who made that terrible sauce!\' Russian starts with "this Senya cooked", a handy way to point at who did it. "Terrible" comes from "horror".'),
    (10, None, '\'No, Fedya roasted that partridge himself!\' "Himself" is the shifting-the-blame word, and "that partridge" ends in -u as the thing roasted.'),
    (11, None, '\'Stop arguing! You are all terrible cooks!\' "Enough" is literally "it suffices". "Cooks" has the odd plural in -a.'),
    (12, None, '\'Get out of my kitchen right now!\' The verb is "clear yourselves off", a rude "scram". "Off my kitchen" uses the little word meaning "from".'),
]
