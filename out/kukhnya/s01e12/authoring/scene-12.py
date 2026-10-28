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
INTRO = 'Nastya is convinced that the new ban is about her and Kostya, who have been seeing each other in secret. She has an idea: stage a fake quarrel. Here is their conversation in Russian first.'
OPENER = "Let's go through it slowly and hear how Nastya talks him round."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'Kostya is not sure about this, but he plays along. When you watch, see how well two people who are not actors can fake an argument. Until next time.'
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
    (0, None, "'Kostya, this new ban is because of us!' 'Iz-za' means 'because of', and it's mostly used when the cause is something bad. 'Nas' is 'us', and it changes shape from 'my' after the little word."),
    (1, None, "'But what makes you think that?' 'S chego' is literally 'from what', which is how Russians ask 'what makes you say that?'. 'Vzyala' is 'took', and an 'a' tells you a woman is speaking."),
    (2, None, "'Because only we have a secret relationship.' 'Potomu chto' means 'because'. 'U nas' is 'at us', or 'we have'. 'Tainye' is 'secret' and 'otnosheniya' is 'relationship', which in Russian is always plural."),
    (3, None, "'Victoria simply cares about the dining room discipline.' 'Zabotitsya' is 'cares', with an ending that means 'looks after itself'. 'O discipline' is 'about discipline'. 'Prosto' means 'simply'."),
    (4, None, "'She looked at us very suspiciously.' 'Posmotrela' is 'looked' with an 'a' for 'she', and the 'po' at the front means one glance. 'Podozritelno' is 'suspiciously'."),
    (5, None, "'You imagined it, she was looking at everyone.' 'Smotrela' is 'was looking', without the 'po', so it means she kept looking. Compare it with Nastya's glance in the line before. 'Tebe pokazalos' is literally 'to you it seemed'."),
    (6, None, "'I know that strict look very well!' 'Prekrasno' means 'beautifully', but here it means 'perfectly well'. 'Vzglyad' is a look. 'Strogiy' is 'strict'."),
    (7, None, "'And what should we do now?' 'Chto nam delat' is literally 'what to us to do', which is how Russians say 'what should we do'. The little 'zhe' makes it sound urgent."),
    (8, None, "'We need to quarrel in front of her right away.' 'Porugatsya' is 'to have a row', and the 'sya' makes it mutual, since a quarrel takes two. 'Pered ney' is 'in front of her'."),
    (9, None, "'Why should we quarrel in the restaurant?' 'Rugatsya' is 'to quarrel', and the 'po' at the front of Nastya's version means 'to have a quarrel'. 'V restorane' is 'in the restaurant'."),
    (10, None, "'We will quarrel in pretend, only for show.' 'Ponaroshku' is the childish 'just pretend', the word kids use in games. 'Dlya vida' is literally 'for the look', so for appearance."),
    (11, None, "'Are you sure that this is a good plan?' 'Uverena' ends in 'a' because Kostya is asking a woman. A man would be 'uveren'. 'Chto' means 'that' here, though it also means 'what'."),
    (12, None, "'Vika must believe that we broke up.' 'Dolzhna' ends in 'a' for a woman. 'Poverit' is 'to believe', and 'rasstalis' is 'we parted', with the same 'ourselves' ending as before."),
    (13, None, "'All right, let us put on this show.' 'Davay' means 'let's'. 'Ustroim' is 'we will arrange', and 'spektakl' is a play or a show."),
]
