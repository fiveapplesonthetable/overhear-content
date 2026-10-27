ID = "kukhnya-s01e13-scene-11"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 13
SCENE = 11
TITLE = "Мусорные баки  (The Trash Bins)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "elena": "anja", "timur": "angelina"}
LABELS = {"anya": "Виктор Петрович", "elena": "Елена", "timur": "Тимур"}
SOURCE_NAME = "Кухня (Kukhnya) S1.13"
SOURCE_FILE = "sources/kukhnya/s01/e13.ru.dual.srt"
SOURCE_NOTE = "Cues 145-160. Chef Barinov and Elena argue about the trash bins and Timur the supplier."

INTRO = "Outside the restaurant, Chef Viktor Petrovich is arguing with the rival chef Elena about the trash bins. Let's listen to their confrontation in Russian first."

STORY = [
    ("anya", "С одной вашей мусоркой я справился.", "I handled one of your trash bins.", [(145, "С одной вашей мусоркой справился")], "added я"),
    ("elena", "Вот документ, который это подтверждает.", "Here is a document that proves it.", [(147, "Вот, кстати, документ, который это подтверждает.")], "removed кстати"),
    ("elena", "Это план из управы.", "This is the plan from the district office.", [(148, "Это план из управы")], ""),
    ("elena", "Баки должны стоять именно в этом месте.", "The bins must stand exactly in this place.", [(148, "баки должны стоять именно вот в этом"), (149, "месте.")], "adapted"),
    ("elena", "Вопросы ко мне есть еще?", "Are there any more questions for me?", [(149, "Вопросы ко мне есть еще?")], ""),
    ("anya", "Тимур? Ты решил поставлять ей продукты?", "Timur? You decided to supply her with food?", [(152, "Тимур?"), (156, "будешь ей поставлять продукты")], "adapted"),
    ("timur", "Виктор Петрович, моё почтение.", "Viktor Petrovich, my respects.", [(153, "Виктор Петрович, мое почтение.")], "added ё"),
    ("anya", "Учти, я долг не верну.", "Keep in mind, I will not return the debt.", [(156, "учти,"), (156, "долг не верну.")], "added я"),
    ("timur", "Извините, наше сотрудничество подошло к концу.", "Excuse me, our cooperation has come to an end.", [(157, "Извините,"), (157, "наше сотрудничество подошло к концу.")], "removed к сожалению"),
    ("timur", "Я не могу перечить старшему.", "I cannot contradict an older man.", [(158, "не могу перечить старшему")], "added я"),
    ("timur", "Тем более, вы должны мне пятнадцать тысяч.", "Especially since you owe me fifteen thousand.", [(158, "тем более,"), (159, "у меня торчит 15 штук.")], "adapted to formal numbers"),
    ("anya", "Десять.", "Ten.", [(160, "Десять.")], "")
]

OPENER = "Now let's examine their argument line by line."

WALK = [
    (0, None, "'I handled one of your trash bins.' -- The stubborn Chef refuses to surrender the territory."),
    (1, None, "'Here is a document that proves it.' -- Elena presents official papers to win the argument."),
    (2, None, "'This is the plan from the district office.' -- She relies on local government regulations."),
    (3, None, "'The bins must stand exactly in this place.' -- The rival chef points at the pavement."),
    (4, None, "'Are there any more questions for me?' -- Elena smiles with smug satisfaction at him."),
    (5, None, "'Timur? You decided to supply her with food?' -- Viktor Petrovich notices his supplier nearby."),
    (6, None, "'Viktor Petrovich, my respects.' -- The supplier greets the angry chef nervously."),
    (7, None, "'Keep in mind, I will not return the debt.' -- Barinov immediately threatens his business partner."),
    (8, None, "'Excuse me, our cooperation has come to an end.' -- Timur politely declines Elena's business offer."),
    (9, None, "'I cannot contradict an older man.' -- He explains his respect for the old chef."),
    (10, None, "'Especially since you owe me fifteen thousand.' -- He reminds Barinov about his massive debt."),
    (11, None, "'Ten.' -- The Chef immediately corrects the financial numbers.")
]

TRANSITION = "Now let's listen to the street confrontation without interruption."
OUTRO = "Timur stays loyal to Viktor Petrovich, mostly because he still wants his money back. The restaurant war continues!"
CLOSING = ("anya", "Десять.")
