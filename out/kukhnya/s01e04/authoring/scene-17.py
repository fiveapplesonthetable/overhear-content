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
OUTRO = 'Instead of helping Kostya, Max has talked himself into an imaginary romance. You\'ve learned how Russians say "a friend of mine": "odin drug", literally "one friend".'
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
    (0, None, '\'Nastya, I need to talk to you.\' "Mne nado" is the usual "to me necessary". "S toboy" is "with you", and the friendly form of "you" does the work.'),
    (1, None, '\'Yes, Max, what did you want to discuss?\' Nastya asks "about what did you want?", and the question trails off, as English questions can. "O chyom" is the "about what".'),
    (2, None, '\'I have a good friend.\' Russian says "at me there is one good friend", and "one" here means "a certain". It\'s how you introduce a friend with no name.'),
    (3, None, '\'And he really likes you very much.\' "Ty yemu nravishsya" is "you to him are pleasing", so you are the subject and he is "to him".'),
    (4, None, '\'A friend who likes me so much?\' "Kotoromu" is "to whom", a relative word that joins the friend to the liking. And "ya nravlyus\'" is "I am pleasing".'),
    (5, None, '\'Yes, he wants to ask you on a date.\' Max says it straight: his friend wants to invite her on a date. "To a date" takes "na" and a motion ending.'),
    (6, None, '\'I immediately understood everything perfectly!\' "Ponyala" ends in "-a" for Nastya. "Srazu" is "immediately" and "otlichno" is "perfectly".'),
    (7, None, '\'Guys always say that about friends!\' "Parni" is the plural of "paren\'", guy. "Pro druzey" is "about friends", with "druzey" the plural "of" form of "drug".'),
    (8, None, '\'Wait, you understood completely wrong.\' "Nepravil\'no" is "ne" plus "pravil\'no", correctly: incorrectly. "Sovsem" adds "completely".'),
    (9, None, '\'There is a real cosmic connection between us!\' Nastya declares that "between us there is a real cosmic connection". The word for connection comes from "to tie", so it\'s a tie between them.'),
    (10, None, '\'It is so great that you said this!\' "Zdorovo" is casual for "great", from "zdorov\'ye", health. "Tak... chto" joins "so great" to "that you said it".'),
    (11, None, '\'I must run, the chef is calling for hot food!\' "Pobegu" is "I will run", with "po-" for the start. "Goryacheye" is "hot" used as a noun, "the hot course".'),
    (12, None, '\'Now I really helped Kostya...\' "Vot eto" at the start is sarcastic, like "well, that went well". "Koste" is "to Kostya", the "to" form of his name.'),
]
