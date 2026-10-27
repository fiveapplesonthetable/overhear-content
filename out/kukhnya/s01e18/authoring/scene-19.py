ID = "kukhnya-s01e18-scene-19"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 18
SCENE = 19
TITLE = "Экономия на бармене  (Saving on the Bartender)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "nagiyev": "anja"}
LABELS = {"anya": "Костя", "nagiyev": "Нагиев"}
SOURCE_NAME = "Кухня (Kukhnya) S1.18"
SOURCE_FILE = "sources/kukhnya/s01/e18.ru.dual.srt"
SOURCE_NOTE = "Scene 19"

INTRO = "The austerity measures continue across the restaurant. Nagiyev confronts Kostya the bartender to deliver some bad news. Let's listen closely to their exchange in Russian first, and then walk through each line together."

STORY = [
    ("anya", "Я просто делал свою работу.",
     "I was just doing my job.",
     [], "new"),
    ("nagiyev", "Мы экономим на всём.",
     "We are saving on everything.",
     [], "new"),
    ("nagiyev", "Мы сэкономили на бармене.",
     "We saved on the bartender.",
     [(351, 'на Бармене сэкономили')], "adapted"),
    ("anya", "Вы не можете меня уволить.",
     "You cannot fire me.",
     [], "new"),
    ("nagiyev", "Ты уволен, балбес.",
     "You are fired, idiot.",
     [(352, 'Ты уволен, балбес')], "adapted"),
    ("anya", "Балбес, да?",
     "An idiot, huh?",
     [(353, 'Балбес, да')], "adapted"),
    ("anya", "Это очень несправедливо.",
     "This is very unfair.",
     [], "new"),
    ("nagiyev", "Ресторан в трудном положении.",
     "The restaurant is in a difficult situation.",
     [], "new"),
    ("anya", "Кто будет наливать напитки?",
     "Who will pour drinks?",
     [], "new"),
    ("nagiyev", "Это больше не твоя проблема.",
     "This is no longer your problem.",
     [], "new"),
    ("anya", "Хорошо, я уйду сегодня.",
     "Fine, I will leave today.",
     [], "new"),
    ("nagiyev", "Вот и отлично.",
     "That is excellent.",
     [], "new"),
]

OPENER = "Let us break down this interaction."

WALK = [
    (0, None,
     "'I was just doing my job.' -- ENG The bartender tries to defend his performance."),
    (1, None,
     "'We are saving on everything.' -- ENG Nagiyev explains the new strict budget."),
    (2, None,
     "'We saved on the bartender.' -- ENG He casually announces the elimination of the role."),
    (3, None,
     "'You cannot fire me.' -- ENG Kostya is shocked and tries to argue."),
    (4, None,
     "'You are fired, idiot.' -- ENG The owner insults him while giving the final word."),
    (5, None,
     "'An idiot, huh?' -- ENG The young man is offended by the rude remark."),
    (6, None,
     "'This is very unfair.' -- ENG He feels betrayed by the management."),
    (7, None,
     "'The restaurant is in a difficult situation.' -- ENG Nagiyev justifies his harsh decision."),
    (8, None,
     "'Who will pour drinks?' -- ENG Kostya wonders how the bar will operate without him."),
    (9, None,
     "'This is no longer your problem.' -- ENG The boss dismisses his concerns entirely."),
    (10, None,
     "'Fine, I will leave today.' -- ENG The bartender accepts his fate and decides to pack up."),
    (11, None,
     "'That is excellent.' -- ENG Nagiyev is pleased that the conversation is over."),
]

TRANSITION = "Now let us listen to the conversation again without interruption."
OUTRO = "Kostya realizes he has lost his job as part of the severe cost-cutting strategy."
CLOSING = ("nagiyev", "Вот и отлично.")
