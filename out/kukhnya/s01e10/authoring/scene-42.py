"""Scene 42 — The Pike Roe Scam (s01e10, 00:21:21–00:21:58)."""

ID = "kukhnya-s01e10-scene-42"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 10
SCENE = 42
TITLE = "Щучья афера  (The Pike Roe Scam)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Кухня (Kukhnya) S1.10"
SOURCE_FILE = "sources/kukhnya/s01/e10.ru.dual.srt"

VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "chef": "anja",
}

LABELS = {
    "anya": "Нагиев",
    "chef": "Шеф",
}

INTRO = (
    "Pressed by Nagiyev, Chef Barinov finally confesses that the supposed sturgeon caviar is dyed pike roe. "
    "Furious at the reckless risk to the restaurant's reputation, Nagiyev imposes a crushing fine on the head chef."
)

STORY = [
    ("chef", "Ладно, это обычная щучья икра, Дим.",
     "Fine, it is ordinary pike roe, Dim.",
     [(299, "Щучья.")], "Chef confesses"),

    ("chef", "Учёные говорят, что она даже полезнее чёрной!",
     "Scientists say it is even healthier than black!",
     [(300, "Ученые говорят, что она даже полезнее.")], "Chef argues"),

    ("chef", "Извини, мы не смогли достать нормальную вовремя.",
     "Sorry, we could not get decent one in time.",
     [(301, "Ну, извини, Дим, не смогли достать нормальную.")], "Chef apologizes"),

    ("chef", "Поэтому я решил немного покрасить её.",
     "Therefore I decided to dye it a little.",
     [(302, "Ну, я подумал, что если так...")], "Chef explains dyed roe"),

    ("anya", "Если твоя афера всплывёт, тебя просто убьют!",
     "If your scam surfaces, they will simply kill you!",
     [(303, "Если твоя афера всплывет, тебя, скорее всего, убьют.")], "Nagiyev warns"),

    ("anya", "Тебя убьют и закопают в лесу.",
     "They will kill you and bury you in the woods.",
     [(304, "Убьют и закопают.")], "Nagiyev predicts grim fate"),

    ("anya", "Я даже не буду плакать на могиле.",
     "I will not even weep at your grave.",
     [(304, "Я даже не буду плакать на твоей могиле.")], "Nagiyev adds"),

    ("anya", "А если не всплывёт, ты настоящий везунчик.",
     "And if it does not surface, you are a real lucky guy.",
     [(305, "Если не всплывет, ты везунок.")], "Nagiyev continues"),

    ("anya", "Ты будешь целый месяц работать без зарплаты!",
     "You will work an entire month without salary!",
     [(306, "Ты просто будешь работать месяц без зарплаты.")], "Nagiyev announces penalty"),

    ("anya", "Я штрафую тебя на двести тысяч рублей.",
     "I am fining you two hundred thousand rubles.",
     [(307, "Я тебя штрафую на двести тысяч.")], "Nagiyev states fine"),

    ("chef", "Серьёзно? На что я буду жить месяц?!",
     "Seriously? On what will I live for a month?!",
     [(308, "Серьезно? Да. А как же я буду жить этот месяц?")], "Chef panics"),

    ("anya", "Всё, иди на кухню и не зли!",
     "That is all, go to the kitchen and do not anger me!",
     [(309, "Все, иди. Не зли меня.")], "Nagiyev dismisses"),

    ("chef", "Слушаюсь, шеф, то есть Дмитрий Владимирович.",
     "Yes sir, chef, I mean Dmitry Vladimirovich.",
     [], "Chef slinks off"),
]

OPENER = "Let's explore Barinov's confession about the dyed pike roe and Nagiyev's furious disciplinary punishment."

WALK = [
    (0, None,
     "'Fine, it is ordinary pike roe, Dim.' Barinov finally drops the charade and admits the truth."),
    (1, None,
     "'Scientists say it is even healthier than black!' The chef tries a nutritional defense."),
    (2, None,
     "'Sorry, we could not get decent one in time.' Barinov cites delivery failures for the scam."),
    (3, None,
     "'Therefore I decided to dye it a little.' The chef reveals his secret culinary trick."),
    (4, None,
     "'If your scam surfaces, they will simply kill you!' Nagiyev points out the grave danger."),
    (5, None,
     "'They will kill you and bury you in the woods.' The owner paints a terrifying picture of revenge."),
    (6, None,
     "'I will not even weep at your grave.' Nagiyev underscores his lack of sympathy."),
    (7, None,
     "'And if it does not surface, you are a real lucky guy.' Nagiyev offers small comfort."),
    (8, None,
     "'You will work an entire month without salary!' Nagiyev hands down a painful penalty."),
    (9, None,
     "'I am fining you two hundred thousand rubles.' The restaurant owner names the stiff financial penalty."),
    (10, None,
     "'Seriously? On what will I live for a month?!' Barinov gasps at the severe financial loss."),
    (11, None,
     "'That is all, go to the kitchen and do not anger me!' Nagiyev cuts the discussion short."),
    (12, None,
     "'Yes sir, chef, I mean Dmitry Vladimirovich.' Barinov quickly obeys and heads back inside."),
]

TRANSITION = "Now let's listen to the heated confrontation over the dyed caviar and penalty once more."

OUTRO = "Facing a massive deduction and living on edge, Barinov hurries back to the kitchen to see through the banquet service."

CLOSING = ("chef", "Слушаюсь, шеф, то есть Дмитрий Владимирович.")
