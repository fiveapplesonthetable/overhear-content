# Authoring module for kukhnya-s01e02-scene-22.
ID = 'kukhnya-s01e02-scene-22'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 2
SCENE = 22
TITLE = 'Ищите везде  (Look Everywhere)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'lyova': 'Лёва'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.02'
SOURCE_FILE = 'sources/kukhnya/s01/e02.ru.dual.srt'
INTRO = "In the kitchen of Claude Monet, Chef Viktor Barinov fumes as his prized knife remains missing. After barking orders about a dirty box left lying around, he questions sous-chef Lyova, wildly guessing where the blade could have ended up. Let's listen to their conversation in Russian first."
OPENER = "Now let's examine Chef Barinov and Lyova's exchange line by line."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Lyova scrambles to continue the frantic search for Barinov's knife, unaware of where it has actually gone. Next time you watch the episode, listen for the Russian expressions for 'fast' and 'everywhere' — you will catch every word right away. See you next time!"
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('barinov', 'Ты почему тут поставил грязную коробку?', 'Why did you put a dirty box here?', [(235, 'коробку грязную поставил')], ''),
    ('barinov', 'Убери её отсюда очень быстро!', 'Remove it from here very quickly!', [(236, 'Убери давай быстро.')], ''),
    ('barinov', 'Лёва, вы уже нашли мой нож?', 'Lyova, have you already found my knife?', [(237, 'Лёва, нож нашли?')], ''),
    ('lyova', 'Мы ещё не нашли его, шеф.', 'We have not found it yet, Chef.', [(238, 'Ещё нет, шеф.')], ''),
    ('barinov', 'Вы точно везде хорошо искали?', 'Did you definitely look well everywhere?', [(238, 'Везде смотрели?')], ''),
    ('lyova', 'Да, мы всё проверили на кухне.', 'Yes, we checked everything in the kitchen.', [(239, 'Везде.')], ''),
    ('barinov', 'Значит, продолжайте искать дальше!', 'Then continue to look further!', [(239, 'Ну ищите.')], ''),
    ('barinov', 'Кто-то мог случайно оставить нож внутри.', 'Someone could accidentally leave the knife inside.', [(240, 'оставил там нож')], ''),
    ('barinov', 'Например, кто-то забыл нож в рыбе.', 'For example, someone forgot the knife in the fish.', [(241, 'Ну, в рыбе, например.')], ''),
    ('lyova', 'В рыбе? Это невозможно, шеф!', 'In the fish? That is impossible, Chef!', [(242, 'В рыбе?')], ''),
    ('barinov', 'Я не знаю. Ищите везде!', 'I do not know. Look everywhere!', [(243, 'Ищите везде.')], ''),
    ('lyova', 'Хорошо, шеф, мы всё найдём.', 'Alright, Chef, we will find everything.', [(244, 'Да, шеф.')], ''),
    ('barinov', 'Без ножа мы не сможем работать!', 'Without the knife we will not be able to work!', [], ''),
]
WALK = [
    (0, None, "'Why did you put a dirty box here?' Barinov scolds the kitchen staff for leaving clutter around."),
    (1, None, "'Remove it from here very quickly!' The head chef demands immediate cleanliness in the kitchen."),
    (2, None, "'Lyova, have you already found my knife?' Barinov checks in on the urgent search for his tool."),
    (3, None, "'We have not found it yet, Chef.' Lyova nervously reports that the blade has not turned up."),
    (4, None, "'Did you definitely look well everywhere?' Barinov presses his sous-chef to verify every spot."),
    (5, None, "'Yes, we checked everything in the kitchen.' Lyova confirms they searched all normal work areas."),
    (6, None, "'Then continue to look further!' The chef refuses to accept that the knife is gone."),
    (7, None, "'Someone could accidentally leave the knife inside.' Barinov suspects someone got careless while prepping."),
    (8, None, "'For example, someone forgot the knife in the fish.' The chef suggests an absurd place where it might be."),
    (9, None, "'In the fish? That is impossible, Chef!' Lyova reacts with complete disbelief at the wild suggestion."),
    (10, None, "'I do not know. Look everywhere!' Barinov insists that no possibility can be ruled out."),
    (11, None, "'Alright, Chef, we will find everything.' Lyova obediently promises to continue the search."),
    (12, None, "'Without the knife we will not be able to work!' Barinov emphasizes how crucial the blade is to the restaurant."),
]
