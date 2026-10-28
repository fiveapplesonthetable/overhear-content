# Authoring module for kukhnya-s05e17-scene-01.
ID = 'kukhnya-s05e17-scene-01'
SHOW = 'kukhnya'
SEASON = 5
EPISODE = 17
SCENE = 1
TITLE = 'В приёмном отделении роддома  (At the Maternity Hospital Reception)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'doctor': 'Врач', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S5.17'
SOURCE_FILE = 'sources/kukhnya/s05/e17.ru.srt'
INTRO = 'Max rushes into the maternity hospital reception desk searching for Vika. While the nurse explains the strict visiting rules, Max tries to reach his wife on the phone.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "Max slips through the reception doors in a hurry to find Vika's ward. Until next time!"
CLOSING = ('doctor', 'До встречи!')
STORY = [
    ('max', 'Здравствуйте, Гончарова уже родила?', 'Hello, has Goncharova given birth yet?', [(1, 'Гончарова родила')], 'adapted'),
    ('doctor', 'Ещё нет, ждите здесь.', 'Not yet, wait here.', [(2, 'Ещё нет')], 'adapted'),
    ('max', 'Чего она трубку не берёт?', 'Why is she not picking up the phone?', [(2, 'Чего он трубку не берёт')], 'adapted'),
    ('doctor', 'Мужчина, как вы себе роды представляете?', 'Sir, how do you imagine childbirth?', [(3, 'Мужчина, а вы вообще как себе')], 'adapted'),
    ('max', 'Да, привет, всё нормально?', 'Yes, hi, is everything alright?', [(4, 'Да, привет'), (5, 'всё нормально')], 'adapted'),
    ('max', 'Я уже в роддоме.', 'I am already at the maternity hospital.', [(5, 'я в роддоме')], 'adapted'),
    ('max', 'Повиси секундочку на линии.', 'Hold on the line for a second.', [(6, 'повиси секундочку')], 'adapted'),
    ('max', 'Скажите, а как мне пройти?', 'Tell me, how can I get through?', [(9, 'а как мне пройти')], 'adapted'),
    ('doctor', 'А вы вообще кто?', 'And who are you anyway?', [(10, 'А вы кто')], 'adapted'),
    ('max', 'Я её законный муж.', 'I am her lawful husband.', [(10, 'Я муж')], 'adapted'),
    ('doctor', 'По контракту мы родственников пускаем.', 'Under the contract we let close relatives in.', [(11, 'По контракту мы только ближайших родственников пускаем')], 'adapted'),
    ('max', 'Откройте мне дверь, пожалуйста.', 'Open the door for me, please.', [(13, 'Сейчас я открою')], 'adapted'),
]
WALK = [
    (0, None, "'Hello, has Goncharova given birth yet?' By asking whether Goncharova given birth yet, Max presses the doctor for a straight answer."),
    (1, None, "'Not yet, wait here.' Around the hospital and conversation, the doctor sets a calm, everyday tone with Max."),
    (2, None, '\'Why is she not picking up the phone?\' Asking why she not picking up the phone is is how Max puts the doctor on the spot. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (3, None, "'Sir, how do you imagine childbirth?' When the doctor asks if sir how do Max imagines childbirth, Max has to answer fast."),
    (4, None, '\'Yes, hi, is everything alright?\' By checking whether everything alright, Max presses the doctor for a straight answer. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (5, None, "'I am already at the maternity hospital.' Max tells the doctor that he is already at the maternity hospital without dressing it up."),
    (6, None, "'Hold on the line for a second.' Holding on the line for a second moves the conversation forward without extra drama."),
    (7, None, '\'Tell me, how can I get through?\' Questioning whether tell him how can he gets is how Max tests the doctor\'s story. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (8, None, '\'And who are you anyway?\' By asking who Max anyway is, the doctor presses Max for a straight answer. Notice how he sticks to the formal "you", keeping a professional line between them.'),
    (9, None, "'I am her lawful husband.' Being her lawful husband moves the conversation forward without extra drama."),
    (10, None, "'Under the contract we let close relatives in.' Because under the contract they let close relatives, the doctor treats the matter as settled."),
    (11, None, "'Open the door for me, please.' By telling the doctor to open the door for him please, Max keeps his side of the story grounded."),
]
