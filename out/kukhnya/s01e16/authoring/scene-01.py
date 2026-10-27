ID = "kukhnya-s01e16-scene-01"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 16
SCENE = 1
TITLE = "Пожарная тревога  (Fire Alarm)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "leva": "anja"}
LABELS = {'anya': 'Инспектор', 'leva': 'Вика'}
SOURCE_NAME = "Кухня (Kukhnya) S1.16"
SOURCE_FILE = "sources/kukhnya/s01/e16.ru.dual.srt"
SOURCE_NOTE = "Cues."

INTRO = (
    "A strict fire safety inspector visits Claude Monet and points out numerous violations in the kitchen. Victoria tries to argue that they passed all previous inspections, but the inspector is not convinced. Let us listen to their conversation in Russian first."
)

STORY = [
    ("anya", "У вас очень плохая картина по безопасности.",
     "You have a very bad picture regarding safety.",
     [(1, 'У вас тут просто удручающая картина по технике пожарной безопасности.')], "adapted"),
    ("leva", "У нас всё в порядке.",
     "Everything is fine with us.",
     [(2, 'Да все же в порядке.')], "adapted"),
    ("leva", "Мы прошли все проверки.",
     "We passed all inspections.",
     [(2, 'Мы прошли все проверки.')], "adapted"),
    ("anya", "Как вы прошли проверки?",
     "How did you pass the inspections?",
     [(3, 'Ну как вы прошли проверки?')], "adapted"),
    ("anya", "У вас нет огнетушителей на кухне.",
     "You have no fire extinguishers in the kitchen.",
     [(3, 'Когда у вас на кухне даже огнетушителей нет.')], "adapted"),
    ("leva", "У нас есть один.",
     "We have one.",
     [(4, 'Да он есть, под собки висит.')], "adapted"),
    ("leva", "Он висит под столом.",
     "It is hanging under the table.",
     [(4, 'под собки висит.')], "adapted"),
    ("anya", "Он должен висеть в трёх метрах.",
     "It must hang within three meters.",
     [(5, 'А должен висеть в трех метрах от предполагаемого места возможного пожара.')], "adapted"),
    ("anya", "От места возможного пожара.",
     "From the place of a possible fire.",
     [(5, 'от предполагаемого места возможного пожара.')], "adapted"),
    ("leva", "Это не проблема.",
     "This is not a problem.",
     [], "new"),
    ("anya", "Это очень большая проблема.",
     "This is a very big problem.",
     [], "new"),
    ("anya", "Ох, как всё плохо.",
     "Oh, how bad everything is.",
     [(6, 'Ох-ох-ох.')], "adapted"),
    ("anya", "Я даю вам два дня на исправление.",
     "I give you two days for correction.",
     [(7, 'Даю два дня на исправление ситуации.')], "adapted"),
    ("leva", "Мы всё сделаем.",
     "We will do everything.",
     [], "new"),
]

OPENER = "Now let us examine the conversation line by line."

WALK = [
    (0, None,
     "'You have a very bad picture regarding safety.' -- The speaker makes the statement."),
    (1, None,
     "'Everything is fine with us.' -- The speaker makes the statement."),
    (2, None,
     "'We passed all inspections.' -- The speaker makes the statement."),
    (3, None,
     "'How did you pass the inspections?' -- The speaker makes the statement."),
    (4, None,
     "'You have no fire extinguishers in the kitchen.' -- The speaker makes the statement."),
    (5, None,
     "'We have one.' -- The speaker makes the statement."),
    (6, None,
     "'It is hanging under the table.' -- The speaker makes the statement."),
    (7, None,
     "'It must hang within three meters.' -- The speaker makes the statement."),
    (8, None,
     "'From the place of a possible fire.' -- The speaker makes the statement."),
    (9, None,
     "'This is not a problem.' -- The speaker makes the statement."),
    (10, None,
     "'This is a very big problem.' -- The speaker makes the statement."),
    (11, None,
     "'Oh, how bad everything is.' -- The speaker makes the statement."),
    (12, None,
     "'I give you two days for correction.' -- The speaker makes the statement."),
    (13, None,
     "'We will do everything.' -- The speaker makes the statement."),
]

TRANSITION = "Now let us listen to the conversation once again."
OUTRO = "The conversation concludes the matter at hand."
CLOSING = ("leva", "Мы всё сделаем.")
