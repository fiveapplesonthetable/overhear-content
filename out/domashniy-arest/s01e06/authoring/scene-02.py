# domashniy-arest/s01e06/scene-02.py
ID = "domashniy-arest-s01e06-scene-02"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 6
SCENE = 2
TITLE = "Ваш долг полностью аннулирован  (Your Debt Is Fully Canceled)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.06"
SOURCE_FILE = "sources/domashniy-arest/s01/e06.ru.dual.srt"
VOICES = {"narrator": "sky", "grisha": "anja", "kostik": "angelina"}
LABELS = {"grisha": "Дядя Гриша", "kostik": "Костик"}
INTRO = "Out on the landing of the communal flat that morning, neighbour Marina opens the door and finds the two debt collectors, Uncle Grisha and Kostik, standing there with fresh bruises. Listen as Uncle Grisha politely cancels her debt, hands her flowers, and passes on a message from Dean Eduard Vladimirovich."
STORY = [
    ("grisha", "Здравствуйте, Марина Сергеевна!", "Hello, Marina Sergeyevna!", [(51, 'Здравствуйте, Марина Сергеевна')], ""),
    ("kostik", "Что вам опять надо?", "What do you need again?", [(52, 'Что вам опять надо')], ""),
    ("grisha", "Наша организация приносит свои извинения.", "Our organization offers its apologies.", [(53, 'Наша организация приносит свои извинения')], ""),
    ("grisha", "Мы с радостью сообщаем вам новость. Ваш долг полностью аннулирован!", "We gladly inform you of the news. Your debt is completely canceled!", [(54, 'с радостью'), (55, 'ваш долг полностью аннулирован')], "cue 54 'за возникшее недоразумение и с радостью сообщает' simplified"),
    ("grisha", "Поздравляем вас! Константин, дай цветы.", "Congratulations to you! Konstantin, give her the flowers.", [(56, 'Поздравляем'), (57, 'Константин')], "'вас' and 'дай цветы' added"),
    ("kostik", "Это небольшой комплимент от нашего заведения.", "This is a small gift from our establishment.", [(58, 'Небольшой комплимент от нашего заведения')], "'Это' added"),
    ("grisha", "И ещё кое-что. Эдуард Владимирович просил передать привет.", "And one more thing. Eduard Vladimirovich asked us to pass on his regards.", [(59, 'И еще'), (60, 'Эдуард'), (60, 'просил передать')], "cue 60 'Валентинович' restored to 'Владимирович'; 'привет' added"),
    ("grisha", "Он жить без вас не может! В общем, просил позвонить.", "He cannot live without you! In short, he asked you to call.", [(60, 'жить без вас не может'), (62, 'В общем, просил позвонить')], ""),
    ("kostik", "Да, пожалуйста, возьмите цветы.", "Yes, please, take the flowers.", [(64, 'Да, пожалуйста')], "'возьмите цветы' added"),
    ("grisha", "И, Марина Сергеевна, читайте всё внимательно! Особенно мелким шрифтом!", "And, Marina Sergeyevna, read everything carefully! Especially in fine print!", [(65, 'И, Марина Сергеевна, читайте'), (65, 'все'), (65, 'мелким шрифтом')], "cue 65 split into two short sentences"),
    ("grisha", "Не все компании такие добрые, как наша.", "Not all companies are as kind as ours.", [(66, 'не все'), (66, 'такие'), (66, 'как')], "cue 66 'микрофинансовые структуры такие же лояльные, как наши' simplified to A1"),
    ("grisha", "Костик, чего ты улыбаешься? Из-за тебя я сейчас унижался!", "Kostik, what are you smiling at? Because of you I just humiliated myself!", [(67, 'Чего улыбаешься'), (68, 'я'), (68, 'сейчас'), (68, 'унижался')], "cue 68 garbled 'Ветыш, если б не ты' -> 'Костик... Из-за тебя'"),
    ("grisha", "Сильный ищет способ, а слабый ищет причину.", "The strong man looks for a way, and the weak man looks for an excuse.", [(71, 'способ, слабый причину')], "cue 71 garbled 'Сильно ищи' -> 'Сильный ищет'"),
    ("kostik", "Я ничего не ищу. Так проходит жизнь!", "I'm not looking for anything. That is how life passes!", [(72, 'Ничего не ищу. Так проходит жизнь')], "'Я' added"),
]
OPENER = "Let's go back through the scene step by step. Uncle Grisha stands respectfully on the landing in his leather cap while Kostik holds a bouquet of flowers."
WALK = [
    (0, None, "'Hello, Marina Sergeyevna!' Today Uncle Grisha greets Marina politely by her first name and patronymic."),
    (1, None, "'What do you need again?' Literally 'what to you again is necessary?', with 'to you' in the 'to/for' form."),
    (2, None, "'Our organization offers its apologies.' Literally 'brings its apologies', using the formal plural noun."),
    (3, 'Мы с радостью сообщаем вам новость.', "'We gladly inform you of the news.' Literally 'with joy we report to you the news'."),
    (3, 'Ваш долг полностью аннулирован!', "'Your debt is completely canceled!' The short passive form matches the masculine noun 'debt'."),
    (4, None, "'Congratulations to you! Konstantin, give her the flowers.' Uncle Grisha addresses Kostik by his full name."),
    (5, None, "'This is a small gift from our establishment.' In Russian service talk, a 'compliment from the house' means a free gift on the house."),
    (6, None, "'And one more thing. Eduard Vladimirovich asked us to pass on his regards.' Marina has no idea that Arkady was the one who actually sent his bodyguards to rescue her."),
    (7, 'Он жить без вас не может!', "'He cannot live without you!' The preposition 'without' always takes the 'of' form."),
    (7, 'В общем, просил позвонить.', "'In short, he asked you to call.' Kostik holds the bouquet out to Marina."),
    (8, None, "'Yes, please, take the flowers.' Marina takes the bouquet in surprise."),
    (9, 'И, Марина Сергеевна, читайте всё внимательно!', "'And, Marina Sergeyevna, read everything carefully!' Before leaving, Uncle Grisha offers one piece of advice."),
    (9, 'Особенно мелким шрифтом!', "'Especially in fine print!' Literally 'by small font', using the 'with/as' form."),
    (10, None, "'Not all companies are as kind as ours.' Then Marina closes the door, and the two bruised collectors walk down the stairs."),
    (11, 'Костик, чего ты улыбаешься?', "'Kostik, what are you smiling at?' In colloquial speech, 'of what' is often used to mean 'why'."),
    (11, 'Из-за тебя я сейчас унижался!', "'Because of you I just humiliated myself!' The preposition for 'because of' (for a bad reason) takes the 'of' form."),
    (12, None, "'The strong man looks for a way, and the weak man looks for an excuse.' Uncle Grisha quotes a solemn proverb."),
    (13, None, "'I'm not looking for anything. That is how life passes!' Kostik sighs philosophically, echoing the phrase Arkady taught them the day before."),
]
TRANSITION = "Now let's hear the whole scene on the landing again from the start."
OUTRO = "So Marina's microloan debt is gone and she thinks Dean Eduard Vladimirovich is her hero. See you next time!"
CLOSING = ("grisha", "Пока!")
