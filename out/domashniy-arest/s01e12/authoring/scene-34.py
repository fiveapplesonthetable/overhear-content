"""Scene 34 — Sitting Before the Journey (s01e12, 01:07:26–01:17:28)."""

ID = "domashniy-arest-s01e12-scene-34"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 12
SCENE = 34
TITLE = "Присели на дорожку  (Sitting Before the Journey)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.12"
SOURCE_FILE = "sources/domashniy-arest/s01/e12.ru.dual.srt"

VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "samson": "anja",
    "klavdiya": "angelina",
}

LABELS = {
    "anya": "Нина",
    "samson": "Самсон",
    "klavdiya": "Клавдия",
}

INTRO = (
    "In the communal apartment, the Samsonov family finishes packing their bags and sits together "
    "with their neighbor before departing for their new life in Siberia."
)

STORY = [
    ("samson", "Нина, хорош там возиться на кухне!",
     "Nina, stop fussing around in the kitchen!",
     [(868, "Нина, хорош там возиться.")], "Samson calls Nina"),

    ("samson", "Давайте скорее присядем на дорожку.",
     "Come on, let us sit for a moment before the road.",
     [(869, "Давайте, присели на дорожку.")], "tradition of sitting before travel"),

    ("anya", "Я уже собрала все наши вещи.",
     "I have already packed all our things.",
     [], "Nina packed bags"),

    ("klavdiya", "Деткам вы жизнь, конечно, перечеркнули!",
     "You have certainly ruined those children's lives!",
     [(873, "Деткам вы жизнь, конечно, перечеркнули.")], "Klavdiya scolds them"),

    ("klavdiya", "Как вы будете жить в Сибири?",
     "How will you live in Siberia?",
     [(874, "Как они там будут в этой Сибири?")], "dismay over Siberia"),

    ("anya", "Клавдия Викторовна, можете помолчать хотя бы минуту?",
     "Klavdiya Viktorovna, can you be quiet for at least a minute?",
     [(877, "Клавдия Викторовна, вы можете помолчать?")], "Nina asks for quiet"),

    ("samson", "Нина, проверь билеты, паспорта и деньги.",
     "Nina, check the tickets, passports, and money.",
     [(883, "Билеты, паспорта, деньги?")], "checking travel documents"),

    ("anya", "Все наши документы лежат в сумке.",
     "All our documents are lying in the bag.",
     [(884, "Да.")], "documents safe"),

    ("samson", "Такси уже подъехало к нашему дому.",
     "The taxi has already driven up to our house.",
     [(886, "Машина пришла.")], "taxi arrives"),

    ("samson", "Всё, берём чемоданы и выходим!",
     "That is it, we take the suitcases and go out!",
     [(885, "Все, выходим, выходим.")], "departing"),

    ("klavdiya", "Я буду очень скучать по вам.",
     "I will miss you very much.",
     [], "neighbor's affection"),

    ("anya", "Спасибо вам за всё, соседка дорогая.",
     "Thank you for everything, dear neighbor.",
     [], "gratitude expressed"),

    ("samson", "Прощайте, наш старый коммунальный дом!",
     "Farewell, our old communal apartment!",
     [], "farewell to apartment"),

    ("anya", "Начинается наша совершенно новая жизнь.",
     "Our completely new life is beginning.",
     [], "fresh start"),
]

OPENER = "Let's explore the poignant moments before the Samsonovs depart their communal apartment."

WALK = [
    (0, None,
     "'Nina, stop fussing around in the kitchen!' Samsonov urges his wife to hurry up with packing."),
    (1, None,
     "'Come on, let us sit for a moment before the road.' The Russian tradition involves sitting quietly before departing."),
    (2, None,
     "'I have already packed all our things.' Nina confirms that preparations for departure are complete."),
    (3, None,
     "'You have certainly ruined those children's lives!' The elderly neighbor scolds them for moving away."),
    (4, None,
     "'How will you live in Siberia?' Klavdiya expresses dramatic dismay over the distant relocation."),
    (5, None,
     "'Klavdiya Viktorovna, can you be quiet for at least a minute?' Nina politely begs her neighbor to stop nagging."),
    (6, None,
     "'Nina, check the tickets, passports, and money.' Samsonov reminds her of essential travel documents."),
    (7, None,
     "'All our documents are lying in the bag.' Nina reassures Samsonov that everything is secure."),
    (8, None,
     "'The taxi has already driven up to our house.' Samsonov spots their transport waiting outside."),
    (9, None,
     "'That is it, we take the suitcases and go out!' Samsonov announces that it is time to depart."),
    (10, None,
     "'I will miss you very much.' Despite her complaints, Klavdiya feels genuine sadness at their leaving."),
    (11, None,
     "'Thank you for everything, dear neighbor.' Nina embraces her neighbor with warm gratitude."),
    (12, None,
     "'Farewell, our old communal apartment!' Samsonov bids a final farewell to his lifelong home."),
    (13, None,
     "'Our completely new life is beginning.' Nina looks forward with hope to a fresh start."),
]

TRANSITION = "Now let's listen to the emotional communal apartment farewell once more."

OUTRO = "With suitcases packed and farewells spoken, the Samsonov family steps out into their new chapter."

CLOSING = ("anya", "Начинается наша совершенно новая жизнь.")
