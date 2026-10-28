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
    (0, None, '\'Hello, has Goncharova given birth yet?\' Max naturally voices this formal greeting to the doctor using "zdravstvuyte" ("hello") — the polite Russian greeting that literally wishes the other person good health.'),
    (1, None, "'Not yet, wait here.' Holding firm directly around Max, spoken Russian compresses the whole thought into just 4 words, skipping the extra helper words English needs."),
    (2, None, "'Why is she not picking up the phone?' Max challenges sharply where this conversation is heading next."),
    (3, None, '\'Sir, how do you imagine childbirth?\' Talking about the man during the talk, the doctor chooses "predstavlyayete" ("to imagine", from the root "predstavlyat") so Max hears the exact meaning.'),
    (4, None, '\'Yes, hi, is everything alright?\' Max gently voices this casual greeting in the exchange using "privet" ("hi") — the everyday informal hello used between friends and close coworkers.'),
    (5, None, "'I am already at the maternity hospital.' Max speaks up lightly in their talk, watching the doctor's face to see how the news lands."),
    (6, None, '\'Hold on the line for a second.\' Talking about a second to the doctor, Max uses "sekundochku" ("one little second", from "sekundochka") to make the point stick.'),
    (7, None, '\'Tell me, how can I get through?\' Answering boldly during the talk, Max puts the question word "kak" right at the start so the doctor hears the focus immediately.'),
    (8, None, "'And who are you anyway?' The doctor questions plainly while looking straight at Max here."),
    (9, None, '\'I am her lawful husband.\' Insisting on how legitimate he is beside the doctor, Max puts the emphasis on "zakonnyy" ("legitimate") in the middle of the talk.'),
    (10, None, '\'Under the contract we let close relatives in.\' Highlighting the relatives right here, the doctor brings in "rodstvennikov" ("relatives", from "rodstvennik") as the key Russian word here.'),
    (11, None, '\'Open the door for me, please.\' Max casually directs this courtesy word without hesitation using "pozhaluysta" ("please") — the all-purpose Russian politeness word that covers both "please" and "you\'re welcome".'),
]
