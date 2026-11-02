# Authoring module for kukhnya-s01e12-scene-12.
ID = 'kukhnya-s01e12-scene-12'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 12
SCENE = 12
TITLE = 'Ссора понарошку  (Pretend Quarrel)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kostya': 'Костя', 'nastya': 'Настя'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.12'
SOURCE_FILE = 'sources/kukhnya/s01/e12.ru.dual.srt'
INTRO = 'Nastya is convinced that the new ban is about her and Kostya, who have been seeing each other in secret. She has an idea: stage a fake quarrel. Hear the plan in Russian first.'
OPENER = 'Slowly, and listen to how Nastya talks him round.'
TRANSITION = 'Now, all the lines together again.'
OUTRO = "Kostya is not sure about this, but he plays along. Ask yourself how well two people who aren't actors can fake an argument. Speak soon."
CLOSING = ('kostya', 'Пока!')
STORY = [
    ('nastya', 'Костя, этот новый запрет из-за нас!', 'Kostya, this new ban is because of us!', [(101, 'Это из-за нас.')], ''),
    ('kostya', 'Но с чего ты это взяла?', 'But what makes you think that?', [(103, 'С чего ты взяла?')], ''),
    ('nastya', 'Потому что только у нас тайные отношения.', 'Because only we have a secret relationship.', [(103, 'Потому что только у нас отношения.')], ''),
    ('kostya', 'Виктория просто заботится о дисциплине зала.', 'Victoria simply cares about the dining room discipline.', [], ''),
    ('nastya', 'Она очень подозрительно посмотрела на нас.', 'She looked at us very suspiciously.', [(104, 'она вот так посмотрела.')], ''),
    ('kostya', 'Тебе показалось, она смотрела на всех.', 'You imagined it, she was looking at everyone.', [], ''),
    ('nastya', 'Я прекрасно знаю этот строгий взгляд!', 'I know that strict look very well!', [(105, 'Я знаю этот взгляд.')], ''),
    ('kostya', 'И что же нам теперь делать?', 'And what should we do now?', [], ''),
    ('nastya', 'Нам нужно срочно поругаться перед ней.', 'We need to quarrel in front of her right away.', [(106, 'Нам надо поругаться.')], ''),
    ('kostya', 'Зачем нам ругаться в ресторане?', 'Why should we quarrel in the restaurant?', [(106, 'Как поругаться?')], ''),
    ('nastya', 'Мы поругаемся понарошку, только для вида.', 'We will quarrel in pretend, only for show.', [(107, 'Ну, понарошку...'), (108, 'а сейчас поругаемся понарошку.')], ''),
    ('kostya', 'Ты уверена, что это хороший план?', 'Are you sure that this is a good plan?', [], ''),
    ('nastya', 'Вика должна поверить, что мы расстались.', 'Vika must believe that we broke up.', [(109, 'Но главное, чтобы Виктория Сергеевна подумала, что мы не встречаемся.')], ''),
    ('kostya', 'Хорошо, давай устроим этот спектакль.', 'All right, let us put on this show.', [(110, 'Давай.')], ''),
]
WALK = [
    (0, None, ["'Kostya, this new ban is because of us!' Let us inspect the words: ", ('nastya', 'из'), '-', ('nastya', 'за'), ('nastya', 'нас'), " for 'because of us'. The first word means 'because of' for a bad cause, and 'we' changes its ending after it."]),
    (1, None, ["'But what makes you think that?' Let us examine this part: ", ('kostya', 'с'), ('kostya', 'чего'), " says 'from what', which is how Russians ask 'what makes you say that?'. And ", ('kostya', 'взяла'), " is 'took', with an ending showing the speaker is a woman."]),
    (2, None, ["'Because only we have a secret relationship.' Russians use ", ('nastya', 'у'), ('nastya', 'нас'), " to say 'we have'. In the sense of a romance, relationships are plural, so 'secret' is plural too in ", ('nastya', 'тайные'), ('nastya', 'отношения'), '.']),
    (3, None, ["'Victoria simply cares about the dining room discipline.' Now we can analyze the words: ", ('kostya', 'заботится'), ('kostya', 'о'), " for 'cares about'. This verb always carries a reflexive ending, and after the preposition, 'discipline' takes a new ending."]),
    (4, None, ["'She looked at us very suspiciously.' The verb ", ('nastya', 'посмотрела'), " is a completed action: one look, done. The ending shows 'she' did it. We also hear ", ('nastya', 'подозрительно'), " for 'suspiciously'."]),
    (5, None, ["'You imagined it, she was looking at everyone.' The verb ", ('kostya', 'смотрела'), " means 'was looking', implying she kept looking. Compare it with Nastya's single glance earlier. We hear ", ('kostya', 'Тебе'), ('kostya', 'показалось'), " means 'it seemed to you'."]),
    (6, None, ["'I know that strict look very well!' Let us break down the phrase: ", ('nastya', 'прекрасно'), " means 'beautifully', but here it means 'perfectly well'. And ", ('nastya', 'этот'), ('nastya', 'строгий'), ('nastya', 'взгляд'), " is 'that strict look', keeping its plain shape."]),
    (7, None, ["'And what should we do now?' The line is 'what to us to do', which covers 'what should we do'. The short term ", ('kostya', 'же'), ' makes it urgent.']),
    (8, None, ["'We need to quarrel in front of her right away.' On its own, the verb means 'to scold', but ", ('nastya', 'поругаться'), " means 'to have a row' with each other. We hear ", ('nastya', 'перед'), ('nastya', 'ней'), " for 'in front of her'."]),
    (9, None, ["'Why should we quarrel in the restaurant?' Let us look at the speech: ", ('kostya', 'ругаться'), " for 'to quarrel', while Nastya's previous word was its completed partner, one quarrel and done. And ", ('kostya', 'в'), ('kostya', 'ресторане'), " is 'in the restaurant'."]),
    (10, None, ["'We will quarrel in pretend, only for show.' The term ", ('nastya', 'понарошку'), " is 'just pretend', like kids use in games. We hear ", ('nastya', 'для'), ('nastya', 'вида'), " for 'for appearance', or 'for the look'."]),
    (11, None, ["'Are you sure that this is a good plan?' The term ", ('kostya', 'уверена'), ' has an ending showing Kostya is asking a woman. Here, ', ('kostya', 'что'), " means 'that', though it often means 'what'."]),
    (12, None, ["'Vika must believe that we broke up.' Let's look at the dialogue: ", ('nastya', 'должна'), ' ending to match a woman. The verb ', ('nastya', 'поверить'), " is 'to believe', and ", ('nastya', 'расстались'), " means 'we parted'."]),
    (13, None, ["'All right, let us put on this show.' Let us focus on the phrase: ", ('kostya', 'давай'), " means 'let's'. We hear ", ('kostya', 'устроим'), " for 'we will arrange', and ", ('kostya', 'спектакль'), ' is a play or a show.']),
]
