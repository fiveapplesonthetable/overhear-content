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
    (0, None, "'Olive oil, two bottles.' Over the kitchen and the point, Barinov answers Lyova without a second thought."),
    (1, None, "'Shrimp, one pack.' Around the kitchen and truth, Barinov sets a calm, everyday tone with Lyova."),
    (2, None, "'Oysters, five pieces, salt and pepper.' With the kitchen and situation in play, Barinov keeps this short reply brisk and direct."),
    (3, None, '\'This is what you tried to steal this week.\' Claiming that this is what Lyova tried to steal this week sounds confident, even if Lyova has doubts. Speaking with the close, informal "you" strips away any polite distance between them.'),
    (4, None, '\'Or maybe he has kleptomania?\' Asking whether maybe he has kleptomania puts Barinov right on the defensive. In Russian you say "by me" or "with us" rather than "I have", so the situation sits right with the person.'),
    (5, None, "'Maybe he needs to be treated?' Wondering if maybe he needs to be treated shows Lyova caught off guard."),
    (6, None, "'For starters, I will fire him.' Realizing that for starters he will fire him changes how Barinov handles the situation."),
    (7, None, "'And after that let him get treated.' Noting that after that let him get treated keeps Barinov's side of the story simple and clear."),
    (8, None, "'I will not do that anymore, I swear.' Even though he will not do that anymore he swears, Senya keeps a steady face in front of Barinov."),
    (9, None, "'If you catch me one more time, fire me.' Admitting that if Barinov catches him one more time fire him shows Senya being honest for a change."),
    (10, None, "'Fine.' With the moment and kitchen in play, Barinov keeps this short reply brisk and direct."),
    (11, None, "'Well, this time does not count, alright?' Questioning whether this time does not count alright is how Senya tests Barinov's story."),
]
