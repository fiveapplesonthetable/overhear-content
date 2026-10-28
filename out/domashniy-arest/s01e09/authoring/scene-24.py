# Authoring module for domashniy-arest-s01e09-scene-24.
ID = 'domashniy-arest-s01e09-scene-24'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 9
SCENE = 24
TITLE = "Срочные дела Аркадия  (Arkady's Urgent Business)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'arkady': 'Аркадий', 'marina': 'Марина'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.09'
SOURCE_FILE = 'sources/domashniy-arest/s01/e09.ru.dual.srt'
INTRO = "After feeding Marina a fake story about hiding his money in a kindergarten, Arkady pretends he suddenly remembered his political duties. He excuses himself politely from the table to prepare Samsonov's campaign speech. Listen to their Russian conversation first, and do not worry about catching every single word."
OPENER = "Let's examine line by line how Arkady politely wraps up the conversation."
TRANSITION = "Now listen to Arkady and Marina's conversation one more time."
OUTRO = 'Arkady leaves the cafe having successfully planted the false clue. See you next time!'
CLOSING = ('arkady', 'Всего хорошего!')
STORY = [
    ('arkady', 'Господи, я совсем забыл!', 'Good heavens, I completely forgot!', [(709, 'Господи, я совсем забыл')], ''),
    ('arkady', 'Я должен написать речь для Самсонова.', 'I must write a speech for Samsonov.', [(710, 'Я же должен речь написать для Самсонова')], ''),
    ('marina', 'Какую речь? Вы уже уходите?', 'What speech? Are you already leaving?', [], 'Marina asks surprised'),
    ('arkady', 'Да, у нас скоро важные дебаты.', 'Yes, we have important debates soon.', [], 'Arkady explains the campaign rush'),
    ('marina', 'А как же наш прекрасный разговор?', 'And what about our wonderful conversation?', [], 'Marina tries to keep him'),
    ('arkady', 'Мы так чудесно с вами посидели!', 'We had such a wonderful time together!', [(711, 'Мы так чудесно с вами посидели')], ''),
    ('marina', 'Но вы даже не допили чай.', 'But you did not even finish your tea.', [], 'she gestures at his cup'),
    ('arkady', 'Я прошу прощения, теперь работа, к сожалению.', 'I ask for forgiveness, now it is work, unfortunately.', [(712, 'Я прошу прощения, теперь работа, к сожалению')], ''),
    ('marina', 'Вы вернётесь сюда вечером?', 'Will you return here in the evening?', [], 'Marina probes his schedule'),
    ('arkady', 'Дел очень много, не знаю.', 'There are so many tasks, I do not know.', [], 'Arkady stays noncommittal'),
    ('arkady', 'Я пойду. Всего хорошего!', 'I will go. All the best!', [(713, 'Я пойду'), (714, 'Всего хорошего')], ''),
    ('marina', 'До свидания, Аркадий Борисович.', 'Goodbye, Arkady Borisovich.', [], 'Marina watches him leave'),
]
WALK = [
    (0, None, "'Good heavens, I completely forgot!' Arkady feigns a sudden realization of urgency."),
    (1, None, "'I must write a speech for Samsonov.' Looking at his watch, he claims he urgently needs to draft a debate speech for Samsonov."),
    (2, 'Какую речь?', "'What speech?' Caught off guard by his sudden rush, Marina asks what speech he is talking about."),
    (2, 'Вы уже уходите?', "'Are you already leaving?' Disappointed that her sting is being cut short, she asks if he is really leaving already."),
    (3, None, "'Yes, we have important debates soon.' He uses the upcoming campaign debates as his excuse to bolt from the table."),
    (4, None, "'And what about our wonderful conversation?' Marina tries to guilt him into staying by reminding him how nicely they were talking."),
    (5, None, "'We had such a wonderful time together!' Laying on the charm, Arkady gushes about what a lovely time they just had together."),
    (6, None, "'But you did not even finish your tea.' Pointing to his cup, she notes that he hasn't even finished drinking his tea."),
    (7, None, "'I ask for forgiveness, now it is work, unfortunately.' With a theatrical sigh, he apologizes and says duty calls."),
    (8, None, "'Will you return here in the evening?' Still hoping to keep tabs on him, she asks if he will come back this evening."),
    (9, None, "'There are so many tasks, I do not know.' Keeping his options open, Arkady claims he is swamped with work and can't promise anything."),
    (10, 'Я пойду.', "'I will go.' Rising from the table, he excuses himself before she can ask another question."),
    (10, 'Всего хорошего!', "'All the best!' He offers a breezy, polite farewell as he heads for the door."),
    (11, None, "'Goodbye, Arkady Borisovich.' Left alone at the table, Marina bids him a formal goodbye by name and patronymic."),
]
