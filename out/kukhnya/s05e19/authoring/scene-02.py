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
    (0, None, '\'Senya, have you seen my hat today?\' Checking whether Kostya seen her hat today cuts straight through the tension between Katya and Kostya. Using the informal "you" shows how direct and unfiltered their kitchen relationship is.'),
    (1, None, "'If you want to find the hat, follow the clues.' Because if Kostya wants to find the hat follow the clues, Katya treats the matter as settled."),
    (2, None, "'The first clue will perk you up early in the morning.' Explaining that the first clue will perk Kostya up early in the morning lays the cards on the table for Kostya."),
    (3, None, "'Okay, we need diapers, baby powder, and a car seat.' With the shift and coffee in play, Max keeps this short reply brisk and direct."),
    (4, None, '\'Vika, is it not too early to buy a seat?\' Asking whether it not too early to buy a seat cuts straight through the tension between Max and Katya. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (5, None, "'Alright, do not worry, I will buy everything today.' Pointing out that Alright do not worry he will buy everything today gives Katya a sobering reality check."),
    (6, None, '\'Kostya, how much money goes into supporting a child?\' Asking whether how much money goes into supporting a child puts Katya right on the defensive. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (7, None, "'Honestly speaking, absolutely everything goes to the child.' Realizing that speaking absolutely everything goes to the child changes how Kostya handles the situation."),
    (8, None, "'And how do I support a daughter on a cook's salary?' Wondering how he supports a daughter on a cook salary cuts straight through the tension between Max and Katya."),
    (9, None, '\'Well, that depends on what exactly you cook.\' Even though that depends on what exactly Katya cooks, Kostya keeps a steady face in front of Katya. Russian drops "is" in the present, setting the two halves of the thought side by side.'),
    (10, None, "'I urgently need to earn more money.' With the work and coffee in play, Max keeps this short reply brisk and direct. Russian packs the whole idea of what is allowed or needed into one impersonal word at the front."),
    (11, None, "'Then think about how to get a raise.' Telling Katya to think about how to get a raise moves the conversation forward without extra drama."),
]
