# Authoring module for kukhnya-s01e09-scene-13.
ID = 'kukhnya-s01e09-scene-13'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 9
SCENE = 13
TITLE = 'Полная тишина  (Absolute Silence)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'lyova': 'Лёва'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.09'
SOURCE_FILE = 'sources/kukhnya/s01/e09.ru.dual.srt'
INTRO = 'Barinov is out of ideas, so he does the one thing a Russian chef can do: he orders silence. The whole kitchen freezes while he listens for his daughter. Listen out for the little words.'
OPENER = "Let's see how it's put together."
TRANSITION = 'Now it should sound clearer.'
OUTRO = 'The kitchen is silent, and then they find her. Whatever she has in her hands will be a problem. See you soon.'
CLOSING = ('lyova', 'Пока!')
STORY = [
    ('barinov', 'Тихо все, мне нужна полная тишина!', 'Quiet everyone, I need complete silence!', [(282, 'Тихо все, полная тишина')], ''),
    ('lyova', 'Шеф, мы уже выключили все шумные приборы.', 'Chef, we have already turned off all noisy equipment.', [(284, 'Выключили все приборы')], ''),
    ('barinov', 'Молчать, я требую абсолютного спокойствия на кухне.', 'Be quiet, I demand absolute calm in the kitchen.', [(283, 'Молчать')], ''),
    ('lyova', 'Все повара замолчали и стоят на месте.', 'All the cooks fell silent and are standing in place.', [(285, 'Все заткнулись')], ''),
    ('barinov', 'Не дышать, я хочу слышать каждый тихий звук.', 'Do not breathe, I want to hear every quiet sound.', [(286, 'Не дышать')], ''),
    ('lyova', 'Вы уверены, что наша маленькая гостья здесь?', 'Are you sure our little guest is here?', [(286, 'Мне нужна полная гробовая тишина')], ''),
    ('barinov', 'Она точно где-то спряталась в этом зале.', 'She definitely hid somewhere in this dining room.', [(286, 'Мне нужна полная')], ''),
    ('lyova', 'Я слышу странный лёгкий шорох возле стола.', 'I hear a strange faint rustling near the table.', [(286, 'полная гробовая тишина')], ''),
    ('barinov', 'Кто сейчас стоит там около большого холодильника?', 'Who is standing there near the big refrigerator right now?', [(287, 'Инвалид')], ''),
    ('lyova', 'Там никого нет, только большие коробки продуктов.', 'There is no one there, only large boxes of groceries.', [(286, 'гробовая тишина')], ''),
    ('barinov', 'Смотри внимательно, девочка сидит прямо под столом!', 'Look carefully, the girl is sitting right under the table!', [(286, 'Мне нужна')], ''),
    ('lyova', 'Какое счастье, мы наконец нашли нашу пропажу!', 'What joy, we finally found our missing one!', [(286, 'тишина')], ''),
]
WALK = [
    (0, None, ["'Quiet everyone, I need complete silence!' Here we hear him demand complete ", ('barinov', 'тишина'), ', which means silence and sets the entire mood.']),
    (1, None, ["'Chef, we have already turned off all noisy equipment.' The second in command confirms they ", ('lyova', 'выключили'), ' or turned off the annoying kitchen appliances.']),
    (2, None, ["'Be quiet, I demand absolute calm in the kitchen.' To demand absolute quiet, he simply says ", ('barinov', 'Молчать'), ' to tell everyone to completely shut up.']),
    (3, None, ["'All the cooks fell silent and are standing in place.' As expected, all the cooks instantly ", ('lyova', 'замолчали'), ' and stopped making any sound at all.']),
    (4, None, ["'Do not breathe, I want to hear every quiet sound.' He is listening so closely for ", ('barinov', 'каждый'), ' single sound that might reveal her location.']),
    (5, None, ["'Are you sure our little guest is here?' His worried colleague mentions their little ", ('lyova', 'гостья'), ', the female visitor they are desperately seeking.']),
    (6, None, ["'She definitely hid somewhere in this dining room.' Since she is missing, she definitely ", ('barinov', 'спряталась'), ' or hid away somewhere in this room.']),
    (7, None, ["'I hear a strange faint rustling near the table.' A faint noise is heard, a ", ('lyova', 'шорох'), ' which is just a very light rustle.']),
    (8, None, ["'Who is standing there near the big refrigerator right now?' The angry chef looks over at the ", ('barinov', 'холодильника'), ' which is the big cooling machine nearby.']),
    (9, None, ["'There is no one there, only large boxes of groceries.' But the large space is empty, with ", ('lyova', 'никого'), ' meaning nobody is standing around at all.']),
    (10, None, ["'Look carefully, the girl is sitting right under the table!' He tells his friend to look very ", ('barinov', 'внимательно'), ' and pay close attention to the bottom.']),
    (11, None, ["'What joy, we finally found our missing one!' They finally found their lost thing, the ", ('lyova', 'пропажу'), ', bringing a huge sense of shared relief.']),
]
