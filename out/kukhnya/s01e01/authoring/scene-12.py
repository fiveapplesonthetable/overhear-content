"""s01e01 scene 12: Спасительный литр воды (A Lifesaving Liter of Water)."""

ID = "kukhnya-s01e01-scene-12"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 1
SCENE = 12
TITLE = "Спасительный литр воды  (A Lifesaving Liter of Water)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "kostya": "anja"}
LABELS = {"anya": "Макс", "kostya": "Костя"}
SOURCE_NAME = "Кухня (Kukhnya) S1.01"
SOURCE_FILE = "sources/kukhnya/s01/e01.ru.dual.srt"
SOURCE_NOTE = "Cues 75-80. Max sits at the bar nursing a hangover, and bartender Kostya fetches him water."

INTRO = (
    "Slumping onto a stool at the Claude Monet bar, Max attempts to recover from a sleepless night of drinking at the nightclub. "
    "Bartender Kostya immediately detects the painful signs of a hangover and pours a lifesaving jug of cold water for the young newcomer. "
    "Let's listen to their conversation in Russian first."
)

STORY = [
    ("kostya", "Бухал вчера?",
     "Been drinking yesterday?",
     [(75, "Бухал вчера")], "noticing Max's rough condition"),
    ("anya", "Заметно?",
     "Is it noticeable?",
     [(76, "Заметно")], "asking ruefully"),
    ("kostya", "Лицо бледное, руки немного дрожат.",
     "Your face is pale, your hands are shaking a bit.",
     [], "listing the symptoms"),
    ("anya", "Да, ночь была очень бурной.",
     "Yes, the night was very wild.",
     [], "admitting the partying"),
    ("kostya", "Приятного аппетита.",
     "Enjoy your meal.",
     [(77, "Приятного аппетита")], "serving a nearby diner"),
    ("anya", "Кому ты сейчас это сказал?",
     "Who did you just say that to?",
     [], "confused by the greeting"),
    ("kostya", "Гостю за соседним столиком.",
     "To a guest at the next table.",
     [], "clarifying who he addressed"),
    ("kostya", "Что-нибудь желаете?",
     "Would you like anything?",
     [(78, "Что-нибудь желаете")], "switching to Max"),
    ("anya", "Воды.",
     "Water.",
     [(78, "Воды")], "pleading for hydration"),
    ("kostya", "С газом или без газа?",
     "Sparkling or still?",
     [(79, "без газа")], "asking for preference"),
    ("anya", "Литр! Без всякого газа!",
     "A liter! Without any gas at all!",
     [(79, "Литр")], "demanding still water urgently"),
    ("kostya", "Всё, я уже несу.",
     "Right away, I am already bringing it.",
     [(80, "я несу")], "hurrying to pour water"),
    ("anya", "Спасибо, друг, ты спасаешь мне жизнь.",
     "Thank you, my friend, you are saving my life.",
     [], "expressing profound gratitude"),
]

OPENER = "Let's replay a few lines to examine key phrases and grammar."

WALK = [
    (0, "Бухал вчера?",
     "'Been drinking yesterday?' Kostya asks casually, using the colloquial verb for drinking alcohol."),
    (1, "Заметно?",
     "'Is it noticeable?' Max replies ruefully, realizing his rough night shows on his face."),
    (7, "Что-нибудь желаете?",
     "'Would you like anything?' the bartender inquires, switching into professional hospitality mode."),
    (8, "Воды.",
     "'Water,' Max croaks, as he is in need of cold water before his interview."),
    (10, "Литр! Без всякого газа!",
     "'A liter! Without any gas at all!' Max exclaims, emphasizing the urgent quantity of cold still water he requires."),
]

TRANSITION = "Now listen to the full bar dialogue once more."

OUTRO = "Kostya slides a large carafe of water across the bar."

CLOSING = ("anya", "Холодная вода — лучшее лекарство.")
