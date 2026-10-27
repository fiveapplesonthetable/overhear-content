"""s01e08 scene 14: Вежливый шеф (The Polite Chef)."""

ID = "kukhnya-s01e08-scene-14"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 8
SCENE = 14
TITLE = "Вежливый шеф  (The Polite Chef)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "senya": "anja", "sasha": "angelina"}
LABELS = {"anya": "Елена", "senya": "Сеня", "sasha": "Саша"}
SOURCE_NAME = "Кухня (Kukhnya) S1.08"
SOURCE_FILE = "sources/kukhnya/s01/e08.ru.dual.srt"
SOURCE_NOTE = "Cues 163-184. Acting chef Elena treats the kitchen brigade with polite respect and resolves a service delay."

INTRO = (
    "While Chef Barinov is away, guest chef Elena Sokolova introduces a remarkably calm and respectful atmosphere to Claude Monet's kitchen. "
    "Praising the cooks and gently managing an urgent food ticket for waitress Sasha, Elena demonstrates an entirely different leadership style. "
    "Let's listen to their polite kitchen dialogue in Russian."
)

STORY = [
    ("anya", "Фёдор, приготовьте две порции креветок.", "Fyodor, prepare two portions of shrimp.",
     [(163, "приготовьте, пожалуйста, еще две порции креветок")], ""),
    ("senya", "Шеф должен кричать на поваров!", "A chef should shout at cooks!",
     [(166, "шеф должен орать на подчиненных")], ""),
    ("anya", "Арсений, вы заслуживаете достойного обращения.", "Arseny, you deserve respectful treatment.",
     [(169, "вы профессионалы и заслуживаете достойного обращения")], ""),
    ("senya", "Но на кухне нужна строгая дисциплина.", "But strict discipline is needed in the kitchen.",
     [], ""),
    ("anya", "У вас самое чистое рабочее место.", "You have the cleanest workstation.",
     [(168, "у вас самое чистое рабочее место")], ""),
    ("sasha", "Где горячее блюдо для третьего столика?", "Where is the hot dish for table three?",
     [(170, "Где моя бобовая косуля, в конце концов")], ""),
    ("sasha", "Гости ждут уже сорок минут!", "The guests have been waiting forty minutes already!",
     [(176, "Гости уже 40 минут")], ""),
    ("anya", "Саша, спокойно, давайте глубоко дышать.", "Sasha, calmly, let us breathe deeply.",
     [(172, "спокойно, спокойно"), (173, "Давайте дышать")], ""),
    ("anya", "Это блюдо готовится больше часа.", "This dish takes over an hour to cook.",
     [(178, "готовится больше часа")], ""),
    ("sasha", "Они грозятся уйти без оплаты.", "They threaten to leave without paying.",
     [(171, "Если я сегодня останусь без чаевых")], ""),
    ("anya", "Попросите гостей подождать ещё немного.", "Ask the guests to wait a little longer.",
     [(180, "попросите их еще подождать")], ""),
    ("anya", "Новый заказ: куропатка и грибы.", "New order: partridge and mushrooms.",
     [(182, "Новый заказ. Куропатка"), (183, "грибами в белом соусе")], ""),
    ("senya", "Мы всё сделаем вовремя, шеф!", "We will make everything on time, chef!",
     [(184, "Да, шеф")], ""),
]

OPENER = "Let's observe how Elena Sokolova introduces calm professionalism and constructive compliments to the restaurant kitchen."

WALK = [
    (2, None,
     "'Arseny, you deserve respectful treatment.' The polite address uses the formal plural pronoun and a verb governing genitive case."),
    (4, None,
     "'You have the cleanest workstation.' The superlative adjective phrase highlights excellence in workplace cleanliness."),
    (7, None,
     "'Sasha, calmly, let us breathe deeply.' Elena de-escalates kitchen tension using an encouraging imperative and a reassuring tone."),
    (10, None,
     "'Ask the guests to wait a little longer.' The polite imperative guides the front-of-house staff with an infinitive complement."),
]

TRANSITION = "Now, let's review Elena's respectful kitchen guidance once more."

OUTRO = (
    "Now you understand how to communicate with respect, handle kitchen rush orders, and calm flustered colleagues in Russian. "
    "Listen for these professional phrases in the next scene."
)

CLOSING = ("anya", "Вежливость всегда даёт отличный результат.")
