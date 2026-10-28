ID = "kukhnya-s01e16-scene-03"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 16
SCENE = 3
TITLE = "Ответный удар  (Strike Back)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "leva": "anja"}
LABELS = {'anya': 'Дмитрий', 'leva': 'Шеф'}
SOURCE_NAME = "Кухня (Kukhnya) S1.16"
SOURCE_FILE = "sources/kukhnya/s01/e16.ru.dual.srt"
SOURCE_NOTE = "Cues."

INTRO = (
    "Realizing that the neighboring Italian restaurant, Arcobaleno, ordered the fake fire inspection, Dmitry decides to take revenge. He angrily calls the immigration service with a fake complaint against his rivals. Let us listen to their conversation in Russian first."
)

STORY = [
    ("anya", "Вы хотите войну?",
     "Do you want a war?",
     [(27, 'Война и хотите, будет вам война.')], "adapted"),
    ("anya", "Будет вам война.",
     "There will be a war for you.",
     [(27, 'будет вам война.')], "adapted"),
    ("anya", "Алло, добрый день.",
     "Hello, good afternoon.",
     [(28, 'Алло, за что вам, интересно, деньги платят в вашем ФМСе?')], "adapted"),
    ("anya", "За что вам платят деньги?",
     "For what do they pay you money?",
     [(28, 'за что вам, интересно, деньги платят в вашем ФМСе?')], "adapted"),
    ("anya", "Вы куда смотрите?",
     "Where are you looking?",
     [(29, 'Вы куда смотрите?')], "adapted"),
    ("anya", "В моём дворе мигранты.",
     "There are migrants in my courtyard.",
     [(29, 'В моем дворе гастарбайтеры из ресторана')], "adapted"),
    ("anya", "Из ресторана Аркабалена.",
     "From the restaurant Arcobaleno.",
     [(30, 'Аркабалена')], "adapted"),
    ("anya", "Они режут живого барана.",
     "They are slaughtering a live ram.",
     [(30, 'барана режут живого.')], "adapted"),
    ("anya", "А вы там спите?",
     "And are you sleeping there?",
     [(31, 'А вы что, там спите?')], "adapted"),
    ("anya", "Приезжайте быстро.",
     "Come quickly.",
     [], "new"),
    ("anya", "Аркабалена.",
     "Arcobaleno.",
     [(32, 'Аркабалена.')], "adapted"),
    ("leva", "Что ты делаешь?",
     "What are you doing?",
     [], "new"),
    ("anya", "Я решаю наши проблемы.",
     "I am solving our problems.",
     [], "new"),
    ("leva", "Молодец, так держать.",
     "Well done, keep it up.",
     [], "new"),
]

OPENER = "Now let us examine the conversation line by line."

WALK = [
    (0, None,
     "'Do you want a war?' A compact expression built around 'you' and 'the war'."),
    (1, None,
     "'There will be a war for you.' Notice the word order: 'will be' comes first, and 'a war' finishes the sentence."),
    (2, None,
     "'Hello, good afternoon.' Here 'hello?' sets up the idea, while 'day' comes at the end for emphasis."),
    (3, None,
     "'For what do they pay you money?' In Russian, 'what' leads into 'money' in a very natural everyday phrasing."),
    (4, None,
     "'Where are you looking?' The question word for 'where to' comes right at the start, followed directly by 'look'."),
    (5, None,
     "'There are migrants in my courtyard.' Dmitry starts with 'yard' and pairs it with 'migrant' to make the point clear."),
    (6, None,
     "'From the restaurant Arcobaleno.' Dmitry puts 'restaurant' up front so the listener immediately catches the tone, followed by 'Arcobaleno'."),
    (7, None,
     "'They are slaughtering a live ram.' Here 'they' sets up the idea, while 'ram' comes at the end for emphasis."),
    (8, None,
     "'And are you sleeping there?' Listen for the word meaning 'you' right alongside 'there' in this line."),
    (9, None,
     "'Come quickly.' Notice the word order: 'to come' comes first, and 'quickly' finishes the sentence."),
    (10, None,
     "'Arcobaleno.' Listen for the word meaning 'Arcobaleno' right alongside 'Arcobaleno' in this line."),
    (11, None,
     "'What are you doing?' The first content word means 'what', and 'are you doing' rounds out the thought."),
    (12, None,
     "'I am solving our problems.' A compact expression built around 'I' and 'problems'. Chef Viktor answers straight away."),
    (13, None,
     "'Well done, keep it up.' In Russian, 'well done' leads into 'to keep' in a very natural everyday phrasing."),
]

TRANSITION = "Now let us listen to the conversation once again."
OUTRO = "And that's it for this scene. When you watch the episode, listen out for the exchange around strike back, and for the words meaning 'want' and 'the war'. You'll catch them now. See you next time."
CLOSING = ("leva", "Молодец, так держать.")
