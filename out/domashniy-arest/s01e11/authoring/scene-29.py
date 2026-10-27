"""s01e11 scene 29: Элементарный развод (A Simple Setup)."""

ID = "domashniy-arest-s01e11-scene-29"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 11
SCENE = 29
TITLE = "Элементарный развод  (A Simple Setup)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "pasha": "anja",
}
LABELS = {
    "anya": "Аркадий",
    "pasha": "Паша",
}
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.11"
SOURCE_FILE = "sources/domashniy-arest/s01/e11.ru.dual.srt"
SOURCE_NOTE = "Cues 838-851. Pasha confronts Arkady with the money bags, revealing the entire escape plan was a calculated trap."

INTRO = (
    "Just as Arkady prepares to flee with the bags of cash, his former deputy Pasha intercepts him. "
    "With cold arrogance, Pasha reveals that the entire plan was an elementary trap orchestrated to strip "
    "Arkady of his remaining fortune. Let's listen in Russian first."
)

STORY = [
    ("pasha", "Это элементарный развод, дорогой Аркашенька!",
     "This is an elementary setup, dear Arkashenka!",
     [(838, "Развод, Аркашенька, элементарный развод.")], ""),

    ("anya", "Ты всё это подстроил заранее?",
     "Did you set all this up in advance?",
     [], ""),

    ("pasha", "Как же ты этого не просëк?",
     "How did you not figure this out?",
     [(839, "Как же ты со своей знаменитой чуйкой-то это не просек?")], ""),

    ("pasha", "Не тот ты стал, совсем не тот!",
     "You are not the same man, not at all!",
     [(840, "Не тот ты стал, совсем же не тот, да?")], ""),

    ("anya", "Мы же заключили честный договор.",
     "We made an honest agreement after all.",
     [(845, "У нас договор.")], ""),

    ("pasha", "Твои миллионы теперь останутся у меня.",
     "Your millions will now stay with me.",
     [(846, "Миллион сразу.")], ""),

    ("anya", "Отдай мне хотя бы мою долю.",
     "Give me at least my share.",
     [], ""),

    ("pasha", "Ты больше не получишь ни рубля.",
     "You will not get another single ruble.",
     [], ""),

    ("anya", "Я могу сейчас же вызвать полицию.",
     "I can call the police right now.",
     [(848, "Я все равно ментам могу сообщить")], ""),

    ("pasha", "У тебя нет никаких доказательств против меня.",
     "You have no proof whatsoever against me.",
     [(849, "А где доказательства?")], ""),

    ("anya", "Ты ответишь за это подлое предательство.",
     "You will answer for this vile betrayal.",
     [], ""),

    ("pasha", "Пора возвращаться в твою тесную коммуналку.",
     "Time to return to your cramped communal flat.",
     [(851, "пора тебе уже возвращаться в свой уютный")], ""),

    ("anya", "Я никогда не прощу тебе этот обман.",
     "I will never forgive you for this deception.",
     [], ""),

    ("pasha", "Привыкай к своей новой скромной жизни.",
     "Get used to your new modest life.",
     [], ""),
]

OPENER = (
    "Let's examine the dialogue line by line. Notice the expressions used to describe betrayals, "
    "broken agreements, and bitter confrontations."
)

WALK = [
    (0, None,
     "'This is an elementary setup, dear Arkashenka!' A mocking announcement using a diminutive name and descriptive predicate adjective."),
    (1, None,
     "'Did you set all this up in advance?' Interrogative question with perfective past verb and temporal adverb."),
    (2, None,
     "'How did you not figure this out?' Colloquial exclamatory negative question criticizing Arkady's lack of intuition."),
    (3, None,
     "'You are not the same man, not at all!' Contrastive predicate construction emphasizing Arkady's diminished standing."),
    (4, None,
     "'We made an honest agreement after all.' Emphatic particle with perfective past transitive verb and descriptive object."),
    (5, None,
     "'Your millions will now stay with me.' Possessive subject phrase with future perfective verb and locative prepositional pronoun."),
    (6, None,
     "'Give me at least my share.' Imperative verb governing a restrictive particle and accusative direct object."),
    (7, None,
     "'You will not get another single ruble.' Negative future construction with intensifying negative particle and genitive noun."),
    (8, None,
     "'I can call the police right now.' Present modal verb with temporal adverb phrase and infinitive governing an accusative object."),
    (9, None,
     "'You have no proof whatsoever against me.' Negative existential construction with genitive noun and prepositional pronoun."),
    (10, None,
     "'You will answer for this vile betrayal.' Future perfective verb with prepositional phrase indicating the grounds of responsibility."),
    (11, None,
     "'Time to return to your cramped communal flat.' Predicative word with reflexive infinitive and prepositional destination phrase."),
    (12, None,
     "'I will never forgive you for this deception.' Negative future transitive verb with temporal adverb, dative pronoun, and accusative object."),
    (13, None,
     "'Get used to your new modest life.' Imperative verb governing a prepositional dative object phrase."),
]

TRANSITION = "Now let's listen to Pasha's harsh revelation and Arkady's indignation once more."

OUTRO = (
    "Stripped of his money and his illusions, Arkady is forced to accept total defeat and return to "
    "confinement. See you next time!"
)

CLOSING = ("pasha", "Это элементарный развод, дорогой Аркашенька!")
