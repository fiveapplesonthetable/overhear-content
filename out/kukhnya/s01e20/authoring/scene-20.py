ID = "kukhnya-s01e20-scene-20"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 20
SCENE = 20
TITLE = "Утро  (Morning)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "anton": "anja", "max": "angelina"}
LABELS = {"anya": "Аня", "anton": "Антон", "max": "Макс"}
SOURCE_NAME = "Кухня (Kukhnya) S1.20"
SOURCE_FILE = "sources/kukhnya/s01/e20.ru.dual.srt"

INTRO = "This is the final episode of the first season of Kukhnya, and everything is about to change. Elena comes to the apartment where Max and the Chef live early in the morning."

STORY = [
 ("anya", "Здрасте.", "Hello.", [(330, "Здрасте")], ''),
 ("anya", "Доброе утро.", "Good morning.", [(330, "Доброе утро")], ''),
 ("anya", "Это Макс?", "Is this Max?", [], 'new'),
 ("anton", "Да, это я.", "Yes, it is me.", [], 'new'),
 ("anya", "Я ищу его.", "I am looking for him.", [], 'new'),
 ("anya", "Дома не могу ему дозвониться.", "At home I can't reach him.", [(331, "дома не могу ему дозвониться")], ''),
 ("anya", "Где он?", "Where is he?", [], 'new'),
 ("anton", "Я не знаю.", "I don't know.", [(332, "Не знаю")], ''),
 ("anton", "Наверное, ключи висят.", "Probably, the keys are hanging.", [(332, "Наверное, ключи висят")], ''),
 ("anton", "Значит, он дома.", "So, he is home.", [(332, "значит, дома")], ''),
 ("anton", "Вы хотите войти?", "Do you want to come in?", [], 'new'),
 ("anton", "Проходите.", "Come in.", [(333, "Проходите")], ''),
]

OPENER = "Let's listen to their conversation."

WALK = [
 (0, None, "'Hello.' A simple greeting to start the day."),
 (1, "Доброе утро.", "'Good morning.' She is polite but worried."),
 (2, None, "'Is this Max?' She wants to make sure she is talking to the right person."),
 (3, None, "'Yes, it is me.' He confirms his identity."),
 (4, None, "'I am looking for him.' She means the Chef."),
 (5, "Дома не могу ему дозвониться.", "'At home I can't reach him.' She tried calling but there was no answer."),
 (6, None, "'Where is he?' She is getting impatient."),
 (7, "Я не знаю.", "'I don't know.' He is genuinely confused."),
 (8, "Наверное, ключи висят.", "'Probably, the keys are hanging.' He notices the keys on the wall."),
 (9, "Значит, он дома.", "'So, he is home.' A logical conclusion."),
 (10, None, "'Do you want to come in?' He offers her to enter."),
 (11, "Проходите.", "'Come in.' He steps aside to let her pass."),
]

TRANSITION = "Now let's hear the whole thing once more."

OUTRO = "That wraps up this scene."
CLOSING = ("anya", "До свидания!")
