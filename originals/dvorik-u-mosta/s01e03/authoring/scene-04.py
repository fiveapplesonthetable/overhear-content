# Authoring module for dvorik-u-mosta-s01e03-scene-04.
ID = 'dvorik-u-mosta-s01e03-scene-04'
SHOW = 'dvorik-u-mosta'
SEASON = 1
EPISODE = 3
SCENE = 4
TITLE = 'Гость под дождём  (In from the Rain)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kira': 'Кира', 'roman': 'Роман', 'zoya': 'Зоя'}
INTRO = 'Down in the lobby, quiet traveller Roman steps inside shaking out a wet umbrella. Kira greets him at the desk while Zoya brings a warm towel. Listen to the Russian first.'
OPENER = "Now let's take their rainy-night welcome line by line."
TRANSITION = "Let's listen to the whole conversation again from start to finish."
OUTRO = 'Honesty, a dry towel, and a cup of hot soup kept the conversation calm. Next time, Roman climbs the stairs to judge the attic room for himself.'
CLOSING = ('roman', 'До встречи!')
STORY = [
    ('kira', 'Добрый вечер! Проходите скорее с дождя в тепло.', 'Good evening! Come inside quickly out of the rain into the warmth.'),
    ('roman', 'Добрый вечер. Извините, с моего зонта капает вода на чистый пол.', 'Good evening. Sorry, water is dripping from my umbrella onto the clean floor.'),
    ('kira', 'Ничего страшного! Вы, наверное, Роман?', 'No problem at all! You must be Roman?'),
    ('roman', 'Да, я Роман. Вчера я бронировал седьмой номер по телефону.', 'Yes, I am Roman. Yesterday I booked room seven by phone.'),
    ('zoya', 'Вот сухое полотенце для пальто и чашка горячего супа.', 'Here is a dry towel for your coat and a cup of hot soup.'),
    ('roman', 'Горячий суп? После холодной платформы это звучит чудесно.', 'Hot soup? After that cold platform, that sounds wonderful.'),
    ('kira', 'Роман, прежде чем мы поднимемся наверх, я хочу честно извиниться.', 'Roman, before we go upstairs, I want to apologize honestly.'),
    ('roman', 'Ой? С моей бронью какая-то проблема?', 'Oh? Is there some problem with my booking?'),
    ('kira', 'Мы случайно записали двух гостей в седьмой номер на сегодня.', 'We accidentally wrote down two guests for room seven tonight.'),
    ('roman', 'Вот как... под таким дождём? У вокзала все отели были полные.', 'I see... in rain like this? Near the station all the hotels were full.'),
    ('kira', 'Пожалуйста, не волнуйтесь! Мы подготовили для вас тихую мансарду на третьем этаже.', 'Please do not worry! We prepared a quiet attic room on the third floor for you.'),
    ('roman', 'Мансарду на третьем этаже? Сначала я могу её посмотреть?', 'An attic room on the third floor? May I see it first?'),
]
WALK = [
    (0, None, ["'Good evening! Come inside quickly out of the rain into the warmth.' Stepping inside out of bad weather uses ", (None, 'с дождя'), " — literally 'off the rain'."]),
    (1, None, ["'Good evening. Sorry, water is dripping from my umbrella onto the clean floor.' Listen to ", (None, 'капает'), ' — you can practically hear individual raindrops falling in its sound.']),
    (2, None, ["'No problem at all! You must be Roman?' Whenever someone apologizes for a minor spill, ", (None, 'Ничего страшного!'), " reassures them — literally 'nothing terrible!'."]),
    (3, None, ["'Yes, I am Roman. Yesterday I booked room seven by phone.' Doing business over the telephone uses ", (None, 'по телефону.'), " — 'along the phone line'."]),
    (4, None, ["'Here is a dry towel for your coat and a cup of hot soup.' Notice neuter ", (None, 'сухое полотенце'), " — 'dry towel', Zoya's instant cure for Petersburg rain."]),
    (5, None, ["'Hot soup? After that cold platform, that sounds wonderful.' Agreeing warmly with a plan uses ", (None, 'звучит чудесно.'), " — 'sounds wonderful'."]),
    (6, None, ["'Roman, before we go upstairs, I want to apologize honestly.' Joining two clauses in order uses ", (None, 'прежде чем'), " for 'before'."]),
    (7, None, ["'Oh? Is there some problem with my booking?' Adding an indefinite tail onto 'what kind' creates ", (None, 'какая-то'), " — 'some kind of' problem."]),
    (8, None, ["'We accidentally wrote down two guests for room seven tonight.' Happening by pure chance is ", (None, 'случайно'), " — 'accidentally'."]),
    (9, None, ["'I see... in rain like this? Near the station all the hotels were full.' Calm, understated ", (None, 'Вот как...'), " means 'oh, is that so...' while Roman takes in the news."]),
    (10, None, "'Please do not worry! We prepared a quiet attic room on the third floor for you.' Kira pivots immediately from the mistake to the solution ready upstairs."),
    (11, None, ["'An attic room on the third floor? May I see it first?' Asking polite permission uses ", (None, 'я могу'), ' plus ', (None, 'посмотреть?'), " — 'can I take a look?'."]),
]
