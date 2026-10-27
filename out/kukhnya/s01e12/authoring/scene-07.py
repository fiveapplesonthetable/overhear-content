"""s01e12 scene 07: На кухне шефа (In the Chef's Kitchen)."""

ID = "kukhnya-s01e12-scene-07"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 12
SCENE = 7
TITLE = "На кухне шефа  (In the Chef's Kitchen)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "chef": "anja"}
LABELS = {"anya": "Сеня", "chef": "Шеф"}
SOURCE_NAME = "Кухня (Kukhnya) S1.12"
SOURCE_FILE = "sources/kukhnya/s01/e12.ru.dual.srt"
SOURCE_NOTE = "Cues 64-72. Chef Viktor Barinov furiously scolds his line cooks over messy prep stations and demands total discipline."

INTRO = (
    "During the busy afternoon prep shift at Claude Monet, Chef Viktor Barinov storms through the kitchen, furious about mess and delays. "
    "Catching his cooks hesitating at their stations, Barinov aggressively reprimands Senya and demands strict kitchen discipline. "
    "Let's listen to their fast-paced kitchen exchange in Russian."
)

STORY = [
    ("chef", "Сеня, почему ты стоишь без дела?", "Senya, why are you standing doing nothing?",
     [], "new"),
    ("anya", "Я жду нужные специи для мяса.", "I am waiting for the needed spices for the meat.",
     [], "new"),
    ("chef", "Ты ждёшь, пока гном насыпет корицу?", "Are you waiting until a gnome sprinkles cinnamon?",
     [(64, "насыпет корицу")], "adapted"),
    ("anya", "Шеф, я всё делаю быстро.", "Chef, I do everything quickly.",
     [(65, "Ну, шеф")], "adapted"),
    ("chef", "Тогда работай быстрее и не стой.", "Then work faster and do not stand around.",
     [(66, "Сам ты")], "adapted"),
    ("chef", "И всегда убирай за собой стол.", "And always clean up your table.",
     [(67, "убирай за собой")], "adapted"),
    ("anya", "Шеф, говорите немного тише, пожалуйста.", "Chef, please speak a bit quieter.",
     [(68, "потише бы")], "adapted"),
    ("chef", "Не надо учить меня дисциплине!", "Do not teach me discipline!",
     [(69, "Учи меня еще")], "adapted"),
    ("anya", "Мы просто очень стараемся для вас.", "We are simply trying very hard for you.",
     [], "new"),
    ("chef", "На моей кухне должен быть идеальный порядок.", "There must be perfect order in my kitchen.",
     [], "new"),
    ("anya", "Мы сейчас же всё уберём, шеф.", "We will clean everything up right now, chef.",
     [], "new"),
    ("chef", "Спокойнее, я проверю каждое блюдо лично.", "Calm down, I will check every dish personally.",
     [(71, "Покойнее")], "adapted"),
]

OPENER = "Let's explore how Chef Barinov demands discipline and reprimands his cooks for kitchen slowdowns."

WALK = [
    (2, None,
     "'Are you waiting until a gnome sprinkles cinnamon?' A sarcastic rhetorical question criticizing hesitation at the prep station for the cook."),
    (5, None,
     "'And always clean up your table.' An authoritative imperative demanding cleanliness at the workstation from the team."),
    (6, None,
     "'Chef, please speak a bit quieter.' A polite imperative with a comparative adverb requesting lowered volume in the kitchen."),
    (9, None,
     "'There must be perfect order in my kitchen.' A firm modal statement establishing high professional standards for the restaurant brigade."),
]

TRANSITION = "Now, let's hear Chef Barinov command his kitchen brigade once more."

OUTRO = (
    "Now you know how to give urgent kitchen commands, address mess at workstations, and ask for quiet in Russian. "
    "Listen for these intense workplace phrases in the upcoming scene."
)

CLOSING = ("chef", "Работаем без лишних разговоров.")
