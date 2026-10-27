"""s01e02 scene 12: Гнев шеф-повара (The Head Chef's Wrath)."""

ID = "kukhnya-s01e02-scene-12"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 2
SCENE = 12
TITLE = "Гнев шеф-повара  (The Head Chef's Wrath)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "senya": "anja", "fedya": "angelina"}
LABELS = {"anya": "Шеф", "senya": "Сеня", "fedya": "Федя"}
SOURCE_NAME = "Кухня (Kukhnya) S1.02"
SOURCE_FILE = "sources/kukhnya/s01/e02.ru.dual.srt"
SOURCE_NOTE = "Cues 169-178. Chef Barinov storms into the kitchen furious about his stolen knife and the improvised dish."

INTRO = (
    "Furious that someone took his prized Japanese chef's knife and served an unauthorized dish, Viktor Barinov storms back into the kitchen. "
    "Confronting cooks Senya and Fedya, Barinov maliciously lies that the rival chef found their fricassee utterly revolting, "
    "triggering a frantic blame game between the panicked staff. Let's listen in Russian first."
)

STORY = [
    ("anya", "Вы украли мой любимый японский нож!",
     "You stole my favorite Japanese knife!",
     [(169, "нож мой сперли")], "accusing the kitchen staff"),
    ("anya", "И вы совершенно испортили моё блюдо!",
     "And you completely ruined my dish!",
     [(169, "блюдо мое испохабили")], "chastising their cooking"),
    ("anya", "А вы все быстро вышли отсюда!",
     "And all of you get out of here quickly!",
     [(170, "А вы все вышли")], "clearing out the onlookers"),
    ("senya", "Шеф, мы хотели как лучше!",
     "Chef, we were only trying to help!",
     [(171, "Шеф"), (172, "Мы как лучше хотели")], "pleading innocence"),
    ("anya", "Мне плевать, чего вы там хотели!",
     "I do not care what you were trying to do!",
     [(173, "Да мне плевать, что вы хотели")], "dismissing their excuses"),
    ("anya", "Знаете, что гостья сказала про фрикасе?",
     "Do you know what the guest said about the fricassee?",
     [(174, "Знаете, что она сказала про ваше фрикассе")], "setting up his malicious lie"),
    ("fedya", "Она была в полном восторге?",
     "Was she completely delighted?",
     [], "hoping for praise"),
    ("anya", "Она сказала, что оно отвратительно!",
     "She said that it was disgusting!",
     [(175, "Что оно отвратительно")], "dropping the hammer"),
    ("senya", "Шеф, а я им сразу говорил!",
     "Chef, I told them right away!",
     [(176, "Шеф, а я им сразу сказал")], "shifting blame to Fedya"),
    ("fedya", "Это Сеня готовил этот ужасный соус!",
     "It was Senya who made that terrible sauce!",
     [], "blaming Senya back"),
    ("senya", "Нет, Федя сам жарил эту куропатку!",
     "No, Fedya roasted that partridge himself!",
     [], "pointing the finger"),
    ("anya", "Хватит спорить! Вы все плохие повара!",
     "Stop arguing! You are all terrible cooks!",
     [(178, "Вы инвалиды")], "insulting them together"),
    ("anya", "Убирайтесь с моей кухни прямо сейчас!",
     "Get out of my kitchen right now!",
     [], "kicking them out"),
]

OPENER = "Let's replay a few lines to examine key phrases and vocabulary."

WALK = [
    (2, "А вы все быстро вышли отсюда!",
     "'And all of you get out of here quickly!' Chef Barinov bellows, clearing the line in fury."),
    (3, "Шеф, мы хотели как лучше!",
     "'Chef, we were only trying to help!' Senya pleads defensively."),
    (7, "Она сказала, что оно отвратительно!",
     "'She said that it was disgusting!' Barinov lies gleefully to terrify his subordinate cooks."),
    (8, "Шеф, а я им сразу говорил!",
     "'Chef, I told them right away!' Senya exclaims, instantly throwing his fellow cooks under the bus."),
]

TRANSITION = "Now listen to the full kitchen confrontation once more."

OUTRO = "Senya and Fedya scurry away as Barinov stands alone fuming in the kitchen."

CLOSING = ("anya", "На моей кухне командую только я.")
