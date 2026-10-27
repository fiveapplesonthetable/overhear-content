ID = "kukhnya-s01e19-scene-10"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 19
SCENE = 10
TITLE = "Подозрительный гость  (A Suspicious Guest)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "kostya": "anja"}
LABELS = {"anya": "Макс", "kostya": "Костя"}
SOURCE_NAME = "Кухня (Kukhnya) S1.19"
SOURCE_FILE = "sources/kukhnya/s01/e19.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 210-212. In the restaurant hall, Max spots Victoria talking with an unfamiliar customer "
    "holding flowers and asks Kostya to go over and find out what they are discussing."
)

INTRO = (
    "In the main hall of Claude Monet, Max notices Victoria having an animated chat with an unfamiliar man. "
    "Filled with suspicion and jealousy, Max tries to convince Kostya to walk over and listen in on their conversation. "
    "Let's listen to their discussion in Russian first."
)

OPENER = "Now let's examine the conversation line by line."

STORY = [
    ("anya", "Костя, посмотри скорее туда.",
     "Kostya, look over there quickly.",
     [(210, "Ой, Костян")], "adapted"),
    ("kostya", "Что случилось, Макс?",
     "What happened, Max?",
     [], "new"),
    ("anya", "О чём Вика говорит с этим человеком?",
     "What is Vika talking about with that person?",
     [(210, "а о чем Вика с этим кренделем разговаривает?")], "adapted"),
    ("kostya", "Макс, я вообще без понятия.",
     "Max, I have no idea at all.",
     [(211, "Макс, я вообще без понятия.")], "adapted"),
    ("anya", "Этот мужчина подарил ей огромный букет.",
     "This man gave her a huge bouquet.",
     [], "new"),
    ("kostya", "Может быть, это просто постоянный гость.",
     "Maybe it is just a regular guest.",
     [], "new"),
    ("anya", "Они слишком мило улыбаются друг другу.",
     "They are smiling too sweetly at each other.",
     [], "new"),
    ("kostya", "Тебе не стоит так сильно переживать.",
     "You should not worry so much.",
     [], "new"),
    ("anya", "Костя, подойди поближе к ним.",
     "Kostya, get closer to them.",
     [(212, "Ну, подойди поближе.")], "adapted"),
    ("kostya", "Зачем мне подходить к их столику?",
     "Why should I approach their table?",
     [], "new"),
    ("anya", "Послушай, что они сейчас обсуждают.",
     "Listen to what they are discussing right now.",
     [], "new"),
    ("kostya", "Ладно, я пойду и узнаю всё.",
     "Fine, I will go and find out everything.",
     [], "new"),
    ("anya", "Спасибо, друг, я жду новостей.",
     "Thank you, friend, I await the news.",
     [], "new"),
]

WALK = [
    (0, None,
     "'Kostya, look over there quickly.' -- Max frantically points across the dining room."),
    (1, None,
     "'What happened, Max?' -- Kostya asks what is troubling his friend."),
    (2, None,
     "'What is Vika talking about with that person?' -- Max questions the identity of the customer."),
    (3, None,
     "'Max, I have no idea at all.' -- The bartender confesses his total ignorance."),
    (4, None,
     "'This man gave her a huge bouquet.' -- Max points out the suspicious romantic flowers."),
    (5, None,
     "'Maybe it is just a regular guest.' -- Kostya offers a logical and innocent explanation."),
    (6, None,
     "'They are smiling too sweetly at each other.' -- Max reads romance into their polite smiles."),
    (7, None,
     "'You should not worry so much.' -- Kostya advises him not to jump to conclusions."),
    (8, None,
     "'Kostya, get closer to them.' -- Max pushes his friend to spy on them."),
    (9, None,
     "'Why should I approach their table?' -- The bartender questions the risky assignment."),
    (10, None,
     "'Listen to what they are discussing right now.' -- Max wants concrete intelligence on their conversation."),
    (11, None,
     "'Fine, I will go and find out everything.' -- Kostya reluctantly agrees to help him."),
    (12, None,
     "'Thank you, friend, I await the news.' -- Max thanks his friend for taking the risk."),
]

TRANSITION = "Now let's listen to the hall discussion once again."

OUTRO = (
    "Watching Kostya walk toward Victoria's table, Max nervously waits by the kitchen doors, "
    "hoping to uncover the truth behind the mysterious encounter."
)

CLOSING = ("anya", "Спасибо, друг, я жду новостей.")
