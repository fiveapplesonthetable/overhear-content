ID = "kukhnya-s04e17-scene-03"
SHOW = "kukhnya"
SEASON = 4
EPISODE = 17
SCENE = 3
TITLE = "Подруга детства  (Childhood Friend)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "guest": "angelina"}
LABELS = {"anya": "Катя", "guest": "Гость"}
SOURCE_NAME = "Кухня (Kukhnya) S4.17"
SOURCE_FILE = "sources/kukhnya/s04/e17.ru.srt"
SOURCE_NOTE = "In the dining room, molecular-cuisine specialist Katya runs into her competitive childhood friend Lilya and impulsively claims she is getting married in a month."

INTRO = "While walking through the dining room, Chef Barinov's daughter Katya spots her childhood friend Lilya. The two women have competed fiercely since kindergarten, so when Lilya introduces her wealthy husband, Katya invents a fiancé on the spot. Let's listen to their rivalry in Russian."

STORY = [
    ("guest", "Привет, это моя подруга Катя.", "Hello, this is my friend Katya.", [(22, 'Привет'), (23, 'Это Катя, моя подруга детства')], "adapted"),
    ("guest", "Мы вместе в садик ходили.", "We went to kindergarten together.", [(24, 'Мы с ней еще в садик вместе ходили')], "adapted"),
    ("anya", "Мы всегда спорили с детства.", "We always argued since childhood.", [], "new"),
    ("guest", "Меня тогда в университет взяли.", "They accepted me into the university back then.", [(32, 'а меня в МГУ взяли')], "adapted"),
    ("anya", "А я во Францию поехала.", "And I went to France.", [(33, 'А я во Францию еду учиться')], "adapted"),
    ("guest", "Катя, это мой муж Эрнест.", "Katya, this is my husband Ernest.", [(34, 'Кать, а это Эрнест, мой муж')], "adapted"),
    ("anya", "Здравствуйте, мне очень приятно познакомиться.", "Hello, it is very nice to meet you.", [(35, 'Очень приятно')], "adapted"),
    ("guest", "Ну, а ты замуж вышла?", "Well, and did you get married?", [(36, 'Ну, а ты замуж вышла')], ""),
    ("anya", "Нет, но скоро обязательно выйду.", "No, but I will definitely get married soon.", [(36, 'Да нет'), (37, 'Но скоро выйду')], "adapted"),
    ("anya", "Через месяц у нас свадьба.", "Our wedding is in a month.", [(37, 'Через месяц свадьба')], "adapted"),
    ("guest", "Тогда завтра вечером поужинаем вместе!", "Then let's have dinner together tomorrow evening!", [(38, 'тогда завтра поужинаем вместе')], "adapted"),
    ("anya", "Не знаю, он очень занят.", "I do not know, he is very busy.", [(40, 'Ну, не знаю, он так занят')], "adapted"),
    ("guest", "Отлично, во сколько завтра встречаемся?", "Great, what time are we meeting tomorrow?", [(42, 'Во сколько встречаемся')], "adapted"),
]

OPENER = "Let's examine Katya and Lilya's competitive reunion line by line."

WALK = [
    (0, None, "'Hello, this is my friend Katya.' Lilya greets Katya casually and introduces her using a demonstrative pronoun and a feminine noun for a female friend."),
    (1, None, "'We went to kindergarten together.' A multidirectional past-tense verb of motion expresses repeated round-trip attendance in childhood."),
    (2, None, "'We always argued since childhood.' Katya recalls their lifelong rivalry with a frequency adverb and a plural imperfective past verb."),
    (3, None, "'They accepted me into the university back then.' An impersonal third-person plural past verb with an accusative pronoun means being admitted to school."),
    (4, None, "'And I went to France.' Katya counters using a contrastive conjunction and an accusative destination phrase for France."),
    (5, None, "'Katya, this is my husband Ernest.' Lilya proudly presents her spouse with a masculine possessive determiner."),
    (6, None, "'Hello, it is very nice to meet you.' The standard polite greeting phrase pairs naturally with a reflexive perfective infinitive."),
    (7, None, "'Well, and did you get married?' For a woman, Russian uses a specific verbal idiom literally meaning to step out behind a husband."),
    (8, None, "'No, but I will definitely get married soon.' Katya uses the first-person singular perfective future verb with a temporal adverb meaning soon."),
    (9, None, "'Our wedding is in a month.' A temporal preposition plus an accusative noun marks how soon the wedding will happen."),
    (10, None, "'Then let's have dinner together tomorrow evening!' The first-person plural perfective future verb functions as an enthusiastic dinner invitation."),
    (11, None, "'I do not know, he is very busy.' Katya tries to stall with a masculine singular short-form predicate adjective meaning busy."),
    (12, None, "'Great, what time are we meeting tomorrow?' An interrogative time phrase asks for the exact hour of their scheduled meeting."),
]

TRANSITION = "Let's listen to their dining room conversation again without interruption."
OUTRO = "Katya's pride traps her into promising to bring her non-existent fiancé to dinner the very next evening. Listen for the feminine phrase for getting married in Russian. See you in the next scene."
CLOSING = ("anya", "Через месяц у нас свадьба.")
CLOSING_TRANS = "Our wedding is in a month."
