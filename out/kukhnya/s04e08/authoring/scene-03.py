ID = "kukhnya-s04e08-scene-03"
SHOW = "kukhnya"
SEASON = 4
EPISODE = 8
SCENE = 3
TITLE = "Комната за двадцатку  (A Room for Twenty Grand)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "denis": "anja", "fedya": "angelina"}
LABELS = {"anya": "Сеня", "denis": "Денис", "fedya": "Федя"}
SOURCE_NAME = "Кухня (Kukhnya) S4.08"
SOURCE_FILE = "sources/kukhnya/s04/e08.ru.srt"
SOURCE_NOTE = "Cues 40-56. Denis asks the kitchen crew if anyone is renting out a room, and after Fedya reminds Senya about the motorboat, Senya offers Denis a room in his apartment for twenty thousand rubles."

INTRO = "In the kitchen of Claude Monet, Denis asks the cooks whether anyone knows of a room for rent. At first Senya brushes him off, until Fedya reminds him of the twenty thousand rubles he needs for his motorboat—prompting Senya to offer Denis a room in his own apartment!"

STORY = [
    ("denis", "Парни, никто из знакомых комнату не сдаёт?", "Guys, is nobody you know renting out a room?", [(40, "Парни, не слышали? Комнату никто не сдает.")], "adapted"),
    ("anya", "Мы тебе что, похожи на агентство жилья?", "What do we look like to you, a housing agency?", [(41, "Тебе риелторы, что ли? Давай греби отсюда.")], "adapted"),
    ("fedya", "Сеня, он ищет комнату, чего ты тупишь?", "Senya, he is looking for a room, why are you being slow?", [(42, "Комнату. Ну, чего ты тупишь?")], "adapted"),
    ("fedya", "Ведь иначе твоя красная лодка точно уйдёт!", "Otherwise your red boat will definitely slip away!", [(43, "Уйдет же лодка.")], "adapted"),
    ("anya", "Подожди, есть хорошая комната у меня в квартире!", "Wait, there is a nice room in my apartment!", [(45, "Стоять. Есть комната за двадцатку у меня в квартире.")], "adapted"),
    ("anya", "Я сдам тебе её всего за двадцать тысяч.", "I will rent it to you for just twenty thousand.", [(45, "Есть комната за двадцатку у меня в квартире.")], "adapted"),
    ("denis", "Честно говоря, это для меня немного дороговато.", "Honestly speaking, that is a bit pricey for me.", [(46, "Чего-то дороговато.")], "adapted"),
    ("anya", "Ты же будешь жить не у чужих людей!", "After all, you will not be living with strangers!", [(47, "Ты же не у чужих будешь жить, у своих.")], "adapted"),
    ("anya", "Я тебя ночью на улицу точно не выгоню.", "I definitely will not kick you out onto the street at night.", [(48, "Я тебя ночью на улицу не выгоню.")], "adapted"),
    ("denis", "Ладно, я хорошо подумаю над твоим предложением.", "All right, I will think carefully about your offer.", [(50, "Я подумаю.")], "adapted"),
    ("fedya", "А жена твоя Марина тебе не возразит?", "And will your wife Marina not object to you?", [(52, "Маленькая перешка."), (53, "Маленькая не навтыкаешь по башке?")], "adapted"),
    ("anya", "В доме хозяин я, как попрошу, так и будет!", "I am the master of the house, whatever I ask for is how it will be!", [(54, "Кто в доме хозяин, я как скажу, так и будет."), (55, "Ну, как я попрошу, так и будет.")], "adapted"),
]

OPENER = "Let's break down Senya's room-rental pitch to Denis line by line."

WALK = [
    (0, None, "'Guys, is nobody you know renting out a room?' Imperfective present verb 'rents out' takes the feminine accusative 'room'."),
    (1, None, "'What do we look like to you, a housing agency?' Senya initially waves the rookie away without thinking."),
    (2, None, "'Senya, he is looking for a room, why are you being slow?' Colloquial verb 'to be slow-witted' nudges Senya to connect the dots."),
    (3, None, "'Otherwise your red boat will definitely slip away!' Fedya reminds Senya that a tenant means instant boat money."),
    (4, None, "'Wait, there is a nice room in my apartment!' Senya immediately reverses course and calls Denis back."),
    (5, None, "'I will rent it to you for just twenty thousand.' Conveniently, the rent equals the exact price of the motorboat."),
    (6, None, "'Honestly speaking, that is a bit pricey for me.' Suffix on the adverb 'a bit expensive' softens the objection."),
    (7, None, "'After all, you will not be living with strangers!' Substantivized plural adjective 'strangers' contrasts with 'your own people'."),
    (8, None, "'I definitely will not kick you out onto the street at night.' Perfective future verb 'will drive out' promises security."),
    (9, None, "'All right, I will think carefully about your offer.' Preposition 'over/about' governs the instrumental singular 'offer'."),
    (10, None, "'And will your wife Marina not object to you?' Fedya knows that Marina actually runs Senya's household."),
    (11, None, "'I am the master of the house, whatever I ask for is how it will be!' Senya quickly downgrades 'as I say' to 'as I ask'."),
]

TRANSITION = "Now let's hear the room-rental negotiation in the kitchen again."
OUTRO = "While Senya figures out how to persuade his wife Marina, Viktor Barinov uncovers a troubling secret next door at Arcobaleno. See you in the next scene."
CLOSING = ("anya", "В доме хозяин я, как попрошу, так и будет!")
CLOSING_TRANS = "I am the master of the house, whatever I ask for is how it will be!"
