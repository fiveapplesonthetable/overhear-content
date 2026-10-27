"""s01e13 scene 18: Тайны персонала (Staff Secrets)."""

ID = "kukhnya-s01e13-scene-18"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 13
SCENE = 18
TITLE = "Тайны персонала  (Staff Secrets)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "max": "anja"}
LABELS = {"anya": "Вика", "max": "Макс"}
SOURCE_NAME = "Кухня (Kukhnya) S1.13"
SOURCE_FILE = "sources/kukhnya/s01/e13.ru.dual.srt"
SOURCE_NOTE = "Cues 253-254. Victoria returns to Max's room furious that Nastya saw her, accusing him of ruining her reputation before they leave for work."

INTRO = (
    "Returning to Max's bedroom in a panic after bumping into Nastya, Victoria furiously rebukes him for exposing her presence to the staff. "
    "While Max tries to downplay her fears and urges her to hurry to the restaurant, Victoria insists that they leave the apartment separately. "
    "Let's listen to their confrontation in Russian."
)

STORY = [
    ("max", "Почему ты вернулась такая злая?", "Why did you come back so angry?",
     [(253, "А че мы такие злые?")], "adapted"),
    ("anya", "Настя только что видела меня здесь!", "Nastya just saw me in here!",
     [], "new"),
    ("max", "Она просто живёт в этой квартире.", "She simply lives in this apartment.",
     [], "new"),
    ("anya", "Ты пригласил сюда весь наш ресторан?", "Did you invite our whole restaurant here?",
     [(253, "А ты бы еще весь персонал к тебе пригласил")], "adapted"),
    ("max", "По-моему, ты сильно преувеличиваешь сейчас.", "In my opinion, you are exaggerating greatly now.",
     [(254, "По-моему, ты преувеличиваешь")], "adapted"),
    ("anya", "Моя репутация в ресторане будет разрушена.", "My reputation at the restaurant will be ruined.",
     [], "new"),
    ("max", "Настя добрая девушка и умеет молчать.", "Nastya is a kind girl and knows how to keep quiet.",
     [], "new"),
    ("anya", "Официанты всегда обсуждают личную жизнь начальства.", "Waiters always discuss the management's personal life.",
     [], "new"),
    ("max", "Никто не станет обсуждать тебя, успокойся.", "No one will discuss you, calm down.",
     [], "new"),
    ("anya", "Я больше никогда не приду сюда.", "I will never come here again.",
     [], "new"),
    ("max", "Пожалуй, тебе уже пора на работу.", "Perhaps it is already time for you to go to work.",
     [(254, "пожалуй, тебе пора")], "adapted"),
    ("anya", "Мы должны выйти из дома раздельно.", "We must leave the building separately.",
     [], "new"),
    ("max", "Я согласен, иди первой, Вика.", "I agree, you go first, Vika.",
     [], "new"),
]

OPENER = "Let's see how Victoria vents her frustration and how Max attempts to calm her down."

WALK = [
    (1, None,
     "'Nastya just saw me in here!' A frantic exclamation revealing sudden fear of discovery by a coworker."),
    (3, None,
     "'Did you invite our whole restaurant here?' A hyperbolic accusation expressing frustration over lack of privacy."),
    (5, None,
     "'My reputation at the restaurant will be ruined.' A dramatic expression of worry concerning professional standing."),
    (11, None,
     "'We must leave the building separately.' A cautious instruction intended to prevent coworkers from suspecting a romance."),
]

TRANSITION = "Now, let's hear Victoria and Max settle their departure once more."

OUTRO = (
    "Now you know how to express anger over a ruined reputation, dismiss exaggerated fears, and plan a discreet exit in Russian. "
    "Listen for these lively dialogue patterns in future episodes."
)

CLOSING = ("anya", "Увидимся на кухне ресторана, Макс.")
