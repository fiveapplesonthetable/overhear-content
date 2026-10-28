# Authoring module for kukhnya-s05e19-scene-02.
ID = 'kukhnya-s05e19-scene-02'
SHOW = 'kukhnya'
SEASON = 5
EPISODE = 19
SCENE = 2
TITLE = 'Первая подсказка и расходы на ребёнка  (The First Clue and Baby Expenses)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'katya': 'Катя', 'kostya': 'Костя', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S5.19'
SOURCE_FILE = 'sources/kukhnya/s05/e19.ru.srt'
INTRO = 'Katya notices her favorite hat is missing and finds a mysterious note telling her to follow clues starting at the coffee machine. Meanwhile, Max receives a long shopping list from Vika.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'Kostya suggests a practical way for Max to earn a promotion from Chef Barinov. See you next time!'
CLOSING = ('max', 'До завтра!')
STORY = [
    ('katya', 'Сеня, ты мою шляпку сегодня не видел?', 'Senya, have you seen my hat today?', [(29, 'ты мою шляпку не видел')], 'adapted'),
    ('katya', 'Хочешь найти шляпку, тогда следуй подсказкам.', 'If you want to find the hat, follow the clues.', [(31, 'Хочешь найти шляпку, следуй подсказкам')], 'adapted'),
    ('katya', 'Первая подсказка взбодрит тебя рано с утра.', 'The first clue will perk you up early in the morning.', [(32, 'Первая подсказка взбодрит тебя с утра')], 'adapted'),
    ('max', 'Так, нужны подгузники, присыпка и детское кресло.', 'Okay, we need diapers, baby powder, and a car seat.', [(33, 'Так, подгузники'), (34, 'Присыпка'), (35, 'кресло')], 'adapted'),
    ('max', 'Вика, а кресло покупать ещё не рано?', 'Vika, is it not too early to buy a seat?', [(36, 'Вика, не рано')], 'adapted'),
    ('max', 'Ладно, не волнуйся, я сегодня всё куплю.', 'Alright, do not worry, I will buy everything today.', [(37, 'Ладно, ладно, не волнуйся, все куплю')], 'adapted'),
    ('max', 'Костя, сколько денег уходит на содержание ребёнка?', 'Kostya, how much money goes into supporting a child?', [(39, 'сколько вообще денег уходит на содержание ребенка')], 'adapted'),
    ('kostya', 'Честно говоря, на ребёнка уходит абсолютно всё.', 'Honestly speaking, absolutely everything goes to the child.', [(40, 'Уходит все')], 'adapted'),
    ('max', 'И как содержать дочку на зарплату повара?', "And how do I support a daughter on a cook's salary?", [(41, 'И как содержать дочку на зарплату повара')], 'adapted'),
    ('kostya', 'Ну, это смотря что именно варить.', 'Well, that depends on what exactly you cook.', [(42, 'Смотря что варить')], 'adapted'),
    ('max', 'Мне срочно нужно больше зарабатывать.', 'I urgently need to earn more money.', [(39, 'сколько вообще денег')], 'adapted'),
    ('kostya', 'Тогда подумай, как получить прибавку.', 'Then think about how to get a raise.', [(40, 'Уходит все')], 'adapted'),
]
WALK = [
    (0, None, "'Senya, have you seen my hat today?' Opening up firmly to Max, Katya keeps normal statement word order here, turning the line into a question for Max purely through rising pitch."),
    (1, None, "'If you want to find the hat, follow the clues.' Katya continues openly in their talk, steering the talk right where she wants it."),
    (2, None, '\'The first clue will perk you up early in the morning.\' Discussing the first clue in this beat, Katya centers the remark on "podskazka" ("clue") without any extra fuss.'),
    (3, None, '\'Okay, we need diapers, baby powder, and a car seat.\' Highlighting the diapers right here, Max uses "podguzniki" ("diapers", from "podguznik") to make the point stick.'),
    (4, None, "'Vika, is it not too early to buy a seat?' Max checks candidly where this conversation is heading next."),
    (5, None, '\'Alright, do not worry, I will buy everything today.\' Max replies sharply in the exchange and centers the thought on "volnuysya" ("worry", from "volnovatsya") without wasting a word.'),
    (6, None, '\'Kostya, how much money goes into supporting a child?\' Addressing the upkeep in this beat, Max puts the question word "skolko" right at the start so Kostya hears the focus immediately.'),
    (7, None, "'Honestly speaking, absolutely everything goes to the child.' Kostya replies earnestly around Max, so Max knows he is not just making small talk."),
    (8, None, '\'And how do I support a daughter on a cook\'s salary?\' Bringing up the salary beside Kostya, Max centers the thought on "zarplatu" ("salary", from "zarplata") without wasting a word.'),
    (9, None, '\'Well, that depends on what exactly you cook.\' Kostya weighs in openly with Max and brings in "smotrya" ("depending on", from "smotret") as the key Russian word here.'),
    (10, None, "'I urgently need to earn more money.' Max proceeds evenly beside Kostya, letting the remark speak for itself."),
    (11, None, '\'Then think about how to get a raise.\' Addressing a raise beside Max, Kostya leans on "pribavku" ("pay raise", a form of "pribavka") to give the remark its edge.'),
]
