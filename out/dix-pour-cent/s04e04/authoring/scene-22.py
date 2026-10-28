ID = "dix-pour-cent-s04e04-scene-22"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 4
SCENE = 22
TITLE = "Camille Valentini, je suis absente  (Camille Valentini, I am absent)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E04"
SOURCE_FILE = "sources/dix-pour-cent/s04/e04.fr.dual.srt"

VOICES = {
    "narrator": "sky",
    "lea": "lucie",
    "mathias": "theo"
}

INTRO = (
    "Mathias realises his mistake. He wants to apologise to his daughter. "
    "He takes his phone and calls Camille. But she doesn't answer. "
    "We'll hear it in French first, don't worry about catching every word."
)
OPENER = "Let's go back through it. Mathias calls Camille."
TRANSITION = "Let's listen to the whole scene again."
OUTRO = "And that's it for this scene. When you watch the episode, listen out for the exchange around camille valentini, i am absent, and for the words meaning 'to answer' and 'to please'. You'll catch them now. See you next time."

STORY = [
    ("mathias", "Camille, réponds-moi.", "Camille, answer me.", [], ""),
    ("mathias", "S'il te plaît, ma chérie.", "Please, my darling.", [], ""),
    ("lea", "Camille Valentini, je suis absente,", "Camille Valentini, I'm not available,", [(1206, "Camille Valentini, je suis absente,")], ""),
    ("lea", "mais laissez-moi un message.", "but please leave a message.", [(1206, "mais laissez-moi un message.")], ""),
    ("mathias", "C'est moi, Mathias.", "It's me, Mathias.", [], ""),
    ("mathias", "Je suis désolé.", "I am sorry.", [], ""),
    ("mathias", "Je regrette tout.", "I regret everything.", [], ""),
    ("mathias", "Pardonne-moi, s'il te plaît.", "Forgive me, please.", [], ""),
    ("mathias", "Je t'en prie.", "I beg you.", [], ""),
    ("mathias", "Rappelle-moi.", "Call me back.", [], ""),
    ("mathias", "Je t'aime, ma fille.", "I love you, my daughter.", [], ""),
    ("mathias", "Au revoir, Camille.", "Goodbye, Camille.", [], "")
]

WALK = [
    (0, None, "'Camille, answer me.' Mathias begs her to pick up the phone."),
    (1, None, "'Please, my darling.' He uses an affectionate term for his daughter."),
    (2, None, "'Camille Valentini, I am not available.' It goes straight to her voicemail."),
    (3, None, "'But please leave a message.' She asks the caller to speak after the beep."),
    (4, None, "'It is me, Mathias.' He starts his message hesitantly."),
    (5, None, "'I am sorry.' He apologises directly to her."),
    (6, None, "'I regret everything.' He wishes he had acted differently with her."),
    (7, None, "'Forgive me, please.' He asks for her forgiveness."),
    (8, None, "'I beg you.' This is a strong expression of pleading."),
    (9, None, "'Call me back.' He gives an instruction using an imperative verb."),
    (10, None, "'I love you, my daughter.' He finally admits his true feelings."),
    (11, None, "'Goodbye, Camille.' He ends the emotional message and hangs up.")
]

LABELS = {
    "lea": "Camille",
    "mathias": "Mathias"
}

CLOSING = ("mathias", "À bientôt.")
