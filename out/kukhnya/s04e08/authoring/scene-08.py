ID = "kukhnya-s04e08-scene-08"
SHOW = "kukhnya"
SEASON = 4
EPISODE = 8
SCENE = 8
TITLE = "Новый человек в ресторане  (The New Man at the Restaurant)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "lyova": "anja", "guest": "angelina"}
LABELS = {"anya": "Шеф", "lyova": "Лёва", "guest": "Гость"}
SOURCE_NAME = "Кухня (Kukhnya) S4.08"
SOURCE_FILE = "sources/kukhnya/s04/e08.ru.srt"
SOURCE_NOTE = "Cues 135-148. While the owner of Arcobaleno shows a young man around the restaurant, Viktor Barinov assumes the newcomer is Elena's replacement and recruits Lyova to scare him away outside."

INTRO = "At Arcobaleno, the restaurant owner gives a young man a tour of the kitchen, pantry, and office, and the newcomer remarks that a lot will need to be changed. Watching from across the room, Viktor Barinov is certain this young man is the new chef hired to replace Elena!"

STORY = [
    ("guest", "Вот это наша кухня, а там дальше кабинет.", "Here is our kitchen, and further over there is the office.", [(135, "Ну, вот это, собственно, кухня."), (136, "Там кладовая, там кабинет,")], "adapted"),
    ("guest", "Там раздевалки и душ для нашего персонала.", "Over there are the locker rooms and shower for our staff.", [(137, "там раздевалки, душевые, туалет для персонала.")], "adapted"),
    ("guest", "Даже не знаю, что вам ещё тут показать.", "I do not even know what else to show you here.", [(138, "Что вам еще показать, я не знаю.")], "adapted"),
    ("guest", "Мне всё понятно, тут надо многое изменить.", "Everything is clear to me, a lot needs to be changed here.", [(139, "Да мне, в принципе, все понятно."), (140, "да вообще много чего изменить.")], "adapted"),
    ("anya", "Лёва, скажи быстро, а где сейчас Лена?", "Lyova, tell me quickly, where is Lena right now?", [(142, "Лёва, где Лена?")], "adapted"),
    ("lyova", "Хозяин её куда-то отправил, она будет через час.", "The owner sent her somewhere, she will be back in an hour.", [(143, "Уехал её Николай Андреевич куда-то отправил, через час будет.")], "adapted"),
    ("anya", "Видишь, Лёва, вот этот парень твой новый шеф!", "Do you see, Lyova, that guy right there is your new chef!", [(144, "Видишь, вот этот урод твой новый шеф.")], "adapted"),
    ("lyova", "Виктор Петрович, может быть, не надо вмешиваться?", "Viktor Petrovich, maybe we should not get involved?", [(145, "Виктор Петрович, может, не надо?")], "adapted"),
    ("anya", "Лёва, не начинай, мы просто с ним поговорим.", "Lyova, do not start, we will simply have a talk with him.", [(146, "Люва, не начинай."), (147, "Культурно поговорим.")], "adapted"),
    ("anya", "Объясним ему, что здесь ему работать не надо.", "We will explain to him that he does not need to work here.", [(146, "Просто объясним, что ему здесь работать не надо.")], ""),
    ("anya", "Мы поговорим с ним очень вежливо и культурно!", "We will speak with him very politely and civilly!", [(147, "Культурно поговорим.")], "adapted"),
    ("anya", "Давай, Лёва, пошли скорее за ним на улицу!", "Come on, Lyova, let's go after him outside quickly!", [(148, "Давай, давай.")], "adapted"),
]

OPENER = "Let's examine how Barinov misinterprets the kitchen tour line by line."

WALK = [
    (0, None, "'Here is our kitchen, and further over there is the office.' Demonstrative particle 'here is' points out each area of the restaurant."),
    (1, None, "'Over there are the locker rooms and shower for our staff.' Preposition 'for' governs the genitive collective noun 'staff'."),
    (2, None, "'I do not even know what else to show you here.' Infinitive question 'what else to show' takes the dative pronoun 'to you'."),
    (3, None, "'Everything is clear to me, a lot needs to be changed here.' Unaware the man is an interior designer, Barinov bristles at his comment."),
    (4, None, "'Lyova, tell me quickly, where is Lena right now?' Barinov checks when Elena Pavlovna is expected back."),
    (5, None, "'The owner sent her somewhere, she will be back in an hour.' Indefinite adverb 'to somewhere' marks an unspecified errand."),
    (6, None, "'Do you see, Lyova, that guy right there is your new chef!' Barinov jumps to the conclusion that the young man is the new head chef."),
    (7, None, "'Viktor Petrovich, maybe we should not get involved?' Gentle Lyova senses trouble as Barinov rolls up his sleeves."),
    (8, None, "'Lyova, do not start, we will simply have a talk with him.' Perfective future 'we will talk' sounds much calmer than Barinov's real plan."),
    (9, None, "'We will explain to him that he does not need to work here.' Dative pronoun 'to him' combines with 'does not need to work'."),
    (10, None, "'We will speak with him very politely and civilly!' Adverb 'culturally/civilly' is pure irony coming from Chef Barinov."),
    (11, None, "'Come on, Lyova, let's go after him outside quickly!' The two chefs follow the young man out to the parking lot."),
]

TRANSITION = "Now let's listen to the kitchen tour and Barinov's reaction again."
OUTRO = "Following the young man out to the courtyard parking lot, Viktor Barinov and Lyova decide to give him a memorable warning. See you in the next scene."
CLOSING = ("anya", "Объясним ему, что здесь ему работать не надо.")
CLOSING_TRANS = "We will explain to him that he does not need to work here."
