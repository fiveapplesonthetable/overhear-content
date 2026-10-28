# Authoring module for kukhnya-s03e01-scene-14.
ID = 'kukhnya-s03e01-scene-14'
SHOW = 'kukhnya'
SEASON = 3
EPISODE = 1
SCENE = 14
TITLE = 'Обеденный перерыв  (Lunch Break)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'guest': 'Гость', 'katya': 'Катя', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S3.01'
SOURCE_FILE = 'sources/kukhnya/s03/e01.ru.srt'
INTRO = "After Fedya and Senya mock Max in the kitchen as a lowly waiter, Max decides to get revenge on Chef Barinov by recommending Katya's molecular menu to Nastya's hungry father."
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'That brings Scene Fourteen to a close. Listen for Max assuring the sausage-factory boss that the molecular dishes are completely natural. See you next time!'
CLOSING = ('katya', 'До встречи!')
STORY = [
    ('katya', 'Мы ещё посмотрим!', 'We will see about that yet!', [(255, 'Мы еще посмотрим')], 'adapted'),
    ('guest', 'Я проголодался.', 'I have gotten hungry.', [(256, 'я проголодался')], 'adapted'),
    ('guest', 'Господа, давайте сделаем обеденный перерыв.', "Gentlemen, let's take a lunch break.", [(257, 'Господа, давайте сделаем обеденный перерыв')], ''),
    ('guest', 'Потом подпишем.', 'We will sign afterward.', [(257, 'потом подпишем')], ''),
    ('guest', 'Максим, что тут у вас вкусного?', 'Maxim, what do you have that is delicious here?', [(258, 'Максим, будь любезен, что тут у вас')], 'adapted'),
    ('max', 'Знаете, у нас появилось новое меню.', 'You know, we have a new menu.', [(259, 'знаете, у нас появилось новое меню')], ''),
    ('max', 'Молекулярная кухня. Пожалуйста.', 'Molecular cuisine. Here you go.', [(260, 'Молекулярная кухня. Пожалуйста')], ''),
    ('guest', 'Химия?', 'Chemicals?', [(261, 'Химия')], 'adapted'),
    ('max', 'Нет, всё натуральное.', 'No, everything is natural.', [(261, 'Нет, всё натуральное')], ''),
    ('guest', 'Как в вашей колбасе? Тогда неси.', 'Like in your sausage? Then bring it.', [(262, 'Как в вашей колбасе'), (263, 'Тогда неси')], 'adapted'),
    ('max', 'Спагетти и утка, четыре порции!', 'Spaghetti and duck, four portions!', [(264, 'Спагетти'), (264, 'и утка')], 'adapted'),
    ('katya', 'Принято!', 'Order received!', [(265, 'Принято')], ''),
]
WALK = [
    (0, None, '\'We will see about that yet!\' Katya offers a clear style in their talk, putting "yeshchyo" ("more, still") alongside "posmotrim" ("have a look") in a tight, everyday turn of phrase.'),
    (1, None, '\'I have gotten hungry.\' The guest establishes a warm tone beside Max, putting "progolodalsya" ("got hungry") alongside "ya" ("I") in a tight, everyday turn of phrase.'),
    (2, None, '\'Gentlemen, let\'s take a lunch break.\' The guest takes a thoughtful tack at this moment, putting "gospoda" ("gentlemen") alongside "davayte" ("let\'s") in a tight, everyday turn of phrase.'),
    (3, None, '\'We will sign afterward.\' The guest displays a steady mood beside Max, pairing "potom" ("then") with "podpishem" ("will sign") to get the point across in plain spoken Russian.'),
    (4, None, '\'Maxim, what do you have that is delicious here?\' The guest quizzes quietly right away, combining "tut" ("here") and "vkusnogo" ("tasty, delicious") so the key meaning lands right away.'),
    (5, None, '\'You know, we have a new menu.\' Max displays a brisk stance for Katya, combining "znayete" ("know") and "poyavilos" ("appeared") so the key meaning lands right away.'),
    (6, None, '\'Molecular cuisine. Here you go.\' Max sustains a pointed manner toward the guest, joining "molekulyarnaya" ("molecular") to "kukhnya" ("kitchen") so every word pulls its weight.'),
    (7, None, '\'Chemicals?\' The guest tests lightly with Max now, putting all the weight on "khimiya" ("chemicals, chemistry") so the reply lands immediately.'),
    (8, None, '\'No, everything is natural.\' Max strikes a direct note during the exchange, combining "naturalnoye" ("natural") and "net" ("no") so the key meaning lands right away.'),
    (9, None, '\'Like in your sausage? Then bring it.\' The guest checks earnestly as they speak, linking "kak" ("how"), "kolbase" ("sausage"), and "togda" ("back then") in one brisk exchange.'),
    (10, None, '\'Spaghetti and duck, four portions!\' Max conveys a serious note for the guest, linking "spagetti" ("spaghetti"), "utka" ("duck"), and "portsii" ("portions") in one brisk exchange.'),
    (11, None, '\'Order received!\' Katya conveys an earnest bearing for Max, putting all the weight on "prinyato" ("accepted, copy that") so the reply lands immediately.'),
]
