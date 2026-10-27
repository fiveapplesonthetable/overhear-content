"""
Scene 16 of s01e07: "Ну не шуршите!  (Stop Rustling!)" (00:29:32,310 -> 00:31:44,050, cues 618-651).

At night, Arkady ruins Eduard's romantic plans by banging on the bedroom wall
and shouting for quiet for a sick man, while Samsonov phones Danya to apologize
and invite him over with his cheese fondue tomorrow.
"""

ID = "domashniy-arest-s01e07-scene-16"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 7
SCENE = 16
TITLE = "Ну не шуршите!  (Stop Rustling!)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.07"
SOURCE_FILE = "sources/domashniy-arest/s01/e07.ru.dual.srt"

VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "marina": "angelina",
    "samson": "anja",
}

LABELS = {
    "anya": "Аркадий",
    "marina": "Марина",
    "samson": "Самсон",
}

INTRO = (
    "In the last scene, Samsonov dreamed that ancient strategist Sun Tzu told him to lure lawyer Danya onto his own territory. "
    "Now it is late at night in the communal flat: Arkady is listening through the thin wall of Marina's room to spoil Eduard's romantic evening, while Samsonov phones Danya to set his trap in motion. "
    "Listen to the Russian first, and don't worry about catching every word."
)

STORY = [
    ("marina", "А вдруг мы его разбудим? И у него начнутся боли?",
     "What if we wake him up? And what if his pains start?",
     [(618, "А вдруг мы его разбудим"), (618, "и у него начнутся боли")], ""),
    ("marina", "Ему в больнице всё сделали. Ну а вдруг ему станет хуже?",
     "They did everything for him at the hospital. Well, what if he gets worse?",
     [(619, "в больнице"), (621, "Ну а вдруг ему станет хуже")], "Eduard's reassurance in 619-620 echoed by Marina"),
    ("marina", "Ты думаешь только о себе! Просто день был сложный, давай спать.",
     "You only think about yourself! It was just a tough day, let's go to sleep.",
     [(623, "Ты думаешь только о"), (630, "Просто день был сложный"), (631, "давай спать")], "adult pill joke in 624-629 omitted"),
    ("anya", "Ай, да что ж такое? Ну только я задремал!",
     "Oh, what is going on? I had only just dozed off!",
     [(634, "Ай, да что ж такое"), (635, "Ну только я задремал")], ""),
    ("anya", "Вы можете помолчать ради больного человека? Мне нужен покой!",
     "Can you be quiet for the sake of a sick person? I need peace and quiet!",
     [(637, "ради больного человека")], "crude 'неуемную похоть' in 637 cleaned to 'помолчать'"),
    ("anya", "Ну не шуршите там за стеной!",
     "Stop rustling behind the wall!",
     [(638, "Ну не шуршите")], ""),
    ("anya", "Ну будет тишина или нет?",
     "Will there be silence or not?",
     [(639, "Ну будет тишина или нет")], ""),
    ("marina", "Да спим мы уже, спим!",
     "We are sleeping already, we are sleeping!",
     [(640, "Да спим мы")], ""),
    ("samson", "Алло, Даня, привет! Это Самсонов. Как дела?",
     "Hello, Danya, hi! This is Samsonov. How are things?",
     [(641, "Алло, Даня, привет"), (641, "Самсонов")], ""),
    ("samson", "Слушай, ты прости меня сегодня. Я был неправ.",
     "Listen, forgive me for today. I was wrong.",
     [(643, "Слушай, ты прости меня сегодня")], ""),
    ("samson", "Славик сказал, ты завтра придёшь? Хочешь фондю принести?",
     "Slavik said you are coming over tomorrow? Do you want to bring fondue?",
     [(645, "ты завтра"), (646, "фондю"), (646, "принести")], ""),
    ("samson", "Не передумал ещё? Давай, приходи к нам в гости!",
     "Haven't you changed your mind yet? Come on, come visit us!",
     [(647, "Не передумал еще"), (648, "давай, приходи")], ""),
    ("samson", "Не бойся, всё в порядке! Посидим дружно за столом.",
     "Don't be afraid, everything is fine! We will sit together in a friendly way at the table.",
     [(650, "все в порядке")], "crude 'По писярику накатим' / 'не бздо' (649-650) cleaned"),
    ("samson", "Ждём тебя завтра! Спокойной ночи, Даня.",
     "We are waiting for you tomorrow! Good night, Danya.",
     [(651, "Спокойной ночи")], ""),
]

OPENER = "Did you hear how Arkady ruined Eduard's night and how Samsonov invited Danya over? Let's break it down."

WALK = [
    (0, "А вдруг мы его разбудим?", "In Marina's bedroom, Marina whispers anxiously about Arkady in the next room: 'What if we wake him up?'"),
    (0, "И у него начнутся боли?", "'And what if his pains start?' Eduard grumbles that the hospital already took care of everything."),
    (1, "Ему в больнице всё сделали.", "'They did everything for him at the hospital,' Marina repeats Eduard's excuse."),
    (1, "Ну а вдруг ему станет хуже?", "'Well, what if he gets worse?' Notice the dative pronoun with the impersonal verb for feeling worse."),
    (2, "Ты думаешь только о себе!", "When Eduard complains that Marina only thinks about Arkady, she snaps back: 'You only think about yourself!'"),
    (2, "Просто день был сложный, давай спать.", "'It was just a hard day, let's go to sleep.' Still, a moment later they start whispering again."),
    (3, "Ай, да что ж такое?", "Right on cue, Arkady bangs his plaster cast against the wall: 'Oh, what is going on?'"),
    (3, "Ну только я задремал!", "'I had only just dozed off!' he groans loudly."),
    (4, "Вы можете помолчать ради больного человека?", "'Can you be quiet for the sake of a sick person?' he calls through the wall."),
    (4, "Мне нужен покой!", "'I need peace and quiet!'"),
    (5, None, "A few seconds later he knocks again: 'Well, stop rustling behind the wall!' Notice the negative imperative plural."),
    (6, None, "'Well, will there be silence or not?' Arkady demands."),
    (7, None, "'We are sleeping already, we're sleeping!' Marina calls back, completely ending Eduard's romantic mood."),
    (8, "Алло, Даня, привет!", "Meanwhile, Samsonov picks up his phone and calls Nina's lawyer friend: 'Hello, Danya, hi!'"),
    (8, "Это Самсонов. Как дела?", "'This is Samsonov. How are things?'"),
    (9, "Слушай, ты прости меня сегодня.", "'Listen, forgive me for today,' Samsonov says, pretending to make peace."),
    (9, "Я был неправ.", "'I was wrong.'"),
    (10, "Славик сказал, ты завтра придёшь?", "'Slavik said you are coming over tomorrow?' he asks."),
    (10, "Хочешь фондю принести?", "'Do you want to bring fondue?'"),
    (11, "Не передумал ещё?", "'Haven't you changed your mind yet?'"),
    (11, "Давай, приходи к нам в гости!", "'Come on, come visit us!'"),
    (12, "Не бойся, всё в порядке!", "'Don't be afraid, everything is fine!' Samsonov reassures him."),
    (12, "Посидим дружно за столом.", "'We will sit together in a friendly way at the table.'"),
    (13, "Ждём тебя завтра!", "'We're waiting for you tomorrow!'"),
    (13, "Спокойной ночи, Даня.", "'Good night, Danya,' Samsonov says with a sly smile."),
]

TRANSITION = "Now let's listen to the whole scene again from start to finish."

OUTRO = "While Arkady grins in the dark after ruining Eduard's evening through the wall, Samsonov hangs up the phone satisfied that Danya has walked right into his invitation."

CLOSING = ("anya", "Ну будет тишина или нет?")
