# Authoring module for kukhnya-s01e06-scene-18.
ID = 'kukhnya-s01e06-scene-18'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 6
SCENE = 18
TITLE = 'Секретный ингредиент  (The Secret Ingredient)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'louis': 'Луи'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.06'
SOURCE_FILE = 'sources/kukhnya/s01/e06.ru.dual.srt'
INTRO = "In the kitchen at Claude Monet, Barinov has just heard that the inspector turned down the free wine. He isn't giving up. If the man won't drink it, he'll eat it, and he tells Louis, the pastry chef, to put alcohol in everything. It's in Russian first."
OPENER = "Let's go back through the scheme. Barinov is very pleased with himself, and Louis is horrified."
TRANSITION = 'Now the whole scheme again, at full speed.'
OUTRO = 'Keep "napoit" and "nakormit" together: to get someone drunk and to feed someone up. Both have na- on the front, and Barinov makes a slogan of them. See you next time.'
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('barinov', 'Этот инспектор отказался пить наше вино!', 'This inspector refused to drink our wine!', [], ''),
    ('louis', 'Шеф, что же нам теперь делать?', 'Chef, what are we to do now?', [], ''),
    ('barinov', 'Раз не можем напоить, мы его накормим!', 'Since we cannot give him drink, we will feed him!', [(233, 'не можем напоить, мы тебя накормим')], ''),
    ('louis', 'Вы хотите добавить алкоголь в еду?', 'Do you want to add alcohol to food?', [], ''),
    ('barinov', 'Луи, приготовь для него десерт с коньяком!', 'Louis, prepare a dessert with cognac for him!', [(234, 'Луис, тебе десерт с коньяком')], ''),
    ('louis', 'Сколько ложек коньяка добавить в крем?', 'How many spoonfuls of cognac to add to the cream?', [], ''),
    ('barinov', 'Лей от души, коньяка не жалей!', 'Pour from the heart, do not spare cognac!', [], ''),
    ('louis', 'А как поступить с горячими блюдами?', 'And how to deal with hot dishes?', [], ''),
    ('barinov', 'В мясо мы щедро нальём сухое вино.', 'We will generously pour dry wine into the meat.', [], ''),
    ('louis', 'Инспектор точно почувствует вкус крепкого алкоголя.', 'The inspector will definitely taste strong alcohol.', [], ''),
    ('barinov', 'Он ничего не заметит в соусе!', 'He will not notice anything in the sauce!', [], ''),
    ('louis', 'Шеф, это очень дерзкий и опасный план.', 'Chef, this is a very daring and dangerous plan.', [], ''),
    ('barinov', 'Зато наш ресторан будет спасён, работай!', 'At least our restaurant will be saved, work!', [(236, 'Папочка будет готовить')], ''),
]
WALK = [
    (0, None, ["'This inspector refused to drink our wine!' The opening phrase meaning 'This inspector refused to drink our wine!' contains ", ('barinov', 'отказался'), ', showing he decided against it completely.']),
    (1, None, ["'Chef, what are we to do now?' In the pastry chef's worried question, the word ", ('louis', 'же'), ' adds a lot of extra urgency to his confusion.']),
    (2, None, ["'Since we cannot give him drink, we will feed him!' Here we see the boss start with ", ('barinov', 'Раз'), ', which means since or because in this context.']),
    (3, None, ["'Do you want to add alcohol to food?' Listen closely to the polite request starting with ", ('louis', 'хотите'), ', asking if he really wants to do this.']),
    (4, None, ["'Louis, prepare a dessert with cognac for him!' The head of the kitchen clearly commands ", ('barinov', 'приготовь'), ', telling his employee to get a sweet dish ready.']),
    (5, None, ["'How many spoonfuls of cognac to add to the cream?' Asking about the exact amount, the assistant says ", ('louis', 'Сколько'), ', to find out the number of spoonfuls needed.']),
    (6, None, ["'Pour from the heart, do not spare cognac!' Giving his passionate instruction, the big boss shouts ", ('barinov', 'Лей'), ', telling him to pour the drink freely and generously.']),
    (7, None, ["'And how to deal with hot dishes?' Wondering about the next step, the helper asks ", ('louis', 'поступить'), ', which means how to act or what action to take.']),
    (8, None, ["'We will generously pour dry wine into the meat.' Explaining the next part of the scheme, he says ", ('barinov', 'щедро'), ', meaning they will pour the drink very generously.']),
    (9, None, ["'The inspector will definitely taste strong alcohol.' Pointing out the obvious flaw, the baker says ", ('louis', 'точно'), ', meaning the man will absolutely notice the strong flavor.']),
    (10, None, ["'He will not notice anything in the sauce!' Brushing off the concern entirely, the leader states ", ('barinov', 'ничего'), ', meaning the inspector will notice absolutely nothing at all.']),
    (11, None, ["'Chef, this is a very daring and dangerous plan.' Still feeling very unsure, the poor guy calls it ", ('louis', 'дерзкий'), ', meaning the idea is extremely bold or cheeky.']),
    (12, None, ["'At least our restaurant will be saved, work!' Looking on the bright side, the older man begins with ", ('barinov', 'Зато'), ', shifting the focus to the positive outcome.']),
]
