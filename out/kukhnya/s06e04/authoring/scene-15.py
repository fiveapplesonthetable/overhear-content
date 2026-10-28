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
    (0, None, "'Where is your restroom?' Nikita prompts skeptically if there is more going on behind the scenes."),
    (1, None, '\'To the left down the corridor.\' Barinov picks one concrete choice for Nikita: "koridoru" means "corridor, hall" (from "koridor"), giving the line its exact edge.'),
    (2, None, "'So if he is not real, maybe I should pour him the cheapest wine?' Nikita drops the comment frankly here: Russian keeps the exact word order of a normal statement here, turning it into a question for Barinov purely through rising pitch at the end."),
    (3, None, "'Why waste good product on him?' Nikita inquires promptly to see how Katya will answer on the spot."),
    (4, None, '\'That photograph does not prove anything at all.\' Barinov features this clear term in reply: "fotografiya" means "photograph", and it carries the main weight of what Barinov is saying.'),
    (5, None, "'Maybe this guy is an inspector too.' Barinov fires back honestly with Nikita, to clear the air between them once and for all."),
    (6, None, "'The dish lacks spiciness.' Barinov responds at once without any doubt, so Katya knows he is not just making small talk."),
    (7, None, '\'Well there, now it is just right.\' Barinov anchors one key element in earnest: "samyy" means "the most", and it carries the main weight of what Barinov is saying.'),
    (8, None, "'I think the respected inspector should like it.' Barinov continues pointedly across the room, making his position completely clear."),
    (9, None, "'Katya, wait, we have an important conversation.' Nikita steps in promptly without a pause, testing Katya's reaction in the middle of the exchange."),
    (10, None, '\'The thing is that Nikita glued the piano lid shut, and I decided to get revenge.\' Barinov sharpens this sharp choice on cue: "kryshku" means "lid" (from "kryshka"), giving the line its exact edge.'),
    (11, None, '\'How exactly did you get revenge?\' Katya drops this line at once: putting the question word "kak" right at the front of the line lets Nikita hear the point of the question on the very first beat.'),
]
