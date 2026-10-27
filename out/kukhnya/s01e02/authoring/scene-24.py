"""Scene 24 — The Crusader's Sword (s01e02, 00:19:09–00:20:57)."""

ID = "kukhnya-s01e02-scene-24"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 2
SCENE = 24
TITLE = "Меч крестоносца  (The Crusader's Sword)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Кухня (Kukhnya) S1.02"
SOURCE_FILE = "sources/kukhnya/s01/e02.ru.dual.srt"

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
    "In the elegant dining room of Claude Monet, panic erupts when an influential guest discovers "
    "a filleting knife baked inside his fish, threatening the restaurant with immediate disaster."
)

STORY = [
    ("chef", "В зале гость нашёл нож в рыбе!",
     "In the dining room a guest found a knife in the fish!",
     [(253, "Там рыбий нож нашли.")], "Kitchen alert"),

    ("anya", "Шеф, нужно срочно что-то делать.",
     "Chef, we must urgently do something.",
     [(256, "Нужно что-то делать.")], "Max urges action"),

    ("chef", "Я сам пойду в зал.",
     "I will go out to the dining room myself.",
     [(260, "Я шеф-повар этого ресторана.")], "Chef goes to hall"),

    ("guest", "Вы объясните мне, что это такое?",
     "Will you explain to me what this is?",
     [(261, "Вы не объясните мне, что это.")], "Guest questions"),

    ("anya", "Позвольте мне всё объяснить гостю.",
     "Allow me to explain everything to the guest.",
     [(262, "А позвольте я, шеф.")], "Max intervenes"),

    ("anya", "Перед вами уникальный старинный рецепт.",
     "Before you is a unique ancient recipe.",
     [(264, "уникальный рецепт более чем с тысячелетней")], "Max begins tale"),

    ("anya", "Крестоносцы готовили рыбу прямо на мечах.",
     "The Crusaders prepared fish right on their swords.",
     [(268, "нанизывания ее на лезвие меча.")], "Crusader legend"),

    ("guest", "Да, это действительно очень вкусно!",
     "Yes, this is indeed very delicious!",
     [(271, "Да, действительно.")], "Guest delighted"),

    ("guest", "Это настоящая поэзия высокой кухни.",
     "This is true poetry of haute cuisine.",
     [(272, "Это же настоящая поэзия кулинарии.")], "Guest praises"),

    ("guest", "Принесите мне ещё одну такую рыбу!",
     "Bring me another fish just like this!",
     [(275, "А можно мне такую же рыбу?")], "Guest reorders"),

    ("chef", "Сейчас всё сделаем, приятного аппетита.",
     "We will prepare everything right away, bon appetit.",
     [(277, "Приятного аппетита.")], "Chef closes sale"),

    ("chef", "Макс, пошли скорее на кухню.",
     "Max, let's head quickly to the kitchen.",
     [(276, "Макс, пошли.")], "Chef retreats"),

    ("anya", "Шеф, вы назвали меня по имени!",
     "Chef, you called me by my name!",
     [(278, "Шеф, а вы меня по именем назвали.")], "Max notices name"),

    ("chef", "Огузок, без спроса не выходи в зал!",
     "Runt, do not come out to the dining room without permission!",
     [(279, "если ты еще раз без моего разрешения")], "Chef's warning"),
]

OPENER = "Let's explore the kitchen emergency and Max's brilliant storytelling."

WALK = [
    (0, None,
     "'In the dining room a guest found a knife in the fish!' The kitchen staff realizes an enormous disaster is unfolding."),
    (1, None,
     "'Chef, we must urgently do something.' Max alerts the head chef to the catastrophic mistake."),
    (2, None,
     "'I will go out to the dining room myself.' Barinov braces himself to confront the outraged guest."),
    (3, None,
     "'Will you explain to me what this is?' The wealthy diner angrily demands an explanation for the blade."),
    (4, None,
     "'Allow me to explain everything to the guest.' Max boldly steps forward to take command of the crisis."),
    (5, None,
     "'Before you is a unique ancient recipe.' Max begins weaving an astonishing historical legend."),
    (6, None,
     "'The Crusaders prepared fish right on their swords.' The young cook invents a glamorous medieval culinary technique."),
    (7, None,
     "'Yes, this is indeed very delicious!' Tasting the fish, the enchanted patron expresses immense delight."),
    (8, None,
     "'This is true poetry of haute cuisine.' The guest completely buys into the captivating story."),
    (9, None,
     "'Bring me another fish just like this!' The guest enthusiastically orders a second portion."),
    (10, None,
     "'We will prepare everything right away, bon appetit.' Barinov smoothly closes the sale with immense relief."),
    (11, None,
     "'Max, let's head quickly to the kitchen.' The head chef hurries his clever rookie back to safety."),
    (12, None,
     "'Chef, you called me by my name!' Max proudly notices that Barinov recognized his true identity."),
    (13, None,
     "'Runt, do not come out to the dining room without permission!' Barinov reasserts authority while hiding his relief."),
]

TRANSITION = "Now let's listen to the high-stakes dining room confrontation once more."

OUTRO = "Saved from disaster by quick thinking, Max earns grudging respect from the head chef."

CLOSING = ("chef", "Огузок, без спроса не выходи в зал!")
