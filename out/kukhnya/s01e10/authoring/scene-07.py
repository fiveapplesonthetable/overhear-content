"""Authoring module for Kukhnya s01e10 scene 07."""
from pathlib import Path

ID = "kukhnya-s01e10-scene-07"
TITLE = "Побег от разговора  (Escaping the Conversation)"
LEVEL = "A1"
PAIR = "ru-en"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 10
SCENE = 7

VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "vika": "anja",
    "kostya": "angelina",
}

LABELS = {
    "narrator": "Narrator",
    "anya": "Макс",
    "vika": "Вика",
    "kostya": "Костя",
}

SOURCE_NAME = "Кухня s01e10"
SOURCE_FILE = Path("sources/kukhnya/s01/e10.ru.dual.srt")
SOURCE_NOTE = "Cues 57-66 in the dining room and bar."

INTRO = (
    "In this scene in the restaurant hallway, Victoria tries to approach Max for an important talk. "
    "Panicked by the thought of relationship commitments, Max fakes an incoming phone call from Kostya and runs away to the bar. "
    "Listen to their fast-paced exchange in Russian first, and then we will examine each sentence."
)

OPENER = (
    "Now, let us examine the vocabulary and phrasing of this comical escape attempt."
)

STORY = [
    ("vika", "Макс, нам надо серьёзно поговорить!", "Max, we need to talk seriously!", [(57, "Макс!")], "adapted: added goal"),
    ("anya", "Привет, Вика! Рад тебя видеть.", "Hey, Vika! Glad to see you.", [(58, "Привет, Вик!")], "adapted: added greeting"),
    ("anya", "Ой, Костя звонит, извини!", "Oh, Kostya is calling, sorry!", [(59, "Костян звонит, извини!")], "adapted: simplified name"),
    ("anya", "Алло, Костя, говори громче!", "Hello, Kostya, speak louder!", [(60, "Алло, Костян, говори громче, не слышу!")], "adapted: shortened"),
    ("anya", "Плохо слышно, я сейчас подойду!", "Hard to hear, I will come over right now!", [(63, "Да, сейчас!")], "adapted: expanded promise"),
    ("vika", "Макс, подожди, не уходи!", "Max, wait, do not leave!", [], "new"),
    ("anya", "Вика, это очень срочное дело!", "Vika, this is a very urgent matter!", [], "new"),
    ("anya", "Костя, а ты чего звонил?", "Kostya, why did you call?", [(64, "Костян, а ты чего звонил-то?")], "adapted: simplified name"),
    ("kostya", "В смысле, я тебе не звонил.", "What do you mean, I did not call you.", [(65, "В смысле, звоню?")], "adapted: clarified"),
    ("anya", "Сделай вид, что нужна помощь!", "Pretend that you need help!", [(65, "ты помочь, чтобы я тебе помог, да?")], "adapted: simplified request"),
    ("kostya", "А, ты прячешься от Вики?", "Oh, you are hiding from Vika?", [], "new"),
    ("anya", "Да, подыграй мне, пожалуйста!", "Yes, play along with me, please!", [], "new"),
    ("kostya", "Ну давай, пошли на склад.", "All right, let us go to the storeroom.", [(66, "Ну давай, пошли.")], "adapted: added destination"),
    ("anya", "Спасибо, друг, ты меня спас!", "Thank you, friend, you saved me!", [], "new"),
]

WALK = [
    (0, None, "'Max, we need to talk seriously!' Victoria approaches him with an important purpose."),
    (1, None, "'Hey, Vika! Glad to see you.' Max replies nervously while searching for an escape."),
    (2, None, "'Oh, Kostya is calling, sorry!' Max pretends that his phone is ringing."),
    (3, None, "'Hello, Kostya, speak louder!' Max fakes a noisy conversation into his device."),
    (4, None, "'Hard to hear, I will come over right now!' Max invents a reason to leave immediately."),
    (5, None, "'Max, wait, do not leave!' Victoria tries to stop him from slipping away."),
    (6, None, "'Vika, this is a very urgent matter!' Max insists with dramatic urgency before rushing off."),
    (7, None, "'Kostya, why did you call?' Max whispers hurriedly as he reaches the bar."),
    (8, None, "'What do you mean, I did not call you.' Kostya responds with genuine confusion."),
    (9, None, "'Pretend that you need help!' Max begs him to maintain the illusion."),
    (10, None, "'Oh, you are hiding from Vika?' Kostya quickly figures out his friend's motive."),
    (11, None, "'Yes, play along with me, please!' Max urges him with frantic hand gestures."),
    (12, None, "'All right, let us go to the storeroom.' Kostya agrees to help him escape the dining room."),
    (13, None, "'Thank you, friend, you saved me!' Max breathes a sigh of relief as they walk away."),
]

TRANSITION = (
    "Now, let us listen to the complete scene again to practice your comprehension."
)

OUTRO = (
    "A funny depiction of dodging uncomfortable romantic conversations at all costs."
)

CLOSING = ("anya", "Я спасся от серьёзного разговора!")
