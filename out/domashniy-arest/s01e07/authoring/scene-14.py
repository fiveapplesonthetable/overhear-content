# domashniy-arest/s01e07/scene-14.py
ID = "domashniy-arest-s01e07-scene-14"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 7
SCENE = 14
TITLE = "Рентгеновские снимки  (The X-Rays)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Домашний арест, Сезон 1, Эпизод 7"
SOURCE_FILE = "sources/domashniy-arest/s01/e07.ru.dual.srt"
VOICES = {"narrator": "sky", "anya": "alisa", "marina": "angelina", "dean": "anja"}
LABELS = {"anya": "Аркадий", "marina": "Марина", "dean": "Эдуард Владимирович"}
INTRO = "Previously, down in the FSB paper archive, Lieutenant Lyova Sokolov walked out on Lavrov and Zavarzin when they refused to transfer him to Moscow. Now, back at the communal apartment stairwell, Marina and Eduard carefully help Arkady up the stairs with both of his arms immobilized in plaster casts."
STORY = [
    ("marina", "Аккуратнее! Держи его, Эдик!", "More carefully! Hold him, Edik!", [(528, 'Аккуратнее!'), (533, 'Держи')], "combined cues 528 and 533"),
    ("dean", "Держу, держу.", "I'm holding him, I'm holding him.", [(534, 'Держу, держу')], ""),
    ("anya", "Послушайте, спасибо вам огромное! Заходите.", "Listen, thank you so very much! Come on in.", [(536, 'Послушайте, спасибо вам огромное. Заходите')], ""),
    ("anya", "Спасибо за всё, что вы сделали.", "Thank you for everything that you did.", [(537, 'за все, что вы сделали')], "added Спасибо"),
    ("anya", "Я потратил столько вашего времени!", "I took up so much of your time!", [(538, 'Я потратил'), (539, 'столько вашего времени')], "combined cues 538-539"),
    ("anya", "Скажите, а где мои рентгеновские снимки?", "Tell me, where are my X-ray pictures?", [(540, 'Скажите, а'), (541, 'снимки'), (543, 'Рентгеновские')], "combined cues 540, 541, and 543"),
    ("marina", "Что? Снимки? Они остались в больнице!", "What? The pictures? They stayed at the hospital!", [(542, 'Что?'), (541, 'снимки'), (544, 'Они остались в больнице')], "combined cues 541, 542, and 544"),
    ("anya", "Как остались? Надо срочно за ними бежать!", "How could they stay there? I must urgently run back for them!", [(545, 'Как остались?'), (546, 'Надо за ними бежать')], "omitted mild oath Черт; added срочно"),
    ("dean", "Вы что, специально это делаете?", "Are you doing this on purpose or what?", [(548, 'Вы что'), (548, 'специально')], "adapted colloquial что ли"),
    ("marina", "Спокойно, Эдик! Он никуда не может бежать!", "Calm down, Edik! He can't run anywhere!", [(550, 'Спокойно, Эдик!'), (551, 'Никуда не может бежать!')], "added pronoun Он"),
    ("anya", "Ну что вы, давайте я сам!", "Oh come on, let me go myself!", [(552, 'Ну что вы, давайте')], "added я сам"),
    ("marina", "Что вы обнимаетесь? Вы с ума сошли!", "Why are you two hugging? Have you lost your minds!", [(554, 'Что вы обнимаетесь? С ума')], "fixed ASR сошлитесь to Вы с ума сошли"),
    ("marina", "Эдик, не бросай его!", "Edik, don't drop him!", [(558, 'Не бросайте')], "adapted plural Не бросайте to singular"),
    ("dean", "Вы отдыхайте, а мы сами поедем.", "You rest, and we'll go ourselves.", [(559, 'Вы отдыхайте')], "replaced ASR если что-то завидите with а мы сами поедем"),
    ("dean", "А я ему, между прочим, не доверяю!", "And by the way, I don't trust him!", [(561, 'А я ему, между прочим, не доверяю')], ""),
]
OPENER = "Let's unpack how Arkady tricks Marina and Eduard into going back to the hospital."
WALK = [
    (0, None, "'More carefully! Hold him, Edik!' Marina guides Arkady up the stairs as if he were helpless."),
    (2, None, "'Listen, thank you so very much! Come on in.' Arkady plays the grateful neighbor."),
    (4, None, "'I spent so much of your time!' He pretends to feel guilty about the long evening."),
    (5, None, "'Tell me, where are my X-ray pictures?' Suddenly he asks about the hospital files."),
    (6, 'Они остались в больнице!', "'They stayed at the hospital!' Marina realizes they left the X-rays behind."),
    (7, None, "'How could they stay there? I must urgently run back for them!' Notice the self-action verb form on the verb for 'stayed', which directs the action back onto the subject."),
    (8, None, "'Are you doing this on purpose?' Eduard suspects that Arkady is playing another trick."),
    (9, None, "'Calm down, Edik! He cannot run anywhere!' Remember that Arkady is under house arrest with an ankle bracelet."),
    (10, None, "'Oh come on, let me go myself!' Arkady lunges toward the stairs, tangling his plaster casts around Eduard."),
    (11, None, "'Why are you two hugging? Have you lost your minds!' Their awkward struggle looks like a clinch."),
    (13, None, "'You rest, and we will go ourselves.' Eduard agrees to go back to the hospital just to get away from him."),
    (14, None, "'And by the way, I do not trust him!' Eduard grumbles as Marina pulls him down the stairs."),
]
TRANSITION = "Now listen to the stairwell scene again."
OUTRO = "As soon as Marina and Eduard hurry down the stairs, Arkady grins and slips inside with his fake casts. See you next time!"
CLOSING = ("dean", "Пока!")
