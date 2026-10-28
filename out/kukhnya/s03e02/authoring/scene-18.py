# Authoring module for kukhnya-s03e02-scene-18.
ID = 'kukhnya-s03e02-scene-18'
SHOW = 'kukhnya'
SEASON = 3
EPISODE = 2
SCENE = 18
TITLE = "Чужой столик  (Someone Else's Table)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'ilya': 'Илья', 'max': 'Макс', 'sasha': 'Саша'}
SOURCE_NAME = 'Кухня (Kukhnya) S3.02'
SOURCE_FILE = 'sources/kukhnya/s03/e02.ru.srt'
INTRO = "When Ilya's fake guest arrives in a hurry, Max starts taking his order—but remembering the waiters' code, he hands the table over to waitress Sasha instead."
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "That brings Scene Eighteen to a close. Notice Ilya's horror when he realizes that Sasha, not Max, served his accomplice and brought the bill folder. See you next time!"
CLOSING = ('max', 'Всего хорошего!')
STORY = [
    ('sasha', 'Макс, позови Илью, к нему постоянный гость пришёл.', 'Max, call Ilya, a regular guest of his has arrived.', [(257, 'Макс'), (258, 'Позови Илью, к нему постоянный гость пришел')], 'adapted'),
    ('max', 'Да, конечно.', 'Yes, of course.', [(259, 'Да, конечно')], ''),
    ('max', 'Добрый день. Знаете, Ильи сегодня нет.', 'Good afternoon. You know, Ilya is not here today.', [(260, 'Добрый день. Знаете, Ильи сегодня')], 'adapted'),
    ('max', 'Могу я чем-то помочь?', 'Can I help you with something?', [(261, 'Могу я чем-то помочь')], ''),
    ('ilya', 'Да, я очень тороплюсь.', 'Yes, I am in a big hurry.', [(261, 'Да'), (262, 'Я очень тороплюсь')], 'adapted'),
    ('ilya', 'Будьте добры, тартар и кофе.', 'Please bring me tartare and coffee.', [(263, 'Будьте добры, тартар'), (263, 'кофе')], 'adapted'),
    ('max', 'Приятного аппетита.', 'Bon appetit.', [(264, 'Приятного аппетита')], ''),
    ('max', 'Чего стоишь?', 'Why are you standing here?', [(265, 'Чего стоишь')], ''),
    ('ilya', 'Да так, вышел подышать.', 'Oh nothing, I stepped out to get some air.', [(265, 'Да так вышел подышать')], ''),
    ('ilya', 'Макс, чего ты твой столик не забрал?', "Max, why didn't you take your table?", [(266, 'Макс, чего-то твой столик не забрал')], 'adapted'),
    ('max', 'Это столик Ильи. Передай ему заказ.', "That is Ilya's table. Pass the order to him.", [(269, 'это столик Ильи'), (270, 'передай ему заказ')], 'adapted'),
    ('sasha', 'Да я вынесла заказ, принесла счёт, он просто торопился.', 'I brought out the order and brought the bill, he was just in a hurry.', [(271, 'Да я вынесла заказ, принесла счет, он просто торопился')], ''),
]
WALK = [
    (0, None, "'Max, call Ilya, a regular guest of his has arrived.' Once Ilya should call Ilya a regular guest of his has arrived, Sasha can finally tell Ilya what she means."),
    (1, None, "'Yes, of course.' Around the table and guest, Max sets a calm, everyday tone with Ilya."),
    (2, None, "'Good afternoon. You know, Ilya is not here today.' Even though Ilya is not here today, Max keeps a steady face in front of Ilya."),
    (3, None, '\'Can I help you with something?\' Checking whether he helps Ilya with something cuts straight through the tension between Max and Ilya. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (4, None, "'Yes, I am in a big hurry.' Ilya explains that he is in a big hurry, keeping his voice calm and direct."),
    (5, None, "'Please bring me tartare and coffee.' Bringing him tartare and coffee is how Ilya lays out the situation for Max."),
    (6, None, "'Bon appetit.' Around the table and truth, Max sets a calm, everyday tone with Ilya."),
    (7, None, "'Why are you standing here?' Asking why Ilya standing here is cuts straight through the tension between Max and Ilya."),
    (8, None, "'Oh nothing, I stepped out to get some air.' Over the order and the kitchen, Ilya answers Max without a second thought."),
    (9, None, '\'Max, why didn\'t you take your table?\' Here wondering why not Max takes Max\'s table shows Ilya looking for the real truth. Speaking with the close, informal "you" strips away any polite distance between them.'),
    (10, None, "'That is Ilya's table. Pass the order to him.' Saying that that is Ilya table is how Max sets the tone with Ilya."),
    (11, None, "'I brought out the order and brought the bill, he was just in a hurry.' Because she brought out the order and brought the bill he was just in a hurry, Sasha treats the matter as settled."),
]
