ID = "kukhnya-s02e02-scene-16"
SHOW = "kukhnya"
SEASON = 2
EPISODE = 2
SCENE = 16
TITLE = "Срочное дело  (Urgent Business)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "anja": "anja"}
LABELS = {"anya": "Вика", "anja": "Нагиев"}
SOURCE_NAME = "Кухня (Kukhnya) S2.02"
SOURCE_FILE = "sources/kukhnya/s02/e02.ru.dual.srt"
SOURCE_NOTE = "Scene 16"

INTRO = "Nagiyev urgently asks Victoria to come with him to discuss a very important matter. Victoria is busy and annoyed by his sudden request."

STORY = [
    ("anja", "Вика!",
     "Vika!",
     [(273, 'Вика!')], "adapted"),
    ("anya", "Да, я тебя внимательно слушаю.",
     "Yes, I am listening to you carefully.",
     [(274, 'Я тебя слушаю.')], "adapted"),
    ("anja", "Нам нужно срочно поговорить.",
     "We need to talk urgently.",
     [], "new"),
    ("anya", "Что у тебя там за срочное дело?",
     "What urgent business do you have there?",
     [(275, 'Что у тебя там за срочное дело')], "adapted"),
    ("anya", "О котором ты не можешь говорить по телефону?",
     "About which you cannot speak on the phone?",
     [(275, 'о котором ты не можешь говорить по телефону')], "adapted"),
    ("anja", "Это не для телефонного разговора.",
     "This is not for a telephone conversation.",
     [], "new"),
    ("anya", "Я сейчас очень занята.",
     "I am very busy right now.",
     [], "new"),
    ("anja", "Это действительно очень важно.",
     "This is truly very important.",
     [], "new"),
    ("anya", "Хорошо, что случилось?",
     "Fine, what happened?",
     [], "new"),
    ("anja", "Просто пойдем со мной.",
     "Just come with me.",
     [(276, 'Пойдем со мной.')], "adapted"),
    ("anya", "Куда мы идём?",
     "Where are we going?",
     [], "new"),
    ("anja", "Ты скоро всё сама увидишь.",
     "You will soon see everything yourself.",
     [], "new"),
]

OPENER = "Let us break down this interaction."

WALK = [
    (0, None,
     "'Vika!' -- ENG He shouts her name across the busy restaurant floor."),
    (1, None,
     "'Yes, I am listening to you carefully.' -- ENG She crosses her arms and waits for his explanation."),
    (2, None,
     "'We need to talk urgently.' -- ENG He insists that they must have a private conversation."),
    (3, None,
     "'What urgent business do you have there?' -- ENG She asks what could possibly be so important."),
    (4, None,
     "'About which you cannot speak on the phone?' -- ENG She questions why he could not just call her."),
    (5, None,
     "'This is not for a telephone conversation.' -- ENG He explains that the matter is highly confidential."),
    (6, None,
     "'I am very busy right now.' -- ENG She tries to dismiss him and return to work."),
    (7, None,
     "'This is truly very important.' -- ENG He begs her to give him just a few minutes."),
    (8, None,
     "'Fine, what happened?' -- ENG She finally gives in and asks for the details."),
    (9, None,
     "'Just come with me.' -- ENG He refuses to explain and asks her to follow."),
    (10, None,
     "'Where are we going?' -- ENG She demands to know their mysterious destination."),
    (11, None,
     "'You will soon see everything yourself.' -- ENG He promises that all her questions will be answered."),
]

TRANSITION = "Now let us listen to the conversation again without interruption."
OUTRO = "Victoria reluctantly agrees to follow her boss, wondering what kind of problem he has created this time."
CLOSING = ("anja", "Ты скоро всё сама увидишь.")
