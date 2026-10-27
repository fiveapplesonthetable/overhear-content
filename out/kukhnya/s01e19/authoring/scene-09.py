ID = "kukhnya-s01e19-scene-09"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 19
SCENE = 9
TITLE = "Возвращение поваров  (Return of the Cooks)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "shef": "anja"}
LABELS = {"anya": "Федя", "shef": "Шеф"}
SOURCE_NAME = "Кухня (Kukhnya) S1.19"
SOURCE_FILE = "sources/kukhnya/s01/e19.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 179-209. Viktor calls his fired cook Fedya to persuade him to return to Claude Monet, "
    "bluffing that Senya has already agreed to rejoin the kitchen staff."
)

INTRO = (
    "In his private office at Claude Monet, Chef Viktor is on the phone with Fedya. "
    "Desperate to assemble his original kitchen crew after their wrongful firing, Viktor tries to persuade Fedya to return. "
    "Let's listen to their phone call in Russian first."
)

OPENER = "Now let's examine the conversation line by line."

STORY = [
    ("shef", "Алло, Федя, привет!",
     "Hello, Fedya, hi!",
     [(182, "Алло, Федь, привет.")], "adapted"),
    ("anya", "Здравствуйте, шеф, как ваши дела?",
     "Hello, chef, how are you?",
     [(183, "Как дела? Эктор Петрович, приветствую.")], "adapted"),
    ("shef", "Федя, хватит ломать комедию.",
     "Fedya, quit acting.",
     [(194, "Биль, хватит ломать комедию.")], "adapted"),
    ("shef", "Возвращайся назад, ты мне очень нужен.",
     "Come back, I really need you.",
     [(195, "Возвращайся, ты мне нужен.")], "adapted"),
    ("anya", "Шеф, я не вернусь на кухню.",
     "Chef, I will not return to the kitchen.",
     [(196, "Шеф, знаете, скорее всего, нет.")], "adapted"),
    ("shef", "Я знаю, что я был виноват.",
     "I know that I was at fault.",
     [(198, "Я знаю, я виноват.")], "adapted"),
    ("shef", "Извини, но Сеня уже согласился вернуться.",
     "Sorry, but Senya has already agreed to return.",
     [(199, "Извини. Сеня с Лёвой уже согласились вернуться.")], "adapted"),
    ("anya", "Неужели Сеня правда согласился?",
     "Did Senya really agree?",
     [(200, "Да ладно, и Сеня?")], "adapted"),
    ("shef", "Сеня первый согласился на всё.",
     "Senya was the first to agree to everything.",
     [(200, "Сеня первый согласился.")], "adapted"),
    ("anya", "Тогда сделайте меня новым су-шефом.",
     "Then make me the new sous-chef.",
     [(202, "Вы сделаете меня су-шефом.")], "adapted"),
    ("shef", "Нет, никаких су-шефов, Федя.",
     "No, no sous-chefs, Fedya.",
     [(203, "Нет. Поднимите зарплату."), (204, "Нет.")], "adapted"),
    ("anya", "Хорошо, тогда я приду завтра утром.",
     "Fine, then I will come tomorrow morning.",
     [(205, "Ну ладно. Тогда завтра в десять.")], "adapted"),
    ("shef", "Жду тебя ровно в десять часов.",
     "I expect you at exactly ten o'clock.",
     [(205, "Тогда завтра в десять.")], "adapted"),
]

WALK = [
    (0, None,
     "'Hello, Fedya, hi!' -- Viktor opens the phone call warmly."),
    (1, None,
     "'Hello, chef, how are you?' -- Fedya answers with polite caution."),
    (2, None,
     "'Fedya, quit acting.' -- The chef cuts right through the excuses."),
    (3, None,
     "'Come back, I really need you.' -- Viktor honestly admits that he needs his skilled cook."),
    (4, None,
     "'Chef, I will not return to the kitchen.' -- Fedya plays hard to get."),
    (5, None,
     "'I know that I was at fault.' -- The chef swallows his pride and apologizes."),
    (6, None,
     "'Sorry, but Senya has already agreed to return.' -- Viktor uses clever peer pressure to persuade him."),
    (7, None,
     "'Did Senya really agree?' -- Fedya is surprised by his partner's swift decision."),
    (8, None,
     "'Senya was the first to agree to everything.' -- Viktor doubles down on his playful bluff."),
    (9, None,
     "'Then make me the new sous-chef.' -- Fedya tries to negotiate a promotion."),
    (10, None,
     "'No, no sous-chefs, Fedya.' -- The chef immediately shuts down the demand."),
    (11, None,
     "'Fine, then I will come tomorrow morning.' -- Fedya gives in and agrees to return to work."),
    (12, None,
     "'I expect you at exactly ten o'clock.' -- Viktor confirms the start time of the morning shift."),
]

TRANSITION = "Now let's listen to the phone negotiation once again without interruption."

OUTRO = (
    "With Fedya agreeing to return to Claude Monet, Viktor prepares his next call, "
    "ready to reunite his talented kitchen crew step by step."
)

CLOSING = ("shef", "Жду тебя ровно в десять часов.")
