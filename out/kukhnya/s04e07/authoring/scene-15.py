ID = "kukhnya-s04e07-scene-15"
SHOW = "kukhnya"
SEASON = 4
EPISODE = 7
SCENE = 15
TITLE = "Секретный ингредиент Сени  (Senya's Secret Ingredient)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "senya": "anja", "fedya": "angelina"}
LABELS = {"anya": "Шеф", "senya": "Сеня", "fedya": "Федя"}
SOURCE_NAME = "Кухня (Kukhnya) S4.07"
SOURCE_FILE = "sources/kukhnya/s04/e07.ru.srt"
SOURCE_NOTE = "Cues 230-241. Fedya distracts German and Barinov so Senya can secretly spoon sugar into the onion soup to neutralize the vinegar, and the guest praises Barinov's main course."

INTRO = "With German watching the pass counter like a hawk, Senya asks Fedya to create a distraction so he can stir sugar into the sour onion soup. While Gavril Ilyich praises Barinov's dishes in the dining room, Barinov turns around and catches Senya holding a bowl of sugar by the soup!"

STORY = [
    ("senya", "Федя, а ты можешь их немного отвлечь?", "Fedya, can you distract them for a moment?", [(230, "Федь, а ты можешь их отвлечь, а?")], "adapted"),
    ("senya", "А я пока незаметно насыплю туда сахара!", "And meanwhile I will unnoticeably pour some sugar in there!", [(231, "А я пока не заветно сахара сыпану.")], "adapted"),
    ("fedya", "Да как же я тебе их отвлеку?", "Just how am I supposed to distract them for you?", [(232, "Да? Как? Голым по залу пробежать?")], "adapted"),
    ("fedya", "Ладно, давай сюда, сейчас я их отвлеку!", "Fine, give it here, I will distract them right now!", [(233, "Я отвлеку."), (234, "Держи.")], "adapted"),
    ("anya", "Приятного аппетита, попробуйте наше новое горячее блюдо!", "Enjoy your meal, taste our new hot dish!", [(235, "Приятного аппетита.")], "adapted"),
    ("fedya", "Гость сказал, что это совсем другое дело!", "The guest said that this is a completely different matter!", [(237, "Конечно, другое дело.")], "adapted"),
    ("fedya", "В каждом кусочке сразу видна рука мастера!", "In every bite the hand of a master is immediately visible!", [(238, "Видна рука мастера.")], "adapted"),
    ("anya", "Я бы сказал, что работал двумя руками!", "I would say that I worked with both hands!", [(239, "Я бы сказал, двумя руками работал.")], "adapted"),
    ("anya", "Сеня, что ты сейчас делаешь возле супа?", "Senya, what are you doing near the soup right now?", [(240, "оказаться тут, Сеня?")], "adapted"),
    ("senya", "А я подумал, вдруг вам нужен сахар?", "And I thought, what if you need sugar?", [(241, "А я подумал, вдруг он сахар нужен.")], "adapted"),
    ("anya", "Зачем мне сахар в горячем луковом супе?", "What do I need sugar for in hot onion soup?", [], "new"),
    ("senya", "Простите, Шеф, я уже ухожу на место!", "Forgive me, Chef, I am already going back to my station!", [], "new"),
]

OPENER = "Let's break down Senya's secret rescue of the onion soup line by line."

WALK = [
    (0, None, "'Fedya, can you distract them for a moment?' Perfective infinitive 'to distract' takes the accusative pronoun 'them'."),
    (1, None, "'And meanwhile I will unnoticeably pour some sugar in there!' Partitive genitive 'of sugar' follows the verb of pouring."),
    (2, None, "'Just how am I supposed to distract them for you?' Perfective future expresses wondering how to accomplish the task."),
    (3, None, "'Fine, give it here, I will distract them right now!' Fedya steps up to block German's line of sight."),
    (4, None, "'Enjoy your meal, taste our new hot dish!' Out in the dining room, the partridge course is served."),
    (5, None, "'The guest said that this is a completely different matter!' Idiom 'another matter' expresses enthusiastic approval."),
    (6, None, "'In every bite the hand of a master is immediately visible!' Short feminine adjective 'visible' agrees with 'hand'."),
    (7, None, "'I would say that I worked with both hands!' Instrumental phrase 'with two hands' jokes about his culinary effort."),
    (8, None, "'Senya, what are you doing near the soup right now?' Returning to the pass, Barinov spots Senya with the sugar bowl."),
    (9, None, "'And I thought, what if you need sugar?' Senya hides the spoon behind his back after neutralizing the vinegar."),
    (10, None, "'What do I need sugar for in hot onion soup?' Barinov has no idea that Senya just saved the soup from German's vinegar."),
    (11, None, "'Forgive me, Chef, I am already going back to my station!' Meanwhile, Denis's busy evening in the dining room begins."),
]

TRANSITION = "Now let's hear the soup rescue scene again from start to finish."
OUTRO = "Unaware that Senya neutralized the vinegar with sugar, German prepares to expose Barinov in the dining room. See you in the next scene."
CLOSING = ("fedya", "В каждом кусочке сразу видна рука мастера!")
CLOSING_TRANS = "In every bite the hand of a master is immediately visible!"
