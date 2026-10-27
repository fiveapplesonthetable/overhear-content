ID = "kukhnya-s01e14-scene-11"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 14
SCENE = 11
TITLE = "Разбитое сердце  (Broken Heart)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "max": "anja"}
LABELS = {"anya": "Девушка", "max": "Макс"}
SOURCE_NAME = "Кухня (Kukhnya) S1.14"
SOURCE_FILE = "sources/kukhnya/s01/e14.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 172-174. In the dining room, an angry woman guest confronts Max for breaking her heart, "
    "demanding that he forget her phone number forever."
)

INTRO = (
    "In the dining room near the entrance of Claude Monet, an upset young woman stops Max. "
    "Furious about his past behavior, she accuses him of being a liar and demands that he never contact her again. "
    "Let us listen to their tense exchange in Russian first."
)

STORY = [
    ("anya", "Макс, ты разбил моё бедное сердце!",
     "Max, you broke my poor heart!",
     [(172, "разбил мое сердце, подлый бабник.")], "adapted"),
    ("max", "Подожди, давай спокойно поговорим об этом.",
     "Wait, let us talk calmly about this.",
     [], "new"),
    ("anya", "Ты просто ужасный и подлый обманщик!",
     "You are simply a terrible and vile deceiver!",
     [(172, "подлый бабник")], "adapted"),
    ("max", "Я не хотел обидеть тебя тогда.",
     "I did not want to offend you back then.",
     [], "new"),
    ("anya", "Ты обещал звонить мне каждый день.",
     "You promised to call me every single day.",
     [], "new"),
    ("max", "У меня было очень много работы.",
     "I had a huge amount of work.",
     [], "new"),
    ("anya", "Забудь навсегда мой личный номер телефона!",
     "Forget my personal phone number forever!",
     [(173, "Забудь мой номер телефона.")], "adapted"),
    ("max", "Не злись, пожалуйста, выслушай меня сейчас.",
     "Do not be angry, please, listen to me now.",
     [], "new"),
    ("anya", "Забудь, что у меня вообще есть телефон!",
     "Forget that I even have a phone at all!",
     [(174, "Забудь, что у меня в принципе есть телефон.")], "adapted"),
    ("max", "Мне искренне жаль, прости меня, пожалуйста.",
     "I am sincerely sorry, forgive me, please.",
     [], "new"),
    ("anya", "Я больше никогда не поверю тебе.",
     "I will never believe you anymore.",
     [], "new"),
    ("max", "Дай мне один маленький последний шанс.",
     "Give me one small last chance.",
     [], "new"),
    ("anya", "Уходи немедленно, я не хочу слушать!",
     "Leave immediately, I do not want to listen!",
     [], "new"),
]

OPENER = "Now let us examine the woman and Max's angry confrontation line by line."

WALK = [
    (0, None,
     "'Max, you broke my poor heart!' -- The young woman confronts the cook with an angry accusation."),
    (1, None,
     "'Wait, let us talk calmly about this.' -- Max attempts to defuse the heated confrontation in the dining room."),
    (2, None,
     "'You are simply a terrible and vile deceiver!' -- She vents her frustration over his unfaithfulness and broken promises."),
    (3, None,
     "'I did not want to offend you back then.' -- Max weakly defends his past actions and tries to apologize."),
    (4, None,
     "'You promised to call me every single day.' -- The upset guest recalls the commitments Max made when they met."),
    (5, None,
     "'I had a huge amount of work.' -- The cook offers a busy work schedule as an excuse for his absence."),
    (6, None,
     "'Forget my personal phone number forever!' -- She furiously cuts off any future contact between them."),
    (7, None,
     "'Do not be angry, please, listen to me now.' -- Max pleads for another moment to explain his side of the story."),
    (8, None,
     "'Forget that I even have a phone at all!' -- The woman emphasizes that she never wants to hear from him again."),
    (9, None,
     "'I am sincerely sorry, forgive me, please.' -- Realizing his fault, Max offers a direct and earnest apology."),
    (10, None,
     "'I will never believe you anymore.' -- The woman firmly rejects his words, stating her trust is destroyed."),
    (11, None,
     "'Give me one small last chance.' -- Max makes a final desperate appeal to salvage good terms."),
    (12, None,
     "'Leave immediately, I do not want to listen!' -- The customer demands he walk away and ends the conversation."),
]

TRANSITION = "Now let us listen to the woman and Max once again."
OUTRO = (
    "Stunned by the unexpected encounter and harsh rejection, Max is left standing "
    "in the dining room while the offended guest storms off."
)
CLOSING = ("anya", "Уходи немедленно, я не хочу слушать!")
