# Authoring module for kukhnya-s01e02-scene-17.
ID = 'kukhnya-s01e02-scene-17'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 2
SCENE = 17
TITLE = 'Один нормальный день  (One Normal Day)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'sasha': 'Саша', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.02'
SOURCE_FILE = 'sources/kukhnya/s01/e02.ru.dual.srt'
INTRO = 'The crises keep coming, and Vika finally sits down in the dining room, worn out. Sasha, the waitress, offers her a coffee and listens as Vika complains that nothing ever goes right at Claude Monet. Here is their talk in Russian first.'
OPENER = "Now let's look at the complaints."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'Vika asks for nothing more than one quiet day, which is not much to ask. If you take away only the phrase for "I\'m sure", you\'ll find it useful.'
CLOSING = ('vika', 'Пока!')
STORY = [
    ('sasha', 'Виктория Сергеевна, вам принести чашку кофе?', 'Viktoriya Sergeyevna, should I bring you a cup of coffee?', [], ''),
    ('vika', 'Господи, как же меня всё достало!', 'Lord, how sick of everything I am!', [(205, 'меня все достало')], ''),
    ('sasha', 'В ресторане опять возникли новые проблемы?', 'Have new problems arisen in the restaurant again?', [], ''),
    ('vika', 'Конечно, в баре пропал дорогой коньяк.', 'Of course, expensive cognac went missing in the bar.', [], ''),
    ('sasha', 'Бармен Костя сейчас ищет эту бутылку.', 'Bartender Kostya is looking for that bottle now.', [], ''),
    ('vika', 'Ну почему всё всегда идёт не так?', 'Well why does everything always go wrong?', [(206, 'Ну почему все всегда')], ''),
    ('sasha', 'Наша работа всегда очень нервная.', 'Our work is always very stressful.', [], ''),
    ('vika', 'Шеф кричит, повара спорят, бардак везде!', 'The chef shouts, cooks argue, mess everywhere!', [], ''),
    ('sasha', 'Вам нужно немного отдохнуть и успокоиться.', 'You need to rest a bit and calm down.', [], ''),
    ('vika', 'Неужели нельзя, чтобы день прошёл нормально?', 'Can a day really not pass normally?', [(207, 'прошел нормально')], ''),
    ('sasha', 'Я уверена, скоро всё наладится.', 'I am sure everything will work out soon.', [], ''),
    ('vika', 'Хочу хотя бы один спокойный день!', 'I want at least one calm day!', [(208, 'Один день')], ''),
    ('sasha', 'Мы все очень хотим этого, поверьте.', 'We all want this very much, believe me.', [], ''),
]
WALK = [
    (0, None, [
        '\'Viktoriya Sergeyevna, should I bring you a cup of coffee?\' The phrase ',
        ('sasha', 'вам принести'),
        ' literally means "to you to bring", which is how Russians offer something. The word for coffee, ',
        ('sasha', 'кофе?'),
        ', never changes its ending.'
    ]),
    (1, None, [
        '\'Lord, how sick of everything I am!\' The first word is ',
        ('vika', 'Господи,'),
        ', an exclamation like "oh Lord". The second half literally translates to "everything reached me", a stock way to say you\'ve had enough.'
    ]),
    (2, None, [
        '\'Have new problems arisen in the restaurant again?\' The place comes first. The phrase ',
        ('sasha', 'В ресторане'),
        ' translates to "in the restaurant". The action word ',
        ('sasha', 'возникли'),
        ' means "arose", and it already shows it refers to multiple things, even though the word for problems, ',
        ('sasha', 'проблемы?'),
        ', only turns up at the end.'
    ]),
    (3, None, [
        '\'Of course, expensive cognac went missing in the bar.\' The word for "disappeared", ',
        ('vika', 'пропал'),
        ', has an ending that matches the word for cognac. It\'s the same action word as "disappear to" in the last scene.'
    ]),
    (4, None, [
        '\'Bartender Kostya is looking for that bottle now.\' The action word ',
        ('sasha', 'ищет'),
        ' translates to "is looking for", and is from the same root as the word used in the knife scene. The phrase for "that bottle", ',
        ('sasha', 'эту бутылку.'),
        ', ends in a specific way to show it is the thing being sought.'
    ]),
    (5, None, [
        '\'Well, why does everything always go wrong?\' The phrase ',
        ('vika', 'идёт не так?'),
        ' literally translates to "goes not so". Russians use the word for "to go" about events as well as people.'
    ]),
    (6, None, [
        '\'Our work is always very stressful.\' The word for "stressful", ',
        ('sasha', 'нервная.'),
        ', is built from the word for "nerves". It has an ending to match the word for work, ',
        ('sasha', 'работа'),
        '.'
    ]),
    (7, None, [
        '\'The chef shouts, cooks argue, mess everywhere!\' The word for a mess, ',
        ('vika', 'бардак'),
        ', is slang and is stronger than the standard term. Notice there is no little word for "and" between the items, just commas.'
    ]),
    (8, None, [
        '\'You need to rest a bit and calm down.\' The phrase ',
        ('sasha', 'Вам нужно'),
        ' literally translates to "to you necessary", which is how to say "you need". The action word for "to rest" is ',
        ('sasha', 'отдохнуть'),
        ', and the one for "to calm down", ',
        ('sasha', 'успокоиться.'),
        ', has a special ending for actions done to oneself.'
    ]),
    (9, None, [
        '\'Can a day really not pass normally?\' Vika opens with ',
        ('vika', 'Неужели'),
        ', a word of pure disbelief translating to "can it really be?". After the little word ',
        ('vika', 'чтобы'),
        ', the action word is in the past form. So ',
        ('vika', 'день прошёл'),
        ' literally translates to "the day passed", even though she means any day from now on.'
    ]),
    (10, None, [
        '\'I am sure everything will work out soon.\' A woman says ',
        ('sasha', 'уверена,'),
        ' for "sure", while a man would say it differently. The action word for "will work out", ',
        ('sasha', 'наладится.'),
        ', is built from the same root as the word for "fine", so it literally translates to "will get into harmony".'
    ]),
    (11, None, [
        '\'I want at least one calm day!\' The action word ',
        ('vika', 'Хочу'),
        ' already says "I want", so Vika drops the word for "I". The phrase for "at least", ',
        ('vika', 'хотя бы'),
        ', is made of two small words.'
    ]),
    (12, None, [
        '\'We all want this very much, believe me.\' The word ',
        ('sasha', 'поверьте.'),
        ', meaning "believe me", is the polite command built from the action word for "to believe". The phrase ',
        ('sasha', 'Мы все'),
        ' translates to "we all".'
    ]),
]
