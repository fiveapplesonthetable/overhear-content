"""s01e11 scene 30: Судьба выдала сдачу (Fate Gave Change Back)."""

ID = "domashniy-arest-s01e11-scene-30"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 11
SCENE = 30
TITLE = "Судьба выдала сдачу  (Fate Gave Change Back)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "samson": "anja",
}
LABELS = {
    "anya": "Аркадий",
    "samson": "Самсон",
}
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.11"
SOURCE_FILE = "sources/domashniy-arest/s01/e11.ru.dual.srt"
SOURCE_NOTE = "Cue 917. Arkady arrives back at the communal flat penniless, where Samsonov bluntly reminds him that fate has returned his change."

INTRO = (
    "Defeated, empty-handed, and escorted back to the communal flat, Arkady steps into the corridor. "
    "Samsonov meets him by the door, bluntly pointing out that fate has caught up with him. "
    "Let's listen in Russian first."
)

STORY = [
    ("samson", "Ну что, судьба тебе сдачу выдала!",
     "Well then, fate gave you change back!",
     [(917, "Судьба тебе сдачу выдала.")], ""),

    ("anya", "Я не хочу сейчас с тобой спорить.",
     "I do not want to argue with you now.",
     [], ""),

    ("samson", "Ты думал, что легко сбежишь отсюда?",
     "Did you think that you would easily escape from here?",
     [], ""),

    ("anya", "Меня снова вернули в эту старую квартиру.",
     "They returned me to this old apartment again.",
     [], ""),

    ("samson", "Здесь твоё настоящее место, бывший мэр.",
     "Here is your real place, former mayor.",
     [], ""),

    ("anya", "Я потерял абсолютно всё своё богатство.",
     "I lost absolutely all my wealth.",
     [], ""),

    ("samson", "Честный труд всегда лучше любых взяток.",
     "Honest labor is always better than any bribes.",
     [], ""),

    ("anya", "Теперь мне придётся жить по правилам.",
     "Now I will have to live by the rules.",
     [], ""),

    ("samson", "Привыкай жить просто, как все соседи.",
     "Get used to living simply, like all neighbors.",
     [], ""),

    ("anya", "Я готов спокойно дождаться решения суда.",
     "I am ready to wait calmly for the court decision.",
     [], ""),

    ("samson", "Вот это уже умные слова, Аркаша.",
     "Now those are smart words already, Arkasha.",
     [], ""),

    ("anya", "Пожалуйста, оставь меня одного в комнате.",
     "Please leave me alone in the room.",
     [], ""),

    ("samson", "Иди, отдыхай, завтра начнётся новый день.",
     "Go, rest, a new day will begin tomorrow.",
     [], ""),
]

OPENER = (
    "Let's examine the dialogue line by line. Notice the conversational idioms expressing resignation, "
    "moral lessons, and neighbourly banter."
)

WALK = [
    (0, None,
     "'Well then, fate gave you change back!' Colloquial idiom using a past perfective transitive verb to describe poetic justice."),
    (1, None,
     "'I do not want to argue with you now.' First person negative modal verb followed by temporal adverb and reflexive infinitive."),
    (2, None,
     "'Did you think that you would easily escape from here?' Interrogative past verb introducing a subordinate clause with future perfective verb."),
    (3, None,
     "'They returned me to this old apartment again.' Impersonal plural past construction with temporal adverb and accusative direct object."),
    (4, None,
     "'Here is your real place, former mayor.' Locative adverb introducing a descriptive nominative noun phrase with apposition."),
    (5, None,
     "'I lost absolutely all my wealth.' Past transitive verb with emphatic adverb and neuter accusative object phrase."),
    (6, None,
     "'Honest labor is always better than any bribes.' Comparative predicate adjective governing a genitive plural noun phrase."),
    (7, None,
     "'Now I will have to live by the rules.' Impersonal modal construction with dative pronoun and prepositional phrase."),
    (8, None,
     "'Get used to living simply, like all neighbors.' Imperative verb governing an infinitive with manner adverb and comparative phrase."),
    (9, None,
     "'I am ready to wait calmly for the court decision.' Short predicative adjective with adverb and perfective infinitive governing genitive."),
    (10, None,
     "'Now those are smart words already, Arkasha.' Demonstrative particle with qualifying adjective and familiar diminutive address."),
    (11, None,
     "'Please leave me alone in the room.' Courtesy adverb with imperative verb governing masculine accusative adjective and locative phrase."),
    (12, None,
     "'Go, rest, a new day will begin tomorrow.' Two consecutive imperatives followed by future perfective clause with temporal adverb."),
]

TRANSITION = "Now let's listen to Samson's blunt reality check and Arkady's acceptance once more."

OUTRO = (
    "Back in the modest communal flat, Arkady begins to accept that his former life of privilege "
    "is gone. See you next time!"
)

CLOSING = ("samson", "Ну что, судьба тебе сдачу выдала!")
