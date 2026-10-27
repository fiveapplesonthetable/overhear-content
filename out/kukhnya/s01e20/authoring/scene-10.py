ID = "kukhnya-s01e20-scene-10"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 20
SCENE = 10
TITLE = "Дима ждёт  (Dima is Waiting)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "viktor": "anja"}
LABELS = {"anya": "Хостес", "viktor": "Шеф"}
SOURCE_NAME = "Кухня (Kukhnya) S1.20"
SOURCE_FILE = "sources/kukhnya/s01/e20.ru.dual.srt"
SOURCE_NOTE = "Scene 10"

INTRO = "The hostess spots Chef Viktor and delivers an important message from a celebrity, and we will listen to them in Russian first; do not worry about catching every single word."

STORY = [
    ("anya", "Здравствуйте.",
     "Hello.",
     [], "new"),
    ("viktor", "Доброе утро.",
     "Good morning.",
     [], "new"),
    ("anya", "Шеф, вас ожидают.",
     "Chef, they are waiting for you.",
     [], "new"),
    ("viktor", "Кто меня ждет?",
     "Who is waiting for me?",
     [], "new"),
    ("anya", "Дима тебя ждет.",
     "Dima is waiting for you.",
     [], "new"),
    ("viktor", "Нагиев здесь?",
     "Nagiyev is here?",
     [], "new"),
    ("anya", "Да, он за своим столом.",
     "Yes, he is at his table.",
     [], "new"),
    ("viktor", "Что он хочет?",
     "What does he want?",
     [], "new"),
    ("anya", "Я не знаю.",
     "I do not know.",
     [], "new"),
    ("viktor", "Обычно он сначала звонит.",
     "He usually calls first.",
     [], "new"),
    ("anya", "Он кажется очень взволнованным.",
     "He seems very excited.",
     [], "new"),
    ("viktor", "Хорошо, я иду.",
     "Okay, I am coming.",
     [], "new"),
    ("viktor", "Принеси ему немного кофе.",
     "Bring him some coffee.",
     [], "new"),
]

OPENER = "Let us break down this interaction."

WALK = [
    (0, None,
     "'Hello.' -- She tells him this."),
    (1, None,
     "'Good morning.' -- He says this to her."),
    (2, None,
     "'Chef, they are waiting for you.' -- She talks directly to him."),
    (3, None,
     "'Who is waiting for me?' -- He asks her a question."),
    (4, None,
     "'Dima is waiting for you.' -- She talks directly to him."),
    (5, None,
     "'Nagiyev is here?' -- He asks her a question."),
    (6, None,
     "'Yes, he is at his table.' -- She tells him this."),
    (7, None,
     "'What does he want?' -- He asks her a question."),
    (8, None,
     "'I do not know.' -- She explains her feelings to him."),
    (9, None,
     "'He usually calls first.' -- He says this to her."),
    (10, None,
     "'He seems very excited.' -- She tells him this."),
    (11, None,
     "'Okay, I am coming.' -- He explains his feelings to her."),
    (12, None,
     "'Bring him some coffee.' -- He says this to her."),
]

TRANSITION = "Now let us listen to the conversation again without interruption."
OUTRO = "The chef heads out to the dining room to see what the celebrity wants."
CLOSING = ("viktor", "Принеси ему немного кофе.")
