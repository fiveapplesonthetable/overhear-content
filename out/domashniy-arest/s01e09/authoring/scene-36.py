"""Scene 36 — I Lied to You (s01e09, 00:58:34–01:00:37)."""

ID = "domashniy-arest-s01e09-scene-36"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 9
SCENE = 36
TITLE = "Я вам соврал  (I Lied to You)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.09"
SOURCE_FILE = "sources/domashniy-arest/s01/e09.ru.dual.srt"

VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "marina": "angelina",
}

LABELS = {
    "anya": "Аркадий",
    "marina": "Марина",
}

INTRO = (
    "In the hospital room after Samsonov's dramatic debate victory, Marina Sergeyevna visits "
    "former mayor Arkady Anikeyev in his ward. Surprised and touched by her visit, Arkady decides "
    "it is time to tell the truth about his missing fortune. Let's listen to their conversation in "
    "Russian first; don't worry if you don't understand every word right away."
)

STORY = [
    ("anya", "Марина, спасибо, что пришли ко мне.",
     "Marina, thank you for visiting me.",
     [(1034, "что вы пришли")], ""),
    ("marina", "Я хотела узнать, как ваше самочувствие.",
     "I wanted to know how you are feeling.",
     [(1034, "Но это очень хорошо")], ""),
    ("anya", "Я очень хотел поговорить с вами.",
     "I really wanted to talk with you.",
     [(1037, "хотел с вами поговорить")], ""),
    ("marina", "О чём вы хотите поговорить?",
     "What do you want to talk about?",
     [(1037, "Я вот как раз хотел")], ""),
    ("anya", "Я хочу попросить у вас прощения.",
     "I want to ask your forgiveness.",
     [(1038, "Хотел извиниться")], ""),
    ("marina", "За что вы хотите извиниться?",
     "What do you want to apologize for?",
     [(1038, "Хотел извиниться")], ""),
    ("anya", "Потому что я соврал про деньги.",
     "Because I lied to you about the money.",
     [(1038, "соврал насчет денег")], ""),
    ("anya", "Я больше не хочу вам врать.",
     "I don't want to lie to you anymore.",
     [(1039, "не хочу вам совсем врать")], ""),
    ("marina", "А где же эти деньги?",
     "Where is that money then?",
     [(1040, "деньги я")], ""),
    ("anya", "Я спрятал их в детском саду.",
     "I hid them in the kindergarten.",
     [(1040, "спрятал на самом деле в детском суду")], ""),
    ("marina", "В детском саду? Почему там?",
     "In the kindergarten? Why there?",
     [(1041, "Почему?")], ""),
    ("anya", "Потому что там никто не ищет.",
     "Because nobody looks there.",
     [(1040, "на самом деле")], ""),
    ("marina", "Вы очень странный человек, Аркадий.",
     "You are a very strange man, Arkady.",
     [(1041, "Почему?")], ""),
]

OPENER = "Now let's walk through the confession in the hospital ward line by line."

WALK = [
    (0, None,
     "'Marina, thank you for visiting me.' Arkady expresses polite gratitude using the standard formula for thanking someone."),
    (1, None,
     "'I wanted to know how you are feeling.' The feminine past tense verb expresses her polite concern for his health."),
    (2, None,
     "'I really wanted to talk with you.' The past tense modal verb pairs with an imperfective infinitive to state an intention."),
    (3, None,
     "'What do you want to talk about?' The prepositional phrase asks directly about the topic of conversation."),
    (4, None,
     "'I want to ask your forgiveness.' The idiomatic construction literally means 'to request forgiveness from someone'."),
    (5, None,
     "'What do you want to apologize for?' The preposition governs the accusative interrogative pronoun."),
    (6, None,
     "'Because I lied to you about the money.' The past tense verb takes a colloquial prepositional phrase indicating the topic."),
    (7, None,
     "'I don't want to lie to you anymore.' The negative construction combines an adverb meaning 'no longer' with an imperfective infinitive."),
    (8, None,
     "'Where is that money then?' The emphatic particle adds mild curiosity to the question about location."),
    (9, None,
     "'I hid them in the kindergarten.' The prepositional phrase names the specific building where the funds were placed."),
    (10, None,
     "'In the kindergarten? Why there?' The short rhetorical question reflects Marina's astonishment at his confession."),
    (11, None,
     "'Because nobody looks there.' The negative pronoun pairs with a negated present tense verb meaning 'no one searches'."),
    (12, None,
     "'You are a very strange man, Arkady.' The evaluative adjective summarizes her reaction to his confession."),
]

TRANSITION = "Now let's listen to the entire conversation once again from start to finish."

OUTRO = (
    "Arkady comes clean to Marina about hiding the embezzled money in the local kindergarten, "
    "taking a tentative first step toward honesty."
)

CLOSING = ("anya", "Я больше не хочу вам врать.")
