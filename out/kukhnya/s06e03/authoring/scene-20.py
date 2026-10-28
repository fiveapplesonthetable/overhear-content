# Authoring module for kukhnya-s06e03-scene-20.
ID = 'kukhnya-s06e03-scene-20'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 3
SCENE = 20
TITLE = 'Одна семья и бутафорские деньги  (One Family and Prop Money)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'eleonora': 'Элеонора', 'kostya': 'Костя'}
SOURCE_NAME = 'Кухня (Kukhnya) S6.03'
SOURCE_FILE = 'sources/kukhnya/s06/e03.ru.srt'
INTRO = "In the final scene, Nastya's father tells orphan Kostya that they are his parents now too; back at the hotel, Barinov hands Eleonora his 100,000 rubles as restaurant profit—only to learn it is fake movie money."
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "Realizing that Nagiyev paid him for the shoot and the crew lunch with fake movie money, Barinov roars Nagiyev's name across the hotel. See you next time!"
CLOSING = ('barinov', 'До завтра!')
STORY = [
    ('kostya', 'Давай я тебе тридцать тысяч в месяц буду платить.', 'Let me pay you thirty thousand a month.', [(347, 'тысяч в месяц буду платить')], 'adapted'),
    ('barinov', 'Это нормально, когда родители помогают детям.', 'It is normal when parents help their children.', [(349, 'Это нормально, когда родители помогают детям')], 'exact'),
    ('kostya', 'У меня не было родителей.', 'I did not have parents.', [(350, 'У меня не было родителей')], 'exact'),
    ('barinov', 'Я знаю, но мы ведь одна семья.', 'I know, but after all we are one family.', [(352, 'Я знаю, но мы ведь одна семья')], 'exact'),
    ('barinov', 'Мы теперь и твои родители тоже, понимаешь?', 'We are now your parents too, do you understand?', [(353, 'Мы теперь и твои родители тоже'), (354, 'Понимаешь?')], 'adapted'),
    ('kostya', 'Давайте тогда ваш коньяк пить.', "Then let's drink your cognac.", [(355, 'Давайте тогда ваш коньяк пить')], 'exact'),
    ('eleonora', 'Я так понимаю, кухня сегодня не работала.', 'As I understand it, the kitchen did not work today.', [(357, 'Я так понимаю, кухня сегодня не работала')], 'exact'),
    ('eleonora', 'И этот день можно вычесть из зарплаты.', 'And this day can be deducted from your salary.', [(358, 'И этот день можно вычесть из зарплаты')], 'exact'),
    ('barinov', 'Ну почему же, авторская кухня принесла несколько копеек.', 'Why say that, the auteur cuisine brought in a few pennies.', [(359, 'Ну почему же?'), (360, 'Авторская кухня'), (361, 'принесла несколько копеек')], 'adapted'),
    ('eleonora', 'Витя, можешь оставить эти деньги себе.', 'Vitya, you can keep this money for yourself.', [(362, 'Витя, можешь оставить эти деньги себе')], 'exact'),
    ('eleonora', 'Там таких купюр много валяется.', 'There are plenty of banknotes like those lying around out there.', [(364, 'таких купюр много валяется')], 'adapted'),
    ('eleonora', 'Это бутафорские деньги.', 'This is prop money.', [(366, 'Это бутафорские деньги')], 'exact'),
]
WALK = [
    (0, None, '\'Let me pay you thirty thousand a month.\' Addressing the thousand with Barinov, Kostya starts with "davay" ("come on, let\'s") to invite Barinov right into the action.'),
    (1, None, "'It is normal when parents help their children.' Barinov steps in plainly with a smile, watching Kostya's face to see how the news lands."),
    (2, None, '\'I did not have parents.\' Mentioning the parents with Barinov, Kostya chooses "roditeley" ("parents", from the root "roditeli") so Barinov hears the exact meaning.'),
    (3, None, '\'I know, but after all we are one family.\' Talking about the family with Kostya, Barinov lands on "semya" ("family") as the key everyday word here.'),
    (4, None, "'We are now your parents too, do you understand?' Barinov presses calmly why things suddenly took this turn between them."),
    (5, None, '\'Then let\'s drink your cognac.\' Mentioning the cognac around Barinov, Kostya leans on "konyak" ("cognac, brandy") to give the whole sentence its punch.'),
    (6, None, '\'As I understand it, the kitchen did not work today.\' Bringing up the kitchen in this beat, Eleonora uses "kukhnya" ("kitchen") to carry the main weight of the thought.'),
    (7, None, "'And this day can be deducted from your salary.' Eleonora fires back frankly watching Barinov, refusing to let the moment slip past."),
    (8, None, '\'Why say that, the auteur cuisine brought in a few pennies.\' Focusing on the kitchen around Eleonora, Barinov reaches for the Russian word "avtorskaya" ("signature, author\'s", built from "avtorskiy") right at the center of the line.'),
    (9, None, '\'Vitya, you can keep this money for yourself.\' Pointing to the money to Barinov, Eleonora uses "dengi" ("money") to carry the main weight of the thought.'),
    (10, None, "'There are plenty of banknotes like those lying around out there.' Eleonora reacts frankly on the spot, steering the talk right where she wants it."),
    (11, None, '\'This is prop money.\' Pointing out how prop things are around Barinov, Eleonora puts the weight on "butaforskiye" ("prop, fake", from "butaforskiy") as the exchange unfolds.'),
]
