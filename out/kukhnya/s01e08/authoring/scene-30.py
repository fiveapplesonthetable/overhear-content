"""Scene 30 — The Illusion of Control (s01e08, 00:21:10–00:21:21)."""

ID = "kukhnya-s01e08-scene-30"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 8
SCENE = 30
TITLE = "Иллюзия контроля  (The Illusion of Control)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Кухня (Kukhnya) S1.08"
SOURCE_FILE = "sources/kukhnya/s01/e08.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 357-358. Max reflects on the inevitability of human errors and the illusion of total control, "
    "while Chef Barinov stubbornly claims he orchestrated every chaotic event."
)

VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "chef": "anja",
}

LABELS = {
    "anya": "Макс",
    "chef": "Шеф",
}

INTRO = (
    "Watching Chef Barinov pour himself a victory drink in his office, "
    "Max reflects on how human beings dread making mistakes yet commit them continuously. "
    "When Max challenges the head chef's inflated pride, Barinov insists that the kitchen's chaos "
    "was part of his grand master plan all along. "
    "Let's listen to their conversation in Russian first."
)

STORY = [
    ("anya", "Шеф, люди очень не любят делать ошибки.",
     "Chef, people really do not like making mistakes.",
     [(357, "Люди не любят делать ошибки")], "Max opens on mistakes"),

    ("anya", "Но тем не менее постоянно их совершают.",
     "Yet nevertheless constantly make them.",
     [(357, "но тем не менее постоянно их совершают.")], "Max notes inevitability"),

    ("chef", "Макс, умные повара вообще не ошибаются.",
     "Max, smart cooks do not make mistakes at all.",
     [], "Barinov claims perfection"),

    ("anya", "Вы думаете, что контролируете абсолютно всё?",
     "You think that you control absolutely everything?",
     [], "Max questions control"),

    ("chef", "Конечно, на моей кухне всегда идеальный порядок!",
     "Of course, in my kitchen there is always perfect order!",
     [], "Barinov boasts authority"),

    ("anya", "Одни заблуждаются, что могут всё контролировать.",
     "Some fool themselves into thinking they can control everything.",
     [(358, "Одни заблуждаются, что могут все контролировать.")], "Max reflects on illusion"),

    ("chef", "Я выиграл пари и доказал свою правоту.",
     "I won the bet and proved I was right.",
     [], "Barinov points to wager"),

    ("anya", "Но повара сегодня устроили настоящий кошмар.",
     "But the cooks caused a real nightmare today.",
     [], "Max recalls kitchen mess"),

    ("chef", "Они точно выполнили мой секретный план!",
     "They accurately carried out my secret plan!",
     [], "Barinov claims orchestration"),

    ("anya", "Иногда наши победы бывают слишком странными.",
     "Sometimes our victories turn out too strange.",
     [], "Max observes irony"),

    ("chef", "Главное, что победа осталась за мной!",
     "The main thing is that victory remained mine!",
     [], "Barinov savors triumph"),

    ("anya", "Самоуверенность часто приводит к неожиданным проблемам.",
     "Overconfidence often leads to unexpected problems.",
     [], "Max warns of pride"),

    ("chef", "Иди работай и не умничай здесь!",
     "Go work and do not be a smart-aleck here!",
     [], "Barinov cuts Max off"),
]

OPENER = "Now let's examine Max and Barinov's philosophical exchange line by line."

WALK = [
    (0, None,
     "'Chef, people really do not like making mistakes.' As Max begins his philosophical contemplation about human imperfection."),
    (1, None,
     "'Yet nevertheless constantly make them.' The rookie notes the inescapable nature of daily blunders."),
    (2, None,
     "'Max, smart cooks do not make mistakes at all.' Barinov pompously claims absolute immunity to errors."),
    (3, None,
     "'You think that you control absolutely everything?' Max gently challenges the chef's inflated sense of mastery."),
    (4, None,
     "'Of course, in my kitchen there is always perfect order!' Viktor proudly insists that his authority remains supreme."),
    (5, None,
     "'Some fool themselves into thinking they can control everything.' Max reflects on the classic illusion of total domination."),
    (6, None,
     "'I won the bet and proved I was right.' The head chef clings stubbornly to his victory over Elena."),
    (7, None,
     "'But the cooks caused a real nightmare today.' Max points to the chaotic kitchen sabotage earlier that evening."),
    (8, None,
     "'They accurately carried out my secret plan!' Barinov spins the kitchen breakdown as deliberate tactical genius."),
    (9, None,
     "'Sometimes our victories turn out too strange.' The young cook remains skeptical of the Pyrrhic triumph."),
    (10, None,
     "'The main thing is that victory remained mine!' Viktor dismisses any doubt and relishes his winning position."),
    (11, None,
     "'Overconfidence often leads to unexpected problems.' Max warns about the perils of excessive professional pride."),
    (12, None,
     "'Go work and do not be a smart-aleck here!' Barinov brusquely shooes the rookie back to his cooking station."),
]

TRANSITION = "Now let's listen to Max and the chef once more without interruption."

OUTRO = (
    "Max's reflections on human errors reveal that even master chefs are blinded by the illusion of control."
)

CLOSING = ("chef", "Иди работай и не умничай здесь!")
