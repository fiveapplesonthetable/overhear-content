# Authoring module for kukhnya-s05e02-scene-17.
ID = 'kukhnya-s05e02-scene-17'
SHOW = 'kukhnya'
SEASON = 5
EPISODE = 2
SCENE = 17
TITLE = 'Месть лжеревизору  (Payback for the Fake Inspector)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'guest': 'Гость', 'mikhail': 'Михаил'}
SOURCE_NAME = 'Кухня (Kukhnya) S5.02'
SOURCE_FILE = 'sources/kukhnya/s05/e02.ru.srt'
INTRO = 'Convinced that the guest in room 313 is just a freeloader who exploited them for two days, Chef Barinov and Mikhail barge into his suite to force-feed him coffee and steaks. Listen to the confrontation.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "And that captures Barinov and Mikhail's disastrous revenge in room 313. Notice how Barinov calls the guest 'Khlestakov' and 'revizor' after Gogol's famous play 'The Government Inspector'. Until next time!"
CLOSING = ('guest', 'Увидимся!')
STORY = [
    ('barinov', 'А вот и наш дорогой гость.', 'And here is our dear guest.', [(211, 'мой гость')], 'adapted'),
    ('barinov', 'Мы вам горячий кофе принесли.', 'We brought you hot coffee.', [(212, 'Мы вам кофе принесли')], 'adapted'),
    ('mikhail', 'Пожалуйста, вот ваш лучший кофе.', 'Here you go, here is your finest coffee.', [(215, 'Пожалуйста, ваш кофе')], 'adapted'),
    ('guest', 'Я не понял, что здесь происходит?', 'I do not understand, what is going on here?', [(216, 'я не понял, что здесь происходит?')], 'verbatim'),
    ('guest', 'Вы что творите, вы чего?', 'What are you doing, what is with you?', [(217, 'Да! Вы чего?')], 'adapted'),
    ('guest', 'Вы что, совсем с ума сошли?', 'Have you completely lost your minds?', [(218, 'Вы что, с ума сошли?')], 'verbatim'),
    ('barinov', 'Пей давай свой вкусный кофе!', 'Drink up your delicious coffee!', [(218, 'Поешь')], 'adapted'),
    ('guest', 'Что вы себе здесь позволяете?', 'What are you allowing yourselves here?', [(219, 'Что себе')], 'adapted'),
    ('mikhail', 'Витя, дай ему немного дышать.', 'Vitya, let him breathe a little.', [(219, 'Дай ему дышать')], 'adapted'),
    ('mikhail', 'Подожди, дай ему спокойно дышать.', 'Wait, let him breathe calmly.', [(220, 'Дай ему дышать')], 'adapted'),
    ('barinov', 'А куда пропал весь кофе?', 'And where did all the coffee go?', [(221, 'А там все кофе, а?')], 'adapted'),
    ('barinov', 'Держи этого хитрого ревизора!', 'Hold that clever inspector!', [(222, 'Держи ревизора')], 'adapted'),
]
WALK = [
    (0, None, '\'And here is our dear guest.\' Underscoring how dear things are at once, Barinov links the Russian words directly in the present with no word for "am", "is", or "are" needed.'),
    (1, None, "'We brought you hot coffee.' Barinov speaks pointedly without a pause, making his position completely clear."),
    (2, None, '\'Here you go, here is your finest coffee.\' Mikhail simply speaks this courtesy word while facing Barinov using "pozhaluysta" ("please") — the all-purpose Russian politeness word that covers both "please" and "you\'re welcome".'),
    (3, None, '\'I do not understand, what is going on here?\' Holding firm openly around Mikhail, the guest puts the question word "chto" right at the start so Mikhail hears the focus immediately.'),
    (4, None, "'What are you doing, what is with you?' The guest wonders openly about what Barinov just brought up."),
    (5, None, '\'Have you completely lost your minds?\' Focusing on the mind beside Barinov, the guest brings in "sovsem" ("at all") to make the meaning unmistakable.'),
    (6, None, '\'Drink up your delicious coffee!\' Mentioning the coffee during the talk, Barinov starts with "davay" ("come on, let\'s") to invite the guest right into the action.'),
    (7, None, "'What are you allowing yourselves here?' The guest presses deadpan why things suddenly took this turn between them."),
    (8, None, '\'Vitya, let him breathe a little.\' Mikhail responds candidly in front of the guest and uses "nemnogo" ("a bit") to carry the main weight of the thought.'),
    (9, None, '\'Wait, let him breathe calmly.\' Mikhail continues sharply beside Barinov and chooses "podozhdi" ("wait", from the root "podozhdat") so Barinov hears the exact meaning.'),
    (10, None, "'And where did all the coffee go?' Barinov presses earnestly why things suddenly took this turn between them."),
    (11, None, '\'Hold that clever inspector!\' Highlighting the inspector in the exchange, Barinov centers the thought on "khitrogo" ("cunning, sly", from "khitryy") without wasting a word.'),
]
