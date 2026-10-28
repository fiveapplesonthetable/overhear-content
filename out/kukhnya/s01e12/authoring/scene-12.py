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
    (0, None, "'Kostya, this new ban is because of us!' 'Iz-za nas' is 'because of us': iz-za is the 'because of' for a bad cause, and my, 'we', becomes nas after it."),
    (1, None, "'But what makes you think that?' 'S chego' is literally 'from what', which is how Russians ask 'what makes you say that?'. 'Vzyala' is 'took', and it ends in 'a' because the 'you' is Nastya."),
    (2, None, "'Because only we have a secret relationship.' 'U nas' is 'at us', or 'we have'. In the sense of a romance, otnosheniya is plural, so 'secret' is plural too: taynye otnosheniya."),
    (3, None, "'Victoria simply cares about the dining room discipline.' 'Zabotitsya o' is 'cares about'. This verb always carries its sya, and after o the noun ends in 'e': o distsipline."),
    (4, None, "'She looked at us very suspiciously.' 'Posmotrela' is the completed form of smotret, 'to look': one look, done. The 'a' is for 'she'. 'Podozritelno' is 'suspiciously'."),
    (5, None, "'You imagined it, she was looking at everyone.' 'Smotrela' is 'was looking', without the 'po', so it means she kept looking. Compare it with Nastya's glance in the line before. 'Tebe pokazalos' is literally 'to you it seemed'."),
    (6, None, "'I know that strict look very well!' 'Prekrasno' means 'beautifully', but here it means 'perfectly well'. 'Etot strogiy vzglyad', 'that strict look': vzglyad is a masculine thing, so it keeps its plain shape as the object."),
    (7, None, "'And what should we do now?' The line is 'what to us to do', which covers 'what should we do'. The little 'zhe' makes it urgent."),
    (8, None, "'We need to quarrel in front of her right away.' Without the sya, rugat means 'to scold' someone; with it, porugatsya is 'to have a row' with each other. 'Pered ney' is 'in front of her'."),
    (9, None, "'Why should we quarrel in the restaurant?' 'Rugatsya' is 'to quarrel', and Nastya's porugatsya is its completed partner, one quarrel and done. 'V restorane' is 'in the restaurant'."),
    (10, None, "'We will quarrel in pretend, only for show.' 'Ponaroshku' is the childish 'just pretend', the word kids use in games. 'Dlya vida' is literally 'for the look', so for appearance."),
    (11, None, "'Are you sure that this is a good plan?' 'Uverena' ends in 'a' because Kostya is asking a woman. A man would be 'uveren'. 'Chto' means 'that' here, though it also means 'what'."),
    (12, None, "'Vika must believe that we broke up.' 'Dolzhna' ends in 'a' for a woman. 'Poverit' is 'to believe', and 'rasstalis' is 'we parted', with the same 'ourselves' ending as before."),
    (13, None, "'All right, let us put on this show.' 'Davay' means 'let's'. 'Ustroim' is 'we will arrange', and 'spektakl' is a play or a show."),
]
