# Authoring module for kukhnya-s05e10-scene-14.
ID = 'kukhnya-s05e10-scene-14'
SHOW = 'kukhnya'
SEASON = 5
EPISODE = 10
SCENE = 14
TITLE = 'Плата за молчание и коктейль  (Hush Money and a Cocktail)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'max': 'Макс', 'mikhail': 'Михаил', 'nastya': 'Настя'}
SOURCE_NAME = 'Кухня (Kukhnya) S5.10'
SOURCE_FILE = 'sources/kukhnya/s05/e10.ru.srt'
INTRO = 'After Senya hints that he must report the injury to the police unless he is paid for his silence, Mikhail promises to settle up with him. In the restaurant, a polite woman orders a Sex on the Beach cocktail from Nastya while Max frets over his mistake.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'That brings the bar scene to a close. Listen for the cocktail order that suddenly gives Max the clue he needed to solve the mystery. See you next time!'
CLOSING = ('max', 'До свидания!')
STORY = [
    ('max', 'Надо в полицию сообщать. Понял?', 'We have to report it to the police. Understood?', [(203, 'полицию сообщать'), (204, 'Понял')], 'adapted'),
    ('mikhail', 'Не понял. За молчание, да?', 'I did not understand. For silence, yes?', [(204, 'Не понял'), (206, 'там')], 'adapted'),
    ('mikhail', 'Ничего, вы не беспокойтесь. Мы решим это.', 'It is nothing, do not worry. We will solve this.', [(206, 'Ничего, вы не беспокойтесь'), (207, 'Мы решим это')], 'adapted'),
    ('nastya', 'Добрый день. Готовы делать заказ?', 'Good afternoon. Are you ready to place an order?', [(208, 'Добрый день'), (209, 'Готовы делать заказ')], 'adapted'),
    ('mikhail', 'Да, пожалуйста, коктейль.', 'Yes, please, a cocktail.', [(209, 'Да, пожалуйста, коктейли')], 'adapted'),
    ('mikhail', 'Коктейль на пляже.', 'A beach cocktail.', [(210, 'на пляже')], 'adapted'),
    ('max', 'Вика сильно расстроилась.', 'Vika got very upset.', [(211, 'Вика сильно расстроилась')], 'adapted'),
    ('max', 'Как думаешь, я проверку сорвал?', 'What do you think, did I ruin the inspection?', [(212, 'Как думаешь? Я, наверное, проверку сорвал')], 'adapted'),
    ('nastya', 'Конечно сорвал, Макс.', 'Of course you ruined it, Max.', [(212, 'проверку сорвал')], 'adapted'),
    ('nastya', 'Костя, сделай один коктейль на пляже!', 'Kostya, make one beach cocktail!', [(213, 'Костя, один'), (213, 'на пляже')], 'adapted'),
    ('max', 'Подожди, что она заказала?', 'Wait, what did she order?', [(209, 'заказ')], 'adapted'),
    ('nastya', 'Пожалуйста, ваш коктейль.', 'Here you go, your cocktail.', [(209, 'пожалуйста, коктейли')], 'adapted'),
]
WALK = [
    (0, None, "'We have to report it to the police. Understood?' Max asks whether they have to report it to the police, refusing to let the point slide. Russian packs the whole idea of what is allowed or needed into one impersonal word at the front."),
    (1, None, '\'I did not understand. For silence, yes?\' Asking whether he did not understand puts Max right on the defensive. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (2, None, "'It is nothing, do not worry. We will solve this.' Claiming that it is nothing do not worry sounds confident, even if Max has doubts."),
    (3, None, '\'Good afternoon. Are you ready to place an order?\' Asking whether Max ready to place an order cuts straight through the tension between Nastya and Max. In Russian, she does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (4, None, "'Yes, please, a cocktail.' With the conversation and police in play, Mikhail keeps this short reply brisk and direct."),
    (5, None, "'A beach cocktail.' Over the conversation and the police, Mikhail answers Max without a second thought."),
    (6, None, "'Vika got very upset.' Noting that Vika got very upset keeps Max's side of the story simple and clear."),
    (7, None, '\'What do you think, did I ruin the inspection?\' Wondering what Mikhail thinks did he ruins the inspection cuts straight through the tension between Max and Mikhail. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (8, None, "'Of course you ruined it, Max.' Over the conversation and the mistake, Nastya answers Max without a second thought."),
    (9, None, "'Kostya, make one beach cocktail!' Nastya insists that Max should make one beach cocktail, leaving Max no room to argue. Russian puts the key word right up front so her emotion lands on the first beat."),
    (10, None, '\'Wait, what did she order?\' By wondering what she order, Max presses Mikhail for a straight answer. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (11, None, "'Here you go, your cocktail.' Adding that here Max goes Max's cocktail fills in the missing piece for Max."),
]
