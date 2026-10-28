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
    (0, None, '\'Hello, has Goncharova given birth yet?\' Max emphasizes this clear term with the doctor: "zdravstvuyte" means "hello", and it carries the main weight of what Max is saying.'),
    (1, None, "'Not yet, wait here.' The doctor hands over that reply toward Max: spoken Russian trims this down to just 4 words, dropping the extra helper words that English has to spell out."),
    (2, None, "'Why is she not picking up the phone?' Max challenges sharply as the doctor tries to explain the situation."),
    (3, None, '\'Sir, how do you imagine childbirth?\' The doctor chooses one key touch right here: "predstavlyayete" means "to imagine" (from "predstavlyat"), giving the line its exact edge.'),
    (4, None, '\'Yes, hi, is everything alright?\' Max sends that answer at once: opening with the casual greeting "privet" ("hi") signals right away that Max and the doctor are on familiar terms.'),
    (5, None, "'I am already at the maternity hospital.' Max steps in lightly on the spot, refusing to let the moment slip past."),
    (6, None, '\'Hold on the line for a second.\' Max grounds one loaded touch with the doctor: "sekundochku" means "one little second" (from "sekundochka"), giving the line its exact edge.'),
    (7, None, '\'Tell me, how can I get through?\' Max shares this statement with warmth: putting the question word "kak" right at the front of the line lets the doctor hear the point of the question on the very first beat.'),
    (8, None, "'And who are you anyway?' The doctor questions plainly in front of Max without any preamble."),
    (9, None, '\'I am her lawful husband.\' Max emphasizes one clear touch in reply: "zakonnyy" means "legitimate", and it carries the main weight of what Max is saying.'),
    (10, None, "'Under the contract we let close relatives in.' The doctor counters right away without any doubt, to clear the air between them once and for all."),
    (11, None, "'Open the door for me, please.' Max weighs in boldly to be clear, refusing to let the moment slip past."),
]
