ID = 'kukhnya-s03e20-scene-02'
SHOW = "kukhnya"
SEASON = 3
EPISODE = 20
SCENE = 2
TITLE = 'Диагноз: травматическая амнезия  (Diagnosis: Traumatic Amnesia)'
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {'narrator': 'sky', 'anya': 'alisa', 'kostya': 'anja', 'doctor': 'angelina'}
LABELS = {'anya': 'Макс', 'kostya': 'Костя', 'doctor': 'Врач'}
SOURCE_NAME = "Кухня (Kukhnya) S3.20"
SOURCE_FILE = 'sources/kukhnya/s03/e20.ru.srt'

INTRO = "When Kostya rushes into the hospital room, Max pretends not to know him either. The doctor shows Vika and Kostya a brain scan with a dark spot and explains that Max's recent memories might never return."

STORY = [
    ('kostya', 'Макс, ну как ты себя чувствуешь, друг?', 'Max, how are you feeling, my friend?', [(23, 'как ты')], 'adapted'),
    ('anya', 'Здравствуйте, скажите, а мы с вами знакомы?', 'Hello, tell me, do we know each other?', [(25, 'Знакомый')], 'adapted'),
    ('kostya', 'Очень смешно! Подожди, я сейчас не понял.', 'Very funny! Wait, I do not get it right now.', [(26, 'Очень смешно'), (27, 'Не понял')], 'adapted'),
    ('doctor', 'Ну, как сегодня самочувствие нашего больного?', 'Well, how is our patient feeling today?', [(28, 'как самочувствие нашего больного')], 'adapted'),
    ('kostya', 'Доктор, кажется, у него что-то с памятью.', 'Doctor, it seems there is something wrong with his memory.', [(29, 'Доктор, кажется, у него что-то с памятью')], 'adapted'),
    ('doctor', 'Удар был сильным, это могло вызвать амнезию.', 'The blow was strong, it could have caused amnesia.', [(31, 'Удар был сильным. Это могло вызвать'), (31, 'амнезию')], 'adapted'),
    ('doctor', 'Вот посмотрите сюда, видите тёмное пятно?', 'Look right here, do you see the dark spot?', [(32, 'Вот посмотрите сюда'), (33, 'Видите темное пятно')], 'adapted'),
    ('doctor', 'Это гематома, она и стала причиной потери памяти.', 'That is a hematoma, it became the cause of memory loss.', [(34, 'Это гематома'), (35, 'быть причиной потери памяти')], 'adapted'),
    ('kostya', 'Он помнит всё, что происходило два года назад.', 'He remembers everything that happened two years ago.', [(37, 'Он помнит все, что происходило'), (37, 'два года назад')], 'adapted'),
    ('doctor', 'Сначала к человеку возвращаются очень старые воспоминания.', 'First very old memories return to a person.', [(38, 'воспоминания возвращаются'), (39, 'Сначала очень старые воспоминания')], 'adapted'),
    ('kostya', 'Если вовремя не сохранился, начинаешь игру заново!', 'If you did not save in time, you start the game over!', [(43, 'если не сохранился, начинаешь заново')], 'adapted'),
    ('doctor', 'Придёте завтра утром, сейчас больному нужен покой.', 'Come back tomorrow morning, right now the patient needs rest.', [(46, 'Придете завтра, больному нужен покой')], 'adapted'),
]

OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."

WALK = [
    (0, None, "'Max, how are you feeling, my friend?' Notice how Russian expresses 'Max' and 'friend' with crisp inflection rather than helper words."),
    (1, None, "'Hello, tell me, do we know each other?' Here the Russian phrasing highlights 'hello' before landing on 'acquainted'. Kostya answers right away."),
    (2, None, "'Very funny! Wait, I do not get it right now.' Notice how Russian expresses 'very' and 'understood' with crisp inflection rather than helper words."),
    (3, None, "'Well, how is our patient feeling today?' The meaning hinges on 'come on' working together with 'of the patient' in spoken Russian."),
    (4, None, "'Doctor, it seems there is something wrong with his memory.' Notice how Russian expresses 'Doctor' and 'with memory' with crisp inflection rather than helper words. the doctor answers right away."),
    (5, None, "'The blow was strong, it could have caused amnesia.' the doctor brings out the contrast between 'blow' and 'was' in a few short words."),
    (6, None, "'Look right here, do you see the dark spot?' In Russian, the idea of 'here' flows naturally into 'spot' without extra filler words."),
    (7, None, "'That is a hematoma, it became the cause of memory loss.' Spoken Russian keeps this brisk, leaning on 'this' and finishing on 'of memory'. Kostya answers right away."),
    (8, None, "'He remembers everything that happened two years ago.' Notice how Russian expresses 'he' and 'back' with crisp inflection rather than helper words."),
    (9, None, "'First very old memories return to a person.' The grammar packs 'at first' and 'memories' into a tight, idiomatic kitchen exchange."),
    (10, None, "'If you did not save in time, you start the game over!' The '-l' ending on the verb meaning 'saved' places the action in the masculine past tense. the doctor answers right away."),
    (11, None, "'Come back tomorrow morning, right now the patient needs rest.' the doctor anchors the line on 'to come', while 'peace' completes the thought."),
]

TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "Completely convinced by the doctor's brain scan, Vika and Kostya leave Max to rest in his hospital room."
CLOSING = ('doctor', 'Сейчас больному очень нужен покой.')
