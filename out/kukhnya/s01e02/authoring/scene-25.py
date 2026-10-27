"""Scene 25 — Two Sides of the Coin (s01e02, 00:21:11–00:24:10)."""

ID = "kukhnya-s01e02-scene-25"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 2
SCENE = 25
TITLE = "Две стороны медали  (Two Sides of the Coin)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Кухня (Kukhnya) S1.02"
SOURCE_FILE = "sources/kukhnya/s01/e02.ru.dual.srt"

VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "dmitry": "angelina",
    "chef": "anja",
}

LABELS = {
    "anya": "Макс",
    "dmitry": "Дмитрий",
    "chef": "Шеф",
}

INTRO = (
    "In the restaurant office, art director Vika shows owner Dmitry Nagiyev a video of Max fighting "
    "in the courtyard, hoping to get him fired, leading to surprising revelations."
)

STORY = [
    ("dmitry", "Вика говорит, что ты устроил драку.",
     "Vika says that you started a fight.",
     [(310, "Еще он сегодня устроил драку.")], "Dmitry asks"),

    ("anya", "Мы просто дурачились на заднем дворе.",
     "We were simply fooling around in the backyard.",
     [(313, "Да мы так дурачились.")], "Max explains"),

    ("dmitry", "Покажите мне видео этой вашей драки.",
     "Show me the video of this fight of yours.",
     [(315, "Я все сняла.")], "Dmitry watches"),

    ("dmitry", "Разве это драка? Ты даже не дрался!",
     "Is that really a fight? You did not even fight back!",
     [(322, "Ну какая же это драка, а?")], "Dmitry laughs"),

    ("dmitry", "Так что увольнять повара пока не за что.",
     "So there is no reason to fire the cook yet.",
     [(324, "Так что увольнять пока его не за что.")], "Dmitry decides"),

    ("chef", "Дмитрий, спасибо вам за справедливое решение.",
     "Dmitry, thank you for the fair decision.",
     [(325, "Спасибо большое.")], "Chef thanks"),

    ("chef", "Слушайте меня все: забудьте об этом видео!",
     "Listen to me everyone: forget about this video!",
     [(331, "Чтобы об этом больше никто не знал.")], "Chef's order"),

    ("chef", "Вике ещё работать здесь арт-директором.",
     "Vika still has to work here as art director.",
     [(332, "но арт-директор не самый плохой")], "Chef defends Vika"),

    ("chef", "Кто посмеет смеяться, сразу пойдёт вон!",
     "Whoever dares laugh will immediately get out!",
     [(333, "Ей еще здесь работать. Понятно?")], "Chef threatens"),

    ("anya", "У каждой медали есть две стороны.",
     "Every coin has two sides.",
     [(335, "У каждой медали есть две стороны,")], "Max reflects"),

    ("anya", "Однажды всё вокруг может резко измениться.",
     "One day everything around can change drastically.",
     [(335, "и однажды все может перевернуться.")], "Fortune shifts"),

    ("anya", "Бывший враг неожиданно становится твоим другом.",
     "A former enemy unexpectedly becomes your friend.",
     [(337, "становится твоим другом.")], "Friendship emerges"),

    ("anya", "А строгий тиран становится немного добрее.",
     "And a strict tyrant becomes a little bit kinder.",
     [(338, "Ну а тот, кто казался злобным тираном,")], "Chef's heart"),

    ("anya", "Жизнь продолжается, и завтра новый день!",
     "Life goes on, and tomorrow is a new day!",
     [(334, "Вот как-то так.")], "Closing optimism"),
]

OPENER = "Let's explore the courtyard video inquiry and Max's philosophical reflections."

WALK = [
    (0, None,
     "'Vika says that you started a fight.' Dmitry questions Max about the backstage conflict."),
    (1, None,
     "'We were simply fooling around in the backyard.' Max explains the playful nature of the brawl."),
    (2, None,
     "'Show me the video of this fight of yours.' The restaurant owner asks to inspect the recorded evidence."),
    (3, None,
     "'Is that really a fight? You did not even fight back!' Dmitry laughs upon seeing Max passively taking hits."),
    (4, None,
     "'So there is no reason to fire the cook yet.' Dmitry decides to keep Max on the kitchen staff."),
    (5, None,
     "'Dmitry, thank you for the fair decision.' The chef expresses gratitude for defending his kitchen team."),
    (6, None,
     "'Listen to me everyone: forget about this video!' Barinov firmly orders the cooks to protect Vika's dignity."),
    (7, None,
     "'Vika still has to work here as art director.' Barinov shows unexpected professional loyalty toward Vika."),
    (8, None,
     "'Whoever dares laugh will immediately get out!' The head chef threatens anyone who ridicules the footage."),
    (9, None,
     "'Every coin has two sides.' Max begins his poignant closing reflection on the nature of life."),
    (10, None,
     "'One day everything around can change drastically.' Max reflects on the shifting dynamics of life and work."),
    (11, None,
     "'A former enemy unexpectedly becomes your friend.' Bonds form in surprising ways in the restaurant."),
    (12, None,
     "'And a strict tyrant becomes a little bit kinder.' Even the terrifying chef has a warm and protective heart."),
    (13, None,
     "'Life goes on, and tomorrow is a new day!' Max looks forward with renewed optimism to his culinary career."),
]

TRANSITION = "Now let's listen to the final resolution and closing thoughts once more."

OUTRO = "Saved from dismissal, Max reflects on how fortunes shift and enemies can turn into allies."

CLOSING = ("anya", "Жизнь продолжается, и завтра новый день!")
