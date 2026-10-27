"""s01e05 scene 10: Тайное поручение (A Secret Errand)."""

ID = "kukhnya-s01e05-scene-10"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 5
SCENE = 10
TITLE = "Тайное поручение  (A Secret Errand)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "chef": "anja"}
LABELS = {"anya": "Макс", "chef": "Шеф"}
SOURCE_NAME = "Кухня (Kukhnya) S1.05"
SOURCE_FILE = "sources/kukhnya/s01/e05.ru.dual.srt"
SOURCE_NOTE = "Cues 141-144. Chef Barinov gives Max a secret errand to fetch cognac from the bar."

INTRO = (
    "During a hectic evening service at Claude Monet, Chef Viktor Barinov pulls junior cook Max aside. "
    "Desperate for a drink during his demanding shift, Barinov orders Max to secretly fetch a bottle of cognac from the bar. "
    "Let's listen to their conspiratorial dialogue in Russian first."
)

STORY = [
    ("chef", "Слушай, Огузок, подойди ко мне.", "Listen, Oguzok, come here to me.",
     [(141, "Слушай, Агузик")], ""),
    ("anya", "Да, шеф! Что нужно сделать?", "Yes, chef! What needs to be done?",
     [], ""),
    ("chef", "Сходи в бар и принеси коньяк.", "Go to the bar and bring cognac.",
     [(141, "ходи в бар, принеси коньяк")], ""),
    ("anya", "Какой именно коньяк вам нужен?", "Which cognac exactly do you need?",
     [], ""),
    ("chef", "Я написал название на этой бумажке.", "I wrote the name on this piece of paper.",
     [(142, "Я для идиотов тут название написал")], ""),
    ("anya", "А если кто-то заметит меня?", "And what if someone notices me?",
     [], ""),
    ("chef", "В бар сходи для отвода глаз.", "Go to the bar to keep up appearances.",
     [(144, "В бар сходи для отвода глаз")], ""),
    ("anya", "А что сказать бармену Косте?", "And what should I say to bartender Kostya?",
     [], ""),
    ("chef", "Скажи, что это для мясного соуса.", "Say that this is for meat sauce.",
     [], ""),
    ("anya", "Понял, сделаю всё быстро и тихо.", "Understood, I will do everything quickly and quietly.",
     [], ""),
    ("chef", "И фаршируй рыбу жюльеном с лимоном.", "And stuff the fish with julienne and lemon.",
     [(143, "Фаршируй рыбу жульеном с лимоном")], ""),
    ("chef", "Потом ставь её в горячую духовку.", "Then put it into the hot oven.",
     [(143, "и ставь ее в духовку")], ""),
    ("anya", "Слушаюсь, шеф, уже бегу!", "Right away, chef, I'm already running!",
     [], ""),
]

OPENER = "Let's examine how Chef Barinov issues disguised commands to his cook."

WALK = [
    (2, None,
     "'Go to the bar and bring cognac.' The chef uses two imperative verbs joined by the conjunction 'and' to give clear orders to his cook."),
    (4, None,
     "'I wrote the name on this piece of paper.' The past tense verb indicates completed action, and the preposition specifies the location."),
    (6, None,
     "'Go to the bar to keep up appearances.' This Russian idiom means doing something purely as a diversion so nobody suspects the truth."),
    (10, None,
     "'And stuff the fish with julienne and lemon.' The verb is in the imperative mood, followed by the direct object in the accusative case."),
]

TRANSITION = "Okay, let's hear the full kitchen exchange once more."

OUTRO = (
    "Now you know how Barinov disguises his drinking habits as culinary tasks. "
    "Listen for these phrases next time you watch the episode."
)

CLOSING = ("anya", "Никто ничего не должен узнать.")
