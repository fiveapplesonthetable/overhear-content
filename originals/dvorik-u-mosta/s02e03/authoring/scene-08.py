# Authoring module for dvorik-u-mosta-s02e03-scene-08.
ID = 'dvorik-u-mosta-s02e03-scene-08'
SHOW = 'dvorik-u-mosta'
SEASON = 2
EPISODE = 3
SCENE = 8
TITLE = 'Гром в полночь  (Thunder at Midnight)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kira': 'Кира', 'matvey': 'Матвей'}
INTRO = 'Just before midnight on Sunday, Kira is locking the cash drawer at the front desk while Matvey checks his brass keys, when a low rumble shakes the courtyard glass. Listen first.'
OPENER = "Let's go back to that stormy midnight and replay it line by line."
TRANSITION = 'Now listen to the whole midnight rescue again without stopping.'
OUTRO = 'Kira and Matvey rescue the bare wooden shutters seconds before the midnight rain pours down. But with rain forecast all Monday, how will the paint dry before Wednesday? This episode is complete. See you in the next one.'
CLOSING = ('kira', 'Спокойной ночи!')
STORY = [
    ('kira', 'Матвей, это тяжёлый грузовик проехал по Липовому переулку?', 'Matvey, was that a heavy truck driving down Lipovy Lane?'),
    ('matvey', 'В полночь грузовиков нет. Посмотри в окно — молния!', 'There are no trucks at midnight. Look out the window, lightning!'),
    ('kira', 'Ой нет! Ты же снял все четыре ставни с петель!', 'Oh no! You took all four shutters off their hinges!'),
    ('matvey', 'И они стоят у стены во дворе прямо сейчас!', 'And they are standing against the courtyard wall right now!'),
    ('kira', 'Если сухое дерево промокнет, краска в понедельник не будет держаться!', "If the dry wood gets soaked, the paint won't stick on Monday!"),
    ('matvey', 'Бери фонарь у задней двери, Кира, уже падают первые капли!', 'Grab the lantern by the back door, Kira, the first drops are already falling!'),
    ('kira', 'Я держу левый край первой ставни — поднимаем и бегом в коридор!', "I've got the left end of the first shutter, lift and run to the hallway!"),
    ('matvey', 'Хорошо! Две есть, ещё две на улице. Осторожно, мокрые камни!', 'Good! Two done, two more outside. Careful, wet stones!'),
    ('kira', 'Последние две, и тут небо открылось! Фух, рукава совсем мокрые!', 'The last two, and then the sky opened! Phew, my sleeves are soaking wet!'),
    ('matvey', 'Дерево совсем сухое, Кира. Ты быстро бегаешь в грозу.', 'The wood is completely dry, Kira. You run fast in a storm.'),
    ('kira', 'Подожди, а если в понедельник весь день дождь, где красить ставни?!', 'Wait, and if it rains all day Monday, where do we paint the shutters?!'),
    ('matvey', 'Смотри прогноз на понедельник... сильный дождь до обеда вторника!', 'Look at the forecast for Monday... heavy rain until Tuesday lunchtime!'),
]
WALK = [
    (0, None, ["'Matvey, was that a heavy truck driving down Lipovy Lane?' Moving along a street takes 'along' in Russian: ", (None, 'проехал по'), " is 'drove along'."]),
    (1, None, ["'There are no trucks at midnight. Look out the window, lightning!' After 'there is no', the noun shifts its ending, so ", (None, 'грузовиков нет.'), " is literally 'of trucks, there is none'."]),
    (2, None, ["'Oh no! You took all four shutters off their hinges!' Kira's tiny ", (None, 'же'), " adds 'but you did, remember!', a spoken nudge with no direct English match."]),
    (3, None, ["'And they are standing against the courtyard wall right now!' Leaning things 'stand' in Russian, and ", (None, 'у стены'), " means 'by the wall', right up against it."]),
    (4, None, ["'If the dry wood gets soaked, the paint won't stick on Monday!' Soaked right through is ", (None, 'промокнет,'), " with a front part that means 'through', so the water goes all the way in."]),
    (5, None, ["'Grab the lantern by the back door, Kira, the first drops are already falling!' In a hurry, Matvey uses the quick informal ", (None, 'Бери'), ", 'take!', the way you talk to a close colleague."]),
    (6, None, ["'I've got the left end of the first shutter, lift and run to the hallway!' A word made from running, ", (None, 'бегом'), " means 'at a run', perfect for any rush."]),
    (7, None, ["'Good! Two done, two more outside. Careful, wet stones!' Matvey keeps score with ", (None, 'Две есть,'), " literally 'two there are', meaning 'two done'."]),
    (8, None, ["'The last two, and then the sky opened! Phew, my sleeves are soaking wet!' Notice there's no 'my' in ", (None, 'рукава совсем мокрые!'), " Russian drops it when the owner is obvious."]),
    (9, None, ["'The wood is completely dry, Kira. You run fast in a storm.' A thunderstorm is ", (None, 'в грозу.'), " in Russian, a different word from the thunder in this scene's title."]),
    (10, None, ["'Wait, and if it rains all day Monday, where do we paint the shutters?!' Kira asks ", (None, 'где красить'), ", literally 'where to paint', a short way to ask about a plan with no 'we' at all."]),
    (11, None, ["'Look at the forecast for Monday... heavy rain until Tuesday lunchtime!' The weather report is ", (None, 'прогноз'), ", close to English 'prognosis', and it's always 'forecast for' a day."]),
]
