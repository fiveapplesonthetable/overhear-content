# -*- coding: utf-8 -*-
"""Scene 27 of domashniy-arest s01e08: Friends Reject Ivan."""

ID = "domashniy-arest-s01e08-scene-27"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 8
SCENE = 27
TITLE = "Друзья против Самсона  (Friends Reject Ivan)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.08"
SOURCE_FILE = "sources/domashniy-arest/s01/e08.ru.dual.srt"

VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "grisha": "anja",
    "sanya": "angelina",
}

LABELS = {
    "anya": "Самсон",
    "grisha": "Гриша",
    "sanya": "Саня",
}

INTRO = (
    "In the previous scene, Arkady's political rivals plotted their next move. Now on "
    "the building site, Ivan Samsonov gathers his construction co-workers to ask for their "
    "support at the upcoming televised debates, only to hear one ridiculous excuse after "
    "another. Listen to the Russian conversation first, and do not worry about catching "
    "every word."
)

OPENER = "Let's examine how Samsonov's friends turn their backs on him line by line."

STORY = [
    ("anya", "Короче, мужики! Если поддержите меня, мы прорвёмся.",
     "In short, guys! If you support me, we will break through.",
     [(458, "короче, мужики"), (459, "Если поддержите меня, прорвемся")], ""),
    ("anya", "Давайте дадим жару на этих дебатах! Что скажете?",
     "Let's bring the heat at these debates! What do you say?",
     [(460, "Давайте дадим жару на этих дебатах"), (461, "Что скажете")], ""),
    ("grisha", "Самсон, я не могу. У меня тёща приезжает.",
     "Samson, I cannot. My mother-in-law is arriving.",
     [(462, "Самсон, я не могу"), (463, "У меня теща приезжает")], ""),
    ("grisha", "Встретить надо.",
     "I need to meet her.",
     [(464, "Устретить надо")], ""),
    ("anya", "А ты чего молчишь? К тебе кто приезжает?",
     "And why are you silent? Who is coming to see you?",
     [(467, "Вот тебя кто приезжает")], ""),
    ("sanya", "Никто. У меня зуб болит.",
     "Nobody. My tooth hurts.",
     [(468, "Никто"), (469, "У меня зуб болит")], ""),
    ("sanya", "Я к врачу записался.",
     "I made an appointment with the doctor.",
     [(470, "Я к врачу записался")], ""),
    ("anya", "Вы что, с дуба рухнули? Какой зуб?",
     "Have you lost your minds? What tooth?",
     [(474, "Вы что, с дуба рухнули"), (476, "Какой")], "crude 'нахрен' omitted"),
    ("sanya", "Зуб мудрости болит!",
     "My wisdom tooth hurts!",
     [(477, "мудрости"), (478, "мудрости")], ""),
    ("anya", "Мы твою тёщу три года назад похоронили! Откуда она приезжает?",
     "We buried your mother-in-law three years ago! Where is she coming from?",
     [(483, "Мы твою тещу хоронили"), (485, "откуда он у тебя приезжает-то")], ""),
    ("grisha", "Самсон, если мы пойдём, все подумают плохо.",
     "Samson, if we go, everyone will think badly.",
     [(488, "Самсон"), (489, "ну если я пойду"), (490, "все подумают")], ""),
    ("grisha", "Подумают, что мы плохих людей поддерживаем.",
     "They will think that we support bad people.",
     [(491, "поддерживаю")], "crude accusations simplified to A1"),
    ("anya", "А по-вашему, я плохой человек? Чего молчите?",
     "And in your opinion, am I a bad person? Why are you silent?",
     [(492, "А, по-вашему, я что"), (493, "Чего молчите")], ""),
    ("sanya", "Слушай, Самсон, ты извини. Но ты изменился.",
     "Listen, Samson, forgive us. But you have changed.",
     [(494, "Слушай, Самсон, ты извини"), (494, "есть в тебе это")], ""),
    ("anya", "Ну и сидите тут одни! Я сам всё сделаю.",
     "Well, stay here by yourselves! I will do everything myself.",
     [], "new closing A1 line as Samsonov storms out"),
]

WALK = [
    (0, "Короче, мужики!",
     "'In short, guys!' Samsonov addresses his construction team informally."),
    (0, "Если поддержите меня, мы прорвёмся.",
     "'If you support me, we will break through.' The conditional sentence uses the future tense in Russian."),
    (1, "Давайте дадим жару на этих дебатах!",
     "'Let's bring the heat at these debates!' The idiom means to show everyone what they are capable of."),
    (1, "Что скажете?",
     "'What do you say?' He looks around the locker room expecting enthusiastic cheers."),
    (2, "Самсон, я не могу.",
     "'Samson, I can't.' His friend Grisha makes a nervous excuse."),
    (2, "У меня тёща приезжает.",
     "'My mother-in-law is arriving.' In Russian, 'at my place' is expressed with the preposition and genitive."),
    (3, None,
     "'I need to meet her.' Notice the predicative word used with the infinitive to express necessity."),
    (4, "А ты чего молчишь?",
     "'And why are you silent?' Samsonov turns sharply to Sanya."),
    (4, "К тебе кто приезжает?",
     "'Who is coming to your place?' The preposition with dative indicates motion toward someone."),
    (5, "Никто.",
     "'Nobody.' Sanya stares down at the floor."),
    (5, "У меня зуб болит.",
     "'My tooth hurts.' The verb means 'to ache' or 'to cause pain'."),
    (6, None,
     "'I made an appointment with the doctor.' The reflexive verb means to sign up or register for an appointment."),
    (7, "Вы что, с дуба рухнули?",
     "'Have you fallen from an oak tree?' This colourful Russian idiom means 'have you gone completely mad?'."),
    (7, "Какой зуб?",
     "'What tooth?' Samsonov sees right through all of their transparent excuses."),
    (8, None,
     "'My wisdom tooth hurts!' Sanya stubbornly insists on his dentist appointment."),
    (9, "Мы твою тёщу три года назад похоронили!",
     "'We buried your mother-in-law three years ago!' Samsonov angrily reminds Grisha of the funeral they all attended."),
    (9, "Откуда она приезжает?",
     "'Where is she coming from?' He asks sarcastically if she is rising from the cemetery."),
    (10, "Самсон, если мы пойдём, все подумают плохо.",
     "'Samson, if we go, everyone will think badly.' Grisha admits the real problem."),
    (11, None,
     "'They will think that we support bad people.' The smear campaign against Samsonov has scared his own friends."),
    (12, "А по-вашему, я плохой человек?",
     "'And in your opinion, am I a bad person?' Notice the parenthetical phrase meaning 'in your view'."),
    (12, "Чего молчите?",
     "'Why are you silent?' Nobody in the room dares to meet his eyes."),
    (13, "Слушай, Самсон, ты извини.",
     "'Listen, Samson, forgive us.' Sanya tries to soften the blow."),
    (13, "Но ты изменился.",
     "'But you have changed.' They feel he has moved into the mayor's corrupt circle."),
    (14, "Ну и сидите тут одни!",
     "'Well, stay here by yourselves!' Samsonov snaps back in deep hurt."),
    (14, "Я сам всё сделаю.",
     "'I will do everything myself.' He slams the locker room door behind him."),
]

TRANSITION = "Now listen to Samsonov's confrontation with his friends again."

OUTRO = (
    "Shocked that his closest co-workers have deserted him right before the election debates, "
    "Samsonov heads off alone. In the next scene, we check back on young Lyosha and his doctor."
)

CLOSING = ("anya", "Я сам всё сделаю.")
