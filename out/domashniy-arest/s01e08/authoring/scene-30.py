# -*- coding: utf-8 -*-
"""Scene 30 of domashniy-arest s01e08: Buying Alcohol."""

ID = "domashniy-arest-s01e08-scene-30"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 8
SCENE = 30
TITLE = "В ночном магазине  (At the Night Shop)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.08"
SOURCE_FILE = "sources/domashniy-arest/s01/e08.ru.dual.srt"

VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "clerk": "angelina",
}

LABELS = {
    "anya": "Самсон",
    "clerk": "Продавщица",
}

INTRO = (
    "After his friends abandoned him, Ivan Samsonov walked into a small corner shop late at "
    "night. Hurt and brooding over being called a fascist, he buys a bottle of alcohol and "
    "vents to the shopkeeper about German cars and sloppy Russian construction. Listen to "
    "the Russian conversation first, and do not worry about catching every word."
)

OPENER = "Let's follow Samsonov on his late-night shop visit line by line."

STORY = [
    ("clerk", "Я в долг больше не даю.",
     "I am not giving credit anymore.",
     [(611, "в долг больше не даю")], ""),
    ("anya", "У меня есть деньги. Дайте шнапс.",
     "I have money. Give me schnapps.",
     [(617, "Шнапс")], ""),
    ("clerk", "Какой шнапс? Есть местная бутылка.",
     "What schnapps? There is a local bottle.",
     [], "clerk pointing to shelf"),
    ("anya", "Мне всё равно. Давайте её.",
     "It is all the same to me. Give me that one.",
     [], "new A1 line for Samsonov buying alcohol"),
    ("anya", "Может, правы мужики были, а?",
     "Maybe the guys were right, huh?",
     [(625, "Может, правы мужики были, а")], ""),
    ("clerk", "Не смеши меня, Самсонов. В чём правы?",
     "Do not make me laugh, Samsonov. In what were they right?",
     [(627, "Не смеши меня, Самсонов")], ""),
    ("anya", "В школе я первый на немецкий записался.",
     "In school I was the first to sign up for German.",
     [(630, "В школе я первый на немецкий записался сам")], ""),
    ("anya", "Все пошли на английский, а я на немецкий.",
     "Everyone went for English, and I for German.",
     [(632, "а я говорю, нет, немецкий")], ""),
    ("clerk", "Ну и что с того?",
     "Well, and what of it?",
     [], "new conversational A1 question"),
    ("anya", "Почему меня всё бесит вокруг?",
     "Why does everything around here bother me?",
     [(638, "все бесит, а")], ""),
    ("anya", "Стыки неровные, всё делают тяп-ляп!",
     "The seams are uneven, they do everything slapdash!",
     [(639, "Это все стыки неровные"), (640, "все тяп-ляп")], ""),
    ("anya", "А в Германии машины хорошие и работают нормально.",
     "And in Germany cars are good and they work properly.",
     [(645, "тачки"), (648, "Зато работают нормально")], "crude lines in 646-647 omitted"),
    ("clerk", "Ладно, иди домой, Самсон. Пора спать.",
     "Alright, go home, Samson. It is time to sleep.",
     [(650, "Ладно, пойду я сам сон")], ""),
]

WALK = [
    (0, None,
     "'I'm not giving credit anymore.' The shopkeeper greets him with a firm rule."),
    (1, "У меня есть деньги.",
     "'I have money.' Samsonov assures her that he can pay in cash."),
    (1, "Дайте шнапс.",
     "'Give me schnapps.' He jokingly asks for German schnapps after being called pro-German."),
    (2, "Какой шнапс?",
     "'What schnapps?' The shopkeeper points to the ordinary domestic shelf."),
    (2, "Есть местная бутылка.",
     "'There is a local bottle.' The feminine adjective agrees with 'bottle'."),
    (3, "Мне всё равно.",
     "'It's all the same to me.' That is the standard phrase for indifference."),
    (3, "Давайте её.",
     "'Give me that one.' He points to the nearest bottle."),
    (4, None,
     "'Maybe the guys were right, huh?' Samsonov wonders aloud if he really has a fascination with Germany."),
    (5, "Не смеши меня, Самсонов.",
     "'Don't make me laugh, Samsonov.' The shopkeeper uses the negative imperative."),
    (5, "В чём правы?",
     "'In what were they right?' The preposition takes the prepositional interrogative."),
    (6, None,
     "'In school I was the first to sign up for German.' He recalls choosing German over English as a child."),
    (7, None,
     "'Everyone went for English, and I for German.' The ellipsis omits the repeated verb."),
    (8, None,
     "'Well, and what of it?' The clerk fails to see any connection."),
    (9, None,
     "'Why does everything around here bother me?' Samsonov vents his frustration with local life."),
    (10, "Стыки неровные, всё делают тяп-ляп!",
     "'The seams are uneven, they do everything slapdash!' That is a classic Russian idiom for careless work."),
    (11, "А в Германии машины хорошие и работают нормально.",
     "'And in Germany cars are good and they work properly.' He admires quality craftsmanship, not fascism."),
    (12, "Ладно, иди домой, Самсон.",
     "'Alright, go home, Samson.' The tired clerk gently urges him to leave."),
    (12, "Пора спать.",
     "'It's time to sleep.' The predicative word expresses the right time for an action."),
]

TRANSITION = "Let's listen to Samsonov's late-night store monologue again."

OUTRO = (
    "Pocketing his bottle, Samsonov heads into the cold night air. In our final scene, "
    "we turn to the surveillance van of the FSB."
)

CLOSING = ("anya", "Ладно, пойду я. Пора спать.")
