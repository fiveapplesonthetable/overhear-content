# Authoring module for kukhnya-s06e15-scene-04.
ID = 'kukhnya-s06e15-scene-04'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 15
SCENE = 4
TITLE = 'Ссора с Шефом  (Quarrel with the Chef)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'lyova': 'Лёва', 'senya': 'Сеня'}
SOURCE_NAME = 'Кухня (Kukhnya) S6.15'
SOURCE_FILE = 'sources/kukhnya/s06/e15.ru.srt'
INTRO = "When Lyova mentions that he slightly improved Chef Barinov's recipe, Chef Barinov explodes with anger and insults Lyova's hands. Offended by the outburst, Lyova agrees to write his resignation letter on the spot."
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'Lyova storms off to write his resignation letter, while Chef Barinov stubbornly pretends he does not care. See you next time!'
CLOSING = ('lyova', 'До свидания!')
STORY = [
    ('barinov', 'Хочешь на моих блюдах карьеру сделать?', 'Do you want to build a career on my dishes?', [(43, 'На моих блюдах хочешь себе карьеру сделать')], 'adapted'),
    ('lyova', 'Вообще-то я его немного сам доработал.', 'Actually, I improved it a little myself.', [(44, 'Вообще-то я его немного доработал')], 'adapted'),
    ('barinov', 'Не смей никогда дорабатывать мои блюда!', 'Never dare to modify my dishes!', [(46, 'Дорабатывать мои блюда')], 'adapted'),
    ('barinov', 'Сначала стань сам главным шефом ресторана!', 'First become the head chef of a restaurant yourself!', [(47, 'Станешь шефом')], 'adapted'),
    ('barinov', 'Тогда и будешь свои блюда дорабатывать!', 'Then you can modify your own dishes!', [(48, 'блюда дорабатывать')], 'adapted'),
    ('lyova', 'Значит, я плохо готовлю на кухне?', 'So I cook poorly in the kitchen?', [(49, 'Значит, у меня')], 'adapted'),
    ('lyova', 'А вы без моей помощи обойдётесь?', 'And will you manage without my help?', [(51, 'обойдетесь')], 'adapted'),
    ('senya', 'Слушай, а может, он не уйдёт?', 'Listen, maybe he will not leave?', [(52, 'А может, еще не уйдет')], 'adapted'),
    ('barinov', 'Легко обойдусь, ты даже не беспокойся!', 'I will manage easily, do not even worry!', [(53, 'Обойдусь. Не беспокойся')], 'adapted'),
    ('barinov', 'Пиши заявление и уходи с кухни!', 'Write your resignation letter and leave the kitchen!', [(54, 'Пиши заявление')], 'adapted'),
    ('lyova', 'Хорошо, я прямо сейчас напишу заявление!', 'Fine, I will write the resignation letter right now!', [(55, 'И напишу')], 'adapted'),
    ('senya', 'Жалко, кто теперь будет следить за порядком?', 'What a pity, who will keep order now?', [(58, 'Кто теперь будет за порядком следить')], 'adapted'),
]
WALK = [
    (0, None, '\'Do you want to build a career on my dishes?\' Talking about the dish in this beat, Barinov lands on "blyudakh" ("dish, course", built on "blyudo") to keep the statement grounded.'),
    (1, None, '\'Actually, I improved it a little myself.\' Following up warmly in this beat, Lyova drops in "voobshche" ("in general, altogether") to sum up the whole situation at once.'),
    (2, None, "'Never dare to modify my dishes!' Barinov counters at once on the spot, making his position completely clear."),
    (3, None, '\'First become the head chef of a restaurant yourself!\' Addressing a restaurant in the exchange, Barinov lands on "restorana" ("restaurant", built on "restoran") to keep the statement grounded.'),
    (4, None, '\'Then you can modify your own dishes!\' Mentioning the dish in this beat, Barinov chooses "dorabatyvat" ("to modify, improve") so Lyova gets the point right away.'),
    (5, None, "'So I cook poorly in the kitchen?' Lyova prompts bluntly how Barinov expects that to work in practice."),
    (6, None, '\'And will you manage without my help?\' Focusing on his help in front of Senya, Lyova lands on "pomoshchi" ("help", built on "pomoshch") to keep the statement grounded.'),
    (7, None, "'Listen, maybe he will not leave?' Speaking calmly before Barinov, Senya keeps normal statement word order here, turning the line into a question for Barinov purely through rising pitch."),
    (8, None, "'I will manage easily, do not even worry!' Barinov answers candidly watching Senya, to clear the air between them once and for all."),
    (9, None, '\'Write your resignation letter and leave the kitchen!\' Highlighting the statement in the exchange, Barinov brings in "zayavleniye" ("statement") to make the meaning unmistakable.'),
    (10, None, '\'Fine, I will write the resignation letter right now!\' Highlighting the statement before Barinov, Lyova centers the remark on "zayavleniye" ("statement") without any extra fuss.'),
    (11, None, "'What a pity, who will keep order now?' Senya wonders evenly why things suddenly took this turn between them."),
]
