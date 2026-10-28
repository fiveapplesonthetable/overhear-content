# Authoring module for kukhnya-s06e04-scene-08.
ID = 'kukhnya-s06e04-scene-08'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 4
SCENE = 8
TITLE = 'Ложный след в блокноте  (The False Trail in the Notebook)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'eleonora': 'Элеонора', 'katya': 'Катя'}
SOURCE_NAME = 'Кухня (Kukhnya) S6.04'
SOURCE_FILE = 'sources/kukhnya/s06/e04.ru.srt'
INTRO = "Katya tells Barinov and Eleonora that she spotted restaurant names and notes inside Olivier's notebook, sending the entire hotel into full Michelin-inspector panic!"
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'Hook, line, and sinker: Barinov mobilizes the entire kitchen while Katya heads upstairs to tell Olivier about the prank. See you next time!'
CLOSING = ('barinov', 'Хорошего дня!')
STORY = [
    ('katya', 'Похоже, вы были правы насчет Оливье.', 'It looks like you were right about Olivier.', [(123, 'Похоже, вы были правы насчет оливье')], 'exact'),
    ('barinov', 'Ну, что там в блокноте?', 'Well, what is in the notebook?', [(124, 'что в блокноте?')], 'adapted'),
    ('katya', 'Названия ресторанов и какие-то пометки.', 'Names of restaurants and some kind of notes.', [(125, 'ресторанов, какие-то пометки')], 'adapted'),
    ('katya', 'Да я толком и не успела рассмотреть.', 'I did not really manage to get a good look.', [(126, 'Да я толком и не успела рассмотреть')], 'exact'),
    ('eleonora', 'Он жаловался на что-нибудь?', 'Did he complain about anything?', [(127, 'Он жаловался на что-нибудь?')], 'exact'),
    ('katya', 'Он говорил, что в номере очень жарко, можно утку пожарить.', 'He said that it is so hot in the room you could roast a duck.', [(129, 'что в номере'), (129, 'можно утку пожарить')], 'adapted'),
    ('eleonora', 'Наверное, опять кондиционер сломался.', 'Probably the air conditioner broke again.', [(130, 'Наверное, опять кондиционер сломался')], 'exact'),
    ('eleonora', 'Значит, переселяй его в люкс!', 'Then move him into a luxury suite!', [(132, 'в люкс')], 'adapted'),
    ('eleonora', 'Катя, у тебя выходной, ни на шаг от него не отходи.', 'Katya, you have the day off, do not leave his side for a single step.', [(133, 'Катя, у тебя выходной'), (134, 'Ни на шаг от него не отходи')], 'adapted'),
    ('barinov', 'Алло, Лёва, ты мне нужен срочно на кухню!', 'Hello, Lyova, I need you urgently in the kitchen!', [(135, 'Алло, Лёва, ты мне нужен срочно на кухню')], 'exact'),
    ('barinov', 'Какой выходной, какой еще барбарис?', 'What day off, what barberries?', [(136, 'Какой выходной?'), (137, 'Какой')], 'adapted'),
    ('barinov', 'Официальное заявление: у нас в отеле инспектор!', 'Official announcement: we have an inspector in the hotel!', [(139, 'Официальное заявление'), (140, 'У нас в отеле инспектор')], 'adapted'),
]
WALK = [
    (0, None, "'It looks like you were right about Olivier.' Katya jumps in quietly with a nod, refusing to let the moment slip past."),
    (1, None, "'Well, what is in the notebook?' Barinov inquires briskly where this conversation is heading next."),
    (2, None, '\'Names of restaurants and some kind of notes.\' Focusing on the restaurants in the exchange, Katya centers the thought on "restoranov" ("restaurants", from "restoran") without wasting a word.'),
    (3, None, '\'I did not really manage to get a good look.\' Katya speaks up briskly on the spot and uses "rassmotret" ("to examine") to carry the main weight of the thought.'),
    (4, None, "'Did he complain about anything?' Eleonora prompts promptly while looking straight at Katya here."),
    (5, None, '\'He said that it is so hot in the room you could roast a duck.\' Highlighting the room in front of Eleonora, Katya centers the thought on "nomere" ("in the hotel room", from "nomer") without wasting a word.'),
    (6, None, "'Probably the air conditioner broke again.' Dwelling on the air conditioner in the exchange, spoken Russian compresses the whole thought into just 4 words, skipping the extra helper words English needs."),
    (7, None, "'Then move him into a luxury suite!' Eleonora counters right away watching Katya, to clear the air between them once and for all."),
    (8, None, '\'Katya, you have the day off, do not leave his side for a single step.\' Emphasizing the day around Katya, Eleonora lands on "vykhodnoy" ("a day off") as the key everyday word here.'),
    (9, None, "'Hello, Lyova, I need you urgently in the kitchen!' Barinov jumps in quietly during the talk, bringing things back to earth after the buildup."),
    (10, None, "'What day off, what barberries?' Barinov asks frankly where this conversation is heading next."),
    (11, None, '\'Official announcement: we have an inspector in the hotel!\' Highlighting the statement to Eleonora, Barinov centers the thought on "ofitsialnoye" ("official", from "ofitsialnyy") without wasting a word.'),
]
