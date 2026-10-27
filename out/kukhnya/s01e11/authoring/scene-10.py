"""s01e11 scene 10: Подозрительная гостья (A Suspicious Guest)."""

ID = "kukhnya-s01e11-scene-10"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 11
SCENE = 10
TITLE = "Подозрительная гостья  (A Suspicious Guest)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "chef": "anja"}
LABELS = {"anya": "Вика", "chef": "Шеф"}
SOURCE_NAME = "Кухня (Kukhnya) S1.11"
SOURCE_FILE = "sources/kukhnya/s01/e11.ru.dual.srt"
SOURCE_NOTE = "Cues 152-158. Victoria and Chef Barinov closely watch a solitary woman dining at Claude Monet, wondering if she is the food critic."

INTRO = (
    "A stylish woman sits alone in the Claude Monet dining room, speaking quietly on her mobile phone while observing her surroundings. "
    "Watching her intently from the entrance, Chef Barinov and Victoria struggle to determine whether she is the dreaded restaurant critic. "
    "Let's listen to their nervous discussion in Russian."
)

STORY = [
    ("chef", "Вика, посмотри на ту даму.", "Vika, look at that lady.",
     [], ""),
    ("anya", "Ну как она себя ведёт?", "Well, how is she behaving?",
     [(152, "как она?")], ""),
    ("chef", "Вроде всё совершенно нормально.", "Everything seems completely fine.",
     [(152, "Вроде нормально")], ""),
    ("anya", "Она долго говорит по телефону.", "She is talking on the phone for a long time.",
     [], ""),
    ("chef", "Она просто обедает в нашем зале.", "She is simply dining in our dining room.",
     [(154, "Я в Клотмана обедаю")], ""),
    ("anya", "Но она ничего не ест.", "But she is not eating anything.",
     [], ""),
    ("chef", "Может быть, блюдо слишком горячее?", "Maybe the dish is too hot?",
     [], ""),
    ("anya", "Она только что попросила счёт.", "She just asked for the bill.",
     [], ""),
    ("chef", "Она ресторанный критик или нет?", "Is she a restaurant critic or not?",
     [(158, "или нет?")], ""),
    ("anya", "Мы до сих пор не уверены.", "We are still not sure.",
     [], ""),
    ("chef", "Нужно срочно выяснить всю правду.", "We need to urgently find out the whole truth.",
     [], ""),
    ("anya", "Я сейчас же всё узнаю, шеф.", "I will find out everything right now, chef.",
     [], ""),
]

OPENER = "Let's explore how Chef Barinov and Victoria analyze the suspicious visitor sitting in the restaurant."

WALK = [
    (1, None,
     "'Well, how is she behaving?' An interrogative inquiry about the guest's conduct in the dining room."),
    (4, None,
     "'She is simply dining in our dining room.' A descriptive present tense statement about the customer's activity for the staff."),
    (8, None,
     "'Is she a restaurant critic or not?' A direct alternative question expressing acute uncertainty about the visitor's true identity."),
    (10, None,
     "'We need to urgently find out the whole truth.' An impersonal modal phrase indicating pressing necessity for the restaurant team."),
]

TRANSITION = "Now, let's hear Victoria and Chef Barinov discuss the guest once more."

OUTRO = (
    "Now you know how to discuss dining behavior, express uncertainty, and talk about investigations in Russian. "
    "Listen for these watchful workplace expressions in the upcoming scene."
)

CLOSING = ("chef", "Нам нельзя делать ни одной ошибки.")
