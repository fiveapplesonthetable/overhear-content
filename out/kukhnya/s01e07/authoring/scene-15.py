"""s01e07 scene 15: Правда отменяется (The Truth Is Canceled)."""

ID = "kukhnya-s01e07-scene-15"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 7
SCENE = 15
TITLE = "Правда отменяется  (The Truth Is Canceled)"
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
SOURCE_NAME = "Кухня (Kukhnya) S1.07"
SOURCE_FILE = "sources/kukhnya/s01/e07.ru.dual.srt"

INTRO = (
    "In the Claude Monet kitchen, Chef Viktor Barinov tastes Max's freshly prepared dish and admits it is delicious. "
    "Max cheekily remarks on the chef's rare smile, prompting Barinov to declare the day of brutal truth officially over before quietly thanking him. "
    "Listen to their conversation in Russian first, then we will break down each line in English."
)

STORY = [
    ("anya", "Шеф, попробуйте, пожалуйста, это горячее блюдо.",
     "Chef, please taste this hot dish.",
     [], "inviting tasting"),
    ("chef", "Давай сюда тарелку, я сейчас попробую.",
     "Give the plate here, I will taste it now.",
     [], "taking plate"),
    ("chef", "Очень вкусно, можно подавать гостям.",
     "Very tasty, we can serve it to the guests.",
     [(313, "Очень вкусно. Можно подавать")], "approving course"),
    ("anya", "Неужели вы говорите мне чистую правду?",
     "Are you really telling me the pure truth?",
     [(312, "Правда")], "shocked disbelief"),
    ("chef", "Да, блюдо получилось действительно великолепным.",
     "Yes, the dish turned out truly magnificent.",
     [], "confirming praise"),
    ("anya", "Шеф, вы сейчас так радостно улыбаетесь!",
     "Chef, you are smiling so joyfully now!",
     [(314, "Не улыбайтесь так")], "noticing smile"),
    ("chef", "А что, повар уже не может улыбнуться?",
     "Why, can a cook no longer smile?",
     [], "defending smile"),
    ("anya", "Не улыбайтесь так, вы похожи на клоуна.",
     "Do not smile like that, you look like a clown.",
     [(314, "вы похожи на бесеного класса")], "cheeky joke"),
    ("chef", "Замолчи сейчас же, наглый огузок!",
     "Be quiet right now, insolent rump!",
     [(315, "Заткнись")], "playful wrath"),
    ("chef", "С этого момента вся правда отменяется!",
     "From this moment on, all truth is canceled!",
     [(316, "с этого момента правда отменяется")], "ending honesty"),
    ("anya", "Я вас понял, возвращаемся к работе.",
     "I understood you, we return to work.",
     [], "accepting order"),
    ("chef", "И ещё одно важное слово, Максим.",
     "And one more important word, Maxim.",
     [(317, "И еще")], "serious pause"),
    ("chef", "Спасибо за отличную работу на кухне.",
     "Thank you for the excellent work in the kitchen.",
     [(318, "Спасибо")], "sincere thanks"),
    ("anya", "Спасибо вам большое, шеф!",
     "Thank you very much, chef!",
     [], "grateful finish"),
]

OPENER = "Now let us go through each phrase to see how it works in Russian."

WALK = [
    (0, "Шеф, попробуйте, пожалуйста, это горячее блюдо.",
     "'Chef, please taste this hot dish.' The nervous cook invites his mentor to sample the food."),
    (1, "Давай сюда тарелку, я сейчас попробую.",
     "'Give the plate here, I will taste it now.' Barinov prepares to evaluate the culinary attempt."),
    (2, "Очень вкусно, можно подавать гостям.",
     "'Very tasty, we can serve it to the guests.' The head chef gives his rare and coveted approval."),
    (3, "Неужели вы говорите мне чистую правду?",
     "'Are you really telling me the pure truth?' Max cannot believe he is receiving genuine praise."),
    (4, "Да, блюдо получилось действительно великолепным.",
     "'Yes, the dish turned out truly magnificent.' Barinov confirms the high quality of the cooking."),
    (5, "Шеф, вы сейчас так радостно улыбаетесь!",
     "'Chef, you are smiling so joyfully now!' Max points out the unusual happiness on Barinov's face."),
    (6, "А что, повар уже не может улыбнуться?",
     "'Why, can a cook no longer smile?' The chef defends his right to show positive emotion."),
    (7, "Не улыбайтесь так, вы похожи на клоуна.",
     "'Do not smile like that, you look like a clown.' Max delivers a cheeky observation about the grin."),
    (8, "Замолчи сейчас же, наглый огузок!",
     "'Be quiet right now, insolent rump!' Barinov snaps back with his familiar kitchen insult."),
    (9, "С этого момента вся правда отменяется!",
     "'From this moment on, all truth is canceled!' The head chef declares the end of brutal honesty."),
    (10, "Я вас понял, возвращаемся к работе.",
     "'I understood you, we return to work.' Max accepts the end of the frank exchange."),
    (11, "И ещё одно важное слово, Максим.",
     "'And one more important word, Maxim.' Barinov calls him by his real name to deliver a message."),
    (12, "Спасибо за отличную работу на кухне.",
     "'Thank you for the excellent work in the kitchen.' A quiet moment of sincere gratitude from the master."),
    (13, "Спасибо вам большое, шеф!",
     "'Thank you very much, chef!' Max warmly thanks his tough mentor for the acknowledgement."),
]

TRANSITION = "Alright, let's hear the whole thing once more."

OUTRO = (
    "In a rare moment of tenderness, Chef Barinov genuinely compliments Max before returning to kitchen discipline. "
    "Next time, we will see how Max solves his housing crisis in Moscow. Until then!"
)

CLOSING = ("anya", "Шеф впервые похвалил молодого повара.")
