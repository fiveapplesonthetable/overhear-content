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
    (0, None, "'We will see about that yet!' Holding firm boldly around the guest, spoken Russian compresses the whole thought into just 3 words, skipping the extra helper words English needs."),
    (1, None, "'I have gotten hungry.' The guest responds steadily hearing Katya, to clear the air between them once and for all."),
    (2, None, '\'Gentlemen, let\'s take a lunch break.\' Talking about the gentlemen in front of Katya, the guest brings in "obedennyy" ("dining") to make the meaning unmistakable.'),
    (3, None, "'We will sign afterward.' Reacting warmly in this beat, spoken Russian compresses the whole thought into just 2 words, skipping the extra helper words English needs."),
    (4, None, "'Maxim, what do you have that is delicious here?' The guest prompts wryly how Max expects that to work in practice."),
    (5, None, '\'You know, we have a new menu.\' Bringing up a new menu in the exchange, Max uses "poyavilos" ("appeared", from "poyavitsya") to make the point stick.'),
    (6, None, '\'Molecular cuisine. Here you go.\' Max quietly directs this courtesy word at this moment using "pozhaluysta" ("please") — the all-purpose Russian politeness word that covers both "please" and "you\'re welcome".'),
    (7, None, "'Chemicals?' The guest checks bluntly if there is more going on behind the scenes."),
    (8, None, '\'No, everything is natural.\' Emphasizing how natural things are in the exchange, Max chooses "naturalnoye" ("natural", from the root "naturalnyy") so the guest hears the exact meaning.'),
    (9, None, '\'Like in your sausage? Then bring it.\' Focusing on the sausage in front of Max, the guest puts the question word "kak" right at the start so Max hears the focus immediately.'),
    (10, None, "'Spaghetti and duck, four portions!' Max proceeds candidly toward the guest, before the guest can change the subject."),
    (11, None, '\'Order received!\' Katya pushes back readily right here and chooses "prinyato" ("accepted, copy that", from the root "prinyatyy") so Max hears the exact meaning.'),
]
