"""s01e08 scene 19: Квота на операцию (communal apartment)."""

ID = "domashniy-arest-s01e08-scene-19"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 8
SCENE = 19
TITLE = "Квота на операцию  (Quota for the Surgery)"
LEVEL = "beginner"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "lyosha": "anja", "marina": "angelina"}
LABELS = {"anya": "Аркадий", "lyosha": "Лёша", "marina": "Марина"}
SOURCE_NAME = "Домашний арест, Сезон 1, Эпизод 8"
SOURCE_FILE = "sources/domashniy-arest/s01/e08.ru.dual.srt"
SOURCE_NOTE = "Cues 287-294 (00:18:27-00:18:45). Arkady thanks Lyosha, and Marina receives news of the surgery quota."

INTRO = (
    "Previously, after Marina scolded her son for breaking the toy tank, she stepped away to answer her ringing phone. "
    "Now, alone in the room with Lyosha, Arkady warmly thanks the boy for not betraying him, "
    "just before Marina returns with big news about Lyosha's medical surgery."
)

STORY = [
    ("anya", "Мужчина! Настоящий мужчина!",
     "A man! A real man!",
     [(287, "Мужчина")], "expanded cue 287"),
    ("anya", "Спасибо, что не сдал меня.",
     "Thanks for not ratting me out.",
     [(288, "Спасибо, что не сдал меня")], ""),
    ("lyosha", "Пожалуйста, дядя Аркадий.",
     "You are welcome, Uncle Arkady.",
     [], "natural conversational response"),
    ("anya", "Лёха, я тебе обязательно куплю танк.",
     "Lyokha, I'll definitely buy you a tank.",
     [(289, "Леха, я тебе обязательно куплю")], "shortened cue 289"),
    ("lyosha", "Точно купите?",
     "Will you really buy it?",
     [], "natural boy inquiry"),
    ("anya", "Я не вру! Деньги появятся, сразу куплю.",
     "I'm not lying! Soon as money appears, I'll buy it right away.",
     [(291, "Не вру. Деньги появятся, сразу куплю")], "adapted cues 290-291"),
    ("anya", "Ты понял меня?",
     "Did you understand me?",
     [(291, "Понял?")], "expanded cue 291"),
    ("lyosha", "Да, понял.",
     "Yes, I understood.",
     [], "boy agreement"),
    ("marina", "Лёша, нам квоту на операцию дали!",
     "Lyosha, they gave us a quota for the surgery!",
     [(292, "Леша, нам квоты на операцию дали")], "singularized квоту"),
    ("lyosha", "Правда, мам?",
     "Really, Mom?",
     [], "boy reaction"),
    ("marina", "Да! Я сейчас в больницу еду.",
     "Yes! I'm going to the hospital right now.",
     [(293, "Я сейчас в больницу")], "added еду"),
    ("marina", "Буду важные документы оформлять.",
     "I will process important paperwork.",
     [(293, "документы оформлять")], "added Буду важные"),
    ("marina", "А ты не сиди здесь!",
     "And you, don't sit around here!",
     [(294, "А ты не сиди здесь")], ""),
]

OPENER = "Let's break down Arkady's heartfelt promise to Lyosha and Marina's big announcement."

WALK = [
    (0, None,
     "'A man! A real man!' Arkady praises the boy for showing adult loyalty and courage."),
    (1, None,
     "'Thanks for not ratting me out.' The colloquial verb means to betray or turn someone in."),
    (3, None,
     "'Lyokha, I will definitely buy you a tank.' The future tense makes a firm promise."),
    (5, "Деньги появятся, сразу куплю.",
     "'Soon as money appears, I will buy it right away.' Arkady swears he is not lying."),
    (6, None,
     "'Did you understand me?' A common colloquial check ensuring agreement."),
    (8, None,
     "'Lyosha, they gave us a quota for the surgery!' Marina rushes in with excitement."),
    (10, None,
     "'Yes! I am going to the hospital right now.' She cannot wait to secure the opportunity."),
    (11, None,
     "'I will process important paperwork.' The verbal noun construction describes sorting out documents."),
    (12, None,
     "'And you, do not sit around here!' Marina warns her son not to hang around Arkady."),
]

TRANSITION = "Now listen to the scene in the room once more."
OUTRO = "Marina rushes off to the hospital to sign the surgery papers, leaving Arkady and Lyosha together again."
CLOSING = ("marina", "Нам квоту на операцию дали!")
