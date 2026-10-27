ID = "kukhnya-s01e18-scene-17"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 18
SCENE = 17
TITLE = "Увольнения  (Firings)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "nagiyev": "anja"}
LABELS = {"anya": "Виктор", "nagiyev": "Нагиев"}
SOURCE_NAME = "Кухня (Kukhnya) S1.18"
SOURCE_FILE = "sources/kukhnya/s01/e18.ru.dual.srt"
SOURCE_NOTE = "Scene 17"

INTRO = "Nagiyev and Viktor have a heated argument in the office about the restaurant's budget. Nagiyev wants to save money by firing the most expensive kitchen staff."

STORY = [
    ("nagiyev", "Я должен уволить твоих поваров.",
     "I must fire your cooks.",
     [(308, 'уволить')], "adapted"),
    ("anya", "Ты совсем сошёл с ума?",
     "Have you gone completely crazy?",
     [], "new"),
    ("nagiyev", "Они слишком дорого стоят.",
     "They cost too much.",
     [], "new"),
    ("nagiyev", "Это почти полмиллиона каждый месяц.",
     "This is almost half a million every month.",
     [(305, 'полмиллиона каждый месяц')], "adapted"),
    ("anya", "Ты не можешь их увольнять.",
     "You cannot fire them.",
     [(309, 'нельзя увольнять')], "adapted"),
    ("anya", "Это лучшая команда в Москве.",
     "This is the best team in Moscow.",
     [(312, 'лучшие в Москве')], "adapted"),
    ("nagiyev", "Дешевле найти новых людей.",
     "It is cheaper to find new people.",
     [(314, 'Дешевле')], "adapted"),
    ("nagiyev", "Какая разница, кто режет морковь?",
     "What difference does it make who cuts carrots?",
     [(313, 'какая разница, кто будет морковь')], "adapted"),
    ("anya", "Это моя команда!",
     "This is my team!",
     [(315, 'моя команда')], "adapted"),
    ("anya", "Если ты их уволишь, ты потеряешь меня.",
     "If you fire them, you will lose me.",
     [(328, 'уволишь их, потеряешь меня')], "adapted"),
    ("nagiyev", "Витя, просто сядь и успокойся.",
     "Vitya, just sit and calm down.",
     [(318, 'Витя, сядь')], "adapted"),
    ("anya", "Хорошо, разбирайтесь сами.",
     "Alright, sort it out yourselves.",
     [(320, 'Разбирайтесь')], "adapted"),
    ("anya", "А я пока увольняюсь.",
     "And I am quitting in the meantime.",
     [(320, 'А я пока увольняюсь')], "adapted"),
    ("nagiyev", "Подожди, мы всё решим.",
     "Wait, we will solve everything.",
     [], "new"),
]

OPENER = "Let us break down this interaction."

WALK = [
    (0, None,
     "'I must fire your cooks.' -- ENG The restaurant owner wants to reduce costs."),
    (1, None,
     "'Have you gone completely crazy?' -- ENG The chef is shocked by this sudden decision."),
    (2, None,
     "'They cost too much.' -- ENG Nagiyev explains that the current salaries are too high."),
    (3, None,
     "'This is almost half a million every month.' -- ENG He calculates the massive expenses."),
    (4, None,
     "'You cannot fire them.' -- ENG Viktor defends his talented colleagues."),
    (5, None,
     "'This is the best team in Moscow.' -- ENG He insists that their skills are unmatched."),
    (6, None,
     "'It is cheaper to find new people.' -- ENG The owner prefers to hire less experienced workers."),
    (7, None,
     "'What difference does it make who cuts carrots?' -- ENG He argues that basic tasks do not require experts."),
    (8, None,
     "'This is my team!' -- ENG The loyal chef refuses to abandon his kitchen staff."),
    (9, None,
     "'If you fire them, you will lose me.' -- ENG Viktor gives him a strict ultimatum."),
    (10, None,
     "'Vitya, just sit and calm down.' -- ENG Nagiyev tries to de-escalate the conflict."),
    (11, None,
     "'Alright, sort it out yourselves.' -- ENG The angry chef gives up on the conversation."),
    (12, None,
     "'And I am quitting in the meantime.' -- ENG He decides to leave his job immediately."),
    (13, None,
     "'Wait, we will solve everything.' -- ENG The owner tries to stop him from leaving."),
]

TRANSITION = "Now let us listen to the conversation again without interruption."
OUTRO = "Angry and feeling betrayed, Viktor threatens to resign rather than lose his best kitchen team."
CLOSING = ("nagiyev", "Подожди, мы всё решим.")
