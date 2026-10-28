# Authoring module for kukhnya-s04e17-scene-03.
ID = 'kukhnya-s04e17-scene-03'
SHOW = 'kukhnya'
SEASON = 4
EPISODE = 17
SCENE = 3
TITLE = 'Подруга детства  (Childhood Friend)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'guest': 'Гость', 'katya': 'Катя'}
SOURCE_NAME = 'Кухня (Kukhnya) S4.17'
SOURCE_FILE = 'sources/kukhnya/s04/e17.ru.srt'
INTRO = "While walking through the dining room, Chef Barinov's daughter Katya spots her childhood friend Lilya. The two women have competed fiercely since kindergarten, so when Lilya introduces her wealthy husband, Katya invents a fiancé on the spot. Let's listen to their rivalry in Russian."
OPENER = "Let's examine Katya and Lilya's competitive reunion line by line."
TRANSITION = "Let's listen to their dining room conversation again without interruption."
OUTRO = "Katya's pride traps her into promising to bring her non-existent fiancé to dinner the very next evening. Listen for the feminine phrase for getting married in Russian. Until next time!"
CLOSING = ('katya', 'До свидания!')
STORY = [
    ('guest', 'Привет, это моя подруга Катя.', 'Hello, this is my friend Katya.', [(22, 'Привет'), (23, 'Это Катя, моя подруга детства')], 'adapted'),
    ('guest', 'Мы вместе в садик ходили.', 'We went to kindergarten together.', [(24, 'Мы с ней еще в садик вместе ходили')], 'adapted'),
    ('katya', 'Мы всегда спорили с детства.', 'We always argued since childhood.', [], 'new'),
    ('guest', 'Меня тогда в университет взяли.', 'They accepted me into the university back then.', [(32, 'а меня в МГУ взяли')], 'adapted'),
    ('katya', 'А я во Францию поехала.', 'And I went to France.', [(33, 'А я во Францию еду учиться')], 'adapted'),
    ('guest', 'Катя, это мой муж Эрнест.', 'Katya, this is my husband Ernest.', [(34, 'Кать, а это Эрнест, мой муж')], 'adapted'),
    ('katya', 'Здравствуйте, мне очень приятно познакомиться.', 'Hello, it is very nice to meet you.', [(35, 'Очень приятно')], 'adapted'),
    ('guest', 'Ну, а ты замуж вышла?', 'Well, and did you get married?', [(36, 'Ну, а ты замуж вышла')], ''),
    ('katya', 'Нет, но скоро обязательно выйду.', 'No, but I will definitely get married soon.', [(36, 'Да нет'), (37, 'Но скоро выйду')], 'adapted'),
    ('katya', 'Через месяц у нас свадьба.', 'Our wedding is in a month.', [(37, 'Через месяц свадьба')], 'adapted'),
    ('guest', 'Тогда завтра вечером поужинаем вместе!', "Then let's have dinner together tomorrow evening!", [(38, 'тогда завтра поужинаем вместе')], 'adapted'),
    ('katya', 'Не знаю, он очень занят.', 'I do not know, he is very busy.', [(40, 'Ну, не знаю, он так занят')], 'adapted'),
    ('guest', 'Отлично, во сколько завтра встречаемся?', 'Great, what time are we meeting tomorrow?', [(42, 'Во сколько встречаемся')], 'adapted'),
]
WALK = [
    (0, None, '\'Hello, this is my friend Katya.\' The guest directly offers this casual greeting right on cue using "privet" ("hi") — the everyday informal hello used between friends and close coworkers.'),
    (1, None, '\'We went to kindergarten together.\' Touching on the daycare beside Katya, the guest brings in "sadik" ("daycare, kindergarten") to make the meaning unmistakable.'),
    (2, None, '\'We always argued since childhood.\' Discussing the childhood in this beat, Katya brings in "detstva" ("childhood", from "detstvo") as the key Russian word here.'),
    (3, None, "'They accepted me into the university back then.' The guest chimes in decisively with a nod, bringing things back to earth after the buildup."),
    (4, None, '\'And I went to France.\' Katya replies promptly at once and leans on "poyekhala" ("to go, to set off", a form of "poyekhat") to give the remark its edge.'),
    (5, None, '\'Katya, this is my husband Ernest.\' Returning to his husband in the exchange, the guest links the Russian words directly in the present with no word for "am", "is", or "are" needed.'),
    (6, None, '\'Hello, it is very nice to meet you.\' Katya gently voices this formal greeting with the guest using "zdravstvuyte" ("hello") — the polite Russian greeting that literally wishes the other person good health.'),
    (7, None, '\'Well, and did you get married?\' The guest cuts in decisively during the talk and leans on "zamuzh" ("in marriage") to give the whole sentence its punch.'),
    (8, None, '\'No, but I will definitely get married soon.\' Katya counters decisively on the spot and puts the emphasis on "obyazatelno" ("surely, without fail") in the middle of the talk.'),
    (9, None, "'Our wedding is in a month.' Katya opens up sharply watching the guest, so the guest knows she is not just making small talk."),
    (10, None, '\'Then let\'s have dinner together tomorrow evening!\' The guest replies briskly in this beat and leans on "pouzhinayem" ("to have dinner", a form of "pouzhinat") to give the remark its edge.'),
    (11, None, '\'I do not know, he is very busy.\' Describing how busy he is in this beat, Katya centers the thought on "zanyat" ("busy", from "zanyatyy") without wasting a word.'),
    (12, None, "'Great, what time are we meeting tomorrow?' The guest asks eagerly how Katya expects that to work in practice."),
]
