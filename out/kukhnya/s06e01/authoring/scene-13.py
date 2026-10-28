# Authoring module for kukhnya-s06e01-scene-13.
ID = 'kukhnya-s06e01-scene-13'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 1
SCENE = 13
TITLE = 'Катя заступилась за Дениса  (Katya Stood Up for Denis)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'katya': 'Катя', 'senya': 'Сеня'}
SOURCE_NAME = 'Кухня (Kukhnya) S6.01'
SOURCE_FILE = 'sources/kukhnya/s06/e01.ru.srt'
INTRO = 'In the kitchen, Chef Barinov loses his patience over the wedding cookies, while Senya and Fedya welcome Denis back and tell him how fiercely Katya defended him in front of her mother.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'Hearing that Katya fought for him gives Denis hope, while Barinov heads into the banquet hall to speak with Eleonora. Until next time!'
CLOSING = ('senya', 'До завтра!')
STORY = [
    ('barinov', 'С меня хватит.', 'I have had enough.', [(231, 'С меня хватит')], 'exact'),
    ('barinov', 'Я больше ничего делать не буду.', 'I will not do anything more.', [(231, 'Я больше пальцем о палец не ударю')], 'adapted'),
    ('barinov', 'Я сам сейчас всё скажу Элеоноре.', 'I will tell Eleonora everything myself right now.', [(235, 'сам сейчас всё скажу')], 'adapted'),
    ('senya', 'Давай отметим твоё возвращение, Денис.', "Let's celebrate your return, Denis.", [(237, 'Давай отметим твоё возвращение')], 'adapted'),
    ('katya', 'Какое возвращение?', 'What return?', [(238, 'Какое возвращение?')], 'exact'),
    ('katya', 'Я тут не задержусь.', 'I will not stay here long.', [(238, 'Я тут не задержусь')], 'exact'),
    ('senya', 'А я думал, ты навсегда вернёшься.', 'And I thought you would come back for good.', [(239, 'что ты навсегда вернёшься')], 'adapted'),
    ('senya', 'Катя из-за тебя поговорила с мамой.', 'Katya talked to her mom because of you.', [(239, 'Катя из-за тебя поговорила')], 'adapted'),
    ('senya', 'Да, она просила за тебя.', 'Yes, she pleaded for you.', [(240, 'Да, она просила за тебя')], 'exact'),
    ('katya', 'Сказала, не лезь в мою личную жизнь.', 'She said, do not meddle in my personal life.', [(241, 'не лезь в мою личную жизнь')], 'adapted'),
    ('senya', 'Она тебя любит еще, я тебе точно говорю.', 'She still loves you, I am telling you for sure.', [(242, 'Она тебя любит еще, я тебе точно говорю')], 'exact'),
    ('katya', 'Не знаю, посмотрим.', 'I do not know, we will see.', [(238, 'Я тут не задержусь')], 'adapted'),
]
WALK = [
    (0, None, '\'I have had enough.\' Barinov cuts in decisively on the spot and puts the emphasis on "khvatit" ("enough") in the middle of the talk.'),
    (1, None, '\'I will not do anything more.\' Looking over openly around Senya, Barinov pairs the negative word with "ne" ("not"), since Russian naturally doubles its negatives for emphasis.'),
    (2, None, "'I will tell Eleonora everything myself right now.' Barinov opens up lightly during the talk, leaving no doubt about where he stands."),
    (3, None, '\'Let\'s celebrate your return, Denis.\' Focusing on the return right here, Senya chooses "vozvrashcheniye" ("return") so Barinov gets the point right away.'),
    (4, None, "'What return?' Checking on the return right here, Katya keeps normal statement word order here, turning the line into a question for Senya purely through rising pitch."),
    (5, None, "'I will not stay here long.' Katya weighs in right away without any doubt, without trying to dress up how she really feels."),
    (6, None, '\'And I thought you would come back for good.\' Senya replies plainly around Katya and chooses "vernyoshsya" ("you come back", from the root "vernutsya") so Katya hears the exact meaning.'),
    (7, None, "'Katya talked to her mom because of you.' Senya proceeds plainly on the spot, keeping the focus on what actually matters here."),
    (8, None, "'Yes, she pleaded for you.' Senya opens up pointedly hearing Katya, making his position completely clear."),
    (9, None, '\'She said, do not meddle in my personal life.\' Mentioning the life in this beat, Katya lands on "lichnuyu" ("personal", built on "lichnyy") to keep the statement grounded.'),
    (10, None, "'She still loves you, I am telling you for sure.' Senya chimes in quietly in their talk, grounding the moment in plain reality."),
    (11, None, "'I do not know, we will see.' Katya replies evenly on the spot, leaving no doubt about where she stands."),
]
