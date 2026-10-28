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
    (0, None, '\'Hello, Chef, are you feeling better already?\' The guest naturally delivers this formal greeting in one quick breath using "zdravstvuyte" ("hello") — the polite Russian greeting that literally wishes the other person good health.'),
    (1, None, '\'Yes, thank you, guys, already better.\' Mentioning the thank at once, Barinov centers the remark on "spasibo" ("thank you") without any extra fuss.'),
    (2, None, "'And when will you pay me back my ten thousand?' The guest questions promptly why things suddenly took this turn between them."),
    (3, None, '\'Get out of here, understood?\' Barinov speaks up dryly around the guest and uses "otsyuda" ("from here") to carry the main weight of the thought.'),
    (4, None, '\'And where are you going?\' Holding firm warmly during the talk, the "-sya" ending on "sobralas" ("to get ready") marks an action that unfolds mutually or turns back on the speaker.'),
    (5, None, "'I want to buy something to go with tea.' Raising the tea toward the guest, Gulya puts the real issue right on the table for the guest."),
    (6, None, '\'Show us your handbag first.\' Pointing to the handbag at once, the guest puts the weight on "sumochku" ("handbag", from "sumochka") as the exchange unfolds.'),
    (7, None, '\'What are you saying?\' Leaning in smoothly on the spot, Gulya puts the question word "chto" right at the start so the guest hears the focus immediately.'),
    (8, None, "'Gulya, we are not accusing you of anything.' The guest cuts in lightly on the spot, before Gulya can change the subject."),
    (9, None, '\'You took five thousand, do you think nobody noticed?\' Bringing up the thousand right here, Gulya uses "tysyach" ("thousand", from "tysyacha") to make the point stick.'),
    (10, None, '\'Come on, give it here, show the bag!\' Highlighting the bag in the exchange, the guest puts the weight on "sumku" ("bag, purse", from "sumka") as the exchange unfolds.'),
    (11, None, "'What are you doing, let go!' Gulya cuts in candidly hearing the guest, shifting the mood of the conversation in a single beat."),
]
