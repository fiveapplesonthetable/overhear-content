ID = "domashniy-arest-s01e05-scene-16"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 5
SCENE = 16
TITLE = "Золотые часы мэра  (The Mayor's Gold Watch)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "grisha": "anja", "kostik": "angelina"}
LABELS = {"anya": "Аркадий", "grisha": "Дядя Гриша", "kostik": "Костик"}
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.05"
SOURCE_FILE = "sources/domashniy-arest/s01/e05.ru.dual.srt"

INTRO = (
    "In Arkady's room, Uncle Grisha grips the mayor's sore ear and dares him to call his tough friends right now. "
    "Arkady phones his former bodyguards Vitalik and Valerik, who politely refuse to come because they no longer guard him, "
    "leaving Arkady to bluff for his life. Listen to the Russian conversation first; don't worry about catching every word."
)

STORY = [
    ("grisha", "Звони ребятам своим этим!",
     "Call those guys of yours!",
     [(582, "Звони ребятам своим этим")], ""),
    ("anya", "А вот это зря, ребята. Секундочку!",
     "Now that's a mistake, guys. One second!",
     [(584, "А вот это зря"), (590, "Секундочку")], ""),
    ("anya", "Алло, Виталик, приезжай быстрее! Вы можете сейчас приехать сюда? Меня тут убивают!",
     "Hello, Vitalik, come quickly! Can you come over here right now? They're killing me here!",
     [(593, "Алло, Виталик?"), (596, "вы можете сейчас приехать сюда")], "Vitalik's replies on the phone narrated"),
    ("anya", "В смысле не можете? Живо сюда, быстро, оба!",
     "What do you mean you can't? Get over here right now, quickly, both of you!",
     [(600, "В смысле?"), (604, "Живо сюда, быстро, оба!")], "dropped 'нахрен' in 603 and 'Бандерлоги' in 605"),
    ("anya", "Всё, я вас жду. Через пять минут будут.",
     "Right, I'm waiting for you. They'll be here in five minutes.",
     [(611, "Все, я вас жду"), (612, "Через пять минут будут")], ""),
    ("grisha", "Видишь, Костик, что значит головой думать?",
     "You see, Kostik, what it means to think with your head?",
     [(613, "Видишь, Костик, что значит головой думать?")], ""),
    ("kostik", "Ну да.",
     "Well, yes.",
     [(614, "Ну да")], ""),
    ("grisha", "Серьёзных людей из окна не выкидывают!",
     "Serious people don't get thrown out of a window!",
     [(615, "Серьезных людей из окна не")], "cue 615 'выкидывай' -> 'выкидывают'"),
    ("anya", "Ай, ухо больное! Стой, подожди! Что ты делаешь? Не надо!",
     "Ow, my sore ear! Stop, wait! What are you doing? Don't!",
     [(616, "Ай! Ухо больное!"), (621, "Стой, подожди"), (621, "что ты делаешь? Не надо")], "omitted crude threat in 620"),
    ("anya", "Послушай, я оплачу весь долг этой женщины! Клянусь, весь долг!",
     "Listen, I'll pay this woman's entire debt! I swear, the whole debt!",
     [(625, "Послушай, я оплачу весь долг этой женщины"), (626, "Клянусь, весь долг")], ""),
    ("grisha", "Тогда давай деньги сейчас! Иначе сейчас разберём его.",
     "Then hand over the money right now! Otherwise we'll take him apart right now.",
     [(627, "Давай"), (631, "Сейчас разберем его")], ""),
    ("anya", "Вот у меня на левой руке золотые часы!",
     "Here on my left hand I have a gold watch!",
     [(633, "Вот у меня на левой руке золотые часы!")], ""),
    ("anya", "Возьмите! Они десять тысяч долларов стоят!",
     "Take it! It costs ten thousand dollars!",
     [(634, "Возьмите! Они"), (634, "тысяч долларов стоят!")], "cue 634 '10' written out as 'десять'"),
    ("kostik", "Точно золотые?",
     "Definitely gold?",
     [(637, "Точно золотые?")], ""),
    ("anya", "Ну конечно золотые! Я же мэр, в конце концов!",
     "Well, of course gold! I'm the mayor, after all!",
     [(638, "Ну, конечно, золотые. Я же мэр, в конце концов")], ""),
    ("grisha", "Хорошие часы, забираем их. Ладно, отпусти его.",
     "Nice watch, we're taking it. Alright, let him go.",
     [(635, "хорошие часы"), (639, "Ладно, отпусти его")], ""),
    ("grisha", "Был начальник, стал никто. Так проходит земная слава!",
     "He was a boss, he became nobody. Thus passes earthly glory!",
     [(644, "Был начальник, стал"), (645, "проходит"), (645, "слава")], "cleaned up 'говно' in 644"),
]

OPENER = "Let's follow how Arkady's bluff collapses and costs him his gold watch."

WALK = [
    (0, None,
     "Twisting Arkady's ear, Uncle Grisha calls his bluff: 'Call those guys of yours!'"),
    (1, None,
     "'Now that's a mistake, guys. One second!' Arkady still tries to sound confident as he dials his former chief bodyguard Vitalik."),
    (2, "Алло, Виталик, приезжай быстрее!",
     "'Hello, Vitalik, come quickly!' Notice the informal imperative as Arkady begs his driver to hurry."),
    (2, "Вы можете сейчас приехать сюда? Меня тут убивают!",
     "'Can you come over here right now? They're killing me here!' On the other end of the line, Vitalik and his twin brother Valerik politely reply that they cannot come because they no longer guard him."),
    (3, "В смысле не можете?",
     "'What do you mean you can't?' Arkady is stunned by their refusal."),
    (3, "Живо сюда, быстро, оба!",
     "'Get over here right now, quickly, both of you!' Vitalik calmly says goodbye and hangs up on him, so Arkady pretends to the collectors that help is on the way."),
    (4, "Всё, я вас жду.",
     "'Right, I'm waiting for you,' he says into the dead phone."),
    (4, "Через пять минут будут.",
     "'They'll be here in five minutes.' Notice how Russian uses the preposition meaning 'through' or 'across' with an accusative time span to mean 'in five minutes'. Uncle Grisha sees straight through the act."),
    (5, None,
     "'You see, Kostik, what it means to think with your head?' The noun for 'head' is in the instrumental case, 'with your head'."),
    (6, None,
     "'Well, yes,' Kostik agrees with a nod."),
    (7, None,
     "'Serious people don't get thrown out of a window!' Grisha twists Arkady's ear harder and moves with Kostik to beat him up."),
    (8, "Ай, ухо больное!",
     "'Ow, my sore ear!' Arkady winces in pain as Grisha pulls harder."),
    (8, "Стой, подожди! Что ты делаешь? Не надо!",
     "'Stop, wait! What are you doing? Don't!' Four frantic exclamations in a row."),
    (9, "Послушай, я оплачу весь долг этой женщины!",
     "Terrified, Arkady begs them to stop: 'Listen, I'll pay this woman's entire debt!'"),
    (9, "Клянусь, весь долг!",
     "'I swear, the whole debt!' He uses the reflexive present tense of 'to swear'."),
    (10, None,
     "'Then hand over the money right now! Otherwise we'll take him apart right now.' Having no cash on him, Arkady holds up his left wrist."),
    (11, None,
     "'Here on my left hand I have a gold watch!' Remember that the Russian word for 'watch' or 'clock' is always plural."),
    (12, "Возьмите!",
     "'Take it!' A polite or plural imperative addressed to both men."),
    (12, "Они десять тысяч долларов стоят!",
     "'It costs ten thousand dollars!' Because 'watch' is plural in Russian, he says 'they cost'."),
    (13, None,
     "'Definitely gold?' Kostik checks suspiciously."),
    (14, "Ну конечно золотые!",
     "'Well, of course gold!' Arkady insists."),
    (14, "Я же мэр, в конце концов!",
     "'I'm the mayor, after all!' Uncle Grisha inspects the heavy Swiss watch and nods."),
    (15, "Хорошие часы, забираем их.",
     "'Nice watch, we're taking it,' Grisha decides with satisfaction."),
    (15, "Ладно, отпусти его.",
     "'Alright, let him go,' he tells Kostik."),
    (16, "Был начальник, стал никто.",
     "'He was a boss, he became nobody.' Notice how 'was' takes the nominative here."),
    (16, "Так проходит земная слава!",
     "'Thus passes earthly glory!' Grisha translates his favourite Latin saying as they head for the door."),
]

TRANSITION = "Now listen to the whole scene again from start to finish."

OUTRO = (
    "Leaving Arkady nursing his sore ear and bare wrist, Uncle Grisha and Kostik stroll out of the flat with "
    "a ten-thousand-dollar Swiss watch—while across town Pasha arrives at the City Hall archive. Listen for "
    "'in five minutes', 'entire debt', and 'gold watch' when you watch; see you next time."
)
CLOSING = ("grisha", "Пошли!")
