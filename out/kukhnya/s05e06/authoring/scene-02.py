# Authoring module for kukhnya-s05e06-scene-02.
ID = 'kukhnya-s05e06-scene-02'
SHOW = 'kukhnya'
SEASON = 5
EPISODE = 6
SCENE = 2
TITLE = "Клептомания Сени  (Senya's Kleptomania)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'lyova': 'Лёва', 'senya': 'Сеня'}
SOURCE_NAME = 'Кухня (Kukhnya) S5.06'
SOURCE_FILE = 'sources/kukhnya/s05/e06.ru.srt'
INTRO = 'In the storage room, Chef Barinov reads off an inventory of olive oil, shrimp, and oysters that Senya tried to sneak out of the kitchen this week. Senya swears he will never steal again.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'Now on his final warning from Chef Barinov, Senya reluctantly puts the stolen delicacies back on the shelf. See you next time!'
CLOSING = ('barinov', 'До завтра!')
STORY = [
    ('barinov', 'Масло оливковое, две бутылки.', 'Olive oil, two bottles.', [(29, 'Масло оливковое. Две бутылки')], 'adapted'),
    ('barinov', 'Креветки, одна пачка.', 'Shrimp, one pack.', [(30, 'Креветки. Одна пачка')], 'adapted'),
    ('barinov', 'Устрицы, пять штук, соль и перец.', 'Oysters, five pieces, salt and pepper.', [(31, 'Устрицы. Пять штук. Соль'), (32, 'Перец')], 'adapted'),
    ('barinov', 'Это ты пытался украсть за эту неделю.', 'This is what you tried to steal this week.', [(32, 'ты пытался украсть только за эту неделю')], 'adapted'),
    ('lyova', 'А может, у него клептомания?', 'Or maybe he has kleptomania?', [(33, 'А может, у него клептомания')], 'adapted'),
    ('lyova', 'Может, его лечить надо?', 'Maybe he needs to be treated?', [(33, 'Может, его лечить надо')], 'adapted'),
    ('barinov', 'Для начала я его уволю.', 'For starters, I will fire him.', [(34, 'для начала я его уволю')], 'adapted'),
    ('barinov', 'А потом пусть лечится.', 'And after that let him get treated.', [(34, 'а потом пусть лечится')], 'adapted'),
    ('senya', 'Я больше не буду так, клянусь.', 'I will not do that anymore, I swear.', [(35, 'Я больше не буду так, клянусь')], 'adapted'),
    ('senya', 'Ещё раз поймаешь, увольняй.', 'If you catch me one more time, fire me.', [(36, 'Еще раз поймаешь, увольняй')], 'adapted'),
    ('barinov', 'Хорошо.', 'Fine.', [(37, 'Хорошо')], 'adapted'),
    ('senya', 'Ну, этот раз не в счёт, ладно?', 'Well, this time does not count, alright?', [(38, 'это раз не в счет, ладно')], 'adapted'),
]
WALK = [
    (0, None, "'Olive oil, two bottles.' Barinov sends the reply facing Lyova: spoken Russian trims this down to just 4 words, dropping the extra helper words that English has to spell out."),
    (1, None, "'Shrimp, one pack.' Barinov answers evenly as they talk, saying out loud what both of them already know."),
    (2, None, '\'Oysters, five pieces, salt and pepper.\' Barinov frames this sharp piece in earnest: "ustritsy" means "waste", and it carries the main weight of what Barinov is saying.'),
    (3, None, '\'This is what you tried to steal this week.\' Barinov colors one familiar touch on cue: "nedelyu" means "for a week" (from "nedelya"), giving the line its exact edge.'),
    (4, None, "'Or maybe he has kleptomania?' Lyova inquires frankly if there is more going on behind the scenes."),
    (5, None, '\'Maybe he needs to be treated?\' Lyova features one pointed word in reply: "mozhet" means "can" (from "moch"), giving the line its exact edge.'),
    (6, None, "'For starters, I will fire him.' Barinov steps in briskly across the room, shifting the whole mood of the room in a single beat."),
    (7, None, "'And after that let him get treated.' Barinov fires back earnestly as things stand, saying out loud what both of them already know."),
    (8, None, '\'I will not do that anymore, I swear.\' Senya anchors this direct word in earnest: "klyanus" means "I swear" (from "klyastsya"), giving the line its exact edge.'),
    (9, None, "'If you catch me one more time, fire me.' Senya hands over this line toward Lyova: spoken Russian trims this down to just 4 words, dropping the extra helper words that English has to spell out."),
    (10, None, "'Fine.' Barinov fires back sharply around Lyova, grounding the moment in plain reality."),
    (11, None, '\'Well, this time does not count, alright?\' Senya grounds one classic piece in reply: "schyot" means "counting, account", and it carries the main weight of what Senya is saying.'),
]
