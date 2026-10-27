ID = "kukhnya-s02e01-scene-02"
SHOW = "kukhnya"
SEASON = 2
EPISODE = 1
SCENE = 2
TITLE = "Строгий приказ  (Strict Order)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "max": "anja", "sasha": "angelina"}
LABELS = {"anya": "Вика", "max": "Макс", "sasha": "Саша"}
SOURCE_NAME = "Кухня (Kukhnya) S2.01"
SOURCE_FILE = "sources/kukhnya/s02/e01.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 64-94. Max regrets his mistake with Sasha, and when Victoria arrives at the restaurant, "
    "she immediately fires Sasha and orders Max back to the kitchen."
)

INTRO = (
    "In the dining room of Claude Monet, Max tries to tell waitress Sasha that their previous evening "
    "was a mistake. Art director Victoria arrives, immediately fires Sasha on the spot, and coldly "
    "puts Max in his place. Let us listen to their confrontation in Russian first."
)

STORY = [
    ("sasha", "Привет, Макс, почему ты утром рано убежал?",
     "Hi, Max, why did you run away early in the morning?",
     [(66, "Ты так рано убежал с утра?")], "adapted"),
    ("max", "Мне надо было быстро поехать домой утром.",
     "I had to quickly go home in the morning.",
     [(67, "Да, мне надо было забежать домой.")], "adapted"),
    ("max", "Саша, вчера мы сделали очень большую ошибку.",
     "Sasha, yesterday we made a very big mistake.",
     [(68, "Переодеться. Слушай, Саша, мне кажется, мы вчера переборщили немного.")], "adapted"),
    ("sasha", "Не волнуйся, всё было просто очень хорошо.",
     "Do not worry, everything was simply very good.",
     [(69, "Да все нормально.")], "adapted"),
    ("anya", "Здравствуй, Саша, сегодня ты больше не работаешь.",
     "Hello, Sasha, today you no longer work here.",
     [(72, "Здрасте, Виктория Сергеевна. Здравствуй, до свидания.")], "adapted"),
    ("anya", "Ты уволена, собирай сразу все свои вещи.",
     "You are fired, pack all your things immediately.",
     [(73, "Ты уволена."), (74, "Можешь собрать вещи, завтра получишь расчет.")], "adapted"),
    ("sasha", "Простите, Виктория, за что вы меня уволили?",
     "Excuse me, Victoria, what did you fire me for?",
     [(75, "Простите, а за что?")], "adapted"),
    ("anya", "Завтра утром ты получишь все свои деньги.",
     "Tomorrow morning you will receive all your money.",
     [(74, "Можешь собрать вещи, завтра получишь расчет.")], "adapted"),
    ("max", "Вика, подожди, так нельзя поступать с людьми!",
     "Vika, wait, one cannot act like this with people!",
     [(77, "Вик, подожди, так нельзя. Во-первых, Виктория Сергеевна.")], "adapted"),
    ("anya", "Для тебя я теперь только Виктория Сергеевна.",
     "For you I am now only Victoria Sergeyevna.",
     [(77, "Вик, подожди, так нельзя. Во-первых, Виктория Сергеевна.")], "adapted"),
    ("anya", "А теперь иди на кухню и работай!",
     "And now go to the kitchen and work!",
     [(78, "А во-вторых, Лавров. Иди работай.")], "adapted"),
    ("max", "Пожалуйста, давай спокойно поговорим об этом вечером.",
     "Please, let us calmly talk about this in the evening.",
     [], "new"),
    ("anya", "Надеюсь, я всё очень понятно тебе объяснила!",
     "I hope I explained everything very clearly to you!",
     [(84, "Лавров, надеюсь, я все понятно объяснила.")], "adapted"),
]

OPENER = "Now let us examine Victoria's dismissal of Sasha line by line."

WALK = [
    (0, None,
     "'Hi, Max, why did you run away early in the morning?' -- Sasha greets Max and asks about his sudden departure."),
    (1, None,
     "'I had to quickly go home in the morning.' -- Max makes an excuse about needing to change clothes."),
    (2, None,
     "'Sasha, yesterday we made a very big mistake.' -- Max expresses deep regret over what happened the night before."),
    (3, None,
     "'Do not worry, everything was simply very good.' -- Sasha brushes off his concern and stays relaxed."),
    (4, None,
     "'Hello, Sasha, today you no longer work here.' -- Victoria enters and coldly announces Sasha's termination."),
    (5, None,
     "'You are fired, pack all your things immediately.' -- Victoria orders the waitress to leave the restaurant at once."),
    (6, None,
     "'Excuse me, Victoria, what did you fire me for?' -- Sasha asks for an official reason for being dismissed."),
    (7, None,
     "'Tomorrow morning you will receive all your money.' -- Victoria promises final severance pay instead of an explanation."),
    (8, None,
     "'Vika, wait, one cannot act like this with people!' -- Max steps in to defend Sasha from the sudden firing."),
    (9, None,
     "'For you I am now only Victoria Sergeyevna.' -- Victoria demands formal distance and rejects Max's familiarity."),
    (10, None,
     "'And now go to the kitchen and work!' -- Victoria orders Max back to his station immediately."),
    (11, None,
     "'Please, let us calmly talk about this in the evening.' -- Max pleads for a chance to explain himself later."),
    (12, None,
     "'I hope I explained everything very clearly to you!' -- Victoria cuts end to the discussion and walks away."),
]

TRANSITION = "Now let us listen to the entire confrontation once again."
OUTRO = (
    "Heartbroken and furious, Victoria fires Sasha on the spot and refuses to let Max speak "
    "to her informally, leaving their relationship in ruins."
)
CLOSING = ("anya", "Надеюсь, я всё очень понятно тебе объяснила!")
