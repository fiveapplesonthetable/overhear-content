"""s01e11 scene 11: Гость Насти (Nastya's Guest)."""

ID = "kukhnya-s01e11-scene-11"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 11
SCENE = 11
TITLE = "Гость Насти  (Nastya's Guest)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "vika": "anja"}
LABELS = {"anya": "Саша", "vika": "Вика"}
SOURCE_NAME = "Кухня (Kukhnya) S1.11"
SOURCE_FILE = "sources/kukhnya/s01/e11.ru.dual.srt"
SOURCE_NOTE = "Cue 159. Victoria questions waitress Sasha about a strange customer who is seated in Nastya's section."

INTRO = (
    "Noticing an unfamiliar man sitting quietly at a corner table with a notebook, Victoria becomes increasingly suspicious. "
    "She quickly calls over waitress Sasha to investigate who the silent visitor is and which server is assigned to his table. "
    "Let's listen to their urgent hallway exchange in Russian."
)

STORY = [
    ("vika", "Саша, подойди сюда на секунду.", "Sasha, come over here for a second.",
     [], ""),
    ("anya", "Что случилось, Виктория Сергеевна?", "What happened, Victoria Sergeyevna?",
     [], ""),
    ("vika", "Кто сидит за пятым столиком?", "Who is sitting at the fifth table?",
     [], ""),
    ("anya", "Там сидит довольно странный мужчина.", "A rather strange man is sitting there.",
     [], ""),
    ("vika", "Почему он ничего не заказывает?", "Why is he not ordering anything?",
     [], ""),
    ("anya", "Я не знаю, это гость Насти.", "I do not know, this is Nastya's guest.",
     [(159, "Я не знаю")], ""),
    ("vika", "Она уже подошла к нему?", "Did she already approach him?",
     [], ""),
    ("anya", "Да, она только что дала меню.", "Yes, she just gave him the menu.",
     [], ""),
    ("vika", "Он внимательно изучает наш зал?", "Is he carefully studying our hall?",
     [], ""),
    ("anya", "Он постоянно пишет в свой блокнот.", "He is constantly writing in his notebook.",
     [], ""),
    ("vika", "Это очень похоже на проверку.", "This looks very much like an inspection.",
     [], ""),
    ("anya", "Мне позвать Настю к вам?", "Should I call Nastya to you?",
     [], ""),
    ("vika", "Да, позови её прямо сейчас.", "Yes, call her right now.",
     [], ""),
]

OPENER = "Let's examine how Victoria questions Sasha about the quiet man taking notes in the dining area."

WALK = [
    (2, None,
     "'Who is sitting at the fifth table?' An urgent interrogative inquiry identifying a specific customer in the dining room."),
    (5, None,
     "'I do not know, this is Nastya's guest.' A disclaimer of knowledge followed by a statement of table responsibility for the staff."),
    (9, None,
     "'He is constantly writing in his notebook.' A continuous descriptive sentence detailing suspicious note-taking activity by the visitor."),
    (10, None,
     "'This looks very much like an inspection.' An apprehensive assessment comparing a patron's behavior to an official audit."),
]

TRANSITION = "Now, let's hear Victoria question Sasha about the mystery guest once more."

OUTRO = (
    "Now you know how to ask about restaurant tables, assign service tasks, and express suspicion about audits in Russian. "
    "Listen for these floor management phrases in the next scene."
)

CLOSING = ("vika", "Нужно следить за каждым его шагом.")
