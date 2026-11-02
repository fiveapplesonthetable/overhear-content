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
OUTRO = 'Barinov sends them all out, and he is still fuming when they go. The phrase to keep means "enough".'
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
    (0, None, ['\'You stole my favorite Japanese knife!\' The word for stole is built from ', ('barinov', 'украли'), ', which comes from a root meaning to steal, with an "away" part at the front. It ends with an action word ending that shows the chef is accusing several people.']),
    (1, None, ['\'And you completely ruined my dish!\' Literally, completely translates to ', ('barinov', 'совершенно'), ', which is related to a describing word meaning perfect. The word for spoiled is ', ('barinov', 'испортили'), '.']),
    (2, None, ['\'And all of you get out of here quickly!\' The action word meaning went out translates to ', ('barinov', 'вышли'), ', but the chef barks it as an order. Locals sometimes do that when they want something done right now. The word for from here is ', ('barinov', 'отсюда!'), '.']),
    (3, None, ['\'Chef, we were only trying to help!\' Literally, this translates to we wanted as better: ', ('senya', 'мы хотели как лучше!'), '. It is the stock excuse when good intentions go wrong.']),
    (4, None, ['\'I do not care what you were trying to do!\' Literally, this starts with to me to spit: ', ('barinov', 'Мне плевать,'), ', which is a rude way of saying I could not care less. Then the word for what you there wanted is added.']),
    (5, None, ['\'Do you know what the guest said about the fricassee?\' A rising voice turns the word for you know into a question: ', ('barinov', 'Знаете,'), '. The word for guest is ', ('barinov', 'гостья'), ', which refers specifically to a woman, and the little word for about is casual.']),
    (6, None, ['\'Was she completely delighted?\' Literally, in full delight translates to ', ('fedya', 'в полном восторге?'), ', which is a phrase worth keeping. The action word meaning was ends with a sound indicating a woman.']),
    (7, None, ['\'She said that it was disgusting!\' The word for disgusting is ', ('barinov', 'отвратительно!'), ', ending in a sound to match the dish. The word for that is the same word as what.']),
    (8, None, ['\'Chef, I told them right away!\' The action word for told translates to ', ('senya', 'говорил!'), ', which is the same one used in the local phrase for I told you so. Little words meaning to them like to sit right before the action word, and the word for at once is ', ('senya', 'сразу'), '.']),
    (9, None, ['\'It was Senya who made that terrible sauce!\' Literally, this translates to this Senya cooked: ', ('fedya', 'Это Сеня готовил'), ', which is a handy way to point at who did it. The word for terrible is built from a root meaning horror.']),
    (10, None, ['\'No, Fedya roasted that partridge himself!\' The word for himself translates to ', ('senya', 'сам'), ', which is the word for passing the blame. The action word for roasted is built from a root meaning heat, and the naming word for the bird changes its ending as the thing being roasted.']),
    (11, None, ['\'Stop arguing! You are all terrible cooks!\' The word for enough or it suffices translates to ', ('barinov', 'Хватит'), '. The naming word for cooks changes its ending for multiple people, similar to houses.']),
    (12, None, ['\'Get out of my kitchen right now!\' Literally, take yourselves away translates to ', ('barinov', 'Убирайтесь'), ', which is a rude way to say clear off. In the phrase for off my kitchen, the little word for from is the one that goes with on places.']),
]
