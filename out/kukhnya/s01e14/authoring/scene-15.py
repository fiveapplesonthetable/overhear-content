ID = "kukhnya-s01e14-scene-15"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 14
SCENE = 15
TITLE = "Знакомство с шефом  (Meeting the Chef)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "vika": "anja", "anya": "alisa"}
LABELS = {"vika": "Елена", "anya": "Макс"}
SOURCE_NAME = "Кухня (Kukhnya) S1.14"
SOURCE_FILE = "sources/kukhnya/s01/e14.ru.dual.srt"
SOURCE_NOTE = "Scene 15"

INTRO = "In the dining room, a woman introduces Max as a French culinary expert. Let's listen closely to their exchange in Russian first, and then walk through each line together."

STORY = [
    ("vika", "Дорогие друзья, минуточку внимания.",
     "Dear friends, a moment of attention.",
     [(1, "Макс")], "adapted"),
    ("vika", "Я хочу познакомить вас с лучшим шеф-поваром.",
     "I want to introduce you to the best chef.",
     [(1, "Макс")], "adapted"),
    ("anya", "Добрый вечер, дорогие гости.",
     "Good evening, dear guests.",
     [(1, "Макс")], "new"),
    ("vika", "Это Максимилиан, специалист по французской кухне.",
     "This is Maximilian, an expert in French cuisine.",
     [(1, "Макс")], "adapted"),
    ("anya", "Я очень рад быть здесь.",
     "I am very glad to be here.",
     [(1, "Макс")], "new"),
    ("vika", "Он любезно согласился приготовить старинное блюдо.",
     "He kindly agreed to prepare an old dish.",
     [(1, "Макс")], "adapted"),
    ("vika", "Мы взяли его из этой французской книги.",
     "We took it from this French book.",
     [(1, "Макс")], "new"),
    ("vika", "Я выбрала для нас вот это блюдо.",
     "I chose this dish for us.",
     [(1, "Макс")], "new"),
    ("anya", "Это прекрасный выбор для сегодняшнего вечера.",
     "This is an excellent choice for tonight.",
     [(1, "Макс")], "new"),
    ("vika", "Максимилиан приготовит его для нас сегодня.",
     "Maximilian will prepare it for us today.",
     [(1, "Макс")], "new"),
    ("anya", "Я сделаю все в лучшем виде.",
     "I will do everything in the best way.",
     [(1, "Макс")], "new"),
    ("vika", "Мы ждем ваш кулинарный шедевр.",
     "We are waiting for your culinary masterpiece.",
     [(1, "Макс")], "new"),
]

OPENER = "Let us break down this interaction."

WALK = [
    (0, None,
     "'Dear friends, a moment of attention.' Russian leaves out 'am', 'is', or 'are' in the present tense, linking 'dear' straight to 'attention'."),
    (1, None,
     "'I want to introduce you to the best chef.' Notice the word order: 'I' comes first, and 'head chef' finishes the sentence."),
    (2, None,
     "'Good evening, dear guests.' Here 'good' sets up the idea, while 'visitors' comes at the end for emphasis."),
    (3, None,
     "'This is Maximilian, an expert in French cuisine.' You'll hear 'this' all the time in the show, here connected with 'kitchen'. And Max jumps in."),
    (4, None,
     "'I am very glad to be here.' Listen for the word meaning 'I' right alongside 'very much' in this line."),
    (5, None,
     "'He kindly agreed to prepare an old dish.' Notice the word order: 'he' comes first, and 'dish' finishes the sentence."),
    (6, None,
     "'We took it from this French book.' Elena puts 'we' up front so the listener immediately catches the tone, followed by 'took'."),
    (7, None,
     "'I chose this dish for us.' Elena puts 'I' up front so the listener immediately catches the tone, followed by 'chose'."),
    (8, None,
     "'This is an excellent choice for tonight.' The first content word means 'this', and 'evening' rounds out the thought."),
    (9, None,
     "'Maximilian will prepare it for us today.' Elena puts 'person name' up front so the listener immediately catches the tone, followed by 'makes'. Then Max replies."),
    (10, None,
     "'I will do everything in the best way.' The key word here means 'I', which Max combines with 'I'll do'."),
    (11, None,
     "'We are waiting for your culinary masterpiece.' The first content word means 'we', and 'masterpiece' rounds out the thought."),
]

TRANSITION = "Now let us listen to the conversation again without interruption."
OUTRO = "The guests are thrilled, but Max now has to actually cook a complex dish."
CLOSING = ("vika", "Мы ждем ваш кулинарный шедевр.")
