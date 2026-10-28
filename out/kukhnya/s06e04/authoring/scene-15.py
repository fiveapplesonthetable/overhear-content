# Authoring module for kukhnya-s06e04-scene-15.
ID = 'kukhnya-s06e04-scene-15'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 4
SCENE = 15
TITLE = 'Острый соус и месть за рояль  (Hot Sauce and Revenge for the Piano)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'katya': 'Катя', 'nikita': 'Никита'}
SOURCE_NAME = 'Кухня (Kukhnya) S6.04'
SOURCE_FILE = 'sources/kukhnya/s06/e04.ru.srt'
INTRO = "Refusing to believe Louis's photo, Barinov spikes Olivier's galantine with hot sauce to teach the supposed fake a lesson—while Denis confesses to Katya how he just booby-trapped Nikita's napkin."
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'Both pranks collide at the exact same table as Barinov marches out with the pepper-loaded galantine. Until next time!'
CLOSING = ('barinov', 'Хорошего дня!')
STORY = [
    ('nikita', 'Где у вас туалет?', 'Where is your restroom?', [(235, 'Где у вас туалет?')], 'exact'),
    ('barinov', 'Налево по коридору.', 'To the left down the corridor.', [(235, 'Налево по коридору')], 'exact'),
    ('nikita', 'Так если он не настоящий, может, я ему самого дешевого вина налью?', 'So if he is not real, maybe I should pour him the cheapest wine?', [(237, 'Так если он не настоящий, может, я ему самого дешевого вина налью?')], 'exact'),
    ('nikita', 'А зачем продукт на него переводить?', 'Why waste good product on him?', [(238, 'продукт на него переводить?')], 'adapted'),
    ('barinov', 'Эта фотография вообще ничего не доказывает.', 'That photograph does not prove anything at all.', [(239, 'Эта фотография вообще ничего не доказывает')], 'exact'),
    ('barinov', 'Может быть, это тоже инспектор.', 'Maybe this guy is an inspector too.', [(240, 'Может быть, это тоже инспектор')], 'exact'),
    ('barinov', 'В блюде не хватает остроты.', 'The dish lacks spiciness.', [(241, 'Не хватает остроты')], 'adapted'),
    ('barinov', 'Ну вот, теперь в самый раз.', 'Well there, now it is just right.', [(244, 'Ну вот, теперь в самый раз')], 'exact'),
    ('barinov', 'Думаю, уважаемому инспектору должно понравиться.', 'I think the respected inspector should like it.', [(245, 'Думаю, уважаемому инспектору')], 'adapted'),
    ('nikita', 'Катя, подожди, у нас важный разговор.', 'Katya, wait, we have an important conversation.', [(246, 'Катя!'), (247, 'Подожди, у нас важный разговор')], 'adapted'),
    ('barinov', 'Дело в том, что Никита склеил крышку рояля, и я решил отомстить.', 'The thing is that Nikita glued the piano lid shut, and I decided to get revenge.', [(249, 'дело в том, что Никита'), (249, 'крышку рояля'), (250, 'И я решил отомстить')], 'adapted'),
    ('katya', 'Как именно отомстить?', 'How exactly did you get revenge?', [(251, 'Как отомстить?')], 'adapted'),
]
WALK = [
    (0, None, "'Where is your restroom?' Nikita prompts skeptically to see how Barinov will answer on the spot."),
    (1, None, '\'To the left down the corridor.\' Emphasizing the corridor before Nikita, Barinov reaches for the Russian word "koridoru" ("corridor, hall", built from "koridor") right at the center of the line.'),
    (2, None, "'So if he is not real, maybe I should pour him the cheapest wine?' Confirming how real he is around Barinov, Nikita keeps normal statement word order here, turning the line into a question for Barinov purely through rising pitch."),
    (3, None, "'Why waste good product on him?' Nikita inquires promptly if there is more going on behind the scenes."),
    (4, None, '\'That photograph does not prove anything at all.\' Underscoring the photograph at once, Barinov uses "fotografiya" ("photograph") to carry the main weight of the thought.'),
    (5, None, '\'Maybe this guy is an inspector too.\' Highlighting an inspector in the exchange, Barinov uses "inspektor" ("inspector") to carry the main weight of the thought.'),
    (6, None, "'The dish lacks spiciness.' Focusing on the spiciness facing Nikita, Barinov lets Nikita see exactly where things stand."),
    (7, None, '\'Well there, now it is just right.\' Barinov follows up promptly right here and centers the remark on "samyy" ("the most") without any extra fuss.'),
    (8, None, '\'I think the respected inspector should like it.\' Discussing the respected inspector beside Nikita, Barinov uses "uvazhayemomu" ("respected", from "uvazhayemyy") to make the point stick.'),
    (9, None, "'Katya, wait, we have an important conversation.' Nikita jumps in promptly without holding back, letting the remark speak for itself."),
    (10, None, '\'The thing is that Nikita glued the piano lid shut, and I decided to get revenge.\' Underscoring the piano lid beside Nikita, Barinov lands on "kryshku" ("lid", built on "kryshka") to keep the statement grounded.'),
    (11, None, '\'How exactly did you get revenge?\' Stepping in warmly on the spot, Katya puts the question word "kak" right at the start so Barinov hears the focus immediately.'),
]
