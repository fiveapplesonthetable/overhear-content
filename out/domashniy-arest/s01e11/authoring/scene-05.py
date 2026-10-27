ID = "domashniy-arest-s01e11-scene-05"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 11
SCENE = 5
TITLE = "Неожиданная новость Илоны  (Ilona's Unexpected News)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "samson": "anja", "ilona": "angelina"}
LABELS = {"anya": "Аркадий", "samson": "Самсон", "ilona": "Илона"}
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.11"
SOURCE_FILE = "sources/domashniy-arest/s01/e11.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 84-104. Back in the present, Arkady and Samsonov look at online photos of Nina and Danya on vacation. "
    "Samsonov is furious, but Arkady tries to calm him down. Suddenly, Ilona rushes in with shocking news: President Putin is visiting Sineozersk."
)

INTRO = (
    "In this scene, Samsonov and Arkady are in the communal flat examining painful social media photos of Nina vacationing with her new lover. "
    "Ivan is enraged and threatens violence, but Arkady urges him to focus on the mayoral campaign instead. "
    "Their argument is interrupted by Ilona, who bursts through the door bursting with excitement to deliver game-changing political news. "
    "Let's listen to their conversation in Russian first."
)

STORY = [
    ("samson", "Посмотри, что они там творят!",
     "Look at what they are doing over there!",
     [(84, "смотри, что творит")], ""),
    ("samson", "Они выложили фотографию прямо из душа.",
     "They posted a photo straight from the shower.",
     [(87, "Мы в душе")], ""),
    ("samson", "Я пойду и переломаю ему кости!",
     "I will go and break his bones!",
     [(91, "Надо пойти ему кости переломать")], ""),
    ("anya", "Самсон, успокойся и не накручивай себя.",
     "Samson, calm down and don't wind yourself up.",
     [(92, "Да не накручивай себя, Самсон")], ""),
    ("anya", "Ты скоро выиграешь выборы и станешь мэром.",
     "You will soon win the election and become mayor.",
     [(93, "Ты мэром станешь")], ""),
    ("anya", "У тебя будет сто таких женщин!",
     "You will have a hundred such women!",
     [(93, "у тебя сто таких нин будет")], ""),
    ("ilona", "Привет всем! Что вы тут грустите?",
     "Hello everyone! Why are you sad here?",
     [(97, "Привет")], ""),
    ("samson", "Илона, почему ты такая радостная сегодня?",
     "Ilona, why are you so joyful today?",
     [(101, "А ты чего такая радостная")], ""),
    ("ilona", "У меня есть одна важная новость.",
     "I have one important piece of news.",
     [(102, "есть одна маленькая")], ""),
    ("anya", "И какая же у тебя новость?",
     "And what news do you have?",
     [(103, "Чего")], ""),
    ("ilona", "К нам в город приезжает президент!",
     "The president is coming to our town!",
     [(103, "Какой еще Путин")], ""),
    ("samson", "Президент? Ты говоришь совершенно серьёзно?",
     "The president? Are you speaking completely seriously?",
     [], ""),
    ("ilona", "Да, сам президент едет к нам!",
     "Yes, the president himself is coming to us!",
     [(104, "Тот самый")], ""),
]

OPENER = "Now let's examine the dramatic argument and unexpected revelation line by line."

WALK = [
    (0, None,
     "'Look at what they are doing over there!' Samson reacts with outrage using a vivid colloquial verb."),
    (1, None,
     "'They posted a photo straight from the shower.' The plural past verb describes an online provocation."),
    (2, None,
     "'I will go and break his bones!' Samson threatens physical revenge using future perfective verbs."),
    (3, None,
     "'Samson, calm down and don't wind yourself up.' Arkady urges emotional restraint using a reflexive imperative."),
    (4, None,
     "'You will soon win the election and become mayor.' Arkady refocuses Ivan on the political campaign."),
    (5, None,
     "'You will have a hundred such women!' The cardinal numeral governs the genitive plural adjective phrase."),
    (6, None,
     "'Hello everyone! Why are you sad here?' Ilona enters breezily, mocking their gloomy mood."),
    (7, None,
     "'Ilona, why are you so joyful today?' Samson grumbles at her joyful demeanor with a short adjective."),
    (8, None,
     "'I have one important piece of news.' Ilona teases her announcement with a genitive construction."),
    (9, None,
     "'And what news do you have?' Arkady asks with curiosity using an interrogative pronoun."),
    (10, None,
     "'The president is coming to our town!' Ilona drops the bombshell using a directional motion verb."),
    (11, None,
     "'The president? Are you speaking completely seriously?' Samson reacts in shock with a modal adverb."),
    (12, None,
     "'Yes, the president himself is coming to us!' Ilona confirms the visit with an emphatic pronoun."),
]

TRANSITION = "Now let's listen to the revelation of Putin's visit once more without pauses."
OUTRO = (
    "Ilona's unexpected announcement changes everything for Arkady's political ambitions. "
    "In the next scene, the campaign team scrambles to verify the news and prepare for the presidential visit."
)
CLOSING = ("ilona", "Да, сам президент едет к нам!")
