ID = "kukhnya-s02e03-scene-16"
SHOW = "kukhnya"
SEASON = 2
EPISODE = 3
SCENE = 16
TITLE = 'Где мой салат?  (Where is My Salad?)'
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "fedya": "anja"}
LABELS = {"anya": "Сеня", "fedya": "Федя"}
SOURCE_NAME = "Кухня (Kukhnya) S2.03"
SOURCE_FILE = "sources/kukhnya/s02/e03.ru.dual.srt"
SOURCE_NOTE = "Scene 16"

INTRO = 'The kitchen staff is very busy preparing food for the evening guests. One of the cooks suddenly realizes that a dish he just prepared has mysteriously disappeared from his table.'

STORY = [
    ('anya', 'Привет. Где мой салат?',
     'Hello. Where is my salad?',
     [], 'new'),
    ('fedya', 'Я его не брал.',
     'I did not take it.',
     [], 'new'),
    ('anya', 'Утром он был здесь.',
     'It was here in the morning.',
     [], 'new'),
    ('fedya', 'Спроси у других поваров.',
     'Ask the other cooks.',
     [], 'new'),
    ('anya', 'Уи, ты мой салат не видел?',
     'Hey, have you seen my salad?',
     [(280, 'ты мой салат не видел')], 'adapted'),
    ('fedya', 'Нет, я готовил десерты.',
     'No, I was preparing desserts.',
     [], 'new'),
    ('anya', 'Куда он мог пропасть?',
     'Where could it have gone?',
     [], 'new'),
    ('fedya', 'Может, его уже подали.',
     'Maybe it was already served.',
     [], 'new'),
    ('anya', 'Это был мой лучший салат.',
     'It was my best salad.',
     [], 'new'),
    ('fedya', 'Сделай новый, время есть.',
     'Make a new one, there is time.',
     [], 'new'),
    ('anya', 'Гости будут ждать.',
     'The guests will wait.',
     [], 'new'),
    ('fedya', 'Ничего страшного не случится.',
     'Nothing terrible will happen.',
     [], 'new'),
    ('anya', 'Я не успею сделать новый.',
     'I will not have time to make a new one.',
     [], 'new'),
    ('fedya', 'Тогда придумай что-нибудь другое.',
     'Then think of something else.',
     [], 'new'),
]

OPENER = "Let us break down this interaction."

WALK = [
    (4, None,
     "'Hey, have you seen my salad?' In Russian, 'oui' leads into 'saw' in a very natural everyday phrasing."),
    (8, None,
     "'It was my best salad.' Notice the word order: 'this' comes first, and 'salad' finishes the sentence. Then Fedya replies."),
    (9, None,
     "'Make a new one, there is time.' The first content word means 'make', and 'there is' rounds out the thought."),
    (12, None,
     "'I will not have time to make a new one.' You'll hear 'I' all the time in the show, here connected with 'new'."),
    (13, None,
     "'Then think of something else.' In Russian, 'back then' leads into 'another' in a very natural everyday phrasing."),
]

TRANSITION = "Now let us listen to the conversation again without interruption."
OUTRO = 'The cook continues searching for his missing dish while the others ignore him and focus on their own work.'
CLOSING = ('anya', 'Гости будут ждать.')
