# Authoring module for kukhnya-s06e04-scene-19.
ID = 'kukhnya-s06e04-scene-19'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 4
SCENE = 19
TITLE = 'Обвинение в краже  (Accusation of Theft)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'guest': 'Гость', 'gulya': 'Гуля'}
SOURCE_NAME = 'Кухня (Kukhnya) S6.04'
SOURCE_FILE = 'sources/kukhnya/s06/e04.ru.srt'
INTRO = "After the kitchen brigade visits Barinov in the hospital, Lyova's mother and her friend block Gulya at the apartment door and demand that she open her handbag to prove she did not steal the five thousand rubles."
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "Right as the two women wrestle for Gulya's purse in the hallway, Lyova opens the front door and freezes at the sight. Until next time!"
CLOSING = ('guest', 'До встречи!')
STORY = [
    ('guest', 'Здравствуйте, шеф, вам лучше уже?', 'Hello, Chef, are you feeling better already?', [(298, 'Здрасте'), (299, 'Ну что, шеф, вам лучше уже?')], 'adapted'),
    ('barinov', 'Да, спасибо, ребята, уже лучше.', 'Yes, thank you, guys, already better.', [(299, 'Да, спасибо'), (302, 'Да, ребят, уже лучше')], 'adapted'),
    ('guest', 'А когда мне десять тысяч вернете?', 'And when will you pay me back my ten thousand?', [(300, 'А когда мне'), (300, 'тысяч вернете')], 'adapted'),
    ('barinov', 'Пошел вон отсюда, все понял?', 'Get out of here, understood?', [(301, 'Пошел вон. Все понял?')], 'adapted'),
    ('guest', 'А ты куда собралась?', 'And where are you going?', [(303, 'а ты куда')], 'adapted'),
    ('gulya', 'Я к чаю хочу чего-нибудь купить.', 'I want to buy something to go with tea.', [(304, 'Я к чаю хочу чего-нибудь купить')], 'exact'),
    ('guest', 'Ты нам сумочку свою сначала покажи.', 'Show us your handbag first.', [(305, 'Ты нам сумочку свою покажи')], 'adapted'),
    ('gulya', 'Что вы говорите?', 'What are you saying?', [(307, 'Что?')], 'adapted'),
    ('guest', 'Гуля, мы тебя ни в чем не обвиняем.', 'Gulya, we are not accusing you of anything.', [(307, 'мы тебя ни в чем не обвиняем')], 'adapted'),
    ('gulya', 'Взяла пять тысяч, думаешь, никто не заметил?', 'You took five thousand, do you think nobody noticed?', [(308, 'пять тысяч, думаешь, никто не заметил?')], 'adapted'),
    ('guest', 'Ну, дай сюда, покажи сумку!', 'Come on, give it here, show the bag!', [(309, 'Ну, дай сюда, покажи сумку')], 'exact'),
    ('gulya', 'Что вы такое делаете, пустите!', 'What are you doing, let go!', [(311, 'Что вы такое делаете?')], 'adapted'),
]
WALK = [
    (0, None, '\'Hello, Chef, are you feeling better already?\' The guest centers this vivid touch on cue: "zdravstvuyte" means "hello", and it carries the main weight of what the guest is saying.'),
    (1, None, '\'Yes, thank you, guys, already better.\' Barinov directs this answer to Gulya: the everyday word "spasibo" ("thank you") grew out of an old blessing meaning "save you", and it anchors the whole line here.'),
    (2, None, "'And when will you pay me back my ten thousand?' The guest questions promptly about what Barinov just brought up."),
    (3, None, '\'Get out of here, understood?\' Barinov highlights one familiar expression for Gulya: "otsyuda" means "from here", and it carries the main weight of what Barinov is saying.'),
    (4, None, '\'And where are you going?\' The guest drops the reaction briskly now: the "-sya" ending on "sobralas" ("to get ready") turns the action inward or makes it happen between people naturally.'),
    (5, None, "'I want to buy something to go with tea.' Gulya continues frankly without holding back, testing the guest's reaction in the middle of the exchange."),
    (6, None, '\'Show us your handbag first.\' The guest underscores one loaded detail toward Barinov: "sumochku" means "handbag" (from "sumochka"), giving the line its exact edge.'),
    (7, None, '\'What are you saying?\' Gulya states this answer to the guest: putting the question word "chto" right at the front of the line lets the guest hear the point of the question on the very first beat.'),
    (8, None, "'Gulya, we are not accusing you of anything.' The guest opens up lightly before Barinov, steering the talk right where he wants it."),
    (9, None, '\'You took five thousand, do you think nobody noticed?\' Gulya highlights one concrete detail on cue: "tysyach" means "thousand" (from "tysyacha"), giving the line its exact edge.'),
    (10, None, "'Come on, give it here, show the bag!' The guest counters openly in this moment, so Barinov knows he is not just making small talk."),
    (11, None, "'What are you doing, let go!' Gulya opens up candidly toward the guest, without trying to dress up how she really feels."),
]
