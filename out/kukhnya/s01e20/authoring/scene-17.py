ID = "kukhnya-s01e20-scene-17"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 20
SCENE = 17
TITLE = 'Уход с праздника  (Leaving the Party)'
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "vika": "anja"}
LABELS = {"anya": "Костя", "vika": "Настя"}
SOURCE_NAME = "Кухня (Kukhnya) S1.20"
SOURCE_FILE = "sources/kukhnya/s01/e20.ru.dual.srt"
SOURCE_NOTE = "Scene 17"

INTRO = 'Nastya decides to leave the restaurant party early because she is feeling bored. Kostya rushes after her to stop her from leaving, as he has something very important to tell her.'

STORY = [
    ('anya', 'Настя, подожди!',
     'Nastya, wait!',
     [], 'new'),
    ('vika', 'Пока.',
     'Bye.',
     [(288, 'Пока')], 'adapted'),
    ('anya', 'О, уже уходишь?',
     'Oh, you are leaving already?',
     [(289, 'О, уже уходишь')], 'adapted'),
    ('vika', 'Ага. Как-то здесь невесело.',
     'Yeah. It is kind of a downer here.',
     [(290, 'Ага. Как-то здесь невесело')], 'adapted'),
    ('anya', 'Не уходи так быстро.',
     'Do not leave so fast.',
     [], 'new'),
    ('vika', 'У меня много дел.',
     'I have a lot of things to do.',
     [], 'new'),
    ('anya', 'Я хочу поговорить с тобой.',
     'I want to talk to you.',
     [], 'new'),
    ('vika', 'О чем ты хочешь поговорить?',
     'What do you want to talk about?',
     [], 'new'),
    ('anya', 'Это очень важно.',
     'This is very important.',
     [], 'new'),
    ('vika', 'Говори быстрее.',
     'Speak faster.',
     [], 'new'),
    ('anya', 'Подойди поближе.',
     'Come closer.',
     [], 'new'),
    ('vika', 'Я слушаю.',
     'I am listening.',
     [], 'new'),
    ('anya', 'Я',
     'I',
     [(291, 'Я')], 'adapted'),
    ('anya', 'Пожалуйста, выслушай меня.',
     'Please, hear me out.',
     [], 'new'),
]

OPENER = "Let us break down this interaction."

WALK = [
    (1, None,
     "'Bye.' A compact expression built around 'bye' and 'bye'."),
    (2, None,
     "'Oh, you are leaving already?' Notice the word order: 'already' comes first, and 'are leaving' finishes the sentence."),
    (3, None,
     "'Yeah. It is kind of a downer here.' Here 'yeah' sets up the idea, while 'sadly' comes at the end for emphasis. Then Kostya replies."),
    (13, None,
     "'Please, hear me out.' Kostya puts 'hear out' up front so the listener immediately catches the tone, followed by 'me'."),
]

TRANSITION = "Now let us listen to the conversation again without interruption."
OUTRO = 'Kostya successfully stops Nastya, preparing himself for a major life decision.'
CLOSING = ('anya', 'Я хочу поговорить с тобой.')
