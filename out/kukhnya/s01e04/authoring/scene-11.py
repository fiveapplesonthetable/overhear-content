"""s01e04 scene 11: Девчонки любят смелых (Girls Like a Guy with Guts)."""

ID = "kukhnya-s01e04-scene-11"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 4
SCENE = 11
TITLE = "Девчонки любят смелых  (Girls Like a Guy with Guts)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "kostya": "anja"}
LABELS = {"anya": "Макс", "kostya": "Костя"}
SOURCE_NAME = "Кухня (Kukhnya) S1.04"
SOURCE_FILE = "sources/kukhnya/s01/e04.ru.dual.srt"
SOURCE_NOTE = "Cue 145. Bartender Kostya encourages Max to take the initiative with Vika."

INTRO = (
    "Near the dining room entrance, novice cook Max hesitates anxiously, uncertain whether to approach glamorous art director Vika. "
    "Bartender Kostya notices his hesitation and offers encouraging romantic advice, urging Max to take the initiative with confidence. "
    "Let's listen to their conversation in Russian first."
)

STORY = [
    ("kostya", "Опять смотришь на неё издалека?",
     "Watching her from afar again?",
     [], "observing Max's longing glance"),
    ("anya", "Она кажется такой недоступной сегодня.",
     "She seems so unapproachable today.",
     [], "feeling intimidated"),
    ("kostya", "Хватит стоять и просто смотреть.",
     "Stop standing and merely watching.",
     [], "prodding him to action"),
    ("anya", "А что мне делать, Костя?",
     "And what should I do, Kostya?",
     [], "seeking advice"),
    ("kostya", "Прояви инициативу прямо сейчас!",
     "Take the initiative right now!",
     [(145, "Прояви инициативу")], "giving direct counsel"),
    ("anya", "Думаешь, это хорошая идея?",
     "Do you think that is a good idea?",
     [], "doubting himself"),
    ("kostya", "Девчонки любят смелых парней.",
     "Girls like brave guys.",
     [(145, "Девчонки любят смелых")], "sharing a romantic maxim"),
    ("anya", "А если она прогонит меня?",
     "And what if she sends me away?",
     [], "fearing rejection"),
    ("kostya", "Тогда ты хотя бы попробовал.",
     "Then at least you tried.",
     [], "encouraging bravery"),
    ("anya", "Ты прав, нельзя вечно бояться.",
     "You are right, one cannot be afraid forever.",
     [], "accepting the logic"),
    ("kostya", "Подойди и уверенно заговори с ней.",
     "Walk over and talk with her confidently.",
     [], "coaching the approach"),
    ("anya", "Спасибо за совет, я сделаю это!",
     "Thanks for the advice, I will do it!",
     [], "resolving to act"),
    ("kostya", "Удачи, друг, покажи свою смелость.",
     "Good luck, my friend, show your courage.",
     [], "wishing him success"),
]

OPENER = "Let's replay a few lines to examine key phrases and vocabulary."

WALK = [
    (1, "Она кажется такой недоступной сегодня.",
     "'She seems so unapproachable today,' Max confides, admiring Vika from across the dining room."),
    (4, "Прояви инициативу прямо сейчас!",
     "'Take the initiative right now!' Kostya urges, using the imperative form to motivate his friend."),
    (6, "Девчонки любят смелых парней.",
     "'Girls like brave guys,' the bartender declares, quoting the popular romantic maxim."),
    (11, "Спасибо за совет, я сделаю это!",
     "'Thanks for the advice, I will do it!' Max resolves, gathering up his courage to approach Vika."),
]

TRANSITION = "Now listen to the full hallway conversation once more."

OUTRO = "Max takes a deep breath and prepares to walk toward Vika."

CLOSING = ("anya", "Настало время действовать решительно.")
