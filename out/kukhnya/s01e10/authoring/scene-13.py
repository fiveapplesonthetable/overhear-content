"""s01e10 scene 13: Угроза для бармена (A Threat for the Bartender)."""

ID = "kukhnya-s01e10-scene-13"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 10
SCENE = 13
TITLE = "Угроза для бармена  (A Threat for the Bartender)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "kostya": "anja"}
LABELS = {"anya": "Вика", "kostya": "Костя"}
SOURCE_NAME = "Кухня (Kukhnya) S1.10"
SOURCE_FILE = "sources/kukhnya/s01/e10.ru.dual.srt"
SOURCE_NOTE = "Cues 95-108. Victoria threatens to change Nastya's work shifts, forcing Kostya to reveal that Max panicked after learning Victoria supposedly loves him."

INTRO = (
    "Determined to find out why Max is deliberately avoiding her, art director Victoria corners bartender Kostya with an ultimatum. "
    "Faced with the threat of having his girlfriend Nastya moved to a conflicting shift, Kostya cracks under pressure and confesses Max's comedic terror of marriage and children. "
    "Let's listen to their lively exchange in Russian first."
)

STORY = [
    ("anya", "Костя, быстро говори, в чём дело!",
     "Kostya, quickly speak, what is the matter!",
     [(95, "Костя, или ты мне сейчас говоришь")], "demanding the explanation"),
    ("kostya", "Вика, пожалуйста, перестань меня пугать!",
     "Vika, please, stop scaring me!",
     [], "begging for mercy"),
    ("anya", "Или я переведу Настю в другую смену!",
     "Or I will transfer Nastya to another shift!",
     [(96, "Или я Настю перевожу в другую смену")], "threatening his girlfriend's schedule"),
    ("kostya", "Ладно, я скажу тебе всё прямо сейчас!",
     "All right, I will tell you everything right now!",
     [(99, "Он узнал от вашей племянницы")], "giving in to the pressure"),
    ("anya", "Я внимательно слушаю твоё признание.",
     "I am listening attentively to your confession.",
     [], "awaiting the truth"),
    ("kostya", "Макс узнал от Алисы твой секрет.",
     "Max found out your secret from Alice.",
     [(99, "Он узнал от вашей племянницы, что вы его любите")], "revealing the source"),
    ("anya", "Какой ещё секрет узнал этот дурак?",
     "What secret did that fool find out?",
     [], "curious about what was said"),
    ("kostya", "Он думает, что ты любишь его!",
     "He thinks that you love him!",
     [(99, "что вы его любите")], "blurting out the confession"),
    ("anya", "И почему он стал прятаться теперь?",
     "And why did he start hiding now?",
     [(101, "И что? Как что")], "asking for the logic"),
    ("kostya", "Он испугался свадьбы и маленьких детей!",
     "He got scared of a wedding and little kids!",
     [(103, "Вдруг свадьба, потом что, дети")], "explaining his panic"),
    ("anya", "Бедный трусливый Максик, испугался детей.",
     "Poor cowardly Maxik, got scared of kids.",
     [(106, "Бедный Максик. Да"), (107, "Детишек испугался")], "mocking his foolish terror"),
    ("kostya", "Спасибо, что не трогаешь смену Насти!",
     "Thank you for not touching Nastya's shift!",
     [(108, "Спасибо, Костя")], "relieved that his girlfriend is safe"),
]

OPENER = "Let's examine how Victoria pressures Kostya in the bar line by line."

WALK = [
    (0, None,
     "'Kostya, quickly speak, what is the matter!' Victoria presses for immediate answers using two imperative expressions."),
    (1, None,
     "'Vika, please, stop scaring me!' Kostya protests the interrogation using a polite particle and an infinitive."),
    (2, None,
     "'Or I will transfer Nastya to another shift!' Victoria issues a direct threat regarding staff scheduling to force compliance."),
    (3, None,
     "'All right, I will tell you everything right now!' The cornered bartender capitulates with a future tense verb."),
    (4, None,
     "'I am listening attentively to your confession.' Victoria demands full details using an adverb of manner and an accusative noun."),
    (5, None,
     "'Max found out your secret from Alice.' Kostya discloses the leak using a past tense verb with a genitive prepositional phrase."),
    (6, None,
     "'What secret did that fool find out?' Victoria expresses exasperation using an interrogative pronoun and a derogatory noun."),
    (7, None,
     "'He thinks that you love him!' Kostya delivers the punchline with a present tense verb and a subordinate clause."),
    (8, None,
     "'And why did he start hiding now?' Victoria seeks clarification with a compound past verb phrase."),
    (9, None,
     "'He got scared of a wedding and little kids!' Kostya outlines Max's relationship anxieties with two genitive objects."),
    (10, None,
     "'Poor cowardly Maxik, got scared of kids.' Victoria reacts with amused condescension using diminutive forms."),
    (11, None,
     "'Thank you for not touching Nastya's shift!' Kostya expresses gratitude for preserving his shared work hours."),
]

TRANSITION = "Now let's listen to the whole dialogue again at normal conversational speed."

OUTRO = (
    "Now you know how to talk about workplace leverage, unexpected confessions, and relationship fears in Russian. "
    "See you next time!"
)

CLOSING = ("anya", "Бедный трусливый Максик, испугался детей.")
