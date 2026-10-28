ID = "kukhnya-s04e07-scene-02"
SHOW = "kukhnya"
SEASON = 4
EPISODE = 7
SCENE = 2
TITLE = "Банкет кинематографистов  (The Filmmakers' Banquet)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "nagiyev": "anja", "guest": "angelina"}
LABELS = {"anya": "Вика", "nagiyev": "Нагиев", "guest": "Гость"}
SOURCE_NAME = "Кухня (Kukhnya) S4.07"
SOURCE_FILE = "sources/kukhnya/s04/e07.ru.srt"
SOURCE_NOTE = "Cues 17-39. Gavril Ilyich from the Filmmakers' Union arrives on behalf of director Nikita Mikhalkov to book a banquet at Claude Monet, specifically requesting Chef Viktor Barinov's cooking."

INTRO = "An important visitor enters Claude Monet before opening hours: Gavril Ilyich, deputy chairman of the Filmmakers' Union, sent by legendary director Nikita Mikhalkov. He wants to book a prestigious banquet at the restaurant, but only if Viktor Barinov is the chef!"

STORY = [
    ("anya", "Дмитрий Владимирович, к нам пришёл важный гость.", "Dmitry Vladimirovich, an important guest has come to see us.", [(17, "Дмитрий Владимирович, у нас гость.")], "adapted"),
    ("nagiyev", "Доброе утро, но наш ресторан ещё закрыт.", "Good morning, but our restaurant is still closed.", [(18, "Доброе утро."), (19, "Мы еще закрыты.")], "adapted"),
    ("guest", "Позвольте мне сначала представиться вам, господа.", "Allow me to introduce myself to you first, gentlemen.", [(21, "Позвольте представиться.")], "adapted"),
    ("guest", "Я пришёл по поручению известного кинорежиссёра.", "I have come on behalf of the famous film director.", [(23, "я к вам по поручению Никиты Сергеевича Михалкова.")], "adapted"),
    ("nagiyev", "Ради съёмок я готов освободить любые даты!", "For the sake of filming I am ready to clear any dates!", [(24, "Я ради."), (25, "готов освободить все даты")], "adapted"),
    ("guest", "Спасибо, но я здесь по другому вопросу.", "Thank you, but I am here on another matter.", [(26, "но я здесь по другому вопросу.")], "adapted"),
    ("guest", "Мы хотим провести банкет в вашем ресторане.", "We want to hold a banquet in your restaurant.", [(27, "Мы хотели бы провести банкет Союза кинематографистов в вашем ресторане.")], "adapted"),
    ("guest", "Мы недавно обедали у вас, всё понравилось.", "We had lunch at your place recently, we liked everything.", [(28, "пару месяцев назад у вас обедали, нам очень понравилось.")], "adapted"),
    ("guest", "Все были в восторге от Виктора Баринова!", "Everyone was delighted with Viktor Barinov!", [(29, "был в восторге от вашего шеф-повара Виктора Баринова.")], "adapted"),
    ("guest", "Мы с нетерпением вновь ждём встречи с ним.", "We eagerly look forward to meeting him again.", [(31, "Так что с нетерпением."), (32, "Вновь ждем встречи с ним.")], "adapted"),
    ("guest", "Я зайду сегодня вечером попробовать банкетное меню.", "I will drop by this evening to taste the banquet menu.", [(37, "я зайду сегодня часиков в 7,"), (38, "попробовать банкетное меню.")], "adapted"),
    ("nagiyev", "Можете не сомневаться, Баринов обязательно будет здесь!", "You need not doubt it, Barinov will definitely be here!", [(39, "Можете не сомневаться, Маринов будет как штык.")], "adapted"),
]

OPENER = "Let's examine the Filmmakers' Union banquet request line by line."

WALK = [
    (0, None, "'Dmitry Vladimirovich, an important guest has come to see us.' Vika alerts the owner to the morning visitor."),
    (1, None, "'Good morning, but our restaurant is still closed.' Masculine short passive participle agrees with 'restaurant'."),
    (2, None, "'Allow me to introduce myself to you first, gentlemen.' Polite plural imperative 'allow' introduces the reflexive infinitive."),
    (3, None, "'I have come on behalf of the famous film director.' The dative phrase 'by commission of' means on someone's behalf."),
    (4, None, "'For the sake of filming I am ready to clear any dates!' Actor Nagiyev immediately hopes he is being cast in a movie."),
    (5, None, "'Thank you, but I am here on another matter.' Preposition 'on/by' governs the dative singular phrase 'another question'."),
    (6, None, "'We want to hold a banquet in your restaurant.' Perfective infinitive 'to conduct' is the standard verb for holding an event."),
    (7, None, "'We had lunch at your place recently, we liked everything.' Imperfective past plural verb describes dining at the restaurant."),
    (8, None, "'Everyone was delighted with Viktor Barinov!' The idiom 'in delight from' takes the genitive case of the chef's name."),
    (9, None, "'We eagerly look forward to meeting him again.' Instrumental phrase 'with impatience' pairs with 'waiting for a meeting'."),
    (10, None, "'I will drop by this evening to taste the banquet menu.' Perfective future verb 'will drop in' takes a purpose infinitive."),
    (11, None, "'You need not doubt it, Barinov will definitely be here!' Rather than admit he fired Barinov, Nagiyev promises he will be there."),
]

TRANSITION = "Now let's listen to the banquet booking conversation again in full."
OUTRO = "Having promised that Viktor Barinov will personally cook the banquet tasting tonight, Nagiyev now has to convince his fired chef to come back. See you in the next scene."
CLOSING = ("guest", "Все были в восторге от Виктора Баринова!")
CLOSING_TRANS = "Everyone was delighted with Viktor Barinov!"
