"""Scene 22 — Conversation in the Office (s01e04, 00:21:12–00:22:35)."""

ID = "kukhnya-s01e04-scene-22"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 4
SCENE = 22
TITLE = "Разговор в кабинете  (Conversation in the Office)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Кухня (Kukhnya) S1.04"
SOURCE_FILE = "sources/kukhnya/s01/e04.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 290-316. Vika enters Barinov's office to defend Max, admitting she was the one "
    "who went to the rival restaurant and urging the chef not to ruin a promising talent."
)

VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "chef": "anja",
}

LABELS = {
    "anya": "Вика",
    "chef": "Шеф",
}

INTRO = (
    "In his quiet private office at Claude Monet, Chef Viktor Barinov fumes alone after firing Max. "
    "Dining room director Vika enters to confront him, bravely confessing the truth about the rival job interview "
    "and challenging the chef to reconsider his harsh decision. "
    "Let's listen to their emotional conversation in Russian first."
)

STORY = [
    ("chef", "Этого парня больше никуда не возьмут!",
     "They will not take this guy anywhere anymore!",
     [(290, "не возьмут")], "Chef vents"),

    ("anya", "Виктор, нам нужно срочно поговорить.",
     "Viktor, we need to talk urgently.",
     [(292, "Надо поговорить.")], "Vika demands conversation"),

    ("chef", "Я не хочу говорить об этом поваре.",
     "I do not want to talk about this cook.",
     [], "Chef resists"),

    ("anya", "Макс не ходил на то собеседование.",
     "Max did not go to that interview.",
     [(295, "Макс не ходил на собеседование.")], "Vika reveals truth"),

    ("chef", "Что ты такое сейчас говоришь?",
     "What are you saying right now?",
     [], "Chef is stunned"),

    ("anya", "Это я ходила в чужой ресторан.",
     "It was I who went to the other restaurant.",
     [(297, "Это я ходила.")], "Vika confesses"),

    ("anya", "Макс действительно очень талантливый парень.",
     "Max really is a very talented guy.",
     [(301, "парень")], "Vika defends Max"),

    ("anya", "Но ты совсем не даёшь ему расти.",
     "But you do not let him grow at all.",
     [], "Vika critiques chef"),

    ("anya", "Сколько хороших людей ушли отсюда?",
     "How many good people have left here?",
     [(305, "Сколько талантливых поваров ушли")], "Vika points to past departures"),

    ("chef", "Хватит читать мне свои нравоучения!",
     "Stop giving me your moral lectures!",
     [(313, "Хватит")], "Chef snaps back"),

    ("anya", "Мне просто искренне жаль этого парня.",
     "I simply genuinely feel sorry for this guy.",
     [], "Vika appeals to heart"),

    ("anya", "Я могу сказать, что он не уволен?",
     "Can I say that he is not fired?",
     [(316, "что он не уволен")], "Vika requests reinstatement"),

    ("chef", "Делай что хочешь, только оставь меня!",
     "Do what you want, just leave me alone!",
     [], "Chef relents"),
]

OPENER = "Now let's examine the intense office conversation with Vika line by line."

WALK = [
    (0, None,
     "'They will not take this guy anywhere anymore!' Barinov bitterly declares that Max has ruined his career forever."),
    (1, None,
     "'Viktor, we need to talk urgently.' Vika enters the office determined to clear up the misunderstanding."),
    (2, None,
     "'I do not want to talk about this cook.' The stubborn head chef tries to dismiss the discussion immediately."),
    (3, None,
     "'Max did not go to that interview.' Vika delivers the surprising fact that changes everything."),
    (4, None,
     "'What are you saying right now?' Caught completely off guard, Barinov struggles to process her words."),
    (5, None,
     "'It was I who went to the other restaurant.' Vika bravely admits her own secret meeting with the rival owner."),
    (6, None,
     "'Max really is a very talented guy.' The dining room director vouches for the young cook's genuine potential."),
    (7, None,
     "'But you do not let him grow at all.' Vika boldly challenges Barinov's harsh and oppressive management style."),
    (8, None,
     "'How many good people have left here?' Vika reminds the chef of how many great culinary talents he has driven away."),
    (9, None,
     "'Stop giving me your moral lectures!' The head chef bristles defensively against Vika's cutting accusations."),
    (10, None,
     "'I simply genuinely feel sorry for this guy.' Vika sets pride aside and appeals to common decency."),
    (11, None,
     "'Can I say that he is not fired?' Vika presses for the one concession that matters to Max's future."),
    (12, None,
     "'Do what you want, just leave me alone!' Grudgingly yielding, Barinov allows his apprentice to stay."),
]

TRANSITION = "Now let's listen to Vika and Barinov's crucial office conversation once more without interruption."

OUTRO = (
    "Thanks to Vika's courage and honesty, Max is saved from immediate dismissal "
    "and given another chance to prove himself in the kitchen."
)

CLOSING = ("chef", "Делай что хочешь, только оставь меня!")
