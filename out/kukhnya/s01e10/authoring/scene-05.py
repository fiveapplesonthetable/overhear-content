ID = "kukhnya-s01e10-scene-05"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 10
SCENE = 5
TITLE = "Неожиданное признание  (An Unexpected Confession)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "chef": "anja"}
LABELS = {"anya": "Макс", "chef": "Шеф"}
SOURCE_NAME = "Кухня (Kukhnya) S1.10"
SOURCE_FILE = "sources/kukhnya/s01/e10.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 21-25. At the bar, Max greets a grim Chef Barinov, who stuns him with the news "
    "that Victoria confessed she loves him."
)

INTRO = (
    "At the Claude Monet bar counter, junior cook Max notices Chef Viktor Barinov sitting gloomily with a dark "
    "expression. When Max asks what went wrong, expecting another complaint about football or hangovers, Barinov "
    "abruptly shocks him by revealing a secret about Victoria's feelings. Let's listen to their conversation in Russian first."
)

STORY = [
    ("anya", "Здравствуйте, шеф, как ваши дела сегодня?",
     "Hello, chef, how are your affairs today?",
     [(21, "Здрасте.")], "adapted"),
    ("chef", "Макс, не задавай мне глупых вопросов.",
     "Max, do not ask me foolish questions.",
     [], "new"),
    ("anya", "Вы опять проиграли деньги на ставках?",
     "Did you lose money on bets again?",
     [(22, "Опять проигрался?")], "adapted"),
    ("chef", "Я бы сейчас с удовольствием выпил водки.",
     "I would gladly drink vodka right now.",
     [(23, "Да я бы водки хлебнул.")], "adapted"),
    ("anya", "Что ещё неприятного у вас случилось?",
     "What else unpleasant has happened to you?",
     [(24, "Что случилось?")], "adapted"),
    ("chef", "Дело вовсе не в моих ставках.",
     "The matter is not at all about my bets.",
     [], "new"),
    ("anya", "А в чём тогда настоящая проблема?",
     "Then what is the real problem?",
     [], "new"),
    ("chef", "У меня есть для тебя важная новость.",
     "I have important news for you.",
     [], "new"),
    ("anya", "Какая новость, шеф, говорите скорее.",
     "What news, chef, tell me quickly.",
     [], "new"),
    ("chef", "Тётя Вика сказала, что любит тебя.",
     "Aunt Vika said that she loves you.",
     [(25, "А тетя Вика сказала, что любит тебя.")], "adapted"),
    ("anya", "Что? Этого просто не может быть!",
     "What? That simply cannot be!",
     [], "new"),
    ("chef", "Она сама призналась мне в этом.",
     "She herself confessed this to me.",
     [], "new"),
    ("anya", "Шеф, вы точно не шутите сейчас?",
     "Chef, are you definitely not joking right now?",
     [], "new"),
]

OPENER = "Now let's examine this startling revelation from Barinov line by line."

WALK = [
    (0, None,
     "'Hello, chef, how are your affairs today?' -- Max greets his boss cordially at the counter."),
    (1, None,
     "'Max, do not ask me foolish questions.' -- The irritated chef rebuffs his casual pleasantries."),
    (2, None,
     "'Did you lose money on bets again?' -- Max attempts to diagnose the chef's sour mood."),
    (3, None,
     "'I would gladly drink vodka right now.' -- Barinov expresses a strong wish for hard liquor."),
    (4, None,
     "'What else unpleasant has happened to you?' -- The young cook asks about additional troubles."),
    (5, None,
     "'The matter is not at all about my bets.' -- The chef clarifies that sports betting is not the source."),
    (6, None,
     "'Then what is the real problem?' -- Max probes deeper into the unexpected dilemma."),
    (7, None,
     "'I have important news for you.' -- Barinov announces that he carries crucial personal information."),
    (8, None,
     "'What news, chef, tell me quickly.' -- Max urges him impatiently to disclose the announcement."),
    (9, None,
     "'Aunt Vika said that she loves you.' -- Barinov drops the shocking revelation about Victoria's feelings."),
    (10, None,
     "'What? That simply cannot be!' -- Stunned, Max refuses to believe what he has just heard."),
    (11, None,
     "'She herself confessed this to me.' -- The chef confirms the direct authenticity of her confession."),
    (12, None,
     "'Chef, are you definitely not joking right now?' -- Max checks anxiously whether Barinov is playing a prank."),
]

TRANSITION = "Now let's listen to the bar conversation again without interruption."
OUTRO = (
    "Leaving Max in absolute disbelief and questioning everything about his future with Victoria, "
    "Chef Barinov watches his bewildered expression with grim amusement."
)
CLOSING = ("anya", "Шеф, вы точно не шутите сейчас?")
