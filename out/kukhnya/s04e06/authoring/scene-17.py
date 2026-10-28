ID = "kukhnya-s04e06-scene-17"
SHOW = "kukhnya"
SEASON = 4
EPISODE = 6
SCENE = 17
TITLE = "Лучший сомелье Москвы  (Moscow's Best Sommelier)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "kostya": "anja", "nagiyev": "angelina"}
LABELS = {"anya": "Макс", "kostya": "Костя", "nagiyev": "Нагиев"}
SOURCE_NAME = "Кухня (Kukhnya) S4.06"
SOURCE_FILE = "sources/kukhnya/s04/e06.ru.srt"
SOURCE_NOTE = "Cues 247-259. When Nagiyev demands his bottle of wine, Max and Kostya stall him in the storeroom hoping Vika's courier will arrive, only to learn Nagiyev's guest is Moscow's top sommelier."

INTRO = "Dmitry Nagiyev approaches the bar demanding his bottle of wine for his VIP guest. Max and Kostya try to stall him in the storeroom with a story about a broken lock while waiting for Vika's courier—until Nagiyev reveals his guest is Moscow's finest sommelier!"

STORY = [
    ("nagiyev", "Костя, давай бутылку, важный гость уже пожаловал!", "Kostya, give me the bottle, the important guest has arrived!", [(247, "Бутылку давай, гость пожаловал.")], "adapted"),
    ("nagiyev", "Чего ты молчишь, давай скорее моё вино!", "Why are you silent, give me my wine quickly!", [(249, "Давай вино я тебе сказал.")], "adapted"),
    ("anya", "Костя, эту бутылку уже пора нести в зал?", "Kostya, is it time to carry this bottle to the hall already?", [(250, "Костян, бутылку нести уже?")], "adapted"),
    ("nagiyev", "Что здесь вообще происходит у вас, парни?", "What on earth is going on with you here, guys?", [(251, "Чё происходит, пацаны?")], "adapted"),
    ("anya", "Костя просил подержать вашу бутылку на складе.", "Kostya asked us to keep your bottle in the storeroom.", [(252, "Да Костян просто просил вашу бутылку у нас на складе подержать.")], "adapted"),
    ("anya", "У него в баре случайно сломался замок.", "A lock accidentally broke at his bar.", [(253, "У него сломался замок барный.")], "adapted"),
    ("nagiyev", "Давай неси её в зал очень быстро!", "Come on, carry it to the dining room very fast!", [(254, "Давай мухой. Давай-давай-давай.")], "adapted"),
    ("nagiyev", "Ты хоть понимаешь, кто сегодня сидит в зале?", "Do you even understand who is sitting in the hall today?", [(255, "Понимаешь, кто это?")], "adapted"),
    ("nagiyev", "Это же самый лучший сомелье всей Москвы!", "That is the very best sommelier in all of Moscow!", [(255, "Лучший сомелье Москвы.")], "adapted"),
    ("nagiyev", "Я хочу переманить его в наш ресторан.", "I want to lure him over to our restaurant.", [(256, "Хочу его переманить из метрополя.")], "adapted"),
    ("nagiyev", "Пускай попьёт сегодня нашего хорошего элитного вина!", "Let him drink some of our good elite wine today!", [(257, "Пускай хорошего вина попьёт.")], "adapted"),
    ("kostya", "Вика, курьер наконец привёз твоё новое вино?", "Vika, did the courier finally bring your new wine?", [(258, "Мне вино привезли.")], "adapted"),
    ("anya", "Слишком поздно, Костя уже открыл мою бутылку!", "Too late, Kostya has already opened my bottle!", [(259, "Поздно.")], "adapted"),
]

OPENER = "Let's break down Nagiyev's revelation in the storeroom line by line."

WALK = [
    (0, None, "'Kostya, give me the bottle, the important guest has arrived!' Expressive verb 'has graced us with his presence' highlights the VIP."),
    (1, None, "'Why are you silent, give me my wine quickly!' Nagiyev loses patience as Kostya hesitates behind the bar."),
    (2, None, "'Kostya, is it time to carry this bottle to the hall already?' Max runs in to buy a few extra minutes."),
    (3, None, "'What on earth is going on with you here, guys?' Nagiyev follows them to see why the wine is taking so long."),
    (4, None, "'Kostya asked us to keep your bottle in the storeroom.' Prepositional case marks location in the storage room."),
    (5, None, "'A lock accidentally broke at his bar.' Reflexive perfective past verb describes the lock breaking by itself."),
    (6, None, "'Come on, carry it to the dining room very fast!' Nagiyev waves them toward the dining room."),
    (7, None, "'Do you even understand who is sitting in the hall today?' Particle 'even/at least' intensifies the question."),
    (8, None, "'That is the very best sommelier in all of Moscow!' The borrowed French noun for sommelier is indeclinable in Russian."),
    (9, None, "'I want to lure him over to our restaurant.' Prefixed verb 'to lure across' means recruiting someone from a rival."),
    (10, None, "'Let him drink some of our good elite wine today!' Partitive genitive 'of good wine' follows the prefixed verb of drinking."),
    (11, None, "'Vika, did the courier finally bring your new wine?' Vika receives the real bottle at the entrance a moment too late."),
    (12, None, "'Too late, Kostya has already opened my bottle!' Kostya is already pouring the 600-ruble Spanish wine for the sommelier."),
]

TRANSITION = "Now let's listen to the storeroom wine scene again without interruption."
OUTRO = "With Moscow's top sommelier about to taste Max's cheap Spanish wine, both Max's scheme and Barinov's charade reach their climax at once. See you in the next scene."
CLOSING = ("nagiyev", "Это же самый лучший сомелье всей Москвы!")
CLOSING_TRANS = "That is the very best sommelier in all of Moscow!"
