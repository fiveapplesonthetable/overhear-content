"""s01e10 scene 34: Проверка икры (Checking the Caviar)."""

ID = "kukhnya-s01e10-scene-34"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 10
SCENE = 34
TITLE = "Проверка икры  (Checking the Caviar)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "senya": "anja",
}
LABELS = {
    "anya": "Федя",
    "senya": "Сеня",
}
SOURCE_NAME = "Кухня (Kukhnya) S1.10"
SOURCE_FILE = "sources/kukhnya/s01/e10.ru.dual.srt"

INTRO = (
    "In the Claude Monet kitchen, Fedya and Senya finish preparing the caviar for the VIP table. "
    "Fedya inspects the bowl and worries they did not add enough dye, but Senya insists it looks perfectly authentic. "
    "Listen to their conversation in Russian first, then we will break down each line in English."
)

STORY = [
    ("anya", "Сеня, подойди сюда на секунду.",
     "Senya, come over here for a second.",
     [], "calling partner"),
    ("senya", "Что такое, Федя? Всё готово?",
     "What is it, Fedya? Is everything ready?",
     [], "asking status"),
    ("anya", "Мне кажется, мы её не докрасили.",
     "I think we did not finish dyeing it.",
     [(244, "Мне кажется, мы её не докрасили.")], "voicing concern"),
    ("senya", "Да брось, она абсолютно чёрная!",
     "Come on, it is completely black!",
     [], "rejecting doubt"),
    ("anya", "А вдруг шеф увидит светлые икринки?",
     "What if Chef sees light caviar eggs?",
     [], "imagining risk"),
    ("senya", "Никто ничего подозрительного не заметит.",
     "Nobody will notice anything suspicious.",
     [], "reassuring"),
    ("senya", "Если бы икра не была настоящей,",
     "If the caviar were not like real caviar,",
     [(245, "Если бы икра не была похожа на настоящую,")], "making argument"),
    ("senya", "ты бы сам её сейчас не пробовал.",
     "you would not be tasting it yourself right now.",
     [(246, "Сеня бы ее не спер.")], "teasing friend"),
    ("anya", "Ладно, ладно, ты меня убедил.",
     "All right, all right, you convinced me.",
     [], "yielding point"),
    ("senya", "Тогда зови официанта, пора подавать блюдо.",
     "Then call the waiter, it is time to serve the dish.",
     [], "prompting delivery"),
    ("anya", "Официант, забирай заказ на первый стол!",
     "Waiter, take the order for table one!",
     [], "calling waiter"),
    ("senya", "Давай, выносим икру в зал.",
     "Come on, let us bring the caviar into the hall.",
     [(248, "выносим икру.")], "ordering send-off"),
]

OPENER = "Let us practice the key lines together."

WALK = [
    (0, "Сеня, подойди сюда на секунду.",
     "'Senya, come over here for a second.' — informal imperative followed by a temporal phrase."),
    (2, "Мне кажется, мы её не докрасили.",
     "'I think we did not finish dyeing it.' — impersonal verb with a negated prefix verb."),
    (3, "Да брось, она абсолютно чёрная!",
     "'Come on, it is completely black!' — colloquial imperative followed by an adjective of degree."),
    (4, "А вдруг шеф увидит светлые икринки?",
     "'What if Chef sees light caviar eggs?' — hypothetical conjunction followed by a future verb."),
    (5, "Никто ничего подозрительного не заметит.",
     "'Nobody will notice anything suspicious.' — double negative pronoun with a genitive adjective."),
    (8, "Ладно, ладно, ты меня убедил.",
     "'All right, all right, you convinced me.' — past perfective verb expressing concession."),
    (9, "Тогда зови официанта, пора подавать блюдо.",
     "'Then call the waiter, it is time to serve the dish.' — imperative verb with a predicative noun phrase."),
    (11, "Давай, выносим икру в зал.",
     "'Come on, let us bring the caviar into the hall.' — hortative particle with a present verb of carrying."),
]

TRANSITION = "Now listen to the full conversation once more."
OUTRO = "Great job! Keep practicing these lively dialogues with us to master everyday Russian."
CLOSING = ("senya", "Давай, выносим икру в зал.")
