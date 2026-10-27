"""Authoring module for Kukhnya s01e10 scene 06."""
from pathlib import Path

ID = "kukhnya-s01e10-scene-06"
TITLE = "Серьёзные отношения  (A Serious Relationship)"
LEVEL = "A1"
PAIR = "ru-en"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 10
SCENE = 6

VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "kostya": "anja",
}

LABELS = {
    "narrator": "Narrator",
    "anya": "Макс",
    "kostya": "Костя",
}

SOURCE_NAME = "Кухня s01e10"
SOURCE_FILE = Path("sources/kukhnya/s01/e10.ru.dual.srt")
SOURCE_NOTE = "Cues 26-29 at the restaurant bar."

INTRO = (
    "In this scene at the restaurant bar, Max panics while confiding in his friend Kostya. "
    "Convinced that Victoria has developed feelings for him, Max fears this will lead to a serious relationship, "
    "marriage, and unwanted family responsibilities. Listen to their conversation in Russian first, and then we will examine each sentence."
)

OPENER = (
    "Now, let us examine the vocabulary and phrasing of this honest conversation between friends."
)

STORY = [
    ("anya", "Костя, кажется, Вика меня любит!", "Kostya, it seems Vika loves me!", [], "new"),
    ("kostya", "Класс! Или нет?", "Great! Or is it?", [(26, "Класс! Или нет?")], "verbatim"),
    ("anya", "Блин, Костя, это опасная ситуация.", "Damn, Kostya, this is a dangerous situation.", [(27, "Блин, Костян,")], "adapted: simplified name"),
    ("anya", "Если она меня любит, нужны отношения.", "If she loves me, a relationship is needed.", [(27, "если она меня любит, значит, сейчас ей будут нужны отношения.")], "adapted: shortened"),
    ("kostya", "А что плохого в отношениях?", "And what is bad about a relationship?", [], "new"),
    ("anya", "Потом свадьба, а потом дети!", "Then a wedding, and then kids!", [(28, "Потом свадьба, а потом что, дети?")], "adapted: shortened"),
    ("anya", "Зачем мне всё это сейчас?", "Why do I need all of this right now?", [(29, "Фига мне это надо.")], "adapted: polite A1 register"),
    ("kostya", "Ты просто боишься взрослой жизни.", "You are simply afraid of adult life.", [], "new"),
    ("anya", "Я люблю свободу и приключения!", "I love freedom and adventures!", [], "new"),
    ("kostya", "Вика взрослая и умная девушка.", "Vika is a mature and smart girl.", [], "new"),
    ("kostya", "Она не будет терпеть твои глупости.", "She will not tolerate your nonsense.", [], "new"),
    ("anya", "Вот именно, она начнет меня воспитывать.", "Exactly, she will start educating me.", [], "new"),
    ("kostya", "Тогда поговори с ней честно.", "Then talk to her honestly.", [], "new"),
    ("anya", "Нет, лучше я буду молчать.", "No, better that I keep quiet.", [], "new"),
]

WALK = [
    (0, None, "'Kostya, it seems Vika loves me!' Max shares his surprising realization with a troubled expression."),
    (1, None, "'Great! Or is it?' Kostya wonders about his friend's mixed reaction."),
    (2, None, "'Damn, Kostya, this is a dangerous situation.' Max expresses his growing anxiety about romance."),
    (3, None, "'If she loves me, a relationship is needed.' Max worries about serious emotional commitments."),
    (4, None, "'And what is bad about a relationship?' Kostya questions his dramatic reluctance."),
    (5, None, "'Then a wedding, and then kids!' Max lists the inevitable stages of family life."),
    (6, None, "'Why do I need all of this right now?' Max rejects settling down at this young age."),
    (7, None, "'You are simply afraid of adult life.' Kostya teases his friend's childish fears."),
    (8, None, "'I love freedom and adventures!' Max defends his carefree bachelor lifestyle."),
    (9, None, "'Vika is a mature and smart girl.' Kostya reminds him of Victoria's serious character."),
    (10, None, "'She will not tolerate your nonsense.' Kostya warns him about testing her patience."),
    (11, None, "'Exactly, she will start educating me.' Max dreads losing control over his daily routine."),
    (12, None, "'Then talk to her honestly.' Kostya offers sensible advice for resolving the issue."),
    (13, None, "'No, better that I keep quiet.' Max chooses avoidance instead of an open conversation."),
]

TRANSITION = (
    "Now, let us listen to the complete scene again to practice your comprehension."
)

OUTRO = (
    "A humorous reflection on the comical terror of sudden romantic commitment."
)

CLOSING = ("anya", "Надо держаться от неё подальше.")
