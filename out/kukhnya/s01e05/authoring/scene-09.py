"""s01e05 scene 09: Поддержка подруги (A Friend's Support)."""

ID = "kukhnya-s01e05-scene-09"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 5
SCENE = 9
TITLE = "Поддержка подруги  (A Friend's Support)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "sasha": "anja"}
LABELS = {"anya": "Настя", "sasha": "Саша"}
SOURCE_NAME = "Кухня (Kukhnya) S1.05"
SOURCE_FILE = "sources/kukhnya/s01/e05.ru.dual.srt"

INTRO = (
    "In the quiet service area, waitress Nastya is sobbing after her painful breakup with Max. "
    "Her close colleague Sasha comes over to comfort her, telling her not to waste tears on a careless cook and reminding her of her worth. "
    "Let's listen to their conversation in Russian first."
)

STORY = [
    ("sasha", "Настя, перестань так сильно расстраиваться!",
     "Nastya, stop being so deeply upset!",
     [(137, "Да не расстраивайся ты")], "comforting her colleague"),
    ("anya", "Мне очень больно, он разбил мне сердце.",
     "It hurts me very much, he broke my heart.",
     [], "expressing intense heartbreak"),
    ("sasha", "Знаешь, сколько парней у тебя ещё будет?",
     "Do you know how many more guys you will still have?",
     [(138, "Знаешь, сколько мужиков тебя еще кинет")], "encouraging her with optimism"),
    ("anya", "Мне не нужны другие, мне нравился Макс.",
     "I do not need others, I liked Max.",
     [], "explaining her feelings"),
    ("sasha", "Неужели стоит так убиваться из-за каждого?",
     "Is it really worth falling apart over every one?",
     [(139, "Что, и за каждого убиваться, что ли")], "questioning her excessive grief"),
    ("anya", "Я боюсь, что меня снова обманут.",
     "I am afraid that they will deceive me again.",
     [(140, "Меня опять кинут")], "sharing her recurring fear"),
    ("sasha", "Ты добрая, красивая и очень умная.",
     "You are kind, beautiful, and very smart.",
     [], "reassuring her of her worth"),
    ("anya", "Тогда почему он так быстро забыл меня?",
     "Then why did he forget me so quickly?",
     [], "asking with genuine sorrow"),
    ("sasha", "Потому что он глупый и ветреный парень.",
     "Because he is a foolish and fickle guy.",
     [], "criticizing Max's carelessness"),
    ("anya", "Я хочу, чтобы он понял свою ошибку.",
     "I want him to understand his mistake.",
     [], "shifting to injured pride"),
    ("sasha", "Вот это уже правильные мысли, подруга!",
     "Now those are the right thoughts, my friend!",
     [], "supporting her determination"),
    ("anya", "Спасибо тебе огромное за тёплую поддержку.",
     "Thank you so much for the warm support.",
     [], "thanking her friend warmly"),
]

OPENER = "Let's review this supportive conversation between colleagues line by line."

WALK = [
    (0, None,
     "'Nastya, stop being so deeply upset!' Sasha tries to calm her distraught friend down."),
    (1, None,
     "'It hurts me very much, he broke my heart.' Nastya confesses how wounded she feels by the sudden rejection."),
    (2, None,
     "'Do you know how many more guys you will still have?' Sasha reminds her that she has a bright romantic future ahead."),
    (3, None,
     "'I do not need others, I liked Max.' Nastya laments that she was genuinely interested in the new cook."),
    (4, None,
     "'Is it really worth falling apart over every one?' Sasha argues that no careless man is worth so many tears."),
    (5, None,
     "'I am afraid that they will deceive me again.' Nastya shares her deep fear of repeated heartbreak."),
    (6, None,
     "'You are kind, beautiful, and very smart.' Sasha boosts Nastya's self-esteem with warm compliments."),
    (7, None,
     "'Then why did he forget me so quickly?' Nastya struggles to comprehend Max's indifferent attitude."),
    (8, None,
     "'Because he is a foolish and fickle guy.' Sasha bluntly assesses Max's immature behavior."),
    (9, None,
     "'I want him to understand his mistake.' Nastya shifts from despair to a sense of injured pride."),
    (10, None,
     "'Now those are the right thoughts, my friend!' Sasha encourages Nastya's newfound resolve."),
    (11, None,
     "'Thank you so much for the warm support.' Nastya expresses heartfelt gratitude to her loyal friend."),
]

TRANSITION = "Now let's listen to the whole dialogue again at normal conversational speed."

OUTRO = (
    "With Sasha's sincere support, Nastya begins to recover her dignity and self-confidence. "
    "See you next time!"
)

CLOSING = ("anya", "Спасибо тебе огромное за тёплую поддержку.")
