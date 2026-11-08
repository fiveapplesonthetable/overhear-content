# Authoring module for dvorik-u-mosta-s01e01-scene-04.
ID = 'dvorik-u-mosta-s01e01-scene-04'
SHOW = 'dvorik-u-mosta'
SEASON = 1
EPISODE = 1
SCENE = 4
TITLE = 'Четвёртый номер на втором этаже  (Room Four on the Second Floor)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kira': 'Кира', 'larisa': 'Лариса', 'matvey': 'Матвей'}
INTRO = 'Retired piano teacher Larisa Borisovna steps in from her taxi pulling a large dark-blue suitcase. Kira greets her very first guest at the desk while Matvey stands ready to help. Listen to the scene in Russian first.'
OPENER = "Now let's go through each line together."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'Kira handled her first check-in smoothly, though Matvey noticed that blue suitcase felt strangely heavy. See you next time to find out why.'
CLOSING = ('larisa', 'Всего доброго!')
STORY = [
    ('kira', 'Добро пожаловать! Здравствуйте, проходите, пожалуйста.', 'Welcome! Hello, please come in.'),
    ('larisa', 'Доброе утро, дорогая. У меня бронирование на имя Эвелин.', 'Good morning, my dear. I have a booking for Evelyn.'),
    ('kira', 'Да, четвёртый номер на втором этаже! Как прошла поездка на поезде?', 'Yes, room four on the second floor! How did your train trip go?'),
    ('larisa', 'Поездка была тихой и приятной, спасибо, но чемодан сегодня очень тяжёлый.', 'The trip was quiet and pleasant, thank you, though the suitcase is very heavy today.'),
    ('matvey', 'Разрешите мне. Ого, вы туда камни положили?', 'Allow me. Goodness, did you pack stones in there?'),
    ('larisa', 'Только платья, ноты и моя любимая чашка!', 'Only dresses, sheet music, and my favourite teacup!'),
    ('kira', 'Вот ваш ключ, номер четыре. Завтрак с половины восьмого до десяти.', 'Here is your key, number four. Breakfast is from half past seven to ten.'),
    ('larisa', 'Чудесно. А окно выходит на улицу или во двор?', 'Wonderful. Does the window face the street or the courtyard?'),
    ('kira', 'Во двор, прямо над старым деревом. Там очень тихо.', 'Into the courtyard, right above the old tree. It is very quiet there.'),
    ('larisa', 'Как раз то, что мне нужно. А где лестница?', 'Just what I need. And where are the stairs?'),
    ('matvey', 'Прямо через эту арку. Я отнесу синий чемодан наверх.', 'Right through this archway. I will carry the blue suitcase upstairs.'),
    ('larisa', 'Большое спасибо вам обоим.', 'Thank you both very much.'),
]
WALK = [
    (0, None, ["'Welcome! Hello, please come in.' Kira uses the full formal greeting ", (None, 'Здравствуйте,'), ' whose old root literally wishes the listener good health.']),
    (1, None, ["'Good morning, my dear. I have a booking for Evelyn.' Instead of 'I have', Russian says ", (None, 'У меня бронирование'), " — literally 'at me a booking'."]),
    (2, None, ["'Yes, room four on the second floor! How did your train trip go?' For floors of a building, Russian uses 'on', so ", (None, 'на втором этаже!'), " means 'on the second floor'."]),
    (3, None, ["'The trip was quiet and pleasant, thank you, though the suitcase is very heavy today.' Notice ", (None, 'была'), " in the first half for the past trip, while the second half drops 'is' in the present."]),
    (4, None, ["'Allow me. Goodness, did you pack stones in there?' Even gruff Matvey turns courteous with guests, opening with ", (None, 'Разрешите мне.'), " — 'permit me'."]),
    (5, None, ["'Only dresses, sheet music, and my favourite teacup!' Musical notes on paper are simply plural ", (None, 'ноты'), ' — the exact word a piano teacher travels with.']),
    (6, None, ["'Here is your key, number four. Breakfast is from half past seven to ten.' Pointing something out as you hand it over starts with ", (None, 'Вот ваш ключ,'), " — 'here is your key'."]),
    (7, None, ["'Wonderful. Does the window face the street or the courtyard?' In Russian a window literally 'walks out' toward a view: ", (None, 'выходит'), " means 'goes out' or 'faces'."]),
    (8, None, ["'Into the courtyard, right above the old tree. It is very quiet there.' Describing the peaceful atmosphere uses the short impersonal form ", (None, 'тихо.'), " — 'it is quiet'."]),
    (9, None, ["'Just what I need. And where are the stairs?' One staircase is singular in Russian: ", (None, 'лестница?'), ' names the whole flight of stairs as a single thing.']),
    (10, None, ["'Right through this archway. I will carry the blue suitcase upstairs.' Destination and location split cleanly: ", (None, 'наверх.'), " means 'upward, to the top floor'."]),
    (11, None, ["'Thank you both very much.' Turning plain thanks into ", (None, 'Большое спасибо'), " literally gives someone a 'big thank you'."]),
]
