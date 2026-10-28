"""s01e08 scene 28: Порядок на кухне (Order in the Kitchen)."""

ID = "kukhnya-s01e08-scene-28"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 8
SCENE = 28
TITLE = "Порядок на кухне  (Order in the Kitchen)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "chef": "anja",
}
LABELS = {
    "anya": "Елена",
    "chef": "Шеф",
}
SOURCE_NAME = "Кухня (Kukhnya) S1.08"
SOURCE_FILE = "sources/kukhnya/s01/e08.ru.dual.srt"

INTRO = (
    "In the Claude Monet kitchen, temporary chef Elena is overwhelmed as orders back up and customers return dishes. "
    "Chef Barinov suddenly arrives and calmly restores order within seconds by addressing each cook's individual habits. "
    "Listen to their conversation in Russian first, then we will break down each line in English."
)

STORY = [
    ("anya", "У нас уже три возврата блюд!",
     "We already have three returned dishes!",
     [(324, "три отката от блюд.")], "despairing over kitchen"),
    ("anya", "Повара ничего не успевают вовремя отдавать.",
     "The cooks cannot serve anything on time.",
     [(325, "Вы ничего не успеваете вовремя подавать.")], "panicking at delay"),
    ("chef", "Елена Павловна, что здесь случилось?",
     "Elena Pavlovna, what happened here?",
     [(327, "Елена Павловна, что случилось?")], "stepping in calmly"),
    ("anya", "Шеф, я совсем не справляюсь.",
     "Chef, I am not coping at all.",
     [(328, "Ну, в общем...")], "admitting defeat"),
    ("chef", "Спокойно, сейчас я наведу порядок.",
     "Calm down, now I will restore order.",
     [], "taking charge"),
    ("chef", "Федя, иди покури три минуты.",
     "Fedya, go have a smoke for three minutes.",
     [(330, "Федя, иди покури, у тебя три минуты.")], "managing Fedya"),
    ("chef", "Ему нужен перекур каждые полтора часа.",
     "He needs a smoke break every hour and a half.",
     [(331, "Ему надо давать перекур каждые полтора часа.")], "explaining cook habit"),
    ("chef", "Сеня, переходи готовить мясо.",
     "Senya, switch to preparing meat.",
     [(332, "Сеня, переходи на мясо.")], "reassigning station"),
    ("chef", "Он совершенно не умеет готовить птицу.",
     "He does not know how to cook poultry at all.",
     [(334, "Он не может готовить птицу.")], "explaining limitation"),
    ("chef", "Луи, позвони другу на две минуты.",
     "Louis, call your friend for two minutes.",
     [(339, "Пара минут трепа по телефону, и он в норме.")], "handling pastry chef"),
    ("anya", "А почему Мазар ничего не делает?",
     "And why is Mazar doing nothing?",
     [(340, "А это почему не справляется?")], "pointing out slacker"),
    ("chef", "Потому что он никогда ничего не умеет.",
     "Because he never knows how to do anything.",
     [(341, "А это вообще никогда не справляется.")], "dismissing slacker"),
    ("chef", "Мазар, ты уволен!",
     "Mazar, you are fired!",
     [(342, "Мазар, ты уволен.")], "firing worker"),
    ("chef", "Вот теперь кухня работает идеально.",
     "Now the kitchen works perfectly.",
     [(343, "Что и требовалось доказать.")], "triumphant conclusion"),
]

OPENER = "Let us practice the key lines together."

WALK = [
    (0, "У нас уже три возврата блюд!",
     "'We already have three returned dishes!' — expressing a count of noun returns in genitive plural."),
    (1, "Повара ничего не успевают вовремя отдавать.",
     "'The cooks cannot serve anything on time.' — negative indefinite pronoun with an adverbial infinitive."),
    (2, "Елена Павловна, что здесь случилось?",
     "'Elena Pavlovna, what happened here?' — addressing a person with polite name and patronymic."),
    (3, "Шеф, я совсем не справляюсь.",
     "'Chef, I am not coping at all.' — an admission of difficulty using an emphatic negative particle."),
    (4, "Спокойно, сейчас я наведу порядок.",
     "'Calm down, now I will restore order.' — an adverb of reassurance followed by a future perfective promise."),
    (5, "Федя, иди покури три минуты.",
     "'Fedya, go have a smoke for three minutes.' — informal imperative giving a time duration."),
    (6, "Ему нужен перекур каждые полтора часа.",
     "'He needs a smoke break every hour and a half.' — dative construction of necessity with a time expression."),
    (7, "Сеня, переходи готовить мясо.",
     "'Senya, switch to preparing meat.' — imperative followed by an infinitive specifying a new station."),
    (8, "Он совершенно не умеет готовить птицу.",
     "'He does not know how to cook poultry at all.' — stating inability using an intensifying adverb."),
    (9, "Луи, позвони другу на две минуты.",
     "'Louis, call your friend for two minutes.' — imperative directed at a specific team member."),
    (11, "Потому что он никогда ничего не умеет.",
     "'Because he never knows how to do anything.' — double negation highlighting permanent incompetence."),
    (12, "Мазар, ты уволен!",
     "'Mazar, you are fired!' — a short decisive dismissal in the short passive form."),
    (13, "Вот теперь кухня работает идеально.",
     "'Now the kitchen works perfectly.' — pointing particle and temporal adverb declaring success."),
]

TRANSITION = "Now listen to the full conversation once more."
OUTRO = "And that's it for this scene. When you watch the episode, listen out for the exchange around order in the kitchen, and for the words meaning 'returns' and 'dishes'. You'll catch them now. See you next time."
CLOSING = ("chef", "Вот теперь кухня работает идеально.")
