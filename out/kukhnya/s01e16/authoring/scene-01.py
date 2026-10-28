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
     "'You have a very bad picture regarding safety.' — Notice the pronoun meaning 'you' paired with the adverb for 'very much'."),
    (1, None,
     "'Everything is fine with us.' — Notice the pronoun meaning 'us' paired with the det for 'everything'."),
    (2, None,
     "'We passed all inspections.' — Notice the pronoun meaning 'we' paired with the verb for 'to go through, to pass; to come along'."),
    (3, None,
     "'How did you pass the inspections?' — Notice the adverb meaning 'how' paired with the pronoun for 'you'."),
    (4, None,
     "'You have no fire extinguishers in the kitchen.' — Notice the pronoun meaning 'you' paired with the noun for 'fire extinguisher'."),
    (5, None,
     "'We have one.' — Notice the pronoun meaning 'us' paired with the verb for 'there is (   = I have)'."),
    (6, None,
     "'It is hanging under the table.' — Notice the pronoun meaning 'he' paired with the verb for '(it) has been hanging'."),
    (7, None,
     "'It must hang within three meters.' — Notice the pronoun meaning 'he' paired with the adjective for 'has to, must'."),
    (8, None,
     "'From the place of a possible fire.' — Notice the noun meaning 'places' paired with the adjective for 'possible, feasible'."),
    (9, None,
     "'This is not a problem.' — Notice the pronoun meaning 'this' paired with the noun for 'problem'."),
    (10, None,
     "'This is a very big problem.' — Notice the pronoun meaning 'this' paired with the adverb for 'very much'."),
    (11, None,
     "'Oh, how bad everything is.' — Notice the interjection meaning 'oh' paired with the adverb for 'how'."),
    (12, None,
     "'I give you two days for correction.' — Notice the pronoun meaning 'I' paired with the verb for 'give'."),
    (13, None,
     "'We will do everything.' — Notice the pronoun meaning 'we' paired with the det for 'everything'."),
]

TRANSITION = "Now let us listen to the conversation once again."
OUTRO = "The conversation concludes the matter at hand."
CLOSING = ("leva", "Мы всё сделаем.")
