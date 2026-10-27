ID = "domashniy-arest-s01e11-scene-07"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 11
SCENE = 7
TITLE = "Паника в штабе  (Panic at Headquarters)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "aide": "anja"}
LABELS = {"anya": "Павел Юрьевич", "aide": "Помощник"}
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.11"
SOURCE_FILE = "sources/domashniy-arest/s01/e11.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 114-129. Furious over the news of the presidential visit, Pavel lashes out at everyone in the hallway. "
    "His campaign aide attempts to reassure him with polling figures, but Pavel angrily rejects the numbers "
    "and throws everyone out of the room."
)

INTRO = (
    "In this scene, Pavel Yuryevich erupts in anger at his campaign headquarters. "
    "He furiously berates his staff and threatens to fire anyone idling in the corridors. "
    "When his aide tries to calm him with positive poll numbers, Pavel dismisses them in utter panic. "
    "Let's listen to their confrontation in Russian first."
)

STORY = [
    ("anya", "Почему вы все здесь стоите?",
     "Why are you all standing here?",
     [(117, "Что мы смотрим, стоим")], ""),
    ("anya", "Быстро идите работать на свои места!",
     "Quickly go work at your places!",
     [(117, "Идите, идите"), (117, "быстрее")], ""),
    ("anya", "Я уволю каждого ленивого сотрудника!",
     "I will fire every lazy employee!",
     [(118, "Уволю")], ""),
    ("aide", "Павел Юрьевич, пожалуйста, послушайте меня.",
     "Pavel Yuryevich, please listen to me.",
     [(119, "Павел Юрьевич")], ""),
    ("anya", "Что у вас там опять случилось?",
     "What has happened over there with you again?",
     [(120, "Да")], ""),
    ("aide", "В целом наша ситуация пока нормальная.",
     "Overall our situation is still normal.",
     [(121, "в целом ситуация нормальная")], ""),
    ("aide", "У вас по-прежнему есть хорошее преимущество.",
     "You still have a good lead.",
     [(121, "У вас по-прежнему преимущество")], ""),
    ("anya", "О каком преимуществе ты сейчас говоришь?",
     "What lead are you talking about now?",
     [(122, "какие 6%")], ""),
    ("anya", "Если приедет Путин, Самсонов сразу победит!",
     "If Putin arrives, Samsonov will immediately win!",
     [(122, "Если Путин приедет")], ""),
    ("anya", "Ты понимаешь, что это прямая поддержка?",
     "Do you understand that this is direct support?",
     [(123, "Ты не понимаешь, что это поддержка прямая")], ""),
    ("aide", "Но ведь это же совсем нечестно!",
     "But that is completely unfair!",
     [(124, "Это же"), (126, "нечестно")], ""),
    ("anya", "Всё, замолчите и уйдите вон!",
     "That's it, be quiet and get out!",
     [(127, "Все, пошли вон")], ""),
    ("anya", "Уходите отсюда прямо сейчас, я сказал!",
     "Leave here right now, I said!",
     [(128, "я сказал")], ""),
    ("anya", "И к тебе это тоже относится!",
     "And this applies to you too!",
     [(129, "К тебе это тоже относится")], ""),
]

OPENER = (
    "Now let's examine Pavel's furious breakdown line by line. "
    "Pavel scolds the campaign team and rejects all reassuring statistics."
)

WALK = [
    (0, None,
     "'Why are you all standing here?' Pavel lashes out at the staff lingering in the hallway."),
    (1, None,
     "'Quickly go work at your places!' The imperative forms command the staff to return to work."),
    (2, None,
     "'I will fire every lazy employee!' The future tense verb threatens imminent dismissal."),
    (3, None,
     "'Pavel Yuryevich, please listen to me.' The campaign aide tries to calm his boss down."),
    (4, None,
     "'What has happened over there with you again?' Pavel impatiently demands the latest news."),
    (5, None,
     "'Overall our situation is still normal.' The adverbial phrase presents an optimistic assessment."),
    (6, None,
     "'You still have a good lead.' The construction with 'u vas' indicates a statistical advantage."),
    (7, None,
     "'What lead are you talking about now?' Pavel dismisses the polling numbers angrily."),
    (8, None,
     "'If Putin arrives, Samsonov will immediately win!' The conditional clause expresses Pavel's panic."),
    (9, None,
     "'Do you understand that this is direct support?' The rhetorical question emphasizes presidential authority."),
    (10, None,
     "'But that is completely unfair!' The short neuter adjective describes the political injustice."),
    (11, None,
     "'That's it, be quiet and get out!' Pavel barks an order to clear the room."),
    (12, None,
     "'Leave here right now, I said!' The past tense verb reinforces his angry command."),
    (13, None,
     "'And this applies to you too!' The reflexive verb directs the dismissal at the aide."),
]

TRANSITION = "Now let's listen to Pavel's confrontation with his campaign staff once more without pauses."
OUTRO = (
    "Driven to desperation by Samsonov's growing advantage, Pavel drives out his own team. "
    "In the next scene, Arkady begins training Samsonov for the presidential encounter."
)
CLOSING = ("anya", "И к тебе это тоже относится!")
