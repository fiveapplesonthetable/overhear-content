SHOW = "kukhnya"
SEASON = 2
EPISODE = 1
SCENE = 11
TITLE = "Строгий друг  (A Strict Friend)"
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
    ('anya', 'Представляешь, она даже слушать не стала.', "Can you believe it? She wouldn't even listen.", [], ''),
    ('kostya', 'Я бы тоже не стал.', "I wouldn't either.", [], ''),
    ('anya', 'В смысле?', 'What do you mean?', [], ''),
    ('anya', 'Ты за кого? За Вику или за друга?', "Whose side are you on? Vika's or your friend's?", [], ''),
    ('kostya', 'Конечно, за друга.', "Of course, my friend's.", [], ''),
    ('kostya', 'Но это не отменяет того, что ты козел.', "But that doesn't change the fact you're a bastard.", [], ''),
    ('anya', 'Пилите, Костя, пилите.', 'Keep at it, Kostya, keep at it.', [], ''),
    ('anya', 'То есть если бы я тебе изменил...', 'So if I cheated on you...', [], ''),
    ('anya', 'ты бы меня не простил?', "you wouldn't forgive me?", [], ''),
    ('kostya', 'Костян, это не то, что ты думаешь.', "Kostyan, it's not what you think.", [], ''),
    ('kostya', 'Мы с ним вовсе не друзья.', "We're not even friends.", [], ''),
    ('anya', 'Ты мой друг.', "You're my friend.", [], ''),
    ('kostya', 'Не простил бы.', "I wouldn't forgive you.", [], '')
]
WALK = [
    (0, None, "'Can you believe it? She wouldn't even listen.' — Notice the verb meaning 'can you imagine, believe' paired with the pronoun for 'it (the pipe)'."),
    (1, None, "'I wouldn't either.' ENG: The second word means also or too, and the last words mean would not start."),
    (2, None, "'What do you mean?' ENG: The phrase translates to in what sense and is a common way to ask what someone means."),
    (3, None, "'Whose side are you on? Vika's or your friend's?' ENG: The first phrase means who are you for, asking which side they are taking."),
    (5, None, "'But that doesn't change the fact you're a bastard.' ENG: The phrase means does not cancel, and the word for goat is used as an insult."),
    (6, None, "'Keep at it, Kostya, keep at it.' ENG: The first word literally means saw as in cutting wood but colloquially means nag."),
    (7, None, "'So if I cheated on you...' ENG: The first phrase means that is, and the verb means cheated or betrayed."),
    (8, None, "'you wouldn't forgive me?' ENG: The verb means would not forgive."),
    (9, None, "'Kostyan, it's not what you think.' ENG: The name is an affectionate form of his name."),
    (10, None, "'We're not even friends.' ENG: The adverb adds emphasis, meaning at all or not even.")
]

INTRO = "Max complains to Kostya that Vika refuses to listen to his apologies. Kostya bluntly tells Max that he is to blame for his own mistake and admits that he would never forgive a betrayal either."
OPENER = "In the dining room, Max expresses his frustration to his friend Kostya."
TRANSITION = "Kostya surprises Max by taking Vika's side in the argument."
OUTRO = "Max is shocked by Kostya's unexpected response to his situation."
PAIR = "ru-en"
ID = "kukhnya-s02e01-scene-11"
CLOSING = STORY[-1][:2]
