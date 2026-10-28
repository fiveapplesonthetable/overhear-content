ID = "kukhnya-s02e01-scene-23"
SHOW = "kukhnya"
SEASON = 2
EPISODE = 1
SCENE = 23
TITLE = "Чаепитие шефа  (The Chef's Tea Party)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "igor": "angelina"}
LABELS = {"anya": "Шеф", "igor": "Игорь"}
SOURCE_NAME = "Кухня (Kukhnya) S2.01"
SOURCE_FILE = "sources/kukhnya/s02/e01.ru.dual.srt"
SOURCE_NOTE = "Scene 23"

INTRO = "Chef Barinov sits comfortably at the kitchen table and calmly drinks a cup of hot tea while complete chaos unfolds around him. Igor Valentinovich slowly approaches the chef, clearly annoyed by the man's relaxed behavior in the middle of a busy workday."

STORY = [
    ('igor', 'Что здесь происходит?',
     'What is happening here?',
     [], 'new'),
    ('anya', 'Мы просто работаем.',
     'We are just working.',
     [], 'new'),
    ('igor', 'На кухне полный хаос.',
     'There is complete chaos in the kitchen.',
     [], 'new'),
    ('igor', 'А вы сидите здесь.',
     'And you are sitting here.',
     [], 'new'),
    ('igor', 'Чайком балуемся, Виктор Петрович?',
     'Having some tea, Viktor Petrovich?',
     [(266, 'Чайком балуемся')], 'adapted'),
    ('anya', 'Да, чай очень вкусный.',
     'Yes, the tea is very tasty.',
     [], 'new'),
    ('anya', 'Я люблю отдыхать.',
     'I like to rest.',
     [], 'new'),
    ('anya', 'Это правильно.',
     'That is right.',
     [(267, 'Это правильно')], 'adapted'),
    ('igor', 'Вы должны работать.',
     'You must work.',
     [], 'new'),
    ('anya', 'Мои повара всё знают.',
     'My cooks know everything.',
     [], 'new'),
    ('anya', 'Они работают за меня.',
     'They work for me.',
     [], 'new'),
    ('igor', 'Это просто возмутительно.',
     'This is simply outrageous.',
     [], 'new'),
    ('anya', 'Не кричите на меня.',
     'Do not yell at me.',
     [], 'new'),
]

OPENER = "Let us break down this interaction."

WALK = [
    (4, None,
     "'Having some tea, Viktor Petrovich?' Russian leaves out 'am', 'is', or 'are' in the present tense, linking 'tea' straight to 'Petrovich'."),
    (7, None,
     "'That is right.' Notice the word order: 'this' comes first, and 'right' finishes the sentence."),
    (8, None,
     "'You must work.' Here 'you' sets up the idea, while 'to work' comes at the end for emphasis."),
    (11, None,
     "'This is simply outrageous.' You'll hear 'this' all the time in the show, here connected with 'outrageous'."),
]

TRANSITION = "Now let us listen to the conversation again without interruption."
OUTRO = "Chef Barinov remains completely unbothered by the boss's passive-aggressive remarks."
CLOSING = ('anya', 'Не кричите на меня.')
