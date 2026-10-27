"""Scene 38 — Colleagues Again (s01e11, 01:10:33–01:10:34)."""

ID = "domashniy-arest-s01e11-scene-38"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 11
SCENE = 38
TITLE = "Снова коллеги  (Colleagues Again)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.11"
SOURCE_FILE = "sources/domashniy-arest/s01/e11.ru.dual.srt"

VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "sokolov": "anja",
}

LABELS = {
    "anya": "Лавров",
    "sokolov": "Соколов",
}

INTRO = (
    "Inside the surveillance van, Sokolov hangs up the phone and delivers the general's unexpected decision "
    "to Lavrov, celebrating that both officers remain on the active mission together."
)

STORY = [
    ("sokolov", "Генерал только что положил трубку.",
     "The general just hung up the phone.",
     [], "call finished"),

    ("anya", "И что же сказал наш начальник?",
     "And what did our boss say?",
     [], "Lavrov asks"),

    ("sokolov", "Он не принял твой рапорт.",
     "He did not accept your resignation report.",
     [], "report rejected"),

    ("anya", "Правда? Он отказался его подписать?",
     "Really? Did he refuse to sign it?",
     [], "Lavrov surprised"),

    ("sokolov", "Он приказал продолжать нашу операцию.",
     "He ordered our operation to continue.",
     [], "mission ordered"),

    ("anya", "Значит, меня не выгонят со службы?",
     "Does that mean I won't be fired from service?",
     [], "job secured"),

    ("sokolov", "Ты остаёшься майором, Анатолий.",
     "You remain a major, Anatoliy.",
     [], "rank confirmed"),

    ("anya", "Какое это огромное облегчение для меня!",
     "What a huge relief this is for me!",
     [], "relief expressed"),

    ("sokolov", "Мы теперь снова коллеги!",
     "We are colleagues again now!",
     [(1151, "Мы теперь снова коллеги.")], "colleagues again"),

    ("anya", "Я очень рад работать с тобой.",
     "I am very glad to work with you.",
     [], "partnership confirmed"),

    ("sokolov", "Тогда садись скорее за аппаратуру.",
     "Then sit down at the surveillance equipment quickly.",
     [], "back to work"),

    ("anya", "Надо следить за каждым шагом кандидата.",
     "We must monitor every step of the candidate.",
     [], "focus on mission"),

    ("sokolov", "Наша работа ещё только начинается.",
     "Our work is only just beginning.",
     [], "looking forward"),

    ("anya", "Тогда продолжаем слушать этот эфир.",
     "Then let us continue listening to this broadcast.",
     [], "listening in"),
]

OPENER = "Let's explore the relief and renewed camaraderie between Lavrov and Sokolov."

WALK = [
    (0, None,
     "'The general just hung up the phone.' Sokolov finishes the phone call with headquarters."),
    (1, None,
     "'And what did our boss say?' Lavrov asks nervously about the general's decision."),
    (2, None,
     "'He did not accept your resignation report.' Sokolov reveals that the resignation was rejected."),
    (3, None,
     "'Really? Did he refuse to sign it?' Lavrov reacts with surprise to the good news."),
    (4, None,
     "'He ordered our operation to continue.' Sokolov confirms that the wiretap mission proceeds."),
    (5, None,
     "'Does that mean I won't be fired from service?' Lavrov seeks reassurance about his military rank."),
    (6, None,
     "'You remain a major, Anatoliy.' Sokolov reminds him of his official officer standing."),
    (7, None,
     "'What a huge relief this is for me!' Lavrov expresses heartfelt gratitude and relief."),
    (8, None,
     "'We are colleagues again now!' Sokolov cheerfully announces their partnership is restored."),
    (9, None,
     "'I am very glad to work with you.' Lavrov appreciates having an experienced partner."),
    (10, None,
     "'Then sit down at the surveillance equipment quickly.' Sokolov urges him to get back to duty."),
    (11, None,
     "'We must monitor every step of the candidate.' Lavrov focuses on observing Samsonov."),
    (12, None,
     "'Our work is only just beginning.' Sokolov emphasizes the ongoing covert investigation."),
    (13, None,
     "'Then let us continue listening to this broadcast.' Lavrov puts his headphones back on."),
]

TRANSITION = "Now let's listen to the heartwarming reunion between the two partners once more."

OUTRO = "With their partnership restored, Lavrov and Sokolov resume their round-the-clock surveillance."

CLOSING = ("sokolov", "Мы теперь снова коллеги!")
