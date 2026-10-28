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
    (0, None, '\'Are athletes the most superstitious people in the world?\' Underscoring how superstitious things are in this beat, Max chooses "suyevernyye" ("superstitious", from the root "suyevernyy") so Nastya hears the exact meaning.'),
    (1, None, '\'Nothing of the sort. The most superstitious people are waiters.\' Pointing out how superstitious things are beside Nastya, Max links the Russian words directly in the present with no word for "am", "is", or "are" needed.'),
    (2, None, "'Your salad.' Nastya proceeds evenly with a nod, grounding the moment in plain reality."),
    (3, None, '\'I spilled the salt. No big deal.\' Highlighting the salt beside Nastya, the guest uses "strashnogo" ("terrible, serious", from "strashnyy") to make the point stick.'),
    (4, None, '\'What do you mean, no big deal?\' Speaking calmly right here, Nastya puts the question word "kak" right at the start so the guest hears the focus immediately.'),
    (5, None, "'Now you and I will definitely quarrel.' Nastya cuts in boldly beside the guest, leaving no doubt about where she stands."),
    (6, None, '\'Miss, I have no intention of quarreling with you.\' Mentioning the girlfriend in front of Nastya, the guest lands on "devushka" ("girlfriend") as the key everyday word here.'),
    (7, None, '\'Where are you looking? First salt, then wine!\' Pushing back openly right here, the guest puts the question word "kuda" right at the start so Nastya hears the focus immediately.'),
    (8, None, "'Call the manager!' The guest counters plainly with a sigh, steering the talk right where he wants it."),
    (9, None, '\'I told you we would quarrel.\' Nastya fires back evenly around the guest and leans on "possorimsya" ("will quarrel", a form of "possoritsya") to give the remark its edge.'),
    (10, None, "'Thank you. Goodbye. We look forward to seeing you again.' Max speaks up sharply in their talk, so Nastya knows he is not just making small talk."),
    (11, None, "'Waiters believe in all omens.' Max responds earnestly hearing Nastya, watching Nastya's face to see how the news lands."),
]
