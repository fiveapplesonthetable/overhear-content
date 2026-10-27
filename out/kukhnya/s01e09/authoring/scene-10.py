"""s01e09 scene 10: Папина дочка (Daddy's Girl)."""

ID = "kukhnya-s01e09-scene-10"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 9
SCENE = 10
TITLE = "Папина дочка  (Daddy's Girl)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "chef": "anja", "alisa": "angelina"}
LABELS = {"anya": "Вика", "chef": "Шеф", "alisa": "Алиса"}
SOURCE_NAME = "Кухня (Kukhnya) S1.09"
SOURCE_FILE = "sources/kukhnya/s01/e09.ru.dual.srt"
SOURCE_NOTE = "Cues 224-244. Vika and little Alisa greet restaurant guests with awkward bluntness before Chef Barinov arrives to check the kitchen."

INTRO = (
    "In the elegant dining room of Claude Monet, art director Victoria tries her best to entertain Chef Barinov's outspoken young daughter Alisa. "
    "After the little girl makes hilariously blunt remarks to arriving diners, Chef Barinov appears and immediately heads to the kitchen to demand speed. "
    "Let's listen to their lively exchanges in Russian."
)

STORY = [
    ("anya", "Добрый день, добро пожаловать в ресторан!", "Good afternoon, welcome to the restaurant!",
     [(224, "Добрый день"), (226, "Мы с моей помощницей рады видеть вас в нашем ресторане")], ""),
    ("alisa", "Здравствуйте, а это ваша девушка?", "Hello, is that your girlfriend?",
     [(227, "Здравствуйте"), (229, "А это твоя девушка?")], ""),
    ("anya", "Алиса, веди себя прилично с гостями.", "Alisa, behave decently with the guests.",
     [], ""),
    ("alisa", "У меня был дедушка в Новороссийске.", "I had a grandfather in Novorossiysk.",
     [(230, "У меня тоже был дедушка в Новороссийске")], ""),
    ("alisa", "Но он умер в прошлом году.", "But he died last year.",
     [(231, "Только он умер")], ""),
    ("anya", "А вот наконец и твой папа!", "And here at last is your dad!",
     [(233, "вот и папа")], ""),
    ("alisa", "Папа, пойдём скорее играть со мной!", "Dad, let us go play with me quickly!",
     [(237, "Пап, давай играть")], ""),
    ("chef", "Сначала я проверю работу наших поваров.", "First I will check our cooks' work.",
     [(238, "Давай-ка я сначала посмотрю, как готовят эти инвалиды")], ""),
    ("chef", "Кладите меньше пармезана в это блюдо!", "Put less Parmesan into this dish!",
     [(239, "Меньше пармезана")], ""),
    ("chef", "Соус заказали целых полчаса назад.", "The sauce was ordered a whole half-hour ago.",
     [(241, "Соус полчаса назад заказали")], ""),
    ("chef", "Шевелитесь быстрее, гости долго ждут заказ.", "Move faster, the guests have been waiting long for the order.",
     [(242, "Шевелись")], ""),
    ("alisa", "Папа всегда так громко командует.", "Dad always commands so loudly.",
     [], ""),
    ("anya", "Твой папа — настоящий хозяин кухни.", "Your dad is the true master of the kitchen.",
     [(236, "Папина дочка")], ""),
]

OPENER = "Let's examine how Victoria and young Alisa welcome guests before Chef Barinov inspects the kitchen."

WALK = [
    (1, None,
     "'Hello, is that your girlfriend?' A direct and humorous question demonstrating childish frankness with a demonstrative pronoun."),
    (2, None,
     "'Alisa, behave decently with the guests.' Victoria gently instructs the child with an imperative verb and an instrumental prepositional phrase."),
    (7, None,
     "'First I will check our cooks' work.' A future tense perfective statement showing the chef's dedication to quality in the kitchen."),
    (10, None,
     "'Move faster, the guests have been waiting long for the order.' A brisk imperative followed by an explanation of customer delays for the team."),
]

TRANSITION = "Now, let's hear the lively dining room and kitchen dialogue once more."

OUTRO = (
    "Now you know how to talk about welcoming restaurant guests, childish frankness, and urgent kitchen instructions in Russian. "
    "Listen for these conversational patterns in the upcoming scene."
)

CLOSING = ("chef", "На моей кухне должен быть идеальный порядок.")
