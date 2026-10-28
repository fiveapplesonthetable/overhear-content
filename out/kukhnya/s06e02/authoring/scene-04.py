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
    (0, None, "'I do not know, I did not understand anything.' Around the conversation and menu, Senya sets a calm, everyday tone with Barinov."),
    (1, None, '\'Chef, why are the dishes so tiny?\' Wondering why the dishes so tiny are cuts straight through the tension between Senya and Barinov. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (2, None, "'Masterpieces are not served in buckets.' Realizing that masterpieces are not served in buckets changes how Barinov handles the situation."),
    (3, None, "'Viktor Petrovich, have you already calculated the prices?' Here asking whether Barinov already calculated the prices shows Nikita looking for the real truth."),
    (4, None, "'We calculated them, from three to five thousand per dish.' Between the conversation and the menu, Barinov gives Nikita a quick, grounded response."),
    (5, None, '\'Five thousand for a dish?\' With the dish and conversation hanging in the air, Nikita puts Barinov on the spot. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (6, None, "'Maybe we should keep the old menu for now?' Questioning whether maybe they should keep the old menu for now is how Nikita tests Barinov's story."),
    (7, None, "'There is no old menu, there is only the new menu.' Once there is no old menu there is only the new menu, Barinov can finally tell Nikita what he means."),
    (8, None, '\'Timur, bring the new menu here.\' Telling Nikita to bring the new menu here is how Barinov lays out the situation for Nikita. Starting with "davay" is the everyday Russian way to say "come on, let us do this".'),
    (9, None, "'It even still smells of ink.' With the work and menu in play, Senya keeps this short reply brisk and direct."),
    (10, None, '\'You will thank me yet when we get the star.\' Since Nikita will thank him yet when they get the star, Barinov does not waste words on excuses. Even in the middle of the drama, he keeps the polite plural "you" that workplace Russian expects.'),
    (11, None, "'Study the recipes!' Once Nikita should study the recipes, Barinov makes sure Nikita hears every word. Russian puts the key word right up front so his emotion lands on the first beat."),
]
