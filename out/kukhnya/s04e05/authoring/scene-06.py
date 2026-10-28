ID = "kukhnya-s04e05-scene-06"
SHOW = "kukhnya"
SEASON = 4
EPISODE = 5
SCENE = 6
TITLE = "Деньги на квартиру  (Money for the Apartment)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "denis": "anja", "senya": "angelina"}
LABELS = {"anya": "Макс", "denis": "Денис", "senya": "Сеня"}
SOURCE_NAME = "Кухня (Kukhnya) S4.05"
SOURCE_FILE = "sources/kukhnya/s04/e05.ru.srt"
SOURCE_NOTE = "Cues 80-98. Denis shows Max sixty thousand rubles that he claims his mother sent for rent, and after Senya easily pickpockets the envelope, Max takes the cash for safekeeping."

INTRO = "Moments after Max's promotion, Denis pulls him aside in the kitchen to share his own good news: he has sixty thousand rubles in cash to rent his own flat. When Senya effortlessly slips the envelope out of Denis's pocket as a prank, Max insists on holding the money himself."

STORY = [
    ("denis", "У меня, кстати, тоже хорошие новости.", "By the way, I also have good news.", [(80, "У меня, кстати, тоже хорошие новости.")], ""),
    ("denis", "Я наконец решил снять себе квартиру.", "I finally decided to rent an apartment for myself.", [(81, "Я квартиру решил снять.")], "adapted"),
    ("anya", "Интересно, а где ты взял деньги?", "Interesting, and where did you get the money?", [(82, "А где денег взял?")], "adapted"),
    ("denis", "Мне мама сегодня прислала эти деньги.", "My mom sent me this money today.", [(84, "Нет, мне мама прислала.")], "adapted"),
    ("denis", "Здесь ровно шестьдесят тысяч рублей.", "There are exactly sixty thousand rubles here.", [(85, "Здесь 60 тысяч.")], "adapted"),
    ("denis", "Я нашёл несколько хороших вариантов.", "I found several good options.", [(90, "Нашел несколько вариантов.")], "adapted"),
    ("denis", "Сейчас сразу после смены еду смотреть.", "Right after the shift I am going to look at them.", [(91, "Сейчас еду смотреть.")], "adapted"),
    ("senya", "Парень, ты случайно ничего не забыл?", "Guy, did you happen to forget anything?", [(93, "ничего не забыл?")], "adapted"),
    ("denis", "Как ты это сделал так незаметно?", "How did you do that so unnoticeably?", [(94, "Ты как это сделал? Незаметно.")], "adapted"),
    ("anya", "В метро деньги ещё незаметнее вытащат.", "On the metro they will steal the money even more unnoticeably.", [(95, "А в метро еще незаметней вытащить.")], "adapted"),
    ("anya", "Пусть деньги лучше полежат у меня.", "Let the money rather stay with me for safekeeping.", [(96, "Пусть у меня полежат, целей будут.")], "adapted"),
    ("anya", "Когда квартиру найдёшь, сразу их заберёшь.", "When you find an apartment, you will take it right back.", [(97, "найдешь, заберешь.")], "adapted"),
    ("denis", "Ладно, пусть пока полежат у тебя.", "All right, let it stay with you for now.", [(98, "Ладно.")], "adapted"),
]

OPENER = "Let's examine the exchange over Denis's rent money line by line."

WALK = [
    (0, None, "'By the way, I also have good news.' A parenthetical conversational word introduces the possessive construction."),
    (1, None, "'I finally decided to rent an apartment for myself.' In housing contexts, the perfective verb for taking off means renting a flat."),
    (2, None, "'Interesting, and where did you get the money?' Max asks about the source of the cash using a past-tense perfective verb."),
    (3, None, "'My mom sent me this money today.' A dative pronoun marks the recipient of the money sent by mail or transfer."),
    (4, None, "'There are exactly sixty thousand rubles here.' Russian compound tens require the genitive plural on the word for thousand."),
    (5, None, "'I found several good options.' The quantifier for several governs the genitive plural case on the following adjective and noun."),
    (6, None, "'Right after the shift I am going to look at them.' A unidirectional verb of motion by vehicle expresses an immediate trip."),
    (7, None, "'Guy, did you happen to forget anything?' Senya dangles the stolen envelope using a negative pronoun in a yes-or-no question."),
    (8, None, "'How did you do that so unnoticeably?' Denis marvels at the sleight of hand with an expressive manner adverb."),
    (9, None, "'On the metro they will steal the money even more unnoticeably.' An impersonal third-person plural verb warns against pickpockets."),
    (10, None, "'Let the money rather stay with me for safekeeping.' The particle for 'let' combines with a prefixed verb meaning to lie for a while."),
    (11, None, "'When you find an apartment, you will take it right back.' Two perfective future verbs form a clear temporal condition and result."),
    (12, None, "'All right, let it stay with you for now.' Denis agrees and hands the envelope of cash over to Max."),
]

TRANSITION = "Now let's listen to the full conversation about the apartment money again."
OUTRO = "With sixty thousand rubles tucked safely into his jacket pocket, Max feels on top of the world until German summons him for his first unpleasant duty as sous-chef. See you in the next scene."
CLOSING = ("denis", "У меня, кстати, тоже хорошие новости.")
CLOSING_TRANS = "By the way, I also have good news."
