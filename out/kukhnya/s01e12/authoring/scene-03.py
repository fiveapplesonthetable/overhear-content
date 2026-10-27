ID = "kukhnya-s01e12-scene-03"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 12
SCENE = 3
TITLE = "Пустое место  (An Empty Place)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "vika": "anja"}
LABELS = {"anya": "Макс", "vika": "Вика"}
SOURCE_NAME = "Кухня (Kukhnya) S1.12"
SOURCE_FILE = "sources/kukhnya/s01/e12.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 16-26. Max follows Victoria to apologize, but she harshly tells him he is "
    "an empty place to her."
)

INTRO = (
    "Undeterred by her initial rejection, Max follows Victoria to her office to apologize for his prank. "
    "However, Victoria is in no mood for jokes and delivers a crushing blow to his ego. "
    "Let's listen to their conversation in Russian first."
)

STORY = [
    ("anya", "Вика, послушай, нам было так хорошо вместе.",
     "Vika, listen, it was so good for us together.",
     [(16, "Вик, ты что-то пишешь, пошутил."), (17, "Слушай, нам было так трогательно.")], "adapted"),
    ("vika", "Слушай меня внимательно, мой дорогой друг.",
     "Listen to me carefully, my dear friend.",
     [(19, "Послушай, можешь шутить сколько угодно")], "adapted"),
    ("anya", "Что с тобой? Ты такая злая сегодня.",
     "What is with you? You are so angry today.",
     [(18, "что с тобой ты такой?")], "adapted"),
    ("vika", "Шути свои дурацкие шутки на кухне!",
     "Joke your stupid jokes in the kitchen!",
     [(20, "как ты, вот там, на кухне, за дверью.")], "adapted"),
    ("anya", "Зачем ты так грубо со мной говоришь?",
     "Why are you talking to me so rudely?",
     [], "new"),
    ("vika", "Там за дверью много таких же идиотов.",
     "There are many of the same idiots behind the door.",
     [(19, "только в компании таких же идиотов,")], "adapted"),
    ("anya", "Но я принёс нам билеты в кино.",
     "But I brought us tickets to the cinema.",
     [], "new"),
    ("vika", "Мне не интересны твои билеты в кино.",
     "I am not interested in your tickets to the cinema.",
     [(21, "Мне не интересны твои шутки и твои билеты в кино.")], "adapted"),
    ("anya", "Почему ты не хочешь пойти со мной?",
     "Why do you not want to go with me?",
     [], "new"),
    ("vika", "Потому что ты для меня пустое место.",
     "Because you are an empty place to me.",
     [(22, "Ты для меня пустое место.")], "adapted"),
    ("anya", "Пустое место? Ты очень добрая девушка.",
     "An empty place? You are a very kind girl.",
     [(24, "Пустое место, значит?")], "adapted"),
    ("vika", "Ты всё понял? А теперь уйди отсюда.",
     "Have you understood everything? And now leave from here.",
     [(23, "Понял?"), (21, "А ко мне не лезь.")], "adapted"),
    ("anya", "Ладно, извините, я ухожу прямо сейчас.",
     "Alright, excuse me, I am leaving right now.",
     [(26, "Ладно, извините.")], "adapted"),
]

OPENER = "Now let's examine this harsh rejection line by line."

WALK = [
    (0, None,
     "'Vika, listen, it was so good for us together.' -- Max tries to remind her of their romantic history."),
    (1, None,
     "'Listen to me carefully, my dear friend.' -- Victoria interrupts his apologies with a cold tone."),
    (2, None,
     "'What is with you? You are so angry today.' -- The confused cook wonders why she is so hostile."),
    (3, None,
     "'Joke your stupid jokes in the kitchen!' -- She tells him to keep his childish behavior out of her sight."),
    (4, None,
     "'Why are you talking to me so rudely?' -- Max is taken aback by her aggressive words."),
    (5, None,
     "'There are many of the same idiots behind the door.' -- The manager compares him to the rest of the immature brigade."),
    (6, None,
     "'But I brought us tickets to the cinema.' -- He still hopes to salvage their date."),
    (7, None,
     "'I am not interested in your tickets to the cinema.' -- Victoria completely dismisses the romantic gesture from him."),
    (8, None,
     "'Why do you not want to go with me?' -- He asks for a clear reason for her rejection."),
    (9, None,
     "'Because you are an empty place to me.' -- She delivers a cruel and devastating insult."),
    (10, None,
     "'An empty place? You are a very kind girl.' -- Max responds to her harsh words with deep sarcasm."),
    (11, None,
     "'Have you understood everything? And now leave from here.' -- She orders him to get out of her presence."),
    (12, None,
     "'Alright, excuse me, I am leaving right now.' -- Finally accepting defeat, he quietly backs away."),
]

TRANSITION = "Now let's listen to the harsh rejection again without interruption."
OUTRO = (
    "Stung by Victoria's cruel words, a humbled Max retreats to the kitchen, "
    "realizing that his charming tricks will not work on her anymore."
)
CLOSING = ("anya", "Ладно, извините, я ухожу прямо сейчас.")
