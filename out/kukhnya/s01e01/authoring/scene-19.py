"""s01e01 scene 19: Настоящий профессионал (A True Professional)."""

ID = "kukhnya-s01e01-scene-19"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 1
SCENE = 19
TITLE = "Настоящий профессионал  (A True Professional)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "chef": "anja",
}
LABELS = {
    "anya": "Макс",
    "chef": "Шеф",
}
SOURCE_NAME = "Кухня (Kukhnya) S1.01"
SOURCE_FILE = "sources/kukhnya/s01/e01.ru.dual.srt"

INTRO = (
    "In the busy restaurant Claude Monet, the fiery Chef commands everyone back to work. "
    "Max has just arrived in kitchen whites, eager to prove that he is a professional cook. "
    "As always, listen to the story first, and then we will break it down together in English."
)

STORY = [
    ("chef", "Все за работу, быстро!",
     "Everyone get to work, quickly!",
     [(168, "все за работу")], "verbatim order"),
    ("chef", "А ты иди переодевайся!",
     "And you, go get changed!",
     [(171, "Иди переодевайся")], "verbatim order"),
    ("anya", "Шеф, я готов. Что мне делать?",
     "Chef, I am ready. What should I do?",
     [(174, "Шеф, я готов"), (175, "Что мне делать")], "verbatim"),
    ("chef", "Почему ты пришёл на эту кухню?",
     "Why did you come to this kitchen?",
     [(179, "Чего тебе на кухню понесло")], "adapted to standard A1 Russian"),
    ("anya", "Потому что я повар. Я настоящий профессионал.",
     "Because I am a cook. I am a true professional.",
     [(180, "потому что я повар"), (181, "Я профессионал")], "verbatim"),
    ("chef", "Профессионал? Иди сюда.",
     "A professional? Come here.",
     [(183, "Профессионал"), (183, "Иди сюда")], "verbatim"),
    ("chef", "Посмотри вокруг на моих поваров.",
     "Look around at my cooks.",
     [(184, "Вон, видишь")], "adapted for A1 context"),
    ("chef", "Что ты сам умеешь делать?",
     "What can you do yourself?",
     [(194, "А ты что можешь")], "verbatim question"),
    ("anya", "Я очень хорошо умею готовить.",
     "I can cook very well.",
     [(195, "Я готовить умею")], "expanded for A1 practice"),
    ("chef", "Да ну? Всем внимание на кухне!",
     "Really? Attention everyone in the kitchen!",
     [(196, "Да ну"), (197, "Внимание")], "verbatim"),
    ("chef", "К нам пришёл великий повар!",
     "A great cook has come to us!",
     [(199, "человек, который умеет готовить")], "sarcastic praise adapted for A1"),
    ("chef", "Мы так долго ждали его!",
     "We waited for him for so long!",
     [(200, "Мы пять лет ждали его"), (201, "Он пришел")], "simplified time reference"),
    ("anya", "Какая у меня будет работа?",
     "What work will I have?",
     [(203, "Есть работа")], "adapted inquiry"),
    ("chef", "Для тебя есть особенная работа!",
     "There is a special job for you!",
     [(203, "Есть работа"), (204, "Только тебе")], "verbatim setup"),
]

OPENER = "Now let us go through each line together to understand every word."

WALK = [
    (0, "Все за работу, быстро!",
     "'Everyone get to work, quickly!' The chef calls everybody to order with a sharp command."),
    (1, "А ты иди переодевайся!",
     "'And you, go get changed!' He uses the informal imperative to order Max to change into kitchen whites."),
    (2, "Шеф, я готов.",
     "'Chef, I am ready.' Max addresses the boss with the standard kitchen title and short adjective."),
    (2, "Что мне делать?",
     "'What should I do?' The infinitive construction asks what action is expected of him."),
    (3, "Почему ты пришёл на эту кухню?",
     "'Why did you come to this kitchen?' The past-tense verb indicates arrival at the location."),
    (4, "Потому что я повар.",
     "'Because I am a cook.' Max explains his background with the direct conjunction."),
    (4, "Я настоящий профессионал.",
     "'I am a true professional.' He proudly asserts his culinary qualifications."),
    (5, "Профессионал?",
     "'A professional?' The chef repeats the noun with skeptical astonishment."),
    (5, "Иди сюда.",
     "'Come here.' A direct order to approach and listen carefully."),
    (6, "Посмотри вокруг на моих поваров.",
     "'Look around at my cooks.' The preposition governs the genitive plural of the crew."),
    (7, "Что ты сам умеешь делать?",
     "'What can you do yourself?' The verb asks about his personal skills and abilities."),
    (8, "Я очень хорошо умею готовить.",
     "'I can cook very well.' Max insists on his primary talent in the kitchen."),
    (9, "Да ну?",
     "'Really?' An everyday conversational marker expressing mild sarcasm or disbelief."),
    (9, "Всем внимание на кухне!",
     "'Attention everyone in the kitchen!' The chef sarcastically addresses the whole team."),
    (10, "К нам пришёл великий повар!",
     "'A great cook has come to us!' Sarcastic praise echoing through the prep room."),
    (11, "Мы так долго ждали его!",
     "'We waited for him for so long!' The past tense underlines his theatrical mockery."),
    (12, "Какая у меня будет работа?",
     "'What work will I have?' Max asks about his very first kitchen assignment."),
    (13, "Для тебя есть особенная работа!",
     "'There is a special job for you!' The chef prepares to give him a humiliating chore."),
]

TRANSITION = "Alright, let's hear the whole thing once more."

OUTRO = (
    "Max is confident and eager to cook, but Chef Viktor Barinov has a very different first task in mind. "
    "Next time, we will see what this special assignment actually is. Until then, keep practicing!"
)

CLOSING = ("anya", "Я готов к любой работе.")
