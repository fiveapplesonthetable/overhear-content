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
    (0, None, "'We will see about that yet!' Once they will see about that yet, Katya makes sure the guest hears every word. Russian puts the key word right up front so her emotion lands on the first beat."),
    (1, None, "'I have gotten hungry.' Having gotten hungry moves the conversation forward without extra drama."),
    (2, None, "'Gentlemen, let's take a lunch break.' Here taking a lunch break together sets up the next turn in their exchange."),
    (3, None, "'We will sign afterward.' The guest tells Katya that they will sign afterward without dressing it up."),
    (4, None, '\'Maxim, what do you have that is delicious here?\' The guest asks whether Maxim what do Katya has that is delicious here, refusing to let the point slide. In Russian you say "by me" or "with us" rather than "I have", so the situation sits right with the person.'),
    (5, None, "'You know, we have a new menu.' Mentioning that they have a new menu moves the talk in a new direction."),
    (6, None, "'Molecular cuisine. Here you go.' Max reminds the guest that here the guest goes before the moment passes."),
    (7, None, '\'Chemicals?\' Over the menu and the truth, the guest presses Katya for a straight answer. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (8, None, "'No, everything is natural.' Explaining that everything is natural lays the cards on the table for the guest."),
    (9, None, '\'Like in your sausage? Then bring it.\' Around the shift and revenge, the guest wants to know where Katya really stands. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (10, None, "'Spaghetti and duck, four portions!' With the shift and moment at stake, Max reacts without holding back. Russian puts the key word right up front so his emotion lands on the first beat."),
    (11, None, "'Order received!' By telling the guest to order received, Katya raises the stakes in the room at once."),
]
