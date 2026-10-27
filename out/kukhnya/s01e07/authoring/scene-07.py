"""s01e07 scene 07: Спасение карпов (Saving the Carp)."""

ID = "kukhnya-s01e07-scene-07"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 7
SCENE = 7
TITLE = "Спасение карпов  (Saving the Carp)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "kostya": "anja"}
LABELS = {"anya": "Настя", "kostya": "Костя"}
SOURCE_NAME = "Кухня (Kukhnya) S1.07"
SOURCE_FILE = "sources/kukhnya/s01/e07.ru.dual.srt"

INTRO = (
    "In the quiet restaurant back area, bartender Kostya finds waitress Nastya in deep distress. "
    "She tearfully confesses that her strict landlady threw her out of her rented apartment for rescuing live carp and keeping them in the bathtub. "
    "Let's listen to their conversation in Russian first."
)

STORY = [
    ("kostya", "Настя, что у тебя сегодня случилось?",
     "Nastya, what happened with you today?",
     [(60, "Значит, что случилось")], "inquiring with concern"),
    ("anya", "Моя злая хозяйка выгнала меня.",
     "My wicked landlady kicked me out.",
     [(61, "Хозяйка поругалась")], "explaining her eviction"),
    ("kostya", "За что она выгнала тебя?",
     "What did she kick you out for?",
     [], "asking for the reason"),
    ("anya", "Я принесла домой живых карпов.",
     "I brought live carp home.",
     [(62, "Это карпы")], "revealing the cause"),
    ("kostya", "Зачем тебе живая рыба дома?",
     "Why do you need live fish at home?",
     [], "asking in confusion"),
    ("anya", "В магазине их могли просто убить!",
     "In the store they could simply kill them!",
     [(63, "В магазине их купят и убьют")], "explaining her animal rescue"),
    ("kostya", "И где они плавают сейчас?",
     "And where are they swimming now?",
     [], "asking about their location"),
    ("anya", "Они прекрасно живут в ванне.",
     "They live wonderfully in the bathtub.",
     [(64, "А у меня они скоро размножаться будут")], "describing their new habitat"),
    ("kostya", "Понятно, хозяйка была очень недовольна.",
     "I see, the landlady was very unhappy.",
     [], "understanding the landlady's reaction"),
    ("anya", "Я не могу жить с жестокими людьми.",
     "I cannot live with cruel people.",
     [(66, "Я не могу жить в квартире убийцы")], "standing on moral principle"),
    ("kostya", "Слушай, ты можешь пока пожить у меня.",
     "Listen, you can stay at my place for now.",
     [(68, "ты можешь пока пожить у меня")], "offering shelter warmly"),
    ("anya", "Спасибо, Костик, ты настоящий друг!",
     "Thank you, Kostik, you are a true friend!",
     [(70, "Спасибо, Костик"), (71, "Ты настоящий друг")], "thanking him gratefully"),
]

OPENER = "Let's review this sweet and humorous conversation line by line."

WALK = [
    (0, None,
     "'Nastya, what happened with you today?' Kostya asks his tearful girlfriend what caused her distress."),
    (1, None,
     "'My wicked landlady kicked me out.' Nastya announces the sudden eviction from her rented flat."),
    (2, None,
     "'What did she kick you out for?' Kostya asks for the backstory behind the dispute."),
    (3, None,
     "'I brought live carp home.' Nastya reveals her unconventional choice of roommates."),
    (4, None,
     "'Why do you need live fish at home?' Kostya struggles to understand the domestic aquatic setup."),
    (5, None,
     "'In the store they could simply kill them!' Nastya explains her compassionate vegetarian intervention."),
    (6, None,
     "'And where are they swimming now?' Kostya asks where the live fish were placed."),
    (7, None,
     "'They live wonderfully in the bathtub.' Nastya proudly describes their temporary pool."),
    (8, None,
     "'I see, the landlady was very unhappy.' Kostya sympathizes with the bewildered homeowner."),
    (9, None,
     "'I cannot live with cruel people.' Nastya defends her unyielding ethical principles."),
    (10, None,
     "'Listen, you can stay at my place for now.' Kostya offers her a spare room in his apartment."),
    (11, None,
     "'Thank you, Kostik, you are a true friend!' Nastya beams with heartfelt gratitude at the kind offer."),
]

TRANSITION = "Now let's listen to the whole dialogue again at normal conversational speed."

OUTRO = (
    "Relieved by Kostya's generous invitation, Nastya prepares to move her belongings out of her old apartment. "
    "See you next time!"
)

CLOSING = ("anya", "Спасибо, Костик, ты настоящий друг!")
