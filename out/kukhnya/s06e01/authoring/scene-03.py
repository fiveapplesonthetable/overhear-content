# Authoring module for kukhnya-s06e01-scene-03.
ID = 'kukhnya-s06e01-scene-03'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 1
SCENE = 3
TITLE = 'Семейный рецепт печенья  (The Family Cookie Recipe)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'guest': 'Гость'}
SOURCE_NAME = 'Кухня (Kukhnya) S6.01'
SOURCE_FILE = 'sources/kukhnya/s06/e01.ru.srt'
INTRO = "Resting in his office, Chef Barinov is startled by the sudden appearance of Eleonora's formidable mother Elizaveta Genrikhovna, who demands that his kitchen bake wedding cookies from an old family recipe."
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "She leaves the handwritten cookie recipe on Barinov's desk and expects it ready in time for the wedding feast. Until next time!"
CLOSING = ('guest', 'Пока!')
STORY = [
    ('barinov', 'Что вы тут делаете?', 'What are you doing here?', [(29, 'что вы тут делаете')], 'adapted'),
    ('guest', 'Моя дочь выходит замуж.', 'My daughter is getting married.', [(30, 'моя дочь выходит замуж')], 'adapted'),
    ('guest', 'Мое присутствие более чем логично.', 'My presence is more than logical.', [(31, 'мое присутствие более чем логично')], 'exact'),
    ('barinov', 'Замуж она выходит не в моем кабинете.', 'She is not getting married in my office.', [(33, 'замуж она выходит не в моем кабинете')], 'adapted'),
    ('guest', 'Да, конечно.', 'Yes, of course.', [(34, 'Да, конечно')], 'exact'),
    ('barinov', 'У вас ко мне какое-то дело?', 'Do you have some business with me?', [(36, 'У вас ко мне какое-то дело')], 'exact'),
    ('barinov', 'Или вы просто соскучились?', 'Or did you simply miss me?', [(37, 'Или вы просто соскучились')], 'exact'),
    ('barinov', 'Короче, что вам нужно?', 'In short, what do you need?', [(41, 'Короче, что вам нужно')], 'exact'),
    ('guest', 'Не знаю, помнишь ты или нет.', 'I do not know whether you remember or not.', [(42, 'Не знаю, помнишь ты или нет')], 'exact'),
    ('guest', 'В нашей семье есть традиция.', 'In our family there is a tradition.', [(42, 'в нашей семье есть традиция')], 'adapted'),
    ('guest', 'Делать печенье по семейному рецепту.', 'To make cookies from the family recipe.', [(43, 'Делать печенье')], 'adapted'),
    ('guest', 'И я хочу, чтобы повара испекли это печенье.', 'And I want the chefs to bake these cookies.', [(44, 'испекли это печенье к банкету')], 'adapted'),
]
WALK = [
    (0, None, "'What are you doing here?' Barinov questions quietly how the guest expects that to work in practice."),
    (1, None, '\'My daughter is getting married.\' Underscoring his daughter during the talk, the guest brings in "vykhodit" ("goes out") to make the meaning unmistakable.'),
    (2, None, '\'My presence is more than logical.\' Mentioning his presence with Barinov, the guest links the Russian words directly in the present with no word for "am", "is", or "are" needed.'),
    (3, None, "'She is not getting married in my office.' Barinov opens up lightly with the guest, grounding the moment in plain reality."),
    (4, None, '\'Yes, of course.\' The guest casually speaks this confirmation for Barinov using "konechno" ("of course") — spoken with a soft "shn" sound in everyday Moscow Russian to mean "of course, certainly".'),
    (5, None, "'Do you have some business with me?' Focusing on the matter beside the guest, Barinov keeps normal statement word order here, turning the line into a question for the guest purely through rising pitch."),
    (6, None, "'Or did you simply miss me?' Barinov probes earnestly while looking straight at the guest here."),
    (7, None, '\'In short, what do you need?\' Barinov jumps in candidly on the spot and uses "koroche" ("long story short") to carry the main weight of the thought.'),
    (8, None, "'I do not know whether you remember or not.' The guest chimes in boldly facing Barinov, keeping the focus on what actually matters here."),
    (9, None, "'In our family there is a tradition.' The guest fires back steadily with a shrug, without trying to dress up how he really feels."),
    (10, None, '\'To make cookies from the family recipe.\' Emphasizing the cookies in this beat, the guest chooses "semeynomu" ("family", from the root "semeynyy") so Barinov hears the exact meaning.'),
    (11, None, '\'And I want the chefs to bake these cookies.\' Focusing on the cookies at once, the guest leans on "pechenye" ("cookies, pastry") to give the whole sentence its punch.'),
]
