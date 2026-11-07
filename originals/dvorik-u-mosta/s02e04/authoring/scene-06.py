# Authoring module for dvorik-u-mosta-s02e04-scene-06.
ID = 'dvorik-u-mosta-s02e04-scene-06'
SHOW = 'dvorik-u-mosta'
SEASON = 2
EPISODE = 4
SCENE = 6
TITLE = 'Осторожно, табуретка  (Watch the Low Stool)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'zoya': 'Зоя', 'kira': 'Кира'}
INTRO = "In the warm kitchen behind the café corner on Tuesday evening, pastry cools on racks as Zoya climbs onto a low wooden stool to reach the big teapot while Kira comes in with the menus. Listen first."
OPENER = "Let's go back through that kitchen accident slowly, line by line."
TRANSITION = "Now listen to the whole scene again from start to finish."
OUTRO = "Nothing is broken, ice is on Zoya's twisted ankle, and Kira already has a rescue plan for Wednesday morning! See you next time."
CLOSING = ('kira', 'Спокойной ночи!')
STORY = [
    ('kira', 'Зоя, подожди! Давай я подержу табуретку, а ты достанешь до полки.', "Zoya, wait! Let me hold the stool while you reach the shelf."),
    ('zoya', 'Я встаю на неё десять раз в неделю, мне только большой чайник... ой!', 'I stand on it ten times a week, I just need the big teapot... ouch!'),
    ('kira', 'Зоя! Держись за меня! Садись на стул и не вставай!', "Zoya! Hold on to me! Sit down on the chair and don't get up!"),
    ('zoya', 'Ой-ой... нога соскользнула, когда я спускалась.', 'Oh, oh... my foot slipped when I was stepping down.'),
    ('kira', 'Давай я осторожно сниму туфлю. Пальцами можешь пошевелить?', 'Let me carefully take off your shoe. Can you wiggle your toes?'),
    ('zoya', 'Пальцы двигаются, ничего не сломано. Просто подвернула ногу.', "My toes move, nothing is broken. I just twisted my ankle."),
    ('kira', 'Положи ногу на второй стул, а я заверну лёд в чистое полотенце.', "Put your foot up on the second chair, and I'll wrap ice in a clean towel."),
    ('zoya', 'Нет, нет, Кира! Завтра среда! Мне нужно сварить суп и испечь двадцать пирогов!', 'No, no, Kira! Tomorrow is Wednesday! I have to make soup and bake twenty tarts!'),
    ('kira', 'Если ты сегодня встанешь на больную ногу, ты две недели не будешь ходить!', "If you stand on a sore foot tonight, you won't walk for two weeks!"),
    ('zoya', 'А кто испечёт хлеб и сделает лимонный крем, если я буду сидеть?', 'And who will bake the bread and make the lemon cream if I am sitting down?'),
    ('kira', 'Посмотри вокруг, Зоя: в доме шесть пар рук и один громкий голос!', 'Look around, Zoya: the house has six pairs of hands and one loud voice!'),
    ('zoya', 'Подожди... ты хочешь, чтобы я сидела на подушке и командовала всеми?', 'Wait... you want me to sit on a cushion and boss everyone around?'),
]
WALK = [
    (0, None, ["'Zoya, wait! Let me hold the stool while you reach the shelf.' Offering help starts with ", (None, 'Давай я'), ", 'let me', a friendly chunk you can finish with any verb."]),
    (1, None, ["'I stand on it ten times a week, I just need the big teapot... ouch!' How often goes with 'in': ", (None, 'десять раз в неделю,'), " is 'ten times a week'."]),
    (2, None, ["'Zoya! Hold on to me! Sit down on the chair and don't get up!' Holding on 'behind' someone is ", (None, 'Держись за меня!'), ", the casual way to say 'grab hold of me'."]),
    (3, None, ["'Oh, oh... my foot slipped when I was stepping down.' Russian uses one word for leg and foot: ", (None, 'нога'), " covers everything from hip to toes."]),
    (4, None, ["'Let me carefully take off your shoe. Can you wiggle your toes?' Toes are simply 'fingers' in Russian: ", (None, 'Пальцами'), " works for both hands and feet."]),
    (5, None, ["'My toes move, nothing is broken. I just twisted my ankle.' The good news comes in three words: ", (None, 'ничего не сломано.'), " Russian needs both 'nothing' and 'not'."]),
    (6, None, ["'Put your foot up on the second chair, and I'll wrap ice in a clean towel.' Ice is the short word ", (None, 'лёд'), ", and it loses its middle vowel in other forms."]),
    (7, None, ["'No, no, Kira! Tomorrow is Wednesday! I have to make soup and bake twenty tarts!' Soup is 'boiled' in Russian: ", (None, 'сварить суп'), " uses the verb for boiling."]),
    (8, None, ["'If you stand on a sore foot tonight, you won't walk for two weeks!' A sore foot is a 'sick' one: ", (None, 'больную ногу,'), " from the same word as being ill."]),
    (9, None, ["'And who will bake the bread and make the lemon cream if I am sitting down?' The future of a long action uses 'will be' plus the verb: ", (None, 'я буду сидеть'), "."]),
    (10, None, ["'Look around, Zoya: the house has six pairs of hands and one loud voice!' Pairs of things are ", (None, 'шесть пар рук'), ", 'six pairs of hands', each word in its 'of' form."]),
    (11, None, ["'Wait... you want me to sit on a cushion and boss everyone around?' Wanting someone else to act takes ", (None, 'чтобы'), " plus a past form: 'you want that I sat'."]),
]
