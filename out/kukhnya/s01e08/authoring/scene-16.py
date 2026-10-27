"""s01e08 scene 16: Возвращение Шефа (The Chef's Return)."""

ID = "kukhnya-s01e08-scene-16"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 8
SCENE = 16
TITLE = "Возвращение Шефа  (The Chef's Return)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "fedya": "angelina", "chef": "anja"}
LABELS = {"anya": "Сеня", "fedya": "Федя", "chef": "Шеф"}
SOURCE_NAME = "Кухня (Kukhnya) S1.08"
SOURCE_FILE = "sources/kukhnya/s01/e08.ru.dual.srt"
SOURCE_NOTE = "Cues 203-211. Senya and Fedya discuss their new female boss when Chef Barinov unexpectedly storms back into the kitchen."

INTRO = (
    "In the kitchen of Claude Monet, cooks Senya and Fedya casually debate the pros and cons of guest chef Elena Sokolova's polite management style. "
    "Their peaceful conversation is abruptly shattered when Chef Viktor Barinov storms in on crutches, furious and demanding absolute obedience. "
    "Let's listen to their sudden kitchen encounter in Russian."
)

STORY = [
    ("anya", "Ну, как тебе новый шеф-повар?", "Well, how do you like the new head chef?",
     [(203, "Ну и как тебе новый шеф")], ""),
    ("fedya", "Она кажется мне немного скучной.", "She seems a bit boring to me.",
     [(204, "какая-то она нудная")], ""),
    ("anya", "Зато она спокойная и вежливая.", "On the other hand she is calm and polite.",
     [(205, "Зато адекватная")], ""),
    ("fedya", "Это правда, она никогда не кричит.", "That is true, she never yells.",
     [(206, "Ну да, не то что этот")], ""),
    ("anya", "С ней на кухне тихо и приятно.", "With her the kitchen is quiet and pleasant.",
     [], ""),
    ("chef", "Бездельники! Огрызки! Что вы делаете?", "Slackers! Scraps! What are you doing?",
     [(207, "Гузки!"), (208, "Огрызки! Огрызки! Уничтожу!")], ""),
    ("chef", "Я вернулся навести полный порядок!", "I returned to restore complete order!",
     [(208, "Уничтожу!")], ""),
    ("fedya", "Шеф, мы просто чистили рыбу.", "Chef, we were just cleaning the fish.",
     [(210, "Ой, шеф, а мы это")], ""),
    ("anya", "Мы очень рады видеть вас!", "We are very glad to see you!",
     [], ""),
    ("chef", "Прекратите болтать и берите ножи!", "Stop chatting and take your knives!",
     [(209, "Раз, два, два!")], ""),
    ("chef", "Кто разрешил вам стоять без дела?", "Who permitted you to stand idle?",
     [], ""),
    ("fedya", "Мы сейчас всё нарежем, шеф.", "We will chop everything right now, chef.",
     [], ""),
    ("chef", "Быстро за работу, живо!", "Get to work quickly, lively!",
     [(211, "Да пошли вы")], ""),
]

OPENER = "Let's explore how Senya and Fedya's casual discussion of management styles is violently disrupted by Chef Barinov."

WALK = [
    (2, None,
     "'On the other hand she is calm and polite.' The coordinating conjunction contrasts an advantage against a previous mild criticism."),
    (3, None,
     "'That is true, she never yells.' A negative statement employing a negative adverb and an imperfective present verb."),
    (6, None,
     "'I returned to restore complete order!' The past tense perfective verb pairs with a purpose infinitive to express forceful intent."),
    (9, None,
     "'Stop chatting and take your knives!' Two imperative verbs command immediate cessation of talking and return to culinary duties."),
]

TRANSITION = "Now, let's hear the cooks reacting to Chef Barinov's chaotic arrival once more."

OUTRO = (
    "Now you know how to contrast workplace personalities and understand authoritative kitchen commands in Russian. "
    "Listen for these dramatic shifts in tone in the next scene."
)

CLOSING = ("anya", "Настоящий шеф снова с нами.")
