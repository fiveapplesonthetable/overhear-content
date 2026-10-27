"""s01e04 scene 12: Чистосердечное признание (A Full Confession)."""

ID = "kukhnya-s01e04-scene-12"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 4
SCENE = 12
TITLE = "Чистосердечное признание  (A Full Confession)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "chef": "anja"}
LABELS = {"anya": "Сеня", "chef": "Шеф"}
SOURCE_NAME = "Кухня (Kukhnya) S1.04"
SOURCE_FILE = "sources/kukhnya/s01/e04.ru.dual.srt"
SOURCE_NOTE = "Cues 146-156. Senya breaks down on the lie detector and confesses to all his kitchen thefts."

INTRO = (
    "Terrified of the lie detector machine in Barinov's office, line cook Senya completely breaks down before the sensors are even attached. "
    "Instead of answering questions about rival restaurant Arcobaleno, Senya frantically confesses to every scrap of food he ever pilfered from the kitchen. "
    "Let's listen to his hilarious confession in Russian first."
)

STORY = [
    ("anya", "Шеф, пожалуйста, не включайте прибор!",
     "Chef, please, do not turn on the device!",
     [(146, "Шеф, пожалуйста")], "panicking in the chair"),
    ("chef", "Ты чего так сильно дрожишь?",
     "Why are you shaking so hard?",
     [], "observing his trembling"),
    ("anya", "Я сам вам всё честно расскажу!",
     "I will tell you everything honestly myself!",
     [(146, "Я все расскажу")], "offering a full confession"),
    ("anya", "Эту рыбу после банкета взял я!",
     "I took that fish after the banquet!",
     [(147, "Эту рыбу"), (147, "после банкета, я взял")], "admitting the first theft"),
    ("anya", "И ту оленину тоже унёс я!",
     "And I took that venison away too!",
     [(148, "И ту оленину"), (148, "тоже я унес")], "confessing to the meat"),
    ("chef", "А полкило дорогой икры?",
     "And half a kilo of expensive caviar?",
     [(149, "А полкило икры")], "checking missing inventory"),
    ("anya", "Нет, шеф, икру я не брал!",
     "No, Chef, I did not take the caviar!",
     [(150, "Нет")], "drawing the line"),
    ("anya", "Простите меня, пожалуйста, шеф!",
     "Forgive me, please, Chef!",
     [(151, "Простите меня, шеф")], "pleading desperately"),
    ("chef", "Мне плевать на твою оленину!",
     "I do not care about your venison!",
     [], "dismissing the petty thefts"),
    ("chef", "Ты ходил в соседний ресторан?",
     "Did you go to the neighboring restaurant?",
     [(152, "Это ты ходил в соседний ресторан")], "asking the real question"),
    ("anya", "Нет, шеф, клянусь вам!",
     "No, Chef, I swear to you!",
     [(153, "Нет")], "swearing his loyalty"),
    ("chef", "Говори правду, да или нет?",
     "Tell the truth, yes or no?",
     [(156, "говори, да или нет")], "demanding binary answer"),
    ("anya", "Нет! Я предан только вам!",
     "No! I am loyal only to you!",
     [(154, "Нет")], "reasserting devotion"),
]

OPENER = "Let's replay a few lines to examine key phrases and vocabulary."

WALK = [
    (0, "Шеф, пожалуйста, не включайте прибор!",
     "'Chef, please, do not turn on the device!' Senya begs, sweating profusely before the machine is even attached."),
    (3, "Эту рыбу после банкета взял я!",
     "'I took that fish after the banquet!' the line cook confesses, voluntarily admitting to kitchen pilfering."),
    (5, "А полкило дорогой икры?",
     "'And half a kilo of expensive caviar?' Chef Barinov presses, seizing the chance to uncover other thefts."),
    (9, "Ты ходил в соседний ресторан?",
     "'Did you go to the neighboring restaurant?' Barinov demands, ignoring the petty food thefts to find the real secret."),
]

TRANSITION = "Now listen to the full office confession once more."

OUTRO = "Barinov stares in disbelief at his sobbing cook before deciding what to do next."

CLOSING = ("anya", "Больше я никогда ничего не украду.")
