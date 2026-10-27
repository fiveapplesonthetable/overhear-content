"""
Scene 04 authoring module — Домашний арест S01E05.

На дачу (Off to the dacha)
Cues 146–169 (00:08:41,920 – 00:09:55,000).
"""

ID = "domashniy-arest-s01e05-scene-04"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 5
SCENE = 4
TITLE = "На дачу  (Off to the dacha)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"

SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.05"
SOURCE_FILE = "sources/domashniy-arest/s01/e05.ru.dual.srt"
CUE_RANGE = (146, 169)

VOICES = {
    "narrator": "sky",
    "anya": "alisa",        # Аркадий
    "golovkin": "anja",     # Данила Головкин
    "klavdia": "angelina",  # Клавдия Викторовна
}

LABELS = {
    "anya": "Аркадий",
    "golovkin": "Головкин",
    "klavdia": "Клавдия Викторовна",
}

INTRO = (
    "Still in the communal kitchen after Samson believes the cover story about restaurant hooligans "
    "and steps out to wash his face, Arkady, Nina, Ilona, and the lawyer Danila Golovkin quickly whisper together. "
    "Arkady realises they must hide Samson out of town before he sees the television news, "
    "and then steps into the corridor to silence the nosy neighbour Klavdia Viktorovna. "
    "Let's listen to the conversation in Russian first; don't worry about catching every word."
)

STORY = [
    ("anya",
     "Ты видишь, он не помнит ничего. Пусть так и остаётся.",
     "You see, he doesn't remember anything. Let it stay that way.",
     [(146, "Ты видишь, он не помнит ничего"), (146, "Пусть так и остаётся")],
     ""),
    ("anya",
     "Но здесь он всё равно узнает. Кто-нибудь на улице скажет.",
     "But here he'll find out anyway. Somebody on the street will tell him.",
     [(147, "он всё равно узнает"), (148, "кто-нибудь на улице скажет")],
     "folded Nina's warning into Arkady's realization"),
    ("anya",
     "Его нужно куда-то увезти, понимаете?",
     "We need to take him away somewhere, do you understand?",
     [(150, "Его нужно куда-то увезти, понимаете")],
     ""),
    ("golovkin",
     "Может, его ко мне на дачу?",
     "Maybe to my place, to the dacha?",
     [(151, "Может его ко мне на дачу")],
     ""),
    ("anya",
     "Вот, отлично! Езжайте на дачу.",
     "There, excellent! Go to the dacha.",
     [(152, "Вот, отлично"), (152, "на дачу")],
     ""),
    ("klavdia",
     "Что, стыдно тебе, пьяница?",
     "What, are you ashamed of yourself, you drunkard?",
     [(157, "Что, стыдно тебе")],
     "replaced slang 'алкашандра' with 'пьяница'"),
    ("anya",
     "Клавдия Викторовна, пойдёмте со мной.",
     "Klavdia Viktorovna, come with me.",
     [(160, "Клавдия Викторовна, пойдемте")],
     ""),
    ("anya",
     "Я вам сюрприз покажу один.",
     "I'll show you one surprise.",
     [(160, "я вам сюрприз покажу один")],
     ""),
    ("klavdia",
     "Какой?",
     "What kind?",
     [(161, "Какой")],
     ""),
    ("anya",
     "Фокус.",
     "A magic trick.",
     [(162, "Фокус")],
     ""),
    ("klavdia",
     "Какой сюрприз?",
     "What surprise?",
     [(166, "Какой сюрприз")],
     ""),
    ("anya",
     "Клавдия Викторовна, послушайте. Будете лезть не в своё дело, телевизоры отберём!",
     "Klavdia Viktorovna, listen. If you meddle in what's not your business, we'll take the TVs away!",
     [(167, "Клавдия Викторовна"), (167, "будете лезть не в свое дело, телевизоры отберем")],
     "split into two short sentences"),
    ("anya",
     "И место на кладбище тоже, ясно?",
     "And the cemetery plot too, is that clear?",
     [(168, "И место на кладбище тоже, ясно")],
     ""),
    ("klavdia",
     "Сейчас отберут они!",
     "Oh sure, right now they'll take them away!",
     [(169, "Сейчас отберут они")],
     ""),
]

OPENER = (
    "Now let's walk through the scene line by line and see how Arkady sends Samson to the country house "
    "and warns Klavdia Viktorovna to keep quiet."
)

WALK = [
    (0, "Ты видишь, он не помнит ничего.",
     "As soon as Samson leaves the kitchen, Arkady whispers to Nina: you see, he does not remember anything. "
     "Notice the double negative required in Russian with the pronoun for nothing."),
    (0, "Пусть так и остаётся.",
     "He adds firmly to the group: let it stay just like that."),
    (1, "Но здесь он всё равно узнает.",
     "Nina warns that if Samson stays here, he will find out all the same from television."),
    (1, "Кто-нибудь на улице скажет.",
     "Or somebody on the street will tell him the truth."),
    (2, None,
     "So Arkady tells the team: we need to take him away somewhere, do you understand?"),
    (3, None,
     "The timid lawyer Danila Golovkin raises his hand and suggests: maybe bring him to my place, to the country dacha?"),
    (4, None,
     "Arkady jumps at the idea: there, excellent! Go to the dacha."),
    (5, None,
     "Out in the corridor, the elderly neighbour Klavdia Viktorovna spots Samson by the washbasin and taunts him: "
     "what, are you ashamed of yourself, you drunkard?"),
    (6, None,
     "Before she can mention the car crash, Arkady hurries out and takes her arm: Klavdia Viktorovna, come with me."),
    (7, None,
     "He smiles sweetly and promises: I will show you one surprise."),
    (8, None,
     "Intrigued by the offer, the old woman asks: which one?"),
    (9, None,
     "A magic trick, Arkady replies, leading her away from Samson into her room."),
    (10, None,
     "Once she is inside the room, Klavdia looks at him suspiciously and asks: what surprise?"),
    (11, "Клавдия Викторовна, послушайте.",
     "Arkady drops the polite smile: Klavdia Viktorovna, listen."),
    (11, "Будете лезть не в своё дело, телевизоры отберём!",
     "If you meddle in what is not your business, we will take away the televisions! "
     "Remember that in the previous episode Arkady bribed her with two huge televisions for her vote."),
    (12, None,
     "And he adds the final blow: and the plot at the cemetery too, is that clear?"),
    (13, None,
     "After Arkady leaves, Klavdia scoffs to herself in disbelief: right now they will take them away, sure they will!"),
]

TRANSITION = (
    "That's the whole exchange. Now listen to the scene once more from start to finish "
    "and follow how every line fits together."
)

OUTRO = (
    "With Samson packed off to Golovkin's country house and Klavdia Viktorovna warned not to blab, "
    "Arkady retreats to his room with Ilona to figure out how to save his campaign."
)

CLOSING = ("anya", "Езжайте на дачу.")
