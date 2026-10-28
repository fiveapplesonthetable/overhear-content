ID = "kukhnya-s04e06-scene-02"
SHOW = "kukhnya"
SEASON = 4
EPISODE = 6
SCENE = 2
TITLE = "Старый друг Шефа  (The Chef's Old Friend)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "guest": "anja"}
LABELS = {"anya": "Шеф", "guest": "Гость"}
SOURCE_NAME = "Кухня (Kukhnya) S4.06"
SOURCE_FILE = "sources/kukhnya/s04/e06.ru.srt"
SOURCE_NOTE = "Cues 19-33. Outside the restaurant, Chef Viktor Barinov runs into an old friend who heard he was fired, so Barinov boasts that he is now the head chef of Arcobaleno."

INTRO = "Walking down the street near the restaurant, Viktor Barinov bumps into his old friend Volodya, who is visiting Moscow in transit. Too proud to admit he was fired and now works as a regular cook, Barinov brags that he was poached to run Arcobaleno as head chef."

STORY = [
    ("guest", "Здравствуй, Витя, как я рад тебя видеть!", "Hello, Vitya, how glad I am to see you!", [(19, "О, Витя!"), (20, "Володька! Витя!")], "adapted"),
    ("anya", "Володя, друг, ты здесь какими судьбами?", "Volodya, pal, what brings you here?", [(22, "Ну, какими судьбами?")], "adapted"),
    ("guest", "Я проездом в Москве, решил забежать.", "I am passing through Moscow and decided to drop by.", [(23, "И вот проездом в Москве решил к тебе забежать.")], "adapted"),
    ("guest", "А мне сказали, что тебя отсюда уволили.", "And people told me that you were fired from here.", [(24, "А мне сказали, что тебя уволили.")], "adapted"),
    ("anya", "Кто меня вообще может уволить с работы?", "Who could ever fire me from work?", [(25, "Кто меня может уволить?")], "adapted"),
    ("anya", "За мной сейчас вся Москва гоняется!", "All of Moscow is chasing after me right now!", [(26, "За мной вся Москва гоняется.")], "adapted"),
    ("anya", "Меня не уволили, а просто перекупили.", "They did not fire me, they simply outbid for me.", [(26, "а перекупили.")], "adapted"),
    ("guest", "И где ты теперь работаешь главным шефом?", "And where are you working as head chef now?", [(27, "Ну, где ты теперь шествуешь?")], "adapted"),
    ("anya", "Да вот тут, в соседнем ресторане руковожу.", "Right over here, I am in charge at the neighboring restaurant.", [(28, "Да вот тут, в соседнем ресторане рулю.")], "adapted"),
    ("anya", "Это очень красивое и модное место.", "It is a very beautiful and fashionable place.", [(29, "Очень пафосное место.")], "adapted"),
    ("guest", "Значит, завтра жди нас с женой в гости!", "Then expect my wife and me for a visit tomorrow!", [(30, "Значит, завтра жди нас с женой в гости.")], ""),
    ("anya", "Отлично, тогда до завтра, дорогой друг!", "Excellent, then see you tomorrow, dear pal!", [(32, "Отлично."), (33, "До завтра.")], "adapted"),
]

OPENER = "Let's examine Chef Barinov's boastful reunion on the street line by line."

WALK = [
    (0, None, "'Hello, Vitya, how glad I am to see you!' Masculine short adjective 'glad' takes an infinitive complement."),
    (1, None, "'Volodya, pal, what brings you here?' The instrumental plural idiom 'by what fates' means 'what brings you here'."),
    (2, None, "'I am passing through Moscow and decided to drop by.' Instrumental noun 'in transit' describes a brief stopover on a trip."),
    (3, None, "'And people told me that you were fired from here.' Impersonal third-person plural past expresses rumor or hearsay."),
    (4, None, "'Who could ever fire me from work?' Barinov bristles at the rumor with a rhetorical question."),
    (5, None, "'All of Moscow is chasing after me right now!' The reflexive verb for chasing governs the preposition 'behind/after' plus instrumental."),
    (6, None, "'They did not fire me, they simply outbid for me.' Prefixed perfective verb means luring an employee away with higher pay."),
    (7, None, "'And where are you working as head chef now?' Instrumental case marks the leadership role he claims to hold."),
    (8, None, "'Right over here, I am in charge at the neighboring restaurant.' Prepositional case locates the rival Italian restaurant next door."),
    (9, None, "'It is a very beautiful and fashionable place.' Neuter singular adjectives agree with the noun for place."),
    (10, None, "'Then expect my wife and me for a visit tomorrow!' The plural idiom 'we with wife' means 'my wife and I'."),
    (11, None, "'Excellent, then see you tomorrow, dear pal!' Barinov smiles outwardly while panicking over how to fake being head chef tomorrow."),
]

TRANSITION = "Now let's hear the reunion between Barinov and his old friend again."
OUTRO = "Barinov's pride has trapped him into pretending to be head chef of Arcobaleno when his friend visits tomorrow. See you in the next scene."
CLOSING = ("anya", "За мной сейчас вся Москва гоняется!")
CLOSING_TRANS = "All of Moscow is chasing after me right now!"
