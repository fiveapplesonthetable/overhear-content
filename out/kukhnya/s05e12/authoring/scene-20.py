# Authoring module for kukhnya-s05e12-scene-20.
ID = 'kukhnya-s05e12-scene-20'
SHOW = 'kukhnya'
SEASON = 5
EPISODE = 12
SCENE = 20
TITLE = 'Выходи за меня  (Marry Me)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'kostya': 'Костя', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S5.12'
SOURCE_FILE = 'sources/kukhnya/s05/e12.ru.srt'
INTRO = "Chasing Elena's taxi in a white horse-drawn carriage, Chef Barinov holds out the ring and asks her to marry him for real. Although Max and Vika's divorce is finalized the next day, Max believes a miracle is still possible—while Kostya role-plays as Masseur Konstantin for Nastya."
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "And that brings Episode Twelve of Season Five to an unforgettable conclusion. Listen for Viktor's marriage proposal—marry me—and Max's hope that a miracle will still happen. See you next time!"
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('max', 'Отпусти меня!', 'Let me go!', [(299, 'Отпусти меня')], 'adapted'),
    ('max', 'Говорят, что мысли материальны.', 'They say that thoughts are material.', [(300, 'Говорят, что мысли материальны')], 'adapted'),
    ('max', 'Если признаться себе в том, чего по-настоящему хочешь.', 'If you admit to yourself what you truly want.', [(301, 'Если признаться себе в том, чего по-настоящему хочешь')], 'adapted'),
    ('max', 'Возможно, чудо произойдёт.', 'Perhaps a miracle will happen.', [(302, 'Возможно, чудо произойдет')], 'adapted'),
    ('barinov', 'Выходи за меня!', 'Marry me!', [(303, 'Выходи за меня')], 'adapted'),
    ('max', 'Теперь ваш брак официально расторгнут.', 'Now your marriage is officially dissolved.', [(304, 'Теперь ваш брак официально')], 'adapted'),
    ('max', 'Но я не сдаюсь.', 'But I am not giving up.', [(302, 'чудо произойдет')], 'adapted'),
    ('max', 'Здравствуйте, можно заказать массаж?', 'Hello, can I order a massage?', [(305, 'Здравствуйте. Можно заказать массаж')], 'adapted'),
    ('max', 'Плюс интимные услуги?', 'Plus intimate services?', [(305, 'плюс интимные услуги')], 'adapted'),
    ('kostya', 'Ну конечно можно!', 'Well of course you can!', [(306, 'Ну, конечно, можно')], 'adapted'),
    ('max', 'Массажист Константин уже выезжает!', 'Masseur Konstantin is already on his way!', [(307, 'Массажист Константин уже выезжает')], 'adapted'),
    ('max', 'Жду вас с нетерпением!', 'I am waiting for you impatiently!', [(306, 'конечно, можно')], 'adapted'),
]
WALK = [
    (0, None, "'Let me go!' Max directs this update calmly now: spoken Russian trims this down to just 2 words, dropping the extra helper words that English has to spell out."),
    (1, None, "'They say that thoughts are material.' Max weighs in decisively watching Kostya, bringing things back to earth after the buildup."),
    (2, None, '\'If you admit to yourself what you truly want.\' Max frames one loaded term on cue: "po-nastoyashchemu" means "truly", and it carries the main weight of what Max is saying.'),
    (3, None, "'Perhaps a miracle will happen.' Max gives the comment with warmth: spoken Russian trims this down to just 3 words, dropping the extra helper words that English has to spell out."),
    (4, None, "'Marry me!' Barinov speaks plainly on the spot, making his position completely clear."),
    (5, None, '\'Now your marriage is officially dissolved.\' Max features one vivid touch right here: "ofitsialno" means "official, officially", and it carries the main weight of what Max is saying.'),
    (6, None, '\'But I am not giving up.\' Max shapes the comment on cue: the "-sya" ending on "sdayus" ("to give up") turns the action inward or makes it happen between people naturally.'),
    (7, None, "'Hello, can I order a massage?' Max questions point-blank if there is more going on behind the scenes."),
    (8, None, '\'Plus intimate services?\' Max points to one vivid term with Barinov: "intimnyye" means "intimate" (from "intimnyy"), giving the line its exact edge.'),
    (9, None, '\'Well of course you can!\' Kostya shapes this point right away: the single Russian word "mozhno" ("it is possible, one may") sets up the whole statement without needing a separate word for "it is".'),
    (10, None, "'Masseur Konstantin is already on his way!' Max speaks up boldly to settle things, before Barinov can change the subject."),
    (11, None, '\'I am waiting for you impatiently!\' Max uses one loaded detail with Kostya: "neterpeniyem" means "to forward" (from "neterpenit"), giving the line its exact edge.'),
]
