ID = "kukhnya-s04e08-scene-02"
SHOW = "kukhnya"
SEASON = 4
EPISODE = 8
SCENE = 2
TITLE = "Секрет от мамы  (A Secret from Mom)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "denis": "anja", "senya": "angelina"}
LABELS = {"anya": "Макс", "denis": "Денис", "senya": "Сеня"}
SOURCE_NAME = "Кухня (Kukhnya) S4.08"
SOURCE_FILE = "sources/kukhnya/s04/e08.ru.srt"
SOURCE_NOTE = "Cues 24-39. Max gives Denis money to buy groceries and flowers for his mother while instructing him to hide that he lives with them, as Senya pines for twenty thousand rubles to buy a red motorboat."

INTRO = "In the courtyard behind the restaurant, Max hands Denis money to buy groceries, flowers, and sweets for his mother's visit, while begging him not to tell his mom that Denis lives with them. Nearby, Senya complains to Fedya that he urgently needs twenty thousand rubles for a boat."

STORY = [
    ("anya", "Вот деньги, купи, пожалуйста, продукты домой.", "Here is the money, please buy groceries for home.", [(24, "Вот деньги."), (25, "Купи продукты домой.")], "adapted"),
    ("anya", "Купи маме цветы и сладости к чаю.", "Buy flowers for Mom and sweets for tea.", [(26, "Маме цветы. И к чаю, что она любит.")], "adapted"),
    ("denis", "Хорошо, я всё сделаю, не волнуйся.", "All right, I will do everything, do not worry.", [(27, "Хорошо? Да, окей, босс.")], "adapted"),
    ("anya", "И смотри, маме про себя не говори!", "And mind you, do not tell Mom about yourself!", [(28, "Ты маме про Дэну не говори.")], "adapted"),
    ("anya", "Не говори, что ты сейчас у нас живёшь.", "Do not say that you are living at our place right now.", [(29, "Вообще, что он у нас живет и что приехал.")], "adapted"),
    ("anya", "Ведь ты якобы сын от первого брака.", "After all, you are supposedly a son from a first marriage.", [(31, "Он сын от первого брака и все такое.")], "adapted"),
    ("anya", "Ты сегодня в подъезде чисто подмёл?", "Did you sweep the entrance hall clean today?", [(33, "Ты в подъезде подмел?")], "adapted"),
    ("denis", "Да, конечно, я уже всё чисто подмёл.", "Yes, of course, I already swept everything clean.", [(33, "Да, подмел, подмел.")], "adapted"),
    ("senya", "Смотри, даже Максу жена спокойно деньги даёт!", "Look, even Max's wife calmly gives him money!", [(35, "Смотри. Даже оглушку же на денег дает.")], "adapted"),
    ("senya", "А мне сейчас очень нужна всего двадцатка!", "And right now I really need just twenty grand!", [(36, "А мне нужна всего двадцатка.")], "adapted"),
    ("senya", "Ведь от меня такая красная лодка уходит!", "After all, such a red boat is slipping away from me!", [(36, "Такая лодка уходит."), (37, "Японский мотор. Красная.")], "adapted"),
    ("senya", "А моя жена мне вообще денег не даёт.", "And my wife does not give me any money at all.", [(39, "Пробовал, попался. Теперь вообще не дает.")], "adapted"),
]

OPENER = "Let's examine Max's instructions to Denis and Senya's boat dream line by line."

WALK = [
    (0, None, "'Here is the money, please buy groceries for home.' Accusative plural 'groceries' follows the imperative 'buy'."),
    (1, None, "'Buy flowers for Mom and sweets for tea.' Preposition 'to/for' with the dative 'tea' denotes treats served with tea."),
    (2, None, "'All right, I will do everything, do not worry.' Denis plays along as Max's helpful houseguest."),
    (3, None, "'And mind you, do not tell Mom about yourself!' Max has to protect his earlier lie to Vika that Denis is his half-brother."),
    (4, None, "'Do not say that you are living at our place right now.' If Max's mother meets Denis, she will immediately expose that he is not Max's brother!"),
    (5, None, "'After all, you are supposedly a son from a first marriage.' Particle 'supposedly' recalls the cover story Max told Vika."),
    (6, None, "'Did you sweep the entrance hall clean today?' Perfective past verb 'swept' checks on the morning chores."),
    (7, None, "'Yes, of course, I already swept everything clean.' Denis heads into the kitchen to look for a new room to rent."),
    (8, None, "'Look, even Max's wife calmly gives him money!' Watching from the doorway, Senya envies the cash in Max's hand."),
    (9, None, "'And right now I really need just twenty grand!' Colloquial feminine noun 'a twenty' means twenty thousand rubles."),
    (10, None, "'After all, such a red boat is slipping away from me!' Present-tense verb 'is leaving/slipping away' conveys urgency."),
    (11, None, "'And my wife does not give me any money at all.' Moments later, Denis's search for a room gives Senya a profitable idea."),
]

TRANSITION = "Now let's listen to the courtyard conversation again without interruption."
OUTRO = "Needing a place to stay while Max's mother visits, Denis walks into the kitchen and asks if anyone has a spare room to rent. See you in the next scene."
CLOSING = ("anya", "Не говори, что ты сейчас у нас живёшь.")
CLOSING_TRANS = "Do not say that you are living at our place right now."
