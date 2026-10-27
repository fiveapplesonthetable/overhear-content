ID = "kukhnya-s01e17-scene-11"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 17
SCENE = 11
TITLE = "День рождения Макса  (Max's Birthday)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "kostya": "anja"}
LABELS = {"anya": "Макс", "kostya": "Костя"}
SOURCE_NAME = "Кухня (Kukhnya) S1.17"
SOURCE_FILE = "sources/kukhnya/s01/e17.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 135-144. Looking for a way to reconcile his feuding friends and his girlfriend Sasha, Max suddenly "
    "remembers that tomorrow is his birthday, though he worries nobody will believe a last-minute invitation."
)

INTRO = (
    "Caught in the middle of a bitter quarrel between his friends and his girlfriend Sasha, Max searches for a way to bring everyone back together. "
    "He suddenly realizes that tomorrow is his own birthday, which could be the perfect excuse for peace. "
    "Let's listen to their conversation in Russian first."
)

STORY = [
    ("anya", "Что делать, если друзья и девушка поссорились?",
     "What to do if friends and girlfriend quarreled?",
     [(135, "если твои друзья и твоя девушка поссорились")], "adapted"),
    ("kostya", "Понятно, что их надо быстро помирить.",
     "Clearly, one must reconcile them quickly.",
     [(136, "Понятно, что их нужно как-то помирить")], "adapted"),
    ("anya", "Но как мне это сделать сегодня?",
     "But how can I do this today?",
     [(137, "Но как?")], "adapted"),
    ("kostya", "Нужен хороший повод для общего праздника.",
     "A good reason for a shared holiday is needed.",
     [], "new"),
    ("anya", "Например, весёлый день рождения!",
     "For example, a cheerful birthday!",
     [(138, "Например, день рождения")], "adapted"),
    ("kostya", "В такой день все должны забыть обиды.",
     "On such a day everyone must forget grudges.",
     [(139, "Все должны забыть свои обиды")], "adapted"),
    ("anya", "Точно! У меня завтра день рождения!",
     "Exactly! Tomorrow is my birthday!",
     [(140, "Точно! У меня же завтра день рождения")], "adapted"),
    ("anya", "Как я сам мог об этом забыть?",
     "How could I forget about this myself?",
     [(141, "Как я мог забыть")], "adapted"),
    ("kostya", "Серьёзно, как ты мог забыть свой праздник?",
     "Seriously, how could you forget your holiday?",
     [(142, "как я мог забыть")], "adapted"),
    ("anya", "Я никому ничего не говорил раньше.",
     "I did not tell anyone anything before.",
     [(143, "Ничего не говорил")], "adapted"),
    ("kostya", "А тут вдруг завтра день рождения.",
     "And then suddenly tomorrow is your birthday.",
     [(143, "день рождения")], "adapted"),
    ("anya", "Они мне просто так не поверят.",
     "They will not believe me just like that.",
     [(144, "Не поверят")], "adapted"),
    ("kostya", "Значит, тебе надо придумать хитрый план.",
     "That means you need to invent a clever plan.",
     [], "new"),
]

OPENER = "Now let's examine this conversation line by line."

WALK = [
    (0, None,
     "'What to do if friends and girlfriend quarreled?' -- Max ponders his difficult social dilemma."),
    (1, None,
     "'Clearly, one must reconcile them quickly.' -- Kostya points out the obvious goal."),
    (2, None,
     "'But how can I do this today?' -- Max wonders what could possibly bring both sides together."),
    (3, None,
     "'A good reason for a shared holiday is needed.' -- Kostya suggests an event that nobody can skip."),
    (4, None,
     "'For example, a cheerful birthday!' -- Max hits upon the idea of a birthday celebration."),
    (5, None,
     "'On such a day everyone must forget grudges.' -- Guests have to be polite to avoid upsetting the host."),
    (6, None,
     "'Exactly! Tomorrow is my birthday!' -- Max suddenly remembers the date on the calendar."),
    (7, None,
     "'How could I forget about this myself?' -- He is amazed that his own birthday slipped his mind."),
    (8, None,
     "'Seriously, how could you forget your holiday?' -- Kostya laughs at his friend's forgetfulness."),
    (9, None,
     "'I did not tell anyone anything before.' -- Max realizes he never mentioned it all week."),
    (10, None,
     "'And then suddenly tomorrow is your birthday.' -- Announcing it now will look like a trick."),
    (11, None,
     "'They will not believe me just like that.' -- Max knows his friends will suspect a trap."),
    (12, None,
     "'That means you need to invent a clever plan.' -- Kostya encourages him to find a smart workaround."),
]

TRANSITION = "Now let's listen to the conversation again without interruption."
OUTRO = (
    "Realizing that nobody will believe a direct announcement, Max comes up with a sly scheme "
    "to make Sasha spread the news about his birthday for him."
)
CLOSING = ("anya", "Я уже всё придумал!")
