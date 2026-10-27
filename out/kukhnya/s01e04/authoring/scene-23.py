"""Scene 23 — Max's Dismissal (s01e04, 00:22:40–00:23:25)."""

ID = "kukhnya-s01e04-scene-23"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 4
SCENE = 23
TITLE = "Увольнение Макса  (Max's Dismissal)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Кухня (Kukhnya) S1.04"
SOURCE_FILE = "sources/kukhnya/s01/e04.ru.dual.srt"

VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "chef": "anja",
    "nastya": "angelina",
}

LABELS = {
    "anya": "Макс",
    "chef": "Шеф",
    "nastya": "Настя",
}

INTRO = (
    "In his private office, Chef Viktor Barinov confides in his pet fish Arkady, "
    "while a dejected Max packs his bag in the locker room, receiving heartfelt comfort from waitress Nastya."
)

STORY = [
    ("chef", "Только ты, Аркадий, меня понимаешь.",
     "Only you, Arkady, understand me.",
     [(317, "Только ты, Аркадий, меня и понимаешь.")], "Barinov talks to fish"),

    ("chef", "Вокруг меня одни лентяи и придурки!",
     "Around me are only slackers and fools!",
     [], "Barinov vents"),

    ("nastya", "Максим, ты куда сейчас собираешься?",
     "Maxim, where are you getting ready to go now?",
     [(318, "Ты куда?")], "Nastya asks"),

    ("anya", "Куда-нибудь, шеф меня только что уволил.",
     "Anywhere, the chef just fired me.",
     [(319, "Куда-нибудь. Меня только что уволили.")], "Max explains"),

    ("nastya", "Может быть, шеф просто неудачно пошутил?",
     "Maybe the chef was just joking unsuccessfully?",
     [(320, "А может, он пошутил?")], "Nastya hopes"),

    ("anya", "Нет, он никогда так не шутит.",
     "No, he never jokes like that.",
     [(321, "Он нас любит шутить.")], "Max responds"),

    ("nastya", "Я очень не хочу, чтобы ты уходил!",
     "I really do not want you to leave!",
     [(327, "Максим, я не хочу, чтобы ты уходил.")], "Nastya protests"),

    ("anya", "Я тоже хотел остаться на этой кухне.",
     "I also wanted to stay in this kitchen.",
     [(328, "Я тоже.")], "Max admits"),

    ("nastya", "Давай я спрячу тебя прямо здесь!",
     "Let me hide you right here!",
     [(325, "Я тебя спрячу.")], "Nastya offers"),

    ("anya", "Спасибо, Настя, но прятаться глупо.",
     "Thank you, Nastya, but hiding is silly.",
     [], "Max declines"),

    ("nastya", "Ты главное не переживай из-за шефа.",
     "The main thing is do not worry because of the chef.",
     [(329, "Ты не переживай.")], "Nastya comforts"),

    ("nastya", "Теперь у тебя в ресторане есть я!",
     "Now you have me in the restaurant!",
     [(330, "Теперь у тебя есть я.")], "Nastya pledges"),

    ("anya", "Спасибо за поддержку, ты настоящий друг.",
     "Thank you for the support, you are a true friend.",
     [], "Max thanks"),

    ("nastya", "Мы обязательно что-нибудь придумаем!",
     "We will definitely come up with something!",
     [], "Nastya promises"),
]

OPENER = "Let's explore Chef Barinov's venting and Nastya's comforting words to Max."

WALK = [
    (0, None,
     "'Only you, Arkady, understand me.' Barinov confides his deep frustrations to his goldfish."),
    (1, None,
     "'Around me are only slackers and fools!' The temperamental chef vents about the kitchen staff."),
    (2, None,
     "'Maxim, where are you getting ready to go now?' Nastya finds Max packing up his backpack."),
    (3, None,
     "'Anywhere, the chef just fired me.' Max sadly shares the bad news about his termination."),
    (4, None,
     "'Maybe the chef was just joking unsuccessfully?' Nastya tries to offer a ray of hope."),
    (5, None,
     "'No, he never jokes like that.' Max knows Barinov was dead serious about the firing."),
    (6, None,
     "'I really do not want you to leave!' Nastya expresses her deep sadness over his departure."),
    (7, None,
     "'I also wanted to stay in this kitchen.' Max admits his culinary dream has been crushed."),
    (8, None,
     "'Let me hide you right here!' Nastya playfully proposes smuggling him inside the restaurant."),
    (9, None,
     "'Thank you, Nastya, but hiding is silly.' Max smiles gently at her sweet but impractical plan."),
    (10, None,
     "'The main thing is do not worry because of the chef.' Nastya encourages Max to stay positive."),
    (11, None,
     "'Now you have me in the restaurant!' The kind waitress vows to always stand by his side."),
    (12, None,
     "'Thank you for the support, you are a true friend.' Max is deeply moved by her loyalty."),
    (13, None,
     "'We will definitely come up with something!' Nastya refuses to give up hope for his return."),
]

TRANSITION = "Now let's listen to the locker room farewell and touching conversation once more."

OUTRO = "Comforted by Nastya's loyal support, Max prepares to leave Claude Monet behind."

CLOSING = ("nastya", "Мы обязательно что-нибудь придумаем!")
