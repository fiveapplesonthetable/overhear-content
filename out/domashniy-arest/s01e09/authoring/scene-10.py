ID = "domashniy-arest-s01e09-scene-10"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 9
SCENE = 10
TITLE = "Повестка в суд  (Court Summons)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "nina": "angelina"}
LABELS = {"anya": "Курьер", "nina": "Нина"}
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.09"
SOURCE_FILE = "sources/domashniy-arest/s01/e09.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 287-297. A theatrical courier delivers the fake divorce summons to Nina Samsonova "
    "in the communal hallway. Nina is stunned and furious, while the courier strictly demands her signature."
)

INTRO = (
    "In this scene, Arkady's psychological scheme is set in motion. "
    "A courier arrives at the communal apartment to hand Nina Samsonova an official-looking document. "
    "Nina is shocked to learn that her husband has filed for divorce, while the formal courier "
    "insists she sign the legal receipt. "
    "Let's listen to their confrontation in Russian first."
)

STORY = [
    ("anya", "Здравствуйте, гражданка Самсонова.",
     "Hello, citizen Samsonova.",
     [(287, "Здравствуйте, гражданка Самсонова")], ""),
    ("anya", "Вам повестка в суд.",
     "A court summons for you.",
     [(287, "Вам повестка в суд")], ""),
    ("nina", "Господи, в какой ещё суд?",
     "Good heavens, what court?",
     [(288, "Господи, какой суд")], ""),
    ("anya", "Дело гражданское. О разводе.",
     "A civil matter. About divorce.",
     [(289, "Дело гражданское. О разводе")], ""),
    ("nina", "О каком ещё разводе?",
     "About what divorce?",
     [(290, "В каком разводе")], ""),
    ("anya", "Ну, не о моём же!",
     "Well, not about mine!",
     [(291, "Ну, не моем же")], ""),
    ("anya", "Ознакомьтесь и распишитесь здесь.",
     "Familiarize yourself and sign here.",
     [(292, "Ознакомьтесь и распишитесь")], ""),
    ("nina", "Слушайте, это ерунда какая-то!",
     "Listen, this is total nonsense!",
     [(293, "Слушайте, ерунда какая-то")], ""),
    ("anya", "Не ерунда, а государственный документ!",
     "Not nonsense, but a government document!",
     [(294, "Не ерунда, а государственный документ")], ""),
    ("anya", "Пожалуйста, распишитесь за получение.",
     "Please sign for the receipt.",
     [(295, "распишитесь")], ""),
    ("nina", "Ваня совсем с ума сошёл!",
     "Vanya has completely lost his mind!",
     [], "Nina expresses disbelief at Samsonov"),
    ("anya", "Будьте любезны явиться в суд.",
     "Kindly appear in court.",
     [(296, "будьте любезны, явиться")], ""),
    ("anya", "В строго назначенное время!",
     "At the strictly appointed time!",
     [(296, "в назначенное время")], ""),
    ("anya", "Всего хорошего. Прощайте!",
     "All the best. Farewell!",
     [(297, "Прощайте")], ""),
]

OPENER = (
    "Now let's examine the dramatic court summons delivery line by line. "
    "The courier speaks with official theatrical gravity."
)

WALK = [
    (0, None,
     "'Hello, citizen Samsonova.' The courier uses formal Soviet-style legal address."),
    (1, None,
     "'A court summons for you.' The dative pronoun indicates the recipient of the official notice."),
    (2, None,
     "'Good heavens, what court?' Nina expresses disbelief at the sudden legal document."),
    (3, None,
     "'A civil matter. About divorce.' The courier concisely specifies the category of lawsuit."),
    (4, None,
     "'About what divorce?' Nina asks with rising indignation using the prepositional case."),
    (5, None,
     "'Well, not about mine!' The courier retorts with deadpan bureaucratic sarcasm."),
    (6, None,
     "'Familiarize yourself and sign here.' Two formal imperative verbs instruct her on procedural protocol."),
    (7, None,
     "'Listen, this is total nonsense!' Nina dismisses the document as an absurd prank."),
    (8, None,
     "'Not nonsense, but a government document!' The courier elevates the fake notice to official status."),
    (9, None,
     "'Please sign for the receipt.' The polite request demands legal compliance."),
    (10, None,
     "'Vanya has completely lost his mind!' Nina realizes that her husband is retaliating."),
    (11, None,
     "'Kindly appear in court.' The courteous formula requires mandatory court attendance."),
    (12, None,
     "'At the strictly appointed time!' The passive participle specifies the court schedule."),
    (13, None,
     "'All the best. Farewell!' The courier concludes his delivery with a melodramatic exit line."),
]

TRANSITION = "Now let's listen to the summons delivery one more time without interruption."
OUTRO = (
    "Nina holds the fake summons in utter shock as Arkady's psychological trap begins to work. "
    "In the next scenes, Marina continues her undercover mission."
)
CLOSING = ("anya", "Вам повестка в суд.")
