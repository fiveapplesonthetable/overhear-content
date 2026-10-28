ID = "kukhnya-s04e06-scene-07"
SHOW = "kukhnya"
SEASON = 4
EPISODE = 6
SCENE = 7
TITLE = "Просьба Луи  (Louis's Request)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "senya": "anja", "louis": "angelina"}
LABELS = {"anya": "Макс", "senya": "Сеня", "louis": "Луи"}
SOURCE_NAME = "Кухня (Kukhnya) S4.06"
SOURCE_FILE = "sources/kukhnya/s04/e06.ru.srt"
SOURCE_NOTE = "Cues 80-98. At Claude Monet, Senya complains that his wife had a toothache during their dinner, and pastry chef Louis convinces Denis to cover his dessert station for the day."

INTRO = "Back in the kitchen of Claude Monet, Max asks Senya how his reconciliation dinner went, while pastry chef Louis looks for someone to cover his shift so he can visit the bathhouse with a friend from Paris. When Fedya refuses, Louis talks young Denis into watching his desserts."

STORY = [
    ("anya", "Сеня, ну как прошёл твой примирительный ужин?", "Senya, well how did your reconciliation dinner go?", [(80, "Ну как, прошел примерительный ужин?")], "adapted"),
    ("senya", "Никак, у жены вечером сильно заболел зуб.", "Nowhere, my wife got a bad toothache in the evening.", [(81, "Никак."), (82, "у нее зуб заболел")], "adapted"),
    ("senya", "Она за весь вечер совсем ничего не ела.", "She ate nothing at all during the whole evening.", [(82, "а она ничего не ела.")], "adapted"),
    ("louis", "Друзья, я хотел попросить вас заменить меня.", "Folks, I wanted to ask you to cover for me.", [(84, "я хотел вас сегодня попросить заменить меня.")], "adapted"),
    ("louis", "Сегодня в Москве проездом мой близкий друг.", "My close friend is passing through Moscow today.", [(85, "Сегодня в Москве так проездом один мой очень близкий-близкий друг.")], "adapted"),
    ("senya", "Луи, давай без подробностей, мы сейчас заняты.", "Louis, spare us the details, we are busy right now.", [(87, "давай без подробностей")], "adapted"),
    ("senya", "Ищи себе замену среди свободных поваров.", "Look for a replacement among the free cooks.", [(92, "Ищи себе замену среди тех")], "adapted"),
    ("louis", "Денис, пожалуйста, не переживай за мою работу.", "Denis, please do not worry about my work.", [(95, "Ты не переживай.")], "adapted"),
    ("louis", "Сегодня вечером на кухне не будет Германа.", "Tonight German will not be in the kitchen.", [(95, "Во-первых, сегодня не будет керма.")], "adapted"),
    ("louis", "И все мои десерты уже полностью готовы.", "And all my desserts are already completely ready.", [(96, "Во-вторых, у меня все десерты уже готовы.")], "adapted"),
    ("louis", "Они аккуратно стоят в моём большом холодильнике.", "They are sitting neatly in my big refrigerator.", [(97, "Они у меня будут в холодильнике.")], "adapted"),
    ("louis", "Я всё подписал, их нужно просто отдать!", "I labeled everything, you just need to hand them out!", [(98, "я все подписал. Теперь их нужно просто отдать.")], "adapted"),
]

OPENER = "Let's examine Louis's request in the kitchen line by line."

WALK = [
    (0, None, "'Senya, well how did your reconciliation dinner go?' Max checks on the outcome of Senya's romantic dinner."),
    (1, None, "'Nowhere, my wife got a bad toothache in the evening.' The inchoative prefix on the verb marks the sudden onset of pain."),
    (2, None, "'She ate nothing at all during the whole evening.' Accusative time span after 'for/during' marks the whole evening."),
    (3, None, "'Folks, I wanted to ask you to cover for me.' Perfective infinitive 'to replace' means covering someone's shift."),
    (4, None, "'My close friend is passing through Moscow today.' Prepositional case marks location in the capital."),
    (5, None, "'Louis, spare us the details, we are busy right now.' Preposition 'without' governs the genitive plural of 'details'."),
    (6, None, "'Look for a replacement among the free cooks.' Preposition 'among' governs the genitive plural case."),
    (7, None, "'Denis, please do not worry about my work.' Louis turns to the newest cook in the kitchen."),
    (8, None, "'Tonight German will not be in the kitchen.' Impersonal negated future takes the genitive singular of German's name."),
    (9, None, "'And all my desserts are already completely ready.' Plural short predicate adjective 'ready' agrees with 'desserts'."),
    (10, None, "'They are sitting neatly in my big refrigerator.' In Russian, upright dishes and containers 'stand' inside the fridge."),
    (11, None, "'I labeled everything, you just need to hand them out!' Unfortunately for Denis, Louis wrote all the labels in French."),
]

TRANSITION = "Now let's hear Louis's shift-swap conversation again from start to finish."
OUTRO = "With Louis gone for the day and Denis left in charge of the French desserts, Max walks out to the bar and gets a nasty shock from Kostya. See you in the next scene."
CLOSING = ("louis", "И все мои десерты уже полностью готовы.")
CLOSING_TRANS = "And all my desserts are already completely ready."
