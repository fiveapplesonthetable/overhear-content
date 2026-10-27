"""s01e09 scene 07: Опасный нож (A Dangerous Knife)."""

ID = "kukhnya-s01e09-scene-07"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 9
SCENE = 7
TITLE = "Опасный нож  (A Dangerous Knife)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "max": "anja"}
LABELS = {"anya": "Шеф", "max": "Макс"}
SOURCE_NAME = "Кухня (Kukhnya) S1.09"
SOURCE_FILE = "sources/kukhnya/s01/e09.ru.dual.srt"
SOURCE_NOTE = "Cues 179-185. In the kitchen, Max retrieves Chef Barinov's favorite knife from Barinov's young daughter Alisa, who has been running around the kitchen."

INTRO = (
    "In the busy kitchen of Claude Monet, Max finally retrieves Chef Viktor Barinov's favorite knife from Barinov's mischievous young daughter Alisa. "
    "Max complains that the little girl almost injured him, but Chef Barinov dismisses his drama and tells him to get back to work. "
    "Let's listen to their sharp exchange in Russian first."
)

STORY = [
    ("max", "Шеф, я наконец забрал ваш любимый нож.",
     "Chef, I finally retrieved your favorite knife.",
     [(179, "мой нож")], "retrieving the sharp knife"),
    ("anya", "Где ты вообще его нашёл, огузок?",
     "Where did you find it at all, Oguzok?",
     [(180, "Шеф, еще бы несколько секунд")], "asking about the location"),
    ("max", "Ваша дочка играла с ним на кухне!",
     "Your daughter was playing with it in the kitchen!",
     [(180, "и я мог бы пострадать от вашей дочери")], "explaining the dangerous situation"),
    ("anya", "Она могла поранить себя или тебя?",
     "Could she hurt herself or you?",
     [], "inquiring about potential harm"),
    ("max", "Она чуть не ранила меня этим ножом!",
     "She almost injured me with this knife!",
     [], "complaining about the close call"),
    ("anya", "Ничего страшного, ты всё ещё жив.",
     "Nothing terrible, you are still alive.",
     [(181, "Узнал бы, пришел бы попозже")], "downplaying the injury risk"),
    ("max", "Мне нужно продолжать готовить блюда?",
     "Do I need to continue preparing dishes?",
     [], "asking about his duties"),
    ("anya", "Хватит болтать, живо иди работать!",
     "Stop chattering, go work immediately!",
     [(182, "Работай")], "ordering him to return to work"),
    ("max", "А что вы будете делать с дочкой?",
     "And what will you do with your daughter?",
     [(183, "Алиса, что мне с тобой делать")], "asking about little Alisa"),
    ("anya", "Алиса, что мне теперь делать с тобой?",
     "Alice, what am I to do with you now?",
     [(183, "Алиса, что мне с тобой делать")], "wondering how to manage the child"),
    ("max", "Она снова убежит в обеденный зал.",
     "She will run off to the dining hall again.",
     [(184, "ты снова куда-нибудь сбежишь")], "predicting another escape"),
    ("anya", "Ладно, я отведу её к тёте Вике!",
     "All right, I will take her to Aunt Vika!",
     [(185, "Ладно")], "finding a quick solution"),
]

OPENER = "Let's examine how Chef Barinov and Max resolve the situation with the missing knife line by line."

WALK = [
    (0, None,
     "'Chef, I finally retrieved your favorite knife.' Max reports recovering the missing kitchen tool to his boss."),
    (1, None,
     "'Where did you find it at all, Oguzok?' Barinov demands an explanation using his customary dismissive nickname for Max."),
    (2, None,
     "'Your daughter was playing with it in the kitchen!' Max explains the dangerous situation with a past tense imperfective verb."),
    (3, None,
     "'Could she hurt herself or you?' The chef asks whether anyone suffered real harm during the encounter."),
    (4, None,
     "'She almost injured me with this knife!' Max emphasizes the narrow escape using the particle meaning almost and an instrumental noun."),
    (5, None,
     "'Nothing terrible, you are still alive.' Barinov brushes off Max's panic with a common reassuring phrase."),
    (6, None,
     "'Do I need to continue preparing dishes?' Max clarifies his immediate assignment using a modal predicative with an infinitive."),
    (7, None,
     "'Stop chattering, go work immediately!' The chef barks a firm command to resume cooking without unnecessary delays."),
    (8, None,
     "'And what will you do with your daughter?' Max wonders how the chef plans to handle the mischievous child."),
    (9, None,
     "'Alice, what am I to do with you now?' Barinov addresses his daughter with an affectionate yet exasperated question."),
    (10, None,
     "'She will run off to the dining hall again.' Max warns that the little girl will wander into the guest area."),
    (11, None,
     "'All right, I will take her to Aunt Vika!' The chef decides to hand over care of the child to the restaurant director."),
]

TRANSITION = "Now let's listen to the whole dialogue again at normal conversational speed."

OUTRO = (
    "Now you know how to talk about kitchen safety, handling sharp tools, and managing energetic children in Russian. "
    "See you next time!"
)

CLOSING = ("anya", "Ладно, я отведу её к тёте Вике!")
