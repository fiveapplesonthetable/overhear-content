# Authoring module for kukhnya-s01e16-scene-04.
ID = 'kukhnya-s01e16-scene-04'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 16
SCENE = 4
TITLE = 'Любопытный Макс  (Curious Max)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.16'
SOURCE_FILE = 'sources/kukhnya/s01/e16.ru.dual.srt'
INTRO = 'In the kitchen, Max is bored and looking for a distraction. He approaches Chef Victor and curiously asks about the special dish the chef is preparing, but Victor quickly shuts him down. Let us listen to their conversation in Russian first.'
OPENER = 'Now let us examine the conversation line by line.'
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "In the kitchen, Max approaches Chef Barinov during a five-minute break, asking what he is cooking and hoping to learn from him and taste the dish. Next time you watch the episode, listen for the Russian expressions for 'it is necessary' and 'to cook' — you will catch every word right away. See you next time!"
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('max', 'Шеф.', 'Chef.', [(33, 'Шеф.')], ''),
    ('barinov', 'Что тебе надо?', 'What do you need?', [], ''),
    ('max', 'А что вы готовите?', 'And what are you preparing?', [(34, 'А что вы готовите?')], ''),
    ('barinov', 'А тебе какое дело?', 'And what is it to you?', [(34, 'Тебе какое дело?')], ''),
    ('barinov', 'Тебе нечем заняться?', 'Do you have nothing to do?', [(35, 'Тебе что, заняться нечем?')], ''),
    ('max', 'У меня есть пять минут.', 'I have five minutes.', [(35, 'Ну, у меня пять минут есть,')], ''),
    ('max', 'Я хотел поучиться у вас.', 'I wanted to learn from you.', [(35, 'я хотел поучиться у вас.')], ''),
    ('barinov', 'Иди работай.', 'Go work.', [], ''),
    ('max', 'А можно попробовать?', 'And can I try it?', [(36, 'А можно попробовать?')], ''),
    ('barinov', 'Нет, нельзя.', 'No, you cannot.', [], ''),
    ('max', 'Почему?', 'Why?', [], ''),
    ('barinov', 'Потому что я так сказал.', 'Because I said so.', [], ''),
    ('max', 'Ладно, я понял.', 'Alright, I understand.', [], ''),
    ('barinov', 'Тогда иди отсюда.', 'Then go from here.', [], ''),
]
WALK = [
    (0, None, "'Chef.' Max tries to grab his boss's attention with a respectful title."),
    (1, None, "'What do you need?' Barinov snaps back, annoyed by the interruption."),
    (2, None, "'And what are you preparing?' Curious about the dish, Max attempts to start a conversation about cooking."),
    (3, None, "'And what is it to you?' The chef dismisses the question entirely, refusing to share his process."),
    (4, None, "'Do you have nothing to do?' Barinov implies that his subordinate should be busy with his own tasks instead of hovering."),
    (5, None, "'I have five minutes.' Max defends his presence by pointing out his brief break."),
    (6, None, "'I wanted to learn from you.' He flatters the older man, expressing a desire to pick up some culinary skills."),
    (7, None, "'Go work.' Unmoved by the compliment, the boss orders him back to his station."),
    (8, None, "'And can I try it?' Max pushes his luck, asking for a taste of the mysterious dish."),
    (9, None, "'No, you cannot.' Barinov flatly denies the request without any hesitation."),
    (10, None, "'Why?' Max whines a little, looking for a reason behind the strict refusal."),
    (11, None, "'Because I said so.' The chef shuts down the argument using his absolute authority."),
    (12, None, "'Alright, I understand.' Defeated, Max backs off and accepts the rejection."),
    (13, None, "'Then go from here.' Barinov delivers a final, harsh instruction for the younger man to leave the area."),
]
