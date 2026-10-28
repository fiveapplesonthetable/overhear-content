# Authoring module for kukhnya-s05e02-scene-05.
ID = 'kukhnya-s05e02-scene-05'
SHOW = 'kukhnya'
SEASON = 5
EPISODE = 2
SCENE = 5
TITLE = "Строгая речь Элеоноры Андреевны  (Eleonora Andreevna's Strict Speech)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'eleonora': 'Элеонора', 'senya': 'Сеня'}
SOURCE_NAME = 'Кухня (Kukhnya) S5.02'
SOURCE_FILE = 'sources/kukhnya/s05/e02.ru.srt'
INTRO = "Addressing the assembled staff in the hotel lobby, Eleonora Andreevna calls yesterday's opening in front of the Prefect a complete failure and demands to know why Chef Barinov is absent. Listen to her speech."
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "And that concludes Eleonora Andreevna's first staff meeting. Notice how 'discipline and once again discipline' sets her no-nonsense tone for the season. Until next time!"
CLOSING = ('eleonora', 'Всего хорошего!')
STORY = [
    ('eleonora', 'Вчерашнее открытие — это полный провал.', "Yesterday's grand opening was a total failure.", [(43, 'Вчерашнее открытие — это полный провал')], 'verbatim'),
    ('eleonora', 'Это случилось при самом префекте.', 'This happened in front of the prefect himself.', [(44, 'префекта')], 'adapted'),
    ('eleonora', 'Я не буду это терпеть.', 'I am not going to tolerate this.', [(46, 'я не')], 'adapted'),
    ('senya', 'Какая строгая у нас хозяйка.', 'What a strict owner we have.', [(47, 'у нас хозяйка')], 'adapted'),
    ('eleonora', 'Это касается здесь каждого.', 'This concerns everyone here.', [(48, 'Это касается всех и каждого')], 'adapted'),
    ('eleonora', 'Главное в отеле — это дисциплина.', 'The main thing in a hotel is discipline.', [(49, 'Дисциплина')], 'adapted'),
    ('eleonora', 'Дисциплина и ещё раз дисциплина.', 'Discipline and once again discipline.', [(51, 'Дисциплина. Еще раз дисциплина')], 'verbatim'),
    ('eleonora', 'Надеюсь, мы избежим таких разговоров.', 'I hope we will avoid such conversations.', [(52, 'мы избежим'), (52, 'разговоров')], 'adapted'),
    ('eleonora', 'А где сейчас ваш шеф?', 'And where is your head chef right now?', [(53, 'Где шеф')], 'adapted'),
    ('barinov', 'Он очень перед вами извинялся.', 'He apologized to you profusely.', [(54, 'Он очень извинялся')], 'adapted'),
    ('barinov', 'Он решает проблемы с поставщиками.', 'He is solving problems with suppliers.', [(55, 'Решает какие-то проблемы с поставщиками')], 'adapted'),
    ('senya', 'Где же сейчас наш шеф?', 'Where is our chef right now, though?', [(56, 'Ты')], 'adapted'),
]
WALK = [
    (0, None, "'Yesterday's grand opening was a total failure.' Eleonora jumps in lightly toward Barinov, steering the talk right where she wants it."),
    (1, None, "'This happened in front of the prefect himself.' Eleonora responds dryly beside Senya, saying out loud what both of them already know."),
    (2, None, '\'I am not going to tolerate this.\' Eleonora underscores this clear expression in reply: "terpet" means "to hold on", and it carries the main weight of what Eleonora is saying.'),
    (3, None, '\'What a strict owner we have.\' Senya states that remark facing Eleonora: the phrase "u nas" literally means "by us" or "at our place", the standard Russian way to talk about what a group or couple shares.'),
    (4, None, "'This concerns everyone here.' Eleonora responds earnestly toward Barinov, bringing things back to earth after the buildup."),
    (5, None, '\'The main thing in a hotel is discipline.\' Eleonora colors one key touch with Senya: "distsiplina" means "discipline", and it carries the main weight of what Eleonora is saying.'),
    (6, None, "'Discipline and once again discipline.' Eleonora speaks up promptly without any doubt, bringing things back to earth after the buildup."),
    (7, None, "'I hope we will avoid such conversations.' Eleonora pushes back at once without a pause, making her position completely clear."),
    (8, None, '\'And where is your head chef right now?\' Eleonora chooses this sharp detail for Barinov: "seychas" means "now", and it carries the main weight of what Eleonora is saying.'),
    (9, None, '\'He apologized to you profusely.\' Barinov sends the reaction with candor: the "-sya" ending on "izvinyalsya" ("apologized") turns the action inward or makes it happen between people naturally.'),
    (10, None, "'He is solving problems with suppliers.' Barinov fires back firmly on the spot, keeping the focus on what actually matters here."),
    (11, None, '\'Where is our chef right now, though?\' Senya picks one memorable term at once: "seychas" means "now", and it carries the main weight of what Senya is saying.'),
]
