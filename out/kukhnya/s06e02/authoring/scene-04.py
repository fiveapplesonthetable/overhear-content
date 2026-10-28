# Authoring module for kukhnya-s06e02-scene-04.
ID = 'kukhnya-s06e02-scene-04'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 2
SCENE = 4
TITLE = 'Маленькие порции и большие цены  (Tiny Portions and High Prices)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'nikita': 'Никита', 'senya': 'Сеня'}
SOURCE_NAME = 'Кухня (Kukhnya) S6.02'
SOURCE_FILE = 'sources/kukhnya/s06/e02.ru.srt'
INTRO = "While Senya and Fedya mock the tiny portions, restaurant director Nikita panics when he hears that each dish on Barinov's new menu costs between three and five thousand rubles."
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'Barinov also invites the entire staff to celebrate the launch of his new menu after their shift. See you next time!'
CLOSING = ('barinov', 'До свидания!')
STORY = [
    ('senya', 'Я не знаю, я ничего не понял.', 'I do not know, I did not understand anything.', [(48, 'Я не знаю, я ничего не понял')], 'exact'),
    ('senya', 'Шеф, а почему блюда такие маленькие?', 'Chef, why are the dishes so tiny?', [(49, 'Шеф, а что блюда такие')], 'adapted'),
    ('barinov', 'Шедевры вёдрами не подают.', 'Masterpieces are not served in buckets.', [(50, 'Шедевры')], 'adapted'),
    ('nikita', 'Виктор Петрович, а цены вы уже рассчитали?', 'Viktor Petrovich, have you already calculated the prices?', [(51, 'цены вы уже рассчитали?')], 'adapted'),
    ('barinov', 'Рассчитали, от трех до пяти тысяч за блюдо.', 'We calculated them, from three to five thousand per dish.', [(52, 'Рассчитали. От трех до пяти тысяч за блюдо')], 'exact'),
    ('nikita', 'Пять тысяч за блюдо?', 'Five thousand for a dish?', [(53, 'Пять тысяч за блюдо?')], 'exact'),
    ('nikita', 'Может, мы пока старое меню оставим?', 'Maybe we should keep the old menu for now?', [(54, 'мы пока старое меню оставим')], 'adapted'),
    ('barinov', 'Нет старого меню, есть только новое меню.', 'There is no old menu, there is only the new menu.', [(55, 'Нет старого меню. Есть только новое меню')], 'exact'),
    ('barinov', 'Тимур, давай сюда новое меню.', 'Timur, bring the new menu here.', [(56, 'Тимур. Да, совсем новое')], 'adapted'),
    ('senya', 'Даже воняет еще краской.', 'It even still smells of ink.', [(58, 'Даже воняет еще')], 'adapted'),
    ('barinov', 'Вы еще меня благодарить будете, когда мы звезду получим.', 'You will thank me yet when we get the star.', [(59, 'Да вы еще меня благодарить будете')], 'adapted'),
    ('barinov', 'Изучайте рецепты!', 'Study the recipes!', [(63, 'Изучайте рецепты')], 'exact'),
]
WALK = [
    (0, None, '\'I do not know, I did not understand anything.\' Senya cuts in sharply beside Barinov and uses "ponyal" ("understood", from "ponyat") to make the point stick.'),
    (1, None, '\'Chef, why are the dishes so tiny?\' Mentioning the dish beside Barinov, Senya links the Russian words directly in the present with no word for "am", "is", or "are" needed.'),
    (2, None, "'Masterpieces are not served in buckets.' Barinov cuts in frankly beside Senya, testing Senya's reaction in the middle of the exchange."),
    (3, None, '\'Viktor Petrovich, have you already calculated the prices?\' Underscoring the price with Barinov, Nikita centers the thought on "rasschitali" ("calculated", from "rasschitat") without wasting a word.'),
    (4, None, '\'We calculated them, from three to five thousand per dish.\' Discussing the thousand to Nikita, Barinov brings in "rasschitali" ("calculated", from "rasschitat") as the key Russian word here.'),
    (5, None, "'Five thousand for a dish?' Nikita inquires earnestly what Barinov is actually getting at here."),
    (6, None, '\'Maybe we should keep the old menu for now?\' Highlighting the old menu beside Barinov, Nikita lands on "staroye" ("old", built on "staryy") to keep the statement grounded.'),
    (7, None, '\'There is no old menu, there is only the new menu.\' Pointing to the new menu to Nikita, Barinov chooses "starogo" ("old", from the root "staryy") so Nikita hears the exact meaning.'),
    (8, None, "'Timur, bring the new menu here.' Barinov proceeds sharply in their talk, before Senya can change the subject."),
    (9, None, '\'It even still smells of ink.\' Mentioning the like with Barinov, Senya leans on "vonyayet" ("like") to give the whole sentence its punch.'),
    (10, None, "'You will thank me yet when we get the star.' Barinov weighs in wryly hearing Senya, testing Senya's reaction in the middle of the exchange."),
    (11, None, "'Study the recipes!' Barinov counters promptly without a pause, without trying to dress up how he really feels."),
]
