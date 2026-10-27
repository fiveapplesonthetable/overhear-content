"""Scene 46 — Delicious Morning (s01e10, 00:23:51–00:24:07)."""

ID = "kukhnya-s01e10-scene-46"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 10
SCENE = 46
TITLE = "Вкусное утро  (Delicious Morning)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Кухня (Kukhnya) S1.10"
SOURCE_FILE = "sources/kukhnya/s01/e10.ru.dual.srt"

VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "host": "anja",
}

LABELS = {
    "anya": "Макс",
    "host": "Ведущий",
}

INTRO = (
    "As the sun rises over Moscow, the cheerful host of the morning TV show 'Delicious Morning' whips up a simple breakfast on air. "
    "Watching the broadcast, Max reflects on the importance of seizing every opportunity, because fate rarely grants a second chance."
)

STORY = [
    ("host", "Доброе утро всем ранним зрителям нашего шоу!",
     "Good morning to all early viewers of our show!",
     [(342, "Доброе утро всем тем, кому не спится в такую рань.")], "Host greets audience"),

    ("host", "С вами снова любимая передача Вкусное утро.",
     "With you again is your favorite show Delicious Morning.",
     [(343, "Вкусное утро.")], "Host announces"),

    ("host", "Сегодня мы приготовим простую аппетитную глазунью.",
     "Today we will prepare simple appetizing sunny-side-up eggs.",
     [(343, "Мы сегодня будем готовить глазунью.")], "Host explains recipe"),

    ("anya", "Каждое утро открывает перед нами новый день.",
     "Every morning opens a new day before us.",
     [], "Max watches TV"),

    ("host", "Берём свежие яйца и разогреваем сковороду.",
     "We take fresh eggs and heat the frying pan.",
     [], "Host demonstrates"),

    ("anya", "Иногда простые вещи оказываются самыми важными.",
     "Sometimes simple things turn out to be the most important.",
     [], "Max reflects on simplicity"),

    ("host", "Добавляем немного сливочного масла и соли.",
     "We add a little butter and salt.",
     [], "Host seasons eggs"),

    ("anya", "Мы часто ищем сложных ответов на вопросы.",
     "We often look for complex answers to questions.",
     [], "Max ponders"),

    ("host", "Несколько минут — и великолепный завтрак готов!",
     "A few minutes and a wonderful breakfast is ready!",
     [], "Host plates breakfast"),

    ("anya", "Главное — никогда не упускать свои возможности.",
     "The main thing is never to miss your opportunities.",
     [(344, "Главное, не упускать эти возможности.")], "Max advises"),

    ("anya", "Судьба может не дать нам второй шанс.",
     "Fate might not give us a second chance.",
     [(345, "Ведь может получиться так, что второго шанса судьба не даст.")], "Max warns"),

    ("host", "Приятного аппетита и хорошего дня всем!",
     "Bon appetit and have a good day everyone!",
     [], "Host wraps up"),

    ("anya", "Цените каждый миг своей настоящей жизни.",
     "Value every moment of your real life.",
     [], "Max concludes episode"),
]

OPENER = "Let's tune into the early morning cooking program and listen to Max's final reflections on fate and second chances."

WALK = [
    (0, None,
     "'Good morning to all early viewers of our show!' The upbeat TV host greets early risers brightly."),
    (1, None,
     "'With you again is your favorite show Delicious Morning.' The cheerful morning theme echoes softly."),
    (2, None,
     "'Today we will prepare simple appetizing sunny-side-up eggs.' The TV chef introduces a classic breakfast."),
    (3, None,
     "'Every morning opens a new day before us.' Max reflects on the fresh possibilities of dawn."),
    (4, None,
     "'We take fresh eggs and heat the frying pan.' The culinary demonstration begins on television."),
    (5, None,
     "'Sometimes simple things turn out to be the most important.' Max realizes that life's joys are uncomplicated."),
    (6, None,
     "'We add a little butter and salt.' The host cooks with calm and rhythmic precision."),
    (7, None,
     "'We often look for complex answers to questions.' Max acknowledges how people complicate simple choices."),
    (8, None,
     "'A few minutes and a wonderful breakfast is ready!' The steaming eggs are proudly presented on the screen."),
    (9, None,
     "'The main thing is never to miss your opportunities.' Max urges embracing every chance with open arms."),
    (10, None,
     "'Fate might not give us a second chance.' Max solemnly notes the rarity of second opportunities."),
    (11, None,
     "'Bon appetit and have a good day everyone!' The TV broadcast signs off with warmth and smiles."),
    (12, None,
     "'Value every moment of your real life.' Max ends his philosophical reflection on a poignant note."),
]

TRANSITION = "Now let's listen to the morning broadcast and Max's parting words on seizing life once more."

OUTRO = "A new day dawns at Claude Monet, reminding everyone to treasure every opportunity before it slips away."

CLOSING = ("anya", "Цените каждый миг своей настоящей жизни.")
