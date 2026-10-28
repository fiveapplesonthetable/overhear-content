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
     "'You have a very bad picture regarding safety.' the speaker puts 'you' up front so the listener immediately catches the tone, followed by 'very much'."),
    (1, None,
     "'Everything is fine with us.' In Russian, 'us' leads into 'order' in a very natural everyday phrasing."),
    (2, None,
     "'We passed all inspections.' Here 'we' sets up the idea, while 'check' comes at the end for emphasis."),
    (3, None,
     "'How did you pass the inspections?' Listen for the word meaning 'how' right alongside 'you' in this line."),
    (4, None,
     "'You have no fire extinguishers in the kitchen.' the speaker uses the polite plural 'you' here alongside 'you', keeping a formal or respectful tone. Then Vika replies."),
    (5, None,
     "'We have one.' Vika starts with 'us' and pairs it with 'there is' to make the point clear."),
    (6, None,
     "'It is hanging under the table.' Listen for the word meaning 'he' right alongside 'has been hanging' in this line."),
    (7, None,
     "'It must hang within three meters.' The first content word means 'he', and 'metre' rounds out the thought."),
    (8, None,
     "'From the place of a possible fire.' The first content word means 'places', and 'fire' rounds out the thought."),
    (9, None,
     "'This is not a problem.' A compact expression built around 'this' and 'problem'."),
    (10, None,
     "'This is a very big problem.' Listen for the word meaning 'this' right alongside 'very much' in this line."),
    (11, None,
     "'Oh, how bad everything is.' Here 'oh' sets up the idea, while 'badly' comes at the end for emphasis."),
    (12, None,
     "'I give you two days for correction.' Notice the word order: 'I' comes first, and 'correction' finishes the sentence."),
    (13, None,
     "'We will do everything.' Here 'we' sets up the idea, while 'we'll do' comes at the end for emphasis."),
]

TRANSITION = "Now let us listen to the conversation once again."
OUTRO = "And that's it for this scene. When you watch the episode, listen out for the exchange around fire alarm, and for the words meaning 'bad' and 'painting'. You'll catch them now. See you next time."
CLOSING = ("leva", "Мы всё сделаем.")
