ID = 'kukhnya-s06e04-scene-06'
SHOW = "kukhnya"
SEASON = 6
EPISODE = 4
SCENE = 6
TITLE = "Амбиции Никиты  (Nikita's Ambitions)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {'narrator': 'sky', 'anya': 'alisa', 'nikita': 'anja', 'mikhail': 'angelina'}
LABELS = {'anya': 'Денис', 'nikita': 'Никита', 'mikhail': 'Михаил'}
SOURCE_NAME = "Кухня (Kukhnya) S6.04"
SOURCE_FILE = 'sources/kukhnya/s06/e04.ru.srt'

INTRO = 'In the hotel corridor, Nikita tries to pull rank on Denis and then boasts to a colleague that he plans to replace hotel manager Mikhail Dzhekovich because Mikhail is old—with Mikhail standing right behind him.'

STORY = [
    ('nikita', 'Денис, можно тебя на минутку?', 'Denis, may I have a word with you for a minute?', [(90, 'Денис, можно тебя на минутку?')], 'exact'),
    ('nikita', 'Ты на работе, поэтому займи свое рабочее место.', 'You are at work, so take your workstation.', [(91, 'ты на работе, поэтому, пожалуйста, займи свое рабочее место')], 'adapted'),
    ('anya', 'Мой начальник — Михаил Джекович.', 'My boss is Mikhail Dzhekovich.', [(92, 'Мой начальник Михаил Джекович')], 'exact'),
    ('anya', 'Поэтому убери руку, пожалуйста.', 'So take your hand off me, please.', [(93, 'Поэтому убери руку, пожалуйста')], 'exact'),
    ('nikita', 'Да, но и со мной портить отношения не стоит.', 'Yes, but it is not worth ruining relations with me either.', [(95, 'Но и со мной портить отношения не стоит')], 'adapted'),
    ('anya', 'Ты хочешь занять место управляющего?', "Do you want to take the manager's place?", [(97, 'на место управляющего?')], 'adapted'),
    ('nikita', 'Ну а почему бы и нет?', 'Well and why not?', [(98, 'Ну, а почему бы и нет?')], 'exact'),
    ('nikita', 'Джекович уже старый, теряет хватку.', 'Dzhekovich is already old, he is losing his grip.', [(99, 'Джекович уже старый, теряет хватку')], 'exact'),
    ('mikhail', 'Во-первых, не старый, а опытный.', 'First of all, not old, but experienced.', [(100, 'во-первых, не старый, а опытный')], 'adapted'),
    ('mikhail', 'А во-вторых, хватку иногда надо ослабить.', 'And secondly, sometimes you need to loosen your grip.', [(101, 'Во-вторых, хватку иногда надо ослабить')], 'exact'),
    ('mikhail', 'Извините, что прервал вашу беседу, хорошего дня.', 'Sorry to interrupt your conversation, have a good day.', [(102, 'Извините, что прервал вашу беседу'), (103, 'Хорошего дня')], 'adapted'),
    ('nikita', 'Ты специально меня подставил?', 'Did you set me up on purpose?', [(104, 'специально меня подставил?')], 'adapted'),
]

OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."

WALK = [
    (0, None, "'Denis, may I have a word with you for a minute?' In Russian, the idea of 'Denis' flows naturally into 'a minute' without extra filler words."),
    (1, None, "'You are at work, so take your workstation.' Here the Russian phrasing highlights 'you' before landing on 'place'."),
    (2, None, "'My boss is Mikhail Dzhekovich.' In Russian, the idea of 'my' flows naturally into 'Mikhail' without extra filler words."),
    (3, None, "'So take your hand off me, please.' Spoken Russian keeps this brisk, leaning on 'therefore' and finishing on 'please'. Nikita answers right away."),
    (4, None, "'Yes, but it is not worth ruining relations with me either.' Nikita brings out the contrast between 'yes' and 'but' in a few short words."),
    (5, None, "'Do you want to take the manager's place?' Spoken Russian keeps this brisk, leaning on 'you' and finishing on 'manager'."),
    (6, None, "'Well and why not?' Spoken Russian keeps this brisk, leaning on 'come on' and finishing on 'no'."),
    (7, None, "'Dzhekovich is already old, he is losing his grip.' Nikita anchors the line on 'already', while 'grip' completes the thought."),
    (8, None, "'First of all, not old, but experienced.' The grammar packs 'first of all' and 'experienced' into a tight, idiomatic kitchen exchange."),
    (9, None, "'And secondly, sometimes you need to loosen your grip.' The meaning hinges on 'and' working together with 'to loosen' in spoken Russian."),
    (10, None, "'Sorry to interrupt your conversation, have a good day.' Here the Russian phrasing highlights 'excuse me' before landing on 'day'."),
    (11, None, "'Did you set me up on purpose?' In Russian, the idea of 'you' flows naturally into 'set up' without extra filler words."),
]

TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "Furious after embarrassing himself in front of Mikhail, Nikita takes out his anger by gluing Denis's piano lid shut. See you in the next scene."
CLOSING = ('mikhail', 'Не старый, а опытный!')
