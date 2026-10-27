"""s01e16 scene 20: Штраф и депортация (Fine and Deportation)."""

ID = "kukhnya-s01e16-scene-20"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 16
SCENE = 20
TITLE = "Штраф и депортация  (Fine and Deportation)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "kostya": "anja"}
LABELS = {"anya": "Шеф", "kostya": "Инспектор"}
SOURCE_NAME = "Кухня (Kukhnya) S1.16"
SOURCE_FILE = "sources/kukhnya/s01/e16.ru.dual.srt"
SOURCE_NOTE = "Cues 271-276. The migration inspector brings Louis to Chef Barinov, announcing a heavy fine for the restaurant and deportation for the pastry chef."

INTRO = (
    "Marching the caught pastry chef into Chef Barinov's office, the migration inspector scolds Viktor Petrovich for trying to hide his undocumented staff. "
    "Instead of letting the restaurant off with a simple warning, the officer announces a steep fine and orders Louis to be sent back home. "
    "Let's listen to their confrontation in Russian."
)

STORY = [
    ("kostya", "Вот я и нашёл вашего повара.", "Here, I found your chef.",
     [(271, "Вот")], "adapted"),
    ("anya", "Луи, почему ты не спрятался?", "Louis, why did you not hide?",
     [], "new"),
    ("kostya", "Зря вы обманывали меня, Виктор Петрович.", "You deceived me in vain, Viktor Petrovich.",
     [(272, "Зря вы, Виктор Петрович")], "adapted"),
    ("anya", "Я хотел защитить своего лучшего повара.", "I wanted to protect my best chef.",
     [], "new"),
    ("kostya", "Нужно было сразу признаться во всём.", "You should have confessed to everything right away.",
     [(273, "Признались бы сразу во всем")], "adapted"),
    ("kostya", "Тогда вы получили бы простое предупреждение.", "Then you would have received a simple warning.",
     [(273, "простым предупреждением")], "adapted"),
    ("anya", "Мы можем договориться с вами сейчас?", "Can we reach an agreement with you now?",
     [], "new"),
    ("kostya", "Нет, теперь уже слишком поздно.", "No, now it is already too late.",
     [], "new"),
    ("kostya", "К сожалению, вам придётся платить штраф.", "Unfortunately, you will have to pay a fine.",
     [(274, "придется платить штраф")], "adapted"),
    ("anya", "Ладно, ресторан заплатит этот большой штраф.", "All right, the restaurant will pay this big fine.",
     [], "new"),
    ("kostya", "Но это ещё далеко не всё.", "But that is still far from all.",
     [], "new"),
    ("kostya", "Этого молодого человека мы отправим домой.", "We will send this young man home.",
     [(275, "молодого человека")], "adapted"),
    ("anya", "Как я буду работать без Луи?", "How will I work without Louis?",
     [], "new"),
]

OPENER = "Let's see how the migration inspector delivers the bad news to Chef Barinov."

WALK = [
    (2, None,
     "'You deceived me in vain, Viktor Petrovich.' The adverb at the start expresses that an effort was pointless or a mistake."),
    (4, None,
     "'You should have confessed to everything right away.' An impersonal past construction expressing what ought to have been done."),
    (8, None,
     "'Unfortunately, you will have to pay a fine.' A formal announcement of a penalty using a dative pronoun and an impersonal verb."),
    (11, None,
     "'We will send this young man home.' A firm statement of future action using the accusative case for the animate object."),
]

TRANSITION = "Now, let's listen to the entire office confrontation once again."

OUTRO = (
    "Now you know how to talk about warnings, fines, and official consequences in Russian. "
    "Keep listening to see how the kitchen staff react to the aftermath."
)

CLOSING = ("anya", "Это просто настоящий кошмар для кухни!")
