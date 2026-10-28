ID = 'kukhnya-s03e03-scene-01'
SHOW = "kukhnya"
SEASON = 3
EPISODE = 3
SCENE = 1
TITLE = 'Суеверные официанты  (Superstitious Waiters)'
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {'narrator': 'sky', 'anya': 'alisa', 'nastya': 'angelina', 'guest': 'anja'}
LABELS = {'anya': 'Макс', 'nastya': 'Настя', 'guest': 'Гость'}
SOURCE_NAME = "Кухня (Kukhnya) S3.03"
SOURCE_FILE = 'sources/kukhnya/s03/e03.ru.srt'

INTRO = 'In Episode Three of Season Three, Max explains that waiters are even more superstitious than athletes: spill a pinch of salt at a table, and a quarrel with the guest is practically guaranteed.'

STORY = [
    ('anya', 'Спортсмены — самые суеверные люди в мире?', 'Are athletes the most superstitious people in the world?', [(1, 'Спортсмены'), (1, 'люди в мире')], 'adapted'),
    ('anya', 'Ничего подобного. Самые суеверные люди — официанты.', 'Nothing of the sort. The most superstitious people are waiters.', [(2, 'Ничего подобного'), (2, 'люди – официанты')], 'adapted'),
    ('nastya', 'Ваш салат.', 'Your salad.', [(3, 'Ваш салат')], ''),
    ('guest', 'Соль просыпала. Ничего страшного.', 'I spilled the salt. No big deal.', [(4, 'Соль просыпала'), (5, 'Ничего страшного')], 'adapted'),
    ('nastya', 'Как это ничего страшного?', 'What do you mean, no big deal?', [(6, 'ничего страшного')], 'adapted'),
    ('nastya', 'Мы теперь с вами обязательно поссоримся.', 'Now you and I will definitely quarrel.', [(6, 'Мы теперь с вами обязательно поссоримся')], ''),
    ('guest', 'Девушка, я не собираюсь с вами ссориться.', 'Miss, I have no intention of quarreling with you.', [(7, 'Девушка, я не собираюсь с вами ссориться')], ''),
    ('guest', 'Вы куда смотрите? Сперва соль, потом вино!', 'Where are you looking? First salt, then wine!', [(9, 'куда смотрите? Сперва соль, потом')], 'adapted'),
    ('guest', 'Позовите администратора!', 'Call the manager!', [(10, 'администратора')], 'adapted'),
    ('nastya', 'Я же говорила, что поссоримся.', 'I told you we would quarrel.', [(10, 'Я же говорила, что поссоримся')], ''),
    ('anya', 'Спасибо. До свидания. Ждём вас снова.', 'Thank you. Goodbye. We look forward to seeing you again.', [(11, 'Спасибо'), (12, 'До свидания. Ждем вас снова')], 'adapted'),
    ('anya', 'Официанты верят во все приметы.', 'Waiters believe in all omens.', [(13, 'Официанты верят во все'), (13, 'приметы')], 'adapted'),
]

OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."

WALK = [
    (0, None, "'Are athletes the most superstitious people in the world?' Here the Russian phrasing highlights 'athletes' before landing on 'peace'."),
    (1, None, "'Nothing of the sort. The most superstitious people are waiters.' The grammar packs 'nothing' and 'waiters' into a tight, idiomatic kitchen exchange."),
    (2, None, "'Your salad.' Nastya chooses the respectful plural 'you' alongside 'salad' to keep a polite distance. the guest answers right away."),
    (3, None, "'I spilled the salt. No big deal.' the guest brings out the contrast between 'salt' and 'spilled' in a few short words."),
    (4, None, "'What do you mean, no big deal?' In Russian, the idea of 'how' flows naturally into 'terrible' without extra filler words."),
    (5, None, "'Now you and I will definitely quarrel.' In Russian, the idea of 'we' flows naturally into 'will quarrel' without extra filler words. the guest answers right away."),
    (6, None, "'Miss, I have no intention of quarreling with you.' Here the Russian phrasing highlights 'miss' before landing on 'to quarrel'."),
    (7, None, "'Where are you looking? First salt, then wine!' In Russian, the idea of 'you' flows naturally into 'wine' without extra filler words."),
    (8, None, "'Call the manager!' Notice how Russian expresses 'call' and 'manager' with crisp inflection rather than helper words. Nastya answers right away."),
    (9, None, "'I told you we would quarrel.' In Russian, the idea of 'I' flows naturally into 'will quarrel' without extra filler words."),
    (10, None, "'Thank you. Goodbye. We look forward to seeing you again.' The meaning hinges on 'thank you' working together with 'again' in spoken Russian."),
    (11, None, "'Waiters believe in all omens.' In Russian, the idea of 'waiters' flows naturally into 'omens' without extra filler words."),
]

TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "And that finishes our opening scene. Listen for how the waitress's prophecy about spilled salt immediately comes true."
CLOSING = ('nastya', 'Мы обязательно поссоримся!')
