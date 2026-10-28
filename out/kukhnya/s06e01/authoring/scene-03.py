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
    (0, None, "'What are you doing here?' Barinov questions quietly what the guest is actually getting at here."),
    (1, None, '\'My daughter is getting married.\' The guest focuses on this vivid term with Barinov: "vykhodit" means "goes out", and it carries the main weight of what the guest is saying.'),
    (2, None, '\'My presence is more than logical.\' The guest voices this warning without fuss: notice how Russian needs no word for "am", "is", or "are" in the present — placing the words side by side says it all.'),
    (3, None, "'She is not getting married in my office.' Barinov follows up lightly hearing the guest, leaving no doubt about where he stands."),
    (4, None, '\'Yes, of course.\' The guest highlights this telling detail on cue: "konechno" means "of course", and it carries the main weight of what the guest is saying.'),
    (5, None, '\'Do you have some business with me?\' Barinov aims that point right away: using "u vas" (literally "by you") is how Russian politely asks or talks about what someone has on their side.'),
    (6, None, "'Or did you simply miss me?' Barinov probes earnestly how the guest expects that to work in practice."),
    (7, None, '\'In short, what do you need?\' Barinov centers one vivid expression at once: "koroche" means "long story short", and it carries the main weight of what Barinov is saying.'),
    (8, None, '\'I do not know whether you remember or not.\' The guest chooses this direct choice at once: "pomnish" means "do you remember" (from "pomnit"), giving the line its exact edge.'),
    (9, None, "'In our family there is a tradition.' The guest speaks up steadily in their talk, keeping the focus on what actually matters here."),
    (10, None, '\'To make cookies from the family recipe.\' The guest underscores this telling term in earnest: "semeynomu" means "family" (from "semeynyy"), giving the line its exact edge.'),
    (11, None, "'And I want the chefs to bake these cookies.' The guest stands firm right away on the spot, saying out loud what both of them already know."),
]
