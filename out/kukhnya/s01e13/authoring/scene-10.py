ID = "kukhnya-s01e13-scene-10"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 13
SCENE = 10
TITLE = "Звонок из Милана  (A Call from Milan)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "angelina": "anja", "vika": "angelina"}
LABELS = {"anya": "Макс", "angelina": "Ангелина", "vika": "Вика"}
SOURCE_NAME = "Кухня (Kukhnya) S1.13"
SOURCE_FILE = "sources/kukhnya/s01/e13.ru.dual.srt"
SOURCE_NOTE = "Cues 127-141. Max makes a fake call to the restaurant to cancel Vika's trip."

INTRO = "Max decides to fix his mistake by making a fake phone call. He calls the restaurant hostess Angelina, pretending to be from the Milan trade show. Let's listen to his brilliant plan in Russian."

STORY = [
    ("anya", "Бонжорно, синьоры.", "Buongiorno, signori.", [(127, "Бонжорно, сеньоры.")], "typo fixed"),
    ("angelina", "Добрый день, ресторан Клод Моне.", "Good afternoon, Claude Monet restaurant.", [(128, "Добрый день, ресторан Клод Мане.")], "typo fixed"),
    ("anya", "Меня зовут Александр.", "My name is Alexander.", [(130, "Меня зовут Александр")], "shortened"),
    ("anya", "Выставка отменяется.", "The exhibition is cancelled.", [(132, "выставка отменится")], "adapted"),
    ("anya", "Передайте это Виктории.", "Pass this on to Victoria.", [(133, "Передайте")], "adapted"),
    ("angelina", "Хорошо, я передам.", "All right, I will pass it on.", [], "new"),
    ("anya", "Граци, синьора, чао-чао.", "Grazie, signora, ciao-ciao.", [(134, "Граци, сеньора"), (135, "Чао-чао.")], "combined"),
    ("angelina", "Да, алло. Виктория Сергеевна, здравствуйте.", "Yes, hello. Victoria Sergeyevna, hello.", [(138, "Да, алло. Виктория Сергеевна, здравствуйте")], ""),
    ("angelina", "Звонил представитель выставки из Милана.", "A representative of the exhibition from Milan called.", [(139, "Звонил представитель выставки из Милана")], ""),
    ("angelina", "Он сказал, что она отменяется.", "He said that it is cancelled.", [(139, "сказал, что она отменяется.")], ""),
    ("vika", "А, правда? Я уже в Домодедово.", "Oh, really? I am already in Domodedovo.", [(140, "А, правда? А я уже в Домодедово")], ""),
    ("vika", "Я чуть не улетела.", "I almost flew away.", [(140, "чуть не улетела.")], ""),
    ("vika", "Спасибо, что предупредили.", "Thank you for warning me.", [(141, "Спасибо, что предупредили.")], "")
]

OPENER = "Let's review the phone calls step by step."

WALK = [
    (0, None, "'Buongiorno, signori.' -- Max starts his performance with a terrible Italian accent."),
    (1, None, "'Good afternoon, Claude Monet restaurant.' -- The hostess answers the phone politely."),
    (2, None, "'My name is Alexander.' -- Max introduces himself using a fake identity."),
    (3, None, "'The exhibition is cancelled.' -- He delivers the crucial fake news about Milan."),
    (4, None, "'Pass this on to Victoria.' -- He makes sure his manager gets the message."),
    (5, None, "'All right, I will pass it on.' -- Angelina takes the important message seriously."),
    (6, None, "'Grazie, signora, ciao-ciao.' -- Max ends the phone call with more bad Italian."),
    (7, None, "'Yes, hello. Victoria Sergeyevna, hello.' -- The hostess greets her boss nervously."),
    (8, None, "'A representative of the exhibition from Milan called.' -- She reports the urgent news immediately."),
    (9, None, "'He said that it is cancelled.' -- The manager receives the shocking information."),
    (10, None, "'Oh, really? I am already in Domodedovo.' -- Vika is standing right at the airport."),
    (11, None, "'I almost flew away.' -- She realizes how close she was to leaving."),
    (12, None, "'Thank you for warning me.' -- The relieved manager thanks her employee.")
]

TRANSITION = "Now let's listen to the fake Italian phone call again."
OUTRO = "Max's crazy plan actually worked, and Vika is heading back to the restaurant. Let's see what happens next."
CLOSING = ("anya", "Выставка отменяется.")
