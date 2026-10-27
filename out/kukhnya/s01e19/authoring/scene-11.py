ID = "kukhnya-s01e19-scene-11"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 19
SCENE = 11
TITLE = "Шпионаж у бара  (Espionage at the Bar)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "kostya": "anja"}
LABELS = {"anya": "Макс", "kostya": "Костя"}
SOURCE_NAME = "Кухня (Kukhnya) S1.19"
SOURCE_FILE = "sources/kukhnya/s01/e19.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 213-218. Kostya reports back to Max about Victoria's conversation with the client, "
    "revealing that they are leaving together for a business meeting."
)

INTRO = (
    "Returning to the bar after clearing glasses near Victoria's table, Kostya reports his findings to Max. "
    "Learning that Victoria is about to depart with the wealthy stranger, Max becomes increasingly agitated. "
    "Let's listen to their conversation in Russian first."
)

OPENER = "Now let's examine the conversation line by line."

STORY = [
    ("kostya", "Макс, я всё услышал.",
     "Max, I heard everything.",
     [], "new"),
    ("anya", "Что она ему сказала, Костя?",
     "What did she tell him, Kostya?",
     [], "new"),
    ("kostya", "Она говорит спасибо за красивые цветы.",
     "She says thank you for the beautiful flowers.",
     [(213, "Она говорит спасибо за цветы.")], "adapted"),
    ("anya", "Вот оно как, а он что?",
     "Is that so, and what about him?",
     [(214, "А, вот оно как. А он что?")], "adapted"),
    ("kostya", "Он говорит о важной деловой встрече.",
     "He speaks about an important business meeting.",
     [(215, "Он говорит о какой-то встрече")], "adapted"),
    ("anya", "О какой встрече он говорит?",
     "What meeting is he talking about?",
     [], "new"),
    ("kostya", "Он сказал, что скоро надо ехать.",
     "He said they need to leave soon.",
     [(215, "что скоро надо ехать.")], "adapted"),
    ("anya", "Значит, у неё сейчас деловая встреча.",
     "So she has a business meeting now.",
     [(216, "А, деловая встреча у нее, значит.")], "adapted"),
    ("kostya", "Вика сказала, что она уже свободна.",
     "Vika said that she is already free.",
     [(217, "А она говорит, что уже освободилась")], "adapted"),
    ("anya", "Она правда собирается поехать с ним?",
     "Is she really going to go with him?",
     [], "new"),
    ("kostya", "Да, она уже готова ехать.",
     "Yes, she is already ready to leave.",
     [(217, "и готова ехать.")], "adapted"),
    ("anya", "Я не позволю им уехать вдвоём.",
     "I will not allow them to leave together.",
     [(218, "Ага, сейчас.")], "adapted"),
    ("kostya", "Макс, не делай никаких глупостей сегодня.",
     "Max, do not do any foolish things today.",
     [], "new"),
]

WALK = [
    (0, None,
     "'Max, I heard everything.' -- Kostya returns to the counter with information."),
    (1, None,
     "'What did she tell him, Kostya?' -- Max immediately asks for the details."),
    (2, None,
     "'She says thank you for the beautiful flowers.' -- The bartender shares Victoria's polite words of gratitude."),
    (3, None,
     "'Is that so, and what about him?' -- Max presses for the man's side of the conversation."),
    (4, None,
     "'He speaks about an important business meeting.' -- Kostya explains the nature of their upcoming plan."),
    (5, None,
     "'What meeting is he talking about?' -- The suspicious cook wants more specific facts."),
    (6, None,
     "'He said they need to leave soon.' -- Kostya relays the client's urgent reminder."),
    (7, None,
     "'So she has a business meeting now.' -- Max pieces together the timeline of her departure."),
    (8, None,
     "'Vika said that she is already free.' -- The bartender reveals that Victoria agreed to accompany him."),
    (9, None,
     "'Is she really going to go with him?' -- Max cannot believe she is leaving during work hours."),
    (10, None,
     "'Yes, she is already ready to leave.' -- Kostya confirms that the pair are packing up."),
    (11, None,
     "'I will not allow them to leave together.' -- The jealous cook resolves to intervene immediately."),
    (12, None,
     "'Max, do not do any foolish things today.' -- Kostya pleads with him to stay out of trouble."),
]

TRANSITION = "Now let's listen to the bar discussion once again without interruption."

OUTRO = (
    "Ignoring Kostya's sensible advice, Max slips away from the bar and heads toward the parking lot, "
    "determined to confront Victoria before she can leave."
)

CLOSING = ("kostya", "Макс, не делай никаких глупостей сегодня.")
