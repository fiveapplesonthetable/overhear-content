ID = "kukhnya-s01e18-scene-17"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 18
SCENE = 17
TITLE = "Увольнения  (Firings)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "nagiyev": "anja"}
LABELS = {"anya": "Виктор", "nagiyev": "Нагиев"}
SOURCE_NAME = "Кухня (Kukhnya) S1.18"
SOURCE_FILE = "sources/kukhnya/s01/e18.ru.dual.srt"
SOURCE_NOTE = "Scene 17"

INTRO = "Nagiyev and Viktor have a heated argument in the office about the restaurant's budget. Nagiyev wants to save money by firing the most expensive kitchen staff."

STORY = [
    ("nagiyev", "Я должен уволить твоих поваров.",
     "I must fire your cooks.",
     [(308, 'уволить')], "adapted"),
    ("anya", "Ты совсем сошёл с ума?",
     "Have you gone completely crazy?",
     [], "new"),
    ("nagiyev", "Они слишком дорого стоят.",
     "They cost too much.",
     [], "new"),
    ("nagiyev", "Это почти полмиллиона каждый месяц.",
     "This is almost half a million every month.",
     [(305, 'полмиллиона каждый месяц')], "adapted"),
    ("anya", "Ты не можешь их увольнять.",
     "You cannot fire them.",
     [(309, 'нельзя увольнять')], "adapted"),
    ("anya", "Это лучшая команда в Москве.",
     "This is the best team in Moscow.",
     [(312, 'лучшие в Москве')], "adapted"),
    ("nagiyev", "Дешевле найти новых людей.",
     "It is cheaper to find new people.",
     [(314, 'Дешевле')], "adapted"),
    ("nagiyev", "Какая разница, кто режет морковь?",
     "What difference does it make who cuts carrots?",
     [(313, 'какая разница, кто будет морковь')], "adapted"),
    ("anya", "Это моя команда!",
     "This is my team!",
     [(315, 'моя команда')], "adapted"),
    ("anya", "Если ты их уволишь, ты потеряешь меня.",
     "If you fire them, you will lose me.",
     [(328, 'уволишь их, потеряешь меня')], "adapted"),
    ("nagiyev", "Витя, просто сядь и успокойся.",
     "Vitya, just sit and calm down.",
     [(318, 'Витя, сядь')], "adapted"),
    ("anya", "Хорошо, разбирайтесь сами.",
     "Alright, sort it out yourselves.",
     [(320, 'Разбирайтесь')], "adapted"),
    ("anya", "А я пока увольняюсь.",
     "And I am quitting in the meantime.",
     [(320, 'А я пока увольняюсь')], "adapted"),
    ("nagiyev", "Подожди, мы всё решим.",
     "Wait, we will solve everything.",
     [], "new"),
]

OPENER = "Let us break down this interaction."

WALK = [
    (0, None,
     "'I must fire your cooks.' A compact expression built around 'I' and 'cooks'."),
    (1, None,
     "'Have you gone completely crazy?' You'll hear 'you' all the time in the show, here connected with 'mind'."),
    (2, None,
     "'They cost too much.' Dmitry starts with 'they' and pairs it with 'too' to make the point clear."),
    (3, None,
     "'This is almost half a million every month.' You'll hear 'this' all the time in the show, here connected with 'month'."),
    (4, None,
     "'You cannot fire them.' You'll hear 'you' all the time in the show, here connected with 'to fire'."),
    (5, None,
     "'This is the best team in Moscow.' Viktor starts with 'this' and pairs it with 'best' to make the point clear. And Dmitry jumps in."),
    (6, None,
     "'It is cheaper to find new people.' You'll hear 'cheaper' all the time in the show, here connected with 'people'."),
    (7, None,
     "'What difference does it make who cuts carrots?' In Russian, 'what' leads into 'carrot' in a very natural everyday phrasing."),
    (8, None,
     "'This is my team!' The first content word means 'this', and 'team' rounds out the thought."),
    (9, None,
     "'If you fire them, you will lose me.' A compact expression built around 'you' and 'me'."),
    (10, None,
     "'Vitya, just sit and calm down.' Listen for the word meaning 'Vitya' right alongside 'just' in this line."),
    (11, None,
     "'Alright, sort it out yourselves.' The reflexive ending on the verb for 'to understand well' turns the action back onto the subject."),
    (12, None,
     "'And I am quitting in the meantime.' Notice the word order: 'I' comes first, and 'quit' finishes the sentence."),
    (13, None,
     "'Wait, we will solve everything.' Dmitry puts 'wait' up front so the listener immediately catches the tone, followed by 'we'."),
]

TRANSITION = "Now let us listen to the conversation again without interruption."
OUTRO = "Angry and feeling betrayed, Viktor threatens to resign rather than lose his best kitchen team."
CLOSING = ("nagiyev", "Подожди, мы всё решим.")
