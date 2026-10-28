# Authoring module for kukhnya-s01e17-scene-23.
ID = 'kukhnya-s01e17-scene-23'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 17
SCENE = 23
TITLE = 'Тайна паспорта  (The Secret of the Passport)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'max': 'Макс', 'senya': 'Сеня'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.17'
SOURCE_FILE = 'sources/kukhnya/s01/e17.ru.dual.srt'
INTRO = "During the celebration in the kitchen, Chef Viktor examines Max's passport on the counter. Looking at the official stamp, Viktor notices that Max's birthday is actually in February, uncovering Max's well-intentioned lie. Let's listen to their conversation in Russian first."
OPENER = "Now let's examine this surprising revelation line by line."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Faced with the undeniable proof in his passport, Max realizes that even a lie told for good reasons carries serious consequences. Next time you watch the episode, listen for the Russian expressions for 'to show' and 'passport' — you will catch every word right away. See you next time!"
CLOSING = ('max', 'Пока!')
STORY = [
    ('barinov', 'Покажи мне свой паспорт, Макс.', 'Show me your passport, Max.', [(327, 'Паспорте!')], ''),
    ('max', 'Вот мой паспорт, шеф.', 'Here is my passport, chef.', [(327, 'Паспорте!')], ''),
    ('barinov', 'А почему день рождения в феврале?', 'And why is the birthday in February?', [(327, 'А что это тебе день рождения в феврале, а?')], ''),
    ('senya', 'Твой день рождения не сегодня?', 'Your birthday is not today?', [(327, 'день рождения в феврале')], ''),
    ('max', 'Я хотел сделать вам приятное.', 'I wanted to please you.', [(329, 'чтобы сделать тебе приятное')], ''),
    ('barinov', 'Ты соврал нам про праздник?', 'Did you lie to us about the holiday?', [(330, 'немножко соврать')], ''),
    ('max', 'Я хотел забыть все обиды.', 'I wanted to forget all grudges.', [(328, 'забыть свои обиды')], ''),
    ('senya', 'Но врать друзьям нельзя.', 'But one must not lie to friends.', [(330, 'соврать')], ''),
    ('barinov', 'Любая ложь — это плохо.', 'Any lie is bad.', [(331, 'за любое вранье')], ''),
    ('max', 'Я очень виноват перед вами.', 'I am very guilty before you.', [(331, 'приходится платить')], ''),
    ('barinov', 'За любой обман надо отвечать.', 'For any deceit one must answer.', [(331, 'за любое вранье рано или поздно приходится платить.')], ''),
    ('senya', 'Правда всегда открывается.', 'The truth always reveals itself.', [(331, 'Правда')], ''),
    ('max', 'За любой обман приходится платить.', 'For any deceit one has to pay.', [(331, 'за любое вранье рано или поздно приходится платить.')], ''),
]
WALK = [
    (0, None, "'Show me your passport, Max.' Barinov demands proof of identity, sensing something is wrong."),
    (1, None, "'Here is my passport, chef.' Max hands over the document without hesitation."),
    (2, None, "'And why is the birthday in February?' Barinov points out a glaring inconsistency, demanding an explanation."),
    (3, None, "'Your birthday is not today?' Senya expresses surprise, realizing the whole premise was false."),
    (4, None, "'I wanted to please you.' Max tries to justify his actions by claiming good intentions."),
    (5, None, "'Did you lie to us about the holiday?' Barinov asks a direct question to confirm the extent of the deception."),
    (6, None, "'I wanted to forget all grudges.' Max provides his emotional reasoning for the elaborate ruse."),
    (7, None, "'But one must not lie to friends.' Senya lays down a fundamental moral rule about trust."),
    (8, None, "'Any lie is bad.' Barinov makes a blanket statement condemning dishonesty."),
    (9, None, "'I am very guilty before you.' Max expresses deep remorse, acknowledging his fault."),
    (10, None, "'For any deceit one must answer.' Barinov emphasizes that actions have consequences."),
    (11, None, "'The truth always reveals itself.' Senya adds a philosophical note about the inevitability of discovery."),
    (12, None, "'For any deceit one has to pay.' Max accepts his fate, agreeing that he must face the repercussions."),
]
