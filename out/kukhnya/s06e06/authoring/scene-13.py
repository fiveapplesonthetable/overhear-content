# Authoring module for kukhnya-s06e06-scene-13.
ID = 'kukhnya-s06e06-scene-13'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 6
SCENE = 13
TITLE = 'Полиция в номере  (Police in the Room)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'guest': 'Гость', 'inspector': 'Инспектор'}
SOURCE_NAME = 'Кухня (Kukhnya) S6.06'
SOURCE_FILE = 'sources/kukhnya/s06/e06.ru.srt'
INTRO = "Right as the police knock on Olivier's hotel room door, Chef Barinov arrives out of breath in his white chef's coat and improvises a wild cover story. Listen to the full conversation in Russian first, and then we will walk through every line together."
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "Putting on his best air of authority, Chef Barinov tries to talk the baffled police officers out of searching Olivier's luggage. Until next time!"
CLOSING = ('barinov', 'До завтра!')
STORY = [
    ('inspector', 'Немедленно откройте дверь, это полиция!', 'Open the door immediately, this is the police!', [(200, 'Откройте полицию')], 'adapted'),
    ('inspector', 'Скажите, это ваш гостиничный номер?', 'Tell me, is this your hotel room?', [(202, 'ваш номер')], 'adapted'),
    ('guest', 'Простите, я вас совсем не понимаю.', 'Excuse me, I do not understand you at all.', [(203, 'Я вас не понимаю')], 'adapted'),
    ('barinov', 'А что тут вообще сейчас происходит?', 'And what on earth is going on here right now?', [(205, 'А что тут происходит')], 'adapted'),
    ('barinov', 'Почему я до сих пор не в курсе?', 'Why have I not been informed yet?', [(206, 'Почему я не в курсе')], 'adapted'),
    ('guest', 'Я не понимаю, что они хотят.', 'I do not understand what they want.', [(206, 'Я не понимаю, что они от меня хотят')], 'adapted'),
    ('inspector', 'Простите, а вы сами кто такой?', 'Excuse me, and who are you yourself?', [(207, 'Вы кто такой')], 'adapted'),
    ('barinov', 'Я главный управляющий этого отеля.', 'I am the general manager of this hotel.', [(209, 'Управляющий этого отеля')], 'adapted'),
    ('inspector', 'А почему вы тогда в колпаке?', "Then why are you wearing a chef's hat?", [(210, 'А почему'), (211, 'В колпаке')], 'adapted'),
    ('barinov', 'Потому что я ещё и шеф-повар.', 'Because I am also the head chef.', [(211, 'И шеф-повар')], 'adapted'),
    ('barinov', 'Сейчас кризис, поэтому приходится совмещать.', 'There is a crisis now, so I have to combine jobs.', [(212, 'Кризис'), (213, 'Приходится совмещать')], 'adapted'),
    ('barinov', 'А ещё я муж хозяйки отеля.', 'And I am also the husband of the hotel owner.', [(214, 'А еще я муж хозяйки этого отеля')], 'adapted'),
]
WALK = [
    (0, None, '\'Open the door immediately, this is the police!\' Mentioning the police at once, the inspector leans on "politsiya" ("police") to give the whole sentence its punch.'),
    (1, None, "'Tell me, is this your hotel room?' Highlighting how hotel things are in the exchange, the inspector keeps normal statement word order here, turning the line into a question for the guest purely through rising pitch."),
    (2, None, "'Excuse me, I do not understand you at all.' The guest weighs in candidly with a shrug, to clear the air between them once and for all."),
    (3, None, '\'And what on earth is going on here right now?\' Barinov jumps in warmly in the exchange and uses "proiskhodit" ("is going on") to carry the main weight of the thought.'),
    (4, None, '\'Why have I not been informed yet?\' Checking on the course in front of the guest, Barinov puts the question word "pochemu" right at the start so the guest hears the focus immediately.'),
    (5, None, "'I do not understand what they want.' The guest replies calmly without any doubt, bringing things back to earth after the buildup."),
    (6, None, '\'Excuse me, and who are you yourself?\' The inspector speaks naturally on the spot and puts the weight on "prostite" ("excuse me", from "prostit") as the exchange unfolds.'),
    (7, None, '\'I am the general manager of this hotel.\' Addressing the general manager at once, Barinov links the Russian words directly in the present with no word for "am", "is", or "are" needed.'),
    (8, None, "'Then why are you wearing a chef's hat?' The inspector prompts promptly what Barinov is actually getting at here."),
    (9, None, '\'Because I am also the head chef.\' Underscoring the head around the inspector, Barinov uses "shef-povar" ("head chef") to carry the main weight of the thought.'),
    (10, None, '\'There is a crisis now, so I have to combine jobs.\' Touching on a crisis beside the inspector, the "-sya" ending on "prikhoditsya" ("to have to") marks an action that unfolds mutually or turns back on the speaker.'),
    (11, None, "'And I am also the husband of the hotel owner.' Barinov weighs in openly across the room, refusing to let the moment slip past."),
]
