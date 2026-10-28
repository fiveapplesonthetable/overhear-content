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
    (2, None, "'Maybe if something happened to you.' The reflexive ending on the verb for 'happened' turns the action back onto the subject."),
    (4, None, "'When I was a kid, I had a dog.' The key word here means 'childhood', which Kostya combines with 'me'."),
    (5, None, "'Ralph. And one day he bit me really badly.' — Notice the proper name meaning 'Ralph' paired with the pronoun for 'he'."),
    (6, None, "'I was mad at him for a long time.' A compact expression built around 'I' and 'to take offence'."),
    (8, None, "'Then a car hit him.' Here 'a car' sets up the idea, while 'then' comes at the end for emphasis."),
    (10, None, "'Too bad he didn't appreciate it.' You'll hear 'it is a pity' all the time in the show, here connected with 'to appreciate'."),
    (11, None, "'What, he died?' Max puts 'what' up front so the listener immediately catches the tone, followed by 'died'. Then Kostya replies."),
    (12, None, "'No, of course not. He bit me again.' In Russian, 'of course' leads into 'bit' in a very natural everyday phrasing."),
    (15, None, "'Better a live, angry dog than no dog at all.' ENG: The adjective means angry or mean, and the last word means none at all.")
]

INTRO = "Kostya tells Max that he could only forgive someone if misfortune struck them, recalling a childhood story about his angry dog Ralph whom he forgave immediately after the dog was hit by a car."
OPENER = "Continuing their conversation, Kostya explains his stance on forgiveness."
TRANSITION = "Kostya shares a somewhat tragic story from his childhood to illustrate his point."
OUTRO = "The bizarre story from Kostya leaves Max feeling even more confused than before."
PAIR = "ru-en"
ID = "kukhnya-s02e01-scene-12"
CLOSING = STORY[-1][:2]
