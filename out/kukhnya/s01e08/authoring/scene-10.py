"""s01e08 scene 10: Шеф на скамейке (Chef on the Bench)."""

ID = "kukhnya-s01e08-scene-10"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 8
SCENE = 10
TITLE = "Шеф на скамейке  (Chef on the Bench)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "prokhozhiy": "anja"}
LABELS = {"anya": "Шеф", "prokhozhiy": "Прохожий"}
SOURCE_NAME = "Кухня (Kukhnya) S1.08"
SOURCE_FILE = "sources/kukhnya/s01/e08.ru.dual.srt"

INTRO = (
    "Temporarily banned from his own kitchen after losing a bet to his culinary rival Elena, Chef Barinov sits dejectedly on a park bench outside Claude Monet. "
    "A curious passerby stops by to ask why the famous chef is loitering on the street in the middle of a workday. "
    "Let's listen to their conversation in Russian first."
)

STORY = [
    ("prokhozhiy", "Эй, дурак, почему ты сидишь здесь?",
     "Hey, idiot, why are you sitting here?",
     [(124, "Эй, дурак")], "calling out to Barinov"),
    ("anya", "Я великий шеф-повар, а вовсе не дурак!",
     "I am a great head chef, not an idiot at all!",
     [], "defending his dignity"),
    ("prokhozhiy", "Тогда почему ты не готовишь на кухне?",
     "Then why are you not cooking in the kitchen?",
     [], "questioning his presence"),
    ("anya", "Меня временно выгнали из собственного ресторана.",
     "They temporarily kicked me out of my own restaurant.",
     [], "grumbling about his banishment"),
    ("prokhozhiy", "Кто посмел выгнать такого строгого повара?",
     "Who dared to kick out such a strict chef?",
     [], "asking in disbelief"),
    ("anya", "Одна наглая женщина из соседнего ресторана.",
     "An insolent woman from a neighboring restaurant.",
     [], "complaining about Elena"),
    ("prokhozhiy", "Женщины всегда приносят мужчинам большие проблемы.",
     "Women always bring men big problems.",
     [], "offering cynical sympathy"),
    ("anya", "Ты абсолютно прав, мой случайный собеседник.",
     "You are absolutely right, my random conversational partner.",
     [], "finding common ground"),
    ("prokhozhiy", "И что ты теперь собираешься делать?",
     "And what are you going to do now?",
     [], "asking about his plan"),
    ("anya", "Я вернусь и верну свою кухню!",
     "I will return and get my kitchen back!",
     [], "declaring his determination"),
    ("prokhozhiy", "Вот это правильные слова, смелый повар!",
     "Now those are the right words, brave cook!",
     [], "encouraging him warmly"),
    ("anya", "Спасибо за совет, я иду побеждать!",
     "Thank you for the advice, I am going to win!",
     [], "heading back with vigor"),
]

OPENER = "Let's review this unusual street conversation line by line."

WALK = [
    (0, None,
     "'Hey, idiot, why are you sitting here?' A cheeky passerby calls out to Barinov on the park bench."),
    (1, None,
     "'I am a great head chef, not an idiot at all!' Barinov defends his culinary dignity with offended pride."),
    (2, None,
     "'Then why are you not cooking in the kitchen?' The bystander questions why a top chef is idling outside."),
    (3, None,
     "'They temporarily kicked me out of my own restaurant.' Barinov bitterly admits his temporary banishment."),
    (4, None,
     "'Who dared to kick out such a strict chef?' The stranger is amazed that anyone could unseat the fearsome cook."),
    (5, None,
     "'An insolent woman from a neighboring restaurant.' Barinov grumbles about his cunning rival Elena Sokolova."),
    (6, None,
     "'Women always bring men big problems.' The passerby offers a cynical philosophical observation."),
    (7, None,
     "'You are absolutely right, my random conversational partner.' Barinov finds unexpected comfort in the stranger's words."),
    (8, None,
     "'And what are you going to do now?' The bystander asks about Barinov's next move."),
    (9, None,
     "'I will return and get my kitchen back!' Barinov resolves to reclaim his rightful kitchen kingdom."),
    (10, None,
     "'Now those are the right words, brave cook!' The stranger cheers on Barinov's fighting spirit."),
    (11, None,
     "'Thank you for the advice, I am going to win!' Barinov stands up from the bench, ready for victory."),
]

TRANSITION = "Now let's listen to the whole dialogue again at normal conversational speed."

OUTRO = (
    "Revitalized by the brief conversation on the park bench, Chef Barinov prepares to reclaim authority over Claude Monet. "
    "See you next time!"
)

CLOSING = ("anya", "Спасибо за совет, я иду побеждать!")
