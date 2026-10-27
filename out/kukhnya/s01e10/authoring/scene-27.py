ID = "kukhnya-s01e10-scene-27"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 10
SCENE = 27
TITLE = "В кабинете шефа  (In the Chef's Office)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "chef": "anja"}
LABELS = {"anya": "Макс", "chef": "Шеф"}
SOURCE_NAME = "Кухня (Kukhnya) S1.10"
SOURCE_FILE = "sources/kukhnya/s01/e10.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 189-201. Inside his office, Chef Viktor sternly confronts Max about Victoria's situation, "
    "warning him of her demanding family and forbidding him from fleeing back to Voronezh."
)

INTRO = (
    "Behind closed doors in his private office, Chef Viktor Petrovich confronts Max about "
    "Victoria. Drawing on his own painful past experience with her family, the veteran chef "
    "scolds the panicked young cook and strictly forbids him from running away to Voronezh. "
    "Let us listen to their heated exchange in Russian first."
)

STORY = [
    ("chef", "Вот это ты сильно попал, парень.",
     "Now you are in deep trouble, lad.",
     [(189, "Вот это ты попал")], "adapted"),
    ("anya", "Шеф, поверьте, так случайно получилось.",
     "Chef, believe me, it just happened accidentally.",
     [(192, "Шеф, так получилось")], "adapted"),
    ("chef", "Надо было заранее думать головой.",
     "You had to think with your head in advance.",
     [(190, "Надо было как-то думать")], "adapted"),
    ("anya", "Что же мне теперь делать?",
     "What am I to do now?",
     [], "new"),
    ("chef", "Их семья теперь не отстанет от тебя.",
     "Their family will not leave you alone now.",
     [(194, "Теперь они с тебя")], "adapted"),
    ("anya", "Вы так хорошо знаете эту семью?",
     "Do you know this family so well?",
     [], "new"),
    ("chef", "Я сам раньше жил в этой семье.",
     "I myself used to live in this family.",
     [(196, "в их семье"), (198, "О себе")], "adapted"),
    ("anya", "И они выгнали вас из дома?",
     "And did they drive you out of the house?",
     [(197, "Выжили")], "adapted"),
    ("chef", "Они забрали у меня все силы.",
     "They took all strength from me.",
     [(195, "Все соки выжмут")], "adapted"),
    ("anya", "Может, мне просто уехать в Воронеж?",
     "Maybe I should just leave for Voronezh?",
     [(199, "Может, обратно в Воронич свалить")], "adapted"),
    ("chef", "Никуда ты сейчас не поедешь.",
     "You will not go anywhere now.",
     [(200, "Я тебе свалю")], "adapted"),
    ("anya", "Но я очень боюсь такой ответственности.",
     "But I am very afraid of such responsibility.",
     [], "new"),
    ("chef", "Мужчина обязан отвечать за свои поступки.",
     "A man is obliged to answer for his actions.",
     [(201, "За свои поступки надо отвечать")], "adapted"),
]

OPENER = "Now let us examine Viktor's firm life lecture to Max line by line."

WALK = [
    (0, None,
     "'Now you are in deep trouble, lad.' -- Viktor bluntly tells Max that he is in a serious bind."),
    (1, None,
     "'Chef, believe me, it just happened accidentally.' -- The young man tries to plead that it was an accident."),
    (2, None,
     "'You had to think with your head in advance.' -- The head chef scolds the cook for lack of foresight."),
    (3, None,
     "'What am I to do now?' -- Max feels desperate and seeks guidance."),
    (4, None,
     "'Their family will not leave you alone now.' -- Viktor warns that Victoria's relatives are relentless."),
    (5, None,
     "'Do you know this family so well?' -- The young cook asks about Viktor's familiarity with them."),
    (6, None,
     "'I myself used to live in this family.' -- Viktor reveals his own past history as Victoria's former relative."),
    (7, None,
     "'And did they drive you out of the house?' -- Max asks if the family forced Viktor away."),
    (8, None,
     "'They took all strength from me.' -- The chef describes how they drained his vitality."),
    (9, None,
     "'Maybe I should just leave for Voronezh?' -- The panicked cook contemplates running away to his hometown."),
    (10, None,
     "'You will not go anywhere now.' -- Viktor strictly forbids him from fleeing his obligations."),
    (11, None,
     "'But I am very afraid of such responsibility.' -- Max confesses his fear of adult commitment."),
    (12, None,
     "'A man is obliged to answer for his actions.' -- The veteran chef demands maturity and accountability."),
]

TRANSITION = "Now let us listen to the serious conversation between Viktor and Max again."
OUTRO = (
    "Faced with Viktor's strict refusal to let him run away, Max realizes that he cannot "
    "escape his responsibilities and must confront whatever lies ahead."
)
CLOSING = ("chef", "Мужчина обязан отвечать за свои поступки.")
