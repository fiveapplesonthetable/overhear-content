# Authoring module for kukhnya-s02e03-scene-16.
ID = 'kukhnya-s02e03-scene-16'
SHOW = 'kukhnya'
SEASON = 2
EPISODE = 3
SCENE = 16
TITLE = 'Где мой салат?  (Where is My Salad?)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'fedya': 'Федя', 'senya': 'Сеня'}
SOURCE_NAME = 'Кухня (Kukhnya) S2.03'
SOURCE_FILE = 'sources/kukhnya/s02/e03.ru.dual.srt'
INTRO = 'The kitchen staff is very busy preparing food for the evening guests. One of the cooks suddenly realizes that a dish he just prepared has mysteriously disappeared from his table.'
OPENER = "Now let's go back through the exchange around Where is My Salad? line by line and unpack how the Russian works."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "The cook continues searching for his missing dish while the others ignore him and focus on their own work. Next time you watch the episode, listen for the Russian expressions for 'salad' and 'to take' — you will catch every word right away. See you next time!"
CLOSING = ('senya', 'Пока!')
STORY = [
    ('senya', 'Привет. Где мой салат?', 'Hello. Where is my salad?', [], ''),
    ('fedya', 'Я его не брал.', 'I did not take it.', [], ''),
    ('senya', 'Утром он был здесь.', 'It was here in the morning.', [], ''),
    ('fedya', 'Спроси у других поваров.', 'Ask the other cooks.', [], ''),
    ('senya', 'Уи, ты мой салат не видел?', 'Hey, have you seen my salad?', [(280, 'ты мой салат не видел')], ''),
    ('fedya', 'Нет, я готовил десерты.', 'No, I was preparing desserts.', [], ''),
    ('senya', 'Куда он мог пропасть?', 'Where could it have gone?', [], ''),
    ('fedya', 'Может, его уже подали.', 'Maybe it was already served.', [], ''),
    ('senya', 'Это был мой лучший салат.', 'It was my best salad.', [], ''),
    ('fedya', 'Сделай новый, время есть.', 'Make a new one, there is time.', [], ''),
    ('senya', 'Гости будут ждать.', 'The guests will wait.', [], ''),
    ('fedya', 'Ничего страшного не случится.', 'Nothing terrible will happen.', [], ''),
    ('senya', 'Я не успею сделать новый.', 'I will not have time to make a new one.', [], ''),
    ('fedya', 'Тогда придумай что-нибудь другое.', 'Then think of something else.', [], ''),
]
WALK = [
    (0, None, "'Hey, have you seen my salad?' Coming back to his station, Senya asks Louis if he has seen his special salad."),
    (1, None, "'It was my best salad.' Not wanting to admit the leather belt was hidden in it, Senya claims it was his finest salad."),
    (2, None, "'Make a new one, there is time.' Unaware of what was in the bowl, Fedya tells him to just toss a fresh one while there is time."),
    (3, None, "'I will not have time to make a new one.' Senya panics because he knows the belt salad has already gone out to a guest."),
    (4, None, "'Then think of something else.' Fedya shrugs and tells him to come up with something else then."),
]
