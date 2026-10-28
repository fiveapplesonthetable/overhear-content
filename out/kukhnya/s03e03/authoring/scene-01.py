# Authoring module for kukhnya-s03e03-scene-01.
ID = 'kukhnya-s03e03-scene-01'
SHOW = 'kukhnya'
SEASON = 3
EPISODE = 3
SCENE = 1
TITLE = 'Суеверные официанты  (Superstitious Waiters)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'guest': 'Гость', 'max': 'Макс', 'nastya': 'Настя'}
SOURCE_NAME = 'Кухня (Kukhnya) S3.03'
SOURCE_FILE = 'sources/kukhnya/s03/e03.ru.srt'
INTRO = 'In Episode Three of Season Three, Max explains that waiters are even more superstitious than athletes: spill a pinch of salt at a table, and a quarrel with the guest is practically guaranteed.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "And that finishes our opening scene. Listen for how the waitress's prophecy about spilled salt immediately comes true. Until next time!"
CLOSING = ('nastya', 'До завтра!')
STORY = [
    ('max', 'Спортсмены — самые суеверные люди в мире?', 'Are athletes the most superstitious people in the world?', [(1, 'Спортсмены'), (1, 'люди в мире')], 'adapted'),
    ('max', 'Ничего подобного. Самые суеверные люди — официанты.', 'Nothing of the sort. The most superstitious people are waiters.', [(2, 'Ничего подобного'), (2, 'люди – официанты')], 'adapted'),
    ('nastya', 'Ваш салат.', 'Your salad.', [(3, 'Ваш салат')], ''),
    ('guest', 'Соль просыпала. Ничего страшного.', 'I spilled the salt. No big deal.', [(4, 'Соль просыпала'), (5, 'Ничего страшного')], 'adapted'),
    ('nastya', 'Как это ничего страшного?', 'What do you mean, no big deal?', [(6, 'ничего страшного')], 'adapted'),
    ('nastya', 'Мы теперь с вами обязательно поссоримся.', 'Now you and I will definitely quarrel.', [(6, 'Мы теперь с вами обязательно поссоримся')], ''),
    ('guest', 'Девушка, я не собираюсь с вами ссориться.', 'Miss, I have no intention of quarreling with you.', [(7, 'Девушка, я не собираюсь с вами ссориться')], ''),
    ('guest', 'Вы куда смотрите? Сперва соль, потом вино!', 'Where are you looking? First salt, then wine!', [(9, 'куда смотрите? Сперва соль, потом')], 'adapted'),
    ('guest', 'Позовите администратора!', 'Call the manager!', [(10, 'администратора')], 'adapted'),
    ('nastya', 'Я же говорила, что поссоримся.', 'I told you we would quarrel.', [(10, 'Я же говорила, что поссоримся')], ''),
    ('max', 'Спасибо. До свидания. Ждём вас снова.', 'Thank you. Goodbye. We look forward to seeing you again.', [(11, 'Спасибо'), (12, 'До свидания. Ждем вас снова')], 'adapted'),
    ('max', 'Официанты верят во все приметы.', 'Waiters believe in all omens.', [(13, 'Официанты верят во все'), (13, 'приметы')], 'adapted'),
]
WALK = [
    (0, None, "'Are athletes the most superstitious people in the world?' Checking whether athletes the most superstitious people in the world is how Max puts the guest on the spot."),
    (1, None, '\'Nothing of the sort. The most superstitious people are waiters.\' Around the conversation and argument, Max sets a calm, everyday tone with the guest. Russian drops "is" in the present, setting the two halves of the thought side by side.'),
    (2, None, '\'Your salad.\' Over the work and the argument, Nastya answers the guest without a second thought. Notice how she sticks to the formal "you", keeping a professional line between them.'),
    (3, None, "'I spilled the salt. No big deal.' Around the conversation and kitchen, the guest sets a calm, everyday tone with Max."),
    (4, None, '\'What do you mean, no big deal?\' Asking what the guest means no big deal is how Nastya puts the guest on the spot. Russian drops "is" in the present, setting the two halves of the thought side by side.'),
    (5, None, '\'Now you and I will definitely quarrel.\' Noting that the guest and she will definitely quarrel keeps Nastya\'s side of the story simple and clear. Even in the middle of the drama, she keeps the polite plural "you" that workplace Russian expects.'),
    (6, None, "'Miss, I have no intention of quarreling with you.' Mentioning that Max should miss he has no intention of quarreling with Max moves the talk in a new direction."),
    (7, None, '\'Where are you looking? First salt, then wine!\' Asking where Max looking is cuts straight through the tension between the guest and Max. Even in the middle of the drama, he keeps the polite plural "you" that workplace Russian expects.'),
    (8, None, "'Call the manager!' The guest declares that Max should call the manager as the tension in the room peaks. Russian puts the key word right up front so his emotion lands on the first beat."),
    (9, None, "'I told you we would quarrel.' Once she told the guest they would quarrel, Nastya can finally tell the guest what she means."),
    (10, None, '\'Thank you. Goodbye. We look forward to seeing you again.\' By looking forward to seeing the guest again, Max keeps his side of the story grounded. Notice how he sticks to the formal "you", keeping a professional line between them.'),
    (11, None, "'Waiters believe in all omens.' With the point and argument in play, Max keeps this short reply brisk and direct."),
]
