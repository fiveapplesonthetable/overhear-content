ID = "kukhnya-s01e17-scene-04"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 17
SCENE = 4
TITLE = "Дисциплина в зале  (Discipline in the Hall)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "vika": "anja", "kostya": "angelina"}
LABELS = {"anya": "Макс", "vika": "Вика", "kostya": "Костя"}
SOURCE_NAME = "Кухня (Kukhnya) S1.17"
SOURCE_FILE = "sources/kukhnya/s01/e17.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 48-61. Victoria catches Kostya and Nastya flirting during their shift and scolds the staff, "
    "before Max tries to ask Victoria out on an evening date."
)

INTRO = (
    "In the dining hall of Claude Monet, Victoria reprimands the waitstaff for flirting during work hours. "
    "Seeing her visibly stressed, Max approaches Victoria to invite her out for a relaxing evening, hoping to brighten her mood. "
    "Let's listen to their conversation in Russian first."
)

OPENER = "Now let's examine the conversation line by line."

STORY = [
    ("vika", "Настя, быстро убери пятый столик!",
     "Nastya, quickly clear the fifth table!",
     [(48, "Настя, убери пятый столик.")], "adapted"),
    ("vika", "Вы совсем обнаглели на этой работе?",
     "Have you completely lost your nerve at this job?",
     [(50, "На работе вы должны работать")], "adapted"),
    ("vika", "Здесь надо работать, а не обжиматься.",
     "One must work here, not cuddle.",
     [(50, "На работе вы должны работать, а не обжиматься и ржать.")], "adapted"),
    ("kostya", "Мы просто спокойно разговаривали, Виктория Сергеевна.",
     "We were just calmly talking, Victoria Sergeevna.",
     [], "new"),
    ("vika", "У нас строго запрещены любые отношения!",
     "Any relationships are strictly forbidden here!",
     [(51, "Или вам напомнить, что у нас запрещены отношения?")], "adapted"),
    ("kostya", "Мы ничего плохого не сделали.",
     "We did nothing bad.",
     [(55, "Да мы ничего такого и не сделали.")], "adapted"),
    ("vika", "Быстро идите работать в зал.",
     "Quickly go work in the hall.",
     [(56, "Настя, быстро в зал.")], "adapted"),
    ("anya", "Вика, почему ты такая напряжённая?",
     "Vika, why are you so tense?",
     [(58, "Мне кажется, какая-то напряженная.")], "adapted"),
    ("vika", "У меня очень много сложных дел.",
     "I have very many difficult matters.",
     [], "new"),
    ("anya", "Пойдём сегодня вечером в классное место?",
     "Shall we go to an awesome place tonight?",
     [(59, "вечером мы с тобой идем в одно офигенное место?")], "adapted"),
    ("vika", "Макс, я слишком сильно устала.",
     "Max, I am too tired.",
     [(60, "Я как-то устала.")], "adapted"),
    ("anya", "Там ты отлично отдохнёшь со мной.",
     "There you will rest wonderfully with me.",
     [(60, "Ну, ты отдохнешь?")], "adapted"),
    ("vika", "Посмотрим, мне надо подумать об этом.",
     "We will see, I need to think about this.",
     [], "new"),
]

WALK = [
    (0, None,
     "'Nastya, quickly clear the fifth table!' -- Victoria gives a sharp order to the waitress."),
    (1, None,
     "'Have you completely lost your nerve at this job?' -- The administrator angrily scolds the staff."),
    (2, None,
     "'One must work here, not cuddle.' -- Victoria reminds everyone of professional boundaries."),
    (3, None,
     "'We were just calmly talking, Victoria Sergeevna.' -- Kostya attempts to de-escalate the tension politely."),
    (4, None,
     "'Any relationships are strictly forbidden here!' -- Victoria quotes the strict restaurant rule."),
    (5, None,
     "'We did nothing bad.' -- The bartender defends his harmless conversation."),
    (6, None,
     "'Quickly go work in the hall.' -- Victoria dismisses them back to their duties."),
    (7, None,
     "'Vika, why are you so tense?' -- Max notices her stress and asks with concern."),
    (8, None,
     "'I have very many difficult matters.' -- Victoria explains the heavy burden on her shoulders."),
    (9, None,
     "'Shall we go to an awesome place tonight?' -- The young cook proposes a romantic date."),
    (10, None,
     "'Max, I am too tired.' -- Victoria expresses her physical and mental exhaustion."),
    (11, None,
     "'There you will rest wonderfully with me.' -- Max promises a great time together."),
    (12, None,
     "'We will see, I need to think about this.' -- Victoria leaves the invitation open."),
]

TRANSITION = "Now let's listen to the dining hall exchange once again."

OUTRO = (
    "Leaving Victoria to finish her duties, Max hopes she will accept his invitation tonight, "
    "while Victoria tries to keep her focus on managing the busy restaurant."
)

CLOSING = ("vika", "Посмотрим, мне надо подумать об этом.")
