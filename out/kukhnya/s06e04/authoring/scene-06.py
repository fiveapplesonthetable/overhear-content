# Authoring module for kukhnya-s06e04-scene-06.
ID = 'kukhnya-s06e04-scene-06'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 4
SCENE = 6
TITLE = "Амбиции Никиты  (Nikita's Ambitions)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'denis': 'Денис', 'mikhail': 'Михаил', 'nikita': 'Никита'}
SOURCE_NAME = 'Кухня (Kukhnya) S6.04'
SOURCE_FILE = 'sources/kukhnya/s06/e04.ru.srt'
INTRO = 'In the hotel corridor, Nikita tries to pull rank on Denis and then boasts to a colleague that he plans to replace hotel manager Mikhail Dzhekovich because Mikhail is old—with Mikhail standing right behind him.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "Furious after embarrassing himself in front of Mikhail, Nikita takes out his anger by gluing Denis's piano lid shut. See you next time!"
CLOSING = ('mikhail', 'До завтра!')
STORY = [
    ('nikita', 'Денис, можно тебя на минутку?', 'Denis, may I have a word with you for a minute?', [(90, 'Денис, можно тебя на минутку?')], 'exact'),
    ('nikita', 'Ты на работе, поэтому займи свое рабочее место.', 'You are at work, so take your workstation.', [(91, 'ты на работе, поэтому, пожалуйста, займи свое рабочее место')], 'adapted'),
    ('denis', 'Мой начальник — Михаил Джекович.', 'My boss is Mikhail Dzhekovich.', [(92, 'Мой начальник Михаил Джекович')], 'exact'),
    ('denis', 'Поэтому убери руку, пожалуйста.', 'So take your hand off me, please.', [(93, 'Поэтому убери руку, пожалуйста')], 'exact'),
    ('nikita', 'Да, но и со мной портить отношения не стоит.', 'Yes, but it is not worth ruining relations with me either.', [(95, 'Но и со мной портить отношения не стоит')], 'adapted'),
    ('denis', 'Ты хочешь занять место управляющего?', "Do you want to take the manager's place?", [(97, 'на место управляющего?')], 'adapted'),
    ('nikita', 'Ну а почему бы и нет?', 'Well and why not?', [(98, 'Ну, а почему бы и нет?')], 'exact'),
    ('nikita', 'Джекович уже старый, теряет хватку.', 'Dzhekovich is already old, he is losing his grip.', [(99, 'Джекович уже старый, теряет хватку')], 'exact'),
    ('mikhail', 'Во-первых, не старый, а опытный.', 'First of all, not old, but experienced.', [(100, 'во-первых, не старый, а опытный')], 'adapted'),
    ('mikhail', 'А во-вторых, хватку иногда надо ослабить.', 'And secondly, sometimes you need to loosen your grip.', [(101, 'Во-вторых, хватку иногда надо ослабить')], 'exact'),
    ('mikhail', 'Извините, что прервал вашу беседу, хорошего дня.', 'Sorry to interrupt your conversation, have a good day.', [(102, 'Извините, что прервал вашу беседу'), (103, 'Хорошего дня')], 'adapted'),
    ('nikita', 'Ты специально меня подставил?', 'Did you set me up on purpose?', [(104, 'специально меня подставил?')], 'adapted'),
]
WALK = [
    (0, None, "'Denis, may I have a word with you for a minute?' Nikita probes curiously what Denis is actually getting at here."),
    (1, None, '\'You are at work, so take your workstation.\' Nikita grounds one clear piece at once: "rabocheye" means "work" (from "rabochiy"), giving the line its exact edge.'),
    (2, None, '\'My boss is Mikhail Dzhekovich.\' Denis gives the reaction right away: notice how Russian needs no word for "am", "is", or "are" in the present — placing the words side by side says it all.'),
    (3, None, "'So take your hand off me, please.' Denis responds at once toward Nikita, leaving no doubt about where he stands."),
    (4, None, '\'Yes, but it is not worth ruining relations with me either.\' Nikita grounds this key choice in reply: "otnosheniya" means "relations, relationship" (from "otnosheniye"), giving the line its exact edge.'),
    (5, None, "'Do you want to take the manager's place?' Denis frames the remark for Nikita: Russian keeps the exact word order of a normal statement here, turning it into a question for Nikita purely through rising pitch at the end."),
    (6, None, "'Well and why not?' Nikita checks straight out whether Denis really thought this through."),
    (7, None, '\'Dzhekovich is already old, he is losing his grip.\' Nikita uses one direct element in reply: "khvatku" means "grip" (from "khvatka"), giving the line its exact edge.'),
    (8, None, "'First of all, not old, but experienced.' Mikhail steps in wryly toward Denis, making his position completely clear."),
    (9, None, "'And secondly, sometimes you need to loosen your grip.' Mikhail continues plainly watching Nikita, shifting the whole mood of the room in a single beat."),
    (10, None, '\'Sorry to interrupt your conversation, have a good day.\' Mikhail uses one practical piece in earnest: "khoroshego" means "good, the best" (from "khoroshiy"), giving the line its exact edge.'),
    (11, None, "'Did you set me up on purpose?' Nikita makes the reply right away: Russian keeps the exact word order of a normal statement here, turning it into a question for Mikhail purely through rising pitch at the end."),
]
