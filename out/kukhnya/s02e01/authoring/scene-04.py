ID = "kukhnya-s02e01-scene-04"
SHOW = "kukhnya"
SEASON = 2
EPISODE = 1
SCENE = 4
TITLE = "Плохие новости  (Bad News)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "sasha": "anja", "kostya": "angelina"}
LABELS = {"anya": "Кристина", "sasha": "Саша", "kostya": "Костя"}
SOURCE_NAME = "Кухня (Kukhnya) S2.01"
SOURCE_FILE = "sources/kukhnya/s02/e01.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 96-102. Sasha asks Kristina to intervene with Dmitry Nagiyev after Victoria fires her, "
    "but Kristina reveals that she and Dmitry are getting a divorce."
)

INTRO = (
    "Near the bar at Claude Monet, waitress Sasha runs into Kristina and begs her to ask her husband "
    "Dmitry Nagiyev to overturn Victoria's firing. Kristina reveals shocking news of her own and orders "
    "a drink from Kostya. Let us listen to their conversation in Russian first."
)

STORY = [
    ("sasha", "Кристина, привет, я хотела позвонить тебе сегодня.",
     "Kristina, hi, I wanted to call you today.",
     [(96, "Крис, привет. Я уже собралась тебе звонить.")], "adapted"),
    ("anya", "Привет, Саша, что у тебя сейчас случилось?",
     "Hi, Sasha, what happened with you right now?",
     [], "new"),
    ("sasha", "Представляешь, Виктория только что меня зло уволила!",
     "Can you imagine, Victoria just angrily fired me!",
     [(97, "Слушай, эта сучка меня уволила, представляешь?")], "adapted"),
    ("anya", "Почему она вдруг решила уволить тебя сегодня?",
     "Why did she suddenly decide to fire you today?",
     [], "new"),
    ("sasha", "Она очень злится из-за глупой ошибки вчера.",
     "She is very angry because of a foolish mistake yesterday.",
     [], "new"),
    ("sasha", "Ты можешь поговорить со своим мужем Димой?",
     "Can you talk with your husband Dima?",
     [(98, "Ты это, не могла бы там, ну, как-то поговорить с Димой?")], "adapted"),
    ("sasha", "Пусть он поможет мне вернуться в ресторан.",
     "Let him help me return to the restaurant.",
     [], "new"),
    ("anya", "Саша, извини, но у меня не получится.",
     "Sasha, sorry, however I will not be able to.",
     [(99, "Сашуль, извини, не получится.")], "adapted"),
    ("sasha", "Но почему ты не можешь попросить Диму?",
     "But why can you not ask Dima?",
     [], "new"),
    ("anya", "Потому что мы с Димой скоро разводимся.",
     "Because Dima and I are getting divorced soon.",
     [(100, "Мы с Димой разводимся.")], "adapted"),
    ("sasha", "Какой ужас, я совсем не знала этого!",
     "How terrible, I did not know that at all!",
     [], "new"),
    ("anya", "Костя, налей мне быстро бокал хорошего вина!",
     "Kostya, quickly pour me a glass of good wine!",
     [(101, "Костя."), (102, "Налей мне быстро. Момент.")], "adapted"),
    ("kostya", "Один момент, сейчас я налью вам вино.",
     "One moment, right now I will pour you wine.",
     [(102, "Налей мне быстро. Момент.")], "adapted"),
]

OPENER = "Now let us examine Sasha and Kristina's conversation line by line."

WALK = [
    (0, None,
     "'Kristina, hi, I wanted to call you today.' -- Sasha greets her friend Kristina with urgency."),
    (1, None,
     "'Hi, Sasha, what happened with you right now?' -- Kristina notices that Sasha looks upset."),
    (2, None,
     "'Can you imagine, Victoria just angrily fired me!' -- Sasha shares the news of her sudden dismissal."),
    (3, None,
     "'Why did she suddenly decide to fire you today?' -- Kristina asks for the reason behind the firing."),
    (4, None,
     "'She is very angry because of a foolish mistake yesterday.' -- Sasha admits that personal drama caused the trouble."),
    (5, None,
     "'Can you talk with your husband Dima?' -- Sasha asks Kristina to use her influence with Nagiyev."),
    (6, None,
     "'Let him help me return to the restaurant.' -- Sasha hopes the owner can reinstate her job."),
    (7, None,
     "'Sasha, sorry, however I will not be able to.' -- Kristina apologizes and turns down the request."),
    (8, None,
     "'But why can you not ask Dima?' -- Sasha is surprised that Kristina cannot speak to her husband."),
    (9, None,
     "'Because Dima and I are getting divorced soon.' -- Kristina reveals that her marriage is ending."),
    (10, None,
     "'How terrible, I did not know that at all!' -- Sasha expresses shock at the sudden divorce news."),
    (11, None,
     "'Kostya, quickly pour me a glass of good wine!' -- Stressed by the situation, Kristina orders a drink at the bar."),
    (12, None,
     "'One moment, right now I will pour you wine.' -- Bartender Kostya immediately attends to her order."),
]

TRANSITION = "Now let us listen to the entire scene once again."
OUTRO = (
    "Hoping for help after losing her job, Sasha learns that Kristina is divorcing Dmitry Nagiyev "
    "and can no longer pull strings at Claude Monet."
)
CLOSING = ("kostya", "Один момент, сейчас я налью вам вино.")
