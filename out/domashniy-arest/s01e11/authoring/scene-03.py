ID = "domashniy-arest-s01e11-scene-03"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 11
SCENE = 3
TITLE = "Согласие Нины  (Nina Says Yes)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "samson": "anja"}
LABELS = {"anya": "Нина", "samson": "Самсон"}
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.11"
SOURCE_FILE = "sources/domashniy-arest/s01/e11.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 54-55. After seeing Samson's persistence, Nina finally relents and accepts his proposal. "
    "They embrace and head into the registry office together."
)

INTRO = (
    "In this concluding scene of the nineteen-nineties flashback, Samson continues to wait patiently for Nina. "
    "Moved by his stubborn dedication, Nina steps back outside to talk to him once more. "
    "When Ivan asks her one last time if her answer might be yes, Nina smiles and accepts his proposal. "
    "Let's listen to their conversation in Russian first."
)

STORY = [
    ("samson", "Нина, ты вернулась ко мне назад?",
     "Nina, did you come back to me?",
     [], "transition from previous scene"),
    ("anya", "Ты всё ещё стоишь на холоде.",
     "You are still standing in the cold.",
     [], ""),
    ("samson", "Я же обещал, что буду ждать.",
     "I promised that I would wait.",
     [], ""),
    ("anya", "Ты действительно совершенно неисправимый человек.",
     "You are truly a completely incorrigible person.",
     [], ""),
    ("samson", "Так может быть, всё-таки да?",
     "So maybe after all it is yes?",
     [(54, "так может все-таки да")], ""),
    ("anya", "Ну хорошо, может быть и да!",
     "Well alright, maybe it is yes!",
     [(55, "Может и да")], ""),
    ("samson", "Ты правда согласна стать моей женой?",
     "Are you truly willing to become my wife?",
     [], ""),
    ("anya", "Да, я согласна выйти за тебя.",
     "Yes, I agree to marry you.",
     [], ""),
    ("samson", "Тогда надевай скорее это кольцо!",
     "Then put on this ring quickly!",
     [], ""),
    ("anya", "Оно действительно очень красивое и блестит.",
     "It really is very beautiful and shines.",
     [], ""),
    ("samson", "Теперь мы вместе пойдём в ЗАГС.",
     "Now we will go to the registry office together.",
     [], ""),
    ("anya", "И подадим наше первое общее заявление.",
     "And submit our first joint application.",
     [], ""),
    ("samson", "Я обещаю быть самым лучшим мужем!",
     "I promise to be the very best husband!",
     [], ""),
]

OPENER = "Now let's examine Nina's decision to accept Samson's proposal line by line."

WALK = [
    (0, None,
     "'Nina, did you come back to me?' Samson greets her return with an affectionate past verb."),
    (1, None,
     "'You are still standing in the cold.' Nina observes his enduring patience using a prepositional noun."),
    (2, None,
     "'I promised that I would wait.' Samson recalls his pledge with an emphatic particle and a subordinate clause."),
    (3, None,
     "'You are truly a completely incorrigible person.' Nina affectionately teases his stubborn nature."),
    (4, None,
     "'So maybe after all it is yes?' Samson asks the decisive question using conversational particles."),
    (5, None,
     "'Well alright, maybe it is yes!' Nina gives her consent with an optimistic modal phrase."),
    (6, None,
     "'Are you truly willing to become my wife?' Samson confirms the joyful news with an instrumental predicate noun."),
    (7, None,
     "'Yes, I agree to marry you.' Nina accepts using the standard idiom for a woman marrying a man."),
    (8, None,
     "'Then put on this ring quickly!' Samson urges her to accept the token with an imperative verb."),
    (9, None,
     "'It really is very beautiful and shines.' Nina admires the ring with present descriptive verbs and adverbs."),
    (10, None,
     "'Now we will go to the registry office together.' Samson plans the immediate next step with a future verb."),
    (11, None,
     "'And submit our first joint application.' Nina looks forward to formalizing their marriage."),
    (12, None,
     "'I promise to be the very best husband!' Samson makes an earnest vow using a superlative adjective phrase."),
]

TRANSITION = "Now let's listen to their reconciliation once more without pause."
OUTRO = (
    "Nina accepts Ivan's proposal, marking the beginning of their long and tumultuous marriage. "
    "Next comes the opening credits and the satirical theme song."
)
CLOSING = ("samson", "Я обещаю быть самым лучшим мужем!")
