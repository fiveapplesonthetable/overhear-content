"""s01e05 scene 20: Просьба о помощи (A Request for Help)."""

ID = "kukhnya-s01e05-scene-20"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 5
SCENE = 20
TITLE = "Просьба о помощи  (A Request for Help)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "fedya": "anja",
}
LABELS = {
    "anya": "Макс",
    "fedya": "Федя",
}
SOURCE_NAME = "Кухня (Kukhnya) S1.05"
SOURCE_FILE = "sources/kukhnya/s01/e05.ru.dual.srt"

INTRO = (
    "Swamped with dinner orders, Max swallows his pride and asks fish cook Fedya for help on the line. "
    "Fedya seizes the chance to tease the rookie, demanding a loud and completely sincere public apology before the whole kitchen crew. "
    "Listen to their conversation in Russian first, then we will break down each line in English."
)

STORY = [
    ("anya", "Федя, пожалуйста, помоги мне с заказами.",
     "Fedya, please help me with the orders.",
     [(292, "Слушай, Федь, извини"), (294, "Помоги с заказами")], "reluctant request"),
    ("fedya", "Что ты говоришь? Я плохо слышу.",
     "What are you saying? I hear poorly.",
     [(295, "Что? Извини, говорю")], "pretending deafness"),
    ("anya", "Я говорю, что прошу прощения.",
     "I am saying that I ask for forgiveness.",
     [(293, "Я зря себя так вывел")], "reiterating plea"),
    ("fedya", "Коллеги, можно потише на кухне, пожалуйста?",
     "Colleagues, could you be quieter in the kitchen, please?",
     [(296, "Коллеги! Можно потише чуть-чуть, пожалуйста")], "calling room"),
    ("fedya", "Макс хочет сказать нам важные слова.",
     "Max wants to tell us important words.",
     [(297, "человек что-то важное сказать хочет")], "dramatic setup"),
    ("anya", "Федя, извини меня за всё.",
     "Fedya, forgive me for everything.",
     [(298, "Федя, извини")], "public apology"),
    ("anya", "Ты отличный опытный повар, а я нет.",
     "You are an excellent experienced cook, and I am not.",
     [(299, "Ты прекрасный повар, а я нет")], "flattering master"),
    ("anya", "Помоги мне быстро приготовить эти блюда.",
     "Help me quickly prepare these dishes.",
     [(300, "Помоги мне, пожалуйста, с заказами")], "begging speed"),
    ("fedya", "Я всё очень хорошо услышал.",
     "I heard everything very well.",
     [(301, "Понятно")], "acknowledging receipt"),
    ("fedya", "Но я тебе совсем не верю.",
     "But I do not believe you at all.",
     [(302, "Но не верю")], "feigned disbelief"),
    ("fedya", "В твоих словах нет настоящей искренности.",
     "In your words there is no real sincerity.",
     [(303, "Ну, искренности не хватает")], "demanding emotion"),
    ("fedya", "Давай повтори всё ещё разок громче!",
     "Come on, repeat everything once more louder!",
     [(304, "Давай еще разок")], "pressing advantage"),
    ("anya", "Я больше не буду ничего повторять!",
     "I will not repeat anything anymore!",
     [(305, "Да пошел ты")], "refusing humiliation"),
    ("fedya", "Ладно, успокойся, я сейчас помогу.",
     "Alright, calm down, I will help now.",
     [(306, "Ладно, аппендикс"), (307, "Подвинься давай")], "relenting support"),
]

OPENER = "Now let us go through each phrase to see how it works in Russian."

WALK = [
    (0, "Федя, пожалуйста, помоги мне с заказами.",
     "'Fedya, please help me with the orders.' Max desperately turns to his kitchen colleague."),
    (1, "Что ты говоришь? Я плохо слышу.",
     "'What are you saying? I hear poorly.' Fedya pretends to struggle to hear the quiet plea."),
    (2, "Я говорю, что прошу прощения.",
     "'I am saying that I ask for forgiveness.' Max reiterates his reluctant apology."),
    (3, "Коллеги, можно потише на кухне, пожалуйста?",
     "'Colleagues, could you be quieter in the kitchen, please?' Fedya commands the attention of the whole line."),
    (4, "Макс хочет сказать нам важные слова.",
     "'Max wants to tell us important words.' The line cook dramatically sets the stage for a spectacle."),
    (5, "Федя, извини меня за всё.",
     "'Fedya, forgive me for everything.' Max swallows his pride and offers an open apology."),
    (6, "Ты отличный опытный повар, а я нет.",
     "'You are an excellent experienced cook, and I am not.' The rookie acknowledges the veteran chef's superiority."),
    (7, "Помоги мне быстро приготовить эти блюда.",
     "'Help me quickly prepare these dishes.' Max urgently begs for assistance with the tickets."),
    (8, "Я всё очень хорошо услышал.",
     "'I heard everything very well.' Fedya acknowledges receiving the humble speech."),
    (9, "Но я тебе совсем не верю.",
     "'But I do not believe you at all.' The teasing cook feigns complete skepticism."),
    (10, "В твоих словах нет настоящей искренности.",
     "'In your words there is no real sincerity.' Fedya demands a much more convincing delivery."),
    (11, "Давай повтори всё ещё разок громче!",
     "'Come on, repeat everything once more louder!' The cook urges him to perform the confession again."),
    (12, "Я больше не буду ничего повторять!",
     "'I will not repeat anything anymore!' Max furiously refuses to be humiliated any further."),
    (13, "Ладно, успокойся, я сейчас помогу.",
     "'Alright, calm down, I will help now.' Fedya relents with a smile and steps in to assist."),
]

TRANSITION = "Alright, let's hear the whole thing once more."

OUTRO = (
    "After enjoying a moment of playful authority, Fedya steps in to save Max from the rush. "
    "Next time, we will see whether the kitchen crew manages to serve all the orders on time. Until then!"
)

CLOSING = ("anya", "Повар согласился помочь молодому коллеге.")
