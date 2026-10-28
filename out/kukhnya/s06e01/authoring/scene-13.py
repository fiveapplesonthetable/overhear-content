# Authoring module for kukhnya-s06e01-scene-13.
ID = 'kukhnya-s06e01-scene-13'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 1
SCENE = 13
TITLE = 'Катя заступилась за Дениса  (Katya Stood Up for Denis)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'denis': 'Денис', 'senya': 'Сеня'}
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
    ('denis', 'Какое возвращение?', 'What return?', [(238, 'Какое возвращение?')], 'exact'),
    ('denis', 'Я тут не задержусь.', 'I will not stay here long.', [(238, 'Я тут не задержусь')], 'exact'),
    ('senya', 'А я думал, ты навсегда вернёшься.', 'And I thought you would come back for good.', [(239, 'что ты навсегда вернёшься')], 'adapted'),
    ('senya', 'Катя из-за тебя поговорила с мамой.', 'Katya talked to her mom because of you.', [(239, 'Катя из-за тебя поговорила')], 'adapted'),
    ('senya', 'Да, она просила за тебя.', 'Yes, she pleaded for you.', [(240, 'Да, она просила за тебя')], 'exact'),
    ('senya', 'Сказала, не лезь в мою личную жизнь.', 'She said, do not meddle in my personal life.', [(241, 'не лезь в мою личную жизнь')], 'adapted'),
    ('senya', 'Она тебя любит еще, я тебе точно говорю.', 'She still loves you, I am telling you for sure.', [(242, 'Она тебя любит еще, я тебе точно говорю')], 'exact'),
    ('denis', 'Не знаю, посмотрим.', 'I do not know, we will see.', [(238, 'Я тут не задержусь')], 'adapted'),
]
WALK = [
    (0, None, "'I have had enough.' Barinov mentions that he has had enough so Denis sees what is at stake."),
    (1, None, '\'I will not do anything more.\' Admitting that he will not do anything shows Barinov being honest for a change. Russian stacks "never" or "nothing" together with "not", doubling the refusal for extra weight.'),
    (2, None, "'I will tell Eleonora everything myself right now.' Saying that he will tell Eleonora everything himself right now is how Barinov sets the tone with Denis."),
    (3, None, "'Let's celebrate your return, Denis.' Explaining that they should celebrate Barinov's return lays the cards on the table for Barinov."),
    (4, None, '\'What return?\' With the truth and wedding hanging in the air, Denis puts Barinov on the spot. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (5, None, "'I will not stay here long.' Saying that he will not stay here long is how Denis sets the tone with Barinov."),
    (6, None, "'And I thought you would come back for good.' Since he thought Barinov would come back for good, Senya does not waste words on excuses."),
    (7, None, '\'Katya talked to her mom because of you.\' Mentioning that Katya talked to her because of Barinov moves the talk in a new direction. Using the informal "you" shows how direct and unfiltered their kitchen relationship is.'),
    (8, None, '\'Yes, she pleaded for you.\' Around the room and wedding, Senya sets a calm, everyday tone with Barinov. Speaking with the close, informal "you" strips away any polite distance between them.'),
    (9, None, "'She said, do not meddle in my personal life.' Because she said do not meddle in his personal life, Senya treats the matter as settled."),
    (10, None, '\'She still loves you, I am telling you for sure.\' Explaining that she still loves Barinov he is telling Barinov for sure lays the cards on the table for Barinov. Speaking with the close, informal "you" strips away any polite distance between them.'),
    (11, None, "'I do not know, we will see.' Because he does not know they will see, Denis treats the matter as settled."),
]
