# Authoring module for kukhnya-s01e08-scene-29.
ID = 'kukhnya-s01e08-scene-29'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 8
SCENE = 29
TITLE = 'Пари между шефами  (Bet Between the Chefs)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'elena': 'Елена'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.08'
SOURCE_FILE = 'sources/kukhnya/s01/e08.ru.dual.srt'
INTRO = "The service is over. Barinov sits down with Elena Pavlovna, the chef from the rival restaurant, to enjoy winning their bet: she couldn't run his kitchen. Elena does not take it lying down. Here it is in Russian first."
OPENER = "Let's go through the gloating. Barinov is triumphant, and Elena has her own view."
TRANSITION = "Now the whole showdown in one go."
OUTRO = "Elena ends politely and still makes a demand: \"vy mne dolzhny otlichnyy uzhin\", you owe me a great dinner. The word \"dolzhny\" does the work of 'owe' and 'must'. See you next time."
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('barinov', 'Что и требовалось доказать, Елена Павловна!', 'That proves my point, Elena Pavlovna!', [(343, 'Что и требовалось доказать.')], ''),
    ('barinov', 'Я снова оказался абсолютно прав сегодня.', 'I turned out absolutely right again today.', [(344, 'Я говорю, что я оказался прав.')], ''),
    ('barinov', 'Впрочем, как и всегда, я выиграл пари!', 'As always, I won the bet!', [(345, 'Впрочем, как и всегда. Я выиграл парень.')], ''),
    ('elena', 'Виктор, прекратите говорить эту глупую ерунду.', 'Viktor, stop talking this silly nonsense.', [(346, 'Да не говорите ерунду.')], ''),
    ('elena', 'Я проработала на вашей кухне целый день.', 'I worked in your kitchen the whole day.', [(347, 'Я проработала у вас на кухне целый день')], ''),
    ('elena', 'Сначала всё было совершенно спокойно и нормально.', 'At first everything was completely calm and normal.', [(347, 'и все было нормально.')], ''),
    ('elena', 'А потом все повара словно заболели!', 'And then all the cooks seemed to get sick!', [(348, 'что-то случилось'), (349, 'Все как будто заболели.')], ''),
    ('elena', 'У вас на кухне работают сплошные инвалиды!', 'You have nothing but cripples working in your kitchen!', [(350, 'У вас не повара, а инвалиды.')], ''),
    ('barinov', 'Правильно, но это мои родные люди!', 'Right, but these are my own people!', [(351, 'Правильно.'), (352, 'Но это мои инвалиды.')], ''),
    ('barinov', 'И только я имею право их ругать.', 'And only I have the right to scold them.', [(352, 'И только я имею право их так называть.')], ''),
    ('barinov', 'Работа шефа — сделать из них команду!', "The chef's job is to make a team out of them!", [(353, 'И разве не в этом состоит работа шефа?'), (354, 'высококлассную команду?')], ''),
    ('elena', 'Вы умеете красиво оправдать любой беспорядок.', 'You know how to beautifully justify any mess.', [], ''),
    ('elena', 'Шеф, вы мне должны отличный ужин!', 'Chef, you owe me a great dinner!', [(355, 'А? Шеф?'), (356, 'Вы мне ужин должны.')], ''),
]
WALK = [
    (0, None, "'That proves my point, Elena Pavlovna!' Russians know \"chto i trebovalos dokazat\" as their 'Q.E.D.', the line that ends a proof in a school maths book. Barinov uses it to mean 'just as I said'."),
    (1, None, "'I turned out absolutely right again today.' Russians say \"okazalsya\", turned out, when something proved to be so. For being right, \"pravyy\" shrinks to \"prav\"."),
    (2, None, "'As always, I won the bet!' A bet is \"pari\", borrowed from French, and like many such loans its ending never changes. The opening \"vprochem\" is 'come to think of it', a slightly bookish way to add something."),
    (3, None, "'Viktor, stop talking this silly nonsense.' Elena uses his first name and the polite \"prekratite\", stop. The nonsense, \"erunda\", takes -u as the thing being talked: \"glupuyu erundu\"."),
    (4, None, "'I worked in your kitchen the whole day.' Elena's \"prorabotala\" is \"rabotala\", worked, with \"pro-\", which means 'all through a stretch of time'. And \"tselyy den\", the whole day, needs no word for 'for'."),
    (5, None, "'At first everything was completely calm and normal.' Since \"vsyo\", everything, counts as an 'it', the word for 'was' is \"bylo\". And \"snachala\", at first, is \"s\" plus \"nachalo\", beginning."),
    (6, None, "'And then all the cooks seemed to get sick!' Here \"slovno\" means 'as if' or 'like', a little more literary than \"budto\". With \"zaboleli\" the cooks have fallen ill, not just been ill."),
    (7, None, "'You have nothing but cripples working in your kitchen!' The word \"sploshnye\", nothing but, literally means solid or continuous. And \"invalidy\" is a harsh word for disabled people, which Elena throws at the cooks as an insult."),
    (8, None, "'Right, but these are my own people!' Barinov agrees, \"pravilno\", and turns her insult around. In Russian \"rodnye\" means kin, one's own family, so he is calling the cooks family."),
    (9, None, "'And only I have the right to scold them.' To have the right is \"imet pravo\", with \"imet\", a formal 'to have'. And \"rugat\", to scold, also means to swear at."),
    (10, None, "'The chef's job is to make a team out of them!' The dash stands in for 'is', as it often does between two naming words. To make out of is \"sdelat iz\", and after \"iz\" 'them' is \"nikh\"."),
    (11, None, "'You know how to beautifully justify any mess.' Inside \"opravdat\", to justify, sits \"pravda\", truth. And \"besporyadok\", mess, is \"bez\", without, plus \"poryadok\", order."),
    (12, None, "'Chef, you owe me a great dinner!' The word \"dolzhny\" means both 'must' and 'owe', and the person owed comes as 'to me', \"mne\". Since \"otlichno\" is also the top mark in Russian schools, \"otlichnyy\" is high praise."),
]
