# Authoring module for kukhnya-s01e16-scene-08.
ID = 'kukhnya-s01e16-scene-08'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 16
SCENE = 8
TITLE = 'Чей паштет лучше  (Whose Pâté is Better)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kostya': 'Костя', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.16'
SOURCE_FILE = 'sources/kukhnya/s01/e16.ru.dual.srt'
INTRO = 'In the bar area of Claude Monet, Kostya tries to tell Max about the exciting raid at Arcobaleno. However, Max is obsessed with his ongoing culinary bet with Chef Viktor and refuses to discuss anything else. He forces Kostya to make a definitive comparison. Let us listen to their conversation in Russian first.'
OPENER = "Now let us examine Kostya and Max's candid conversation line by line."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Although Kostya honestly confirms Chef Viktor's culinary superiority, Max remains determined to crack the secret recipe and win his two days off. Next time you watch the episode, listen for the Russian expressions for 'to hear' and 'important' — you will catch every word right away. See you next time!"
CLOSING = ('kostya', 'Пока!')
STORY = [
    ('kostya', 'Макс, ты слышал важные новости сегодня?', 'Max, did you hear important news today?', [(58, 'А ты слышал про проверку ФМС в другом ресторане?')], ''),
    ('max', 'Какие ещё новости могут волновать меня?', 'What other news could worry me?', [], ''),
    ('kostya', 'В соседнем ресторане сейчас идёт большая проверка.', 'A huge inspection is going on in the neighboring restaurant right now.', [(58, 'в другом ресторане?')], ''),
    ('max', 'Мне сейчас совсем не до чужих проверок.', 'Right now I do not care at all about outside inspections.', [], ''),
    ('kostya', 'Там полиция проверяет всех работников кухни.', 'The police are checking all kitchen workers over there.', [], ''),
    ('max', 'Ответь честно, чей паштет сейчас лучше?', 'Answer honestly, whose pâté is better right now?', [(59, 'Чей паштет лучше, мой или шефа?')], ''),
    ('kostya', 'Ты обещаешь не обижаться на меня?', 'Do you promise not to be offended with me?', [], ''),
    ('max', 'Я хочу услышать только чистую правду.', 'I want to hear only the pure truth.', [], ''),
    ('kostya', 'И ты точно не скажешь шефу?', 'And you definitely will not tell the chef?', [(60, 'А ты шефу не скажешь?')], ''),
    ('max', 'Нет, я просто хочу знать результат.', 'No, I simply want to know the result.', [(60, 'Нет.')], ''),
    ('kostya', 'У шефа этот паштет намного лучше.', 'The chef makes this pâté much better.', [(61, 'У шефа лучше.')], ''),
    ('max', 'Я обязательно найду его секретный ингредиент!', 'I will definitely find his secret ingredient!', [], ''),
    ('kostya', 'Желаю тебе большой удачи в этом!', 'I wish you great luck in that!', [], ''),
]
WALK = [
    (0, None, "'Max, did you hear important news today?' Kostya asks his friend if he has caught wind of the big event happening today."),
    (1, None, "'What other news could worry me?' Max seems completely uninterested, stating that nothing else matters to him right now."),
    (2, None, "'A huge inspection is going on in the neighboring restaurant right now.' Sharing the gossip, the bartender explains that a massive audit is taking place next door."),
    (3, None, "'Right now I do not care at all about outside inspections.' Brushing off the drama, the cook insists he has zero interest in what other places are dealing with."),
    (4, None, "'The police are checking all kitchen workers over there.' Adding more detail, the friend notes that authorities are actively looking at everyone's paperwork."),
    (5, None, "'Answer honestly, whose pâté is better right now?' Ignoring the news entirely, the young chef demands a straight answer about his food comparison."),
    (6, None, "'Do you promise not to be offended with me?' Kostya asks for reassurance that his honest opinion will not cause hurt feelings."),
    (7, None, "'I want to hear only the pure truth.' Promising to handle it, the cook says he only wants the absolute truth."),
    (8, None, "'And you definitely will not tell the chef?' The friend double-checks the safety of his secret, asking if the boss will find out what he said."),
    (9, None, "'No, I simply want to know the result.' Swearing to keep quiet, the cook insists he just needs to know the final verdict."),
    (10, None, "'The chef makes this pâté much better.' Delivering the tough news, the bartender confirms that the boss still holds the crown."),
    (11, None, "'I will definitely find his secret ingredient!' Max vows to keep digging, determined to uncover the missing component."),
    (12, None, "'I wish you great luck in that!' Wishing his buddy well, the bartender hopes he succeeds in his quest."),
]
