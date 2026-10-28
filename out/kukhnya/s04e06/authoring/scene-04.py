ID = "kukhnya-s04e06-scene-04"
SHOW = "kukhnya"
SEASON = 4
EPISODE = 6
SCENE = 4
TITLE = "Вино для свидания  (Wine for the Date)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "louis": "anja", "senya": "angelina"}
LABELS = {"anya": "Макс", "louis": "Луи", "senya": "Сеня"}
SOURCE_NAME = "Кухня (Kukhnya) S4.06"
SOURCE_FILE = "sources/kukhnya/s04/e06.ru.srt"
SOURCE_NOTE = "Cues 51-55. Louis selects an exquisite bottle of red wine from the bar for Max's romantic dinner with Vika, assuring him he can simply buy Kostya a replacement bottle tomorrow."

INTRO = "When Kostya steps away from the bar counter, Max asks French pastry chef Louis to pick out a romantic bottle of wine. Louis reaches behind the bar for an unlabeled reserve bottle, assuring Max that he can easily buy Kostya an identical bottle the next day."

STORY = [
    ("louis", "Месье, это вино как раз для ужина.", "Monsieur, this wine is just right for dinner.", [(51, "Месье, это вино как раз для романтического ужина.")], "adapted"),
    ("louis", "Оно специально создано, чтобы радовать женщин.", "It was specially created to delight women.", [(52, "Оно создано, чтобы соблазнять женщин.")], "adapted"),
    ("anya", "Но ведь это вино лежит в баре.", "But after all this wine is sitting at the bar.", [], "new"),
    ("louis", "Возьмите эту бутылку сегодня вечером, Максим.", "Take this bottle tonight, Maksim.", [(53, "Возьмите вы, месье Максим")], "adapted"),
    ("louis", "А завтра купите Константину такую же бутылку.", "And tomorrow buy Konstantin the exact same bottle.", [(53, "а завтра купите месье Константину такую же бутылку")], "adapted"),
    ("louis", "И тогда никто совсем ничего не заметит.", "And then nobody will notice anything at all.", [(54, "и никто ничего не заметит.")], "adapted"),
    ("anya", "Спасибо, Луи, ты мне очень помог!", "Thank you, Louis, you helped me a lot!", [], "new"),
    ("anya", "Сеня, держи вкусный десерт за твои почки.", "Senya, take a tasty dessert in exchange for your kidneys.", [], "new"),
    ("senya", "Ладно, ресторанный вредитель, забирай свежие почки.", "All right, restaurant menace, take the fresh kidneys.", [(55, "Ресторанный предатель, забирай.")], "adapted"),
    ("anya", "Сегодня вечером у нас будет чудесный ужин.", "Tonight we will have a wonderful dinner.", [], "new"),
    ("senya", "Смотри только не пережарь их на сковороде.", "Just make sure you do not overcook them in the pan.", [], "new"),
    ("anya", "Не волнуйся, я приготовлю всё идеально!", "Do not worry, I will cook everything perfectly!", [], "new"),
]

OPENER = "Let's examine how Louis chooses the wine at the bar counter line by line."

WALK = [
    (0, None, "'Monsieur, this wine is just right for dinner.' The emphatic particle phrase 'just right' highlights suitability."),
    (1, None, "'It was specially created to delight women.' Neuter short passive participle agrees with the neuter noun 'wine'."),
    (2, None, "'But after all this wine is sitting at the bar.' Prepositional case marks location behind the bar counter."),
    (3, None, "'Take this bottle tonight, Maksim.' Louis uses a polite plural imperative while handing over the rare bottle."),
    (4, None, "'And tomorrow buy Konstantin the exact same bottle.' Demonstrative determiner with the emphatic particle means 'the very same'."),
    (5, None, "'And then nobody will notice anything at all.' Double negative pronouns accompany the negated perfective future verb."),
    (6, None, "'Thank you, Louis, you helped me a lot!' Past-tense verb of helping governs the dative pronoun 'to me'."),
    (7, None, "'Senya, take a tasty dessert in exchange for your kidneys.' Preposition 'for' with the accusative expresses an exchange."),
    (8, None, "'All right, restaurant menace, take the fresh kidneys.' Imperfective imperative invites Max to take the replacement meat."),
    (9, None, "'Tonight we will have a wonderful dinner.' Future tense of 'to be' forms the future possession clause."),
    (10, None, "'Just make sure you do not overcook them in the pan.' Prefixed perfective verb means overcooking or frying too long."),
    (11, None, "'Do not worry, I will cook everything perfectly!' Max heads home with the mystery bottle, unaware of its true price."),
]

TRANSITION = "Now let's hear the wine selection scene at the bar again in full."
OUTRO = "Max takes the mystery bottle home for his reconciliation dinner with Vika, while over at Arcobaleno Chef Barinov prepares his own elaborate ruse. See you in the next scene."
CLOSING = ("louis", "Месье, это вино как раз для ужина.")
CLOSING_TRANS = "Monsieur, this wine is just right for dinner."
