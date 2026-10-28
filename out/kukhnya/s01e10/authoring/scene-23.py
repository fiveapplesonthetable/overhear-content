# Authoring module for kukhnya-s01e10-scene-23.
ID = 'kukhnya-s01e10-scene-23'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 10
SCENE = 23
TITLE = 'Нет денег — нет икры  (No Cash, No Caviar)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'timur': 'Тимур'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.10'
SOURCE_FILE = 'sources/kukhnya/s01/e10.ru.dual.srt'
INTRO = "Barinov has tasted the caviar, and now it's time to pay. Timur wants two hundred thousand rubles, and Barinov has just lost his money on football. Let's hear it."
OPENER = "Now I'll walk you through it."
TRANSITION = 'One more run through, all the way.'
OUTRO = 'No cash, no caviar, and a charge for the spoon. Barinov is in trouble, and he cannot see how to get out. Until we meet again, in Russian.'
CLOSING = ('timur', 'Пока!')
STORY = [
    ('barinov', 'Да, эта чёрная икра действительно очень вкусная.', 'Yes, this black caviar is indeed very tasty.', [(172, 'Да. Да. Вкусная')], ''),
    ('timur', 'Сколько денег ты приготовил за пять килограмм?', 'How much money did you prepare for five kilograms?', [(173, 'Сколько денег? Пять кило')], ''),
    ('barinov', 'Назови точную цену за весь этот товар.', 'Name the exact price for all these goods.', [(174, 'Двести тысяч')], ''),
    ('timur', 'С тебя ровно двести тысяч рублей прямо сейчас.', 'That will be exactly two hundred thousand rubles right now.', [(174, 'Двести тысяч')], ''),
    ('barinov', 'Тимур, оставь икру, а деньги отдам позже.', 'Timur, leave the caviar, and I will pay later.', [(175, 'оставляю икру, а деньги через неделю')], ''),
    ('timur', 'Нет денег — нет никакой вкусной икры.', 'No money — no delicious caviar.', [(176, 'нет налички, нет икры')], ''),
    ('barinov', 'Я поставил все деньги по твоему совету!', 'I bet all the money on your advice!', [(177, 'все деньги поставил на кони по твоей наводке')], ''),
    ('timur', 'Ты всё проиграл на своих любимых конях.', 'You lost everything on your beloved horses.', [(178, 'На коней?')], ''),
    ('barinov', 'Ты же сам клялся, что они выиграют!', 'You swore yourself that they would win!', [(177, 'Тимур, я отдам')], ''),
    ('timur', 'Пусть теперь твои кони приносят тебе икру.', 'Let your horses bring caviar to you now.', [(179, 'пусть твои кони тебе икру и мечут')], ''),
    ('barinov', 'Зачем ты убираешь этот товар обратно?', 'Why are you taking this merchandise back?', [(180, 'триста рублей годи')], ''),
    ('timur', 'Кстати, с тебя триста рублей за эту ложку!', 'By the way, you owe three hundred rubles for this spoonful!', [(180, 'триста рублей годи'), (182, 'Ты целую ложку икры съел')], ''),
]
WALK = [
    (0, None, '\'Yes, this black caviar is indeed very tasty.\' "Deystvitelno", "indeed", is built on "deystvie", "action", so it means "in actual fact". "Vkusnaya" is "tasty", with -aya for "ikra". Barinov praises the caviar.'),
    (1, None, '\'How much money did you prepare for five kilograms?\' "Skolko deneg", literally "how much of money", is "how much money": "dengi" becomes "deneg". "Prigotovil" is "you got ready", from "gotovit". Timur gets to business.'),
    (2, None, '\'Name the exact price for all these goods.\' "Tovar", "goods", is singular in Russian, so it\'s "ves etot tovar", "all this goods". "Nazovi" is "name", said to one person. "Tochnuyu tsenu" is "the exact price".'),
    (3, None, '\'That will be exactly two hundred thousand rubles right now.\' "S tebya", literally "from you", is the usual way to say "you owe". "Dvesti tysyach rubley" is "two hundred thousand rubles". "Pryamo seychas" is "right now".'),
    (4, None, '\'Timur, leave the caviar, and I will pay later.\' "Ostav", "leave", is the verb in Max\'s "ya ostavil ego", "I left it". "Otdam", "I\'ll give back", is how you say you\'ll pay. "Pozzhe" is "later".'),
    (5, None, '\'No money — no delicious caviar.\' "Net deneg, net ikry" is the pattern: after "net", "dengi" becomes "deneg" and "ikra" becomes "ikry". Short sayings like this are common. Timur says it like a rule.'),
    (6, None, '\'I bet all the money on your advice!\' "Postavil", "I put", is how you say "I bet", as in "stavlyu". "Po tvoemu sovetu" is "on your advice", the same "po" as in Max\'s "po retseptu", "by the recipe".'),
    (7, None, '\'You lost everything on your beloved horses.\' "Koni", "horses", is the nickname for CSKA, the Moscow football club, so the "horses" are the team Barinov bet on. "Na konyakh" is "on the horses". "Proigral" is "lost".'),
    (8, None, '\'You swore yourself that they would win!\' "Klyalsya", "swore", has -sya on the end. "Vyigrayut" is "they will win", the opposite of "proigral", "lost". "Ty zhe sam" is "you yourself". Barinov blames Timur.'),
    (9, None, '\'Let your horses bring caviar to you now.\' "Pust" is "let", and it opens the line. "Prinosyat" is "bring", as in bring again and again. "Tvoi koni" is "your horses". Timur is mocking him.'),
    (10, None, '\'Why are you taking this merchandise back?\' "Ubiraesh" is "you\'re taking away", the same verb as "tidy up". "Obratno" is "back". "Zachem" is "what for". Barinov watches the caviar go.'),
    (11, None, '\'By the way, you owe three hundred rubles for this spoonful!\' "Kstati" is "by the way". "S tebya", "from you", comes back for "you owe". "Za etu lozhku" is "for this spoon": "lozhka" becomes "lozhku" after "za".'),
]
