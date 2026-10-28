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
    (0, None, '\'Are athletes the most superstitious people in the world?\' Max anchors one classic word at once: "suyevernyye" means "superstitious" (from "suyevernyy"), giving the line its exact edge.'),
    (1, None, '\'Nothing of the sort. The most superstitious people are waiters.\' Max hands over that remark without fuss: notice how Russian needs no word for "am", "is", or "are" in the present — placing the words side by side says it all.'),
    (2, None, "'Your salad.' Nastya replies evenly with a nod, bringing things back to earth after the buildup."),
    (3, None, '\'I spilled the salt. No big deal.\' The guest emphasizes one clear touch in earnest: "strashnogo" means "terrible, serious" (from "strashnyy"), giving the line its exact edge.'),
    (4, None, '\'What do you mean, no big deal?\' Nastya drops that remark without fuss: putting the question word "kak" right at the front of the line lets the guest hear the point of the question on the very first beat.'),
    (5, None, "'Now you and I will definitely quarrel.' Nastya answers boldly toward Max, letting the remark speak for itself."),
    (6, None, '\'Miss, I have no intention of quarreling with you.\' The guest stresses this clear expression on cue: "devushka" means "girlfriend", and it carries the main weight of what the guest is saying.'),
    (7, None, '\'Where are you looking? First salt, then wine!\' The guest directs the remark toward Nastya: putting the question word "kuda" right at the front of the line lets Nastya hear the point of the question on the very first beat.'),
    (8, None, "'Call the manager!' The guest proceeds plainly with Max, before Max can change the subject."),
    (9, None, '\'I told you we would quarrel.\' Nastya leans on one vivid choice for Max: "possorimsya" means "will quarrel" (from "possoritsya"), giving the line its exact edge.'),
    (10, None, '\'Thank you. Goodbye. We look forward to seeing you again.\' Max lays out this answer toward the guest: the everyday word "spasibo" ("thank you") grew out of an old blessing meaning "save you", and it anchors the whole line here.'),
    (11, None, "'Waiters believe in all omens.' Max holds firm earnestly to be clear, refusing to let the moment slip past."),
]
