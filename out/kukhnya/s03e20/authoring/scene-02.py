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
    (0, None, '\'Max, how are you feeling, my friend?\' Kostya shapes the comeback with ease: putting the question word "kak" right at the front of the line lets the doctor hear the point of the question on the very first beat.'),
    (1, None, "'Hello, tell me, do we know each other?' Max checks wryly about what Kostya just brought up."),
    (2, None, '\'Very funny! Wait, I do not get it right now.\' Kostya spotlights one loaded term on cue: "podozhdi" means "wait" (from "podozhdat"), giving the line its exact edge.'),
    (3, None, '\'Well, how is our patient feeling today?\' The doctor shares this answer on cue: notice how Russian needs no word for "am", "is", or "are" in the present — placing the words side by side says it all.'),
    (4, None, "'Doctor, it seems there is something wrong with his memory.' Kostya stands firm calmly as they talk, making his position completely clear."),
    (5, None, '\'The blow was strong, it could have caused amnesia.\' The doctor leans on this clear term for Max: "amneziyu" means "amnesia" (from "amneziya"), giving the line its exact edge.'),
    (6, None, "'Look right here, do you see the dark spot?' The doctor offers the reaction to Kostya: Russian keeps the exact word order of a normal statement here, turning it into a question for Kostya purely through rising pitch at the end."),
    (7, None, "'That is a hematoma, it became the cause of memory loss.' The doctor counters lightly with Max, shifting the whole mood of the room in a single beat."),
    (8, None, '\'He remembers everything that happened two years ago.\' Kostya centers one pointed choice toward the doctor: "proiskhodilo" means "was happening" (from "proiskhodit"), giving the line its exact edge.'),
    (9, None, '\'First very old memories return to a person.\' The doctor puts the reply beside Max: the "-sya" ending on "vozvrashchayutsya" ("return") turns the action inward or makes it happen between people naturally.'),
    (10, None, "'If you did not save in time, you start the game over!' Kostya holds firm honestly with a smile, letting the remark speak for itself."),
    (11, None, '\'Come back tomorrow morning, right now the patient needs rest.\' The doctor features one vivid touch right here: "bolnomu" means "to the patient" (from "bolnoy"), giving the line its exact edge.'),
]
