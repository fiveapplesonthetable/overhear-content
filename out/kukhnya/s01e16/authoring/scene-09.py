ID = "kukhnya-s01e16-scene-09"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 16
SCENE = 9
TITLE = "Проверка у конкурентов  (Inspection at the Rivals)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "leva": "anja", "dima": "angelina"}
LABELS = {'anya': 'Елена', 'leva': 'Инспектор', 'dima': 'Шеф'}
SOURCE_NAME = "Кухня (Kukhnya) S1.16"
SOURCE_FILE = "sources/kukhnya/s01/e16.ru.dual.srt"
SOURCE_NOTE = "Cues 62-87."

INTRO = (
    "A migration inspector finishes his check at Elena's restaurant. He is very impressed. He says there are no illegal workers. They decide to eat at Claude Monet. Let us listen to their conversation in Russian first."
)

STORY = [
    ("leva", "Ваш ресторан будет отличным.",
     "Your restaurant will be excellent.",
     [(62, "Ну что же, уважаемая Елена Павловна, мне кажется, что ваш ресторан будет..."), (63, "весьма успешным.")], "adapted"),
    ("anya", "Мы все делаем правильно.", "We do everything right.", [], "new"),
    ("anya", "Большое спасибо вам.",
     "Thank you very much.",
     [(64, "Спасибо.")], "adapted"),
    ("leva", "Вы меня очень удивили.",
     "You really surprised me.",
     [(66, "Признаюсь, вы меня очень сильно удивили.")], "adapted"),
    ("leva", "Ни одного повара без документов.",
     "Not a single cook without documents.",
     [(67, "Ни одного нелегального работника на кухне.")], "adapted"),
    ("anya", "Я привыкла работать по закону.",
     "I got used to working by the law.",
     [(68, "Дело в том, что я очень долго работала за границей и привыкла,"), (69, "чтобы все было по закону.")], "adapted"),
    ("leva", "Мне было очень приятно.",
     "It was very pleasant for me.",
     [(72, "Мне было чрезвычайно приятно с вами познакомиться.")], "adapted"),
    ("leva", "Пойдём в другой ресторан?",
     "Let us go to another restaurant?",
     [(74, "Может, мы еще куда-нибудь прогуляемся?")], "adapted"),
    ("leva", "Тут есть Клод Моне.",
     "Here is Claude Monet.",
     [(75, "В этом же здании есть ресторан."), (76, "Клод Мане.")], "adapted"),
    ("anya", "Отлично, люблю французскую кухню.",
     "Excellent, I love French cuisine.",
     [(77, "Отлично. Я обожаю французскую кухню.")], "adapted"),
    ("dima", "К нам идёт проверка!",
     "An inspection is coming to us!",
     [(79, "К нам идет проверка ФМС.")], "adapted"),
    ("dima", "Все без документов, вон!",
     "Everyone without documents, get out!",
     [(84, "Все нелегалы немедленно вон из ресторана.")], "adapted"),
]

OPENER = "Now let us examine the conversation line by line."

WALK = [
    (0, None,
     "'Your restaurant will be excellent.' the speaker uses the polite plural 'you' here alongside 'restaurant', keeping a formal or respectful tone. Elena answers straight away."),
    (1, None,
     "'We do everything right.' Notice the word order: 'we' comes first, and 'right' finishes the sentence."),
    (2, None,
     "'Thank you very much.' Listen for the word meaning 'big' right alongside 'thank you' in this line."),
    (3, None,
     "'You really surprised me.' Here 'to surprise' uses the plural past-tense ending, which also serves for the polite 'you'."),
    (4, None,
     "'Not a single cook without documents.' The key word here means 'alone', which the speaker combines with 'cook'."),
    (5, None,
     "'I got used to working by the law.' The first content word means 'I', and 'law' rounds out the thought."),
    (6, None,
     "'It was very pleasant for me.' the speaker starts with 'to me' and pairs it with 'was' to make the point clear."),
    (7, None,
     "'Let us go to another restaurant?' In Russian, 'let's go' leads into 'restaurant' in a very natural everyday phrasing."),
    (8, None,
     "'Here is Claude Monet.' The key word here means 'here', which the speaker combines with 'there is'."),
    (9, None,
     "'Excellent, I love French cuisine.' Here 'perfect' sets up the idea, while 'kitchen' comes at the end for emphasis. Chef Viktor answers straight away."),
    (10, None,
     "'An inspection is coming to us!' Listen for the word meaning 'us' right alongside 'goes' in this line."),
    (11, None,
     "'Everyone without documents, get out!' Russian leaves out 'am', 'is', or 'are' in the present tense, linking 'documents' straight to 'documents'."),
]



TRANSITION = "Now let us listen to the conversation once again."
OUTRO = "And that's it for this scene. When you watch the episode, listen out for the exchange around inspection at the rivals, and for the words meaning 'restaurant' and 'will be'. You'll catch them now. See you next time."
CLOSING = ("dima", "Все без документов, вон!")
