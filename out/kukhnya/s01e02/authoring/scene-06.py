# Authoring module for kukhnya-s01e02-scene-06.
ID = 'kukhnya-s01e02-scene-06'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 2
SCENE = 6
TITLE = 'Новый бармен  (The New Bartender)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'max': 'Макс', 'nastya': 'Настя'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.02'
SOURCE_FILE = 'sources/kukhnya/s01/e02.ru.dual.srt'
INTRO = 'Max agrees to help behind the restaurant bar and marvels at the computerized cash register. When Nastya comes in to order two espressos, she is surprised to see a cook posing as the new bartender. Listen to their playful exchange in Russian first, and then we will review it in English.'
OPENER = "Let's review this funny encounter behind the bar line by line."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "That concludes our sixth scene. In Kukhnya, Max's endless self-confidence and quick wit get him into and out of all kinds of trouble. See you next time!"
CLOSING = ('nastya', 'До встречи!')
STORY = [
    ('max', 'Так вот как выглядит эта система.', 'So this is what this system looks like.', [], ''),
    ('max', 'Я думал, это просто касса.', 'I thought it was just a cash register.', [(100, 'Я думал, это касса')], ''),
    ('nastya', 'Сделай два эспрессо, пожалуйста.', 'Make two espressos, please.', [(101, 'два эспрессо сделай, пожалуйста')], ''),
    ('nastya', 'Что ты тут делаешь?', 'What are you doing here?', [(102, 'что ты тут делаешь')], ''),
    ('max', 'А я теперь новый бармен.', 'And I am now the new bartender.', [(102, 'А я новый бармен')], ''),
    ('nastya', 'Да ладно тебе выдумывать.', 'Oh, stop making things up.', [(104, 'Да ладно')], ''),
    ('nastya', 'Я тебя на кухне видела.', 'I saw you in the kitchen.', [(104, 'Я тебя на кухне видела')], ''),
    ('nastya', 'Ты же повар.', 'You are a cook after all.', [(105, 'Ты повар')], ''),
    ('max', 'У меня очень много талантов.', 'I have very many talents.', [(105, 'А у меня много талантов')], ''),
    ('max', 'А в душе я бармен.', 'And at heart I am a bartender.', [(105, 'в душе я бармен')], ''),
    ('nastya', 'Костя уже починил аппарат?', 'Did Kostya already fix the machine?', [], ''),
    ('max', 'Конечно, всё прекрасно работает.', 'Of course, everything works wonderfully.', [], ''),
    ('nastya', 'Тогда быстрее вари кофе.', 'Then make coffee faster.', [(107, 'сделай два эспрессо, пожалуйста')], ''),
    ('max', 'Сию секунду. Всё будет готово.', 'Right away. Everything will be ready.', [], ''),
]
WALK = [
    (0, None, "'So this is what this system looks like.' Max inspects the computerized cash register at the bar."),
    (1, None, "'I thought it was just a cash register.' Max thought it was just a simple cash register."),
    (2, None, "'Make two espressos, please.' Nastya arrives at the counter with a beverage order."),
    (3, None, "'What are you doing here?' Nastya is surprised to find a kitchen helper standing behind the bar."),
    (4, None, "'And I am now the new bartender.' Max confidently invents a new position for himself."),
    (5, None, "'Oh, stop making things up.' Nastya tells him to stop making things up."),
    (6, None, "'I saw you in the kitchen.' Nastya mentions she saw him working in the kitchen."),
    (7, None, "'You are a cook after all.' Nastya points out that he is a cook after all."),
    (8, None, "'I have very many talents.' Max boasts that he has very many talents."),
    (9, None, "'And at heart I am a bartender.' Max claims that deep down inside his soul he is a bartender."),
    (10, None, "'Did Kostya already fix the machine?' Nastya asks if Kostya has already fixed the machine."),
    (11, None, "'Of course, everything works wonderfully.' Max confirms that everything works wonderfully."),
    (12, None, "'Then make coffee faster.' Nastya tells him to make the coffee faster."),
    (13, None, "'Right away.' Max promises to do it this very second."),
    (14, None, "'Everything will be ready.' Max assures her that everything will be ready soon."),
]
