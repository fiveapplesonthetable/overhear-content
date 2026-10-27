"""s01e01 scene 23: Объективная оценка (An Objective Opinion)."""

ID = "kukhnya-s01e01-scene-23"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 1
SCENE = 23
TITLE = "Объективная оценка  (An Objective Opinion)"
LEVEL = "beginner"
PAIR = "ru-en"
VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "max": "anja",
    "kostya": "angelina",
}
LABELS = {
    "anya": "Вика",
    "max": "Макс",
    "kostya": "Костя",
}
SOURCE_NAME = "Кухня, Сезон 1, Эпизод 1"
SOURCE_FILE = "sources/kukhnya/s01/e01.ru.dual.srt"
SOURCE_NOTE = "Cues 307-317. Max plates an intricate dish while Kostya warns him that the chef will ignore it."

INTRO = (
    "In the bustling kitchen of Claude Monet, new recruit Max proudly plates an intricate dish. "
    "Barman Kostya warns him that the temperamental head chef Viktor Barinov will never appreciate his efforts, "
    "prompting Max to seek an objective taster before dining room manager Vika suddenly sweeps in."
)

STORY = [
    ("kostya", "Здорово у тебя всё получается, Макс!",
     "You are doing great at everything, Max!",
     [(307, "Здорово у тебя получается")], "adapted cue"),

    ("kostya", "Жалко только, что шеф этого не оценит.",
     "Too bad only that the chef won't appreciate this.",
     [(308, "Жалко только, что он этого не оценит")], "adapted cue"),

    ("max", "Но это мы с тобой ещё посмотрим.",
     "We will see about that yet.",
     [(309, "Но это мы еще посмотрим")], "adapted cue"),

    ("kostya", "Да он даже пробовать не станет!",
     "Why, he won't even taste it!",
     [(309, "Да он даже не попробует")], "adapted cue"),

    ("kostya", "А если попробует, ему не понравится.",
     "And if he tastes it, he won't like it.",
     [(310, "А если попробует, ему все равно не понравится")], "adapted cue"),

    ("kostya", "Я очень хорошо знаю нашего шефа.",
     "I know our chef very well.",
     [(311, "Я его знаю")], "adapted cue"),

    ("max", "Погоди, нам нужна более объективная оценка.",
     "Wait, we need a more objective opinion.",
     [(312, "Погоди"), (313, "Тогда нам нужна более объективная оценка")], "adapted cue"),

    ("max", "Пусть кто-нибудь другой сначала попробует.",
     "Let someone else taste it first.",
     [(314, "И")], "adapted cue"),

    ("anya", "Сколько можно ждать горячее блюдо?",
     "How long must one wait for the hot dish?",
     [(316, "Сколько можно ждать?")], "adapted cue"),

    ("anya", "Всё приходится делать самой на этой кухне.",
     "One has to do everything herself in this kitchen.",
     [(316, "Все приходится самой делать")], "adapted cue"),

    ("max", "Я сейчас сам отнесу в зал.",
     "I will carry it to the hall myself right now.",
     [(317, "Я отнесу")], "adapted cue"),

    ("anya", "Отойди в сторону и иди работай!",
     "Step aside and go back to work!",
     [(317, "Иди работай")], "adapted cue"),

    ("max", "Это блюдо сделано по всем правилам.",
     "This dish is made according to all rules.",
     [], "Max defending his culinary work"),

    ("anya", "Клиенты давно ждут свой вкусный ужин.",
     "The clients have been waiting for their delicious dinner for a long time.",
     [], "Vika hurrying to the dining room"),
]

OPENER = "Let's see how Max prepares his special dish in the restaurant kitchen."

WALK = [
    (0, None,
     "'You are doing great at everything, Max!' Kostya praises the rookie's culinary skill."),
    (1, None,
     "'Too bad only that the chef won't appreciate this.' Predicting Viktor Barinov's dismissive reaction."),
    (2, None,
     "'We will see about that yet.' Max stubbornly refuses to give up hope."),
    (3, None,
     "'Why, he won't even taste it!' Warning that the chef ignores novices completely."),
    (4, None,
     "'And if he tastes it, he won't like it.' Describing Viktor's notoriously impossible standards."),
    (5, None,
     "'I know our chef very well.' Kostya speaks from long experience behind the bar."),
    (6, None,
     "'Wait, we need a more objective opinion.' Max proposes an impartial test."),
    (7, None,
     "'Let someone else taste it first.' Seeking neutral feedback from kitchen staff."),
    (8, None,
     "'How long must one wait for the hot dish?' Vika arrives demanding the delayed order."),
    (9, None,
     "'One has to do everything herself in this kitchen.' Complaining about the kitchen's chronic delays."),
    (10, None,
     "'I will carry it to the hall myself right now.' Max attempts to serve his creation directly."),
    (11, None,
     "'Step aside and go back to work!' Vika dismissively asserts administrative control."),
    (12, None,
     "'This dish is made according to all rules.' Defending the culinary craftsmanship of his plating."),
    (13, None,
     "'The clients have been waiting for their delicious dinner for a long time.' Prioritizing dining room hospitality over kitchen debates."),
]

TRANSITION = "Now let's listen to the heated exchange in the kitchen once more."

OUTRO = "Vika takes the plate to the dining room while Max and Kostya exchange nervous glances."

CLOSING = ("anya", "Клиенты давно ждут свой вкусный ужин.")
