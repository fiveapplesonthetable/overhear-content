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
    (0, None, '\'Hello, has Goncharova given birth yet?\' Max queries bluntly without a pause, leaning on "zdravstvuyte" ("hello") before closing the thought with "uzhe" ("already, now").'),
    (1, None, '\'Not yet, wait here.\' The doctor shows an easygoing posture as they talk, linking "yeshchyo" ("more, still"), "zhdite" ("to wait, to expect"), and "zdes" ("here") in one brisk exchange.'),
    (2, None, '\'Why is she not picking up the phone?\' Max wonders dryly to the doctor here, weaving "trubku" ("the receiver") together with "beryot" ("takes") just the way native speakers do.'),
    (3, None, '\'Sir, how do you imagine childbirth?\' The doctor asks earnestly during the talk, combining "muzhchina" ("man") and "kak" ("how") so the key meaning lands right away.'),
    (4, None, '\'Yes, hi, is everything alright?\' Max queries evenly toward the doctor here, linking "normalno" ("fine, OK"), "da" ("yes"), and "privet" ("hi") in one brisk exchange.'),
    (5, None, '\'I am already at the maternity hospital.\' Max shows a lively posture right away, combining "uzhe" ("already, now") and "roddome" ("maternity hospital") so the key meaning lands right away.'),
    (6, None, '\'Hold on the line for a second.\' Max sustains a lively line without hesitation, using "povisi" (from "poviset", "hold on") alongside "sekundochku" ("one little second") to shape the meaning.'),
    (7, None, '\'Tell me, how can I get through?\' Max presses evenly without hesitation, using "skazhite" (from "skazat", "tell") alongside "kak" ("how") to shape the meaning.'),
    (8, None, '\'And who are you anyway?\' The doctor checks briskly without hesitation, leaning on "voobshche" ("at all") before closing the thought with "vy" ("you").'),
    (9, None, '\'I am her lawful husband.\' Max picks a playful bearing in the scene, leaning on "zakonnyy" ("legitimate") before closing the thought with "muzh" ("husband").'),
    (10, None, '\'Under the contract we let close relatives in.\' The doctor keeps a brisk course toward Max, building the phrase around "kontraktu" ("by contract") and "rodstvennikov" ("relatives") for a crisp, natural delivery.'),
    (11, None, '\'Open the door for me, please.\' Max offers a wry line on the spot, building the phrase around "otkroyte" ("open") and "dver" ("door") for a crisp, natural delivery.'),
]
