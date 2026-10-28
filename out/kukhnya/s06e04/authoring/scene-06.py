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
    (0, None, "'Denis, may I have a word with you for a minute?' Questioning whether may he has a word with Denis for a minute is how Nikita tests Denis's story. Russian packs the whole idea of what is allowed or needed into one impersonal word at the front."),
    (1, None, "'You are at work, so take your workstation.' Since Denis is at work so take Denis's workstation, Nikita does not waste words on excuses."),
    (2, None, '\'My boss is Mikhail Dzhekovich.\' Mentioning that his boss is Mikhail Dzhekovich moves the talk in a new direction. Russian drops "is" in the present, setting the two halves of the thought side by side.'),
    (3, None, "'So take your hand off me, please.' Realizing that Mikhail should take Mikhail's hand off him please changes how Denis handles the situation."),
    (4, None, "'Yes, but it is not worth ruining relations with me either.' Because it is not worth ruining relations with him either, Nikita treats the matter as settled."),
    (5, None, '\'Do you want to take the manager\'s place?\' Checking whether Mikhail wants to take the manager place cuts straight through the tension between Denis and Mikhail. Speaking with the close, informal "you" strips away any polite distance between them.'),
    (6, None, '\'Well and why not?\' Over the work and the job, Nikita presses Denis for a straight answer. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (7, None, "'Dzhekovich is already old, he is losing his grip.' Claiming that Dzhekovich is already old he is losing his grip sounds confident, even if Denis has doubts."),
    (8, None, "'First of all, not old, but experienced.' With the plan and job in play, Mikhail keeps this short reply brisk and direct."),
    (9, None, '\'And secondly, sometimes you need to loosen your grip.\' Mikhail explains that secondly sometimes Denis needs to loosen Denis\'s grip, keeping his voice calm and direct. There is no "you" needed in the Russian here: one short word states the rule for everyone in the room.'),
    (10, None, "'Sorry to interrupt your conversation, have a good day.' Realizing that to interrupt Denis's conversation have a good day changes how Mikhail handles the situation."),
    (11, None, '\'Did you set me up on purpose?\' Here checking whether Denis sets him up on purpose shows Nikita looking for the real truth. Speaking with the close, informal "you" strips away any polite distance between them.'),
]
