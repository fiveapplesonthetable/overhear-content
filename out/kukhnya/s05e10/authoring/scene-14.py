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
    (0, None, '\'We have to report it to the police. Understood?\' Max hands over this answer without pause: the single Russian word "nado" ("it is necessary, one needs to") sets up the whole statement without needing a separate word for "it is".'),
    (1, None, "'I did not understand. For silence, yes?' Mikhail asks bluntly why things suddenly took this turn between them."),
    (2, None, '\'It is nothing, do not worry. We will solve this.\' Mikhail emphasizes one classic word at once: "bespokoytes" means "worry" (from "bespokoitsya"), giving the line its exact edge.'),
    (3, None, "'Good afternoon. Are you ready to place an order?' Nastya lays out this statement frankly here: Russian keeps the exact word order of a normal statement here, turning it into a question for Mikhail purely through rising pitch at the end."),
    (4, None, "'Yes, please, a cocktail.' Mikhail counters earnestly without a pause, before Max can change the subject."),
    (5, None, '\'A beach cocktail.\' Mikhail chooses one direct detail in earnest: "kokteyl" means "cocktail", and it carries the main weight of what Mikhail is saying.'),
    (6, None, '\'Vika got very upset.\' Max puts the comment plainly here: the "-sya" ending on "rasstroilas" ("got upset") turns the action inward or makes it happen between people naturally.'),
    (7, None, "'What do you think, did I ruin the inspection?' Max prompts plainly where this conversation is heading next."),
    (8, None, '\'Of course you ruined it, Max.\' Nastya reaches for this vivid word at once: "konechno" means "of course", and it carries the main weight of what Nastya is saying.'),
    (9, None, "'Kostya, make one beach cocktail!' Nastya reacts decisively to settle things, refusing to let the moment slip past."),
    (10, None, "'Wait, what did she order?' Max quizzes bluntly to see how Mikhail will answer on the spot."),
    (11, None, '\'Here you go, your cocktail.\' Nastya centers one classic term for Mikhail: "kokteyl" means "cocktail", and it carries the main weight of what Nastya is saying.'),
]
