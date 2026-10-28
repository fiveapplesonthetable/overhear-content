# Authoring module for kukhnya-s01e02-scene-09.
ID = 'kukhnya-s01e02-scene-09'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 2
SCENE = 9
TITLE = 'Хорошо или плохо?  (Good or Bad?)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'fedya': 'Федя', 'max': 'Макс', 'senya': 'Сеня'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.02'
SOURCE_FILE = 'sources/kukhnya/s01/e02.ru.dual.srt'
INTRO = 'Huddled behind the kitchen window, Senya, Fedya, and Max anxiously observe the guest tasting their unauthorized fricassee. Unsure how to interpret her stoic expression, they hold their breath in anticipation. Listen to their conversation in Russian first.'
OPENER = "Let's analyze this tense moment of culinary judgment line by line."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'As the critic calls the waitress over, suspense reaches a breaking point in the Claude Monet kitchen. See you next time!'
CLOSING = ('max', 'Пока!')
STORY = [
    ('senya', 'Смотрите, официант уже подал наше блюдо.', 'Look, the waiter has already served our dish.', [], ''),
    ('fedya', 'Она взяла вилку и пробует соус.', 'She picked up the fork and is tasting the sauce.', [], ''),
    ('max', 'Она улыбается или хмурится?', 'Is she smiling or frowning?', [], ''),
    ('senya', 'Она очень внимательно жуёт первый кусочек.', 'She is chewing the first piece very attentively.', [], ''),
    ('fedya', 'И почему-то совсем молчит.', 'And for some reason she is completely silent.', [], ''),
    ('max', 'А это хорошо или плохо?', 'Is that good or bad?', [(130, 'А это хорошо или плохо')], ''),
    ('senya', 'Я сам ничего пока не понимаю.', 'I do not understand anything yet myself.', [], ''),
    ('fedya', 'Главное, чтобы она не позвала директора.', 'The main thing is that she does not call the director.', [], ''),
    ('max', 'Смотрите, она сделала ещё один глоток.', 'Look, she took another bite.', [], ''),
    ('senya', 'Кажется, наше фрикасе ей понравилось!', 'It seems she liked our fricassee!', [], ''),
    ('fedya', 'Не радуйся раньше времени.', 'Do not celebrate too early.', [], ''),
    ('max', 'Ой, она зовёт официантку к столу!', 'Oh, she is calling the waitress to the table!', [], ''),
]
WALK = [
    (0, None, "'Look, the waiter has already served our dish.' Senya watches the dining room through the kitchen window."),
    (1, None, "'She picked up the fork and is tasting the sauce.' Fedya monitors every movement of the food critic."),
    (2, None, "'Is she smiling or frowning?' Max tries to read the woman's subtle facial expression from afar."),
    (3, None, "'She is chewing the first piece very attentively.' Senya observes her chewing the first piece very attentively."),
    (4, None, "'And for some reason she is completely silent.' Fedya grows increasingly nervous as the VIP remains silent."),
    (5, None, "'Is that good or bad?' Max asks the agonizing question while they hold their breath."),
    (6, None, "'I do not understand anything yet myself.' Senya confesses his total inability to predict her verdict."),
    (7, None, "'The main thing is that she does not call the director.' Fedya hopes she does not call the director over."),
    (8, None, "'Look, she took another bite.' Max reports positive progress at the VIP table."),
    (9, None, "'It seems she liked our fricassee!' Senya feels a sudden surge of kitchen optimism."),
    (10, None, "'Do not celebrate too early.' Fedya advises against celebrating too early."),
    (11, None, "'Oh, she is calling the waitress to the table!' Max spots the ominous gesture of her calling the waitress to the table."),
]
