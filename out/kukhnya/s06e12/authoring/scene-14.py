# Authoring module for kukhnya-s06e12-scene-14.
ID = 'kukhnya-s06e12-scene-14'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 12
SCENE = 14
TITLE = 'Слухи на кухне и допрос гостя  (Kitchen Rumors and Questioning the Guest)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'nastya': 'Настя', 'nikita': 'Никита'}
SOURCE_NAME = 'Кухня (Kukhnya) S6.12'
SOURCE_FILE = 'sources/kukhnya/s06/e12.ru.srt'
INTRO = 'Nikita pulls Denis aside and tells him that Katya looked jealous when she heard Denis and Sveta were getting married. In the kitchen, Nastya and Kostya skip the staff pasta to save room for their anniversary dinner, while Barinov corners the bookmaker for match results.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "Believing the truth serum is working on the bookmaker, Barinov eagerly writes down the fake tips, while Gulya has a heart-to-heart with Lyova's mother at the clinic. See you next time!"
CLOSING = ('barinov', 'Увидимся!')
STORY = [
    ('nikita', 'Слушай, я по секрету узнал, что вы со Светой женитесь.', 'Listen, I found out in secret that you and Sveta are getting married.', [(222, 'Слушай, я так по секрету узнала, что Денис со Светой женится')], 'adapted'),
    ('nikita', 'Но это ещё далеко не самая лучшая новость.', 'But that is far from the best news yet.', [(223, 'Это еще не самая лучшая новость')], 'adapted'),
    ('nikita', 'Ты знаешь, как на эту новость Катя отреагировала?', 'Do you know how Katya reacted to this news?', [(224, 'Знаешь, как на это Катя отреагировала')], 'adapted'),
    ('nikita', 'Она сказала, что свадьба — это круто, будто завидовала.', 'She said a wedding is cool, as if she were envious.', [(225, 'свадьба – это круто'), (226, 'будто бы завидовала')], 'adapted'),
    ('nastya', 'Ребята, а вы почему макароны по-флотски не едите?', 'Guys, why are you not eating the navy-style pasta?', [(228, 'макароны по-флотски')], 'adapted'),
    ('nikita', 'Нет, мы с Костей сегодня обедать не будем.', 'No, Kostya and I will not have lunch today.', [(229, 'мы с Костей не будем')], 'adapted'),
    ('nastya', 'Ведь у нас сегодня вечером годовщина нашей свадьбы.', 'Because tonight is our wedding anniversary.', [(229, 'у нас годовщина свадьбы сегодня')], 'adapted'),
    ('nastya', 'Если сейчас поедим, то романтический ужин не поместится.', 'If we eat now, there will be no room for our romantic dinner.', [(230, 'то романтический ужин не поместится')], 'adapted'),
    ('nikita', 'А я заберу все остатки макарон себе домой.', 'And I will take all the leftover pasta home for myself.', [(231, 'потому что я все остатки заберу'), (232, 'Домой')], 'adapted'),
    ('barinov', 'Ну как суп, скажите, вам всё сегодня понравилось?', 'Well how was the soup, tell me, did you like everything today?', [(233, 'Ну как? Вам все понравилось')], 'adapted'),
    ('nastya', 'Да, большое спасибо, суп был очень вкусный.', 'Yes, thank you very much, the soup was very tasty.', [(234, 'Да, спасибо')], 'adapted'),
    ('barinov', 'Тогда скажите мне результаты всех договорных матчей!', 'Then tell me the results of all the fixed matches!', [(235, 'Ну тогда скажите мне результаты всех договорных матчей, которые вы знаете')], 'adapted'),
]
WALK = [
    (0, None, "'Listen, I found out in secret that you and Sveta are getting married.' Touching on the secret with a sigh, Nikita speaks plainly so Nastya gets the message at once."),
    (1, None, "'But that is far from the best news yet.' Nikita cuts in at once without a pause, bringing things back to earth after the buildup."),
    (2, None, '\'Do you know how Katya reacted to this news?\' Highlighting the news beside Nastya, Nikita lands on "otreagirovala" ("reacted", built on "otreagirovat") to keep the statement grounded.'),
    (3, None, '\'She said a wedding is cool, as if she were envious.\' Touching on a wedding in front of Nastya, Nikita reaches for the Russian word "zavidovala" ("to envy", built from "zavidovat") right at the center of the line.'),
    (4, None, "'Guys, why are you not eating the navy-style pasta?' Nastya tests straight out to see how Nikita will answer on the spot."),
    (5, None, '\'No, Kostya and I will not have lunch today.\' Nikita proceeds boldly right here and puts the emphasis on "segodnya" ("today") in the middle of the talk.'),
    (6, None, '\'Because tonight is our wedding anniversary.\' Turning to the anniversary to Nikita, Nastya reaches for "u nas" ("by us, at our place") to talk about what they share.'),
    (7, None, "'If we eat now, there will be no room for our romantic dinner.' Nastya opens up right away with a sigh, leaving no doubt about where she stands."),
    (8, None, '\'And I will take all the leftover pasta home for myself.\' Mentioning the leftovers with Nastya, Nikita chooses "ostatki" ("leftovers", from the root "ostatok") so Nastya hears the exact meaning.'),
    (9, None, '\'Well how was the soup, tell me, did you like everything today?\' Dwelling on the soup before Nastya, Barinov puts the question word "kak" right at the start so Nastya hears the focus immediately.'),
    (10, None, "'Yes, thank you very much, the soup was very tasty.' Nastya reacts dryly during the talk, refusing to let the moment slip past."),
    (11, None, '\'Then tell me the results of all the fixed matches!\' Addressing the results in this beat, Barinov brings in "dogovornykh" ("fixed", from "dogovornoy") as the key Russian word here.'),
]
