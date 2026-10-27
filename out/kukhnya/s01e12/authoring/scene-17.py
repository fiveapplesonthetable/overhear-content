ID = "kukhnya-s01e12-scene-17"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 12
SCENE = 17
TITLE = "Примирение у бара  (Reconciliation by the Bar)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "kostya": "anja"}
LABELS = {"anya": "Настя", "kostya": "Костя"}
SOURCE_NAME = "Кухня (Kukhnya) S1.12"
SOURCE_FILE = "sources/kukhnya/s01/e12.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 234-236. At the bar counter, Kostya apologizes sincerely to Nastya for their recent fight, "
    "and the couple happily reconciles."
)

INTRO = (
    "In a quiet corner near the bar counter, bartender Kostya approaches Nastya to resolve "
    "their recent spat. Regretting harsh words exchanged in the heat of an argument, Kostya "
    "delivers an earnest apology, eager to mend their romantic relationship. "
    "Let us listen to their heartfelt exchange in Russian first."
)

STORY = [
    ("kostya", "Настя, пожалуйста, перестань мучить меня.",
     "Nastya, please stop torturing me.",
     [(234, "Настя, хватит о меня мучить")], "adapted"),
    ("anya", "А почему ты сердишься на меня?",
     "And why are you angry with me?",
     [], "new"),
    ("kostya", "Мы с тобой поспорили из-за пустяка.",
     "You and I argued over a trifle.",
     [(235, "чтобы мы с тобой поругались")], "adapted"),
    ("anya", "Для меня этот вопрос был важным.",
     "For me this question was important.",
     [], "new"),
    ("kostya", "Ты сама хотела немного поспорить вчера.",
     "You yourself wanted to argue a bit yesterday.",
     [(235, "Ты же сама хотела")], "adapted"),
    ("anya", "Но я не хотела такой глупой обиды.",
     "But I did not want such a foolish offense.",
     [], "new"),
    ("kostya", "Извини меня, если я сильно обидел тебя.",
     "Forgive me if I hurt you badly.",
     [(236, "извини, если тебя по-настоящему обидел")], "adapted"),
    ("anya", "Ты действительно сожалеешь о своих словах?",
     "Do you really regret your words?",
     [], "new"),
    ("kostya", "Я очень искренне прошу у тебя прощения.",
     "I very sincerely ask your forgiveness.",
     [], "new"),
    ("anya", "Мне тоже очень тяжело злиться долго.",
     "It is also very hard for me to stay angry long.",
     [], "new"),
    ("kostya", "Давай забудем этот спор прямо сейчас.",
     "Let us forget this argument right now.",
     [], "new"),
    ("anya", "Хорошо, я согласна помириться с тобой.",
     "Good, I agree to make peace with you.",
     [], "new"),
    ("kostya", "Ты самая добрая и красивая девушка.",
     "You are the kindest and most beautiful girl.",
     [], "new"),
]

OPENER = "Now let us examine Kostya and Nastya's tender reconciliation line by line."

WALK = [
    (0, None,
     "'Nastya, please stop torturing me.' -- Kostya begs his girlfriend to end the emotional silence."),
    (1, None,
     "'And why are you angry with me?' -- Nastya asks why he is resentful toward her."),
    (2, None,
     "'You and I argued over a trifle.' -- The bartender minimizes the silly cause of their argument."),
    (3, None,
     "'For me this question was important.' -- The young waitress insists that principle mattered to her."),
    (4, None,
     "'You yourself wanted to argue a bit yesterday.' -- Kostya reminds her that she started the playful debate."),
    (5, None,
     "'But I did not want such a foolish offense.' -- Nastya confesses that feelings were hurt unnecessarily."),
    (6, None,
     "'Forgive me if I hurt you badly.' -- The young man offers an apology for any hurtful remarks."),
    (7, None,
     "'Do you really regret your words?' -- Nastya asks for verification of his true feelings."),
    (8, None,
     "'I very sincerely ask your forgiveness.' -- Kostya emphasizes the genuine depth of his apology."),
    (9, None,
     "'It is also very hard for me to stay angry long.' -- Nastya admits that resentment hurts her as well."),
    (10, None,
     "'Let us forget this argument right now.' -- Kostya proposes putting the whole unpleasant matter behind them."),
    (11, None,
     "'Good, I agree to make peace with you.' -- The smiling waitress accepts his olive branch."),
    (12, None,
     "'You are the kindest and most beautiful girl.' -- Kostya showers his girlfriend with affectionate compliments."),
]

TRANSITION = "Now let us listen to the sweet reconciliation by the bar counter once more."
OUTRO = (
    "With heartfelt apologies accepted and tender affection restored, Kostya and Nastya "
    "happily put their minor misunderstanding behind them."
)
CLOSING = ("kostya", "Ты самая добрая и красивая девушка.")
