ID = "kukhnya-s04e05-scene-05"
SHOW = "kukhnya"
SEASON = 4
EPISODE = 5
SCENE = 5
TITLE = "Новый су-шеф  (The New Sous-Chef)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "german": "anja", "fedya": "angelina"}
LABELS = {"anya": "Макс", "german": "Герман", "fedya": "Федя"}
SOURCE_NAME = "Кухня (Kukhnya) S4.05"
SOURCE_FILE = "sources/kukhnya/s04/e05.ru.srt"
SOURCE_NOTE = "Cues 72-79. German Land gathers the kitchen brigade of Claude Monet and introduces Max Lavrov as their new sous-chef, prompting immediate teasing from Fedya and Senya."

INTRO = "Out in the gleaming kitchen of Claude Monet, German Land claps his hands for attention and presents Max Lavrov as the new sous-chef. As soon as German walks away, Fedya and the other cooks crowd around Max to tease their newly promoted colleague."

STORY = [
    ("german", "Уважаемые коллеги, прошу минуточку вашего внимания!", "Dear colleagues, I ask for a minute of your attention!", [(72, "Коллеги!"), (73, "Минуточку внимания.")], "adapted"),
    ("german", "Хочу представить вам нашего нового су-шефа.", "I want to introduce our new sous-chef to you.", [(74, "Хочу представить вам нашего нового су-шефа.")], ""),
    ("german", "Это повар Лавров Максим Леонидович.", "This is cook Lavrov Maksim Leonidovich.", [(75, "Лавров Максим Леонидович.")], "adapted"),
    ("german", "Прошу всех любить и жаловать его.", "I ask everyone to welcome and respect him.", [(76, "Прошу любить и жаловать.")], "adapted"),
    ("anya", "Приветствую вас, дорогие коллеги по кухне!", "Greetings to you, dear kitchen colleagues!", [], "new"),
    ("fedya", "Повара, низко кланяйтесь нашему новому су-шефу!", "Cooks, bow low to our new sous-chef!", [(77, "кланяйтесь новому су-шефу.")], "adapted"),
    ("fedya", "Макс, скажи честно, что тут происходит?", "Max, tell us honestly, what is going on here?", [(78, "Макс, что происходит?")], "adapted"),
    ("anya", "Ты как к су-шефу обращаешься сейчас?", "How are you addressing the sous-chef right now?", [(78, "Ты как к су-шефу обращаюсь")], "adapted"),
    ("fedya", "Ой, простите нас, уважаемый Максим Леонидович!", "Oh, forgive us, respected Maksim Leonidovich!", [(79, "Максим Леонидович")], "adapted"),
    ("fedya", "Ты теперь у нас выбился в начальники!", "You have now risen to become one of our bosses!", [(79, "начальники выбились.")], "adapted"),
    ("anya", "Да, теперь я ваш новый начальник.", "Yes, now I am your new boss.", [], "new"),
    ("anya", "Давайте все быстро вернёмся к работе.", "Let's all quickly return to work.", [], "new"),
]

OPENER = "Let's break down German's announcement and the cooks' reaction line by line."

WALK = [
    (0, None, "'Dear colleagues, I ask for a minute of your attention!' A diminutive accusative noun softens the formal request for silence."),
    (1, None, "'I want to introduce our new sous-chef to you.' The dative plural pronoun marks the audience receiving the introduction."),
    (2, None, "'This is cook Lavrov Maksim Leonidovich.' Full official Russian style places the surname before the given name and patronymic."),
    (3, None, "'I ask everyone to welcome and respect him.' A classic Russian idiom pairs two infinitives to ask for a warm reception."),
    (4, None, "'Greetings to you, dear kitchen colleagues!' Max enjoys his new status with a formal first-person greeting verb."),
    (5, None, "'Cooks, bow low to our new sous-chef!' Fedya jokes using a plural reflexive imperative governing the dative case."),
    (6, None, "'Max, tell us honestly, what is going on here?' Fedya switches back to informal speech to ask how Max got promoted."),
    (7, None, "'How are you addressing the sous-chef right now?' Max playfully pulls rank using the reflexive verb for addressing someone."),
    (8, None, "'Oh, forgive us, respected Maksim Leonidovich!' Fedya mocks his formality by using Max's full name and patronymic."),
    (9, None, "'You have now risen to become one of our bosses!' A colloquial reflexive idiom describes climbing into the ranks of management."),
    (10, None, "'Yes, now I am your new boss.' Max confirms his promotion with a straightforward nominative predicate noun."),
    (11, None, "'Let's all quickly return to work.' A first-person plural exhortation brings the joking brigade back to their stations."),
]

TRANSITION = "Now let's hear the announcement of the new sous-chef from beginning to end."
OUTRO = "Max is thrilled by his new title, though his authority is about to be tested by both Denis's rent money and a difficult order from German. See you in the next scene."
CLOSING = ("german", "Хочу представить вам нашего нового су-шефа.")
CLOSING_TRANS = "I want to introduce our new sous-chef to you."
