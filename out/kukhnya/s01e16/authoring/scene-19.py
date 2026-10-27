"""s01e16 scene 19: Проверка документов (Document Check)."""

ID = "kukhnya-s01e16-scene-19"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 16
SCENE = 19
TITLE = "Проверка документов  (Document Check)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "kostya": "anja"}
LABELS = {"anya": "Луи", "kostya": "Инспектор"}
SOURCE_NAME = "Кухня (Kukhnya) S1.16"
SOURCE_FILE = "sources/kukhnya/s01/e16.ru.dual.srt"
SOURCE_NOTE = "Cue 270. Having exposed Louis in the dining room, the migration inspector demands his documents and escorts him to the chef's office."

INTRO = (
    "Having seen right through Louis's disguise in the dining room, the migration officer demands to inspect his official work papers. "
    "When the French pastry chef admits that his documents are not in order, the inspector firmly escorts him toward Chef Barinov's office. "
    "Let's listen to their exchange in Russian."
)

STORY = [
    ("kostya", "Где ваше разрешение на работу?", "Where is your work permit?",
     [], "new"),
    ("anya", "Мои документы лежат в кабинете шефа.", "My documents are lying in the chef's office.",
     [], "new"),
    ("kostya", "У вас нет нужных бумаг?", "Do you not have the necessary papers?",
     [], "new"),
    ("anya", "Я просто забыл сделать новые документы.", "I simply forgot to make new documents.",
     [], "new"),
    ("kostya", "Это очень большая проблема для ресторана.", "This is a very big problem for the restaurant.",
     [], "new"),
    ("anya", "Я делаю здесь лучшие десерты!", "I make the best desserts here!",
     [], "new"),
    ("kostya", "Закон один для всех людей.", "The law is one for all people.",
     [], "new"),
    ("anya", "Что вы теперь будете делать?", "What are you going to do now?",
     [], "new"),
    ("kostya", "Мне нужно поговорить с вашим начальником.", "I need to talk to your boss.",
     [], "new"),
    ("anya", "Наш шеф сейчас очень занят.", "Our chef is very busy right now.",
     [], "new"),
    ("kostya", "Он быстро найдёт время для меня.", "He will quickly find time for me.",
     [], "new"),
    ("kostya", "Вставайте, сейчас пройдёмте со мной.", "Get up, now come with me.",
     [(270, "Пройдемте")], "adapted"),
    ("anya", "Хорошо, пойдёмте в кабинет шефа.", "All right, let's go to the chef's office.",
     [], "new"),
]

OPENER = "Let's see how the migration officer questions Louis and orders him to the office."

WALK = [
    (0, None,
     "'Where is your work permit?' A direct question asking for official authorization to work in the country."),
    (3, None,
     "'I simply forgot to make new documents.' An admission of neglect using the past tense and an infinitive."),
    (8, None,
     "'I need to talk to your boss.' A firm statement expressing the necessity of speaking with the manager."),
    (11, None,
     "'Get up, now come with me.' A polite but authoritative command instructing someone to follow an official."),
]

TRANSITION = "Now, let's hear the confrontation between the inspector and Louis once again."

OUTRO = (
    "Now you know how to ask about official paperwork, admit to forgetting a task, and request to see a manager in Russian. "
    "Listen to the final outcome in Chef Barinov's office in the next scene."
)

CLOSING = ("kostya", "Ваш шеф ответит за это.")
