ID = "kukhnya-s01e10-scene-02"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 10
SCENE = 2
TITLE = "Утренний рассол  (Morning Brine)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "chef": "anja"}
LABELS = {"anya": "Сеня", "chef": "Шеф"}
SOURCE_NAME = "Кухня (Kukhnya) S1.10"
SOURCE_FILE = "sources/kukhnya/s01/e10.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 4-5. In the kitchen, line cook Senya brings Chef Barinov cold pickle brine "
    "to relieve his severe morning hangover."
)

INTRO = (
    "Early in the morning in the kitchen of Claude Monet, Chef Viktor Barinov is suffering from an agonizing headache "
    "after an exhausting night. Seeing his boss in distress, line cook Senya rushes over with the ultimate "
    "traditional remedy: a cold glass of pickle brine. Let's listen to their short kitchen exchange in Russian first."
)

STORY = [
    ("anya", "Шеф, как ваше здоровье сегодня утром?",
     "Chef, how is your health this morning?",
     [(4, "Шеф!")], "adapted"),
    ("chef", "Сеня, отойди, у меня болит голова.",
     "Senya, step back, my head hurts.",
     [], "new"),
    ("anya", "Я принёс вам холодный свежий рассол.",
     "I brought you cold fresh brine.",
     [(5, "Рассольчик!")], "adapted"),
    ("chef", "О, Сеня, ты настоящий верный друг.",
     "Oh, Senya, you are a true loyal friend.",
     [], "new"),
    ("anya", "Выпей немного, сразу станет гораздо легче.",
     "Drink a little, it will immediately become much easier.",
     [], "new"),
    ("chef", "Этот напиток очень помогает мне.",
     "This drink helps me very much.",
     [], "new"),
    ("anya", "Вчера Спартак снова проиграл важный матч?",
     "Did Spartak lose an important match again yesterday?",
     [], "new"),
    ("chef", "Не говори мне про этот кошмар.",
     "Do not talk to me about that nightmare.",
     [], "new"),
    ("anya", "Понятно, шеф, больше никаких лишних слов.",
     "Understood, chef, no more unnecessary words.",
     [], "new"),
    ("chef", "Принеси мне ещё один стакан рассола.",
     "Bring me one more glass of brine.",
     [], "new"),
    ("anya", "Сейчас быстро принесу из нашей кухни.",
     "I will quickly bring it now from our kitchen.",
     [], "new"),
    ("chef", "И начинайте готовить обед для гостей.",
     "And begin preparing lunch for the guests.",
     [], "new"),
    ("anya", "Всё будет готово вовремя, шеф.",
     "Everything will be ready on time, chef.",
     [], "new"),
]

OPENER = "Now let's examine the morning hangover remedy line by line."

WALK = [
    (0, None,
     "'Chef, how is your health this morning?' -- Senya inquires respectfully about the chef's well-being."),
    (1, None,
     "'Senya, step back, my head hurts.' -- Barinov complains of a severe morning headache."),
    (2, None,
     "'I brought you cold fresh brine.' -- The cook presents the classic cold pickle brine remedy."),
    (3, None,
     "'Oh, Senya, you are a true loyal friend.' -- The relieved chef thanks him warmly for the thoughtful rescue."),
    (4, None,
     "'Drink a little, it will immediately become much easier.' -- Senya recommends drinking to speed recovery."),
    (5, None,
     "'This drink helps me very much.' -- Barinov praises the revitalizing effect of the cold liquid."),
    (6, None,
     "'Did Spartak lose an important match again yesterday?' -- Senya carefully mentions the football match defeat."),
    (7, None,
     "'Do not remind me about that nightmare.' -- The chef groans and forbids any further talk of the game."),
    (8, None,
     "'Understood, chef, no more unnecessary words.' -- Senya prudently promises complete silence on the matter."),
    (9, None,
     "'Bring me one more glass of brine.' -- The chef requests a second refreshing serving of brine."),
    (10, None,
     "'I will quickly bring it now from our kitchen.' -- The cook runs to fetch the second glass immediately."),
    (11, None,
     "'And begin preparing lunch for the guests.' -- Barinov reminds the line cooks of lunch preparations."),
    (12, None,
     "'Everything will be ready on time, chef.' -- Senya assures him that lunch orders will be punctual."),
]

TRANSITION = "Now let's listen to the kitchen exchange again without interruption."
OUTRO = (
    "With his headache slowly easing thanks to Senya's timely brine, Chef Barinov readies himself "
    "to supervise the busy lunch service at Claude Monet."
)
CLOSING = ("anya", "Всё будет готово вовремя, шеф.")
