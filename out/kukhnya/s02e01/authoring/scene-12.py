SHOW = "kukhnya"
SEASON = 2
EPISODE = 1
SCENE = 12
TITLE = "История про пса  (The Story About the Dog)"
LEVEL = "A1 — Duolingo Section 2"
SOURCE_NAME = "Кухня (Kukhnya) S2.01"
SOURCE_FILE = "sources/kukhnya/s02/e01.ru.dual.srt"
LABELS = {"anya": "Макс", "kostya": "Костя"}
VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "kostya": "anja"
}
STORY = [
    ('anya', 'Никогда?', 'Never?', [], ''),
    ('kostya', 'Не знаю.', "I don't know.", [], ''),
    ('kostya', 'Может, только если бы с тобой что-нибудь случилось.', 'Maybe if something happened to you.', [], ''),
    ('anya', 'В смысле?', 'What do you mean?', [], ''),
    ('kostya', 'В детстве у меня был пёс.', 'When I was a kid, I had a dog.', [], ''),
    ('kostya', 'Ральф. И он меня однажды очень сильно покусал.', 'Ralph. And one day he bit me really badly.', [], ''),
    ('kostya', 'Я на него очень долго обижался.', 'I was mad at him for a long time.', [], ''),
    ('anya', 'И чё?', 'So what?', [], ''),
    ('kostya', 'Машина его сбила потом.', 'Then a car hit him.', [], ''),
    ('kostya', 'Я его простил.', 'I forgave him.', [], ''),
    ('anya', 'Жаль, только он этого не оценил.', "Too bad he didn't appreciate it.", [], ''),
    ('anya', 'Что, умер?', 'What, he died?', [], ''),
    ('kostya', 'Нет, конечно, он опять меня покусал.', 'No, of course not. He bit me again.', [], ''),
    ('kostya', 'Только я уже не обижался.', "Only I wasn't mad anymore.", [], ''),
    ('kostya', 'Потому что я понял...', 'Because I understood...', [], ''),
    ('kostya', 'Лучше живой и злой пес, чем никакого.', 'Better a live, angry dog than no dog at all.', [], '')
]
WALK = [
    (2, None, "'Maybe if something happened to you.' ENG: The last word means happened."),
    (4, None, "'When I was a kid, I had a dog.' ENG: The first phrase means in childhood, and the last word is another word for dog."),
    (5, None, "'Ralph. And one day he bit me really badly.' -- The speaker responds in the scene."),
    (6, None, "'I was mad at him for a long time.' ENG: The verb means took offense or was angry."),
    (8, None, "'Then a car hit him.' ENG: The verb means hit or knocked down, often used for vehicle accidents."),
    (10, None, "'Too bad he didn't appreciate it.' ENG: The first word means it is a pity, and the verb means appreciated."),
    (11, None, "'What, he died?' ENG: The verb means died."),
    (12, None, "'No, of course not. He bit me again.' ENG: The word means of course, and the adverb means again."),
    (15, None, "'Better a live, angry dog than no dog at all.' ENG: The adjective means angry or mean, and the last word means none at all.")
]

INTRO = "Kostya tells Max that he could only forgive someone if misfortune struck them, recalling a childhood story about his angry dog Ralph whom he forgave immediately after the dog was hit by a car."
OPENER = "Continuing their conversation, Kostya explains his stance on forgiveness."
TRANSITION = "Kostya shares a somewhat tragic story from his childhood to illustrate his point."
OUTRO = "The bizarre story from Kostya leaves Max feeling even more confused than before."
PAIR = "ru-en"
ID = "kukhnya-s02e01-scene-12"
CLOSING = STORY[-1][:2]
