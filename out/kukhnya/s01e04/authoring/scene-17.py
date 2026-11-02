# Authoring module for kukhnya-s01e04-scene-17.
ID = 'kukhnya-s01e04-scene-17'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 4
SCENE = 17
TITLE = 'Космическая связь  (A Cosmic Connection)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'max': 'Макс', 'nastya': 'Настя'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.04'
SOURCE_FILE = 'sources/kukhnya/s01/e04.ru.dual.srt'
INTRO = 'Max goes to Nastya to put in a good word for Kostya, but he explains it so clumsily that she is sure Max is talking about himself. Here is the misunderstanding in Russian first.'
OPENER = "Let's follow the mix-up."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'Instead of helping Kostya, Max has talked himself into an imaginary romance. You\'ve learned how to say a friend of mine, literally "one friend".'
CLOSING = ('max', 'Пока!')
STORY = [
    ('max', 'Настя, мне надо с тобой поговорить.', 'Nastya, I need to talk to you.', [(221, 'Мне надо с тобой поговорить')], ''),
    ('nastya', 'Да, Макс, о чём ты хотел?', 'Yes, Max, what did you want to discuss?', [], ''),
    ('max', 'У меня есть один хороший друг.', 'I have a good friend.', [], ''),
    ('max', 'И ты ему очень сильно нравишься.', 'And he really likes you very much.', [(222, 'ты очень нравишься')], ''),
    ('nastya', 'Друг, которому я так нравлюсь?', 'A friend who likes me so much?', [(223, 'Друг, которому я нравлюсь')], ''),
    ('max', 'Да, он хочет пригласить тебя на свидание.', 'Yes, he wants to ask you on a date.', [(226, 'пригласить тебя на свидание')], ''),
    ('nastya', 'Я сразу всё отлично поняла!', 'I immediately understood everything perfectly!', [(229, 'Я поняла')], ''),
    ('nastya', 'Парни всегда так про друзей говорят!', 'Guys always say that about friends!', [(230, 'про друзей говорят')], ''),
    ('max', 'Подожди, ты совсем неправильно поняла.', 'Wait, you understood completely wrong.', [], ''),
    ('nastya', 'Между нами есть настоящая космическая связь!', 'There is a real cosmic connection between us!', [(233, 'космическая связь')], ''),
    ('nastya', 'Так здорово, что ты это сказал!', 'It is so great that you said this!', [(234, 'ты это сказал')], ''),
    ('nastya', 'Я побегу, шеф зовёт горячее!', 'I must run, the chef is calling for hot food!', [(236, 'Я побегу')], ''),
    ('max', 'Вот это я помог Косте...', 'Now I really helped Kostya...', [], ''),
]
WALK = [
    (0, None, ['\'Nastya, I need to talk to you.\' The language puts the person who needs in the "to" form: ', ('max', 'мне надо'), ', literally "to me it is needed". The phrase for "with you", ', ('max', 'с тобой'), ', comes from the familiar "you", so this is a friend talking.']),
    (1, None, ['\'Yes, Max, what did you want to discuss?\' The question translates to "about what did you want?", ', ('nastya', 'о чём ты хотел?'), ' with the action word for "to talk" left unsaid.']),
    (2, None, ['\'I have a good friend.\' The phrase for "I have", ', ('max', 'У меня есть'), ', literally means "at me there is". The number one, ', ('max', 'один'), ', here translates to "a certain", meaning a friend of mine.']),
    (3, None, ['\'And he really likes you very much.\' This translates to "you to him are very much pleasing", ', ('max', 'ты ему очень сильно нравишься.'), '. The phrase for "to him", ', ('max', 'ему'), ', points out the person who feels the liking.']),
    (4, None, ['\'A friend who likes me so much?\' The Russian term for "who", ', ('nastya', 'которому'), ', translates to "to whom", because it pairs with ', ('nastya', 'я так нравлюсь?'), ', literally "I am so pleasing".']),
    (5, None, ['\'Yes, he wants to ask you on a date.\' Going to an event uses the little word for "on", so a date is ', ('max', 'на свидание.'), ', built from the same pattern as going to work. The expression for "you", ', ('max', 'тебя'), ', represents the person being invited.']),
    (6, None, ['\'I immediately understood everything perfectly!\' The action word for "understood", ', ('nastya', 'поняла!'), ', ends with an "a" sound because Nastya is a woman. The term for "immediately", ', ('nastya', 'сразу'), ', translates to "at once".']),
    (7, None, ['\'Guys always say that about friends!\' The Russian term for "guys", ', ('nastya', 'Парни'), ', is the multiple form of "guy". The phrase for "about friends", ', ('nastya', 'про друзей'), ', is built from the naming word for friend.']),
    (8, None, ['\'Wait, you understood completely wrong.\' The Russian term for "wrong", ', ('max', 'неправильно'), ', is built from the word for "not" plus "correctly". The Russian expression for "completely" is ', ('max', 'совсем'), '.']),
    (9, None, ['\'There is a real cosmic connection between us!\' The phrase for "between us" is ', ('nastya', 'Между нами'), '. The Russian term for "connection", ', ('nastya', 'связь!'), ', is built from the action word for "to tie".']),
    (10, None, ['\'It is so great that you said this!\' The phrase for "great", ', ('nastya', 'здорово,'), ', is built from the Russian term for health. The combination ', ('nastya', 'так'), ' and ', ('nastya', 'что'), ' translates to "so" and "that".']),
    (11, None, ['\'I must run, the chef is calling for hot food!\' The phrase for "I will run", ', ('nastya', 'побегу,'), ', translates to "I will run off", with a little piece added for setting off. The describing word for "hot", ', ('nastya', 'горячее!'), ', works as a naming word here, meaning the hot course.']),
    (12, None, ['\'Now I really helped Kostya...\' The starting phrase, ', ('max', 'Вот это'), ', translates to a sarcastic "well, that is how". The name Kostya becomes ', ('max', 'Косте...'), ', literally "to Kostya", because the action word for "help" points to someone.']),
]
