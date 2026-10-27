"""s01e01 scene 11: В поисках укрытия (Looking for Cover)."""

ID = "kukhnya-s01e01-scene-11"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 1
SCENE = 11
TITLE = "В поисках укрытия  (Looking for Cover)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "ilya": "anja"}
LABELS = {"anya": "Макс", "ilya": "Илья"}
SOURCE_NAME = "Кухня (Kukhnya) S1.01"
SOURCE_FILE = "sources/kukhnya/s01/e01.ru.dual.srt"
SOURCE_NOTE = "Cue 74. Max hides behind a pillar with an upside-down menu and is directed to the bar."

INTRO = (
    "Desperate to avoid being seen by Vika before his job interview, Max dives behind a marble pillar in the Claude Monet dining room. "
    "Holding a large menu upside down to mask his face, he attracts the curious attention of a busy waiter who politely intervenes. "
    "Let's listen to the scene in Russian first."
)

STORY = [
    ("ilya", "Молодой человек, вам помочь?",
     "Young man, can I help you?",
     [], "approaching the suspicious customer"),
    ("anya", "Нет, спасибо, я просто читаю меню.",
     "No, thank you, I am simply reading the menu.",
     [], "pretending to browse"),
    ("ilya", "Но вы держите меню вверх ногами.",
     "But you are holding the menu upside down.",
     [], "pointing out the obvious flaw"),
    ("anya", "Правда? Я изучаю оригинальный дизайн.",
     "Really? I am studying the original design.",
     [], "making an absurd excuse"),
    ("ilya", "Вы кого-то боитесь в зале?",
     "Are you afraid of someone in the dining hall?",
     [], "guessing his true motive"),
    ("anya", "Вовсе нет, я жду хозяина ресторана.",
     "Not at all, I am waiting for the restaurant owner.",
     [], "denying his fear"),
    ("ilya", "Хозяин точно не стоит за этой колонной.",
     "The owner definitely is not standing behind this pillar.",
     [], "stating the obvious fact"),
    ("anya", "Я понимаю, я просто отдыхаю здесь.",
     "I understand, I am simply resting here.",
     [], "trying to stay put"),
    ("ilya", "Пожалуйста, не загораживайте проход официантам.",
     "Please do not block the walkway for the waiters.",
     [], "asking him to clear the aisle"),
    ("anya", "О нет, я не хочу никому мешать!",
     "Oh no, I do not want to disturb anyone!",
     [(74, "Дерьмо")], "apologizing for blocking traffic"),
    ("ilya", "Вы можете подождать за барной стойкой.",
     "You can wait at the bar counter.",
     [], "offering a practical alternative"),
    ("anya", "Отличная идея, я пойду в бар!",
     "Great idea, I will go to the bar!",
     [], "accepting the safe haven"),
    ("ilya", "Бармен нальёт вам отличный напиток.",
     "The bartender will pour you an excellent drink.",
     [], "encouraging him toward the bar"),
]

OPENER = "Let's replay a few lines to examine key phrases and grammar."

WALK = [
    (2, "Но вы держите меню вверх ногами.",
     "'But you are holding the menu upside down,' Ilya remarks with amusement, using the idiom meaning upside down."),
    (6, "Хозяин точно не стоит за этой колонной.",
     "'The owner definitely is not standing behind this pillar,' the waiter observes dryly."),
    (10, "Вы можете подождать за барной стойкой.",
     "'You can wait at the bar counter,' Ilya suggests, pointing him away from the busy service lane."),
    (11, "Отличная идея, я пойду в бар!",
     "'Great idea, I will go to the bar!' Max agrees enthusiastically, relieved to find a safe refuge."),
]

TRANSITION = "Now listen to the full dining room dialogue once more."

OUTRO = "Max ducks away and heads toward the bar counter."

CLOSING = ("anya", "Бар — это самое безопасное место.")
