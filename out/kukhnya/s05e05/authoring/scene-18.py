# Authoring module for kukhnya-s05e05-scene-18.
ID = 'kukhnya-s05e05-scene-18'
SHOW = 'kukhnya'
SEASON = 5
EPISODE = 5
SCENE = 18
TITLE = 'Благодарность за сплетню  (Gratitude for the Gossip)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'denis': 'Денис', 'katya': 'Катя', 'kostya': 'Костя'}
SOURCE_NAME = 'Кухня (Kukhnya) S5.05'
SOURCE_FILE = 'sources/kukhnya/s05/e05.ru.srt'
INTRO = 'At the bar counter, Denis warmly thanks Kostya for spilling his secret to Katya, assuming Kostya told her the real reason they broke up. Kostya desperately tries to explain that there is one tiny catch.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'Before Kostya can finish explaining his lie about the child in Voronezh, Eleonora marches into the kitchen arguing with Katya. See you next time!'
CLOSING = ('kostya', 'Хорошего дня!')
STORY = [
    ('kostya', 'Кать, тебя Элеонора Андреевна зовёт.', 'Katya, Eleonora Andreyevna is calling for you.', [(309, 'Кать, Кать, тебя'), (309, 'зовет')], 'adapted'),
    ('denis', 'Слушай, не думал, что я такое скажу.', 'Listen, I did not think that I would say such a thing.', [(311, 'Слушай, не думал, что когда-нибудь я такое скажу')], 'adapted'),
    ('denis', 'Но спасибо тебе за то, что ты трепло.', 'But thank you for being a blabbermouth.', [(311, 'но спасибо тебе за то'), (312, 'что ты трепло')], 'adapted'),
    ('kostya', 'Не понял.', 'I did not understand.', [(313, 'Не понял')], 'adapted'),
    ('denis', 'Я знаю, что ты во всём признался.', 'I know that you confessed everything.', [(314, 'Я знаю, что'), (314, 'во всем признался')], 'adapted'),
    ('denis', 'Катя так спокойно отреагировала.', 'Katya reacted so calmly.', [(315, 'так спокойно отреагировала')], 'adapted'),
    ('denis', 'У меня аж груз с плеч свалился.', 'A huge weight fell right off my shoulders.', [(315, 'у меня аж груз с')], 'adapted'),
    ('kostya', 'Слушай, Дэн, есть один нюанс.', 'Listen, Den, there is one catch.', [(316, 'Слушай, Дэн, есть один нюанс')], 'adapted'),
    ('denis', 'О чём ты говоришь?', 'What are you talking about?', [(313, 'Не понял')], 'adapted'),
    ('katya', 'Мам, это только наше с Денисом дело.', "Mom, this is only Denis's and my business.", [(317, 'Мам, это только наше с Денисом дело')], 'adapted'),
    ('kostya', 'Тебе лучше самому с ней поговорить.', 'You had better talk to her yourself.', [(316, 'есть один нюанс')], 'adapted'),
    ('denis', 'Ладно, сейчас всё выясним.', 'Alright, we will sort everything out right now.', [(314, 'Я знаю, что')], 'adapted'),
]
WALK = [
    (0, None, "'Katya, Eleonora Andreyevna is calling for you.' Kostya chimes in frankly with Denis, refusing to let the moment slip past."),
    (1, None, '\'Listen, I did not think that I would say such a thing.\' Denis replies boldly at once and brings in "slushay" ("listen", from "slushat") as the key Russian word here.'),
    (2, None, "'But thank you for being a blabbermouth.' Denis pushes back evenly with a shrug, keeping the focus on what actually matters here."),
    (3, None, "'I did not understand.' Kostya steps in firmly during the talk, bringing things back to earth after the buildup."),
    (4, None, '\'I know that you confessed everything.\' Denis cuts in naturally at once and puts the weight on "priznalsya" ("did he confess", from "priznatsya") as the exchange unfolds.'),
    (5, None, "'Katya reacted so calmly.' Leaning in quietly in the exchange, spoken Russian compresses the whole thought into just 4 words, skipping the extra helper words English needs."),
    (6, None, "'A huge weight fell right off my shoulders.' Addressing a huge weight around Kostya, Denis sets the direction for the rest of the talk with Kostya."),
    (7, None, '\'Listen, Den, there is one catch.\' Highlighting the nuance around Denis, Kostya leans on "nyuans" ("nuance, catch") to give the whole sentence its punch.'),
    (8, None, "'What are you talking about?' Turning firmly on the spot, Denis keeps normal statement word order here, turning the line into a question for Katya purely through rising pitch."),
    (9, None, "'Mom, this is only Denis's and my business.' Katya jumps in honestly around Denis, to clear the air between them once and for all."),
    (10, None, '\'You had better talk to her yourself.\' Kostya reacts smoothly to Katya and leans on "pogovorit" ("to talk") to give the whole sentence its punch.'),
    (11, None, '\'Alright, we will sort everything out right now.\' Denis simply chooses this word of agreement at the start of the beat using "ladno" ("alright") — built from the old Russian root for harmony and order, used every day for "okay, fine".'),
]
