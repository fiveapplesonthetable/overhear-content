# Authoring module for dvorik-u-mosta-s02e06-scene-05.
ID = 'dvorik-u-mosta-s02e06-scene-05'
SHOW = 'dvorik-u-mosta'
SEASON = 2
EPISODE = 6
SCENE = 5
TITLE = 'Вальс для дворика  (Courtyard Waltz Complete)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'larisa': 'Лариса', 'yaroslav': 'Ярослав', 'kira': 'Кира'}
INTRO = 'Six o\'clock arrives in St Petersburg. Inside the warm glow of Room 9, Larisa stands beside the walnut upright piano while Yaroslav, Kira, and two dozen neighbours listen through the open green shutters. Listen first.'
OPENER = "Now let's play the opening-night concert again, one line at a time."
TRANSITION = "Now listen to the whole concert in the glass room once more."
OUTRO = "Piano and violin carry the finished waltz for the courtyard out into the warm Friday night to heartfelt applause. See you next time."
CLOSING = ('larisa', 'До свидания!')
STORY = [
    ('larisa', 'Добрый вечер, друзья! Снова добро пожаловать на пятничный чай в девятом номере.', 'Good evening, friends! Welcome back to Friday tea in room nine.'),
    ('yaroslav', 'Тридцать лет назад, в мае, моя тётя начала маленький вальс за этим пианино.', 'Thirty years ago, in May, my aunt started a little waltz at this piano.'),
    ('larisa', 'Дождь остановил вторую страницу, пока Кира и Матвей снова не открыли ставни.', 'Rain stopped page two, until Kira and Matvey opened the shutters again.'),
    ('kira', 'А сегодня наш сосед из десятого дома играет с Ларисой Борисовной на скрипке!', 'And tonight our neighbour from number ten plays the violin with Larisa Borisovna!'),
    ('larisa', 'Готовы на счёт три, друг мой? Раз, два, три...', 'Ready on three, my friend? One, two, three...'),
    ('kira', 'Ярослав Ильич, слушайте, как поднимается скрипка на средней клавише!', 'Yaroslav Ilyich, listen to the violin soar on the middle key!'),
    ('yaroslav', 'Даже мои очки запотели — и в первый раз я знаю, где они!', 'Even my glasses have misted up, and for once I know where they are!'),
    ('kira', 'Посмотрите: люди на Липовом переулке остановились у ворот и слушают!', 'Look: people on Lipovy Lane have stopped by the gate and are listening!'),
    ('larisa', 'А вот и тихий последний аккорд, на октаву выше, — и домой.', 'And here is the soft final chord, an octave higher, and home.'),
    ('yaroslav', 'Браво! Браво, Лариса Борисовна! Слышите, весь дворик хлопает!', 'Bravo! Bravo, Larisa Borisovna! Listen, the whole courtyard is clapping!'),
    ('larisa', 'Поклонитесь и вы, Ярослав Ильич: пятничная комната вашей тёти снова живая.', "Take a bow yourself, Yaroslav Ilyich: your aunt's Friday room is alive again."),
    ('kira', 'И никто ещё не хочет домой — время булочек с корицей!', 'And nobody wants to go home yet: time for cinnamon rolls!'),
]
WALK = [
    (0, None, ["'Good evening, friends! Welcome back to Friday tea in room nine.' Larisa welcomes people 'onto' an event: ", (None, 'на пятничный чай'), " is 'to Friday tea'."]),
    (1, None, ["'Thirty years ago, in May, my aunt started a little waltz at this piano.' Sitting at an instrument is 'behind' it in Russian: ", (None, 'за этим пианино.'), " means 'at this piano'."]),
    (2, None, ["'Rain stopped page two, until Kira and Matvey opened the shutters again.' Here 'until' needs an extra 'not' in front of the verb, so Larisa says ", (None, 'не открыли'), ", literally 'had not opened'."]),
    (3, None, ["'And tonight our neighbour from number ten plays the violin with Larisa Borisovna!' Playing an instrument takes 'on': ", (None, 'на скрипке!'), " is 'on the violin'."]),
    (4, None, ["'Ready on three, my friend? One, two, three...' To count out loud, Russians say ", (None, 'Раз,'), " instead of the usual word for 'one'."]),
    (5, None, ["'Yaroslav Ilyich, listen to the violin soar on the middle key!' Kira points to ", (None, 'средней клавише!'), ", the middle key that Matvey fixed this week."]),
    (6, None, ["'Even my glasses have misted up, and for once I know where they are!' Glasses fogging up with warm breath is ", (None, 'запотели'), ", from the word for sweat."]),
    (7, None, ["'Look: people on Lipovy Lane have stopped by the gate and are listening!' Kira says ", (None, 'остановились'), ", 'they stopped', a verb you will need on every street."]),
    (8, None, ["'And here is the soft final chord, an octave higher, and home.' Something arriving at last is ", (None, 'А вот и'), ", 'and here comes', perfect when a moment finally arrives."]),
    (9, None, ["'Bravo! Bravo, Larisa Borisovna! Listen, the whole courtyard is clapping!' Applause is ", (None, 'хлопает!'), " the verb for clapping your hands."]),
    (10, None, ["'Take a bow yourself, Yaroslav Ilyich: your aunt's Friday room is alive again.' The little ", (None, 'и вы,'), " here means 'you too', not 'and you'."]),
    (11, None, ["'And nobody wants to go home yet: time for cinnamon rolls!' Kira drops the verb 'go' in ", (None, 'не хочет домой'), ", 'does not want home', normal in spoken Russian."]),
]
