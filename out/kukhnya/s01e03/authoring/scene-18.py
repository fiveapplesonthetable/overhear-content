"""Scene 18 — The Festive Goose (s01e03, 00:20:59–00:21:00)."""

ID = "kukhnya-s01e03-scene-18"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 3
SCENE = 18
TITLE = "Праздничный гусь  (The Festive Goose)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Кухня (Kukhnya) S1.03"
SOURCE_FILE = "sources/kukhnya/s01/e03.ru.dual.srt"
SOURCE_NOTE = (
    "Cue 319. In the dining room of Claude Monet, Chef Viktor Barinov proudly presents "
    "the roasted banquet goose to the VIP guest, while Max breathes a deep sigh of relief."
)

VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "chef": "anja",
    "guest": "angelina",
}

LABELS = {
    "anya": "Макс",
    "chef": "Шеф",
    "guest": "Гость",
}

INTRO = (
    "Inside the glamorous dining room of Claude Monet, the high-stakes VIP banquet reaches its long-awaited peak. "
    "Chef Viktor Barinov personally escorts the golden roasted goose to the guest of honor, "
    "proudly presenting the culinary triumph that nearly cost the kitchen staff their sanity. "
    "Let's listen to this proud dining room presentation in Russian first."
)

STORY = [
    ("guest", "Скажите, пожалуйста, это мой праздничный гусь?",
     "Tell me please, is that my festive goose?",
     [(319, "Это мой гусь?")], "Guest inquires"),

    ("chef", "Да, это ваш главный заказ сегодня!",
     "Yes, this is your main order today!",
     [], "Chef confirms"),

    ("chef", "Мы готовили его по старинному рецепту.",
     "We prepared it according to an ancient recipe.",
     [], "Culinary tradition"),

    ("anya", "Наш шеф лично проверял каждую деталь.",
     "Our chef personally checked every detail.",
     [], "Max praises chef"),

    ("guest", "Гусь выглядит и пахнет просто великолепно!",
     "The goose looks and smells simply magnificent!",
     [], "Guest is impressed"),

    ("chef", "Мясо получилось очень нежным и сочным.",
     "The meat turned out very tender and juicy.",
     [], "Chef highlights quality"),

    ("anya", "Мы подали его с яблоками и травами.",
     "We served it with apples and herbs.",
     [], "Garnish details"),

    ("guest", "Мои гости будут в полном восторге!",
     "My guests will be in total delight!",
     [], "Guest expects praise"),

    ("chef", "Наш ресторан держит только высший уровень.",
     "Our restaurant maintains only the highest standard.",
     [], "Chef's pride"),

    ("guest", "Спасибо вам за прекрасную работу, повара!",
     "Thank you for the wonderful work, chefs!",
     [], "Gratitude expressed"),

    ("chef", "Приятного аппетита вам и вашим гостям!",
     "Bon appetit to you and your guests!",
     [], "Chef's blessing"),

    ("anya", "Надеемся увидеть вас снова в ресторане.",
     "We hope to see you again at the restaurant.",
     [], "Max bids farewell"),

    ("chef", "Макс, живо возвращайся обратно на кухню!",
     "Max, quickly get back to the kitchen!",
     [], "Chef sends Max back"),
]

OPENER = "Now let's examine Chef Barinov's proud presentation in the dining room line by line."

WALK = [
    (0, None,
     "'Tell me please, is that my festive goose?' The banquet host asks with eager anticipation as the platter arrives."),
    (1, None,
     "'Yes, this is your main order today!' Barinov announces the centerpiece dish with theatrical confidence."),
    (2, None,
     "'We prepared it according to an ancient recipe.' The head chef adds prestige to the dish by citing tradition."),
    (3, None,
     "'Our chef personally checked every detail.' Max supports his mentor by emphasizing the chef's close attention."),
    (4, None,
     "'The goose looks and smells simply magnificent!' The delighted diner marvels at the enticing aroma and plating."),
    (5, None,
     "'The meat turned out very tender and juicy.' Barinov assures the guest that the texture is completely flawless."),
    (6, None,
     "'We served it with apples and herbs.' Max describes the classic culinary accompaniments on the platter."),
    (7, None,
     "'My guests will be in total delight!' The patron expresses profound satisfaction with the banquet presentation."),
    (8, None,
     "'Our restaurant maintains only the highest standard.' Barinov proudly defends Claude Monet's elite reputation."),
    (9, None,
     "'Thank you for the wonderful work, chefs!' The guest graciously thanks the culinary team for their effort."),
    (10, None,
     "'Bon appetit to you and your guests!' Barinov delivers the classic parting wish of haute cuisine."),
    (11, None,
     "'We hope to see you again at the restaurant.' Max politely welcomes the guest back for future visits."),
    (12, None,
     "'Max, quickly get back to the kitchen!' Barinov snaps back into stern chef mode and hustles his rookie inside."),
]

TRANSITION = "Now let's listen to this triumphant dining room exchange once more without interruption."

OUTRO = (
    "With the prized goose triumphantly served and the banquet saved from disaster, "
    "Barinov and Max return to the kitchen to wrap up an eventful first week."
)

CLOSING = ("chef", "Макс, живо возвращайся обратно на кухню!")
