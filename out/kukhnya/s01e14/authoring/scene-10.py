ID = "kukhnya-s01e14-scene-10"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 14
SCENE = 10
TITLE = "Заказ для гостей  (Order for the Guests)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "gost": "anja"}
LABELS = {"anya": "Костя", "gost": "Гость"}
SOURCE_NAME = "Кухня (Kukhnya) S1.14"
SOURCE_FILE = "sources/kukhnya/s01/e14.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 170-171. Kostya delivers the gourmet French dishes to the VIP table "
    "in the dining room, where the guests express their delight with the cuisine."
)

INTRO = (
    "In the dining room of Claude Monet, Kostya arrives at the VIP table carrying the exquisite French meals. "
    "The guests eagerly examine their food, while Kostya politely presents each course on behalf of the kitchen. "
    "Let us listen to their conversation in Russian first."
)

STORY = [
    ("anya", "Господа, вот ваши редкие французские блюда.",
     "Gentlemen, here are your rare French dishes.",
     [(170, "Господа, филиминьон по-фламански и лангусты а-ля Франце.")], "adapted"),
    ("gost", "Ого, как красиво лежит горячее мясо!",
     "Wow, how beautifully the hot meat lies!",
     [], "new"),
    ("anya", "Наш повар старался приготовить настоящий шедевр.",
     "Our cook tried to prepare a real masterpiece.",
     [], "new"),
    ("gost", "Рыба тоже выглядит невероятно аппетитно и вкусно.",
     "The fish also looks incredibly appetizing and tasty.",
     [], "new"),
    ("anya", "Мы всегда используем только самые лучшие продукты.",
     "We always use only the best products.",
     [], "new"),
    ("gost", "Передайте шеф-повару нашу искреннюю благодарность.",
     "Pass on our sincere gratitude to the head chef.",
     [], "new"),
    ("anya", "Обязательно скажу ему эти приятные слова.",
     "I will certainly tell him these pleasant words.",
     [], "new"),
    ("gost", "Мы хотим заказать ещё бутылку вина.",
     "We want to order another bottle of wine.",
     [], "new"),
    ("anya", "Я сейчас быстро принесу ваше вино.",
     "I will quickly bring your wine right now.",
     [], "new"),
    ("gost", "Спасибо за вашу прекрасную работу здесь.",
     "Thank you for your wonderful work here.",
     [], "new"),
    ("anya", "Приятного аппетита и хорошего вечера вам!",
     "Bon appétit and have a good evening!",
     [], "new"),
    ("gost", "Спасибо, мы обязательно вернёмся сюда снова.",
     "Thank you, we will definitely return here again.",
     [], "new"),
    ("anya", "Мы всегда очень рады видеть вас!",
     "We are always very glad to see you!",
     [], "new"),
]

OPENER = "Now let us examine Kostya and the guest's polite conversation line by line."

WALK = [
    (0, None,
     "'Gentlemen, here are your rare French dishes.' -- Kostya presents the special culinary courses at the VIP table."),
    (1, None,
     "'Wow, how beautifully the hot meat lies!' -- The guest marvels at the attractive arrangement on the plate."),
    (2, None,
     "'Our cook tried to prepare a real masterpiece.' -- The waiter proudly highlights the high quality of the cooking."),
    (3, None,
     "'The fish also looks incredibly appetizing and tasty.' -- The diner compliments the second course brought to the table."),
    (4, None,
     "'We always use only the best products.' -- Kostya explains the restaurant's strict standards for quality ingredients."),
    (5, None,
     "'Pass on our sincere gratitude to the head chef.' -- The satisfied guest asks that their compliments reach the kitchen."),
    (6, None,
     "'I will certainly tell him these pleasant words.' -- The waiter promises to relay the appreciative feedback to the chef."),
    (7, None,
     "'We want to order another bottle of wine.' -- The diners decide to pair their dinner with more fine wine."),
    (8, None,
     "'I will quickly bring your wine right now.' -- Kostya accepts the drink order and prepares to fetch the bottle."),
    (9, None,
     "'Thank you for your wonderful work here.' -- The customer expresses appreciation for the attentive and polite service."),
    (10, None,
     "'Bon appétit and have a good evening!' -- The waiter offers traditional polite wishes for the table's dining experience."),
    (11, None,
     "'Thank you, we will definitely return here again.' -- The impressed guest declares their intention to visit Claude Monet soon."),
    (12, None,
     "'We are always very glad to see you!' -- Kostya warmly welcomes their promised return before heading back to the bar."),
]

TRANSITION = "Now let us listen to Kostya and the guest once again."
OUTRO = (
    "Pleasantly greeted and satisfied with their delicious French meals, the VIP diners settle in "
    "for an enjoyable dinner while Kostya heads off to fulfill their wine order."
)
CLOSING = ("anya", "Мы всегда очень рады видеть вас!")
