"""Scene 24 — The Coward and the Firing (s01e11, 00:21:04–00:21:25)."""

ID = "kukhnya-s01e11-scene-24"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 11
SCENE = 24
TITLE = "Трус и увольнение  (The Coward and the Firing)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Кухня (Kukhnya) S1.11"
SOURCE_FILE = "sources/kukhnya/s01/e11.ru.dual.srt"

VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "kostya": "anja",
    "chef": "angelina",
}

LABELS = {
    "anya": "Настя",
    "kostya": "Костя",
    "chef": "Шеф",
}

INTRO = (
    "Following the disastrous confrontation with the restaurant critic, Nastya rushes to apologize to Kostya for calling him a coward. "
    "Before they can reconcile, Chef Barinov storms into the dining hall and abruptly fires the young bartender."
)

STORY = [
    ("anya", "Костя, подожди секунду, выслушай меня пожалуйста.",
     "Kostya, wait a second, listen to me please.",
     [], "Nastya stops him"),

    ("anya", "Прости, что я глупо назвала тебя трусом.",
     "Forgive me for stupidly calling you a coward.",
     [(312, "Прости, что назвала тебя трусом.")], "Nastya apologizes"),

    ("kostya", "Ты поступила со мной очень несправедливо.",
     "You treated me very unfairly.",
     [], "Kostya replies hurt"),

    ("anya", "Я сильно ошиблась и очень сожалею об этом.",
     "I was very mistaken and deeply regret it.",
     [], "Nastya expresses regret"),

    ("chef", "Костя, ты уволен, быстро собирай свои вещи!",
     "Kostya, you are fired, quickly pack your things!",
     [(313, "Костя, ты уволец, собирай вещи.")], "Chef fires Kostya"),

    ("kostya", "Шеф, неужели вы выгоняете меня с работы?",
     "Chef, are you really driving me out of work?",
     [], "Kostya gasps"),

    ("chef", "Ты устроил скандал с важным ресторанным критиком!",
     "You caused a scandal with an important restaurant critic!",
     [], "Chef rages"),

    ("anya", "Шеф, это я во всём виновата!",
     "Chef, it is I who am to blame for everything!",
     [], "Nastya defends him"),

    ("chef", "Мне всё равно, бармен уходит прямо сейчас.",
     "I do not care, the bartender leaves right now.",
     [], "Chef is resolute"),

    ("kostya", "Хорошо, шеф, я сейчас же сниму форму.",
     "All right, chef, I will take off the uniform immediately.",
     [], "Kostya complies sadly"),

    ("anya", "Мы не можем потерять лучшего бармена ресторана.",
     "We cannot lose the restaurant's best bartender.",
     [], "Nastya argues"),

    ("chef", "У нашего ресторана сейчас будут огромные проблемы.",
     "Our restaurant will have huge problems now.",
     [(319, "Я думаю, у нас большие проблемы.")], "Chef worries about review"),

    ("anya", "Мы должны всё исправить до выхода статьи.",
     "We must fix everything before the article comes out.",
     [], "Nastya insists"),
]

OPENER = "Let's witness Nastya's sincere apology and Barinov's ruthless dismissal of Kostya following the critic scandal."

WALK = [
    (0, None,
     "'Kostya, wait a second, listen to me please.' Nastya catches up with the despondent bartender."),
    (1, None,
     "'Forgive me for stupidly calling you a coward.' She regrets her harsh words deeply."),
    (2, None,
     "'You treated me very unfairly.' Kostya responds with wounded pride."),
    (3, None,
     "'I was very mistaken and deeply regret it.' Nastya tries earnestly to make amends."),
    (4, None,
     "'Kostya, you are fired, quickly pack your things!' Barinov shouts ruthlessly across the dining room."),
    (5, None,
     "'Chef, are you really driving me out of work?' Kostya is stunned by the sudden termination."),
    (6, None,
     "'You caused a scandal with an important restaurant critic!' Barinov blames him for the disaster."),
    (7, None,
     "'Chef, it is I who am to blame for everything!' Nastya steps in bravely to protect Kostya."),
    (8, None,
     "'I do not care, the bartender leaves right now.' Barinov refuses to hear any defense."),
    (9, None,
     "'All right, chef, I will take off the uniform immediately.' Kostya accepts his fate with dignity."),
    (10, None,
     "'We cannot lose the restaurant's best bartender.' Nastya desperately appeals for fairness."),
    (11, None,
     "'Our restaurant will have huge problems now.' Barinov fears the pending newspaper review."),
    (12, None,
     "'We must fix everything before the article comes out.' Nastya vows to undo the damage."),
]

TRANSITION = "Now let's listen to the emotional breakup, dismissal, and rising tension once more."

OUTRO = "Dismissed by an unforgiving Barinov, Kostya leaves the restaurant while Nastya searches for a way to save him."

CLOSING = ("anya", "Мы должны всё исправить до выхода статьи.")
