"""s01e09 scene 29: Директор этого бедлама (kindergarten undercover)."""

ID = "domashniy-arest-s01e09-scene-29"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 9
SCENE = 29
TITLE = "Директор этого бедлама  (Director of This Madhouse)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "ilona": "angelina", "officer": "anja"}
LABELS = {"anya": "Землинкин", "ilona": "Илона", "officer": "Сотрудник"}
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.09"
SOURCE_FILE = "sources/domashniy-arest/s01/e09.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 756-775 (00:42:47-00:44:08). Learning that Ilona is arriving in five minutes to inspect the daycare, "
    "the FSB agents scramble because all real children were sent to the water park. "
    "An undercover operative poses as Director Valery Petrovich Zemlinkin, hastily rehearsing with big agent Grisha, "
    "and welcomes Ilona to look around the messy facility."
)

INTRO = (
    "Just after sending the daycare children off to the water park, the security team receives alarming news: "
    "Ilona is arriving in minutes to enroll her child, sent by suspicious politicians to verify the facility. "
    "An agent hastily assumes the role of daycare director Zemlinkin to maintain cover. "
    "Let's listen to this tense undercover greeting in Russian first; don't worry about catching every word."
)

STORY = [
    ("officer", "Давайте, давайте, живее, ребята!",
     "Come on, come on, faster, guys!",
     [(757, "Давайте, давайте, живее, ребята")], "verbatim cue 757"),
    ("officer", "Она будет через пять минут тут.",
     "She will be here in five minutes.",
     [(761, "она будет через пять минут тут")], "adapted cue 761"),
    ("anya", "Детей вернуть не успеем.",
     "We will not make it back with the children in time.",
     [(762, "Детей вернуть не успеем")], "verbatim cue 762"),
    ("anya", "Что же нам делать?",
     "What on earth should we do?",
     [(763, "Что же делать-то")], "adapted cue 763"),
    ("officer", "Я пока фургон отгоню.",
     "I will move the van away for now.",
     [(764, "я пока фургон отгоню")], "adapted cue 764"),
    ("anya", "Ищи зайчика, Гриша!",
     "Look for the little bunny, Grisha!",
     [(766, "Ищи зайчика, Гриша")], "verbatim cue 766"),
    ("anya", "Добрый волк ищет зайчика.",
     "The kind wolf is looking for the bunny.",
     [(767, "Волк ищет зайчика")], "expanded cue 767"),
    ("ilona", "Здравствуйте! Можно войти?",
     "Hello! May I come in?",
     [(768, "Здравствуйте")], "expanded cue 768"),
    ("anya", "Здравствуйте! Я Валерий Петрович.",
     "Hello! I am Valery Petrovich.",
     [(769, "Здравствуйте"), (770, "Землинкин Валерий Петрович")], "adapted cues 769-770"),
    ("anya", "Я директор этого бедлама.",
     "I am the director of this madhouse.",
     [(770, "директор этого бедлама")], "adapted cue 770"),
    ("ilona", "Дочь хочу к вам в садик записать.",
     "I want to enroll my daughter in your daycare.",
     [(772, "Дочь хочу к вам в детский садик записать")], "shortened cue 772"),
    ("anya", "Прекрасно! Проходите, пожалуйста.",
     "Wonderful! Come in, please.",
     [(773, "Прекрасно")], "expanded cue 773"),
    ("anya", "Извините, у нас тут небольшой бардак.",
     "Excuse us, we have a bit of a mess here.",
     [(773, "у нас не всегда такой бардак")], "adapted cue 773"),
    ("anya", "Мы просто к утреннику готовимся.",
     "We are simply preparing for the morning show.",
     [(774, "Мы просто к утреннику готовимся")], "adapted cue 774"),
    ("anya", "Осмотритесь, если хотите.",
     "Have a look around if you wish.",
     [(775, "осмотритесь")], "adapted cue 775"),
]

OPENER = "Let us break down this frantic undercover setup step by step to see how the operative manages the crisis."

WALK = [
    (0, None,
     "'Come on, come on, faster, guys!' The comparative adverb literally means more lively, functioning as an urgent spur."),
    (1, None,
     "'She will be here in five minutes.' The preposition indicates the interval of time elapsed before an event takes place."),
    (2, None,
     "'We will not make it back with the children in time.' The perfective verb expresses having sufficient time."),
    (3, None,
     "'What on earth should we do?' The conversational particle adds expressive emphasis to the rhetorical question."),
    (4, None,
     "'I will move the van away for now.' The temporal adverb means for the time being or meanwhile."),
    (5, None,
     "'Look for the little bunny, Grisha!' The imperative form expresses an urgent instruction during the fake rehearsal."),
    (6, None,
     "'The kind wolf is looking for the bunny.' The diminutive noun for bunny carries an affectionate nursery tone."),
    (7, None,
     "'Hello! May I come in?' The predicative word is used with an infinitive to ask for polite permission."),
    (8, None,
     "'Hello! I am Valery Petrovich.' Addressing oneself by first name and patronymic is standard formal Russian etiquette."),
    (9, None,
     "'I am the director of this madhouse.' The colloquial Russian noun denotes total chaos or an untidy madhouse."),
    (10, None,
     "'I want to enroll my daughter in your daycare.' The infinitive verb takes the accusative case for the person enrolled."),
    (11, None,
     "'Wonderful! Come in, please.' The polite plural imperative invites an arriving guest to step inside."),
    (12, None,
     "'Excuse us, we have a bit of a mess here.' The polite apology is followed by a candid description of clutter."),
    (13, None,
     "'We are simply preparing for the morning show.' The preposition takes the dative case for an upcoming event."),
    (14, None,
     "'Have a look around if you wish.' The reflexive imperative invites the visitor to inspect the room."),
]

TRANSITION = "Now let us listen to the complete scene again, from the frantic scramble to the smooth polite greeting."
OUTRO = ("Director Zemlinkin successfully welcomes Ilona inside, concealing the absence of actual children. "
         "Great job mastering these lively conversational phrases in Russian.")
CLOSING = ("anya", "Осмотритесь, если хотите.")
