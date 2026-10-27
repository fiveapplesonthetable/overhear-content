ID = "kukhnya-s01e14-scene-02"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 14
SCENE = 2
TITLE = "Жажда веселья  (Thirst for Fun)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "vika": "anja"}
LABELS = {"anya": "Макс", "vika": "Саша"}
SOURCE_NAME = "Кухня (Kukhnya) S1.14"
SOURCE_FILE = "sources/kukhnya/s01/e14.ru.dual.srt"
SOURCE_NOTE = "Cues 4-6."

INTRO = "Max compliments Sasha on her work and suggests they have some fun. Let's listen closely to their exchange in Russian first, and then walk through each line together."

STORY = [
    ("anya", "Саша, ты видела новый красивый торт?",
     "Sasha, did you see the new beautiful cake?",
     [], "new"),
    ("vika", "Конечно, я сама его сегодня украшала.",
     "Of course, I decorated it myself today.",
     [], "new"),
    ("anya", "Он выглядит просто великолепно.",
     "It looks simply magnificent.",
     [], "new"),
    ("vika", "Спасибо, я очень сильно старалась.",
     "Thank you, I tried very hard.",
     [], "new"),
    ("anya", "Шеф уже видел твою новую работу?",
     "Has the chef already seen your new work?",
     [], "new"),
    ("vika", "Да, он был очень доволен мной.",
     "Yes, he was very satisfied with me.",
     [], "new"),
    ("anya", "И это у вас получилось.",
     "And you pulled it off.",
     [(4, 'И это у вас получилось.')], "adapted"),
    ("vika", "А теперь можно немного отдохнуть.",
     "And now we can rest a little.",
     [], "new"),
    ("anya", "Кто тут хочет повеселиться?",
     "Who wants to have some fun?",
     [(5, 'Кто тут хочет повеселиться?')], "adapted"),
    ("vika", "Я хочу.",
     "I do.",
     [(6, 'Я хочу.')], "adapted"),
    ("anya", "Тогда пойдём со мной на улицу.",
     "Then let us go outside with me.",
     [], "new"),
    ("vika", "Подожди, я только сниму свой фартук.",
     "Wait, I will just take off my apron.",
     [], "new"),
]

OPENER = "Let's look at this kitchen banter."

WALK = [
    (0, None,
     "'Sasha, did you see the new beautiful cake?' -- Max asks her about the fresh dessert."),
    (1, None,
     "'Of course, I decorated it myself today.' -- Sasha confirms her role in the work."),
    (2, None,
     "'It looks simply magnificent.' -- He compliments her fine culinary skills."),
    (3, None,
     "'Thank you, I tried very hard.' -- She expresses her gratitude to him."),
    (4, None,
     "'Has the chef already seen your new work?' -- The cook asks about their demanding boss."),
    (5, None,
     "'Yes, he was very satisfied with me.' -- Sasha shares her positive feedback from him."),
    (6, None,
     "'And you pulled it off.' -- Max praises her for her great achievement."),
    (7, None,
     "'And now we can rest a little.' -- She suggests taking a break from their tasks."),
    (8, None,
     "'Who wants to have some fun?' -- He loudly asks the kitchen staff a question."),
    (9, None,
     "'I do.' -- Sasha eagerly accepts his fun offer."),
    (10, None,
     "'Then let us go outside with me.' -- He invites her to leave the kitchen together."),
    (11, None,
     "'Wait, I will just take off my apron.' -- She asks him to give her a minute."),
]

TRANSITION = "Now let's listen to the conversation again without interruption."
OUTRO = "They sneak out of the kitchen for a quick break."
CLOSING = ("vika", "Подожди, я только сниму свой фартук.")
