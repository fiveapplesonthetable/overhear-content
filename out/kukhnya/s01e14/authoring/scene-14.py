ID = "kukhnya-s01e14-scene-14"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 14
SCENE = 14
TITLE = "Сим-карта в десерте  (SIM Card in Dessert)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "kostya": "anja"}
LABELS = {"anya": "Лёва", "kostya": "Костя"}
SOURCE_NAME = "Кухня (Kukhnya) S1.14"
SOURCE_FILE = "sources/kukhnya/s01/e14.ru.dual.srt"
SOURCE_NOTE = "Scene 14"

INTRO = "In the kitchen, Kostya tells Lyova about a problem with a customer's dessert. Let's listen closely to their exchange in Russian first, and then walk through each line together."

STORY = [
    ("anya", "Я никому не нужен.",
     "I am not needed by anyone.",
     [(1, "Макс")], "adapted"),
    ("kostya", "Люба, клиент нашел сим-карту в десерте.",
     "Lyuba, a customer found a SIM card in the dessert.",
     [(1, "Макс")], "adapted"),
    ("anya", "Сим-карту? В десерте?",
     "A SIM card? In the dessert?",
     [(1, "Макс")], "new"),
    ("kostya", "Да, он требует шеф-повара.",
     "Yes, he demands the chef.",
     [(1, "Макс")], "new"),
    ("kostya", "Иди к нему, Лёва.",
     "Go to him, Lyova.",
     [(1, "Макс")], "new"),
    ("anya", "Я не пойду туда.",
     "I will not go there.",
     [(1, "Макс")], "new"),
    ("kostya", "Что значит, ты не пойдешь?",
     "What do you mean, you will not go?",
     [(1, "Макс")], "adapted"),
    ("kostya", "Ты сегодня шеф-повар.",
     "You are the chef today.",
     [(1, "Макс")], "new"),
    ("kostya", "Иди и разбирайся с этим.",
     "Go and figure this out.",
     [(1, "Макс")], "new"),
    ("anya", "Но я не шеф-повар.",
     "But I am not the chef.",
     [(1, "Макс")], "new"),
    ("kostya", "Лёва, тебе надо разобраться.",
     "Lyova, you need to figure it out.",
     [(1, "Макс")], "new"),
    ("anya", "Я боюсь туда идти.",
     "I am afraid to go there.",
     [(1, "Макс")], "new"),
    ("kostya", "Давай, иди.",
     "Come on, go.",
     [(1, "Макс")], "new"),
]

OPENER = "Let us break down this interaction."

WALK = [
    (0, None,
     "'I am not needed by anyone.' Russian leaves out 'am', 'is', or 'are' in the present tense, linking 'I' straight to 'is needed'."),
    (1, None,
     "'Lyuba, a customer found a SIM card in the dessert.' Notice the word order: 'Lyuba' comes first, and 'dessert' finishes the sentence."),
    (2, None,
     "'A SIM card? In the dessert?' There is no question word here — in Russian, rising intonation on 'dessert' is enough to make it a question. And Kostya jumps in."),
    (3, None,
     "'Yes, he demands the chef.' The key word here means 'he', which Kostya combines with 'demands'."),
    (4, None,
     "'Go to him, Lyova.' Here 'go' sets up the idea, while 'Lyova' comes at the end for emphasis."),
    (5, None,
     "'I will not go there.' Lyova starts with 'I' and pairs it with 'go' to make the point clear. Kostya answers straight away."),
    (6, None,
     "'What do you mean, you will not go?' The question word for 'what' comes right at the start, followed directly by 'will go'."),
    (7, None,
     "'You are the chef today.' You'll hear 'you' all the time in the show, here connected with 'head chef'."),
    (8, None,
     "'Go and figure this out.' The first content word means 'go', and 'to understand well' rounds out the thought. Then Lyova replies."),
    (9, None,
     "'But I am not the chef.' A compact expression built around 'I' and 'head chef'."),
    (10, None,
     "'Lyova, you need to figure it out.' The first content word means 'Lyova', and 'to deal with' rounds out the thought."),
    (11, None,
     "'I am afraid to go there.' The reflexive ending on the verb for 'am afraid' turns the action back onto the subject. And Kostya jumps in."),
    (12, None,
     "'Come on, go.' Kostya puts 'let's' up front so the listener immediately catches the tone, followed by 'go'."),
]

TRANSITION = "Now let us listen to the conversation again without interruption."
OUTRO = "Kostya pushes Lyova to take responsibility for the kitchen."
CLOSING = ("kostya", "Давай, иди.")
