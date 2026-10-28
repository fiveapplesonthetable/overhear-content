ID = "kukhnya-s01e16-scene-10"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 16
SCENE = 10
TITLE = "Побег через зал  (Escape Through the Hall)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "leva": "anja", "dima": "angelina"}
LABELS = {'anya': 'Макс', 'leva': 'Шеф', 'dima': 'Лановский'}
SOURCE_NAME = "Кухня (Kukhnya) S1.16"
SOURCE_FILE = "sources/kukhnya/s01/e16.ru.dual.srt"
SOURCE_NOTE = "Cues 88-131."

INTRO = (
    "Viktor tells the kitchen staff to leave through the back and front doors. But the back door is blocked. An immigration major introduces himself to Viktor. Let us listen to their conversation in Russian first."
)

STORY = [
    ("anya", "Попробуй новый вариант блюда.",
     "Try the new version of the dish.",
     [(88, "попробуй новый вариант, а?")], "adapted"),
    ("anya", "Шеф, выход через зал закрыт.",
     "Chef, the exit through the hall is closed.",
     [(108, "Шеф, с парадом не вариант.")], "adapted"),
    ("leva", "Мы выходим по одному человеку.",
     "We exit one person at a time.",
     [(92, "Не ломимся толпой, выходим по одному человеку.")], "adapted"),
    ("leva", "Половина идёт через зал.",
     "Half goes through the hall.",
     [(97, "Половина через зал.")], "adapted"),
    ("leva", "Что вы за идиоты?",
     "What kind of idiots are you?",
     [(110, "Что вы за инвалиды?")], "adapted"),
    ("leva", "Быстро ко мне в кабинет.",
     "Quickly to my office.",
     [(113, "Ко мне в кабинет, только тихо.")], "adapted"),
    ("dima", "Добрый день, Виктор Петрович.",
     "Good afternoon, Viktor Petrovich.",
     [(117, "О, Виктор Петрович, чрезвычайно рад с вами лично познакомиться.")], "adapted"),
    ("dima", "Я майор миграционной службы.",
     "I am a major of the migration service.",
     [(121, "майор федеральной миграционной службы.")], "adapted"),
    ("dima", "Мы можем пройти в кабинет?",
     "Can we go to the office?",
     [(124, "Виктор Петрович, мы не могли бы пройти в ваш кабинет и обсудить все там?")], "adapted"),
    ("leva", "К сожалению, я не могу.",
     "Unfortunately, I cannot.",
     [(125, "К сожалению, не могу.")], "adapted"),
    ("leva", "Мне нужно готовить для гостей.",
     "I need to cook for the guests.",
     [(127, "Простите, мне нужно готовить для гостей нашего замечательного ареста.")], "adapted"),
    ("dima", "Хорошо, я подожду вас здесь.",
     "Alright, I will wait for you here.",
     [(131, "Я, с вашего позволения, подожду вас здесь.")], "adapted"),
]

OPENER = "Now let us examine the conversation line by line."

WALK = [
    (0, None,
     "'Try the new version of the dish.' The first content word means 'to try', and 'of dish' rounds out the thought."),
    (1, None,
     "'Chef, the exit through the hall is closed.' Notice the word order: 'chef' comes first, and 'is closed' finishes the sentence. Chef Viktor answers straight away."),
    (2, None,
     "'We exit one person at a time.' In Russian, 'we' leads into 'person' in a very natural everyday phrasing."),
    (3, None,
     "'Half goes through the hall.' Chef Viktor starts with 'half' and pairs it with 'goes' to make the point clear."),
    (4, None,
     "'What kind of idiots are you?' The key word here means 'what', which Chef Viktor combines with 'you'."),
    (5, None,
     "'Quickly to my office.' Chef Viktor starts with 'quickly' and pairs it with 'to me' to make the point clear."),
    (6, None,
     "'Good afternoon, Viktor Petrovich.' the speaker puts 'good' up front so the listener immediately catches the tone, followed by 'day'."),
    (7, None,
     "'I am a major of the migration service.' In Russian, 'I' leads into 'service' in a very natural everyday phrasing."),
    (8, None,
     "'Can we go to the office?' The first content word means 'we', and 'office' rounds out the thought."),
    (9, None,
     "'Unfortunately, I cannot.' A compact expression built around 'regret' and 'can'."),
    (10, None,
     "'I need to cook for the guests.' Listen for the word meaning 'to me' right alongside 'necessary' in this line."),
    (11, None,
     "'Alright, I will wait for you here.' the speaker uses the polite plural 'you' here alongside 'good', keeping a formal or respectful tone."),
]

TRANSITION = "Now let us listen to the conversation once again."
OUTRO = "And that's it for this scene. When you watch the episode, listen out for the exchange around escape through the hall, and for the words meaning 'to try' and 'new'. You'll catch them now. See you next time."
CLOSING = ("dima", "Хорошо, я подожду вас здесь.")
