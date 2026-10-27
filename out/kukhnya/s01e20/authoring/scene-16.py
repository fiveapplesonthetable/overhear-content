ID = "kukhnya-s01e20-scene-16"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 20
SCENE = 16
TITLE = 'Старые часы  (Old Watch)'
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "fedya": "anja"}
LABELS = {"anya": "Макс", "fedya": "Старик"}
SOURCE_NAME = "Кухня (Kukhnya) S1.20"
SOURCE_FILE = "sources/kukhnya/s01/e20.ru.dual.srt"
SOURCE_NOTE = "Scene 16"

INTRO = "Max finds an old homeless man on the street. He decides to give away his grandfather's antique watch because he feels it is time to move on and let go of the past."

STORY = [
    ('anya', 'Привет, старик.',
     'Hello, old man.',
     [], 'new'),
    ('fedya', 'Здравствуй.',
     'Hello.',
     [], 'new'),
    ('anya', 'У меня есть часы.',
     'I have a watch.',
     [], 'new'),
    ('fedya', 'Зачем они мне?',
     'Why do I need them?',
     [], 'new'),
    ('anya', 'Они мне больше не нужны.',
     'I do not need them anymore.',
     [], 'new'),
    ('fedya', 'Они дорогие?',
     'Are they expensive?',
     [], 'new'),
    ('anya', 'Это старые дедовские часы.',
     "This is an old grandfather's watch.",
     [], 'new'),
    ('anya', 'На, держись, старик.',
     'Here, take it, old man.',
     [(286, 'На, держись, старик')], 'adapted'),
    ('fedya', 'Спасибо тебе большое.',
     'Thank you very much.',
     [], 'new'),
    ('anya', 'Тебе нужнее.',
     'You need it more than I do.',
     [(287, 'Тебе нужнее')], 'adapted'),
    ('fedya', 'Я продам их и куплю еды.',
     'I will sell it and buy food.',
     [], 'new'),
    ('anya', 'Делай с ними что хочешь.',
     'Do with them what you want.',
     [], 'new'),
    ('anya', 'Прощай.',
     'Goodbye.',
     [], 'new'),
    ('fedya', 'Ты очень добрый человек.',
     'You are a very kind person.',
     [], 'new'),
]

OPENER = "Let us break down this interaction."

WALK = [
    (4, None,
     "'I do not need them anymore.' -- ENG He explains that he is letting go of the item."),
    (7, None,
     "'Here, take it, old man.' -- ENG He officially hands over the family heirloom."),
    (9, None,
     "'You need it more than I do.' -- ENG He assures the poor man that the gift is well-deserved."),
    (13, None,
     "'You are a very kind person.' -- ENG The man sincerely expresses his deep gratitude."),
]

TRANSITION = "Now let us listen to the conversation again without interruption."
OUTRO = 'The old man gratefully accepts the unexpected gift, leaving Max feeling a sense of relief.'
CLOSING = ('anya', 'Тебе нужнее.')
