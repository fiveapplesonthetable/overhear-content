# domashniy-arest/s01e11/scene-31.py
ID = "domashniy-arest-s01e11-scene-31"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 11
SCENE = 31
TITLE = "Электронный браслет  (The Ankle Monitor)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Домашний арест, Сезон 1, Эпизод 11"
SOURCE_FILE = "sources/domashniy-arest/s01/e11.ru.dual.srt"
VOICES = {"narrator": "sky", "officer": "anja", "anya": "alisa"}
LABELS = {"officer": "Офицер", "anya": "Аркадий"}
INTRO = "Following his sudden return from freedom, former mayor Arkady Borisovich is escorted back to the communal apartment. An enforcement officer attaches the electronic tracking bracelet to his ankle, formally re-establishing house arrest."
STORY = [
    ("officer", "Аркадий Борисович, приготовьтесь к процедуре.", "Arkady Borisovich, prepare for the procedure.", [], "formal address"),
    ("anya", "Я готов, проходите в коридор.", "I am ready, come into the hallway.", [], "Arkady's compliance"),
    ("officer", "Это обязательная техническая процедура.", "This is a mandatory technical procedure.", [], "adapted cue"),
    ("anya", "Я уже носил этот электронный браслет.", "I already wore this electronic bracelet.", [], "Arkady's reminder"),
    ("officer", "Мы должны зафиксировать датчик на ноге.", "We must fasten the sensor on your leg.", [], "officer's instruction"),
    ("anya", "Пожалуйста, не затягивайте ремень слишком сильно.", "Please do not tighten the strap too tightly.", [], "Arkady's polite request"),
    ("officer", "Всё готово, электронный браслет работает.", "Everything is ready, the electronic bracelet is working.", [(920, 'Браслет работает.')], "adapted cue"),
    ("officer", "Дальше вы всё прекрасно знаете сами.", "You know everything very well yourself from here.", [(921, 'Дальше вы знаете.')], "adapted cue"),
    ("anya", "Я помню все установленные законом правила.", "I remember all the rules established by law.", [], "Arkady's assurance"),
    ("officer", "Вам строго запрещено покидать эту квартиру.", "You are strictly forbidden from leaving this apartment.", [], "official warning"),
    ("anya", "Я буду сидеть дома и ждать суда.", "I will sit at home and wait for the trial.", [], "Arkady's resignation"),
    ("officer", "Любое нарушение сигнала фиксируется немедленно.", "Any breach of signal is recorded immediately.", [], "enforcement rule"),
    ("anya", "Я не собираюсь никуда убегать.", "I do not intend to run away anywhere.", [], "Arkady's commitment"),
    ("officer", "Тогда соблюдайте режим и не нарушайте.", "Then observe the regime and do not violate.", [], "officer's farewell"),
]
OPENER = "Let's examine how the officer reinstates Arkady's electronic house arrest."
WALK = [
    (0, None, "'Arkady Borisovich, prepare for the procedure.' A formal administrative command using the patronymic."),
    (1, None, "'I am ready, come into the hallway.' Arkady courteously invites the officer into the residence."),
    (2, None, "'This is a mandatory technical procedure.' Official bureaucratic terminology explaining the fitting."),
    (3, None, "'I already wore this electronic bracelet.' Arkady notes his familiarity with the tracking device."),
    (4, None, "'We must fasten the sensor on your leg.' The officer describes the physical installation process."),
    (5, None, "'Please do not tighten the strap too tightly.' A polite negative command asking for physical comfort."),
    (6, None, "'Everything is ready, the electronic bracelet is working.' Confirmation that the monitoring signal is active."),
    (7, None, "'You know everything very well yourself from here.' An acknowledgment of the prisoner's prior experience."),
    (8, None, "'I remember all the rules established by law.' A formal confirmation of legal compliance."),
    (9, None, "'You are strictly forbidden from leaving this apartment.' A direct statement of the core house arrest restriction."),
    (10, None, "'I will sit at home and wait for the trial.' Arkady expresses his passive acceptance of detention."),
    (11, None, "'Any breach of signal is recorded immediately.' A warning highlighting automated electronic surveillance."),
    (12, None, "'I do not intend to run away anywhere.' Arkady disclaims any intention to attempt escape."),
    (13, None, "'Then observe the regime and do not violate.' A final standard police instruction ordering good behavior."),
]
TRANSITION = "Now let's listen to the formal electronic tagging procedure once more."
OUTRO = "With the electronic cuff secured around his ankle, Arkady returns to his familiar confinement. See you next time!"
CLOSING = ("officer", "Пока!")
