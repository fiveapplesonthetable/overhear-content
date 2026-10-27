ID = "domashniy-arest-s01e05-scene-15"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 5
SCENE = 15
TITLE = "Детей обижать нехорошо  (Scaring Children Isn't Right)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "grisha": "anja", "kostik": "angelina"}
LABELS = {"anya": "Аркадий", "grisha": "Дядя Гриша", "kostik": "Костик"}
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.05"
SOURCE_FILE = "sources/domashniy-arest/s01/e05.ru.dual.srt"

INTRO = (
    "While Ilona searches the City Hall archive, the two microloan debt collectors, Uncle Grisha and young Kostik, "
    "return to the communal flat. Finding Marina's ten-year-old son Lyosha home alone, they ask where his mother is, "
    "and when the boy bravely calls them extortionists, Uncle Grisha decides to smash the furniture in Marina's room. "
    "We'll hear the scene in Russian first; don't worry about catching every word."
)

STORY = [
    ("grisha", "Мальчик, твоя мама должна нам денег!",
     "Boy, your mum owes us money!",
     [(549, "твоя мама должна нам денег")], "Lyosha's lines in 546-551 narrated"),
    ("grisha", "Давай, Костик, оставим ей послание!",
     "Come on, Kostik, let's leave her a message!",
     [(553, "Давай, Костик"), (554, "Оставим ей послание")], ""),
    ("kostik", "Ты что, издеваешься, что ли?",
     "Are you kidding me?",
     [(555, "Ты что, издеваешься, что ли?")], ""),
    ("grisha", "Смотри, как надо иллюстрировать! Круши! Ломай!",
     "Watch how you have to illustrate! Smash! Break!",
     [(556, "Смотри, как надо иллюстрировать"), (557, "Круши! Ломай!")], ""),
    ("kostik", "Давай вот это, да!",
     "Go on, this one, yes!",
     [(558, "Давай вот это, да!")], ""),
    ("anya", "Послушайте, ребята, можно вас на минуту?",
     "Listen, guys, can I have you for a minute?",
     [(560, "Послушайте, ребята"), (561, "Можно вас на минуту?")], ""),
    ("grisha", "Зачем?",
     "What for?",
     [(562, "Зачем?")], ""),
    ("anya", "Есть интересный разговор. Всё хорошо, малыш.",
     "There's an interesting conversation. Everything is fine, kid.",
     [(563, "Есть интересный разговор"), (566, "Все хорошо, малыш")], ""),
    ("anya", "Ребята, я понимаю, работа у вас такая. Но детей обижать нехорошо.",
     "Guys, I understand, that's the job you have. But hurting children isn't right.",
     [(567, "работа у вас такая"), (568, "Детей"), (568, "нехорошо")], "cue 568 'бежать' -> 'обижать'"),
    ("kostik", "Дядя Гриша, я же его знаю! Это мэр, которого из окна выкинули!",
     "Uncle Grisha, I know him! This is the mayor whom they threw out of the window!",
     [(569, "Гриша, я же его знаю. Это мэр, которого из окна выкинули")], "cue 569 'Здесь Гриша' -> 'Дядя Гриша'"),
    ("anya", "Совершенно верно, я мэр этого города. И предложение у меня к вам такое.",
     "Quite right, I am the mayor of this town. And my offer to you is this.",
     [(570, "Совершенно верно"), (570, "Мэр"), (571, "предложение у меня к вам такое")], ""),
    ("anya", "Вы сейчас отсюда оба уходите. И больше сюда не возвращаетесь. Ясно?",
     "You both leave here right now. And you never come back here again. Clear?",
     [(572, "Вы сейчас отсюда оба уходите"), (572, "больше сюда не возвращаетесь"), (573, "Ясно?")], "split into two short sentences"),
    ("grisha", "Как любопытно. И почему мы должны вам подчиняться?",
     "How curious. And why must we obey you?",
     [(574, "Как любопытно. И почему мы должны вам подчиняться?")], ""),
    ("anya", "У меня много опасных друзей. А иначе я позвоню ребятам.",
     "I have many dangerous friends. Otherwise I'll call the guys.",
     [(575, "А иначе я позвоню ребятам")], ""),
    ("anya", "Они приедут и сделают вам так больно!",
     "They'll come and hurt you so badly!",
     [(576, "Они приедут и сделают вам так больно")], "omitted crude underwear threat in 578-581"),
    ("kostik", "Дядя Гриша, может, пойдём отсюда?",
     "Uncle Grisha, maybe let's go from here?",
     [(577, "Пойдем отсюда")], ""),
]

OPENER = "Let's break down how Arkady steps in to stop the debt collectors."

WALK = [
    (0, None,
     "Finding young Lyosha alone in Marina's room, Uncle Grisha tells the boy: 'Boy, your mum owes us money!' When Lyosha replies that his mother called them extortionists, Grisha turns to timid Kostik."),
    (1, None,
     "'Come on, Kostik, let's leave her a message!' Notice the first-person plural future form used as 'let's leave'."),
    (2, None,
     "Kostik is shocked: 'Are you kidding me?' Earlier on the stairs Grisha complained that Kostik did not know how to illustrate a threat, so now Grisha demonstrates."),
    (3, "Смотри, как надо иллюстрировать!",
     "'Watch how you have to illustrate!'"),
    (3, "Круши! Ломай!",
     "'Smash! Break!' Two blunt informal imperatives as Grisha starts wrecking the room."),
    (4, None,
     "'Go on, this one, yes!' Hearing the noise from the corridor, Arkady walks in."),
    (5, None,
     "'Listen, guys, can I have you for a minute?' Literally 'is it possible to have you for a minute?', an everyday polite way to ask for a word with someone."),
    (6, None,
     "'What for?' One blunt question word."),
    (7, "Есть интересный разговор.",
     "'There's an interesting conversation.'"),
    (7, "Всё хорошо, малыш.",
     "He reassures young Lyosha — 'Everything is fine, kid' — and leads the two collectors out to his own room."),
    (8, "Ребята, я понимаю, работа у вас такая.",
     "'Guys, I understand, that's the job you have.'"),
    (8, "Но детей обижать нехорошо.",
     "'But hurting children isn't right.' Suddenly Kostik stares at Arkady's glasses and recognises him."),
    (9, "Дядя Гриша, я же его знаю!",
     "'Uncle Grisha, I know him!'"),
    (9, "Это мэр, которого из окна выкинули!",
     "'This is the mayor whom they threw out of the window!' Notice the accusative relative pronoun for an animate masculine noun."),
    (10, "Совершенно верно, я мэр этого города.",
     "'Quite right, I am the mayor of this town.'"),
    (10, "И предложение у меня к вам такое.",
     "'And my offer to you is this.'"),
    (11, "Вы сейчас отсюда оба уходите.",
     "'You both leave here right now.' Present tense used as a firm command."),
    (11, "И больше сюда не возвращаетесь. Ясно?",
     "'And you never come back here again. Clear?' Contrast the two adverbs: 'from here' versus 'to here'. Uncle Grisha is unimpressed."),
    (12, None,
     "'How curious. And why must we obey you?' The reflexive verb takes the dative case, 'to you'. Arkady tries to intimidate them."),
    (13, "У меня много опасных друзей.",
     "'I have many dangerous friends.' After 'many', both the adjective and the noun take the genitive plural."),
    (13, "А иначе я позвоню ребятам.",
     "'Otherwise I'll call the guys.'"),
    (14, None,
     "'They'll come and hurt you so badly!' Nervous Kostik immediately wants to leave."),
    (15, None,
     "'Uncle Grisha, maybe let's go from here?'"),
]

TRANSITION = "Now let's listen to the whole confrontation again."

OUTRO = (
    "Arkady smugly tells them to leave before they get hurt, but instead of walking out, Uncle Grisha reaches over "
    "and grabs Arkady hard by his sore ear. Listen for 'message', 'hurting children', and 'dangerous friends' when "
    "you watch; see you next time."
)
CLOSING = ("anya", "Да, дядя Гриша, идите!")
