ID = "kukhnya-s01e20-scene-09"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 20
SCENE = 9
TITLE = "Новый шаг  (A New Step)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "kostya": "anja"}
LABELS = {"anya": "Настя", "kostya": "Костя"}
SOURCE_NAME = "Кухня (Kukhnya) S1.20"
SOURCE_FILE = "sources/kukhnya/s01/e20.ru.dual.srt"
SOURCE_NOTE = "Scene 9"

INTRO = "Nastya pushes Kostya to take the next big step in their relationship, and we will listen to their dialogue in Russian first; do not worry about catching every single word."

STORY = [
    ("anya", "А теперь давай поговорим.",
     "Now let us talk.",
     [], "new"),
    ("anya", "Помнишь, мы должны делать новый шаг?",
     "Remember, we should take a new step?",
     [], "new"),
    ("anya", "У меня ощущение, что ты еще не готов.",
     "I have a feeling you are not ready yet.",
     [], "new"),
    ("kostya", "Я?",
     "Me?",
     [], "new"),
    ("kostya", "Я готов.",
     "I am ready.",
     [], "new"),
    ("anya", "Точно?",
     "Are you sure?",
     [], "new"),
    ("kostya", "Точно.",
     "I am sure.",
     [], "new"),
    ("anya", "Тогда на выходные я зову родителей.",
     "Then I will invite my parents over for the weekend.",
     [], "new"),
    ("kostya", "Ладно.",
     "Okay.",
     [], "new"),
    ("kostya", "Подожди, твоих родителей?",
     "Wait, your parents?",
     [], "new"),
    ("anya", "Да, мою маму и папу.",
     "Yes, my mother and father.",
     [], "new"),
    ("kostya", "В нашу квартиру?",
     "To our apartment?",
     [], "new"),
    ("anya", "Конечно, куда ещё?",
     "Of course, where else?",
     [], "new"),
    ("kostya", "Мне надо убрать комнату.",
     "I need to clean the room.",
     [], "new"),
]

OPENER = "Let us break down this interaction."

WALK = [
    (0, None,
     "'Now let us talk.' You'll hear 'now' all the time in the show, here connected with 'we'll have a talk'."),
    (1, None,
     "'Remember, we should take a new step?' Notice the word order: 'do you remember' comes first, and 'step' finishes the sentence."),
    (2, None,
     "'I have a feeling you are not ready yet.' Instead of a verb for 'to have', Russian says 'by me' or 'with you' followed by 'ready'."),
    (3, None,
     "'Me?' You'll hear 'I' all the time in the show, here connected with 'I'."),
    (4, None,
     "'I am ready.' The key word here means 'I', which Kostya combines with 'ready'."),
    (5, None,
     "'Are you sure?' Nastya starts with 'definitely' and pairs it with 'definitely' to make the point clear."),
    (6, None,
     "'I am sure.' Kostya starts with 'definitely' and pairs it with 'definitely' to make the point clear. And Nastya jumps in."),
    (7, None,
     "'Then I will invite my parents over for the weekend.' Nastya puts 'back then' up front so the listener immediately catches the tone, followed by 'weekends'."),
    (8, None,
     "'Okay.' The key word here means 'all right', which Kostya combines with 'all right'."),
    (9, None,
     "'Wait, your parents?' A compact expression built around 'wait' and 'parents'. Nastya answers straight away."),
    (10, None,
     "'Yes, my mother and father.' Listen for the word meaning 'mother' right alongside 'daddy' in this line."),
    (11, None,
     "'To our apartment?' Notice the word order: 'flat' comes first, and 'flat' finishes the sentence."),
    (12, None,
     "'Of course, where else?' Nastya starts with 'of course' and pairs it with 'where to' to make the point clear. Then Kostya replies."),
    (13, None,
     "'I need to clean the room.' Here 'to me' sets up the idea, while 'the room' comes at the end for emphasis."),
]

TRANSITION = "Now let us listen to the conversation again without interruption."
OUTRO = "Kostya is terrified to learn that her parents are coming to visit them."
CLOSING = ("kostya", "Мне надо убрать комнату.")
