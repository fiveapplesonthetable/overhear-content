"""s01e03 scene 09: Разговор у барной стойки (Conversation at the Bar)."""

ID = "kukhnya-s01e03-scene-09"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 3
SCENE = 9
TITLE = "Разговор у барной стойки  (Conversation at the Bar)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "kostya": "anja"}
LABELS = {"anya": "Макс", "kostya": "Костя"}
SOURCE_NAME = "Кухня (Kukhnya) S1.03"
SOURCE_FILE = "sources/kukhnya/s01/e03.ru.dual.srt"
SOURCE_NOTE = "Cues 213-220. Bartender Kostya talks sense into Max about his unrealistic crush on Vika."

INTRO = (
    "At the Claude Monet bar counter, novice cook Max vents his romantic frustrations about art director Vika. "
    "Bartender Kostya tries to inject some harsh reality into Max's daydreaming, arguing that glamorous Vika is completely out of his league. "
    "Let's listen to their conversation in Russian first."
)

STORY = [
    ("kostya", "Расслабься, друг, не нервничай так.",
     "Relax, my friend, do not be so nervous.",
     [(213, "Расслабься")], "trying to calm Max down"),
    ("anya", "Он просто хочет меня позлить.",
     "He simply wants to get a rise out of me.",
     [(214, "меня позлить хочет")], "venting his frustration"),
    ("kostya", "Ты не обижайся на мои слова.",
     "Do not take offense at my words.",
     [(215, "Ты без обид")], "prefacing his blunt advice"),
    ("anya", "Что ты хочешь мне сказать?",
     "What do you want to tell me?",
     [], "asking tensely"),
    ("kostya", "Она никогда не выберет тебя.",
     "She would never choose you.",
     [(216, "она бы не в жизни")], "stating the hard truth"),
    ("anya", "Почему ты так уверен в этом?",
     "Why are you so confident about this?",
     [], "demanding justification"),
    ("kostya", "Она красивая и взрослая женщина.",
     "She is a beautiful and mature woman.",
     [], "pointing out the gap"),
    ("kostya", "А ты просто бедный молодой повар.",
     "And you are simply a broke young cook.",
     [], "describing Max's standing"),
    ("anya", "Я знаю её совсем с другой стороны.",
     "I know her from a completely different side.",
     [(217, "Я-то знаю")], "hinting at their night together"),
    ("kostya", "Хочешь выпить со мной сока?",
     "Do you want to drink some juice with me?",
     [(218, "Выпить хочешь")], "offering a refreshment"),
    ("anya", "Нет, спасибо, я сейчас на работе.",
     "No, thank you, I am at work right now.",
     [(219, "Нет, спасибо")], "declining politely"),
    ("kostya", "Ну, как знаешь, твоё дело.",
     "Well, suit yourself, it is your business.",
     [(220, "как хочешь")], "shrugging it off"),
    ("anya", "Я всё равно поговорю с ней.",
     "I will still talk with her anyway.",
     [], "resolving to pursue Vika"),
]

OPENER = "Let's replay a few lines to examine key phrases and vocabulary."

WALK = [
    (0, "Расслабься, друг, не нервничай так.",
     "'Relax, my friend, do not be so nervous,' Kostya advises, using the imperative form of the reflexive verb."),
    (1, "Он просто хочет меня позлить.",
     "'He simply wants to get a rise out of me,' Max replies, explaining his visible frustration."),
    (9, "Хочешь выпить со мной сока?",
     "'Do you want to drink some juice with me?' the bartender offers generously to distract his friend."),
    (10, "Нет, спасибо, я сейчас на работе.",
     "'No, thank you, I am at work right now,' Max answers responsibly, declining the drink."),
]

TRANSITION = "Now listen to the full bar conversation once more."

OUTRO = "Kostya wipes down the counter as Max remains lost in thought."

CLOSING = ("anya", "Я не собираюсь сдаваться так просто.")
