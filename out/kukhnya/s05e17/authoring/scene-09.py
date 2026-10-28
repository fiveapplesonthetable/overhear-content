# Authoring module for kukhnya-s05e17-scene-09.
ID = 'kukhnya-s05e17-scene-09'
SHOW = 'kukhnya'
SEASON = 5
EPISODE = 17
SCENE = 9
TITLE = 'Три неудачных варианта  (Three Failed Options)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'katya': 'Катя', 'nagiyev': 'Нагиев', 'nikita': 'Никита'}
SOURCE_NAME = 'Кухня (Kukhnya) S5.17'
SOURCE_FILE = 'sources/kukhnya/s05/e17.ru.srt'
INTRO = "Nikita mentally runs through absurd ways to steal Nagiyev's keys—from sleeping pills to faking a heart attack—before grabbing them while Nagiyev steps away, only to get caught immediately."
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "Embarrassed in front of Katya, Nikita receives unexpected help from Katya's mother Eleonora. Until next time!"
CLOSING = ('katya', 'Пока не получилось?')
STORY = [
    ('nikita', 'Где я сейчас снотворное возьму?', 'Where am I going to get sleeping pills right now?', [(165, 'где ты сейчас снотворное возьмёшь')], 'adapted'),
    ('nikita', 'Тогда пробуем вариант номер два.', "Then let's try option number two.", [(167, 'тогда вариант два')], 'adapted'),
    ('nikita', 'Помогите, нужно в скорую звонить!', 'Help, we need to call an ambulance!', [(170, 'Помогите. Скорую звонить')], 'adapted'),
    ('nagiyev', 'У меня же телефон вон лежит.', 'My phone is lying right over there.', [(175, 'У меня же телефон вон лежит')], 'adapted'),
    ('nikita', 'Тогда у меня варианты закончились.', 'Then I have run out of options.', [(180, 'Тогда на этом у меня варианты закончились')], 'adapted'),
    ('nagiyev', 'Ну ладно, сегодня победил лосось.', 'Alright then, today the salmon won.', [(181, 'Ну ладно'), (182, 'Победил лосось')], 'adapted'),
    ('nikita', 'Зачем он мне это сказал?', 'Why did he tell me that?', [(184, 'Зачем я ему это сказал')], 'adapted'),
    ('nagiyev', 'Никита, ты зачем ключи от машины взял?', 'Nikita, why did you take the car keys?', [(187, 'Никита, а ты зачем ключи от машины взял')], 'adapted'),
    ('katya', 'Ну что, пока не получилось?', 'Well, did it not work out yet?', [(189, 'Ну'), (190, 'Пока не получилось')], 'adapted'),
    ('nikita', 'Да, пока ничего не вышло.', 'Yes, nothing worked out yet.', [(190, 'Пока не получилось'), (191, 'Да')], 'adapted'),
    ('katya', 'Врёшь ты лучше, чем тачки угоняешь.', 'You lie much better than you steal cars.', [(191, 'Врешь ты куда лучше, чем тачки угоняешь')], 'adapted'),
    ('nikita', 'Подожди, я обязательно достану ключи.', 'Wait, I will definitely get the keys.', [(187, 'ключи от машины')], 'adapted'),
]
WALK = [
    (0, None, "'Where am I going to get sleeping pills right now?' Nikita tests curiously about what Nagiyev just brought up."),
    (1, None, '\'Then let\'s try option number two.\' Mentioning the option with Nagiyev, Nikita chooses "variant" ("option, variant") so Nagiyev gets the point right away.'),
    (2, None, '\'Help, we need to call an ambulance!\' Returning to an ambulance during the talk, Nikita leans on "nuzhno" ("it is needed, one has to"), which carries the whole predicate in Russian without needing "it is".'),
    (3, None, "'My phone is lying right over there.' Nagiyev cuts in at once watching Nikita, making his position completely clear."),
    (4, None, '\'Then I have run out of options.\' Emphasizing the option in the exchange, Nikita brings in "varianty" ("option, variant", from "variant") as the key Russian word here.'),
    (5, None, '\'Alright then, today the salmon won.\' Underscoring the salmon on the spot, Nagiyev uses "segodnya" ("today") to carry the main weight of the thought.'),
    (6, None, "'Why did he tell me that?' Nikita checks quietly where this conversation is heading next."),
    (7, None, '\'Nikita, why did you take the car keys?\' Talking about the car keys beside Nikita, Nagiyev uses "klyuchi" ("the keys", from "klyuch") to make the point stick.'),
    (8, None, '\'Well, did it not work out yet?\' Replying earnestly at once, the "-sya" ending on "poluchilos" ("worked out") marks an action that unfolds mutually or turns back on the speaker.'),
    (9, None, "'Yes, nothing worked out yet.' Nikita fires back honestly during the talk, testing Katya's reaction in the middle of the exchange."),
    (10, None, '\'You lie much better than you steal cars.\' Highlighting the car beside Nikita, Katya reaches for the Russian word "ugonyayesh" ("you steal", built from "ugonyat") right at the center of the line.'),
    (11, None, '\'Wait, I will definitely get the keys.\' Focusing on the keys at once, Nikita puts the emphasis on "obyazatelno" ("surely, without fail") in the middle of the talk.'),
]
