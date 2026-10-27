ID = "kukhnya-s01e07-scene-02"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 7
SCENE = 2
TITLE = "Секретный жилец  (The Secret Resident)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "kostya": "anja"}
LABELS = {"anya": "Макс", "kostya": "Костя"}
SOURCE_NAME = "Кухня (Kukhnya) S1.07"
SOURCE_FILE = "sources/kukhnya/s01/e07.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 5-11. Kostya arrives early at Claude Monet and catches Max in casual clothes, "
    "discovering that Max has been secretly sleeping overnight in the restaurant."
)

INTRO = (
    "Arriving at Claude Monet well before his shift, Kostya finds Max wandering around in casual clothes "
    "instead of his chef uniform. Pressing him for answers, Kostya uncovers Max's shocking secret: "
    "to avoid Moscow's exorbitant rents, Max has been sleeping overnight in the restaurant dining room. "
    "Let's listen to their confrontation in Russian first."
)

STORY = [
    ("anya", "Костя, почему ты пришёл так рано?",
     "Kostya, why did you arrive so early?",
     [(5, "ты как так рано приперся")], "adapted"),
    ("kostya", "Сейчас уже восемь часов утра, Макс.",
     "It is already eight o'clock in the morning, Max.",
     [(6, "Не рано")], "adapted"),
    ("anya", "Я думал, что ресторан ещё закрыт.",
     "I thought that the restaurant was still closed.",
     [], "new"),
    ("kostya", "Почему ты ещё не надел форму?",
     "Why haven't you put on your uniform yet?",
     [(6, "Че не переоделся")], "adapted"),
    ("anya", "Мой ключ от шкафа лежит здесь.",
     "My locker key is lying here.",
     [(7, "А у меня ключ здесь")], "adapted"),
    ("kostya", "Тогда иди быстрее в раздевалку персонала.",
     "Then go faster to the staff locker room.",
     [(8, "Ну и вали переодеваться")], "adapted"),
    ("anya", "Не командуй мной, я всё успею.",
     "Do not boss me around, I will manage everything in time.",
     [(9, "Погоди, че ты меня строишь")], "adapted"),
    ("kostya", "Что ты вообще делал здесь ночью?",
     "What were you doing here at night at all?",
     [(9, "Че ты здесь делаешь")], "adapted"),
    ("anya", "Честно говоря, я живу прямо здесь.",
     "Honestly speaking, I live right here.",
     [(10, "Живу я здесь")], "adapted"),
    ("kostya", "Ты ночуешь в ресторане шефа Баринова?!",
     "You spend the night in Chef Barinov's restaurant?!",
     [(10, "Как так")], "adapted"),
    ("anya", "Да, я сплю на диване в зале.",
     "Yes, I sleep on the sofa in the dining room.",
     [(11, "Так, так")], "adapted"),
    ("kostya", "Если шеф узнает, он тебя убьёт!",
     "If the chef finds out, he will kill you!",
     [], "new"),
    ("anya", "Пожалуйста, не рассказывай никому мой секрет.",
     "Please do not tell anyone my secret.",
     [], "new"),
]

OPENER = "Now let's examine Kostya and Max's confrontation line by line."

WALK = [
    (0, None,
     "'Kostya, why did you arrive so early?' Max questions his coworker's sudden morning appearance."),
    (1, None,
     "'It is already eight o'clock in the morning, Max.' Kostya counters with a time statement."),
    (2, None,
     "'I thought that the restaurant was still closed.' Max explains his surprised reaction using a past verb."),
    (3, None,
     "'Why haven't you put on your uniform yet?' Kostya presses Max about his casual attire."),
    (4, None,
     "'My locker key is lying here.' Max gestures to his key with a present imperfective verb."),
    (5, None,
     "'Then go faster to the staff locker room.' Kostya urges haste with a comparative adverb and imperative."),
    (6, None,
     "'Do not boss me around, I will manage everything in time.' Max pushes back with a negative imperative."),
    (7, None,
     "'What were you doing here at night at all?' Kostya grows suspicious about Max's overnight presence."),
    (8, None,
     "'Honestly speaking, I live right here.' Max reveals his secret using a parenthetic adverbial phrase."),
    (9, None,
     "'You spend the night in Chef Barinov's restaurant?!' Kostya is astonished by his friend's audacity."),
    (10, None,
     "'Yes, I sleep on the sofa in the dining room.' Max admits where he spends the night with a present verb."),
    (11, None,
     "'If the chef finds out, he will kill you!' Kostya warns of Barinov's wrath using a conditional sentence."),
    (12, None,
     "'Please do not tell anyone my secret.' Max pleads for confidentiality with a negative imperative."),
]

TRANSITION = "Now let's listen to the confrontation again without interruption."
OUTRO = (
    "Terrified of what Chef Barinov would do if he caught a cook sleeping in the restaurant, "
    "Kostya considers how to help his friend out of this dangerous situation."
)
CLOSING = ("anya", "Пожалуйста, не рассказывай никому мой секрет.")
