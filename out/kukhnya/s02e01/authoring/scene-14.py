# Authoring module for kukhnya s02e01 scene 14 (cues 192-194).
# Build: python3 tools/compose.py out/kukhnya/s02e01/authoring/scene-14.py --out out/kukhnya/s02e01/scene-14.json

ID = "kukhnya-s02e01-scene-14"
SHOW = "kukhnya"
SEASON = 2
EPISODE = 1
SCENE = 14
TITLE = "Утренний комплимент  (A Morning Compliment)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "igor": "anja"}
LABELS = {"anya": "Вика", "igor": "Игорь"}
SOURCE_NAME = "Кухня (Kukhnya) S2.01"
SOURCE_FILE = "sources/kukhnya/s02/e01.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 192-194. New restaurant owner Igor Valentinovich greets Vika in the dining room with a warm compliment, "
    "joking gallantly that he would surrender immediately in a competition with her."
)

INTRO = (
    "In the dining room at Claude Monet, the polite new owner Igor Valentinovich greets art director Vika Goncharova. "
    "He compliments her stylish appearance and jokes gallantly about competing with her charm. "
    "Let's listen to their conversation in Russian first."
)

OPENER = "Now let's examine this conversation line by line."

STORY = [
    ("igor", "Доброе утро, дорогая Виктория Сергеевна.",
     "Good morning, dear Victoria Sergeyevna.",
     [(192, "Доброе утро")], "adapted"),
    ("anya", "Доброе утро, уважаемый Игорь Валентинович.",
     "Good morning, respected Igor Valentinovich.",
     [(193, "Игорь Валентинович")], "adapted"),
    ("igor", "Вы сегодня просто прекрасно выглядите!",
     "You look simply wonderful today!",
     [(193, "Прекрасно выглядите")], "adapted"),
    ("anya", "Большое спасибо вам за комплимент.",
     "Thank you very much for the compliment.",
     [(193, "Прекрасно")], "adapted"),
    ("anya", "Я стараюсь не отставать от вас.",
     "I try not to fall behind you.",
     [(193, "Стараюсь не отставать от вас")], "adapted"),
    ("igor", "От меня? Вы очень добры ко мне.",
     "Behind me? You are very kind to me.",
     [(193, "от вас")], "adapted"),
    ("anya", "Вы всегда носите отличный строгий костюм.",
     "You always wear an excellent formal suit.",
     [(193, "выглядите")], "adapted"),
    ("igor", "Значит, для вас это как соревнование?",
     "So for you this is like a competition?",
     [(194, "как соревнование")], "adapted"),
    ("anya", "Может быть, только совсем немного.",
     "Maybe, only just a little bit.",
     [(194, "если вы")], "adapted"),
    ("igor", "Тогда я, пожалуй, сдамся прямо сразу.",
     "Then I think I will surrender right away.",
     [(194, "сдамся сразу")], "adapted"),
    ("anya", "Почему вы так быстро сдаётесь?",
     "Why do you surrender so quickly?",
     [(194, "сразу")], "adapted"),
    ("igor", "Потому что с вами невозможно спорить.",
     "Because it is impossible to argue with you.",
     [(194, "соревнование")], "adapted"),
    ("anya", "Хорошего вам рабочего дня в ресторане.",
     "Have a good workday in the restaurant.",
     [(192, "Доброе утро")], "adapted"),
    ("igor", "Спасибо, Вика, и вам удачного дня!",
     "Thank you, Vika, and have a successful day too!",
     [(194, "пожалуй")], "adapted"),
]

WALK = [
    (0, None,
     "'Good morning, dear Victoria Sergeyevna.' -- Igor Valentinovich greets the manager warmly as he arrives."),
    (1, None,
     "'Good morning, respected Igor Valentinovich.' -- Vika returns the formal greeting politely."),
    (2, None,
     "'You look simply wonderful today!' -- The new owner offers an admiring compliment."),
    (3, None,
     "'Thank you very much for the compliment.' -- Vika smiles graciously at his kind words."),
    (4, None,
     "'I try not to fall behind you.' -- She jokes that she is matching his polished style."),
    (5, None,
     "'Behind me? You are very kind to me.' -- Igor is flattered by her witty comparison."),
    (6, None,
     "'You always wear an excellent formal suit.' -- Vika notes his impeccable business attire."),
    (7, None,
     "'So for you this is like a competition?' -- Igor playfully asks if they are in a style contest."),
    (8, None,
     "'Maybe, only just a little bit.' -- Vika plays along with the lighthearted banter."),
    (9, None,
     "'Then I think I will surrender right away.' -- He gallantly concedes victory to her at once."),
    (10, None,
     "'Why do you surrender so quickly?' -- Vika asks with an amused smile."),
    (11, None,
     "'Because it is impossible to argue with you.' -- Igor charms her with another smooth reply."),
    (12, None,
     "'Have a good workday in the restaurant.' -- Vika wishes her new boss a productive morning."),
    (13, None,
     "'Thank you, Vika, and have a successful day too!' -- Igor heads toward his office in high spirits."),
]

TRANSITION = "Now let's listen to the whole morning greeting scene again without interruption."
OUTRO = (
    "Charmed by Igor Valentinovich's polite compliments and gentle humor, Vika begins her shift "
    "in a bright mood, unaware of the crazy stunt Max is preparing."
)
CLOSING = ("igor", "Вы сегодня просто прекрасно выглядите!")
