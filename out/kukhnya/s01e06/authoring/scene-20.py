"""s01e06 scene 20: До следующей Пасхи (Until Next Easter)."""

ID = "kukhnya-s01e06-scene-20"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 6
SCENE = 20
TITLE = "До следующей Пасхи  (Until Next Easter)"
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
SOURCE_NAME = "Кухня (Kukhnya) S1.06"
SOURCE_FILE = "sources/kukhnya/s01/e06.ru.dual.srt"

INTRO = (
    "Chef Viktor Barinov grows furious over the delay in preparing the truffle salad for the inspector. "
    "He confronts Max, who desperately stalls for time while trying to recover the missing luxury ingredients. "
    "Listen to their conversation in Russian first, then we will break down each line in English."
)

STORY = [
    ("chef", "Огузок, где мой свежий дорогой трюфель?",
     "Rump, where is my fresh expensive truffle?",
     [(243, "свои трюфель")], "impatient demand"),
    ("chef", "Я буду ждать его до следующей Пасхи?",
     "Am I going to wait for it until next Easter?",
     [(243, "дышащей Пасхи буду ждать")], "sarcastic complaint"),
    ("anya", "Шеф, я уже несу, всё хорошо!",
     "Chef, I am already bringing it, all is well!",
     [(244, "Шеф"), (245, "несу. Все хорошо")], "panicked reassurance"),
    ("chef", "Ты слишком медленно работаешь на кухне!",
     "You work too slowly in the kitchen!",
     [], "criticizing pace"),
    ("chef", "Важный гость ждёт свой заказ.",
     "The important guest is waiting for his order.",
     [], "emphasizing VIP"),
    ("anya", "Я ищу самый лучший гриб.",
     "I am looking for the best mushroom.",
     [], "inventing excuse"),
    ("chef", "У тебя есть ровно одна минута!",
     "You have exactly one minute!",
     [], "strict ultimatum"),
    ("chef", "Иначе я лично тебя уволю сегодня!",
     "Otherwise I will personally fire you today!",
     [], "severe threat"),
    ("anya", "Не переживайте, шеф, заказ будет готов.",
     "Do not worry, chef, the order will be ready.",
     [], "desperate pledge"),
    ("chef", "Я хочу видеть результат прямо сейчас.",
     "I want to see the result right now.",
     [], "demanding delivery"),
    ("anya", "Мы выполнили все ваши сложные условия.",
     "We fulfilled all your difficult conditions.",
     [(246, "Мы выполнили твои условия")], "quoting conditions"),
    ("chef", "Что ты там бормочешь себе под нос?",
     "What are you muttering under your breath there?",
     [], "suspicious reaction"),
    ("anya", "Я говорю, что всё под контролем.",
     "I am saying that everything is under control.",
     [], "covering tracks"),
    ("chef", "Тогда неси трюфель на стол шефа!",
     "Then bring the truffle to the chef table!",
     [], "final order"),
]

OPENER = "Now let us go through each phrase to see how it works in Russian."

WALK = [
    (0, "Огузок, где мой свежий дорогой трюфель?",
     "'Rump, where is my fresh expensive truffle?' Chef Barinov aggressively interrogates his assistant."),
    (1, "Я буду ждать его до следующей Пасхи?",
     "'Am I going to wait for it until next Easter?' A sarcastic complaint about the intolerable delay."),
    (2, "Шеф, я уже несу, всё хорошо!",
     "'Chef, I am already bringing it, all is well!' Max offers empty assurances while trying to solve the problem."),
    (3, "Ты слишком медленно работаешь на кухне!",
     "'You work too slowly in the kitchen!' The head chef scolds the young cook for poor pace."),
    (4, "Важный гость ждёт свой заказ.",
     "'The important guest is waiting for his order.' Barinov stresses that a VIP customer is seated."),
    (5, "Я ищу самый лучший гриб.",
     "'I am looking for the best mushroom.' Max invents a perfectionist excuse for the holdup."),
    (6, "У тебя есть ровно одна минута!",
     "'You have exactly one minute!' A fierce ultimatum issued from the pass."),
    (7, "Иначе я лично тебя уволю сегодня!",
     "'Otherwise I will personally fire you today!' Barinov threatens immediate termination."),
    (8, "Не переживайте, шеф, заказ будет готов.",
     "'Do not worry, chef, the order will be ready.' Max desperately promises that the dish will leave the pass."),
    (9, "Я хочу видеть результат прямо сейчас.",
     "'I want to see the result right now.' Barinov demands immediate tangible proof on the line."),
    (10, "Мы выполнили все ваши сложные условия.",
     "'We fulfilled all your difficult conditions.' Max quotes the harsh demands of the mystery holder."),
    (11, "Что ты там бормочешь себе под нос?",
     "'What are you muttering under your breath there?' The chef catches the suspicious quiet comment."),
    (12, "Я говорю, что всё под контролем.",
     "'I am saying that everything is under control.' Max quickly covers up his slip of the tongue."),
    (13, "Тогда неси трюфель на стол шефа!",
     "'Then bring the truffle to the chef table!' Barinov gives a final directive to deliver the delicacy."),
]

TRANSITION = "Alright, let's hear the whole thing once more."

OUTRO = (
    "Max faces extreme pressure from Chef Barinov to deliver the truffle immediately. "
    "Next time, we will see whether Max manages to get the truffle onto the plate in time. Until then!"
)

CLOSING = ("anya", "Повар отчаянно пытался спасти ситуацию.")
