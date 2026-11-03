# Authoring module for kukhnya-s01e08-scene-18.
ID = 'kukhnya-s01e08-scene-18'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 8
SCENE = 18
TITLE = "Обида шефа  (The Chef's Resentment)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'lyova': 'Лёва'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.08'
SOURCE_FILE = 'sources/kukhnya/s01/e08.ru.dual.srt'
INTRO = "Chef Barinov has shut himself in his office at Claude Monet, and his sous-chef Lyova is still trying to talk him round. Barinov has decided that nobody in the restaurant is loyal to him, and he says so at length. Here it is in Russian first."
OPENER = "Let's replay the sulk. Every complaint from Barinov gets a gentle answer from Lyova."
TRANSITION = "Now the whole conversation once more."
OUTRO = "Lyova's last line is a quiet, loyal one, and the Russian phrase for 'all the same' or 'anyway' is worth keeping: you'll hear it every single day. See you next time."
CLOSING = ('lyova', 'Пока!')
STORY = [
    ('barinov', 'Все эти люди вокруг — неблагодарные предатели.', 'All these people around are ungrateful traitors.', [(217, 'они все')], ''),
    ('lyova', 'Шеф, нельзя так плохо думать обо всех.', 'Chef, one should not think so badly about everyone.', [], ''),
    ('barinov', 'Я научил их готовить лучшие блюда города.', "I taught them to cook the city's best dishes.", [(217, 'они все')], ''),
    ('lyova', 'Каждый повар помнит ваш великий урок.', 'Every cook remembers your great lesson.', [], ''),
    ('barinov', 'Тогда почему они сейчас слушают чужие команды?', "Then why are they following someone else's orders now?", [], ''),
    ('lyova', 'Они просто боятся потерять своё рабочее место.', 'They are simply afraid of losing their job.', [], ''),
    ('barinov', 'Настоящий мастер никогда не боится трудностей.', 'A true master is never afraid of difficulties.', [], ''),
    ('lyova', 'Вы самый главный кулинарный мастер для нас.', 'You are the main culinary master for us.', [], ''),
    ('barinov', 'Пусть теперь сами справляются со сложным банкетом.', 'Let them handle the complex banquet themselves now.', [], ''),
    ('lyova', 'Без вашего участия на кухне наступит хаос.', 'Without your participation, chaos will break out in the kitchen.', [], ''),
    ('barinov', 'Вот и отлично, пусть увидят мою силу!', 'That is great, let them see my strength!', [], ''),
    ('lyova', 'Я всё равно останусь рядом с вами.', 'I will stay by your side anyway.', [], ''),
]
WALK = [
    (0, None, ["'All these people around are ungrateful traitors.' To express his frustration, he uses ", ('barinov', 'неблагодарные'), ' to call the people ungrateful.']),
    (1, None, ["'Chef, one should not think so badly about everyone.' Lyova gently corrects his boss with ", ('lyova', 'нельзя'), ', reminding him that such negative thoughts are not allowed.']),
    (2, None, ["'I taught them to cook the city's best dishes.' The chef proudly points out that he taught them everything by saying ", ('barinov', 'научил'), ' to emphasize his role as their mentor.']),
    (3, None, ["'Every cook remembers your great lesson.' Every cook in the kitchen remembers the lessons, which is why the word ", ('lyova', 'помнит'), ' is used here.']),
    (4, None, ["'Then why are they following someone else's orders now?' Questioning their loyalty, the chef says ", ('barinov', 'чужие'), ' to refer to the orders belonging to someone else.']),
    (5, None, ["'They are simply afraid of losing their job.' The sous-chef defends the team, explaining they are simply afraid by using ", ('lyova', 'боятся'), ' to describe their fear.']),
    (6, None, ["'A true master is never afraid of difficulties.' A true master would never be scared, which is expressed with ", ('barinov', 'никогда'), ' to mean absolutely never.']),
    (7, None, ["'You are the main culinary master for us.' Reassuring the boss of his importance, the word ", ('lyova', 'главный'), ' is chosen to mean the most important or main master.']),
    (8, None, ["'Let them handle the complex banquet themselves now.' Leaving them to deal with it, he wants them to manage themselves, using ", ('barinov', 'сами'), ' for emphasis.']),
    (9, None, ["'Without your participation, chaos will break out in the kitchen.' Warning about the consequences of his absence, the sentence starts with ", ('lyova', 'Без'), ' to mean without.']),
    (10, None, ["'That is great, let them see my strength!' He welcomes the chaos so they can witness his strength, referring to it as ", ('barinov', 'силу'), ' at the end.']),
    (11, None, ["'I will stay by your side anyway.' Promising to stay by his side, the loyal assistant says ", ('lyova', 'рядом'), ' to mean near or close.']),
]
