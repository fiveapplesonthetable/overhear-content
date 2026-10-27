"""Authoring module for Kukhnya s01e11 scene 09."""
from pathlib import Path

ID = "kukhnya-s01e11-scene-09"
TITLE = "Средство от похмелья  (A Cure for a Hangover)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 11
SCENE = 9

VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "guest": "anja",
    "chef": "angelina",
}

LABELS = {
    "narrator": "Narrator",
    "anya": "Костя",
    "guest": "Гость",
    "chef": "Шеф",
}

SOURCE_NAME = "Кухня (Kukhnya) S1.11"
SOURCE_FILE = Path("sources/kukhnya/s01/e11.ru.dual.srt")
SOURCE_NOTE = "Cues 116-151 at the bar counter."

INTRO = (
    "Sitting at the Claude Monet bar, the customer confides to Kostya why his girlfriend suddenly dumped him. "
    "When Chef Barinov notices the visitor's miserable physical condition, he warmly prescribes a bowl of hot bouillabaisse as the perfect remedy. "
    "Let's listen to their entertaining dialogue in Russian."
)

OPENER = (
    "Now let's examine how the guest shares his romantic troubles and accepts the chef's culinary cure line by line."
)

STORY = [
    ("guest", "Костя, мы с ней были слишком разными.",
     "Kostya, she and I were too different.",
     [(116, "мы были с ней абсолютно разными людьми.")], "Guest discusses his relationship"),

    ("anya", "Почему вы так думаете, друг мой?",
     "Why do you think so, my friend?",
     [], "Kostya inquires kindly"),

    ("guest", "Она считала меня настоящим трусом.",
     "She considered me a real coward.",
     [(118, "в ее глазах я был жалким трусом")], "Guest explains her harsh view"),

    ("guest", "Но я не хотел прыгать с парашютом!",
     "But I did not want to jump with a parachute!",
     [(120, "Ну, не хотел я вместе с ней прыгать с этим пресловутым парашютом.")], "Guest explains the skydiving refusal"),

    ("guest", "Зачем вообще глупо рисковать своей жизнью?",
     "Why stupidly risk one's life at all?",
     [(121, "Ну, зачем рисковать жизни, вот зачем, а?")], "Guest defends his caution"),

    ("anya", "Я полностью согласен с вами.",
     "I completely agree with you.",
     [(122, "Согласен.")], "Kostya validates his decision"),

    ("guest", "Она бросила меня прямо здесь вчера.",
     "She dumped me right here yesterday.",
     [(124, "Она меня бросила.")], "Guest reveals the breakup"),

    ("chef", "Что здесь происходит у барной стойки?",
     "What is going on here at the bar?",
     [], "Barinov steps up to the bar"),

    ("guest", "Где здесь находится туалет, подскажите?",
     "Where is the restroom located here, tell me?",
     [(139, "А вы не подскажете, а где здесь туалет?")], "Guest asks for directions"),

    ("anya", "Туалет находится сразу слева от бара.",
     "The restroom is located immediately to the left of the bar.",
     [(141, "Слева от бара.")], "Kostya gives clear directions"),

    ("chef", "Друг, тебе сейчас нужен горячий суп!",
     "Friend, you need hot soup right now!",
     [(143, "Тебе, дружище, в твоем состоянии супчик бы не помешал.")], "Barinov offers culinary medicine"),

    ("guest", "Я совсем не против вкусного супа.",
     "I am not at all against tasty soup.",
     [(145, "Ну что, я не против.")], "Guest agrees readily"),

    ("chef", "Костя, срочно закажи нашему гостю буйабес!",
     "Kostya, urgently order bouillabaisse for our guest!",
     [(146, "пробей гостю")], "Barinov orders the soup"),
]

WALK = [
    (0, None,
     "'Kostya, she and I were too different.' The customer explains the irreconcilable differences in his relationship."),
    (1, None,
     "'Why do you think so, my friend?' Kostya listens with attentive empathy."),
    (2, None,
     "'She considered me a real coward.' The man reveals the painful label his girlfriend gave him."),
    (3, None,
     "'But I did not want to jump with a parachute!' He justifies refusing an extreme sports dare."),
    (4, None,
     "'Why stupidly risk one's life at all?' He argues that survival should come before reckless thrills."),
    (5, None,
     "'I completely agree with you.' Kostya sides wholeheartedly with sensible caution."),
    (6, None,
     "'She dumped me right here yesterday.' The visitor describes where the sudden separation happened."),
    (7, None,
     "'What is going on here at the bar?' Chef Barinov approaches and examines the scene."),
    (8, None,
     "'Where is the restroom located here, tell me?' The guest politely asks where to find the bathroom."),
    (9, None,
     "'The restroom is located immediately to the left of the bar.' Kostya provides concise directions to the guest."),
    (10, None,
     "'Friend, you need hot soup right now!' Barinov recognizes the signs of physical exhaustion and hangover."),
    (11, None,
     "'I am not at all against tasty soup.' The visitor gratefully accepts the dining suggestion."),
    (12, None,
     "'Kostya, urgently order bouillabaisse for our guest!' Barinov prescribes the famous rich seafood stew."),
]

TRANSITION = (
    "Now let's listen to the guest's honest confession and the chef's soup prescription once more."
)

OUTRO = (
    "With an order of signature bouillabaisse on the way, the wounded guest finds unexpected sympathy in Claude Monet."
)

CLOSING = ("chef", "Костя, срочно закажи нашему гостю буйабес!")
