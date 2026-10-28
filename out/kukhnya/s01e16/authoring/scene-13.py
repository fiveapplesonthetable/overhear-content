# Authoring module for kukhnya-s01e16-scene-13.
ID = 'kukhnya-s01e16-scene-13'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 16
SCENE = 13
TITLE = 'В поисках ключа  (In Search of the Key)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'inspector': 'Инспектор', 'senya': 'Сеня'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.16'
SOURCE_FILE = 'sources/kukhnya/s01/e16.ru.dual.srt'
INTRO = "Focused on in search of the key, Viktor Petrovich is asked to open the fridge. He pretends to need the spare key. Let's listen closely to Chef Viktor and the staff's exchange in Russian first, and then walk through each line together."
OPENER = 'Now let us examine the conversation line by line.'
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Viktor Petrovich is asked to open the fridge. He pretends to need the spare key. Next time you watch the episode, listen for the Russian expressions for 'inspector' and 'here' — you will catch every word right away. See you next time!"
CLOSING = ('inspector', 'Пока!')
STORY = [
    ('barinov', 'Инспектор здесь.', 'The inspector is here.', [], ''),
    ('senya', 'Я знаю.', 'I know.', [], ''),
    ('barinov', 'Он хочет проверить кухню.', 'He wants to check the kitchen.', [], ''),
    ('senya', 'Пусть проверяет.', 'Let him check.', [], ''),
    ('barinov', 'Он ищет нелегалов.', 'He is looking for illegals.', [], ''),
    ('senya', 'У нас их нет.', 'We do not have them.', [], ''),
    ('barinov', 'Где Федя?', 'Where is Fedya?', [], ''),
    ('senya', 'Он в холодильнике.', 'He is in the fridge.', [], ''),
    ('barinov', 'Отлично.', 'Excellent.', [], ''),
    ('inspector', 'Виктор Петрович, будьте любезны.', 'Viktor Petrovich, would you be so kind.', [(168, 'Виктор Петрович, будьте любезны, откройте, пожалуйста, холодильник.')], ''),
    ('inspector', 'Откройте, пожалуйста, холодильник.', 'Open the fridge, please.', [(168, 'Виктор Петрович, будьте любезны, откройте, пожалуйста, холодильник.')], ''),
    ('inspector', 'Я жду.', 'I am waiting.', [], ''),
]
WALK = [
    (0, None, "'The inspector is here.' Barinov urgently warns his colleague that the immigration officer has arrived on the premises."),
    (1, None, "'I know.' Senya acknowledges the warning calmly, indicating he is already aware of the situation."),
    (2, None, "'He wants to check the kitchen.' Explaining the immediate threat, the chef clarifies what the unexpected guest intends to do."),
    (3, None, "'Let him check.' Displaying casual confidence, the cook dismisses the danger and welcomes the search."),
    (4, None, "'He is looking for illegals.' The chef spells out the exact reason for the visit, highlighting the danger to their undocumented staff."),
    (5, None, "'We do not have them.' Playing dumb, the kitchen worker insists that there is no one breaking the law in their restaurant."),
    (6, None, "'Where is Fedya?' Barinov cuts to the chase, demanding the location of their specific vulnerable employee."),
    (7, None, "'He is in the fridge.' Senya casually reveals the freezing hiding place chosen for their coworker."),
    (8, None, "'Excellent.' The chef responds with sarcastic or genuine relief, depending on how safe he thinks that spot is."),
    (9, None, "'Viktor Petrovich, would you be so kind.' Using a highly formal and polite phrase, the guest commands the head cook to assist him."),
    (10, None, "'Open the fridge, please.' The officer politely but firmly demands access to the very place where the worker is hiding."),
    (11, None, "'I am waiting.' Adding pressure, the official makes it clear that he will not leave until his request is fulfilled."),
]
