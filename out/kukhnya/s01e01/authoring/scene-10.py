"""s01e01 scene 10: Знакомое лицо в зале (A Familiar Face in the Hall)."""

ID = "kukhnya-s01e01-scene-10"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 1
SCENE = 10
TITLE = "Знакомое лицо в зале  (A Familiar Face in the Hall)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "sasha": "anja"}
LABELS = {"anya": "Макс", "sasha": "Саша"}
SOURCE_NAME = "Кухня (Kukhnya) S1.01"
SOURCE_FILE = "sources/kukhnya/s01/e01.ru.dual.srt"
SOURCE_NOTE = "Cues 72-73. Max arrives at Claude Monet for his job interview and spots Vika in the dining hall."

INTRO = (
    "Arriving at Claude Monet for his job interview, Max steps into the elegant dining hall and speaks with a waitress. "
    "Looking across the room, he is horrified to spot Vika—his date from the night before—commanding the floor as the art director. "
    "Let's listen to their conversation in Russian first."
)

STORY = [
    ("anya", "Здравствуйте! Я пришёл на встречу.",
     "Hello! I arrived for an appointment.",
     [], "greeting the waitress"),
    ("sasha", "Добрый день! Вы к Дмитрию Владимировичу?",
     "Good day! Are you here to see Dmitry Vladimirovich?",
     [], "asking about his appointment"),
    ("anya", "Да, он приглашал меня на работу.",
     "Yes, he invited me for a job.",
     [], "explaining his purpose"),
    ("sasha", "Хозяин пока занят на кухне.",
     "The owner is busy in the kitchen for now.",
     [], "updating on owner's status"),
    ("anya", "Понятно. А кто руководит залом?",
     "Understood. And who is managing the dining room?",
     [], "asking about management"),
    ("sasha", "Вон та строгая девушка у окна.",
     "That strict young woman over by the window.",
     [], "pointing across the room"),
    ("anya", "Как зовут эту красивую девушку?",
     "What is this beautiful young woman's name?",
     [], "inquiring about her name"),
    ("sasha", "Это Виктория Сергеевна, наш арт-директор.",
     "This is Viktoria Sergeyevna, our art director.",
     [], "revealing her position"),
    ("anya", "О нет, какая неприятная ситуация!",
     "Oh no, what an unpleasant situation!",
     [(72, "Дерьмо")], "reacting in shock upon recognizing Vika"),
    ("sasha", "Что случилось? Вы так побледнели!",
     "What happened? You turned so pale!",
     [], "noticing his sudden shock"),
    ("anya", "Ничего страшного, голова кружится.",
     "Nothing terrible, my head is spinning.",
     [], "making an excuse"),
    ("sasha", "Хотите сесть за свободный столик?",
     "Would you like to sit at an available table?",
     [], "offering a seat"),
    ("anya", "Нет, спасибо, я отойду назад.",
     "No, thank you, I will step back.",
     [], "retreating to hide"),
]

OPENER = "Let's replay a few lines to examine key phrases and grammar."

WALK = [
    (1, "Вы к Дмитрию Владимировичу?",
     "'Are you here to see Dmitry Vladimirovich?' Sasha asks, using the preposition 'k' with the dative case for visiting a person."),
    (7, "Это Виктория Сергеевна, наш арт-директор.",
     "'This is Viktoria Sergeyevna, our art director,' Sasha explains, introducing the formal patronymic."),
    (8, "О нет, какая неприятная ситуация!",
     "'Oh no, what an unpleasant situation!' Max mutters under his breath in complete shock."),
    (11, "Хотите сесть за свободный столик?",
     "'Would you like to sit at an available table?' the waitress offers courteously."),
]

TRANSITION = "Now listen to the full dining room dialogue once more."

OUTRO = "Max quickly retreats toward the corridor to avoid being spotted."

CLOSING = ("anya", "Мне нужно срочно спрятаться.")
