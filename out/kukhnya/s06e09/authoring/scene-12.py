# Authoring module for kukhnya-s06e09-scene-12.
ID = 'kukhnya-s06e09-scene-12'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 9
SCENE = 12
TITLE = 'Случайная публикация  (Accidental Publication)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'fedya': 'Федя', 'mikhail': 'Михаил'}
SOURCE_NAME = 'Кухня (Kukhnya) S6.09'
SOURCE_FILE = 'sources/kukhnya/s06/e09.ru.srt'
INTRO = "Gathered around the laptop in the office, Barinov, Mikhail, Senya, and Fedya compose a wildly exaggerated rave review of Restaurant Victor in Elena's name. While joking around, Fedya accidentally clicks publish and logs out of the account."
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "To make matters worse, Fedya accidentally logs out of Elena's profile without knowing the password, leaving the ridiculous review live online. See you next time!"
CLOSING = ('barinov', 'До встречи!')
STORY = [
    ('barinov', 'Пиши, вчера мне посчастливилось побывать в ресторане.', 'Write: yesterday I was lucky enough to visit the restaurant.', [(203, 'Вчера мне посчастливилось побывать'), (204, 'в ресторане')], 'adapted'),
    ('mikhail', 'Это настоящее святое место французской кухни.', 'This is a true sacred place of French cuisine.', [(205, 'Святая святых французской'), (206, 'кухни')], 'adapted'),
    ('barinov', 'Миша, нет, такие слова звучат нехорошо.', 'Misha, no, such words do not sound good.', [(206, 'Миша, нехорошо')], 'adapted'),
    ('fedya', 'Тогда давай напишем цитадель французской кухни.', 'Then let us write the citadel of French cuisine.', [(208, 'Давай цитадель французской кухни')], 'adapted'),
    ('barinov', 'Точно, цитадель звучит намного лучше и красивее.', 'Exactly, citadel sounds much better and nicer.', [(209, 'Точно цитадель')], 'adapted'),
    ('mikhail', 'И великий кулинарный гений шефа Виктора Баринова.', 'And the great culinary genius of Chef Viktor Barinov.', [(210, 'И кулинарный гений'), (211, 'Виктора Баринова')], 'adapted'),
    ('fedya', 'Удивит всех гостей самыми изысканными блюдами.', 'Will amaze all guests with the most exquisite dishes.', [(212, 'утолит ваши самые изощренные')], 'adapted'),
    ('mikhail', 'Давайте добавим сюда ещё одно красивое слово.', 'Let us add one more beautiful word here.', [(213, 'гастрономические похоти')], 'adapted'),
    ('fedya', 'Ой, кажется, я случайно нажал кнопку.', 'Oops, I think I accidentally pressed the button.', [(215, 'Ой')], 'adapted'),
    ('barinov', 'Подожди, что ты только что сделал?', 'Wait, what did you just do?', [(216, 'Ты что сейчас сделал')], 'adapted'),
    ('fedya', 'Шеф, я случайно опубликовал эту заметку.', 'Chef, I accidentally published this post.', [(216, 'Опубликовал')], 'adapted'),
    ('mikhail', 'Зачем ты нажал, давай скорее стирай!', 'Why did you press it, come on, erase it quickly!', [(217, 'Зачем'), (217, 'Ну, давай, стирай, стирай')], 'adapted'),
    ('barinov', 'Стирай немедленно, пока Лена не увидела!', 'Erase it immediately before Lena sees it!', [(217, 'стирай, стирай')], 'adapted'),
]
WALK = [
    (0, None, "'Write: yesterday I was lucky enough to visit the restaurant.' Admitting that Fedya should write yesterday he was lucky enough to visit the restaurant shows Barinov being honest for a change."),
    (1, None, "'This is a true sacred place of French cuisine.' Once this is a true sacred place of French cuisine, Mikhail can finally tell Barinov what he means."),
    (2, None, "'Misha, no, such words do not sound good.' Adding that such words do not sound good fills in the missing piece for Fedya."),
    (3, None, '\'Then let us write the citadel of French cuisine.\' Fedya mentions that they should write the citadel of French cuisine so Barinov sees what is at stake. Starting with "davay" is the everyday Russian way to say "come on, let us do this".'),
    (4, None, "'Exactly, citadel sounds much better and nicer.' Since exactly citadel sounds much better and nicer, Barinov does not waste words on excuses."),
    (5, None, "'And the great culinary genius of Chef Viktor Barinov.' Around the restaurant and office, Mikhail sets a calm, everyday tone with Barinov."),
    (6, None, "'Will amaze all guests with the most exquisite dishes.' Fedya reminds Barinov that will amaze all guests with the most exquisite dishes before the moment passes."),
    (7, None, "'Let us add one more beautiful word here.' Claiming that they should add one more beautiful word here sounds confident, even if Barinov has doubts."),
    (8, None, "'Oops, I think I accidentally pressed the button.' Explaining that someone he thinks he accidentally pressed the button lays the cards on the table for Barinov."),
    (9, None, '\'Wait, what did you just do?\' Wondering what Fedya just do is how Barinov puts Fedya on the spot. Speaking with the close, informal "you" strips away any polite distance between them.'),
    (10, None, "'Chef, I accidentally published this post.' Between the restaurant and the office, Fedya gives Barinov a quick, grounded response."),
    (11, None, '\'Why did you press it, come on, erase it quickly!\' Saying that why did Barinov press it come on erase it quickly is how Mikhail takes charge of the moment. Starting with "davay" is the everyday Russian way to say "come on, let us do this".'),
    (12, None, "'Erase it immediately before Lena sees it!' Barinov declares that erase it immediately before sees it as the tension in the room peaks. Russian puts the key word right up front so his emotion lands on the first beat."),
]
