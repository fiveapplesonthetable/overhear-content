ID = 'kukhnya-s05e17-scene-01'
SHOW = "kukhnya"
SEASON = 5
EPISODE = 17
SCENE = 1
TITLE = 'В приёмном отделении роддома  (At the Maternity Hospital Reception)'
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {'narrator': 'sky', 'anya': 'alisa', 'doctor': 'anja'}
LABELS = {'anya': 'Макс', 'doctor': 'Врач'}
SOURCE_NAME = "Кухня (Kukhnya) S5.17"
SOURCE_FILE = 'sources/kukhnya/s05/e17.ru.srt'

INTRO = 'Max rushes into the maternity hospital reception desk searching for Vika. While the nurse explains the strict visiting rules, Max tries to reach his wife on the phone.'

STORY = [
    ('anya', 'Здравствуйте, Гончарова уже родила?', 'Hello, has Goncharova given birth yet?', [(1, 'Гончарова родила')], 'adapted'),
    ('doctor', 'Ещё нет, ждите здесь.', 'Not yet, wait here.', [(2, 'Ещё нет')], 'adapted'),
    ('anya', 'Чего она трубку не берёт?', 'Why is she not picking up the phone?', [(2, 'Чего он трубку не берёт')], 'adapted'),
    ('doctor', 'Мужчина, как вы себе роды представляете?', 'Sir, how do you imagine childbirth?', [(3, 'Мужчина, а вы вообще как себе')], 'adapted'),
    ('anya', 'Да, привет, всё нормально?', 'Yes, hi, is everything alright?', [(4, 'Да, привет'), (5, 'всё нормально')], 'adapted'),
    ('anya', 'Я уже в роддоме.', 'I am already at the maternity hospital.', [(5, 'я в роддоме')], 'adapted'),
    ('anya', 'Повиси секундочку на линии.', 'Hold on the line for a second.', [(6, 'повиси секундочку')], 'adapted'),
    ('anya', 'Скажите, а как мне пройти?', 'Tell me, how can I get through?', [(9, 'а как мне пройти')], 'adapted'),
    ('doctor', 'А вы вообще кто?', 'And who are you anyway?', [(10, 'А вы кто')], 'adapted'),
    ('anya', 'Я её законный муж.', 'I am her lawful husband.', [(10, 'Я муж')], 'adapted'),
    ('doctor', 'По контракту мы родственников пускаем.', 'Under the contract we let close relatives in.', [(11, 'По контракту мы только ближайших родственников пускаем')], 'adapted'),
    ('anya', 'Откройте мне дверь, пожалуйста.', 'Open the door for me, please.', [(13, 'Сейчас я открою')], 'adapted'),
]

OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."

WALK = [
    (0, None, "'Hello, has Goncharova given birth yet?' Spoken Russian keeps this brisk, leaning on 'hello' and finishing on 'gave birth'."),
    (1, None, "'Not yet, wait here.' The grammar packs 'else' and 'here' into a tight, idiomatic kitchen exchange."),
    (2, None, "'Why is she not picking up the phone?' Spoken Russian keeps this brisk, leaning on 'what' and finishing on 'takes'. the doctor answers right away."),
    (3, None, "'Sir, how do you imagine childbirth?' In Russian, the idea of 'man' flows naturally into 'to imagine' without extra filler words."),
    (4, None, "'Yes, hi, is everything alright?' In Russian, the idea of 'yes' flows naturally into 'normally' without extra filler words."),
    (5, None, "'I am already at the maternity hospital.' Notice how Russian expresses 'I' and 'maternity hospital' with crisp inflection rather than helper words."),
    (6, None, "'Hold on the line for a second.' Here the Russian phrasing highlights 'hold on' before landing on 'line'."),
    (7, None, "'Tell me, how can I get through?' The grammar packs 'say' and 'take place' into a tight, idiomatic kitchen exchange."),
    (8, None, "'And who are you anyway?' Spoken Russian keeps this brisk, leaning on 'and' and finishing on 'who'. Max answers right away."),
    (9, None, "'I am her lawful husband.' The grammar packs 'I' and 'husband' into a tight, idiomatic kitchen exchange."),
    (10, None, "'Under the contract we let close relatives in.' The meaning hinges on 'according to' working together with 'to let in' in spoken Russian."),
    (11, None, "'Open the door for me, please.' In Russian, the idea of 'open' flows naturally into 'please' without extra filler words."),
]

TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "Max slips through the reception doors in a hurry to find Vika's ward. See you in the next scene."
CLOSING = ('doctor', 'Сейчас я открою.')
