"""Scene 05 — Arriving Late (s01e13)."""

ID = "kukhnya-s01e13-scene-05"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 13
SCENE = 5
TITLE = "Опоздание Макса  (Max's Tardiness)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Кухня (Kukhnya) S1.13"
SOURCE_FILE = "sources/kukhnya/s01/e13.ru.dual.srt"

VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "kostya": "anja",
    "guest": "angelina",
}

LABELS = {
    "anya": "Вика",
    "kostya": "Макс",
    "guest": "Шеф",
}

INTRO = (
    "Max arrives late to the kitchen, claiming he just overslept. The Chef immediately "
    "punishes him with warehouse duty and asks Victoria for her opinion."
)

STORY = [
    ("kostya", "Привет всем.",
     "Hi to everyone.",
     [(64, "Привет всем.")], "Max walks in nervously"),

    ("kostya", "Шеф, извините, я просто проспал.",
     "Boss, excuse me, I simply overslept.",
     [(66, "Шеф, извините."), (71, "Я просто проспал.")], "Max apologizes to the Chef"),

    ("kostya", "Больше такое не повторится.",
     "Such a thing will not happen again.",
     [(72, "больше такое не повторится.")], "Max promises earnestly"),

    ("guest", "Сегодня ты работаешь на складе.",
     "Today you are working in the stockroom.",
     [(74, "Сегодня работаешь на складе.")], "Chef assigns the punishment"),

    ("guest", "Ещё раз проспишь — я тебя уволю.",
     "Oversleep one more time — I will fire you.",
     [(74, "А еще раз проспишу волю.")], "Chef warns him sternly"),

    ("kostya", "Но шеф, я отличный повар.",
     "But boss, I am an excellent cook.",
     [], "Max complains"),

    ("guest", "Повар должен приходить на работу вовремя.",
     "A cook must arrive at work on time.",
     [], "Chef yells back"),

    ("kostya", "Я обещаю больше никогда не опаздывать.",
     "I promise to never be late again.",
     [], "Max pleads"),

    ("guest", "Я сказал своё слово.",
     "I have said my word.",
     [], "Chef ends the discussion"),

    ("guest", "Виктория Сергеевна, почему вы так молчите?",
     "Victoria Sergeyevna, why are you so silent?",
     [(76, "Виктория Сергеевна, вы почему молчите?")], "Chef turns to Vika"),

    ("anya", "Надо раньше ложиться спать, чтобы не проспать.",
     "It is necessary to go to bed earlier to not oversleep.",
     [(78, "Ложиться надо раньше, чтобы не проспать.")], "Vika smiles subtly"),

    ("guest", "Вот видите, она со мной согласна.",
     "Here you see, she agrees with me.",
     [], "Chef points at Vika"),
]

OPENER = "Let's join the kitchen staff as Max finally arrives to work."

WALK = [
    (0, None,
     "'Hi to everyone.' Max enters the busy kitchen looking slightly guilty."),
    (1, None,
     "'Boss, excuse me, I simply overslept.' He quickly offers an excuse for his lateness."),
    (2, None,
     "'Such a thing will not happen again.' Max tries to sound very responsible and serious."),
    (3, None,
     "'Today you are working in the stockroom.' The Chef does not hesitate to discipline him."),
    (4, None,
     "'Oversleep one more time — I will fire you.' The Chef delivers a final harsh warning."),
    (5, None,
     "'But boss, I am an excellent cook.' Max feels his punishment is too severe."),
    (6, None,
     "'A cook must arrive at work on time.' The Chef reminds him about basic professional discipline."),
    (7, None,
     "'I promise to never be late again.' Max begs for another chance in the kitchen."),
    (8, None,
     "'I have said my word.' The stubborn Chef refuses to change his strict decision."),
    (9, None,
     "'Victoria Sergeyevna, why are you so silent?' He asks the manager to back him up."),
    (10, None,
     "'It is necessary to go to bed earlier to not oversleep.' Vika gives a very ironic piece of advice."),
    (11, None,
     "'Here you see, she agrees with me.' The Chef feels completely justified in his harsh punishment."),
]

TRANSITION = "Now let's listen to the Chef reprimand Max once again."

OUTRO = "Sent to the stockroom for the day, Max learns that arriving late has immediate consequences."

CLOSING = ("guest", "Вот видите, она со мной согласна.")
