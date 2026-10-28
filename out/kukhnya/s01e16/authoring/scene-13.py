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
    (0, None, "'The inspector is here.' Russian leaves out 'am', 'is', or 'are' in the present tense, linking 'inspector' straight to 'here'."),
    (1, None, "'I know.' Senya delivers a punchy one-word reaction built around the Russian word meaning 'know'."),
    (2, None, "'He wants to check the kitchen.' Notice how naturally this everyday Russian phrase expresses the speaker's point."),
    (3, None, "'Let him check.' Senya delivers a punchy one-word reaction built around the Russian word meaning 'is testing'."),
    (4, None, "'He is looking for illegals.' Notice how naturally this everyday Russian phrase expresses the speaker's point."),
    (5, None, "'We do not have them.' To express possession, Russian uses the preposition 'by' plus the matching word ending word followed by 'no'. Then Chef Viktor responds."),
    (6, None, "'Where is Fedya?' Chef Barinov delivers a punchy one-word reaction built around the Russian word meaning 'where'."),
    (7, None, "'He is in the fridge.' Senya delivers a punchy one-word reaction built around the Russian word meaning 'fridge'."),
    (8, None, "'Excellent.' Chef Barinov delivers a punchy one-word reaction built around the Russian word meaning 'perfect'."),
    (9, None, "'Viktor Petrovich, would you be so kind.' the inspector leads with the direct command form meaning 'be', followed by 'kind'."),
    (10, None, "'Open the fridge, please.' the inspector leads with the direct command form meaning 'open', followed by 'fridge'."),
    (11, None, "'I am waiting.' the inspector delivers a punchy conversational reaction built around the Russian word meaning 'I'm waiting'."),
]
