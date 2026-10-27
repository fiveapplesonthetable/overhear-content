"""s01e10 scene 14: Пропавшая плита (The Missing Stove)."""

ID = "kukhnya-s01e10-scene-14"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 10
SCENE = 14
TITLE = "Пропавшая плита  (The Missing Stove)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "senya": "anja"}
LABELS = {"anya": "Шеф", "senya": "Сеня"}
SOURCE_NAME = "Кухня (Kukhnya) S1.10"
SOURCE_FILE = "sources/kukhnya/s01/e10.ru.dual.srt"
SOURCE_NOTE = "Cues 123-130. Senya discovers that the professional stove is gone, and Chef Barinov claims he took it for preventive maintenance while leaving a tiny electric burner."

INTRO = (
    "In the Claude Monet kitchen, line cook Senya is astonished to discover that their large commercial stove has disappeared without explanation. "
    "To conceal the fact that he secretly pawned the kitchen equipment to place a football bet, Chef Barinov insists he sent it for routine maintenance. "
    "Let's listen to their humorous confrontation in Russian first."
)

STORY = [
    ("senya", "Шеф, куда пропала наша большая плита?",
     "Chef, where has our big stove disappeared to?",
     [(125, "Шеф, а где наша плита")], "discovering the missing stove"),
    ("anya", "Я лично отвёз её в надёжный сервис.",
     "I personally took it to a reliable repair service.",
     [(126, "Я ее в сервис отвез")], "offering an excuse"),
    ("senya", "Но она отлично работала вчера вечером!",
     "But it was working perfectly yesterday evening!",
     [(127, "Так она же исправная была")], "protesting the explanation"),
    ("anya", "Я сдал её для важной профилактики.",
     "I turned it in for important preventive maintenance.",
     [(128, "Я ее для профилактики отвез")], "inventing a reason"),
    ("senya", "А на чём нам готовить сегодня?",
     "And on what are we to cook today?",
     [], "asking about current cooking"),
    ("anya", "Пока готовьте блюда на этой плитке.",
     "For now cook the dishes on this little hotplate.",
     [(130, "Пока готовьте на этой")], "pointing to the tiny replacement"),
    ("senya", "Эта маленькая плитка нагревается слишком медленно!",
     "This little hotplate heats up much too slowly!",
     [(123, "На четверочку поставь")], "complaining about weak equipment"),
    ("anya", "Хватит ныть, повара должны уметь всё!",
     "Stop whining, cooks must know how to do everything!",
     [], "commanding resilience"),
    ("senya", "Гости будут очень долго ждать заказы!",
     "The guests will wait for their orders very long!",
     [(142, "Почему заказы делаются так долго")], "warning of customer delays"),
    ("anya", "Поставьте нагрев на четвёрку и работайте!",
     "Set the heat to four and get to work!",
     [(123, "На четверочку поставь")], "giving equipment instructions"),
    ("senya", "Когда нам вернут нашу старую плиту?",
     "When will they return our old stove to us?",
     [], "seeking a timeline"),
    ("anya", "Через день или два всё привезут!",
     "In a day or two they will bring everything!",
     [(129, "День-другой привезут обратно")], "promising a quick return"),
]

OPENER = "Let's review the humorous kitchen confrontation regarding the missing stove line by line."

WALK = [
    (0, None,
     "'Chef, where has our big stove disappeared to?' Senya questions the mysterious absence using a past tense verb."),
    (1, None,
     "'I personally took it to a reliable repair service.' Chef Barinov manufactures an alibi using an adverb and an accusative object."),
    (2, None,
     "'But it was working perfectly yesterday evening!' The cook challenges the claim with an adverb of manner and a time expression."),
    (3, None,
     "'I turned it in for important preventive maintenance.' The chef insists on routine maintenance with a genitive prepositional phrase."),
    (4, None,
     "'And on what are we to cook today?' Senya points out their practical limitation with an interrogative prepositional phrase."),
    (5, None,
     "'For now cook the dishes on this little hotplate.' Barinov orders them to improvise on the domestic electric hotplate."),
    (6, None,
     "'This little hotplate heats up much too slowly!' The cook laments the slow equipment using a reflexive verb and a degree adverb."),
    (7, None,
     "'Stop whining, cooks must know how to do everything!' The boss demands professional flexibility with a modal predicative."),
    (8, None,
     "'The guests will wait for their orders very long!' Senya cautions about kitchen bottlenecks using a compound future construction."),
    (9, None,
     "'Set the heat to four and get to work!' Barinov delivers precise settings using an imperative verb and a numbered dial position."),
    (10, None,
     "'When will they return our old stove to us?' Senya inquires about the return schedule with a future tense verb."),
    (11, None,
     "'In a day or two they will bring everything!' The chef gives an optimistic estimate using an accusative time phrase."),
]

TRANSITION = "Now let's listen to the whole dialogue again at normal conversational speed."

OUTRO = (
    "Now you know how to talk about missing kitchen appliances, cooking adjustments, and chef excuses in Russian. "
    "See you next time!"
)

CLOSING = ("anya", "Поставьте нагрев на четвёрку и работайте!")
