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
     "'One hundred sixty over ninety.' — Notice the numeral meaning 'a hundred' paired with the noun for 'sixty'."),
    (1, None,
     "'Viktor Petrovich, this is not a joke.' — Notice the proper name meaning 'Viktor' paired with the proper name for 'Petrovich'."),
    (2, None,
     "'Such pressure is very dangerous.' — Notice the pronoun meaning '(what) on earth' paired with the noun for 'blood pressure'."),
    (3, None,
     "'Yes, everything will be fine.' — Notice the det meaning 'everything' paired with the verb for 'will be'."),
    (4, None,
     "'Any stress and it will be bad.' — Notice the adjective meaning 'any' paired with the noun for 'stress'."),
    (5, None,
     "'Hi, Mom.' — Notice the interjection meaning 'hi' paired with the noun for 'mum, mother'."),
    (6, None,
     "'How was your workday?' — Notice the adverb meaning 'how' paired with the verb for 'passed'."),
    (7, None,
     "'Fine, they fired me.' — Notice the adverb meaning 'fine, OK' paired with the pronoun for 'me'."),
    (8, None,
     "'Not fired, but demoted.' — Notice the verb meaning 'to fire, to dismiss' paired with the noun for 'demote, lower'."),
    (9, None,
     "'Mom, I am not guilty of anything.' — Notice the noun meaning 'mum, mother' paired with the pronoun for 'I'."),
    (10, None,
     "'You must know how to answer for your actions.' — Notice the adverb meaning 'it is necessary' paired with the verb for 'to know how'."),
    (11, None,
     "'Thank you for the support, Mom.' — Notice the interjection meaning 'thank you' paired with the pronoun for 'for you, to you'."),
]

TRANSITION = "Now let us listen to the conversation once again."
OUTRO = "The conversation concludes the matter at hand."
CLOSING = ("anya", "Спасибо тебе за поддержку, мама.")
