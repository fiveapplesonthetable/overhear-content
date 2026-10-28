ID = "kukhnya-s01e16-scene-02"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 16
SCENE = 2
TITLE = "Случайный звонок  (An Accidental Call)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "leva": "anja", "guest": "angelina"}
LABELS = {'anya': 'Инспектор', 'leva': 'Вика', 'guest': 'Дмитрий'}
SOURCE_NAME = "Кухня (Kukhnya) S1.16"
SOURCE_FILE = "sources/kukhnya/s01/e16.ru.dual.srt"
SOURCE_NOTE = "Cues."

INTRO = (
    "The fire inspector continues his strict check and rejects several fire extinguishers. The restaurant owner, Dmitry, arrives and demands to know the real reason behind this sudden and aggressive inspection. Let us listen to their conversation in Russian first."
)

STORY = [
    ("anya", "Где ваш огнетушитель?",
     "Where is your fire extinguisher?",
     [(10, 'А где огнетушитель?')], "adapted"),
    ("leva", "Он висел здесь в прошлый раз.",
     "It was hanging here last time.",
     [(11, 'Он же висел у вас в прошлый раз.')], "adapted"),
    ("anya", "Вы что, смеётесь надо мной?",
     "Are you laughing at me?",
     [(12, 'Вы что, издеваетесь, что ли?')], "adapted"),
    ("anya", "Этот не подходит.",
     "This one is not suitable.",
     [(14, 'Не годим.')], "adapted"),
    ("leva", "Вот нормальный огнетушитель.",
     "Here is a normal fire extinguisher.",
     [(15, 'Браку! Ну вот, нормальный огнетушитель.')], "adapted"),
    ("anya", "А где его пломба?",
     "And where is its seal?",
     [(16, 'А пломба где?')], "adapted"),
    ("guest", "Добрый день.",
     "Good afternoon.",
     [], "new"),
    ("guest", "Можно узнать одну вещь?",
     "May I know one thing?",
     [(19, 'А можно узнать, чем вызван столь бурный интерес к пожарной безопасности моего')], "adapted"),
    ("guest", "Почему у вас такой интерес к ресторану?",
     "Why do you have such an interest in the restaurant?",
     [(20, 'ресторана? Можно.')], "adapted"),
    ("anya", "Мы боремся с плохим руководством.",
     "We are fighting with bad management.",
     [(21, 'Интерес вызван борьбой с халатностью руководства,')], "adapted"),
    ("anya", "Был звонок моему начальнику.",
     "There was a call to my boss.",
     [(22, 'а также с безобразным состоянием пожарной техники и звонком моему')], "adapted"),
    ("anya", "Из соседнего ресторана.",
     "From the neighboring restaurant.",
     [(23, 'начальнику из соседнего ресторана.')], "adapted"),
    ("guest", "Всё понятно.",
     "Everything is clear.",
     [(25, 'Понятно.')], "adapted"),
    ("anya", "Ну что, до завтра.",
     "Well then, until tomorrow.",
     [(26, 'Ну что, до завтра.')], "adapted"),
]

OPENER = "Now let us examine the conversation line by line."

WALK = [
    (0, None,
     "'Where is your fire extinguisher?' Notice the word order: 'where' comes first, and 'fire extinguisher' finishes the sentence."),
    (1, None,
     "'It was hanging here last time.' Notice the word order: 'he' comes first, and 'time' finishes the sentence."),
    (2, None,
     "'Are you laughing at me?' A compact expression built around 'you' and 'me'."),
    (3, None,
     "'This one is not suitable.' You'll hear 'is coming up' all the time in the show, here connected with 'is coming up'."),
    (4, None,
     "'Here is a normal fire extinguisher.' The key word here means 'decent', which Vika combines with 'fire extinguisher'."),
    (5, None,
     "'And where is its seal?' A compact expression built around 'where' and 'seal'. Then Dmitry replies."),
    (6, None,
     "'Good afternoon.' Dmitry puts 'good' up front so the listener immediately catches the tone, followed by 'day'."),
    (7, None,
     "'May I know one thing?' In Russian, 'may' leads into 'thing' in a very natural everyday phrasing."),
    (8, None,
     "'Why do you have such an interest in the restaurant?' In Russian, 'why' leads into 'restaurant' in a very natural everyday phrasing."),
    (9, None,
     "'We are fighting with bad management.' A compact expression built around 'we' and 'leadership'."),
    (10, None,
     "'There was a call to my boss.' Listen for the word meaning 'was' right alongside 'call' in this line."),
    (11, None,
     "'From the neighboring restaurant.' Russian leaves out 'am', 'is', or 'are' in the present tense, linking 'neighboring' straight to 'restaurant'. Dmitry answers straight away."),
    (12, None,
     "'Everything is clear.' Notice the word order: 'clear' comes first, and 'clear' finishes the sentence."),
    (13, None,
     "'Well then, until tomorrow.' Listen for the word meaning 'what' right alongside 'tomorrow' in this line."),
]

TRANSITION = "Now let us listen to the conversation once again."
OUTRO = "And that's it for this scene. When you watch the episode, listen out for the exchange around an accidental call, and for the words meaning 'fire extinguisher' and 'to hang'. You'll catch them now. See you next time."
CLOSING = ("anya", "Ну что, до завтра.")
