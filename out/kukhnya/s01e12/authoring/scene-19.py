"""s01e12 scene 19: Отчёт разведчика (The Scout's Report)."""

ID = "kukhnya-s01e12-scene-19"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 12
SCENE = 19
TITLE = "Отчёт разведчика  (The Scout's Report)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "fedya": "anja",
}
LABELS = {
    "anya": "Шеф",
    "fedya": "Федя",
}
SOURCE_NAME = "Кухня (Kukhnya) S1.12"
SOURCE_FILE = "sources/kukhnya/s01/e12.ru.dual.srt"

INTRO = (
    "In the kitchen back room of Claude Monet, cook Fedya returns from scouting out their new rival restaurant. "
    "Relieved to hear that the competitor is empty and quiet, Chef Viktor happily concludes that Claude Monet does not need any changes to stay on top. "
    "Listen to their conversation in Russian first, then we will break down each line in English."
)

STORY = [
    ("anya", "Федя, ну что там у конкурентов?",
     "Fedya, well, how are things at the competitors'?",
     [(256, "Ну что?")], "asking for debrief"),
    ("fedya", "Шеф, наш разведчик вернулся с отчётом.",
     "Chef, our scout has returned with a report.",
     [(255, "Здрасте. Штирец.")], "reporting in"),
    ("anya", "Рассказывай быстрее. Ты заходил внутрь?",
     "Tell me faster. Did you go inside?",
     [(260, "Давай рожай быстрее.")], "pressing for details"),
    ("fedya", "Да, я посмотрел их новый зал.",
     "Yes, I looked at their new hall.",
     [], "confirming inspection"),
    ("anya", "И как? Интерьер выглядит красиво?",
     "And how is it? Does the interior look nice?",
     [], "asking about decor"),
    ("fedya", "Честно говоря, интерьер так себе.",
     "To tell the truth, the interior is so-so.",
     [(261, "Ну, интерьер так себе.")], "dismissing decor"),
    ("anya", "А что происходит с гостями?",
     "And what is going on with the guests?",
     [(258, "Я тебя про ресторан спрашиваю.")], "asking about crowd"),
    ("fedya", "В зале тишина, свободных мест полно.",
     "In the hall there is silence, plenty of empty seats.",
     [(262, "В зале штиль. Свободных мест полно.")], "reporting empty hall"),
    ("anya", "Ты видишь, о чём я говорил!",
     "You see what I was talking about!",
     [(263, "Ты о чём я говорил, а?")], "triumphing"),
    ("anya", "Нам пока ничего не нужно менять.",
     "We do not need to change anything yet.",
     [(264, "Рано нам меняться."), (265, "Ничего нам пока менять не надо.")], "confirming strategy"),
    ("fedya", "Шеф, а можно мне поесть?",
     "Chef, can I have something to eat?",
     [], "asking for reward"),
    ("anya", "Иди на кухню, заслужил горячий обед.",
     "Go to the kitchen, you earned a hot lunch.",
     [(267, "Иди, Федь, на кухню. Подхарчи.")], "sending to eat"),
    ("fedya", "Спасибо, шеф, я очень голодный!",
     "Thank you, Chef, I am very hungry!",
     [], "thanking happily"),
]

OPENER = "Let us practice the key lines together."

WALK = [
    (0, "Федя, ну что там у конкурентов?",
     "'Fedya, well, how are things at the competitors'?' — informal inquiry governing a genitive prepositional phrase."),
    (1, "Шеф, наш разведчик вернулся с отчётом.",
     "'Chef, our scout has returned with a report.' — past perfective verb with an instrumental modifier."),
    (2, "Рассказывай быстрее. Ты заходил внутрь?",
     "'Tell me faster. Did you go inside?' — imperative followed by a past motion verb with an adverb of place."),
    (3, "Да, я посмотрел их новый зал.",
     "'Yes, I looked at their new hall.' — past transitive verb governing an accusative direct object phrase."),
    (5, "Честно говоря, интерьер так себе.",
     "'To tell the truth, the interior is so-so.' — conversational parenthetical phrase with an idiomatic qualifier."),
    (7, "В зале тишина, свободных мест полно.",
     "'In the hall there is silence, plenty of empty seats.' — prepositional location with a predicative quantity word."),
    (8, "Ты видишь, о чём я говорил!",
     "'You see what I was talking about!' — present verb governing a prepositional relative pronoun clause."),
    (9, "Нам пока ничего не нужно менять.",
     "'We do not need to change anything yet.' — impersonal dative construction with a double negative and infinitive."),
    (11, "Иди на кухню, заслужил горячий обед.",
     "'Go to the kitchen, you earned a hot lunch.' — imperative of motion paired with an approving past verb."),
    (12, "Спасибо, шеф, я очень голодный!",
     "'Thank you, Chef, I am very hungry!' — polite expression of thanks followed by a predicate adjective."),
]

TRANSITION = "Now listen to the full conversation once more."
OUTRO = "Great job! Keep practicing these lively dialogues with us to master everyday Russian."
CLOSING = ("fedya", "Спасибо, шеф, я очень голодный!")
