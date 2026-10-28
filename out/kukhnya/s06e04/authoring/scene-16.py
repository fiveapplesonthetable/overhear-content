# Authoring module for kukhnya-s06e04-scene-16.
ID = 'kukhnya-s06e04-scene-16'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 4
SCENE = 16
TITLE = "Приступ Шефа  (Chef's Collapse)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'guest': 'Гость', 'katya': 'Катя'}
SOURCE_NAME = 'Кухня (Kukhnya) S6.04'
SOURCE_FILE = 'sources/kukhnya/s06/e04.ru.srt'
INTRO = "At the table, Barinov pushes Olivier's face into the spicy dish while Nikita wipes his eyes with Denis's pepper-sprayed napkin—and when Katya admits she made up the inspector story, Barinov's heart gives out."
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'Overwhelmed by stress after skipping his heart pills, Barinov collapses on the dining room floor and is rushed to the hospital. See you next time!'
CLOSING = ('katya', 'Всего хорошего!')
STORY = [
    ('katya', 'Папа об этом знает?', 'Does Dad know about this?', [(252, 'Папа знает?')], 'adapted'),
    ('barinov', 'А вот и ваше блюдо, почти такое же, как у вашей бабушки!', "And here is your dish, almost the same as your grandmother's!", [(253, 'А вот и ваш'), (254, 'Почти такой же, как у вашей бабушки')], 'adapted'),
    ('guest', 'Спасибо, но я уже сыт.', 'Thank you, but I am already full.', [(255, 'Спасибо, я сыт')], 'adapted'),
    ('barinov', 'Я вас умоляю, хотя бы понюхайте!', 'I beg you, at least smell it!', [(256, 'Я вас умоляю, хотя бы понюхайте')], 'exact'),
    ('barinov', 'Будьте так добры, понюхайте блюдо.', 'Be so kind, smell the dish.', [(257, 'Будьте так добры')], 'adapted'),
    ('guest', 'Мои глаза, мои глаза!', 'My eyes, my eyes!', [(259, 'глаза! Глаза!')], 'adapted'),
    ('katya', 'Вы оба просто сумасшедшие!', 'You are both simply crazy!', [(260, 'Вы оба')], 'adapted'),
    ('barinov', 'Не волнуйся, я куплю тебе темные очки.', 'Do not worry, I will buy you dark glasses.', [(261, 'Не волнуйся, я куплю тебе'), (261, 'темные очки')], 'adapted'),
    ('katya', 'Папа, я тебе все сейчас объясню.', 'Dad, I will explain everything to you right now.', [(262, 'Папа, я тебе все объясню')], 'adapted'),
    ('barinov', 'Что ты мне можешь объяснить?', 'What can you possibly explain to me?', [(262, 'Что ты мне можешь объяснить?')], 'exact'),
    ('katya', 'Это просто шутка была!', 'It was just a joke!', [(263, 'Это шутка была')], 'adapted'),
    ('katya', 'Папа, что с тобой, Витя?', 'Dad, what is wrong with you, Vitya?', [(264, 'Папа, Витя?')], 'adapted'),
]
WALK = [
    (0, None, '\'Does Dad know about this?\' Emphasizing the dad during the talk, Katya reaches for the Russian word "papa" ("Dad") right at the heart of the line.'),
    (1, None, '\'And here is your dish, almost the same as your grandmother\'s!\' Pointing to the grandmothers to Katya, Barinov links the Russian words directly in the present with no word for "am", "is", or "are" needed.'),
    (2, None, '\'Thank you, but I am already full.\' The guest simply sends this word of thanks in front of Barinov using "spasibo" ("thank you") — the everyday word for "thank you", which grew out of the old blessing "spasi Bog" ("God save you").'),
    (3, None, '\'I beg you, at least smell it!\' Barinov proceeds firmly before the guest and leans on "ponyukhayte" ("smell", a form of "ponyukhat") to give the remark its edge.'),
    (4, None, '\'Be so kind, smell the dish.\' Mentioning the dish at once, Barinov lands on "ponyukhayte" ("smell", built on "ponyukhat") to keep the statement grounded.'),
    (5, None, "'My eyes, my eyes!' The guest continues lightly around Barinov, before Barinov can change the subject."),
    (6, None, '\'You are both simply crazy!\' Emphasizing how crazy the guest is in the exchange, Katya chooses "sumasshedshiye" ("crazy, insane", from the root "sumasshedshiy") so the guest hears the exact meaning.'),
    (7, None, "'Do not worry, I will buy you dark glasses.' Barinov weighs in wryly on the spot, so Katya knows he is not just making small talk."),
    (8, None, "'Dad, I will explain everything to you right now.' Katya reacts quietly without holding back, to clear the air between them once and for all."),
    (9, None, '\'What can you possibly explain to me?\' Barinov counters vividly at once and brings in "obyasnit" ("to explain") to make the meaning unmistakable.'),
    (10, None, '\'It was just a joke!\' Dwelling on a joke before Barinov, Katya uses the little word "prosto" ("simply, just") to make the point sound effortless.'),
    (11, None, "'Dad, what is wrong with you, Vitya?' Katya prompts calmly how Barinov expects that to work in practice."),
]
