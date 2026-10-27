ID = "kukhnya-s01e16-scene-08"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 16
SCENE = 8
TITLE = "Чей паштет лучше  (Whose Pâté is Better)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "kostya": "anja"}
LABELS = {"anya": "Макс", "kostya": "Костя"}
SOURCE_NAME = "Кухня (Kukhnya) S1.16"
SOURCE_FILE = "sources/kukhnya/s01/e16.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 58-61. Kostya tries to discuss the police inspection at Arcobaleno, "
    "but Max interrupts him to demand an honest answer on whose pâté is better."
)

INTRO = (
    "In the bar area of Claude Monet, Kostya tries to tell Max about the exciting raid at Arcobaleno. "
    "However, Max is obsessed with his ongoing culinary bet with Chef Viktor and refuses to discuss anything else. "
    "He forces Kostya to make a definitive comparison. Let us listen to their conversation in Russian first."
)

STORY = [
    ("kostya", "Макс, ты слышал важные новости сегодня?",
     "Max, did you hear important news today?",
     [(58, "А ты слышал про проверку ФМС в другом ресторане?")], "adapted"),
    ("anya", "Какие ещё новости могут волновать меня?",
     "What other news could worry me?",
     [], "new"),
    ("kostya", "В соседнем ресторане сейчас идёт большая проверка.",
     "A huge inspection is going on in the neighboring restaurant right now.",
     [(58, "в другом ресторане?")], "adapted"),
    ("anya", "Мне сейчас совсем не до чужих проверок.",
     "Right now I do not care at all about outside inspections.",
     [], "new"),
    ("kostya", "Там полиция проверяет всех работников кухни.",
     "The police are checking all kitchen workers over there.",
     [], "new"),
    ("anya", "Ответь честно, чей паштет сейчас лучше?",
     "Answer honestly, whose pâté is better right now?",
     [(59, "Чей паштет лучше, мой или шефа?")], "adapted"),
    ("kostya", "Ты обещаешь не обижаться на меня?",
     "Do you promise not to be offended with me?",
     [], "new"),
    ("anya", "Я хочу услышать только чистую правду.",
     "I want to hear only the pure truth.",
     [], "new"),
    ("kostya", "И ты точно не скажешь шефу?",
     "And you definitely will not tell the chef?",
     [(60, "А ты шефу не скажешь?")], "adapted"),
    ("anya", "Нет, я просто хочу знать результат.",
     "No, I simply want to know the result.",
     [(60, "Нет.")], "adapted"),
    ("kostya", "У шефа этот паштет намного лучше.",
     "The chef makes this pâté much better.",
     [(61, "У шефа лучше.")], "adapted"),
    ("anya", "Я обязательно найду его секретный ингредиент!",
     "I will definitely find his secret ingredient!",
     [], "new"),
    ("kostya", "Желаю тебе большой удачи в этом!",
     "I wish you great luck in that!",
     [], "new"),
]

OPENER = "Now let us examine Kostya and Max's candid conversation line by line."

WALK = [
    (0, None,
     "'Max, did you hear important news today?' -- Kostya brings up the developing situation with the neighboring raid."),
    (1, None,
     "'What other news could worry me?' -- Max brushes aside other topics, fixated entirely on his culinary contest."),
    (2, None,
     "'A huge inspection is going on in the neighboring restaurant right now.' -- Kostya shares the dramatic event next door."),
    (3, None,
     "'Right now I do not care at all about outside inspections.' -- Max dismisses the migration raid without interest."),
    (4, None,
     "'The police are checking all kitchen workers over there.' -- Kostya elaborates on the scale of the police action."),
    (5, None,
     "'Answer honestly, whose pâté is better right now?' -- Max steers the conversation back to his urgent priority."),
    (6, None,
     "'Do you promise not to be offended with me?' -- Kostya hedges before delivering a potentially hurtful opinion."),
    (7, None,
     "'I want to hear only the pure truth.' -- The determined cook demands straightforward and unvarnished feedback."),
    (8, None,
     "'And you definitely will not tell the chef?' -- The barman makes sure his honest review stays strictly confidential."),
    (9, None,
     "'No, I simply want to know the result.' -- Max reassures his friend that his query is purely professional."),
    (10, None,
     "'The chef makes this pâté much better.' -- Kostya bluntly crowns Viktor as the undisputed master of the recipe."),
    (11, None,
     "'I will definitely find his secret ingredient!' -- Undeterred by the defeat, Max resolves to solve the mystery."),
    (12, None,
     "'I wish you great luck in that!' -- Kostya offers a supportive goodbye as Max prepares for his next attempt."),
]

TRANSITION = "Now let us listen to Kostya and Max once again."
OUTRO = (
    "Although Kostya honestly confirms Chef Viktor's culinary superiority, "
    "Max remains determined to crack the secret recipe and win his two days off."
)
CLOSING = ("kostya", "Желаю тебе большой удачи в этом!")
