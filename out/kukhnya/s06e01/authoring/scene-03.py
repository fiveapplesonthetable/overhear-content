ID = 'kukhnya-s06e01-scene-03'
SHOW = "kukhnya"
SEASON = 6
EPISODE = 1
SCENE = 3
TITLE = 'Семейный рецепт печенья  (The Family Cookie Recipe)'
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {'narrator': 'sky', 'anya': 'alisa', 'guest': 'angelina'}
LABELS = {'anya': 'Шеф', 'guest': 'Гость'}
SOURCE_NAME = "Кухня (Kukhnya) S6.01"
SOURCE_FILE = 'sources/kukhnya/s06/e01.ru.srt'

INTRO = "Resting in his office, Chef Barinov is startled by the sudden appearance of Eleonora's formidable mother Elizaveta Genrikhovna, who demands that his kitchen bake wedding cookies from an old family recipe."

STORY = [
    ('anya', 'Что вы тут делаете?', 'What are you doing here?', [(29, 'что вы тут делаете')], 'adapted'),
    ('guest', 'Моя дочь выходит замуж.', 'My daughter is getting married.', [(30, 'моя дочь выходит замуж')], 'adapted'),
    ('guest', 'Мое присутствие более чем логично.', 'My presence is more than logical.', [(31, 'мое присутствие более чем логично')], 'exact'),
    ('anya', 'Замуж она выходит не в моем кабинете.', 'She is not getting married in my office.', [(33, 'замуж она выходит не в моем кабинете')], 'adapted'),
    ('guest', 'Да, конечно.', 'Yes, of course.', [(34, 'Да, конечно')], 'exact'),
    ('anya', 'У вас ко мне какое-то дело?', 'Do you have some business with me?', [(36, 'У вас ко мне какое-то дело')], 'exact'),
    ('anya', 'Или вы просто соскучились?', 'Or did you simply miss me?', [(37, 'Или вы просто соскучились')], 'exact'),
    ('anya', 'Короче, что вам нужно?', 'In short, what do you need?', [(41, 'Короче, что вам нужно')], 'exact'),
    ('guest', 'Не знаю, помнишь ты или нет.', 'I do not know whether you remember or not.', [(42, 'Не знаю, помнишь ты или нет')], 'exact'),
    ('guest', 'В нашей семье есть традиция.', 'In our family there is a tradition.', [(42, 'в нашей семье есть традиция')], 'adapted'),
    ('guest', 'Делать печенье по семейному рецепту.', 'To make cookies from the family recipe.', [(43, 'Делать печенье')], 'adapted'),
    ('guest', 'И я хочу, чтобы повара испекли это печенье.', 'And I want the chefs to bake these cookies.', [(44, 'испекли это печенье к банкету')], 'adapted'),
]

OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."

WALK = [
    (0, None, "'What are you doing here?' Chef Barinov raises the pitch on 'are doing' to turn the phrase into a direct spoken question. the guest answers right away."),
    (1, None, "'My daughter is getting married.' In Russian, the idea of 'my' flows naturally into 'married' without extra filler words."),
    (2, None, "'My presence is more than logical.' Spoken Russian keeps this brisk, leaning on 'my' and finishing on 'logical'."),
    (3, None, "'She is not getting married in my office.' Notice how Russian expresses 'married' and 'office' with crisp inflection rather than helper words. the guest answers right away."),
    (4, None, "'Yes, of course.' Here the Russian phrasing highlights 'yes' before landing on 'of course'."),
    (5, None, "'Do you have some business with me?' Here the Russian phrasing highlights 'at' before landing on 'business'."),
    (6, None, "'Or did you simply miss me?' Spoken Russian keeps this brisk, leaning on 'or' and finishing on 'missed'."),
    (7, None, "'In short, what do you need?' Chef Barinov brings out the contrast between 'long story short' and 'what' in a few short words."),
    (8, None, "'I do not know whether you remember or not.' the guest addresses the listener with the informal singular 'you' alongside 'no'."),
    (9, None, "'In our family there is a tradition.' In Russian, the idea of 'our' flows naturally into 'tradition' without extra filler words."),
    (10, None, "'To make cookies from the family recipe.' Spoken Russian keeps this brisk, leaning on 'to do' and finishing on 'recipe'."),
    (11, None, "'And I want the chefs to bake these cookies.' The grammar packs 'and' and 'cookies' into a tight, idiomatic kitchen exchange."),
]

TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "She leaves the handwritten cookie recipe on Barinov's desk and expects it ready in time for the wedding feast. See you in the next scene."
CLOSING = ('guest', 'Вот рецепт.')
