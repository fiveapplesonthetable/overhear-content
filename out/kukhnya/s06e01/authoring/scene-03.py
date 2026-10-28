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
    (0, None, '\'What are you doing here?\' By asking what the guest doing here is, Barinov presses the guest for a straight answer. Notice how he sticks to the formal "you", keeping a professional line between them.'),
    (1, None, "'My daughter is getting married.' Admitting that his daughter is getting married shows the guest being honest for a change."),
    (2, None, "'My presence is more than logical.' Saying that his presence is more than logical is how the guest sets the tone with Barinov."),
    (3, None, "'She is not getting married in my office.' Once she is not getting married in his office, Barinov can finally tell the guest what he means."),
    (4, None, "'Yes, of course.' Over the banquet and the conversation, the guest answers Barinov without a second thought."),
    (5, None, '\'Do you have some business with me?\' Here checking whether the guest has some business with him shows Barinov looking for the real truth. Russian expresses having something as "by me is", keeping the phrase short and grounded.'),
    (6, None, '\'Or did you simply miss me?\' By asking whether the guest simply miss him, Barinov presses the guest for a straight answer. Notice how he sticks to the formal "you", keeping a professional line between them.'),
    (7, None, "'In short, what do you need?' Asking whether in short what do the guest needs puts the guest right on the defensive."),
    (8, None, '\'I do not know whether you remember or not.\' Because he does not know whether Barinov remembers or not, the guest treats the matter as settled. Speaking with the close, informal "you" strips away any polite distance between them.'),
    (9, None, "'In our family there is a tradition.' Because in their family there is a tradition, the guest treats the matter as settled."),
    (10, None, "'To make cookies from the family recipe.' Around the shift and family, the guest sets a calm, everyday tone with Barinov."),
    (11, None, '\'And I want the chefs to bake these cookies.\' Realizing that he wants the chefs to bake these cookies changes how the guest handles the situation. Russian drops "is" in the present, setting the two halves of the thought side by side.'),
]
