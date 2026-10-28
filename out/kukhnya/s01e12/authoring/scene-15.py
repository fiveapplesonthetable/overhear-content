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
INTRO = 'Chef Barinov calls Vika into the kitchen to show her his brand-new menu. She takes a look at the soup and the fish and notices that something is off. Here is their conversation in Russian first.'
OPENER = "Let's go back through it slowly, and watch Vika spot the trick."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'Vika leaves smiling, and Barinov carries on admiring his old soup with its new name. Next time you watch, see if you can spot a dish he has only renamed. Catch you next time.'
CLOSING = ('vika', 'Пока!')
STORY = [
    ('vika', 'Виктор Петрович, зачем вы позвали меня сюда?', 'Viktor Petrovich, why did you call me here?', [(184, 'Что такое? Зачем ты меня позвал?')], ''),
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
    (0, None, "'Viktor Petrovich, why did you call me here?' 'Vy' and 'pozvali' are both in the polite form, so Vika is using the formal 'you'. 'Syuda' is 'to here', as in coming over, while 'zdes' would be 'at here'."),
    (1, None, "'Good morning, Vika! I have a surprise for you.' 'Utro' is a neuter word, so 'good' is 'dobroe', not 'dobry'. 'U menya' is 'at me', which is how Russians say 'I have', and 'dlya tebya' is 'for you'."),
    (2, None, "'I finally came up with an absolutely new restaurant menu.' 'Nakonets' is 'finally', 'pridumal' is 'thought up', and 'absolyutno' is 'absolutely'. 'Menyu' is neuter and never changes, so 'new' is 'novoe'."),
    (3, None, "'Really new? Show me your fresh ideas.' 'Deystvitelno' means 'really' and is a good one for expressing doubt. 'Pokazhi' is 'show!', in the friendly form."),
    (4, None, "'Taste this soup, it is a real culinary masterpiece!' 'Poprobuy' means both 'try' and 'taste', in the friendly form. 'Shedevr' is the French 'chef-d'oeuvre' reworked, and 'kulinarny' is the same word as 'culinary'."),
    (5, None, "'Wait, this is your usual old soup after all.' 'Podozhdi' is 'wait a moment'. 'Obychny' means 'usual' and 'stary' means 'old', and the little 'zhe' says 'it's the same one'."),
    (6, None, "'But I added very tasty spices here!' Barinov stresses 'here', 'syuda', which actually means 'to here', as if he were pouring them in. The tasty bit is 'vkusny', and it's what you'd say about food you like."),
    (7, None, "'And is this your usual fish from the past menu?' 'Ryba' is fish, and 'iz proshlogo menyu' is 'from the past menu'. 'Proshly' means 'past' or 'last', as in 'last year'."),
    (8, None, "'No, this is a special French dish from the chef!' 'Osoboe' means 'special', and it's neuter to match 'blyudo'. 'Ot shefa' means 'from the chef', with the 'a' coming from 'ot'."),
    (9, None, "'You simply changed old names to new ones!' 'Nazvaniya' are names of things, not people, and that is the word to use for dish names. Russian leaves out the word 'ones', so it's just 'into new'."),
    (10, None, "'Does that not sound magnificent for the guests?' 'Razve' starts a question where the speaker expects a 'yes'. 'Zvuchit' is 'sounds', and 'velikolepno' means 'magnificent'."),
    (11, None, "'You will not be able to stop these important changes.' 'Ne smozhesh' is 'you won't be able', so Vika is predicting the future. 'Peremeny' is 'changes' and it's always plural."),
]
