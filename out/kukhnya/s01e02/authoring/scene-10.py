"""s01e02 scene 10: Гости просят шефа (The Guests Want the Chef)."""

ID = "kukhnya-s01e02-scene-10"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 2
SCENE = 10
TITLE = "Гости просят шефа  (The Guests Want the Chef)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "fedya": "anja", "sasha": "angelina"}
LABELS = {"anya": "Сеня", "fedya": "Федя", "sasha": "Саша"}
SOURCE_NAME = "Кухня (Kukhnya) S1.02"
SOURCE_FILE = "sources/kukhnya/s01/e02.ru.dual.srt"
SOURCE_NOTE = "Cues 131-148. Sasha tells Senya and Fedya that the rival chef wants to see Barinov."

INTRO = (
    "Inside the kitchen of Claude Monet, panic erupts when waitress Sasha reports that a dining guest has summoned the head chef. "
    "Having secretly improvised a replacement dish behind Barinov's back, cooks Senya and Fedya desperately argue over who must face the fiery chef. "
    "Let's listen to their conversation in Russian first."
)

STORY = [
    ("sasha", "Ребята, гости в зале просят шефа!",
     "Guys, the guests in the dining hall want the chef!",
     [(138, "Гости просят шефа")], "breaking the alarming news"),
    ("anya", "Что? Она уже попробовала наше блюдо?",
     "What? Has she already tasted our dish?",
     [], "asking nervously"),
    ("fedya", "Да, она съела почти всё фрикасе.",
     "Yes, she ate almost all the fricassee.",
     [], "confirming the plate is empty"),
    ("anya", "Может быть, она хочет добавки?",
     "Maybe she wants seconds?",
     [(136, "добавки попросить")], "hoping for the best"),
    ("fedya", "Нет, она зовёт именно шеф-повара.",
     "No, she is calling specifically for the head chef.",
     [(134, "Позовите, пожалуйста, вашего шефа")], "clarifying the summons"),
    ("anya", "Я предупреждал! Это была плохая идея!",
     "I warned you! That was a bad idea!",
     [(140, "Предупреждал")], "blaming Fedya"),
    ("fedya", "Сам иди к шефу в кабинет!",
     "Go to Chef's office yourself!",
     [(140, "Иди к шефу")], "refusing to go"),
    ("anya", "Почему я? Ты всё это придумал!",
     "Why me? You came up with all of this!",
     [(141, "Причем здесь я"), (142, "Все придумал")], "defending himself"),
    ("fedya", "Ты его правая рука на кухне.",
     "You are his right-hand man in the kitchen.",
     [(143, "ты его правая рука")], "giving a flattering excuse"),
    ("anya", "Я не пойду, он меня убьёт!",
     "I am not going, he will kill me!",
     [(144, "Я не пойду")], "panicking completely"),
    ("fedya", "Давайте просто напишем шефу сообщение.",
     "Let us just send Chef a text message.",
     [(146, "давайте напишем шефу")], "proposing a coward's way out"),
    ("anya", "И сразу напишем заявление об увольнении?",
     "And write our resignation letters right away?",
     [(147, "заявления по собственному напишем")], "mocking the proposal"),
    ("fedya", "Не надо каркать раньше времени!",
     "No need to jinx it ahead of time!",
     [(148, "Не надо каркать")], "telling him to stop predicting doom"),
]

OPENER = "Let's replay a few lines to examine key phrases and vocabulary."

WALK = [
    (0, "Ребята, гости в зале просят шефа!",
     "'Guys, the guests in the dining hall want the chef!' Sasha announces urgently to the kitchen staff."),
    (6, "Сам иди к шефу в кабинет!",
     "'Go to Chef's office yourself!' Fedya shouts, refusing to deliver the bad news alone."),
    (8, "Ты его правая рука на кухне.",
     "'You are his right-hand man in the kitchen,' Fedya insists, using the common idiom for a trusted deputy."),
    (12, "Не надо каркать раньше времени!",
     "'No need to jinx it ahead of time!' Fedya warns, using the colloquial verb for inviting bad luck."),
]

TRANSITION = "Now listen to the full kitchen dialogue once more."

OUTRO = "Unable to agree on who will face Barinov, the cooks remain frozen in fear."

CLOSING = ("anya", "Мы точно потеряем эту работу.")
