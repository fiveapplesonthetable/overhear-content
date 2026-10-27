"""Scene 06 — Get the Nets (s01e13)."""

ID = "kukhnya-s01e13-scene-06"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 13
SCENE = 6
TITLE = "Берите сети  (Get the Nets)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Кухня (Kukhnya) S1.13"
SOURCE_FILE = "sources/kukhnya/s01/e13.ru.dual.srt"

VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "kostya": "anja",
}

LABELS = {
    "anya": "Макс",
    "kostya": "Шеф",
}

INTRO = (
    "While working his punishment shift in the stockroom, Max accidentally creates a huge mess, "
    "prompting the Chef to desperately call for all available nets."
)

STORY = [
    ("anya", "Блин, блин, блин, блин.",
     "Damn, damn, damn, damn.",
     [(87, "блин, блин, блин, блин.")], "Max panics in the stockroom"),

    ("anya", "Я уронил коробку на пол.",
     "I dropped the box onto the floor.",
     [], "Max shouts out loudly"),

    ("anya", "Они очень быстро бегают.",
     "They run very fast.",
     [], "Max tries to catch something"),

    ("kostya", "Что ты опять натворил, Макс?",
     "What did you do again, Max?",
     [], "Chef runs in quickly"),

    ("anya", "Я просто хотел взять продукты.",
     "I just wanted to take the products.",
     [], "Max defends himself nervously"),

    ("kostya", "Быстро берите все сети!",
     "Quickly get all the nets!",
     [(88, "Берите сети.")], "Chef shouts to the kitchen"),

    ("kostya", "Берите большие и маленькие.",
     "Take the big and small ones.",
     [(89, "Все берите. Большие, маленькие.")], "Chef gestures wildly"),

    ("kostya", "Берите всё, что у нас есть.",
     "Take everything that we have.",
     [(90, "Все, что есть.")], "Chef grabs a net himself"),

    ("kostya", "Нам надо поймать их всех.",
     "We need to catch them all.",
     [], "Chef commands the team"),

    ("anya", "Один спрятался под столом.",
     "One hid under the table.",
     [], "Max points at the corner"),

    ("kostya", "Не стойте просто так, ищите!",
     "Do not just stand like that, search!",
     [], "Chef yells at everyone"),

    ("anya", "Я сейчас его поймаю.",
     "I will catch it now.",
     [], "Max prepares a net"),
]

OPENER = "Let's join Max and the Chef as chaos breaks out in the back."

WALK = [
    (0, None,
     "'Damn, damn, damn, damn.' Max realizes he made a terrible mistake."),
    (1, None,
     "'I dropped the box onto the floor.' He explains the sudden disaster in the stockroom."),
    (2, None,
     "'They run very fast.' Max watches helplessly as the escaped animals scatter."),
    (3, None,
     "'What did you do again, Max?' The Chef bursts into the room in extreme anger."),
    (4, None,
     "'I just wanted to take the products.' Max claims he was only trying to do his assigned job."),
    (5, None,
     "'Quickly get all the nets!' The Chef orders his team into immediate action."),
    (6, None,
     "'Take the big and small ones.' He wants every single piece of equipment they own."),
    (7, None,
     "'Take everything that we have.' The Chef prepares to catch whatever got loose."),
    (8, None,
     "'We need to catch them all.' He refuses to let a single one escape the building."),
    (9, None,
     "'One hid under the table.' Max spots movement near the kitchen wall."),
    (10, None,
     "'Do not just stand like that, search!' The Chef demands everyone participate in the hunt."),
    (11, None,
     "'I will catch it now.' Max lunges forward to fix his foolish mistake."),
]

TRANSITION = "Now let's listen to the sudden commotion once again."

OUTRO = "Max's clumsy mistake turns his stockroom punishment into an emergency for the whole kitchen."

CLOSING = ("anya", "Я сейчас его поймаю.")
