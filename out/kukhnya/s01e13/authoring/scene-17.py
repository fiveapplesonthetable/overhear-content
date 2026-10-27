"""s01e13 scene 17: Неловкая встреча (An Awkward Encounter)."""

ID = "kukhnya-s01e13-scene-17"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 13
SCENE = 17
TITLE = "Неловкая встреча  (An Awkward Encounter)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "nastya": "anja"}
LABELS = {"anya": "Вика", "nastya": "Настя"}
SOURCE_NAME = "Кухня (Kukhnya) S1.13"
SOURCE_FILE = "sources/kukhnya/s01/e13.ru.dual.srt"
SOURCE_NOTE = "Cues 240-245. In the apartment hallway, Nastya unexpectedly bumps into Victoria leaving Max's room, leading to an awkward exchange."

INTRO = (
    "Trying to leave the apartment unnoticed, Victoria awkwardly bumps into Nastya in the hallway outside the bathroom. "
    "Surprised to see her boss there, Nastya asks whether Victoria and Max are together, creating an uncomfortable and amusing encounter. "
    "Let's listen to their conversation in Russian."
)

STORY = [
    ("nastya", "Здравствуйте, Виктория Сергеевна.", "Hello, Victoria Sergeyevna.",
     [(240, "Здрасте, Виктория Сергеевна")], "adapted"),
    ("anya", "Доброе утро, Настя.", "Good morning, Nastya.",
     [(240, "Привет, Настя")], "adapted"),
    ("nastya", "Проходите, я уже всё закончила.", "Come in, I am already done.",
     [(241, "Проходите, я уже закончила")], "adapted"),
    ("anya", "Спасибо, я просто ухожу на работу.", "Thank you, I am just leaving for work.",
     [], "new"),
    ("nastya", "Извините, я сегодня немного опоздаю.", "Excuse me, I will be a little late today.",
     [(242, "извините, пожалуйста, я, наверное, сегодня немножко задержусь")], "adapted"),
    ("anya", "Да, я всё прекрасно понимаю.", "Yes, I understand everything perfectly.",
     [(243, "Да-да, я понимаю")], "adapted"),
    ("anya", "Я сегодня тоже задержусь немного.", "I will also be delayed a bit today.",
     [(243, "Я, наверное, тоже")], "adapted"),
    ("nastya", "Вы провели здесь всю ночь?", "Did you spend the whole night here?",
     [], "new"),
    ("nastya", "Вы теперь встречаетесь с Максимом?", "Are you seeing Maxim now?",
     [(244, "а вы с Максимом?")], "adapted"),
    ("anya", "Настя, не задавай глупых вопросов.", "Nastya, do not ask silly questions.",
     [(245, "Настя")], "adapted"),
    ("nastya", "Всё, я молчу и всё поняла.", "That is all, I am silent and understood everything.",
     [(245, "Все-все, я поняла")], "adapted"),
    ("anya", "В ресторане об этом никто не знает.", "No one at the restaurant knows about this.",
     [], "new"),
    ("nastya", "Я никому ничего не скажу, обещаю.", "I will not tell anyone anything, I promise.",
     [], "new"),
]

OPENER = "Let's look at how Nastya and Victoria navigate this awkward morning encounter in the hallway."

WALK = [
    (2, None,
     "'Come in, I am already done.' A polite invitation indicating that the bathroom is free and ready for use."),
    (4, None,
     "'Excuse me, I will be a little late today.' A courteous notice to a boss that she expects a delay."),
    (8, None,
     "'Are you seeing Maxim now?' A curious question asking about the nature of a personal relationship."),
    (12, None,
     "'I will not tell anyone anything, I promise.' A reassuring promise to keep the secret safe from others."),
]

TRANSITION = "Now, let's listen to their hallway exchange once again."

OUTRO = (
    "Now you know how to greet a coworker unexpectedly, excuse a morning delay, and ask for discretion in Russian. "
    "Keep listening for these polite phrases in future scenes."
)

CLOSING = ("anya", "Мы с тобой договорились, Настя.")
