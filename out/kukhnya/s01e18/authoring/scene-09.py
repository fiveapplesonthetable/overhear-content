ID = "kukhnya-s01e18-scene-09"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 18
SCENE = 9
TITLE = "Квартплата  (Rent)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "ilya": "anja"}
LABELS = {"anya": "Макс", "ilya": "Илья"}
SOURCE_NAME = "Кухня (Kukhnya) S1.18"
SOURCE_FILE = "sources/kukhnya/s01/e18.ru.dual.srt"
SOURCE_NOTE = "Scene 9"

INTRO = "Max is standing in the kitchen, looking very confused as he discusses finances. Let's listen closely to their exchange in Russian first, and then walk through each line together."

STORY = [
    ("anya", "Наша квартплата?",
     "Our rent?",
     [(1, "девушки")], "adapted"),
    ("anya", "В смысле?",
     "What do you mean?",
     [(1, "девушки")], "adapted"),
    ("ilya", "В прямом смысле.",
     "Exactly what I said.",
     [(1, "девушки")], "adapted"),
    ("ilya", "Сейчас я тебе все объясню.",
     "I will explain everything to you now.",
     [(1, "девушки")], "adapted"),
    ("anya", "Я ничего не понимаю.",
     "I do not understand anything.",
     [(1, "девушки")], "new"),
    ("ilya", "Предположим одну ситуацию.",
     "Let's assume one situation.",
     [(1, "девушки")], "new"),
    ("ilya", "Тимур привозит нам коньяк.",
     "Timur brings us cognac.",
     [(1, "девушки")], "adapted"),
    ("ilya", "Пять литров коньяка каждую неделю.",
     "Five liters of cognac every week.",
     [(1, "девушки")], "adapted"),
    ("anya", "Он привозит его бесплатно?",
     "Does he bring it for free?",
     [(1, "девушки")], "new"),
    ("ilya", "Да, абсолютно бесплатно.",
     "Yes, absolutely for free.",
     [(1, "девушки")], "adapted"),
    ("anya", "И что мы делаем с ним?",
     "And what do we do with it?",
     [(1, "девушки")], "new"),
    ("ilya", "Этот коньяк идет на оплату.",
     "This cognac goes to payment.",
     [(1, "девушки")], "adapted"),
]

OPENER = "Let us break down this interaction."

WALK = [
    (0, None,
     "'Our rent?' Max starts with 'rent' and pairs it with 'rent' to make the point clear."),
    (1, None,
     "'What do you mean?' Max puts 'sense' up front so the listener immediately catches the tone, followed by 'sense'."),
    (2, None,
     "'Exactly what I said.' Here 'straight' sets up the idea, while 'sense' comes at the end for emphasis."),
    (3, None,
     "'I will explain everything to you now.' You'll hear 'now' all the time in the show, here connected with 'I'll explain'. Then Max replies."),
    (4, None,
     "'I do not understand anything.' The key word here means 'I', which Max combines with 'nothing'."),
    (5, None,
     "'Let's assume one situation.' Ilya starts with 'suppose' and pairs it with 'one' to make the point clear."),
    (6, None,
     "'Timur brings us cognac.' Ilya puts 'Timur' up front so the listener immediately catches the tone, followed by 'bring'."),
    (7, None,
     "'Five liters of cognac every week.' In Russian, 'five' leads into 'for a week' in a very natural everyday phrasing."),
    (8, None,
     "'Does he bring it for free?' You'll hear 'he' all the time in the show, here connected with 'for free'."),
    (9, None,
     "'Yes, absolutely for free.' A compact expression built around 'completely' and 'for free'. Max answers straight away."),
    (10, None,
     "'And what do we do with it?' Listen for the word meaning 'what' right alongside 'we' in this line."),
    (11, None,
     "'This cognac goes to payment.' Russian leaves out 'am', 'is', or 'are' in the present tense, linking 'cognac' straight to 'payment'."),
]

TRANSITION = "Now let us listen to the conversation again without interruption."
OUTRO = "Max starts to realize how the unusual business works in this restaurant."
CLOSING = ("ilya", "Этот коньяк идет на оплату.")
