ID = "kukhnya-s01e14-scene-16"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 14
SCENE = 16
TITLE = "Идиот  (Idiot)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "louis": "anja", "vika": "angelina"}
LABELS = {"anya": "Макс", "louis": "Луи", "vika": "Елена"}
SOURCE_NAME = "Кухня (Kukhnya) S1.14"
SOURCE_FILE = "sources/kukhnya/s01/e14.ru.dual.srt"
SOURCE_NOTE = "Scene 16"

INTRO = "The guests realize the recipe is in French, and Louis watches Max embarrass himself. Let's listen closely to their exchange in Russian first, and then walk through each line together."

STORY = [
    ("vika", "Тут все по-французски.",
     "Here everything is in French.",
     [(1, "Макс")], "adapted"),
    ("vika", "Для нашего шефа это не проблема.",
     "For our chef this is not a problem.",
     [(1, "Макс")], "adapted"),
    ("vika", "Правда, Максимилиан?",
     "Right, Maximilian?",
     [(1, "Макс")], "adapted"),
    ("anya", "Си.",
     "Si.",
     [(1, "Макс")], "adapted"),
    ("louis", "Си? Идиот.",
     "Si? Idiot.",
     [(1, "Макс")], "adapted"),
    ("louis", "Си — это по-итальянски.",
     "Si is in Italian.",
     [(1, "Макс")], "adapted"),
    ("louis", "По-французски будет уи.",
     "In French it will be oui.",
     [(1, "Макс")], "new"),
    ("anya", "Да, конечно, я знаю это.",
     "Yes, of course, I know this.",
     [(1, "Макс")], "new"),
    ("vika", "Максимилиан, вы понимаете французский язык?",
     "Maximilian, do you understand the French language?",
     [(1, "Макс")], "new"),
    ("anya", "Конечно, я прекрасно понимаю французский.",
     "Of course, I understand French perfectly.",
     [(1, "Макс")], "new"),
    ("louis", "Ну, что ты будешь делать теперь?",
     "Well, what will you do now?",
     [(1, "Макс")], "adapted"),
    ("anya", "Я прочитаю этот рецепт и приготовлю блюдо.",
     "I will read this recipe and prepare the dish.",
     [(1, "Макс")], "new"),
    ("louis", "Это будет очень смешно.",
     "This will be very funny.",
     [(1, "Макс")], "new"),
]

OPENER = "Let us break down this interaction."

WALK = [
    (0, None,
     "'Here everything is in French.' Russian leaves out 'am', 'is', or 'are' in the present tense, linking 'here' straight to 'in French'."),
    (1, None,
     "'For our chef this is not a problem.' Notice the word order: 'chef' comes first, and 'problem' finishes the sentence."),
    (2, None,
     "'Right, Maximilian?' Elena puts 'honestly' up front so the listener immediately catches the tone, followed by 'person name'."),
    (3, None,
     "'Si.' A compact expression built around 'oui' and 'oui'."),
    (4, None,
     "'Si? Idiot.' The key word here means 'oui', which Louis combines with 'idiot'."),
    (5, None,
     "'Si is in Italian.' Louis starts with 'oui' and pairs it with 'this' to make the point clear."),
    (6, None,
     "'In French it will be oui.' Louis puts 'in French' up front so the listener immediately catches the tone, followed by 'will be'."),
    (7, None,
     "'Yes, of course, I know this.' The key word here means 'of course', which Max combines with 'I'. Elena answers straight away."),
    (8, None,
     "'Maximilian, do you understand the French language?' Here 'person name' sets up the idea, while 'language' comes at the end for emphasis."),
    (9, None,
     "'Of course, I understand French perfectly.' You'll hear 'of course' all the time in the show, here connected with 'French'."),
    (10, None,
     "'Well, what will you do now?' In Russian, 'what' leads into 'now' in a very natural everyday phrasing. Then Max replies."),
    (11, None,
     "'I will read this recipe and prepare the dish.' Listen for the word meaning 'I' right alongside 'to read' in this line."),
    (12, None,
     "'This will be very funny.' The first content word means 'this', and 'ridiculous' rounds out the thought."),
]

TRANSITION = "Now let us listen to the conversation again without interruption."
OUTRO = "Max is trapped and must pretend to read French to save face."
CLOSING = ("louis", "Это будет очень смешно.")
