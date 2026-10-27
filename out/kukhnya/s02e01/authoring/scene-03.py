ID = "kukhnya-s02e01-scene-03"
SHOW = "kukhnya"
SEASON = 2
EPISODE = 1
SCENE = 3
TITLE = "Начало смены  (Start of the Shift)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "max": "anja", "senya": "angelina"}
LABELS = {"anya": "Шеф", "max": "Макс", "senya": "Сеня"}
SOURCE_NAME = "Кухня (Kukhnya) S2.01"
SOURCE_FILE = "sources/kukhnya/s02/e01.ru.dual.srt"
SOURCE_NOTE = (
    "Cue 95. After the new owner confiscates his alcohol, a furious Chef Viktor "
    "orders the kitchen crew to start their shift immediately."
)

INTRO = (
    "In the kitchen of Claude Monet, Chef Viktor is furious after the new owner confiscated "
    "all of his alcohol. As the restaurant opens for service, Viktor barks orders at Max and Senya "
    "to begin cooking immediately. Let us listen to their kitchen exchange in Russian first."
)

STORY = [
    ("anya", "Повара, быстро встаньте все на свои места!",
     "Cooks, quickly stand at your places, everyone!",
     [], "new"),
    ("anya", "Сейчас наш ресторан открывает двери для гостей.",
     "Right now our restaurant is opening its doors for guests.",
     [], "new"),
    ("anya", "Приступайте сразу к своей работе на кухне!",
     "Get started immediately with your work in the kitchen!",
     [(95, "Приступайте.")], "adapted"),
    ("senya", "Шеф, почему вы сегодня такой очень злой?",
     "Chef, why are you so very angry today?",
     [], "new"),
    ("anya", "Новый хозяин забрал весь мой дорогой алкоголь!",
     "The new owner took away all my expensive alcohol!",
     [], "new"),
    ("max", "Он действительно запретил вам пить на работе?",
     "Did he really forbid you to drink at work?",
     [], "new"),
    ("anya", "Да, теперь на кухне действует сухой закон.",
     "Yes, now a dry law is in effect in the kitchen.",
     [], "new"),
    ("senya", "Без вина вам будет трудно готовить блюда.",
     "Without wine it will be hard for you to cook dishes.",
     [], "new"),
    ("anya", "Хватит болтать, начинайте резать свежее мясо!",
     "Enough chatting, start cutting the fresh meat!",
     [], "new"),
    ("max", "Я уже приготовил вкусный соус для рыбы.",
     "I already prepared a delicious sauce for the fish.",
     [], "new"),
    ("senya", "А я сейчас поставлю горячий суп на плиту.",
     "And I will now put the hot soup on the stove.",
     [], "new"),
    ("anya", "Сегодня каждое наше блюдо должно быть идеальным.",
     "Today every dish of ours must be ideal.",
     [], "new"),
    ("max", "Хорошо, шеф, мы сделаем всё очень быстро!",
     "Fine, chef, we will do everything very quickly!",
     [], "new"),
]

OPENER = "Now let us examine the start of the kitchen shift line by line."

WALK = [
    (0, None,
     "'Cooks, quickly stand at your places, everyone!' -- Chef Viktor calls the entire kitchen team to attention."),
    (1, None,
     "'Right now our restaurant is opening its doors for guests.' -- He reminds the cooks that customers are arriving."),
    (2, None,
     "'Get started immediately with your work in the kitchen!' -- Viktor gives the sharp command to begin cooking."),
    (3, None,
     "'Chef, why are you so very angry today?' -- Senya notices the head chef's unusually foul mood."),
    (4, None,
     "'The new owner took away all my expensive alcohol!' -- Viktor reveals the reason for his frustration."),
    (5, None,
     "'Did he really forbid you to drink at work?' -- Max asks about the strict new policy."),
    (6, None,
     "'Yes, now a dry law is in effect in the kitchen.' -- Viktor confirms that alcohol is completely banned."),
    (7, None,
     "'Without wine it will be hard for you to cook dishes.' -- Senya jokes about the chef's usual habit."),
    (8, None,
     "'Enough chatting, start cutting the fresh meat!' -- Viktor cuts off the banter and demands focus."),
    (9, None,
     "'I already prepared a delicious sauce for the fish.' -- Max reports that his station is ready."),
    (10, None,
     "'And I will now put the hot soup on the stove.' -- Senya gets back to his own cooking task."),
    (11, None,
     "'Today every dish of ours must be ideal.' -- Viktor insists on perfection to keep the new boss away."),
    (12, None,
     "'Fine, chef, we will do everything very quickly!' -- Max promises fast and disciplined work from the team."),
]

TRANSITION = "Now let us listen to the full kitchen scene once again."
OUTRO = (
    "Despite losing his prized alcohol stash to the new owner, Chef Viktor channels his anger "
    "into strict discipline as the kitchen team begins the busy shift."
)
CLOSING = ("max", "Хорошо, шеф, мы сделаем всё очень быстро!")
