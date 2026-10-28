ID = "kukhnya-s02e01-scene-24"
SHOW = "kukhnya"
SEASON = 2
EPISODE = 1
SCENE = 24
TITLE = 'Больше чая  (More Tea)'
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "igor": "angelina"}
LABELS = {"anya": "Шеф", "igor": "Игорь"}
SOURCE_NAME = "Кухня (Kukhnya) S2.01"
SOURCE_FILE = "sources/kukhnya/s02/e01.ru.dual.srt"
SOURCE_NOTE = "Scene 24"

INTRO = "The intense tension between Chef Barinov and his boss Igor Valentinovich continues to grow in the busy kitchen. The chef deliberately asks the frustrated boss to serve him another cup of tea, trying to test the man's patience and show who is really in charge."

STORY = [
    ('anya', 'Мой чай уже закончился.',
     'My tea has already finished.',
     [], 'new'),
    ('anya', 'А, налей-ка мне чашечку.',
     'Oh, pour me a cup, would you?',
     [(268, 'мне чашечку')], 'adapted'),
    ('igor', 'А, он закончился.',
     'Oh, it is gone.',
     [(269, 'он закончился')], 'adapted'),
    ('igor', 'Я сейчас скажу, вам принесут.',
     'I will ask them to bring some.',
     [(270, 'сейчас скажу, вам принесут')], 'adapted'),
    ('anya', 'Шеф, еще чаек.',
     'Boss, more tea.',
     [(271, 'Шеф, еще чаек')], 'adapted'),
    ('igor', 'Поражаюсь вам, Виктор Петрович.',
     'I have to hand it to you, Viktor Petrovich.',
     [(272, 'Поражаюсь вам')], 'adapted'),
    ('igor', 'Как у вас все схвачено.',
     'You have got everything under control.',
     [(273, 'все схвачено')], 'adapted'),
    ('igor', 'Стоило только подумать, вот пожалуйста.',
     'You only had to think of it, and there it was.',
     [(274, 'Стоило только подумать')], 'adapted'),
    ('anya', 'Ой, остыл совсем, я свежий заварю.',
     'Oh, it has gone cold. I will brew a fresh pot.',
     [(275, 'остыл совсем')], 'adapted'),
    ('igor', 'Ничего страшного.',
     'That is all right.',
     [(276, 'Ничего страшного')], 'adapted'),
    ('igor', 'Я не люблю горячего.',
     'I do not like it hot.',
     [(277, 'не люблю горячего')], 'adapted'),
    ('anya', 'Как хотите, Игорь Валентинович.',
     'As you wish, Igor Valentinovich.',
     [], 'new'),
    ('anya', 'А я люблю горячий чай.',
     'And I like hot tea.',
     [], 'new'),
]

OPENER = "Let us break down this interaction."

WALK = [
    (1, None,
     "'Oh, pour me a cup, would you?' Russian leaves out 'am', 'is', or 'are' in the present tense, linking 'pour' straight to 'small cup'."),
    (2, None,
     "'Oh, it is gone.' The key word here means 'he', which the speaker combines with 'ended'."),
    (3, None,
     "'I will ask them to bring some.' Here 'I' sets up the idea, while 'will bring' comes at the end for emphasis."),
    (4, None,
     "'Boss, more tea.' You'll hear 'chef' all the time in the show, here connected with 'tea'."),
    (5, None,
     "'I have to hand it to you, Viktor Petrovich.' Here 'be amazed' sets up the idea, while 'Petrovich' comes at the end for emphasis."),
    (6, None,
     "'You have got everything under control.' the speaker starts with 'how' and pairs it with 'you' to make the point clear."),
    (7, None,
     "'You only had to think of it, and there it was.' Notice the word order: 'to cost' comes first, and 'to think' finishes the sentence. Chef Viktor answers straight away."),
    (8, None,
     "'Oh, it has gone cold. I will brew a fresh pot.' In Russian, 'oh' leads into 'brew' in a very natural everyday phrasing."),
    (9, None,
     "'That is all right.' The first content word means 'nothing', and 'terrible' rounds out the thought."),
    (10, None,
     "'I do not like it hot.' A compact expression built around 'I' and 'hot'."),
]

TRANSITION = "Now let us listen to the conversation again without interruption."
OUTRO = 'Chef Barinov successfully annoys the boss by pretending to be helpless.'
CLOSING = ('anya', 'А я люблю горячий чай.')
