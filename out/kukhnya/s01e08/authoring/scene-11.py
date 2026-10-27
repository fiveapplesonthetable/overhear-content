"""s01e08 scene 11: Комплимент от шефа (A Compliment from the Chef)."""

ID = "kukhnya-s01e08-scene-11"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 8
SCENE = 11
TITLE = "Комплимент от шефа  (A Compliment from the Chef)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "elena": "anja"}
LABELS = {"anya": "Федя", "elena": "Елена"}
SOURCE_NAME = "Кухня (Kukhnya) S1.08"
SOURCE_FILE = "sources/kukhnya/s01/e08.ru.dual.srt"

INTRO = (
    "Acting as guest head chef for the day, Elena Sokolova observes fish specialist Fedya at his cooking station. "
    "She surprises the defensive line cook by offering expert praise for his frying technique, comparing his craft to the legendary Paul Bocuse in Lyon. "
    "Let's listen to their conversation in Russian first."
)

STORY = [
    ("elena", "Федя, скажите, вы случайно учились во Франции?",
     "Fedya, tell me, did you by chance study in France?",
     [(125, "Федя, вы учились во Франции")], "inquiring with genuine curiosity"),
    ("anya", "Делать мне больше нечего, чем учиться там!",
     "Like I had nothing better to do than study there!",
     [(126, "Дел с меня больше нечего")], "replying with gruff skepticism"),
    ("elena", "У вас просто потрясающая техника обжарки рыбы.",
     "You have simply amazing technique for frying fish.",
     [(127, "просто такую обжарку делают только в Лионе")], "praising his technique warmly"),
    ("anya", "Я просто жарю рыбу на горячей сковороде.",
     "I simply fry fish on a hot pan.",
     [], "downplaying his skills"),
    ("elena", "Такую обжарку делают только в Лионе у Бокюза.",
     "They only do such searing in Lyon at Bocuse's.",
     [(127, "только в Лионе у мэтра Бакёза")], "comparing him to a culinary legend"),
    ("anya", "Вы серьёзно сравниваете меня с французским мастером?",
     "Are you seriously comparing me to a French master?",
     [], "asking with mild disbelief"),
    ("elena", "Абсолютно серьёзно, у вас редкий природный дар.",
     "Absolutely seriously, you have a rare natural gift.",
     [(128, "у вас природный дар")], "affirming his natural talent"),
    ("anya", "Мне никогда раньше не говорили таких слов.",
     "Nobody ever told me such words before.",
     [], "confessing his touched feelings"),
    ("elena", "Настоящий талант всегда виден с первого взгляда.",
     "True talent is always visible at first sight.",
     [], "encouraging him with respect"),
    ("anya", "Спасибо большое за такую высокую оценку, шеф.",
     "Thank you very much for such high praise, Chef.",
     [], "thanking her respectfully"),
    ("elena", "Продолжайте готовить, гости будут в полном восторге.",
     "Continue cooking, the guests will be in complete delight.",
     [], "urging him to keep up the standard"),
    ("anya", "Обещаю сделать самое вкусное блюдо сегодня!",
     "I promise to make the most delicious dish today!",
     [], "committing to culinary excellence"),
]

OPENER = "Let's review this flattering kitchen exchange line by line."

WALK = [
    (0, None,
     "'Fedya, tell me, did you by chance study in France?' Elena begins with an inquiry about Fedya's culinary training."),
    (1, None,
     "'Like I had nothing better to do than study there!' Fedya dismisses the idea with gruff defensive skepticism."),
    (2, None,
     "'You have simply amazing technique for frying fish.' Elena praises his frying skills with genuine professional admiration."),
    (3, None,
     "'I simply fry fish on a hot pan.' Fedya downplays his technique as basic everyday kitchen routine."),
    (4, None,
     "'They only do such searing in Lyon at Bocuse's.' Elena compares his crust to elite French haute cuisine."),
    (5, None,
     "'Are you seriously comparing me to a French master?' Fedya is visibly touched by the flattering comparison."),
    (6, None,
     "'Absolutely seriously, you have a rare natural gift.' Elena reaffirms that his talent comes straight from nature."),
    (7, None,
     "'Nobody ever told me such words before.' Fedya confesses that Barinov rarely offers such gentle encouragement."),
    (8, None,
     "'True talent is always visible at first sight.' Elena emphasizes her respect for dedicated craftsmanship."),
    (9, None,
     "'Thank you very much for such high praise, Chef.' Fedya warmly expresses sincere gratitude to the visiting chef."),
    (10, None,
     "'Continue cooking, the guests will be in complete delight.' Elena urges him to keep up the stellar standard."),
    (11, None,
     "'I promise to make the most delicious dish today!' Fedya returns to his station with newfound professional pride."),
]

TRANSITION = "Now let's listen to the whole dialogue again at normal conversational speed."

OUTRO = (
    "Charmed by Elena's generous compliments, Fedya happily redoubles his efforts at the fish station. "
    "See you next time!"
)

CLOSING = ("anya", "Обещаю сделать самое вкусное блюдо сегодня!")
