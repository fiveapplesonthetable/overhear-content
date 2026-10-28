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
    (0, None, "'Senya, have you seen my hat today?' Katya shapes that point around Kostya: Russian keeps the exact word order of a normal statement here, turning it into a question for Kostya purely through rising pitch at the end."),
    (1, None, "'If you want to find the hat, follow the clues.' Katya pushes back openly without holding back, before Max can change the subject."),
    (2, None, '\'The first clue will perk you up early in the morning.\' Katya spotlights this telling detail toward Kostya: "podskazka" means "clue", and it carries the main weight of what Katya is saying.'),
    (3, None, "'Okay, we need diapers, baby powder, and a car seat.' Max speaks up decisively with a smile, before Kostya can change the subject."),
    (4, None, "'Vika, is it not too early to buy a seat?' Max checks candidly before Katya can change the subject."),
    (5, None, '\'Alright, do not worry, I will buy everything today.\' Max anchors one pointed choice right here: "volnuysya" means "worry" (from "volnovatsya"), giving the line its exact edge.'),
    (6, None, '\'Kostya, how much money goes into supporting a child?\' Max lays out that point around Katya: putting the question word "skolko" right at the front of the line lets Katya hear the point of the question on the very first beat.'),
    (7, None, "'Honestly speaking, absolutely everything goes to the child.' Kostya jumps in earnestly beside Max, shifting the whole mood of the room in a single beat."),
    (8, None, '\'And how do I support a daughter on a cook\'s salary?\' Max reaches for this sharp piece toward Katya: "zarplatu" means "salary" (from "zarplata"), giving the line its exact edge.'),
    (9, None, "'Well, that depends on what exactly you cook.' Kostya counters right away with a sigh, to clear the air between them once and for all."),
    (10, None, "'I urgently need to earn more money.' Max speaks evenly in their talk, without trying to dress up how he really feels."),
    (11, None, '\'Then think about how to get a raise.\' Kostya spotlights this sharp expression for Max: "pribavku" means "pay raise" (from "pribavka"), giving the line its exact edge.'),
]
