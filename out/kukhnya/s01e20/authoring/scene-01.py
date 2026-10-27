ID = "kukhnya-s01e20-scene-01"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 20
SCENE = 1
TITLE = "Утро после  (The Morning After)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "vika": "anja"}
LABELS = {"anya": "Аня", "anton": "Антон", "max": "Макс"}
LABELS = {"anya": "Макс", "vika": "Вика"}
SOURCE_NAME = "Кухня (Kukhnya) S1.20"
SOURCE_FILE = "sources/kukhnya/s01/e20.ru.dual.srt"
SOURCE_NOTE = "Scene 1"

INTRO = "Vika prepares coffee in the morning while Max searches for his old watch. Max does not realize it is Vika's birthday. Let's listen closely to their exchange in Russian first, and then walk through each line together. Let's listen closely to their exchange in Russian first, and then walk through each line together."

STORY = [
    ("vika", "Я не буду отмечать день рождения.",
     "I will not celebrate my birthday.",
     [(32, 'не буду я отмечать')], "adapted"),
    ("vika", "И дарить мне ничего не надо.",
     "And there is no need to gift me anything.",
     [(34, 'дарить ничего не надо')], "adapted"),
    ("vika", "Может, мы просто посидим с Максом.",
     "Maybe we will just sit with Max.",
     [(36, 'с Максом просто посидим')], "adapted"),
    ("anya", "Я даже не знал про праздник.",
     "I did not even know about the holiday.",
     [], "new"),
    ("anya", "Я только проснулся.",
     "I just woke up.",
     [(39, 'проснулся')], "adapted"),
    ("vika", "А я уже кофе сварила.",
     "And I already brewed coffee.",
     [(41, 'кофе сварила')], "adapted"),
    ("anya", "Доброе утро, спасибо за кофе.",
     "Good morning, thank you for the coffee.",
     [(42, 'Доброе утро')], "adapted"),
    ("anya", "А ты часы мои не видела?",
     "And have you not seen my watch?",
     [(43, 'часы мои не видела')], "adapted"),
    ("vika", "А, ты вот про эти часы?",
     "Ah, you mean this watch?",
     [(44, 'ты вот про эти')], "adapted"),
    ("vika", "Может, тебе купить новые?",
     "Maybe buy you a new one?",
     [(45, 'тебе новые купить')], "adapted"),
    ("vika", "Эти часы уже еле ходят.",
     "This watch already barely works.",
     [(45, 'уже еле ходят')], "adapted"),
    ("anya", "Нет, это мой дедовский антиквариат.",
     "No, this is my grandfather's antique.",
     [(46, 'дедовский антиквариат')], "adapted"),
]

OPENER = "Let us break down this interaction."

WALK = [
    (0, None,
     "'I will not celebrate my birthday.' -- ENG She talks to her friend on the phone."),
    (1, None,
     "'And there is no need to gift me anything.' -- ENG She insists she does not want any presents."),
    (2, None,
     "'Maybe we will just sit with Max.' -- ENG She plans a quiet evening at home."),
    (3, None,
     "'I did not even know about the holiday.' -- ENG He is completely oblivious to the special occasion."),
    (4, None,
     "'I just woke up.' -- ENG He enters the kitchen feeling sleepy."),
    (5, None,
     "'And I already brewed coffee.' -- ENG She greets him with a warm morning drink."),
    (6, None,
     "'Good morning, thank you for the coffee.' -- ENG He appreciates her nice gesture."),
    (7, None,
     "'And have you not seen my watch?' -- ENG He starts looking around for his missing accessory."),
    (8, None,
     "'Ah, you mean this watch?' -- ENG She points to the old item on the table."),
    (9, None,
     "'Maybe buy you a new one?' -- ENG She suggests replacing the broken item."),
    (10, None,
     "'This watch already barely works.' -- ENG She points out that the accessory is practically useless."),
    (11, None,
     "'No, this is my grandfather's antique.' -- ENG He refuses to throw away his precious family heirloom."),
]

TRANSITION = "Now let us listen to the conversation again without interruption."
OUTRO = "Max remains completely unaware of Vika's special day, focusing only on his broken antique watch."
CLOSING = ("anya", "Нет, это мой дедовский антиквариат.")
