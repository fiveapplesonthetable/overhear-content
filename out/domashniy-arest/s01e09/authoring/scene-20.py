"""s01e09 scene 20: Цветы и фотографии (outside communal apartment)."""

ID = "domashniy-arest-s01e09-scene-20"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 9
SCENE = 20
TITLE = "Цветы и фотографии  (Flowers and Photos)"
LEVEL = "beginner"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "danya": "anja"}
LABELS = {"anya": "Нина", "danya": "Даня"}
SOURCE_NAME = "Домашний арест, Сезон 1, Эпизод 9"
SOURCE_FILE = "sources/domashniy-arest/s01/e09.ru.dual.srt"
SOURCE_NOTE = "Cues 643-665 (00:35:15-00:35:54). Danya brings flowers to Nina and asks for a selfie, but she angrily rejects him."

INTRO = (
    "Previously, Nina's marriage reached a breaking point as Samson walked out after seeing online photos. "
    "Meanwhile, outside the communal apartment, young neighbor Danya approaches Nina with a bouquet of flowers, "
    "hoping to take another photo together for social media."
)

STORY = [
    ("danya", "Привет, Нина! Это красивые цветы тебе.",
     "Hello, Nina! These beautiful flowers are for you.",
     [(643, "Привет"), (645, "Это мне")], "adapted cues 643 and 645"),
    ("anya", "Ой, спасибо! Они очень приятно пахнут.",
     "Oh, thank you! They smell very nice.",
     [(646, "Спасибо"), (647, "ой, как пахнут вкусно")], "adapted cues 646-647"),
    ("danya", "Они тебе очень идут.",
     "They suit you very well.",
     [(648, "Мне идет, да?")], "turned into statement"),
    ("danya", "Давай сфотографируемся на фоне дома!",
     "Let's take a photo in front of the house!",
     [(650, "На фоне дома сфоткаемся")], "expanded cue 650"),
    ("danya", "Ты же любишь красивые фотографии?",
     "You like beautiful photos, don't you?",
     [(651, "Ну, ты же любишь фотографировать, да?")], "adapted cue 651"),
    ("danya", "Мы наберём много лайков в интернете.",
     "We will gather many likes on the internet.",
     [(653, "Лайков наберем")], "added в интернете"),
    ("anya", "Подожди. Зачем ты это делаешь?",
     "Wait. Why are you doing this?",
     [], "suspicious pause"),
    ("danya", "Ты чего? Что случилось?",
     "What is wrong with you? What happened?",
     [(656, "Ты чего?")], "added Что случилось?"),
    ("anya", "Ты разрушил мою семью своими фотографиями!",
     "You destroyed my family with your photos!",
     [(658, "своим дебильным инстаграмом"), (659, "мне семью разрушил")], "cleaned cue 658"),
    ("anya", "Муж увидел твой глупый снимок.",
     "My husband saw your foolish snapshot.",
     [(660, "Тебя кто-то просил?")], "explanatory line"),
    ("danya", "Я просто хотел похвастаться.",
     "I simply wanted to show off.",
     [(661, "похвастаться хотел")], "added Я просто"),
    ("anya", "Между нами ничего не будет!",
     "There will never be anything between us!",
     [(663, "Между нами ничего нет, не было и не будет")], "shortened cue 663"),
    ("anya", "Уходи отсюда, я не хочу тебя видеть.",
     "Get out of here, I do not want to see you.",
     [(664, "Я тебя видеть не хочу"), (665, "Дрись мне отсюда")], "cleaned cues 664-665"),
]

OPENER = "Let's see how Danya's romantic selfie attempt turns into a furious rejection."

WALK = [
    (0, None,
     "'Hello, Nina! These beautiful flowers are for you.' Danya approaches her with a flattering gift."),
    (1, None,
     "'Oh, thank you! They smell very nice.' Nina is briefly touched by the sweet aroma."),
    (2, None,
     "'They suit you very well.' The dative construction expresses that something flatters someone."),
    (3, None,
     "'Let's take a photo in front of the house!' Danya eagerly suggests another photo opportunity."),
    (4, None,
     "'You like beautiful photos, don't you?' The particle appeals to her known preferences."),
    (5, None,
     "'We will gather many likes on the internet.' The future verb indicates collecting social approval."),
    (6, None,
     "'Wait. Why are you doing this?' Nina suddenly stops and questions his underlying motives."),
    (7, None,
     "'What is wrong with you? What happened?' Danya is surprised by her sudden shift in mood."),
    (8, None,
     "'You destroyed my family with your photos!' Nina accuses him of causing Samson to leave."),
    (9, None,
     "'My husband saw your foolish snapshot.' The past tense verb reveals Samson's discovery."),
    (10, None,
     "'I simply wanted to show off.' Danya weakly explains his vain desire for attention."),
    (11, None,
     "'There will never be anything between us!' Nina firmly shuts down any romantic illusions."),
    (12, None,
     "'Get out of here, I do not want to see you.' The imperative orders him to leave immediately."),
]

TRANSITION = "Now listen to the tense confrontation in front of the house once more."
OUTRO = "Nina sends Danya packing with his flowers, distraught over her shattered marriage."
CLOSING = ("anya", "Уходи отсюда, я не хочу тебя видеть.")
