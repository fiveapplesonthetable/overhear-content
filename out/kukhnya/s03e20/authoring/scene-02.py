# Authoring module for kukhnya-s03e20-scene-02.
ID = 'kukhnya-s03e20-scene-02'
SHOW = 'kukhnya'
SEASON = 3
EPISODE = 20
SCENE = 2
TITLE = 'Диагноз: травматическая амнезия  (Diagnosis: Traumatic Amnesia)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'doctor': 'Врач', 'kostya': 'Костя', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S3.20'
SOURCE_FILE = 'sources/kukhnya/s03/e20.ru.srt'
INTRO = "When Kostya rushes into the hospital room, Max pretends not to know him either. The doctor shows Vika and Kostya a brain scan with a dark spot and explains that Max's recent memories might never return."
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "Completely convinced by the doctor's brain scan, Vika and Kostya leave Max to rest in his hospital room. See you next time!"
CLOSING = ('doctor', 'Увидимся!')
STORY = [
    ('kostya', 'Макс, ну как ты себя чувствуешь, друг?', 'Max, how are you feeling, my friend?', [(23, 'как ты')], 'adapted'),
    ('max', 'Здравствуйте, скажите, а мы с вами знакомы?', 'Hello, tell me, do we know each other?', [(25, 'Знакомый')], 'adapted'),
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
WALK = [
    (0, None, '\'Max, how are you feeling, my friend?\' By wondering how the doctor feeling is, Kostya presses the doctor for a straight answer. Using the informal "you" shows how direct and unfiltered their kitchen relationship is.'),
    (1, None, '\'Hello, tell me, do we know each other?\' Wondering if tell him do they know each other shows Max caught off guard. Notice how he sticks to the formal "you", keeping a professional line between them.'),
    (2, None, "'Very funny! Wait, I do not get it right now.' By waiting he does not get it right now, Kostya raises the stakes in the room at once."),
    (3, None, '\'Well, how is our patient feeling today?\' Here wondering how their patient feeling today is shows the doctor looking for the real truth. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (4, None, '\'Doctor, it seems there is something wrong with his memory.\' Realizing that doctor it seems there is something wrong with his memory changes how Kostya handles the situation. In Russian you say "by me" or "with us" rather than "I have", so the situation sits right with the person.'),
    (5, None, "'The blow was strong, it could have caused amnesia.' Noting that the blow was strong it could have caused amnesia keeps the doctor's side of the story simple and clear."),
    (6, None, '\'Look right here, do you see the dark spot?\' Wondering if right here do Kostya sees the dark spot shows the doctor caught off guard. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (7, None, '\'That is a hematoma, it became the cause of memory loss.\' Admitting that that is a hematoma it became the cause of memory loss shows the doctor being honest for a change. Russian drops "is" in the present, setting the two halves of the thought side by side.'),
    (8, None, "'He remembers everything that happened two years ago.' Saying that he remembers everything that happened two years ago is how Kostya sets the tone with the doctor."),
    (9, None, "'First very old memories return to a person.' Over the hospital and the conversation, the doctor answers Kostya without a second thought."),
    (10, None, "'If you did not save in time, you start the game over!' Because if the doctor did not save in time the doctor starts the game, Kostya does not bother softening the blow for the doctor. Russian puts the key word right up front so his emotion lands on the first beat."),
    (11, None, "'Come back tomorrow morning, right now the patient needs rest.' By telling Kostya to come back tomorrow morning right now the patient needs rest, the doctor keeps his side of the story grounded."),
]
