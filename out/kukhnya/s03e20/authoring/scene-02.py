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
    (0, None, '\'Max, how are you feeling, my friend?\' Answering warmly in the exchange, Kostya puts the question word "kak" right at the start so Max hears the focus immediately.'),
    (1, None, "'Hello, tell me, do we know each other?' Max checks wryly before Kostya can change the subject."),
    (2, None, '\'Very funny! Wait, I do not get it right now.\' Kostya answers firmly at once and lands on "podozhdi" ("wait", built on "podozhdat") to keep the statement grounded.'),
    (3, None, '\'Well, how is our patient feeling today?\' Addressing the health during the talk, the doctor links the Russian words directly in the present with no word for "am", "is", or "are" needed.'),
    (4, None, "'Doctor, it seems there is something wrong with his memory.' Kostya jumps in calmly facing the doctor, grounding the moment in plain reality."),
    (5, None, '\'The blow was strong, it could have caused amnesia.\' Discussing the amnesia to Kostya, the doctor puts the weight on "amneziyu" ("amnesia", from "amneziya") as the exchange unfolds.'),
    (6, None, "'Look right here, do you see the dark spot?' Touching on the dark spot at once, the doctor keeps normal statement word order here, turning the line into a question for Kostya purely through rising pitch."),
    (7, None, "'That is a hematoma, it became the cause of memory loss.' The doctor speaks lightly with a smile, to clear the air between them once and for all."),
    (8, None, '\'He remembers everything that happened two years ago.\' Kostya follows up warmly in the exchange and chooses "proiskhodilo" ("was happening", from the root "proiskhodit") so the doctor hears the exact meaning.'),
    (9, None, '\'First very old memories return to a person.\' Turning to the memory in front of Kostya, the "-sya" ending on "vozvrashchayutsya" ("return") marks an action that unfolds mutually or turns back on the speaker.'),
    (10, None, "'If you did not save in time, you start the game over!' Kostya pushes back honestly around the doctor, so the doctor knows he is not just making small talk."),
    (11, None, '\'Come back tomorrow morning, right now the patient needs rest.\' Underscoring the peace on the spot, the doctor centers the thought on "bolnomu" ("to the patient", from "bolnoy") without wasting a word.'),
]
