ID = "kukhnya-s01e14-scene-08"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 14
SCENE = 8
TITLE = "Обещание Нагиева  (Nagiyev's Promise)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "nagiev": "anja"}
LABELS = {"anya": "Диана", "nagiev": "Нагиев"}
SOURCE_NAME = "Кухня (Kukhnya) S1.14"
SOURCE_FILE = "sources/kukhnya/s01/e14.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 149-168. Restaurant owner Dmitry Nagiyev greets VIP guest Diana, who excitedly praises "
    "the handsome and sociable head chef she just met, unknowingly talking about Max."
)

INTRO = (
    "In the dining room, restaurant owner Dmitry Nagiyev greets his VIP guest Diana. "
    "She excitedly praises the handsome and sociable head chef she just met, unknowingly "
    "talking about Max instead of Chef Barinov. Confused but eager to please, Nagiyev agrees to her requests. "
    "Let us listen to their conversation in Russian first."
)

STORY = [
    ("nagiev", "Диана, вы как всегда прекрасно пахнете!",
     "Diana, you smell wonderful as always!",
     [(152, "Дианочка, как всегда, прекрасно, цветете, пахнете.")], "adapted"),
    ("anya", "Дмитрий, вы такой смешной.",
     "Dmitry, you are so funny.",
     [(155, "Невечка, вы такой смешной.")], "adapted"),
    ("anya", "Кстати, я уже познакомилась с шеф-поваром.",
     "By the way, I already met the head chef.",
     [(156, "мы уже познакомились с вашим шеф-поваром.")], "adapted"),
    ("nagiev", "Ой, Господи, и как он вам?",
     "Oh, Lord, and how is he for you?",
     [(157, "Ой, господи, а?")], "adapted"),
    ("anya", "Он супер, просто такой красавчик!",
     "He is super, just such a handsome man!",
     [(158, "Он супер, такой красавчик.")], "adapted"),
    ("nagiev", "Это вы вообще о ком говорите?",
     "Who are you talking about anyway?",
     [(159, "Это вы о ком?")], "adapted"),
    ("anya", "Он такой милый и очень общительный!",
     "He is so sweet and very sociable!",
     [(161, "Такой общительный!"), (162, "И вообще просто душка.")], "adapted"),
    ("nagiev", "Наверное, он сегодня в хорошем настроении.",
     "Probably, he is in a good mood today.",
     [], "new"),
    ("anya", "Мне подарили книгу с французскими рецептами.",
     "I was gifted a book with French recipes.",
     [(163, "мне подарили книгу с редкими французскими рецептами.")], "adapted"),
    ("nagiev", "Это очень интересный подарок.",
     "This is a very interesting gift.",
     [], "new"),
    ("anya", "Он мог бы приготовить для нас?",
     "Could he cook for us?",
     [(164, "мог бы приготовить что-нибудь из нее")], "adapted"),
    ("nagiev", "Если он в таком настроении, да.",
     "If he is in such a mood, yes.",
     [(165, "но если его"), (166, "и он в таком прекрасном настроении, думаю, да.")], "adapted"),
    ("anya", "Я хочу, чтобы он готовил здесь!",
     "I want him to cook here!",
     [(164, "прямо перед моими гостями?")], "adapted"),
    ("nagiev", "Хорошо, он всё сделает для вас.",
     "All right, he will do everything for you.",
     [], "new"),
]

OPENER = "Now let us examine Diana and Nagiyev's confusing conversation line by line."

WALK = [
    (0, None,
     "'Diana, you smell wonderful as always!' -- Nagiyev flatters his VIP guest with a charming compliment."),
    (1, None,
     "'Dmitry, you are so funny.' -- Diana giggles at the restaurant owner's energetic greeting."),
    (2, None,
     "'By the way, I already met the head chef.' -- The guest mentions her recent encounter in the dining room."),
    (3, None,
     "'Oh, Lord, and how is he for you?' -- Nagiyev worries about what the usually rude Barinov might have said."),
    (4, None,
     "'He is super, just such a handsome man!' -- Diana swoons over the young cook she mistook for the boss."),
    (5, None,
     "'Who are you talking about anyway?' -- The owner is completely baffled by this glowing description of Barinov."),
    (6, None,
     "'He is so sweet and very sociable!' -- Diana continues to praise Max's charming and talkative personality."),
    (7, None,
     "'Probably, he is in a good mood today.' -- Nagiyev assumes the chef is just having a rare good day."),
    (8, None,
     "'I was gifted a book with French recipes.' -- Diana brings up a new cookbook she recently received."),
    (9, None,
     "'This is a very interesting gift.' -- Nagiyev politely acknowledges her exciting new present."),
    (10, None,
     "'Could he cook for us?' -- The guest asks if the chef can prepare something special from it."),
    (11, None,
     "'If he is in such a mood, yes.' -- The owner cautiously agrees, hoping Barinov remains cooperative."),
    (12, None,
     "'I want him to cook here!' -- Diana requests a live cooking demonstration in front of her table."),
    (13, None,
     "'All right, he will do everything for you.' -- Nagiyev promises to fulfill her demand to keep her happy."),
]

TRANSITION = "Now let us listen to Diana and Nagiyev once again."
OUTRO = (
    "Eager to please his wealthy guest, Nagiyev blindly promises that the chef "
    "will cook live in the dining room, setting up a disastrous encounter with the real Barinov."
)
CLOSING = ("nagiev", "Хорошо, он всё сделает для вас.")
