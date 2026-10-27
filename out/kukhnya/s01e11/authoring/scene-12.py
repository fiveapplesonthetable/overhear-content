"""s01e11 scene 12: Второй критик (The Second Critic)."""

ID = "kukhnya-s01e11-scene-12"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 11
SCENE = 12
TITLE = "Второй критик  (The Second Critic)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "chef": "anja"}
LABELS = {"anya": "Настя", "chef": "Шеф"}
SOURCE_NAME = "Кухня (Kukhnya) S1.11"
SOURCE_FILE = "sources/kukhnya/s01/e11.ru.dual.srt"
SOURCE_NOTE = "Cues 160-165. Chef Barinov interrogates waitress Nastya about the silent guest taking notes and fears there are two critics."

INTRO = (
    "Fearing the mystery visitor may also be a secret inspector, Chef Barinov urgently interrogates waitress Nastya about the man taking notes at her table. "
    "As Nastya reports that the guest has ordered nothing and writes continuously, Barinov panics at the thought of facing two food critics at once. "
    "Let's listen to their panicked exchange in Russian."
)

STORY = [
    ("chef", "Настя, давно у тебя этот гость?", "Nastya, how long have you had this guest?",
     [(160, "Давно у тебя этот гость?")], ""),
    ("anya", "Какой именно гость, шеф?", "Which guest exactly, chef?",
     [(160, "Какой гость?")], ""),
    ("chef", "Тот странный мужчина в тёмном пиджаке.", "That strange man in the dark jacket.",
     [], ""),
    ("anya", "Можно сказать, довольно давно.", "You could say, quite a long time.",
     [(161, "Можно сказать, давно")], ""),
    ("chef", "Что он уже успел заказать?", "What has he already managed to order?",
     [(162, "Что он заказал?")], ""),
    ("anya", "Пока совершенно ничего, только воду.", "Nothing at all so far, only water.",
     [(162, "Пока ничего")], ""),
    ("anya", "Он всё время что-то пишет.", "He is writing something the whole time.",
     [(162, "он все время что-то пишет")], ""),
    ("chef", "Он что, известный писатель?", "Is he some famous writer?",
     [(163, "Писатель?")], ""),
    ("anya", "Вы же говорили про ту девушку!", "But you were talking about that girl!",
     [(164, "что критик – это вот та девушка")], ""),
    ("chef", "Получается, у меня теперь два критика?", "It turns out I have two critics now?",
     [(165, "у меня теперь два критика?")], ""),
    ("anya", "Что мне теперь делать, шеф?", "What should I do now, chef?",
     [], ""),
    ("chef", "Немедленно отнеси ему наше фирменное меню.", "Immediately take him our signature menu.",
     [], ""),
    ("anya", "Я всё сделаю в лучшем виде.", "I will do everything in the best way.",
     [], ""),
]

OPENER = "Let's explore how Chef Barinov questions Nastya and realizes he might be dealing with two simultaneous food critics."

WALK = [
    (0, None,
     "'Nastya, how long have you had this guest?' A direct interrogative question expressing urgency about a patron's visit."),
    (6, None,
     "'He is writing something the whole time.' An imperfective statement highlighting persistent behavior that alarms the staff."),
    (9, None,
     "'It turns out I have two critics now?' A rhetorical question conveying disbelief and escalating panic for the kitchen management."),
    (11, None,
     "'Immediately take him our signature menu.' An urgent imperative directing the server to provide special service to the visitor."),
]

TRANSITION = "Now, let's hear Chef Barinov interrogate Nastya once more."

OUTRO = (
    "Now you know how to interrogate staff about guests, discuss suspicious writing habits, and handle service pressure in Russian. "
    "Keep practicing these dynamic conversational skills as the story develops."
)

CLOSING = ("chef", "Мы должны обслужить обоих идеально.")
