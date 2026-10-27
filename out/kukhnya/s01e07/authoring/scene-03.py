ID = "kukhnya-s01e07-scene-03"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 7
SCENE = 3
TITLE = "Соседи по квартире  (Roommates)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "kostya": "anja"}
LABELS = {"anya": "Макс", "kostya": "Костя"}
SOURCE_NAME = "Кухня (Kukhnya) S1.07"
SOURCE_FILE = "sources/kukhnya/s01/e07.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 12-23. Sympathizing with Max's homeless predicament, Kostya offers him a spare bedroom "
    "in his apartment, and Max gladly accepts after clarifying that his romance with Nastya was fake."
)

INTRO = (
    "Worried that Max will be caught and fired, Kostya generously offers him a room in his two-bedroom apartment. "
    "Before agreeing, Max clarifies whether Nastya visits frequently, revealing their fake relationship. "
    "Relieved that things are purely platonic, Kostya and Max seal their agreement to become roommates. "
    "Let's listen to their conversation in Russian first."
)

STORY = [
    ("kostya", "Почему ты сразу не рассказал правду?",
     "Why didn't you tell the truth right away?",
     [(12, "Че ты сразу не сказал")], "adapted"),
    ("anya", "Мне было очень стыдно признаться, Костя.",
     "I was very ashamed to admit it, Kostya.",
     [(15, "Мне неудобно")], "adapted"),
    ("kostya", "Переезжай ко мне в большую квартиру.",
     "Move in with me into a big apartment.",
     [(13, "Давай, перебирайся ко мне")], "adapted"),
    ("anya", "Сколько комнат в твоей квартире?",
     "How many rooms are in your apartment?",
     [], "new"),
    ("kostya", "У меня есть две отдельные комнаты.",
     "I have two separate rooms.",
     [(13, "У меня две комнаты")], "adapted"),
    ("anya", "Мы будем платить за квартиру пополам?",
     "Will we pay for the apartment fifty-fifty?",
     [(14, "Платим пополам")], "adapted"),
    ("kostya", "Да, каждый платит ровно половину суммы.",
     "Yes, each pays exactly half the amount.",
     [(14, "Платим пополам")], "adapted"),
    ("anya", "А Настя часто приходит к тебе?",
     "And does Nastya come over to you often?",
     [(16, "У вас там вроде с Настей что-то"), (17, "Она, наверное, тебе приходит")], "adapted"),
    ("kostya", "Она не приходит, мы не встречаемся.",
     "She does not come, we are not dating.",
     [(19, "Не приходит она"), (20, "Мы не встречаемся")], "adapted"),
    ("anya", "Значит, между вами нет серьёзных отношений?",
     "So there is no serious relationship between you?",
     [(21, "мы всем как бы врали")], "adapted"),
    ("kostya", "Мы просто хорошие друзья и коллеги.",
     "We are simply good friends and colleagues.",
     [], "new"),
    ("anya", "Тогда я с радостью согласен переехать!",
     "Then I gladly agree to move in!",
     [(23, "Ладно, говорил. Приезжаю к тебе")], "adapted"),
    ("kostya", "Отлично, сегодня вечером жду твои вещи.",
     "Great, this evening I expect your things.",
     [], "new"),
]

OPENER = "Now let's examine Kostya and Max's roommate agreement line by line."

WALK = [
    (0, None,
     "'Why didn't you tell the truth right away?' Kostya asks why Max kept his homelessness a secret."),
    (1, None,
     "'I was very ashamed to admit it, Kostya.' Max confesses his embarrassment using an impersonal construction."),
    (2, None,
     "'Move in with me into a big apartment.' Kostya extends a generous offer with an imperative verb."),
    (3, None,
     "'How many rooms are in your apartment?' Max inquires about the size of the accommodations."),
    (4, None,
     "'I have two separate rooms.' Kostya confirms the layout using a cardinal numeral and plural noun."),
    (5, None,
     "'Will we pay for the apartment fifty-fifty?' Max checks the financial arrangement with an adverb."),
    (6, None,
     "'Yes, each pays exactly half the amount.' Kostya confirms splitting the expenses equally."),
    (7, None,
     "'And does Nastya come over to you often?' Max checks for awkward romantic entanglements."),
    (8, None,
     "'She does not come, we are not dating.' Kostya clarifies his relationship status with present verbs."),
    (9, None,
     "'So there is no serious relationship between you?' Max confirms the absence of romantic tension."),
    (10, None,
     "'We are simply good friends and colleagues.' Kostya describes their platonic connection with plural nouns."),
    (11, None,
     "'Then I gladly agree to move in!' Max enthusiastically accepts the offer using a short adjective."),
    (12, None,
     "'Great, this evening I expect your things.' Kostya looks forward to welcoming his new roommate."),
]

TRANSITION = "Now let's listen to the roommate agreement again without interruption."
OUTRO = (
    "With an affordable roof over his head, Max celebrates finding his first real home in Moscow "
    "as Kostya looks forward to sharing expenses and having a loyal friend as a roommate."
)
CLOSING = ("kostya", "Отлично, сегодня вечером жду твои вещи.")
