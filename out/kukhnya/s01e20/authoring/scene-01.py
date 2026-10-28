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

INTRO = "Vika prepares coffee in the morning while Max searches for his old watch. Max does not realize it is Vika's birthday. Let's listen closely to their exchange in Russian first, and then walk through each line together."

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
     "'I will not celebrate my birthday.' The little negative word sits right in front of the verb for 'will be', just like 'not' in English."),
    (1, None,
     "'And there is no need to gift me anything.' In Russian, 'to gift' leads into 'it is necessary' in a very natural everyday phrasing."),
    (2, None,
     "'Maybe we will just sit with Max.' The key word here means 'can', which Vika combines with 'we'."),
    (3, None,
     "'I did not even know about the holiday.' Notice the word order: 'I' comes first, and 'holiday' finishes the sentence."),
    (4, None,
     "'I just woke up.' The key word here means 'I', which Max combines with 'only'. Then Vika replies."),
    (5, None,
     "'And I already brewed coffee.' Vika puts 'I' up front so the listener immediately catches the tone, followed by 'already'."),
    (6, None,
     "'Good morning, thank you for the coffee.' Max puts 'good' up front so the listener immediately catches the tone, followed by 'morning'."),
    (7, None,
     "'And have you not seen my watch?' The '-a' on the end of the past-tense verb for 'saw' tells you the subject is feminine. And Vika jumps in."),
    (8, None,
     "'Ah, you mean this watch?' Russian leaves out 'am', 'is', or 'are' in the present tense, linking 'you' straight to 'watch'."),
    (9, None,
     "'Maybe buy you a new one?' The first content word means 'can', and 'new' rounds out the thought."),
    (10, None,
     "'This watch already barely works.' Vika starts with 'this' and pairs it with 'watch' to make the point clear. Max answers straight away."),
    (11, None,
     "'No, this is my grandfather's antique.' Russian leaves out 'am', 'is', or 'are' in the present tense, linking 'this' straight to 'antiques'."),
]

TRANSITION = "Now let us listen to the conversation again without interruption."
OUTRO = "Max remains completely unaware of Vika's special day, focusing only on his broken antique watch."
CLOSING = ("anya", "Нет, это мой дедовский антиквариат.")
