ID = "domashniy-arest-s01e10-scene-06"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 10
SCENE = 6
TITLE = "Приказ начальника  (The Chief's Order)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "boss": "anja"}
LABELS = {"anya": "Соколов", "boss": "Начальник"}
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.10"
SOURCE_FILE = "sources/domashniy-arest/s01/e10.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 186-210. The FSB chief reprimands Sokolov for his crude ideas of using force. "
    "He orders him to set up surveillance on Anikeyev's former home, reminding him that orders must be obeyed."
)

INTRO = (
    "In this scene, the FSB chief severely scolds agent Sokolov for his lack of results. "
    "Sokolov rashly proposes using force to extract the hidden millions, but the chief cuts him off. "
    "Instead of violent tactics, the chief orders Sokolov on a routine surveillance post outside Anikeyev's former residence. "
    "Let's listen to their conversation in Russian first."
)

STORY = [
    ("boss", "Вы совсем не умеете работать!",
     "You do not know how to work at all!",
     [(186, "Потому что вы мышей не ловите")], "idiom softened to standard A1"),
    ("boss", "Скоро вас обоих просто уволят.",
     "Soon both of you will simply be fired.",
     [(188, "Вот вас снимут")], ""),
    ("anya", "Я могу быстро найти эти деньги.",
     "I can quickly find that money.",
     [(190, "А я быстро эти бабки вытащу")], ""),
    ("boss", "И как же ты их найдёшь?",
     "And how exactly will you find it?",
     [(191, "Да ты что, и как же")], ""),
    ("anya", "С помощью силы и угроз!",
     "With the help of force and threats!",
     [(192, "Силовыми методами"), (194, "угрозы")], ""),
    ("boss", "Соколов, тебе детского сада мало?",
     "Sokolov, wasn't the kindergarten enough for you?",
     [(195, "Соколов, тебе детского сада мало")], ""),
    ("boss", "Ты находишься в моём подчинении.",
     "You are under my command.",
     [(197, "Ты находишься в прямом моем подчинении")], ""),
    ("boss", "Ноги со стола быстро убери!",
     "Take your feet off the table quickly!",
     [(199, "ноги убрал")], ""),
    ("boss", "Ты сейчас идёшь на задание.",
     "You are going on an assignment now.",
     [(200, "сейчас идешь")], ""),
    ("boss", "Установи наблюдение за домом Аникеева.",
     "Set up surveillance on Anikeyev's house.",
     [(200, "устанавливаешь наблюдение"), (201, "За бывшим домом Аникиева")], ""),
    ("anya", "Вы что, просто сливаете меня?",
     "Are you just throwing me under the bus?",
     [(205, "Вы что, меня сливаете")], ""),
    ("boss", "Да, но приказы не обсуждаются!",
     "Yes, but orders are not discussed!",
     [(206, "Да"), (207, "Но приказы не обсуждаются")], ""),
    ("anya", "Ладно, я всё понял.",
     "Fine, I understood everything.",
     [(208, "Ладно")], ""),
    ("boss", "Не ладно, а так точно!",
     "Not fine, but yes sir!",
     [(209, "Не ладно, а есть")], "military response"),
]

OPENER = (
    "Now let's examine the chief's stern order line by line. "
    "The FSB chief reprimands Sokolov for his crude methods."
)

WALK = [
    (0, None,
     "'You do not know how to work at all!' The chief scolds his subordinates using an infinitive construction."),
    (1, None,
     "'Soon both of you will simply be fired.' The future plural verb expresses imminent dismissal."),
    (2, None,
     "'I can quickly find that money.' Sokolov boasts using a modal verb with an infinitive."),
    (3, None,
     "'And how exactly will you find it?' The chief challenges his boast with an emphatic particle."),
    (4, None,
     "'With the help of force and threats!' Sokolov bluntly advocates heavy-handed methods."),
    (5, None,
     "'Sokolov, wasn't the kindergarten enough for you?' The chief refers to Sokolov's recent failed undercover operation."),
    (6, None,
     "'You are under my command.' The prepositional phrase establishes the chain of command."),
    (7, None,
     "'Take your feet off the table quickly!' The imperative verb commands immediate professional discipline."),
    (8, None,
     "'You are going on an assignment now.' The present tense verb indicates an immediate directive."),
    (9, None,
     "'Set up surveillance on Anikeyev's house.' The imperative verb requires static observation."),
    (10, None,
     "'Are you just throwing me under the bus?' Sokolov complains using a vivid colloquial idiom."),
    (11, None,
     "'Yes, but orders are not discussed!' The reflexive present verb states a military rule."),
    (12, None,
     "'Fine, I understood everything.' Sokolov accepts the order with past tense agreement."),
    (13, None,
     "'Not fine, but yes sir!' The chief demands proper military protocol."),
]

TRANSITION = "Now let's listen to the chief and Sokolov's confrontation once more without pauses."
OUTRO = (
    "Rebuked by his superior, Sokolov is dispatched to a tedious stakeout. "
    "In the next scene, he prepares for his surveillance duty."
)
CLOSING = ("boss", "Но приказы не обсуждаются!")
