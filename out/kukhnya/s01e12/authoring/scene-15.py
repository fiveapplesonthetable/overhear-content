# Authoring module for kukhnya-s01e12-scene-15.
ID = 'kukhnya-s01e12-scene-15'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 12
SCENE = 15
TITLE = 'Новое меню  (The New Menu)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.12'
SOURCE_FILE = 'sources/kukhnya/s01/e12.ru.dual.srt'
INTRO = 'Chef Barinov calls Vika into the kitchen to show her his brand-new menu. She takes a look at the soup and the fish and notices that something is off. Listen to it in Russian first.'
OPENER = 'Here it is again, piece by piece. Listen for the moment Vika sees through the trick.'
TRANSITION = 'Now the new menu, from the top.'
OUTRO = "Old soup, new name. Vika tells him the changes are coming anyway. Next scene, we see what happens."
CLOSING = ('vika', 'Пока!')
STORY = [
    ('vika', 'Зачем ты позвал меня сюда?', 'Why did you call me here?', [(184, 'Что такое? Зачем ты меня позвал?')], ''),
    ('barinov', 'Доброе утро, Вика! У меня для тебя сюрприз.', 'Good morning, Vika! I have a surprise for you.', [(185, 'Доброе утро'), (186, 'У меня для тебя сюрприз')], ''),
    ('barinov', 'Я наконец придумал абсолютно новое меню ресторана.', 'I finally came up with an absolutely new restaurant menu.', [(187, 'Новое меню')], ''),
    ('vika', 'Действительно новое? Покажи мне твои свежие идеи.', 'Really new? Show me your fresh ideas.', [(188, 'Действительно новое')], ''),
    ('barinov', 'Попробуй этот суп, это настоящий кулинарный шедевр!', 'Taste this soup, it is a real culinary masterpiece!', [(191, 'Суп'), (192, 'Гурме')], ''),
    ('vika', 'Подожди, это же твой обычный старый суп.', 'Wait, this is your usual old soup after all.', [(193, 'Это же твой луковый суп')], ''),
    ('barinov', 'Но я добавил сюда очень вкусные специи!', 'But I added very tasty spices here!', [(194, 'А нотки гибискуса?')], ''),
    ('vika', 'А это твоя обычная рыба из прошлого меню?', 'And is this your usual fish from the past menu?', [(196, 'А вот это?'), (198, 'Это твой старый буэбэс манифик?')], ''),
    ('barinov', 'Нет, это особое французское блюдо от шефа!', 'No, this is a special French dish from the chef!', [(199, 'Ля буэбэс манифик'), (200, 'нотки ля в блюде')], ''),
    ('vika', 'Ты просто изменил старые названия на новые!', 'You simply changed old names to new ones!', [(203, 'Это старые блюда. Ты просто название поменял, да?')], ''),
    ('barinov', 'Разве это не звучит великолепно для гостей?', 'Does that not sound magnificent for the guests?', [(204, 'Правда здорово? Гениально')], ''),
    ('vika', 'Ты не сможешь остановить эти важные перемены.', 'You will not be able to stop these important changes.', [(205, 'Значит так, Витя, у тебя все равно не получится сохранить все это старье'), (206, 'Перемены уже начались')], ''),
]
WALK = [
    (0, None, ["'Why did you call me here?' Vika uses the friendly form with the chef, so the verb is ", ('vika', 'позвал'), ', the plain past of calling someone over. We hear ', ('vika', 'сюда'), " for 'here' with motion, as opposed to just being somewhere."]),
    (1, None, ["'Good morning, Vika! I have a surprise for you.' Notice for 'morning' is neuter, so 'good' matches it. The 'I have' part is the Russian 'at me', followed by ", ('barinov', 'сюрприз'), " for 'surprise'."]),
    (2, None, ["'I finally came up with an absolutely new restaurant menu.' The verb ", ('barinov', 'придумал'), " is 'thought up'. We hear ", ('barinov', 'меню'), ", a borrowed word that never changes its ending. It is neuter, so 'new' matches it, and ", ('barinov', 'ресторана'), " means 'of the restaurant'."]),
    (3, None, ["'Really new? Show me your fresh ideas.' Now we can focus on the dialogue: ", ('vika', 'Действительно'), " means 'really' and is a good one for expressing doubt. Notice ", ('vika', 'Покажи'), " for 'show!', in the friendly form."]),
    (4, None, ["'Taste this soup, it is a real culinary masterpiece!' Let us look at the words: ", ('barinov', 'Попробуй'), " means both 'try' and 'taste', in the friendly form. Notice ", ('barinov', 'шедевр'), " for 'masterpiece', and ", ('barinov', 'настоящий'), " means 'real' or 'genuine'."]),
    (5, None, ["'Wait, this is your usual old soup after all.' Now let's look at the phrase: ", ('vika', 'Подожди'), " is 'wait a moment'. Notice ", ('vika', 'обычный'), " for 'usual' and ", ('vika', 'старый'), " for 'old', while the particle ", ('vika', 'же'), " says 'it's the same one'."]),
    (6, None, ["'But I added very tasty spices here!' Now we can consider this line: ", ('barinov', 'сюда'), " again, the 'here' with motion, because the spices went into the soup. Notice ", ('barinov', 'вкусные'), " for 'tasty', the everyday word for food you like, and ", ('barinov', 'добавил'), " for 'added'."]),
    (7, None, ["'And is this your usual fish from the past menu?' The word ", ('vika', 'рыба'), ' is fish, and ', ('vika', 'из'), ('vika', 'прошлого'), ('vika', 'меню'), " is 'from the past menu'. We hear ", ('vika', 'прошлого'), " for 'past' or 'last', as in 'last year'."]),
    (8, None, ["'No, this is a special French dish from the chef!' The describing words for 'special' and 'French' match the neuter word for 'dish'. The expression ", ('barinov', 'от'), ('barinov', 'шефа'), " means 'from the chef', putting a new ending on the chef."]),
    (9, None, ["'You simply changed old names to new ones!' We will break down the phrase: ", ('vika', 'названия'), ' refers to names of things, not people, which is the right word for dish names. The end is just ', ('vika', 'на'), ('vika', 'новые'), ", leaving out 'ones'."]),
    (10, None, ["'Does that not sound magnificent for the guests?' The word ", ('barinov', 'Разве'), " starts a question where the speaker expects a 'yes'. Notice ", ('barinov', 'звучит'), " for 'sounds', and ", ('barinov', 'великолепно'), " for 'magnificent'."]),
    (11, None, ["'You will not be able to stop these important changes.' Let us examine the sentence: ", ('vika', 'не'), ('vika', 'сможешь'), " is 'you won't be able', predicting the future. We hear ", ('vika', 'перемены'), " for 'changes', usually heard in the plural."]),
]
