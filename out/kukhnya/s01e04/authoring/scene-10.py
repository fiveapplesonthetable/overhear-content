"""s01e04 scene 10: Детектор лжи (The Lie Detector)."""

ID = "kukhnya-s01e04-scene-10"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 4
SCENE = 10
TITLE = "Детектор лжи  (The Lie Detector)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "chef": "anja", "expert": "angelina"}
LABELS = {"anya": "Федя", "chef": "Шеф", "expert": "Эксперт"}
SOURCE_NAME = "Кухня (Kukhnya) S1.04"
SOURCE_FILE = "sources/kukhnya/s01/e04.ru.dual.srt"
SOURCE_NOTE = "Cues 114-144. Fedya is interrogated on a lie detector by Barinov and a polygraph expert."

INTRO = (
    "Determined to discover which kitchen staff member secretly interviewed at the rival restaurant Arcobaleno, Chef Barinov hires a polygraph examiner. "
    "Hooked up to the lie detector machine in Barinov's office, fish cook Fedya undergoes a tense interrogation. "
    "Let's listen to their conversation in Russian first."
)

STORY = [
    ("chef", "Заходи, Федя. Садись на стул.",
     "Come in, Fedya. Sit down on the chair.",
     [(114, "Заходи")], "calling Fedya in"),
    ("anya", "Шеф, а что это такое?",
     "Chef, what is this thing?",
     [(116, "Шеф, это чего")], "asking nervously"),
    ("chef", "Это настоящий детектор лжи, Федя.",
     "This is a real lie detector, Fedya.",
     [(117, "Это детектор лжи, Федя")], "introducing the apparatus"),
    ("chef", "Я должен поймать крысу на кухне.",
     "I must catch the rat in the kitchen.",
     [(118, "поймать крысу")], "stating his goal"),
    ("expert", "Отвечайте только «да» или «нет».",
     "Answer only 'yes' or 'no'.",
     [(120, "Отвечайте только")], "setting the rule"),
    ("anya", "Хорошо, это мне вполне понятно.",
     "Fine, that is completely clear to me.",
     [(121, "Понятно")], "nodding nervously"),
    ("expert", "Скажите, сегодня действительно среда?",
     "Tell me, is today really Wednesday?",
     [(123, "Скажите, сегодня среда")], "testing baseline"),
    ("anya", "Да, сегодня среда.",
     "Yes, today is Wednesday.",
     [(124, "Да")], "confirming truth"),
    ("expert", "Ваше настоящее имя Фёдор?",
     "Is your real name Fyodor?",
     [(129, "Ваше имя Фёдор")], "testing identity"),
    ("anya", "Да.",
     "Yes.",
     [(130, "Да")], "answering quietly"),
    ("chef", "Ты ходил в соседний ресторан?",
     "Did you go to the neighboring restaurant?",
     [(135, "соседний ресторан")], "demanding the truth"),
    ("anya", "Нет, я никуда не ходил.",
     "No, I did not go anywhere.",
     [(137, "Нет")], "denying the charge"),
    ("chef", "Свободен. Позови сюда Сеню.",
     "You are free to go. Call Senya in here.",
     [(138, "Свободен"), (139, "позови там Сеню")], "dismissing Fedya"),
]

OPENER = "Let's replay a few lines to examine key phrases and vocabulary."

WALK = [
    (2, "Это настоящий детектор лжи, Федя.",
     "'This is a real lie detector, Fedya,' Barinov announces sternly as the specialist hooks up the wires."),
    (4, "Отвечайте только «да» или «нет».",
     "'Answer only \"yes\" or \"no\",' the polygraph examiner instructs before beginning the baseline questions."),
    (10, "Ты ходил в соседний ресторан?",
     "'Did you go to the neighboring restaurant?' Chef Barinov asks abruptly, getting to the true point of the test."),
    (12, "Свободен. Позови сюда Сеню.",
     "'You are free to go. Call Senya in here,' Barinov orders, satisfied that Fedya is not the traitor."),
]

TRANSITION = "Now listen to the full lie detector interrogation once more."

OUTRO = "Fedya hurries out of the office, relieved that his dark secrets went undetected."

CLOSING = ("anya", "Я чуть не умер от страха.")
