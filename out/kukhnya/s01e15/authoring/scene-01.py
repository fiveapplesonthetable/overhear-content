ID = "kukhnya-s01e15-scene-01"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 15
SCENE = 1
TITLE = "Новая жизнь втроём  (A New Life for Three)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "kostya": "anja"}
LABELS = {"anya": "Макс", "kostya": "Костя"}
SOURCE_NAME = "Кухня (Kukhnya) S1.15"
SOURCE_FILE = "sources/kukhnya/s01/e15.ru.dual.srt"
SOURCE_NOTE = "Cues 1-3. Nastya moves in, guys play video games."

INTRO = "Nastya moved in with Max and Kostya, but the guys still spend their time playing video games on the couch. Let's listen closely to their exchange in Russian first, and then walk through each line together."

STORY = [
    ("anya", "Неделю назад к нам переехала Настя.",
     "Nastya moved in with us a week ago.",
     [(1, "неделю назад к нам переехала")], "adapted"),
    ("kostya", "Да, теперь мы живём здесь втроём.",
     "Yes, now we live here as three.",
     [], "new"),
    ("anya", "Наша жизнь от этого почти не изменилась.",
     "Our life barely changed from that.",
     [(2, "наша жизнь от этого практически не изменилась")], "adapted"),
    ("kostya", "Мы всё так же играем вместе.",
     "We still play together just the same.",
     [], "new"),
    ("anya", "Костян, давай скорее, стреляй в них!",
     "Kostya, hurry up, shoot at them!",
     [(3, "Костян, давай скорее")], "adapted"),
    ("kostya", "Я выбираю своё новое оружие.",
     "I am choosing my new weapon.",
     [], "new"),
    ("anya", "Меня тут с трёх сторон окружили!",
     "They surrounded me from three sides here!",
     [(3, "меня тут с трех сторон")], "adapted"),
    ("kostya", "Держись, я уже бегу на помощь!",
     "Hold on, I am already running to help!",
     [], "new"),
    ("anya", "Отличная работа, это наша победа!",
     "Great work, this is our victory!",
     [], "new"),
    ("kostya", "Мы отличная команда в этой игре.",
     "We are a great team in this game.",
     [], "new"),
    ("anya", "Главное, чтобы Настя нам не мешала.",
     "The main thing is that Nastya does not disturb us.",
     [], "new"),
    ("kostya", "Она готовит вкусный ужин на кухне.",
     "She is cooking a tasty dinner in the kitchen.",
     [], "new"),
]

OPENER = "Let's break down this conversation."

WALK = [
    (0, None,
     "'Nastya moved in with us a week ago.' -- Max recalls when she came to live with them."),
    (1, None,
     "'Yes, now we live here as three.' -- Kostya agrees that they share the flat."),
    (2, None,
     "'Our life barely changed from that.' -- Max explains that routine is still the same."),
    (3, None,
     "'We still play together just the same.' -- Kostya points out their gaming habits on the sofa."),
    (4, None,
     "'Kostya, hurry up, shoot at them!' -- Max urges his friend to fire at the enemies."),
    (5, None,
     "'I am choosing my new weapon.' -- Kostya looks through his inventory of gear."),
    (6, None,
     "'They surrounded me from three sides here!' -- Max shouts that foes are pressing him."),
    (7, None,
     "'Hold on, I am already running to help!' -- Kostya rushes in to save his partner."),
    (8, None,
     "'Great work, this is our victory!' -- Max celebrates their joint success in the match."),
    (9, None,
     "'We are a great team in this game.' -- Kostya is happy with their joint victory."),
    (10, None,
     "'The main thing is that Nastya does not disturb us.' -- Max hopes that she lets them play in peace."),
    (11, None,
     "'She is cooking a tasty dinner in the kitchen.' -- Kostya mentions that she is busy with food."),
]

TRANSITION = "Now let's listen to the scene again without interruption."
OUTRO = "The boys finish their gaming session as Nastya continues cooking dinner in the kitchen."
CLOSING = ("kostya", "Она готовит вкусный ужин на кухне.")
