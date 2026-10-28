# Authoring module for kukhnya-s06e02-scene-15.
ID = 'kukhnya-s06e02-scene-15'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 2
SCENE = 15
TITLE = 'Приглашение на кофе и падение на роликах  (Coffee Invitation and Rollerblade Fall)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'lyova': 'Лёва', 'nikita': 'Никита', 'sveta': 'Света'}
SOURCE_NAME = 'Кухня (Kukhnya) S6.02'
SOURCE_FILE = 'sources/kukhnya/s06/e02.ru.srt'
INTRO = "Thinking Denis is in love with bartender Sveta, Nikita persuades Sveta to meet Denis for coffee in an hour; meanwhile in the park, Lyova's rollerblading plan takes a painful tumble."
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'Lyova goes flying off the park path into the bushes, only to spot someone even more dangerous approaching: his mother. Until next time!'
CLOSING = ('sveta', 'Хорошего дня!')
STORY = [
    ('nikita', 'Слушай, Света, ты же знаешь, что ты нравишься одному человеку?', 'Listen, Sveta, you know that a certain person likes you, right?', [(249, 'Слушай, Свет, ты же знаешь')], 'adapted'),
    ('sveta', 'Допустим, знаю.', 'Suppose I know.', [(250, 'Допустим')], 'adapted'),
    ('nikita', 'Между прочим, он прямо страдает.', 'By the way, he is really suffering.', [(250, 'Между прочим, он страдает'), (251, 'Прямо страдает')], 'adapted'),
    ('sveta', 'И что же делать?', 'And what should I do?', [(252, 'И что же делать?')], 'exact'),
    ('nikita', 'Не знаю, например, выпить с ним чашечку кофе через час.', 'I do not know, for example, drink a cup of coffee with him in an hour.', [(253, 'Не знаю. Например, выпить с ним чашечку кофе через час')], 'exact'),
    ('sveta', 'Ну хорошо, договорились.', 'Well alright, it is a deal.', [(254, 'Ну, договорились')], 'adapted'),
    ('lyova', 'Давай немного отдохнем.', "Let's rest a little.", [(255, 'Давай'), (256, 'отдохнем')], 'adapted'),
    ('sveta', 'Да я не устала, а ты самый лучший тренер.', 'Why, I am not tired, and you are the very best coach.', [(256, 'Да я не устал'), (259, 'Ты самый лучший тренер')], 'adapted'),
    ('lyova', 'Зато я очень устал, извини.', 'On the other hand, I am very tired, sorry.', [(257, 'Зато я устала'), (258, 'Извини')], 'adapted'),
    ('sveta', 'Лёва, осторожней!', 'Lyova, be more careful!', [(260, 'Осторожней!')], 'adapted'),
    ('sveta', 'Аккуратней, посмотри, куда едешь!', 'More carefully, watch where you are going!', [(261, 'Аккуратней! Посмотри, куда едешь!')], 'exact'),
    ('lyova', 'Ой, помогите!', 'Oh, help!', [(260, 'Осторожней!')], 'adapted'),
]
WALK = [
    (0, None, "'Listen, Sveta, you know that a certain person likes you, right?' Nikita questions plainly where this conversation is heading next."),
    (1, None, '\'Suppose I know.\' Sveta fires back readily to Nikita and reaches for the Russian word "dopustim" ("let\'s say", built from "dopustit") right at the center of the line.'),
    (2, None, '\'By the way, he is really suffering.\' Nikita weighs in sharply before Sveta and reaches for the Russian word "stradayet" ("to suffer", built from "stradat") right at the center of the line.'),
    (3, None, "'And what should I do?' Sveta tests openly about what Nikita just brought up."),
    (4, None, '\'I do not know, for example, drink a cup of coffee with him in an hour.\' Mentioning a cup in the exchange, Nikita lands on "chashechku" ("small cup", built on "chashechka") to keep the statement grounded.'),
    (5, None, '\'Well alright, it is a deal.\' Sveta evenly chooses this word of agreement right on cue using "dogovorilis" ("deal") — literally "we have talked it through to an agreement", used just like "deal!" or "settled!".'),
    (6, None, "'Let's rest a little.' Lyova responds at once toward Sveta, letting the remark speak for itself."),
    (7, None, '\'Why, I am not tired, and you are the very best coach.\' Describing how best Lyova is beside Lyova, Sveta leans on "luchshiy" ("best") to give the whole sentence its punch.'),
    (8, None, '\'On the other hand, I am very tired, sorry.\' Opening up warmly at once, Lyova pivots with "zato" ("on the bright side, to make up for it") to flip a drawback into a plus.'),
    (9, None, "'Lyova, be more careful!' Sveta replies plainly with a shrug, keeping the focus on what actually matters here."),
    (10, None, '\'More carefully, watch where you are going!\' Sveta speaks up vividly at once and chooses "akkuratney" ("more carefully", from the root "akkuratno") so Lyova hears the exact meaning.'),
    (11, None, "'Oh, help!' Stepping in earnestly beside Sveta, spoken Russian compresses the whole thought into just 2 words, skipping the extra helper words English needs."),
]
