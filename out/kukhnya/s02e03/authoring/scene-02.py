ID = "kukhnya-s02e03-scene-02"
SHOW = "kukhnya"
SEASON = 2
EPISODE = 3
SCENE = 2
TITLE = "Авария на улице  (Crash on the Street)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "chef": "anja"}
LABELS = {"anya": "Елена", "chef": "Шеф"}
SOURCE_NAME = "Кухня (Kukhnya) S2.03"
SOURCE_FILE = "sources/kukhnya/s02/e03.ru.dual.srt"

INTRO = "Elena accidentally hits someone with her car. She rushes out to check on the victim and realizes it is her rival, Chef Viktor. Let's listen closely to their exchange in Russian first, and then walk through each line together."

STORY = [
 ("anya", "Виктор Петрович, вы живы?", "Viktor Petrovich, are you alive?", [(8, "Виктор Петрович, вы живы, Виктор Петрович?")], ''),
 ("chef", "А?", "Huh?", [(9, "А?")], ''),
 ("anya", "Ой, вы простите меня.", "Oh, please forgive me.", [(10, "Ой."), (11, "Вы простите меня, ради бога, я вас просто не заметила.")], ''),
 ("anya", "Ради бога, простите.", "For God's sake, forgive me.", [(11, "Вы простите меня, ради бога")], ''),
 ("anya", "Я вас просто не заметила.", "I just didn't see you.", [(11, "я вас просто не заметила.")], ''),
 ("chef", "Так вы расправляетесь с конкурентами.", "So this is how you deal with the competition.", [(12, "Так-то вы расправляетесь с конкурентами.")], ''),
 ("anya", "Дайте, я вас приподниму.", "Here, let me help you up.", [(13, "Дайте, я вас как-то приподниму")], ''),
 ("anya", "Поедем в больницу.", "We will go to the hospital.", [(13, "и в больницу.")], ''),
 ("chef", "Мне больно.", "It hurts.", [], 'new'),
 ("anya", "Надо ехать к врачу.", "We need to go to the doctor.", [], 'new'),
 ("chef", "Ладно, поехали.", "All right, let's go.", [], 'new'),
 ("anya", "Осторожно.", "Careful.", [], 'new'),
]

OPENER = "Let's listen to their conversation."

WALK = [
 (0, "Виктор Петрович, вы живы?", "'Viktor Petrovich, are you alive?' ENG She is shocked and worried."),
 (1, "А?", "'Huh?' ENG He is dazed and confused."),
 (2, "Ой, вы простите меня.", "'Oh, please forgive me.' ENG She apologizes profusely."),
 (3, None, "'For God's sake, forgive me.' ENG She is very sorry."),
 (4, "Я вас просто не заметила.", "'I just didn't see you.' ENG She explains her mistake."),
 (5, "Так вы расправляетесь с конкурентами.", "'So this is how you deal with the competition.' ENG He jokes despite the pain."),
 (6, "Дайте, я вас приподниму.", "'Here, let me help you up.' ENG She tries to assist him."),
 (7, None, "'We will go to the hospital.' ENG She wants to get him medical help."),
 (8, "Мне больно.", "'It hurts.' ENG He complains about his injuries."),
 (9, "Надо ехать к врачу.", "'We need to go to the doctor.' ENG She insists on medical attention."),
 (10, "Ладно, поехали.", "'All right, let's go.' ENG He agrees to go with her."),
 (11, None, "'Careful.' ENG She helps him gently."),
]

TRANSITION = "Now let's hear the whole thing once more."

OUTRO = "That wraps up this scene."
CLOSING = ("anya", "Осторожно.")
