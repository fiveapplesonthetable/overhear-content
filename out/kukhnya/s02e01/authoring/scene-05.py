ID = "kukhnya-s02e01-scene-05"
SHOW = "kukhnya"
SEASON = 2
EPISODE = 1
SCENE = 5
TITLE = "Букет цветов  (A Bouquet of Flowers)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "max": "anja", "viktor": "angelina"}
LABELS = {"anya": "Вика", "max": "Макс", "viktor": "Шеф"}
SOURCE_NAME = "Кухня (Kukhnya) S2.01"
SOURCE_FILE = "sources/kukhnya/s02/e01.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 103-121. Kostya serves Chef Viktor water instead of alcohol, Max sends Victoria "
    "a bouquet of flowers to beg for forgiveness, and Viktor greets guests in the dining room."
)

INTRO = (
    "In the dining room of Claude Monet, Bartender Kostya refuses to pour alcohol for Chef Viktor. "
    "Meanwhile, Max sends Victoria a large bouquet of flowers and begs for her forgiveness, while "
    "Viktor chats with guests at their table. Let us listen to the scene in Russian first."
)

STORY = [
    ("viktor", "Костя, почему ты налил мне простую воду?",
     "Kostya, why did you pour me plain water?",
     [(103, "Это что? Вода, Виктор Петрович.")], "adapted"),
    ("viktor", "Новый хозяин боится, что я буду пить.",
     "The new owner is afraid that I will drink.",
     [(104, "Новый хозяин заплатил мне его наливать, сказал, если налью — уволят.")], "adapted"),
    ("anya", "Посмотрите, кто прислал мне этот красивый букет?",
     "Look, who sent me this beautiful bouquet?",
     [(105, "Вам букет передали."), (106, "Да? Какой красивый."), (107, "От кого? От Макса.")], "adapted"),
    ("max", "Вика, это я подарил тебе свежие цветы.",
     "Vika, it was I who gave you fresh flowers.",
     [(107, "От кого? От Макса.")], "adapted"),
    ("max", "Подожди, пожалуйста, выслушай меня сейчас одну минуту.",
     "Wait, please, listen to me right now for one minute.",
     [(108, "Подождите, Виктория Сергеевна, понимаете, Макс, дело в том,"), (110, "Секунду. Вика, я понимаю,")], "adapted"),
    ("max", "Я понимаю, что сделал вчера ужасный поступок.",
     "I understand that I committed a terrible act yesterday.",
     [(111, "что совершил ваш ужасный, ужас, ужасный поступок.")], "adapted"),
    ("max", "Я очень сильно жалею о своей глупости.",
     "I very deeply regret my foolishness.",
     [(109, "что он очень сильно, очень сожалеет и...")], "adapted"),
    ("max", "Пожалуйста, прости меня за эту плохую ночь!",
     "Please, forgive me for that bad night!",
     [(112, "Пожалуйста, прости меня, дурака.")], "adapted"),
    ("anya", "Я не хочу слушать твои пустые слова.",
     "I do not want to listen to your empty words.",
     [], "new"),
    ("viktor", "Добрый день, я главный повар этого ресторана.",
     "Good afternoon, I am the head chef of this restaurant.",
     [(113, "Добрый день. Я шеф-повар этого ресторана.")], "adapted"),
    ("viktor", "Вам нравятся наши сегодняшние горячие блюда?",
     "Do you like our hot dishes today?",
     [(114, "Вам все нравится? Знаете, все великолепно, очень вкусно.")], "adapted"),
    ("viktor", "Гости предлагают мне выпить с ними вина.",
     "The guests are offering me to drink wine with them.",
     [(115, "Может, выпьете с нами?")], "adapted"),
    ("viktor", "На работе нельзя, но сегодня можно немного!",
     "At work it is forbidden, but today a little is allowed!",
     [(117, "Я ведь на работе."), (119, "Для вас я сделаю скачей.")], "adapted"),
]

OPENER = "Now let us examine Max's apology and Viktor's temptation line by line."

WALK = [
    (0, None,
     "'Kostya, why did you pour me plain water?' -- Chef Viktor is baffled when the bartender serves him water."),
    (1, None,
     "'The new owner is afraid that I will drink.' -- Viktor realizes Igor ordered the staff to cut him off."),
    (2, None,
     "'Look, who sent me this beautiful bouquet?' -- Victoria admires a surprise delivery of flowers."),
    (3, None,
     "'Vika, it was I who gave you fresh flowers.' -- Max steps forward as the sender of the gift."),
    (4, None,
     "'Wait, please, listen to me right now for one minute.' -- Max begs Victoria not to walk away."),
    (5, None,
     "'I understand that I committed a terrible act yesterday.' -- He openly admits his wrongdoing."),
    (6, None,
     "'I very deeply regret my foolishness.' -- Max expresses sincere remorse for hurting her."),
    (7, None,
     "'Please, forgive me for that bad night!' -- He pleads with Victoria for a second chance."),
    (8, None,
     "'I do not want to listen to your empty words.' -- Victoria rejects his apology and walks off."),
    (9, None,
     "'Good afternoon, I am the head chef of this restaurant.' -- Viktor greets a table of VIP guests."),
    (10, None,
     "'Do you like our hot dishes today?' -- He politely checks on the quality of their meal."),
    (11, None,
     "'The guests are offering me to drink wine with them.' -- The delighted patrons invite the chef to share a glass."),
    (12, None,
     "'At work it is forbidden, but today a little is allowed!' -- Viktor gives in to temptation despite the ban."),
]

TRANSITION = "Now let us listen to the full dining room scene once again."
OUTRO = (
    "While Victoria coldly rejects Max's flowers and apology, Chef Viktor finds a clever excuse "
    "to share a drink with appreciative restaurant guests."
)
CLOSING = ("viktor", "На работе нельзя, но сегодня можно немного!")
