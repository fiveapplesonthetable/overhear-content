"""Scene 23 — End of a Difficult Day (s01e05, 00:23:16–00:23:53)."""

ID = "kukhnya-s01e05-scene-23"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 5
SCENE = 23
TITLE = "Конец трудного дня  (End of a Difficult Day)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Кухня (Kukhnya) S1.05"
SOURCE_FILE = "sources/kukhnya/s01/e05.ru.dual.srt"

VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "chef": "anja",
    "kostya": "angelina",
}

LABELS = {
    "anya": "Макс",
    "chef": "Шеф",
    "kostya": "Костя",
}

INTRO = (
    "After a turbulent day of kitchen rush, burned dishes, and fiery shouting from Chef Barinov, "
    "the staff of Claude Monet finally wrap up their evening shift. "
    "Max reflects on life, friendship, and the sweet relief of surviving another chaotic day."
)

STORY = [
    ("anya", "Бывают дни, когда всё идёт не так.",
     "There are days when everything goes wrong.",
     [(314, "бывают дни, когда у тебя все идет не так.")], "Max opens reflection"),

    ("anya", "На кухне сегодня была настоящая запара.",
     "In the kitchen today there was real rush.",
     [], "Max recalls chaos"),

    ("anya", "Шеф кричал, а заказы не заканчивались.",
     "The chef shouted, and the orders did not end.",
     [], "Max describes kitchen"),

    ("anya", "Но такие трудные дни всегда заканчиваются.",
     "But such difficult days always end.",
     [(315, "такие дни всегда заканчиваются.")], "Max notes silver lining"),

    ("anya", "Кому-то этот день принёс что-то новое.",
     "To someone this day brought something new.",
     [(316, "Кому-то этот день принес что-то новое.")], "Max reflects on novelty"),

    ("anya", "Для кого-то всё остаётся по-старому.",
     "For someone everything stays the same.",
     [(317, "Для кого-то все остается по-старому.")], "Max reflects on routine"),

    ("kostya", "Привет, Настя, рад тебя видеть.",
     "Hi, Nastya, glad to see you.",
     [(318, "Привет.")], "Kostya greets Nastya"),

    ("kostya", "Надеюсь, твоя смена прошла хорошо.",
     "I hope your shift went well.",
     [], "Kostya smiles"),

    ("chef", "Семь тысяч рублей на Спартак!",
     "Seven thousand rubles on Spartak!",
     [(319, "Семь тысяч на Спартак.")], "Barinov places bet"),

    ("chef", "Моя любимая команда обязательно победит!",
     "My favorite team will definitely win!",
     [], "Barinov bets passionately"),

    ("anya", "Кто-то искренне рад этому дню.",
     "Someone is sincerely happy with this day.",
     [(320, "Кто-то рад этому дню.")], "Max contrasts feelings"),

    ("anya", "А я счастлив, что он закончился.",
     "And I am happy that it ended.",
     [(321, "А"), (322, "я счастлив, что он закончился.")], "Max expresses relief"),

    ("anya", "Завтра на кухне начнётся новая работа.",
     "Tomorrow in the kitchen new work will begin.",
     [], "Max looks ahead"),

    ("anya", "А сегодня пора немного отдохнуть.",
     "And today it is time to rest a little.",
     [], "Max concludes"),
]

OPENER = "Let's explore Max's closing reflections on surviving a chaotic day at Claude Monet."

WALK = [
    (0, None,
     "'There are days when everything goes wrong.' Max reflects on the turbulent shift in the kitchen."),
    (1, None,
     "'In the kitchen today there was real rush.' The restaurant was overwhelmed with endless orders."),
    (2, None,
     "'The chef shouted, and the orders did not end.' The head chef kept demanding perfection all evening."),
    (3, None,
     "'But such difficult days always end.' Max finds comfort in knowing bad days do not last forever."),
    (4, None,
     "'To someone this day brought something new.' Some staff members experienced unexpected surprises in the dining hall."),
    (5, None,
     "'For someone everything stays the same.' Routine continues unaffected for others in the restaurant."),
    (6, None,
     "'Hi, Nastya, glad to see you.' Kostya warmly greets the waitress at the end of the day."),
    (7, None,
     "'I hope your shift went well.' The bartender smiles shyly as they wrap up work."),
    (8, None,
     "'Seven thousand rubles on Spartak!' Chef Barinov rushes to place a passionate sports bet."),
    (9, None,
     "'My favorite team will definitely win!' Viktor puts all his faith in the team as he bets."),
    (10, None,
     "'Someone is sincerely happy with this day.' Others celebrate their personal triumphs with joy on this evening."),
    (11, None,
     "'And I am happy that it ended.' Max expresses deep relief that the stressful day is finally over."),
    (12, None,
     "'Tomorrow in the kitchen new work will begin.' Another chaotic day awaits the cooking staff in the morning."),
    (13, None,
     "'And today it is time to rest a little.' Max heads home ready for a peaceful night of sleep."),
]

TRANSITION = "Now let's listen to the closing montage and Max's reflections once more."

OUTRO = "With the stressful day behind him, Max heads home ready to face tomorrow's kitchen trials."

CLOSING = ("anya", "А сегодня пора немного отдохнуть.")
