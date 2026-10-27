ID = "kukhnya-s01e11-scene-18"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 11
SCENE = 18
TITLE = "Неожиданное признание  (An Unexpected Confession)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "guest": "anja"}
LABELS = {"anya": "Вика", "guest": "Гость"}
SOURCE_NAME = "Кухня (Kukhnya) S1.11"
SOURCE_FILE = "sources/kukhnya/s01/e11.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 210-226. A male diner approaches Victoria to pay the bill and apologizes, explaining that "
    "his sick wife is pregnant with morning sickness and relieving the staff that she is not the critic."
)

INTRO = (
    "Near the reception desk of Claude Monet, the husband of the ailing female diner steps up "
    "to settle their bill. Expecting an angry complaint or a scandal over food poisoning, "
    "Victoria is astonished when the customer offers an earnest apology and reveals a touching "
    "personal secret. Let us listen to their conversation in Russian first."
)

STORY = [
    ("anya", "Здравствуйте, вам понравился наш ресторан сегодня?",
     "Hello, did you like our restaurant today?",
     [], "new"),
    ("guest", "Вы уж извините нас, ради бога.",
     "Please forgive us, for the love of God.",
     [(221, "Вы уж извините нас, ради бога")], "adapted"),
    ("anya", "Что-то случилось с вашей женой?",
     "Did something happen with your wife?",
     [], "new"),
    ("guest", "Моя жена мне всё подробно рассказала.",
     "My wife told me everything in detail.",
     [(220, "Мне моя жена все рассказала")], "adapted"),
    ("anya", "Она отравилась каким-то нашим блюдом?",
     "Did she get poisoned by some dish of ours?",
     [(210, "после вашего блюда отравилась")], "adapted"),
    ("guest", "Нет, она вовсе не отравилась едой.",
     "No, she was not poisoned by food at all.",
     [], "new"),
    ("anya", "Почему же ей стало так плохо?",
     "Why then did she feel so ill?",
     [], "new"),
    ("guest", "Она беременна, уже на третьем месяце.",
     "She is pregnant, already in the third month.",
     [(222, "Она на третьем месяце беременности")], "adapted"),
    ("anya", "Так у неё просто сильный токсикоз?",
     "So she just has bad morning sickness?",
     [(223, "токсикоз")], "adapted"),
    ("guest", "Да, от запахов еды её тошнит.",
     "Yes, the smells of food make her nauseous.",
     [], "new"),
    ("anya", "Мы очень переживали за её здоровье.",
     "We were very worried about her health.",
     [], "new"),
    ("guest", "Спасибо вам за понимание и заботу.",
     "Thank you for your understanding and care.",
     [], "new"),
    ("anya", "Значит, эта женщина точно не критик.",
     "So this woman is definitely not the critic.",
     [(226, "мы точно знаем, что критик не она")], "adapted"),
]

OPENER = "Now let us examine Victoria and the gentleman's polite discussion line by line."

WALK = [
    (0, None,
     "'Hello, did you like our restaurant today?' -- Victoria courteously greets the patron approaching the counter."),
    (1, None,
     "'Please forgive us, for the love of God.' -- The husband sincerely asks for forgiveness on behalf of his family."),
    (2, None,
     "'Did something happen with your wife?' -- The manager inquires with concern about the sick diner."),
    (3, None,
     "'My wife told me everything in detail.' -- The gentleman explains that his spouse reported the situation."),
    (4, None,
     "'Did she get poisoned by some dish of ours?' -- Victoria asks if the food caused her illness."),
    (5, None,
     "'No, she was not poisoned by food at all.' -- The man reassures her that food was not to blame."),
    (6, None,
     "'Why then did she feel so ill?' -- Victoria wonders about the true cause of her distress."),
    (7, None,
     "'She is pregnant, already in the third month.' -- The husband reveals that his wife is expecting a baby."),
    (8, None,
     "'So she just has bad morning sickness?' -- The manager realizes that nausea was simply pregnancy sickness."),
    (9, None,
     "'Yes, the smells of food make her nauseous.' -- The customer describes her heightened olfactory sensitivity."),
    (10, None,
     "'We were very worried about her health.' -- Victoria expresses relief and compassionate concern."),
    (11, None,
     "'Thank you for your understanding and care.' -- The patron thanks the staff for their gracious attitude."),
    (12, None,
     "'So this woman is definitely not the critic.' -- Victoria breathes a sigh of relief that their food critic nightmare is averted."),
]

TRANSITION = "Now let us listen to the reassuring conversation once again."
OUTRO = (
    "Deeply relieved to discover that pregnancy rather than food poisoning was the cause, "
    "Victoria happily confirms that the restaurant's reputation remains untarnished."
)
CLOSING = ("anya", "Значит, эта женщина точно не критик.")
