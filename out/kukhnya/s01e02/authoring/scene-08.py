# Authoring module for kukhnya-s01e02-scene-08.
ID = 'kukhnya-s01e02-scene-08'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 2
SCENE = 8
TITLE = 'Спасти шефа  (Saving the Head Chef)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'fedya': 'Федя', 'senya': 'Сеня', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.02'
SOURCE_FILE = 'sources/kukhnya/s01/e02.ru.dual.srt'
INTRO = "Vika brings alarming news to the kitchen: Chef Barinov has refused to cook until his knife is found, and the owner might fire him. Senya and Fedya, two of the cooks, argue about whether they should cook the dish themselves. Here's the conversation first."
OPENER = "Let's go back through the argument."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'They go back and forth, and in the end they decide to risk it. You\'ve heard the phrase for "you\'re right", which is a good phrase for any argument.'
CLOSING = ('fedya', 'Пока!')
STORY = [
    ('vika', 'Шеф наотрез отказывается готовить это блюдо.', 'Chef flatly refuses to cook this dish.', [(119, 'шеф отказывается готовить')], ''),
    ('senya', 'Но почему? Что случилось на кухне?', 'But why? What happened in the kitchen?', [], ''),
    ('vika', 'Он потерял свой любимый нож.', 'He lost his favorite knife.', [], ''),
    ('vika', 'Скоро у вас будет новый шеф!', 'Soon you will have a new chef!', [(120, 'Скоро у вас будет новый шеф')], ''),
    ('fedya', 'Его уволят, если он не приготовит фрикасе.', 'He will be fired if he does not make the fricassee.', [(121, 'не приготовит'), (125, 'его уволят')], ''),
    ('senya', 'Ребята, давайте сами приготовим это блюдо!', 'Guys, let us cook this dish ourselves!', [(122, 'Давайте сами приготовим')], ''),
    ('fedya', 'Ты с ума сошёл? Он нас убьёт!', 'Are you out of your mind? He will kill us!', [(123, 'он самих сожрет')], ''),
    ('senya', 'Да, ты прав, лучше не рисковать.', 'Yes, you are right, better not risk it.', [(124, 'ты прав, лучше не рисковать')], ''),
    ('fedya', 'А если мы не приготовим, шефа уволят.', 'But if we do not cook, Chef will be fired.', [(125, 'А если не приготовим, его уволят')], ''),
    ('senya', 'Точно, ты прав, надо срочно готовить!', 'Exactly, you are right, we must cook right away!', [(126, 'ты прав, надо готовить')], ''),
    ('fedya', 'Чёрт, я запутался. Это опасная идея.', 'Darn, I am confused. This is a dangerous idea.', [(128, 'я запутался. Это плохая идея')], ''),
    ('senya', 'Но мы обязаны спасти нашего шефа.', 'But we have a duty to save our chef.', [], ''),
    ('fedya', 'Ладно, включай плиту и доставай мясо!', 'All right, turn on the stove and get the meat!', [], ''),
]
WALK = [
    (0, None, ['\'Chef flatly refuses to cook this dish.\' The word for "flatly", ', ('vika', 'наотрез'), ', is built from the action word meaning to cut off, as if the answer were cut short. The word for "refuses", ', ('vika', 'отказывается'), ', ends with the little "self" ending many action words carry.']),
    (1, None, ['\'But why? What happened in the kitchen?\' The phrase ', ('senya', 'Что случилось'), ', literally translates to "what happened", which is the question for any trouble. The phrase ', ('senya', 'на кухне?'), ', translates to "on the kitchen", as they always put it.']),
    (2, None, ['\'He lost his favorite knife.\' The describing word for favourite, ', ('vika', 'любимый'), ', is literally "loved". The word for "his own", ', ('vika', 'свой'), ', is one short little word, and the action word for "lost" is ', ('vika', 'потерял'), '.']),
    (3, None, ['\'Soon you will have a new chef!\' It literally translates to "at you will be", the "I have" pattern but in the future. The word for "soon" is ', ('vika', 'Скоро'), '.']),
    (4, None, ['\'He will be fired if he does not make the fricassee.\' The word for "they will fire" is ', ('fedya', 'уволят,'), ', with nobody named as doing it. The word for the dish, ', ('fedya', 'фрикасе.'), ', is borrowed from French and never changes its ending.']),
    (5, None, ['\'Guys, let us cook this dish ourselves!\' The word for guys, ', ('senya', 'Ребята,'), ', is for any informal group. The word ', ('senya', 'давайте'), ' turns the next action word into "let\'s", and the word for "ourselves" is ', ('senya', 'сами'), '.']),
    (6, None, ['\'Are you out of your mind? He will kill us!\' The phrase ', ('fedya', 'с ума сошёл?'), ' literally translates to "went off the mind", which they say when someone is being reckless. The action word for "will kill" is ', ('fedya', 'убьёт!'), '.']),
    (7, None, ['\'Yes, you are right, better not risk it.\' The describing word for "right", ', ('senya', 'прав,'), ', is what a man says, and a woman would add an extra sound at the end. Then the phrase for "better not", ', ('senya', 'лучше не'), ', which is as short as it sounds.']),
    (8, None, ['\'But if we do not cook, Chef will be fired.\' The phrase ', ('fedya', 'А если мы не приготовим,'), ' translates to "but if we don\'t cook". It uses the same nameless action word for "they\'ll fire", ', ('fedya', 'уволят,'), ', as before.']),
    (9, None, ['\'Exactly, you are right, we must cook right away!\' The word ', ('senya', 'надо'), ' translates to "it\'s necessary", the way to say "we must". The word for urgently, ', ('senya', 'срочно'), ', has the word for a deadline hiding in it.']),
    (10, None, ['\'Darn, I am confused. This is a dangerous idea.\' The word ', ('fedya', 'Чёрт,'), ' literally translates to "devil", but it\'s a mild curse. The word for "I got confused", ', ('fedya', 'запутался.'), ', is built from the action word to tangle at its heart.']),
    (11, None, ['\'But we have a duty to save our chef.\' The word for "obliged", ', ('senya', 'обязаны'), ', belongs to the same family as the word for definitely. The action word to save, ', ('senya', 'спасти'), ', is built from the same origin as the word for thank you, which began as "God save you".']),
    (12, None, ['\'All right, turn on the stove and get the meat!\' Both action words end in a friendly command sound: ', ('fedya', 'включай'), ', switch on, and ', ('fedya', 'доставай'), ', take out. The word for stove, ', ('fedya', 'плиту'), ', changes its ending sound because it\'s the thing being switched on.']),
]
