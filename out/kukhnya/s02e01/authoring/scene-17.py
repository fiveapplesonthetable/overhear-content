ID = "kukhnya-s02e01-scene-17"
SHOW = "kukhnya"
SEASON = 2
EPISODE = 1
SCENE = 17
TITLE = "Секретный ингредиент  (The Secret Ingredient)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "anja": "anja", "angelina": "angelina"}
LABELS = {"anya": "Шеф", "anja": "Лёва", "angelina": "Костя"}
SOURCE_NAME = "Кухня (Kukhnya) S2.01"
SOURCE_FILE = "sources/kukhnya/s02/e01.ru.dual.srt"
SOURCE_NOTE = "Scene 17"

INTRO = "The chef tastes the spiked tea and immediately recognizes the hidden alcohol. He praises his sous-chef for the clever trick while Kostya delivers a note to Victoria."

STORY = [
    ("anya", "Отличный чай!",
     "Excellent tea!",
     [(233, 'Чай. Чай.')], "adapted"),
    ("anya", "А что это за чай-то?",
     "And what kind of tea is this?",
     [(234, 'А что за чай-то')], "adapted"),
    ("anja", "Это Сенча.",
     "This is Sencha.",
     [(235, 'Сенча')], "adapted"),
    ("anya", "Молодцы, действуем по нашему плану.",
     "Good job, we are acting according to our plan.",
     [(236, 'Молодцы. Действуем по плану.')], "adapted"),
    ("anja", "Давай, Костян, давай, давай!",
     "Come on, Kostyan, come on, come on!",
     [(237, 'Давай, Костян, давай, давай, давай.')], "adapted"),
    ("angelina", "Всё понятно.",
     "Everything is understood.",
     [(238, 'Понятно.')], "adapted"),
    ("anja", "Займись седьмым столиком, пожалуйста.",
     "Take care of the seventh table, please.",
     [(238, 'Займи седьмым столиком, пожалуйста.')], "adapted"),
    ("angelina", "Виктория Сергеевна, это записка вам.",
     "Victoria Sergeyevna, this is a note for you.",
     [(239, 'Виктория Сергеевна, записка вам.')], "adapted"),
    ("anya", "Этот чай очень хорошо успокаивает.",
     "This tea calms very well.",
     [], "new"),
    ("anja", "Я рад, что вам понравилось.",
     "I am glad that you liked it.",
     [], "new"),
    ("anya", "Заварите мне ещё одну чашку.",
     "Brew me one more cup.",
     [], "new"),
    ("anja", "Сейчас всё сделаем.",
     "We will do everything now.",
     [], "new"),
    ("angelina", "А от кого эта записка?",
     "And from whom is this note?",
     [], "new"),
    ("anja", "Просто передай её Виктории Сергеевне.",
     "Just pass it to Victoria Sergeyevna.",
     [], "new"),
]

OPENER = "Let us break down this interaction."

WALK = [
    (0, None,
     "'Excellent tea!' Russian leaves out 'am', 'is', or 'are' in the present tense, linking 'excellent' straight to 'tea'."),
    (1, None,
     "'And what kind of tea is this?' The first content word means 'what', and 'tea' rounds out the thought."),
    (2, None,
     "'This is Sencha.' Here 'this' sets up the idea, while 'sencha' comes at the end for emphasis. Then Chef Viktor replies."),
    (3, None,
     "'Good job, we are acting according to our plan.' Chef Viktor puts 'well done' up front so the listener immediately catches the tone, followed by 'to act'."),
    (4, None,
     "'Come on, Kostyan, come on, come on!' The key word here means 'let's', which Lyova combines with 'Kostyan'."),
    (5, None,
     "'Everything is understood.' Kostya starts with 'clear' and pairs it with 'clear' to make the point clear. And Lyova jumps in."),
    (6, None,
     "'Take care of the seventh table, please.' Lyova puts 'to attend to' up front so the listener immediately catches the tone, followed by 'seventh'."),
    (7, None,
     "'Victoria Sergeyevna, this is a note for you.' Notice the word order: 'Viktoriya' comes first, and 'you' finishes the sentence."),
    (8, None,
     "'This tea calms very well.' Listen for the word meaning 'tea' right alongside 'very much' in this line. Lyova answers straight away."),
    (9, None,
     "'I am glad that you liked it.' The first content word means 'I', and 'pleased' rounds out the thought."),
    (10, None,
     "'Brew me one more cup.' Listen for the word meaning 'brew' right alongside 'to me' in this line."),
    (11, None,
     "'We will do everything now.' In Russian, 'now' leads into 'we'll do' in a very natural everyday phrasing. Then Kostya replies."),
    (12, None,
     "'And from whom is this note?' The key word here means 'whom', which Kostya combines with 'note'."),
    (13, None,
     "'Just pass it to Victoria Sergeyevna.' Lyova puts 'just' up front so the listener immediately catches the tone, followed by 'pass on'."),
]

TRANSITION = "Now let us listen to the conversation again without interruption."
OUTRO = "The kitchen staff successfully manages the boss's temper, allowing the restaurant service to continue smoothly without any further screaming."
CLOSING = ("anja", "Просто передай её Виктории Сергеевне.")
