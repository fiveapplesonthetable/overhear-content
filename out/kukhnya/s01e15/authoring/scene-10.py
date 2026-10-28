ID = "kukhnya-s01e15-scene-10"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 15
SCENE = 10
TITLE = "Высокое давление  (High Blood Pressure)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "leva": "anja", "guest": "angelina"}
LABELS = {'anya': 'Лёва', 'leva': 'Виктор', 'guest': 'Мама'}
SOURCE_NAME = "Кухня (Kukhnya) S1.15"
SOURCE_FILE = "sources/kukhnya/s01/e15.ru.dual.srt"
SOURCE_NOTE = "Cues."

INTRO = (
    "Leva measures Chef Victor's blood pressure and finds it dangerously high. He warns Victor about the risks. Meanwhile, Leva also talks to his mother on the phone about his stressful demotion. Let us listen to their conversation in Russian first."
)

STORY = [
    ("anya", "Сто шестьдесят на девяносто.",
     "One hundred sixty over ninety.",
     [(172, '160 на 90.')], "adapted"),
    ("anya", "Виктор Петрович, это не шутки.",
     "Viktor Petrovich, this is not a joke.",
     [(173, 'Виктор Петрович, это не шутки.')], "adapted"),
    ("anya", "Такое давление — это очень опасно.",
     "Such pressure is very dangerous.",
     [(174, 'Такое давление — это буревестник инфаркта.')], "adapted"),
    ("leva", "Да, всё будет хорошо.",
     "Yes, everything will be fine.",
     [], "new"),
    ("anya", "Любой стресс и будет плохо.",
     "Any stress and it will be bad.",
     [(175, 'Да, какой-нибудь стресс и…')], "adapted"),
    ("anya", "Привет, мама.",
     "Hi, Mom.",
     [(176, 'Привет, мам. Привет.')], "adapted"),
    ("guest", "Как прошёл твой рабочий день?",
     "How was your workday?",
     [(177, 'Как прошел рабочий день?')], "adapted"),
    ("anya", "Нормально, меня уволили.",
     "Fine, they fired me.",
     [(178, 'Нормально. Меня уволили.')], "adapted"),
    ("guest", "Не уволили, а понизили.",
     "Not fired, but demoted.",
     [(179, 'Не уволили, а понизили в воспитательных целях.')], "adapted"),
    ("anya", "Мама, я ни в чём не виноват.",
     "Mom, I am not guilty of anything.",
     [(181, 'За опоздание. Мама, я не виноват.')], "adapted"),
    ("guest", "Надо уметь отвечать за свои поступки.",
     "You must know how to answer for your actions.",
     [(184, 'Нет-нет-нет. Надо уметь отвечать за свои поступки.')], "adapted"),
    ("anya", "Спасибо тебе за поддержку, мама.",
     "Thank you for the support, Mom.",
     [(186, 'Спасибо тебе, мама, за поддержку.')], "adapted"),
]

OPENER = "Now let us examine the conversation line by line."

WALK = [
    (0, None,
     "'One hundred sixty over ninety.' Russian leaves out 'am', 'is', or 'are' in the present tense, linking 'a hundred' straight to 'ninety'."),
    (1, None,
     "'Viktor Petrovich, this is not a joke.' — Notice the proper name meaning 'Viktor' paired with the proper name for 'Petrovich'."),
    (2, None,
     "'Such pressure is very dangerous.' Here 'on earth' sets up the idea, while 'dangerous' comes at the end for emphasis."),
    (3, None,
     "'Yes, everything will be fine.' Viktor starts with 'will be' and pairs it with 'good' to make the point clear."),
    (4, None,
     "'Any stress and it will be bad.' Lyova puts 'any' up front so the listener immediately catches the tone, followed by 'stress'."),
    (5, None,
     "'Hi, Mom.' Lyova starts with 'hi' and pairs it with 'mum' to make the point clear."),
    (6, None,
     "'How was your workday?' Notice the word order: 'how' comes first, and 'day' finishes the sentence."),
    (7, None,
     "'Fine, they fired me.' In Russian, 'fine' leads into 'to fire' in a very natural everyday phrasing."),
    (8, None,
     "'Not fired, but demoted.' the speaker puts 'to fire' up front so the listener immediately catches the tone, followed by 'demote'."),
    (9, None,
     "'Mom, I am not guilty of anything.' A compact expression built around 'mum' and 'at fault'."),
    (10, None,
     "'You must know how to answer for your actions.' The first content word means 'it is necessary', and 'actions' rounds out the thought. Lyova answers straight away."),
    (11, None,
     "'Thank you for the support, Mom.' The key word here means 'thank you', which Lyova combines with 'for you'."),
]

TRANSITION = "Now let us listen to the conversation once again."
OUTRO = "And that's it for this scene. When you watch the episode, listen out for the exchange around high blood pressure, and for the words meaning 'sixty' and 'ninety'. You'll catch them now. See you next time."
CLOSING = ("anya", "Спасибо тебе за поддержку, мама.")
