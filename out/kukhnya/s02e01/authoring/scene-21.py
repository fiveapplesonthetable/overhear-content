ID = "kukhnya-s02e01-scene-21"
SHOW = "kukhnya"
SEASON = 2
EPISODE = 1
SCENE = 21
TITLE = "Короткий разговор  (Brief Exchange)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "vika": "anja", "kostya": "angelina"}
LABELS = {"anya": "Макс", "vika": "Вика", "kostya": "Костя"}
SOURCE_NAME = "Кухня (Kukhnya) S2.01"
SOURCE_FILE = "sources/kukhnya/s02/e01.ru.dual.srt"

INTRO = "Max's dangerous stunt goes horribly wrong when he accidentally slips. He finds himself actually hanging and cries out for help. Let's listen closely to their exchange in Russian first, and then walk through each line together."

STORY = [
 ("anya", "Я хочу, чтобы ты знала.", "I want you to know.", [(248, "Я хочу, чтобы ты знала, я люблю тебя.")], ''),
 ("anya", "Я люблю тебя.", "I love you.", [(248, "Я хочу, чтобы ты знала, я люблю тебя.")], ''),
 ("vika", "Прекрати.", "Stop it.", [], 'new'),
 ("vika", "Ты хочешь вешаться?", "Do you want to hang yourself?", [], 'new'),
 ("vika", "Мне все равно.", "I don't care.", [], 'new'),
 ("anya", "Постой.", "Wait.", [(247, "Постой.")], ''),
 ("anya", "Я не шучу.", "I am not joking.", [], 'new'),
 ("anya", "Помоги!", "Help!", [(249, "Помоги!")], ''),
 ("kostya", "Что вы наделали, Виктория?", "What have you done, Victoria?", [(250, "Что"), (251, "же вы надеяли, Виктория Сергеевна?")], ''),
 ("kostya", "Вы убили его.", "You killed him.", [(251, "же вы надеяли, Виктория Сергеевна?")], ''),
 ("vika", "Костя, помоги ему!", "Kostya, help him!", [(254, "Костя, помоги!")], ''),
 ("kostya", "Ты реально повесился?", "Did you really hang yourself?", [(256, "Ты что, реально повесился?")], ''),
]

OPENER = "Let's listen to their conversation."

WALK = [
 (0, "Я хочу, чтобы ты знала.", "'I want you to know.' ENG Max makes his final dramatic statement."),
 (1, "Я люблю тебя.", "'I love you.' ENG He declares his true feelings."),
 (2, None, "'Stop it.' ENG Vika is not impressed by his act."),
 (3, "Ты хочешь вешаться?", "'Do you want to hang yourself?' ENG She calls his bluff."),
 (4, "Мне все равно.", "'I don't care.' ENG She shows zero sympathy."),
 (5, "Постой.", "'Wait.' ENG Max panics as he slips."),
 (6, None, "'I am not joking.' ENG He realizes he is in actual danger."),
 (7, "Помоги!", "'Help!' ENG He is genuinely choking now."),
 (8, "Что вы наделали, Виктория?", "'What have you done, Victoria?' ENG Kostya blames her for the accident."),
 (9, None, "'You killed him.' ENG Kostya exaggerates the situation."),
 (10, "Костя, помоги ему!", "'Kostya, help him!' ENG Vika finally realizes it is not a joke."),
 (11, None, "'Did you really hang yourself?' ENG Kostya is shocked by Max's foolishness."),
]

TRANSITION = "Now let's hear the whole thing once more."

OUTRO = "That wraps up this scene."
CLOSING = ("anya", "Помоги!")
