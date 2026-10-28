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
     "'Where is your fire extinguisher?' — Notice the adverb meaning 'where' paired with the det for 'your'."),
    (1, None,
     "'It was hanging here last time.' — Notice the pronoun meaning 'he' paired with the verb for 'to hang, be hanging'."),
    (2, None,
     "'Are you laughing at me?' — Notice the pronoun meaning 'you' paired with the pronoun for 'what'."),
    (3, None,
     "'This one is not suitable.' — Notice the det meaning 'this' paired with the verb for 'is coming up, is approaching'."),
    (4, None,
     "'Here is a normal fire extinguisher.' — Notice the adjective meaning 'decent, normal' paired with the noun for 'fire extinguisher'."),
    (5, None,
     "'And where is its seal?' — Notice the adverb meaning 'where' paired with the pronoun for 'him'."),
    (6, None,
     "'Good afternoon.' — Notice the adjective meaning 'good' paired with the noun for 'day'."),
    (7, None,
     "'May I know one thing?' — Notice the adverb meaning 'may, can' paired with the verb for 'to find out'."),
    (8, None,
     "'Why do you have such an interest in the restaurant?' — Notice the adverb meaning 'why' paired with the pronoun for 'you'."),
    (9, None,
     "'We are fighting with bad management.' — Notice the pronoun meaning 'we' paired with the verb for 'to fight, struggle'."),
    (10, None,
     "'There was a call to my boss.' — Notice the verb meaning 'was' paired with the noun for 'call; bell'."),
    (11, None,
     "'From the neighboring restaurant.' — Notice the adjective meaning 'neighboring' paired with the noun for 'restaurant'."),
    (12, None,
     "'Everything is clear.' — Notice the det meaning 'everything' paired with the adverb for '(is) clear'."),
    (13, None,
     "'Well then, until tomorrow.' — Notice the pronoun meaning 'what' paired with the adverb for 'tomorrow'."),
]

TRANSITION = "Now let us listen to the conversation once again."
OUTRO = "The conversation concludes the matter at hand."
CLOSING = ("anya", "Ну что, до завтра.")
